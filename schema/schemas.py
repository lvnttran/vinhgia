from typing import List, Optional
from typing import BinaryIO
from pydantic import BaseModel
from fastapi import UploadFile, File


class FactoryBase(BaseModel):
    name: str
    location: str


class Factory(FactoryBase):
    class Config:
        orm_mode = True


class FactoryShow(FactoryBase):
    id: int

    class Config:
        orm_mode = True


class WorkshopBase(BaseModel):
    name: str
    description: str
    factory_id: int


class Workshop(WorkshopBase):
    class Config:
        orm_mode = True


class WorkshopShow(WorkshopBase):
    id: int

    class Config:
        orm_mode = True


class WorkshopModel(WorkshopBase):
    factory: FactoryShow

    class Config:
        orm_mode = True


class FactoryModel(FactoryShow):
    id: int
    workshops: List[WorkshopShow]

    class Config:
        orm_mode = True




class RouterBase(BaseModel):
    name: str


class Router(RouterBase):
    class Config:
        orm_mode = True


class RouterShow(RouterBase):
    id: int

    class Config:
        orm_mode = True


class PermissionBase(BaseModel):
    name: str
    parent_id: int


class Permission(PermissionBase):
    class Config:
        orm_mode = True


class PermissionShow(PermissionBase):
    id: int

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    name: str
    workshop_id: int


class Role(RoleBase):
    class Config:
        orm_mode = True


class RoleShow(RoleBase):
    id: int

    class Config:
        orm_mode = True


class RoleModel(RoleShow):
    workshop: WorkshopModel

    class Config:
        orm_mode = True


class RolePermissionBase(BaseModel):
    role_id: int
    permission_id: int


class RolePermissionUpdate(BaseModel):
    role_id: int
    permissions: List[int]


class RolePermission(RolePermissionBase):
    class Config:
        orm_mode = True


class RolePermissionShow(RolePermissionBase):
    class Config:
        orm_mode = True


class RoleUserBase(BaseModel):
    role_id: int
    user_id: int


class RoleUser(RoleUserBase):
    class Config:
        orm_mode = True


class RoleUserShow(RoleUserBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    user_email: str


class User(UserBase):
    user_pass: str

    class Config:
        orm_mode = True


class UserShow(UserBase):
    user_id: int

    class Config:
        orm_mode = True


class RouterModel(RouterShow):
    permissions: List[PermissionShow]

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
