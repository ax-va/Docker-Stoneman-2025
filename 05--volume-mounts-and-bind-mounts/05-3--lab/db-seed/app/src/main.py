from faker import Faker
from sqlmodel import Session, SQLModel, create_engine

from models import User

engine = create_engine("sqlite:////data/app.db")
fake = Faker()

with Session(engine) as session:
    for _ in range(10):
        user = User(
            name=fake.name(),
            email=fake.email(),
        )
        session.add(user)

    session.commit()
