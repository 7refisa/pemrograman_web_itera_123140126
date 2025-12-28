from pyramid.config import Configurator


def main(global_config, **settings):
    """
    Entry point untuk aplikasi Pyramid Matakuliah.
    Menginisialisasi dan mengembalikan WSGI application.
    """
    with Configurator(settings=settings) as config:
        # Setup Jinja2 templating
        config.include('pyramid_jinja2')
        
        # Setup database models
        config.include('.models')
        
        # Setup URL routing
        config.include('.routes')
        
        # Scan dan register views
        config.scan('.views')
        
    return config.make_wsgi_app()
