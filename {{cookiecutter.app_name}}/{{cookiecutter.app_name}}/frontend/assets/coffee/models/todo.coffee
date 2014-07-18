define ['models/base', 'module'], (BaseModel, module) ->

  Todo = BaseModel.extend
    
    default:
      title: ''
      completed: false

    toggle: ->
      @.save completed: !@.get('completed')

  module.exports = Todo
