from typing import List, Optional
from app.models import Product # Assuming Product SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import select

class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def list_filtered(self, category_id: Optional[int] = None, brand_id: Optional[int] = None) -> List[Product]:
        query = select(Product)
        if category_id is not None:
            query = query.where(Product.category_id == category_id)
        if brand_id is not None:
            query = query.where(Product.brand_id == brand_id)
        # Explicitly order by id, or as desired
        query = query.order_by(Product.id)
        result = await self.session.execute(query)
        return result.scalars().all()

# The above method now benefits from new indexes, with no code-level filtering (all handled by the DB/indexes).