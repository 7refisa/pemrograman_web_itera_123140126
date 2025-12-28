from sqlalchemy import Column, Integer, Text, Date
from .meta import Base


class Mahasiswa(Base):
    """
    Representasi tabel mahasiswa dalam database.
    Menyimpan informasi data mahasiswa seperti NIM, nama, jurusan, dll.
    """
    __tablename__ = 'mahasiswa'
    
    # Kolom-kolom tabel
    id = Column(Integer, primary_key=True)
    nim = Column(Text, unique=True, nullable=False)  # NIM harus unik
    nama = Column(Text, nullable=False)
    jurusan = Column(Text, nullable=False)
    tanggal_lahir = Column(Date, nullable=True)
    alamat = Column(Text, nullable=True)

    def to_dict(self):
        """
        Mengkonversi object mahasiswa menjadi dictionary.
        Berguna untuk serialisasi ke JSON.
        """
        data = {
            'id': self.id,
            'nim': self.nim,
            'nama': self.nama,
            'jurusan': self.jurusan,
            'alamat': self.alamat
        }
        
        # Format tanggal jika ada
        if self.tanggal_lahir:
            data['tanggal_lahir'] = self.tanggal_lahir.isoformat()
        else:
            data['tanggal_lahir'] = None
            
        return data