define ['backbone', 'module'], (Backbone, module) ->

  BaseModel = Backbone.Model.extend
    fetch: (options) ->
      setHeader = (jqXHR, settings) =>
        jqXHR.setRequestHeader('if-non-match', @etag) if this?.etag
        console.log "tried to set etag"
      setEtag = (jqXHR, textStatus) =>
        @etag = jqXHR.getResponseHeader 'ETag'
        console.log "tried to get etag"
      console.log "in fetch"
      Backbone.Model.prototype.fetch.call(this, {
        beforeSend: (jqXHR, settings) ->
          @setHeader jqXHR, settings
          @options?.beforeSend jqXHR, settings
        complete: (jqXHR, textStatus) ->
          @setEtag jqXHR, textStatus
          @options?.complete jqXHR, textStatus
      })

  module.exports = BaseModel
