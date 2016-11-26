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
        stag: {
            options: {
                build: true,
                config: 'config/base.yml,config/stag.yml'
            }
        },
        prod: {
            options: {
                build: true,
                config: 'config/base.yml,config/prod.yml'
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
