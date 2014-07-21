define ['module'], (module) ->

  BackboneMixin =

    componentDidMount: ->
      for collection in @getBackboneCollections()
        collection.on('add remove change', @forceUpdate.bind(@, null))

    componentWillUnmount: ->
      for collection in @getBackboneCollections()
        collection.off(null, null, @)

  module.exports = BackboneMixin
