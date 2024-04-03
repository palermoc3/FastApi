from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', examples ='crossfit', max_length=20)]

