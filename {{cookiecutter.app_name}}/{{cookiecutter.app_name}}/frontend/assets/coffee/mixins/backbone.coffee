define ['module'], (module) ->

  BackboneMixin =

    componentDidMount: ->
      for collection in @getBackboneCollections()
        collection.on('add remove change', @forceUpdate.bind(@, null))

    componentWillUnmount: ->
      for collection in @getBackboneCollections()
        collection.off null, null, @

    getBackboneCollections: ->
      console.log "override this function in the mixed object"
      undefined

  module.exports = BackboneMixin
