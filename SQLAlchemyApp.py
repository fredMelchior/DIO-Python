from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import select
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect


Base = declarative_base()


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    address = Column(String(9))
    accounts = relationship("Account", back_populates="client")

    def __repr__(self):
        return f"Client {self.id}: name: {self.name}, cpf: {self.cpf}"


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    agency = Column(String)
    number = Column(Integer, unique=True, autoincrement=True)
    id_client = Column(Integer, ForeignKey("client.id"))
    currency = Column(Float)
    client = relationship("Client", back_populates="accounts")

    def __repr__(self):
        return f"Account {self.number} ID {self.id}:\nClient: {self.client.name},\nType: {self.type},\nAgency: {self.agency},\nCurrency: {self.currency}"


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)
insp = inspect(engine)

print(f"Tables testing: {insp.has_table('account')}")

with Session(engine) as session:
    fred = Client(
        name="Fred Melchior",
        cpf="00.079.99",
        address="abc@defg",
        accounts=[
            Account(type="C/C", agency="0001", number=1, currency=324.12),
            Account(type="Savings", agency="0001", number=2, currency=10000000.00),
        ],
    )
    roberta = Client(
        name="Roberta Pardo",
        cpf="72.1239.2",
        address="jj@ska",
        accounts=[Account(type="C/C", agency="0001", number=3, currency=321324.12)],
    )


session.add_all([fred, roberta])
session.commit()

print(f"\nClients:\n")
client_stmt = select(Client)
for user in session.scalars(client_stmt):
    print(user)

print(f"\nAccounts:\n")
accounts_stmt = select(Account)
for acc in session.scalars(accounts_stmt):
    print(acc)

join_stmt = select(Client.name, Account.type).join_from(Client, Account)

connection = engine.connect()
results = connection.execute(join_stmt).fetchall()
for r in results:
    print(r)
