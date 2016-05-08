//gruntfile.js
module.exports = function(grunt) {

  grunt.initConfig({
    watch: {
      files: ['*.py'],
      tasks: ['shell:test']
    },
    shell: {
      test: {
        command: 'nosetests'
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('default', ['watch']);
};