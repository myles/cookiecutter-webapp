module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    bowercopy: {
      options: {
        srcPrefix: 'bower_components',
        destPrefix: '{{ cookiecutter.app_name }}/frontend/static'
      },
      scripts: {
        files: {
          'js/bootstrap.min.js': 'bootstrap/dist/js/bootstrap.min.js',
          'js/html5shiv.js': 'html5shiv/dist/html5shiv.js',
          'js/jquery.js': 'jquery/dist/jquery.js',
          'js/modernizr.js': 'modernizr/modernizr.js',
          'js/pjax.js': 'pjax/src/pjax.js',
          'js/respond.js': 'respond/dest/respond.src.js'
        }
      },
      stylesheets: {
        files: {
          'css/bootstrap.css': 'bootstrap/dist/css/bootstrap.css',
          'css/font-awesome.css': 'font-awesome/css/font-awesome.css'
        }
      },
      fonts: {
        files: {
          'fonts': 'font-awesome/fonts'
        }
      }
    }
  });
  grunt.loadNpmTasks('grunt-bowercopy');
  grunt.registerTask('default', ['bowercopy']);
};
