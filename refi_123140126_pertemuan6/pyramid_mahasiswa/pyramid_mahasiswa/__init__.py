from pyramid.config import Configurator


def main(global_config, **settings):
    """
    Fungsi utama untuk menginisialisasi aplikasi Pyramid.
    Mengembalikan WSGI application yang siap dijalankan.
    """
    with Configurator(settings=settings) as config:
        # Include templating engine Jinja2
        config.include('pyramid_jinja2')
        
        # Include models (database)
        config.include('.models')
        
        # Include routes (URL mapping)
        config.include('.routes')
        
        # Scan views untuk auto-register view configs
        config.scan('.views')
        
    return config.make_wsgi_app()
