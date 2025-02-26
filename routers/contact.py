from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import cruds.contact as contact_crud
from database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.ContactList])
def get_contact_all():
  dummy_data = datetime.now()
  return [contact_schema.Contact(
    id=1,
    name='yama', 
    email="user@example.com", 
    url="http://tet.tes.tte",
    gender=1,
    message="test",
    is_enabled=False,
    created_at=dummy_data)]

@router.post("/contacts", 
             response_model=contact_schema.ContactCreate)
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
  return await contact_crud.create_contact(db, body)

@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail)
def get_contact(id: int):
  return contact_schema.Contact(id)

@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)
def update_contact(id: int, body: contact_schema.ContactCreate):
  return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{id}", response_model=None)
def delete_contact(id: int):
  return