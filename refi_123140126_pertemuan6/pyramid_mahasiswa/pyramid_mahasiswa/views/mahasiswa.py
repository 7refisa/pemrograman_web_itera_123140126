import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from ..models import Mahasiswa


@view_config(route_name='mahasiswa_list', renderer='json')
def mahasiswa_list(request):
    """
    Endpoint untuk mendapatkan semua data mahasiswa.
    Returns: List semua mahasiswa dalam format JSON
    """
    db = request.dbsession
    data_mahasiswa = db.query(Mahasiswa).all()
    
    # Konversi setiap mahasiswa ke dictionary
    result = [mhs.to_dict() for mhs in data_mahasiswa]
    
    return {'mahasiswas': result}


@view_config(route_name='mahasiswa_detail', renderer='json')
def mahasiswa_detail(request):
    """
    Endpoint untuk mendapatkan detail satu mahasiswa berdasarkan ID.
    Returns: Data mahasiswa dalam format JSON atau error 404
    """
    db = request.dbsession
    mhs_id = request.matchdict['id']
    
    # Cari mahasiswa berdasarkan ID
    mhs = db.query(Mahasiswa).filter_by(id=mhs_id).first()

    if not mhs:
        return HTTPNotFound(json_body={'error': 'Data mahasiswa tidak ditemukan'})

    return {'mahasiswa': mhs.to_dict()}


@view_config(route_name='mahasiswa_add', request_method='POST', renderer='json')
def mahasiswa_add(request):
    """
    Endpoint untuk menambah data mahasiswa baru.
    Request body: JSON dengan field nim, nama, jurusan (required) dan 
                  tanggal_lahir, alamat (optional)
    Returns: Data mahasiswa yang baru dibuat
    """
    try:
        data = request.json_body

        # Validasi field yang wajib diisi
        field_wajib = ['nim', 'nama', 'jurusan']
        for field in field_wajib:
            if field not in data:
                return HTTPBadRequest(
                    json_body={'error': f'Field "{field}" harus diisi'}
                )

        # Proses tanggal lahir jika tersedia
        tgl_lahir = None
        if 'tanggal_lahir' in data and data['tanggal_lahir']:
            try:
                tgl_lahir = datetime.datetime.fromisoformat(
                    data['tanggal_lahir']
                ).date()
            except ValueError:
                return HTTPBadRequest(
                    json_body={
                        'error': 'Format tanggal salah. Gunakan format: YYYY-MM-DD'
                    }
                )

        # Membuat instance mahasiswa baru
        mhs_baru = Mahasiswa(
            nim=data['nim'],
            nama=data['nama'],
            jurusan=data['jurusan'],
            tanggal_lahir=tgl_lahir,
            alamat=data.get('alamat')
        )

        # Simpan ke database
        db = request.dbsession
        db.add(mhs_baru)
        db.flush()  # Dapatkan ID yang baru di-generate

        return {
            'success': True, 
            'message': 'Data mahasiswa berhasil ditambahkan',
            'mahasiswa': mhs_baru.to_dict()
        }

    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='mahasiswa_update', request_method='PUT', renderer='json')
def mahasiswa_update(request):
    """
    Endpoint untuk mengupdate data mahasiswa yang sudah ada.
    Request body: JSON dengan field yang ingin diupdate
    Returns: Data mahasiswa yang sudah diupdate
    """
    db = request.dbsession
    mhs_id = request.matchdict['id']

    # Cari data mahasiswa
    mhs = db.query(Mahasiswa).filter_by(id=mhs_id).first()
    if not mhs:
        return HTTPNotFound(json_body={'error': 'Data mahasiswa tidak ditemukan'})

    try:
        data = request.json_body

        # Update field yang dikirim
        if 'nim' in data:
            mhs.nim = data['nim']
        if 'nama' in data:
            mhs.nama = data['nama']
        if 'jurusan' in data:
            mhs.jurusan = data['jurusan']
        if 'alamat' in data:
            mhs.alamat = data['alamat']

        # Proses update tanggal lahir
        if 'tanggal_lahir' in data:
            if data['tanggal_lahir']:
                try:
                    mhs.tanggal_lahir = datetime.datetime.fromisoformat(
                        data['tanggal_lahir']
                    ).date()
                except ValueError:
                    return HTTPBadRequest(
                        json_body={
                            'error': 'Format tanggal salah. Gunakan format: YYYY-MM-DD'
                        }
                    )
            else:
                mhs.tanggal_lahir = None

        return {
            'success': True,
            'message': 'Data mahasiswa berhasil diupdate',
            'mahasiswa': mhs.to_dict()
        }

    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='mahasiswa_delete', request_method='DELETE', renderer='json')
def mahasiswa_delete(request):
    """
    Endpoint untuk menghapus data mahasiswa.
    Returns: Pesan sukses atau error 404
    """
    db = request.dbsession
    mhs_id = request.matchdict['id']

    # Cari data yang akan dihapus
    mhs = db.query(Mahasiswa).filter_by(id=mhs_id).first()
    if not mhs:
        return HTTPNotFound(json_body={'error': 'Data mahasiswa tidak ditemukan'})

    # Simpan info sebelum dihapus
    nama_mhs = mhs.nama
    
    # Hapus dari database
    db.delete(mhs)

    return {
        'success': True,
        'message': f'Data mahasiswa "{nama_mhs}" (ID: {mhs_id}) berhasil dihapus'
    }