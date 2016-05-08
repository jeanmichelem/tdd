var gulp = require('gulp');

var shell = require('gulp-shell');

gulp.task('run-tests', shell.task([
    'run-unit-tests', 'run-behave-tests']));

gulp.task('run-unit-tests', shell.task([
    'nosetests tests']));

gulp.task('run-behave-tests', shell.task([
    'behave --color features']));

gulp.task('watch', function(){
    gulp.watch(['./tests/**/*.py', './features/**/*.py'], ['run-unit-tests', 'run-behave-tests']);
});

var spawn = require("gulp-spawn");
//var spawn = require("child_process").spawnSync;

/**
 * run the sanity test
 */
gulp.task("run-behave-spawn", function () {
  spawn ({
      cmd: "a",
      args:  ["./features"],
      stdio: 'inherit'
  });
});



gulp.task('default',['run-behave-spawn','watch']);
