define ['models/base', 'module'], (Model, module) ->

  class Todo extends Model
    
    default:
      title: ''
      completed: false

    toggle: ->
      @save {
        completed: !@get('completed')
      }, {
        wait: true
      }

    destroy: (options) ->
      options = @extend_options(options)
      super options

    extend_options: (options) ->
      options ?= {}
      options.wait ?= true

  module.exports = Todo
