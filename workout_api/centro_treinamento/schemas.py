from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do CT', example='CT King James', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do CT', example='Rua Tal, 123', max_length=60)]
    proprietario: Annotated[str, Field(description='Dono do CT', example='James', max_length=30)]