def includeme(config):
    """
    Konfigurasi routing untuk aplikasi.
    Mendefinisikan semua endpoint API yang tersedia.
    """
    # Static files (CSS, JS, images)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Route halaman utama
    config.add_route('home', '/')

    # API Routes untuk CRUD Mahasiswa
    config.add_route('mahasiswa_list', '/api/mahasiswa', request_method='GET')      # List semua
    config.add_route('mahasiswa_detail', '/api/mahasiswa/{id}', request_method='GET')  # Detail by ID
    config.add_route('mahasiswa_add', '/api/mahasiswa', request_method='POST')     # Tambah baru
    config.add_route('mahasiswa_update', '/api/mahasiswa/{id}', request_method='PUT')  # Update by ID
    config.add_route('mahasiswa_delete', '/api/mahasiswa/{id}', request_method='DELETE')  # Hapus by ID