from fastapi import FastAPI
from sqlmodel import Field, SQLModel,create_engine, select,Session,delete


DATABASE_KEY= 'add_your_database_key'

#table pizza
class Pizza(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    price: float
    description: str
    size: str

#table user
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str 
    password: str

#engine links table to database 
engine = create_engine(DATABASE_KEY, echo=True)
#SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/pizza")
def get_pizza():
    with Session(engine) as session:
        pizza = session.exec(select(Pizza)).all()
    return pizza

@app.post("/pizza")
def add_pizza(name:str,price:float,description:str,size:str):
    with Session(engine) as session:
        session.add(Pizza(name=name,price=price,description=description,size=size))
        session.commit()
    return "pizza added successfully"

@app.delete("/pizza")
def delete_pizza(id:int):
    with Session(engine) as session:
        session.exec(delete(Pizza).where(id== Pizza.id))
        session.commit()
    return "pizza deleted successfully"

@app.put("/pizza")
def put_pizza(id:int,name:str):
    with Session(engine) as session:
        pizza = session.exec(select(Pizza).where(id== Pizza.id)).one()
        pizza.name = name
        session.add(pizza)
        session.commit()
    return "pizza updated successfully"


@app.get("/user")
def get_User():
    with Session(engine) as session:
        user = session.exec(select(User)).all()
    return user

@app.post("/user")
def add_user(username:str,password:str):
    with Session(engine) as session:
        session.add(User(username=username,password=password))
        session.commit()
    return "user added successfully"

@app.delete("/user")
def delete_user(id:int):
    with Session(engine) as session:
        session.exec(delete(User).where(id== User.id))
        session.commit()
    return "user deleted successfully"

@app.put("/user")
def add_pizza(id:int,username:str):
    with Session(engine) as session:
        user = session.exec(select(User).where(id== User.id)).one()
    user.username = username
    session.add(user)
    session.commit()
    return "user updated successfully"

