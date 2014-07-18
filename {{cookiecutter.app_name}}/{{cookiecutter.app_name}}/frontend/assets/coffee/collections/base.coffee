define ['backbone', 'module'], (Backbone, module) ->

  # Extends Backbone.Collection with ETag and If-None-Match header support
  # An ETag is added to the outgoing headers if `etag` is defined
  # `etag` is set by from the response headers for If-None-Match on completion
  # The `options` object has the final word, i.e. it has the final say
  # See: http://jsfiddle.net/Ewg7q/1/

  class Collection extends Backbone.Collection
    initialize: (@etag) ->
    fetch: (options) ->
      setRequestHeader = (xhr, settings) =>
        xhr.setRequestHeader('If-None-Match', @etag) if this?.etag
      setEtagFromResponse = (xhr, text_status) =>
        @etag = xhr.getResponseHeader 'ETag'
      super
        beforeSend: (xhr, settings) ->
          setRequestHeader xhr, settings
          options?.beforeSend xhr, settings
        complete: (xhr, text_status) ->
          setEtagFromResponse xhr, text_status
          options?.complete xhr, text_status

  module.exports = Collection
