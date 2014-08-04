require ['bootstrap', 'jquery'], (Bootstrap, $) ->

  $('.dropdown-toggle').dropdown()

  $('a[href="#"]').click (e) ->
    e.preventDefault()

  hide_flask_message_container = () ->
    $('#flash_message_container').slideUp 'fast'

