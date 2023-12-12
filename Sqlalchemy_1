""" Primeira Integração de Banco de dados em Python """

import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy import select
Base = declarative_base()

""" Classe para definir atributos do Cliente a ser manipuldado. """
class Cliente(Base):
    
    
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    email_address = Column(String(30), nullable=False)
    endereco = relationship(
        "Conta", back_populates="user_client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id = {self.id}, nome = {self.nome}, cpf = {self.cpf})"


""" Classe para ser manipulada pelo com os atributos do Cliente a ser referenciada no Banco de Dados """
class Conta(Base):
    
     
    __tablename__ = "endereco"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    id_cliente = Column(Integer, ForeignKey("user.id"), nullable=False)
    agencia = Column(String)
    num = Column(String)
    user_client = relationship("Cliente", back_populates="endereco")

    def __repr__(self):
        return f"Conta (id = {self.id}, tipo = {self.tipo}, agencia = {self.agencia}, num = {self.num})"

""" Terminei de referencia as classes """

# Conexão com o banco de dados

engine = create_engine("sqlite://")

# Criando as classe como tabelas no banco de dados
Base.metadata.create_all(engine)

#print(engine.table_name())

# Investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    erickson_conta = Conta(
        tipo = 'Corrente',
        agencia = '12345',
        num = '(33)98645727'
    )

    erickson = Cliente(
        nome = 'Erickson Alves Costa',
        cpf = '143.411.466-02',
        email_address = 'erickson@email.com',  # Fornecer um valor para email_address
        endereco = [erickson_conta]
    )

    natalia_conta = Conta(
        tipo = 'Poupança',
        agencia = '67890',
        num = '(33)98456151'
    )

    natalia = Cliente(
        nome = 'Natalia Andressa Dos Reis',
        cpf = '122.455.457-88',
        email_address = 'natalia@email.com',  # Fornecer um valor para email_address
        endereco = [natalia_conta]
    )

    session.add_all([erickson_conta, erickson, natalia_conta, natalia])
    session.commit()
    # enviando para o banco de dados(persistecia de dados)



stmt = select(Cliente).where(Cliente.nome.in_(["erickson", "natalia"]))
print("\nRecuperando Usuarios")
for user in session.execute(stmt).scalars():
    print(user)

stmt_endereco = select(Conta).where(Conta.id_cliente.in_([2]))
print("\nRecuperando a Conta do usuarios")
for endereco in session.scalars(stmt_endereco):
    print(endereco)

stmt_order = select(Cliente).order_by(Cliente.cpf.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(Cliente.cpf, Cliente.email_address).join_from(Conta, Conta.user_client)
print("\n")
for result in session.scalars(stmt_join):
    print(result)

#print(select(User.fullname, Address.email_address).join_from(Address, User))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\n")
for result in results:
    print(result)
