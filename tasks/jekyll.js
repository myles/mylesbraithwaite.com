module.exports = function (grunt) {
    'use strict';

    var config = {
        options: {
            bundleExec: true,
            config: 'config/base.yml,config/local.yml'
        },
        build: {
            options: {
                build: true
            }
        },
        serve: {
            options: {
                serve: true,
                auto: true,
                future: true,
                unpublished: true
            }
        }
    };

    grunt.config.set('jekyll', config);
};
