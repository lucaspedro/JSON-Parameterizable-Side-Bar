from flask.ext.assets import Bundle, Environment
from my_app import app

bundles = {
    'home_js': Bundle(
        'lib/jquery/jquery.js',
        'lib/bootstrap/js/bootstrap.js',
        'js/home.js',
        output='gen/home.js'),

    'home_css': Bundle(
            'lib/bootstrap/css/bootstrap.css',
            'css/common.css',
            'css/home.css',
            output='gen/home.css')
}


assets = Environment(app)

assets.register(bundles)