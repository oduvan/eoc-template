requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'say_hi',
                js: 'sayHi'
            }
        });
        io.start();
    }
);
