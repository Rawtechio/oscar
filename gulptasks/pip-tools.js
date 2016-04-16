var gulp = require('gulp-help')(require('gulp'));
var shell = require('gulp-shell')

gulp.task('pin:local', 'Pins all Local requirements from local.in', shell.task([
    "pip-compile requirements/local.in -o requirements/pinned/local.txt"
]));

gulp.task('pin:production', 'Pins all Production requirements from production.in', shell.task([
    "pip-compile requirements/production.in -o requirements/pinned/production.txt"
]));

gulp.task('pin:travis', 'Pins all Production requirements from travis.in', shell.task([
    "pip-compile requirements/travis.in -o requirements/pinned/travis.txt"
]));

gulp.task('pin:all', 'Pins all requirements', ['pin:local', 'pin:production', 'pin:travis']);

gulp.task('sync:local', 'Sync your local requirements with pinned versions', shell.task([
    "pip-sync requirements/pinned/local.txt"
]));