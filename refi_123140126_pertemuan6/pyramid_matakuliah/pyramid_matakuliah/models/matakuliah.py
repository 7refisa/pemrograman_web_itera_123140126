from sqlalchemy import Column, Integer, Text
from .meta import Base


class Matakuliah(Base):
    """
    Representasi tabel matakuliah dalam database.
    Menyimpan informasi mata kuliah seperti kode, nama, SKS, dan semester.
    """
    __tablename__ = 'matakuliah'
    
    # Definisi kolom tabel
    id = Column(Integer, primary_key=True)
    kode_mk = Column(Text, unique=True, nullable=False)  # Kode MK harus unik
    nama_mk = Column(Text, nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)

    def to_dict(self):
        """
        Konversi object matakuliah ke format dictionary.
        Digunakan untuk serialisasi data ke JSON.
        """
        return {
            'id': self.id,
            'kode_mk': self.kode_mk,
            'nama_mk': self.nama_mk,
            'sks': self.sks,
            'semester': self.semester
        }