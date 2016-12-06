var netrc = require('netrc');

module.exports = function (grunt) {
    'use strict';

    var netrc_config = netrc();

    grunt.initConfig({
        config: grunt.file.readYAML('config/base.yml'),
        prod: grunt.file.readYAML('config/prod.yml'),
        stag: grunt.file.readYAML('config/stag.yml'),
        aws: netrc_config['aws']
    });

    grunt.loadNpmTasks('grunt-aws-s3');
    grunt.loadNpmTasks('grunt-jekyll');
    grunt.loadNpmTasks('grunt-rsync');
    grunt.loadNpmTasks('grunt-env');

    grunt.task.loadTasks('./tasks/');
};
