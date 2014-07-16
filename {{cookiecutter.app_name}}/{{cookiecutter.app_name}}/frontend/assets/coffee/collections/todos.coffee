define ['backbone', 'models/todo', 'module'], (Backbone, Todo, module) ->

  Todos = Backbone.Collection.extend
    
    model: Todo

    completed: ->
      @where completed: true

    remaining: ->
      @where completed: false

  module.exports = Todos
