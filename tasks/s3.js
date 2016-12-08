module.exports = function (grunt) {
    'use strict';

    var config = {
        options: {
            accessKeyId: grunt.config.get('aws.login'),
            secretAccessKey: grunt.config.get('aws.password'),
            bucket: 'assets.mylesbraithwaite.com',
            differential: true
        },

        up: {
            files: [{
                expand: true,
                cwd: './source/uploads/',
                src: ['**'],
                dest: 'uploads/',
                stream: true
            }]
        },

        down: {
            files: [{
                dest: 'uploads/',
                cwd: './source/uploads',
                action: 'download'
            }]
        }
    };

    grunt.config.set('aws_s3', config);
};
