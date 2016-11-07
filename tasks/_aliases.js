module.exports = function (grunt) {
    'use strict';

    grunt.registerTask('develop', ['jekyll:serve']);

    grunt.registerTask('build', ['jekyll:build']);

    grunt.registerTask('default', ['develop']);
};
