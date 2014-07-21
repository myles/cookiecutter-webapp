define ['backbone', 'module'], (Backbone, module) ->

  # Extends Backbone.Collection with ETag and If-None-Match header support
  # An ETag is added to the outgoing headers if `etag` is defined
  # `etag` is set by from the response headers for If-None-Match on completion
  # The `options` object has the final word, i.e. it has the final say
  # See: http://jsfiddle.net/Ewg7q/1/

  class Collection extends Backbone.Collection

    initialize: (@etag) ->
      super

    fetch: (options) ->
      setRequestHeader = (xhr, settings) =>
        xhr.setRequestHeader('If-None-Match', @etag) if this?.etag
        xhr.setRequestHeader('If-None-Match', 'bambam')
        xhr.setRequestHeader('If-Modified', 'bambam')
      setEtagFromResponse = (xhr, text_status) =>
        @etag = xhr.getResponseHeader 'ETag'
      super
        beforeSend: (xhr, settings) ->
          setRequestHeader xhr, settings
          options?.beforeSend xhr, settings
        success: (resp) ->
          console.log "fetch success called"
        complete: (xhr, text_status) ->
          console.log "fetch completed"
          setEtagFromResponse xhr, text_status
          options?.complete xhr, text_status
        ifModified: true

    _reset: ->
      super
      @etag = undefined

  module.exports = Collection
