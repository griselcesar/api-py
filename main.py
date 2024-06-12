from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.title = "API Py"
app.version = "0.0.1"
app.description = "API REST diseñada para manejo de datos de una empresa standard."
app.contact = {"name":"César Grisel","email":"griselcesar@gmail.com"}

class clientModel(BaseModel):
  id:str
  name:str
  address:str
  phone:str

class clientModelUpdate(BaseModel):
  name:str
  address:str
  phone:str

clients:List[clientModel] = []

@app.get("/",tags=['Home'])
async def root():
  return {"message":"Hola mundo"}


@app.get("/clients",tags=['Clients'])
async def get_all_clients() -> List[clientModel]:
  return clients

@app.get("/clients/{id}",tags=['Clients'])
async def get_one_client_by_id(id:str) -> clientModel:
  for client in clients:
    if client['id'] == id:
      return client

@app.post("/clients",tags=['Clients'])
async def create_one_client(newClient:clientModel) -> List[clientModel]:
  clients.append(dict(newClient))
  return clients

@app.delete("/clients/{id}",tags=['Clients'])
async def delete_one_client_by_id(id:str) -> List[clientModel]:
  for client in clients:
    if client['id'] == id:
      clients.remove(client)
  return clients

@app.put("/client/{id}",tags=['Clients'])
async def update_one_client_by_id(id:str,newClient:clientModelUpdate) -> clientModel:
  for client in clients:
    if client['id'] == id:
      client['name'] = newClient.name
      client['address'] = newClient.address
      client['phone'] = newClient.phone
  return client