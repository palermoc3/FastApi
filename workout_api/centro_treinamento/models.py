from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centro_treinamento'
 
    __table_args__ = {'extend_existing': True}
    
    pk_id : Mapped[int] = mapped_column(Integer, primary_key=True)
    nome : Mapped[str] = mapped_column(String(20), unique=True, nullable = False)
    endereco : Mapped[str] = mapped_column(String(30), nullable = False)
    proprietario : Mapped[str] = mapped_column(String(60), nullable = False)
    atleta : Mapped['AtletaModel'] = relationship(back_populates = 'centro_treinamento')
