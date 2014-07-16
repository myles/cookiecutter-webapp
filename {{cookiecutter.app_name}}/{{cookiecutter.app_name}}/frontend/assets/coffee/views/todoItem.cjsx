define ['react', 'module'], (React, module) ->

  # define a utils package mapping keys to key values
  ESCAPE_KEY = 27
  ENTER_KEY = 13

  TodoItem = React.createClass
    
    getInitialState: ->
      editText: @props.todo.get 'title'

    handleSubmit: ->
      console.log "handleSubmit called"

    handleEdit: ->
      console.log "handleEdit called"

    handleKeyDown: ->
      console.log "handleKeyDown called"

    handleChange: ->
      console.log "handleChange called"

    render: ->
      <li className={React.addons.classSet completed: @props.todo.get('completed') editing: @props.editting}>
        <div className="view">
          <input
            className="toggle"
            type="checkbox"
            checked={@props.todo.get('completed')}
            onChange={@props.onToggle}
          />
          <label onDoubleClick={@handleEdit}>
            {@props.todo.get('title')}
          </label>
          <button className="destroy" onClick={@props.onDestroy} />
        </div>
        <input
          ref="editField"
          className="edit"
          value={@state.editText}
          onBlur={@handleSubmit}
          onChange={@handleChange}
          onKeyDown={@handleKeyDown}
        />
      </li>


