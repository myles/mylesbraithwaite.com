module.exports = function (grunt) {
    'use strict';

    grunt.registerTask('develop', ['jekyll:serve']);

    grunt.registerTask('build', ['jekyll:build']);

    grunt.registerTask('deploy', ['env:stag', 'jekyll:stag', 'rsync:stag']);
    grunt.registerTask('deploy:prod', ['env:prod', 'jekyll:prod',
                                       'rsync:prod']);

    grunt.registerTask('default', ['develop']);
};
