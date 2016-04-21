var gulp = require('gulp-help')(require('gulp'));
var less = require('gulp-less');

gulp.task('pages:less', 'Compile the theme LESS files', function() {
    gulp.src('oscar/base/static/base/pages/less/pages.less')
    .pipe(less())
    .pipe(gulp.dest('oscar/base/static/base/pages/css'));
});