from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atelta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples ='alex', max_length=50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', examples ='16489301711', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples ='24')]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples ='72.1')]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples ='1.70')]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples ='M', max_length=1)]