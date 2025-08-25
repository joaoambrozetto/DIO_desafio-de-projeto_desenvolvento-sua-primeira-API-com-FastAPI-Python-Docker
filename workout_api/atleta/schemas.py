from typing import Annotated

from pydantic import BaseModel, Field, PositiveFloat


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=31)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta em kg', examples=110.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta em m', examples=1.82)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='M', max_length=1)]