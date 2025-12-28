def includeme(config):
    """
    Konfigurasi routing untuk aplikasi Matakuliah.
    Mendefinisikan endpoint API untuk CRUD mata kuliah.
    """
    # Static files configuration
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    # Route halaman utama
    config.add_route('home', '/')

    # API Routes untuk operasi CRUD Matakuliah
    config.add_route('matakuliah_list', '/api/matakuliah', request_method='GET')      # Ambil semua
    config.add_route('matakuliah_detail', '/api/matakuliah/{id}', request_method='GET')  # Ambil by ID
    config.add_route('matakuliah_add', '/api/matakuliah', request_method='POST')     # Tambah baru
    config.add_route('matakuliah_update', '/api/matakuliah/{id}', request_method='PUT')  # Update by ID
    config.add_route('matakuliah_delete', '/api/matakuliah/{id}', request_method='DELETE')  # Hapus by ID