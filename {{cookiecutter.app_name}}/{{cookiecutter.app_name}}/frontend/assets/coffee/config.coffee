require.config {
  baseURL: 'static/js'
  paths:
    jquery: 'vendor/jquery'
    lodash: 'vendor/underscore'
    backbone: 'vendor/backbone'
    bootstrap: 'vendor/bootstrap'
    react: 'vendor/react'
  shim:
    backbone:
      deps: ['lodash, jquery']
      exports: 'Backbone'
    bootstrap:
      deps: ['jquery']
      exports: 'Bootstrap'
    lodash:
      exports: '_'
    jquery:
      exports: '$'
}
