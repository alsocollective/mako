var fs = require('fs');
var childProcess = require('child_process');
module.exports = function(grunt) {
    grunt.registerTask('seed', function() {
        var done = this.async();

        //var seed = fs.createReadStream('huron-svg.json');

        fs.writeFile('huron-svg.json', 'Hello Node', function (err) {
            if (err) throw err;
        });

    });
};