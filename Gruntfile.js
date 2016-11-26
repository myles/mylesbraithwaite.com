module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        config: grunt.file.readYAML('config/base.yml'),
        prod: grunt.file.readYAML('config/prod.yml'),
        stag: grunt.file.readYAML('config/stag.yml')
    });

    grunt.loadNpmTasks('grunt-jekyll');
    grunt.loadNpmTasks('grunt-rsync');
    grunt.loadNpmTasks('grunt-env');

    grunt.task.loadTasks('./tasks/');
};
