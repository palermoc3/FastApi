from pydantic import BaseModel, Field, PositiveFloat

class BaseSchema(BaseModel):
    class Config:   
        extra = 'forbid'
        from_attributes = True