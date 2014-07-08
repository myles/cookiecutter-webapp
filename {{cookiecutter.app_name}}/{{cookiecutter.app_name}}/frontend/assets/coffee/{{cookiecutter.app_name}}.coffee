$ =>

  class WebApp

    hello: (foo)->
      console.log 'yep, WebApp works #{foo}'

  webapp = new WebApp
  webapp.hello "bar"
