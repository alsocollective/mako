module.exports = function(grunt) {

//require('load-grunt-tasks')(grunt); // npm install --save-dev load-grunt-tasks

grunt.initConfig({
  svgcompactor: {
    all: {
      source: 'output',
      target: 'output',
      outputname: 'stack'
    }
  },
  
  pkg: grunt.file.readJSON('package.json'),
    svgmin: {
        options: {
            plugins: [
                { removeViewBox: true },
                { removeUselessStrokeAndFill: true },
                { collections: true },
                { path: true} ,
                { transforms: true },
                { cleanupAttrs: true },
                { cleanupEnableBackground: true },
                { cleanupIDs: true },
                { cleanupNumericValues: true },
                { collapseGroups: false},
                { convertColors: true },
                { convertPathData: true},
                { convertShapeToPath: true},
                { convertStyleToAttrs: true},
                { convertTransform: true},
                { mergePaths: true},
                { moveElemsAttrsToGroup: true},
                { moveGroupAttrsToElems: true},
                { removeComments: true},
                { removeDoctype: true},
                { removeEditorsNSData: true},
                { removeEmptyAttrs: true},
                { removeEmptyContainers: true},
                { removeEmptyText: true},
                { removeHiddenElems: true},
                { removeMetadata: true},
                { removeNonInheritableGroupAttrs: true},
                { removeRasterImages: true},
                { removeTitle: true},
                { removeUnknownsAndDefaults: true},
                { removeUnusedNS: true},
                { removeUselessStrokeAndFill: true},
                { removeViewBox: true},
                { removeXMLProcInst: true},
                { sortAttrs: true},
                { transformsWithOnePath: true},
                { datauri: true}
            ]
        },
        dist: {
            files: {
                './output/test.min.svg': './output/250-09_wv_09-07-14.svg'
            }
        }
    }
});

grunt.loadTasks('tasks');
grunt.loadNpmTasks('grunt-svgmin');
grunt.loadNpmTasks('grunt-svg-compactor');

grunt.registerTask('default', ['svgmin']);
grunt.registerTask('comp', ['svgcompactor']);



};