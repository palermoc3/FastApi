from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples ='maracana', max_length=50)]
    endereco: Annotated[str, Field(description='Nome do endereco', examples ='rua dos bobos', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario', examples ='adriano', max_length=30)]