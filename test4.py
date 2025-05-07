from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str
    @field_validator('username')
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters')
        return value

class SignUpData(BaseModel):
    password: str
    confirm_password:str

    @model_validator(mode='after')
    def check_paswords(cls, value):
        if(value['password'] != value['confirm_password']):
            raise ValueError('password doesnt match')
        return value
    
class Profuct(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def calculate_price(cls, value):
        return value['price'] * value['quantity']