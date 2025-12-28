from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from ..models import Matakuliah


@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    """
    Endpoint untuk mendapatkan daftar semua mata kuliah.
    Returns: List mata kuliah dalam format JSON
    """
    db = request.dbsession
    data_mk = db.query(Matakuliah).all()
    
    # Transform ke dictionary
    result = [mk.to_dict() for mk in data_mk]
    
    return {'matakuliahs': result}


@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    """
    Endpoint untuk mendapatkan detail satu mata kuliah berdasarkan ID.
    Returns: Data mata kuliah atau error 404
    """
    db = request.dbsession
    mk_id = request.matchdict['id']
    
    # Query data berdasarkan ID
    mk = db.query(Matakuliah).filter_by(id=mk_id).first()

    if not mk:
        return HTTPNotFound(json_body={'error': 'Data mata kuliah tidak ditemukan'})

    return {'matakuliah': mk.to_dict()}


@view_config(route_name='matakuliah_add', request_method='POST', renderer='json')
def matakuliah_add(request):
    """
    Endpoint untuk menambahkan mata kuliah baru.
    Request body: JSON dengan field kode_mk, nama_mk, sks, semester (semua required)
    Returns: Data mata kuliah yang baru dibuat
    """
    try:
        data = request.json_body

        # Validasi field yang diperlukan
        field_required = ['kode_mk', 'nama_mk', 'sks', 'semester']
        for field in field_required:
            if field not in data:
                return HTTPBadRequest(
                    json_body={'error': f'Field "{field}" harus diisi'}
                )

        # Buat instance baru
        mk_baru = Matakuliah(
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=int(data['sks']),
            semester=int(data['semester'])
        )

        # Simpan ke database
        db = request.dbsession
        db.add(mk_baru)
        db.flush()  # Generate ID baru

        return {
            'success': True,
            'message': 'Mata kuliah berhasil ditambahkan',
            'matakuliah': mk_baru.to_dict()
        }

    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='matakuliah_update', request_method='PUT', renderer='json')
def matakuliah_update(request):
    """
    Endpoint untuk mengupdate data mata kuliah.
    Request body: JSON dengan field yang ingin diupdate
    Returns: Data mata kuliah yang sudah diupdate
    """
    db = request.dbsession
    mk_id = request.matchdict['id']
    
    # Cari data yang akan diupdate
    mk = db.query(Matakuliah).filter_by(id=mk_id).first()

    if not mk:
        return HTTPNotFound(json_body={'error': 'Data mata kuliah tidak ditemukan'})

    try:
        data = request.json_body

        # Update field yang dikirim
        if 'kode_mk' in data:
            mk.kode_mk = data['kode_mk']
        if 'nama_mk' in data:
            mk.nama_mk = data['nama_mk']
        if 'sks' in data:
            mk.sks = int(data['sks'])
        if 'semester' in data:
            mk.semester = int(data['semester'])

        return {
            'success': True,
            'message': 'Data mata kuliah berhasil diupdate',
            'matakuliah': mk.to_dict()
        }

    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='matakuliah_delete', request_method='DELETE', renderer='json')
def matakuliah_delete(request):
    """
    Endpoint untuk menghapus mata kuliah.
    Returns: Pesan sukses atau error 404
    """
    db = request.dbsession
    mk_id = request.matchdict['id']
    
    # Cari data yang akan dihapus
    mk = db.query(Matakuliah).filter_by(id=mk_id).first()

    if not mk:
        return HTTPNotFound(json_body={'error': 'Data mata kuliah tidak ditemukan'})

    # Simpan info sebelum dihapus
    nama_mk = mk.nama_mk
    
    # Hapus dari database
    db.delete(mk)

    return {
        'success': True,
        'message': f'Mata kuliah "{nama_mk}" (ID: {mk_id}) berhasil dihapus'
    }