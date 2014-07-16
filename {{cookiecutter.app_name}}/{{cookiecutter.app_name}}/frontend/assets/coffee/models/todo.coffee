define ['backbone', 'module'], (Backbone, module) ->

  Todo = Backbone.Model.extend

    default:
      title: ''
      completed: false

    toggle: ->
      @.save completed: !@.get('completed')

  module.exports = Todo
