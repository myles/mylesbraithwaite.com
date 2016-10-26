module.exports = function (grunt) {
    'use strict';

    grunt.registerTask('develop', ['jekyll:serve']);

    grunt.registerTask('default', ['develop']);
};
