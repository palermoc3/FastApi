from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    
    __table_args__ = {'extend_existing': True}
       
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable = False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates = 'categoria')

