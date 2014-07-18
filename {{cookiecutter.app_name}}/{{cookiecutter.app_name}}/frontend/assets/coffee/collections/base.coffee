define ['backbone', 'module'], (Backbone, module) ->

  BaseCollection = Backbone.Collection.extend
    initialize: (@etag) ->
    fetch: (options) ->
      setHeader = (jqXHR, settings) =>
        jqXHR.setRequestHeader('If-None-Match', @etag) if this?.etag
      setEtag = (jqXHR, textStatus) =>
        @etag = jqXHR.getResponseHeader 'ETag'
      Backbone.Collection.prototype.fetch.call(this, {
        beforeSend: (jqXHR, settings) ->
          setHeader jqXHR, settings
          options?.beforeSend jqXHR, settings
        complete: (jqXHR, textStatus) ->
          setEtag jqXHR, textStatus
          options?.complete jqXHR, textStatus
      })

  module.exports = BaseCollection
