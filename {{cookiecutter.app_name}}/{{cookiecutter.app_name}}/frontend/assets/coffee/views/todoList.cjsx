define ['backbone', 'react', 'mixins/backbone', 'views/todoItem', 'module'],
  (Backbone, React, BackboneMixin, TodoItem, module) ->

  TodoList = React.createClass

    mixins: [BackboneMixin]

    getBackboneCollections: -> [ @props.todos ]

    getInitialState: -> editing: null

#   componentDidMount: ->
#     Router = Backbone.Router.extend
#       routes:
#         "": "all"
#         "active": "active"
#         "completed": "completed"
#       all: @setState.bind @ nowShowing: 'all'
#       active: @setState.bind @ nowShowing: 'active'
#       completed: @setState.bind @ nowShowing: 'completed'
#     router = new Router
#     Backbone.history.start
#     @props.todos.fetch

    handleNewTodoKeyDown: (event) ->
      console.log "KeyPressed ", + event.which


    toggleAll: ->
      console.log "toggleAll called"

    edit: (todo, callback) ->
      @setState editing: todo.get('id') callback

    save: (todo, text) ->
      todo.save title: text
      @setState editing: null

    cancel:
      @setState editing: null

    clearCompleted: ->
      todo.destroy for todo in @props.todos.completed()

    render: ->
      console.log @props.todos

      visibleTodos = @props.todos.filter (todo) ->
        switch @state.nowShowing
          when 'active' then return !todo.get('completed')
          when 'completed'then return todo.get('completed')
          else return true

      console.log visibleTodos

      todoItems = (<TodoItem key={todo.get('id')} todo={todo} /> \
        for todo in @props.todos)

      if @props.todos.length
        main = (
          <section id="main">
            <input
              id="toggle-all"
              type="checkbox"
              onChange={@toggleAll}
            />
            <ul id="todo-list">
              {todoItems}
            </ul>
          </section>
        )
 
      <div>
        <header id="header">
          <h1>todos</h1>
          <input
            ref="newField"
            id="new-todo"
            placeholder="What needs to be done?"
            onKeyDown={@handleNewTodoKeyDown}
            autoFocus={true}
          />
        </header>
        {body}
        {footer}
      </div>

  module.exports = TodoList
