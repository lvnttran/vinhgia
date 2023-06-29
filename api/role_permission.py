from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from api import role, permission
from schema import schemas
from schema.hash import Hash


def create(request: schemas.RolePermission, db: Session):
    
    role_ = role.show(id=request.role_id, db=db)
    permission_ = permission.show(id=request.permission_id, db=db)
    rolepermission = db.query(models.RolePermission).filter(
        models.RolePermission.role_id == role_.id, models.RolePermission.permission_id == permission_.id).first()
    if rolepermission:
        return rolepermission
    new_role_permission = models.RolePermission(role_id=role_.id, permission_id= permission_.id)
    db.add(new_role_permission)
    db.commit()
    db.refresh(new_role_permission)
    return new_role_permission


def show(id: int, db: Session):
    
    roles = db.query(models.RolePermission).filter(models.RolePermission.role_id == id).all()
    print(roles)
    return roles

def update(request: schemas.RolePermissionUpdate, db: Session):
    role_ = role.show(id=request.role_id, db=db)
    for perms in request.permissions:
        permission_ = permission.show(id=perms, db=db)
    old_permission_ids =  db.query(models.RolePermission).filter(models.RolePermission.role_id == role_.id).all()
    old_permission_ids = [RolePermission.permission_id for RolePermission in old_permission_ids]
    delete_permission_ids = [premid for premid in old_permission_ids if not premid in request.permissions]
    add_permission_ids = [perm_id for perm_id in request.permissions if perm_id not in old_permission_ids]
    for permission_id in add_permission_ids:
        newRolePermission = schemas.RolePermission(role_id=role_.id, permission_id= permission_id)
        create(newRolePermission, db)
    for permission_id in delete_permission_ids:
        deleteRolePermission = schemas.RolePermission(role_id=role_.id, permission_id= permission_id)
        destroy(deleteRolePermission, db)

def destroy(request: schemas.RolePermission, db: Session):
    rolepermission = db.query(models.RolePermission).filter(
        models.RolePermission.role_id == request.role_id, models.RolePermission.permission_id == request.permission_id)

    if not rolepermission.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"RolePermission type with id {request} not found.",
        )
    rolepermission.delete(synchronize_session=False)
    db.commit()
    return


