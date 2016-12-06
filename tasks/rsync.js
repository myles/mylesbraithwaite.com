module.exports = function (grunt) {
    'use strict';

    var config = {
        options: {
            args: ['--verbose'],
            exclude: ['.git*', '*.scss', 'node_modules'],
            recursive: true,
            delete: true
        },
        prod: {
            options: {
                src: '.cache/prod',
                dest: grunt.config.get('prod.rsync.dest'),
                host: grunt.config.get('prod.rsync.host')
            }
        },
        stag: {
            options: {
                src: '.cache/prod',
                dest: grunt.config.get('stag.rsync.dest'),
                host: grunt.config.get('stag.rsync.host')
            }
        }
    };

    grunt.config.set('rsync', config);
};
