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
        local: {
            options: {
                build: true,
                config: 'config/base.yml,config/local.yml',
                dest: '~/Sites/sites/mylesbraithwaite-com/html/'
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
                unpublished: true,
                limit_posts: 50,
                incremental: true
            }
        }
    };

    grunt.config.set('jekyll', config);
};
