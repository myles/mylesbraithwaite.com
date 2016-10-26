module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        config: grunt.file.readYAML('config/base.yml')
    });

    grunt.loadNpmTasks('grunt-jekyll');

    grunt.task.loadTasks('./tasks/');
};

