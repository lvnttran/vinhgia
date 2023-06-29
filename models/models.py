from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

from database.configuration import Base


class Factory(Base):
    __tablename__ = "NhaMay"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(128))
    location = Column(String(128))
    workshops = relationship("Workshop", backref="factory", cascade="all, delete-orphan")


class Workshop(Base):
    __tablename__ = "Xuong"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    description = Column(String(256))
    factory_id = Column(Integer, ForeignKey("NhaMay.id"))
    roles = relationship("Role", backref="workshop", cascade="all, delete-orphan")


class Router(Base):
    __tablename__ = "SubQuyen"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    permissions = relationship("Permission", backref="router", cascade="all, delete-orphan")


class Permission(Base):
    __tablename__ = "Quyen"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    parent_id = Column(Integer, ForeignKey("SubQuyen.id"))


class Role(Base):
    __tablename__ = "NhomQuyen"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    workshop_id = Column(Integer, ForeignKey("Xuong.id"))


class RolePermission(Base):
    __tablename__ = "PhanQuyen"
    role_id = Column(Integer, ForeignKey("NhomQuyen.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("Quyen.id"), primary_key=True)


class User(Base):
    __tablename__ = 'TaiKhoan'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256))
    user_email = Column(String(256))
    user_pass = Column(String(256))


class RoleUser(Base):
    __tablename__ = 'CapQuyen'
    role_id = Column(Integer, ForeignKey("NhomQuyen.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("TaiKhoan.user_id"), primary_key=True)


class Donhang(Base):
    __tablename__ = "donhang"

    donhang_id = Column(Integer, primary_key=True, index=True)
    donhang_madh = Column(String)
    donhang_masp = Column(String)
    donhang_mota = Column(String)
    donhang_soluong = Column(String)
    donhang_ngay = Column(Date)


class Maloi(Base):
    __tablename__ = "maloi"

    maloi_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    maloi_maloi = Column(String)
    maloi_tenloi = Column(String)
    maloi_khacphuc = Column(String)
    maloi_nguyennhan = Column(String)
    maloi_phongngua = Column(String)
