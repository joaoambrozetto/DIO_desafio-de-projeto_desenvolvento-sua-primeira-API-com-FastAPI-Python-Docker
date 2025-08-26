from typing import Annotated

from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=31)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta em kg', example=110.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta em m', example=1.82)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]