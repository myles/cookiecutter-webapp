require ['backbone', 'module'], (Backbone, module) ->


  token = undefined

  settings =
    url: '/auth/jwt/token'

  updateJWT = (xhr, args..., on_error) ->
    retry = @
    retry.error = on_error
    $.ajax settings.url,
      type: 'POST'
      data: {}
      dataType: 'json'
      beforeSend: (xhr) ->
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.setRequestHeader("Accept", "application/json")
      success: (data, textStatus, jqXHR) ->
        console.log "update_jwt token succeeded"
        token = data?.token
        $.ajax(retry)
      error: (jqXHR, textStatus, errorThrown, on_error) ->
        console.log "update_jwt error: #{textStatus}"
        console.log jqXHR
        console.log errorThrown
        on_error?(xhr, args...)

  extender = (options) ->
    options ?= {}

    # beforeSend - Set JWT Bearer token
    beforeSend = options?.beforeSend
    options.beforeSend = (xhr, args...) ->
      xhr.setRequestHeader("Authorization", "Bearer #{token}") if token
      beforeSend?(xhr, args...)

    # error - override ajax error handler; try to update the jwt token
    # if we see a 400 or 401 error from the server
    error = options?.error
    options.error = (args...) ->
      args.push error
      updateJWT.apply(@, args...)

    return options

  Backbone.ajax = (args...) ->
    args[0] = extender(args[0])
    Backbone.$.ajax.apply(Backbone.$, args)

  console.log "backbone-ajax-jwt initialized"

