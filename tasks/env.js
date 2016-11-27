module.exports = function (grunt) {
    'use strict';

    var config = {
        local: {
            JEKYLL_ENV: 'development'
        },
        stag: {
            JEKYLL_ENV: 'production'
        },
        prod: {
            JEKYLL_ENV: 'production'
        }
    };

    grunt.config.set('env', config);
};
