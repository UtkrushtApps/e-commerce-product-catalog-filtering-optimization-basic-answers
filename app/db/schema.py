from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    category_id: int
    brand_id: int
    price: float
    # ...

    # No need to add explicit sqlmodel indexes here, we create them as native SQL for more control
