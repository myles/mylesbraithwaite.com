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
                watch: true,
                config: 'config/base.yml,config/local.yml',
                dest: '~/Sites/sites/mylesbraithwaite-com/html/'
            }
        },

        stag: {
            options: {
                build: true,
                config: 'config/base.yml,config/stag.yml',
                dest: '.cache/stag',
                quiet: true
            }
        },

        prod: {
            options: {
                build: true,
                config: 'config/base.yml,config/prod.yml',
                dest: '.cache/prod',
                quiet: true
            }
        },

        serve: {
            options: {
                serve: true,
                auto: true,
                future: true,
                unpublished: true,
                drafts: true,
                limit_posts: 50,
                incremental: false
            }
        }
    };

    grunt.config.set('jekyll', config);
};
