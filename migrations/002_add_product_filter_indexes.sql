-- Migration: add indexes for fast filtered queries

-- Composite index for common queries filtering by category_id and brand_id
drop index if exists idx_products_category_brand;
CREATE INDEX idx_products_category_brand ON products (category_id, brand_id);

-- Individual indexes (optional, often already present)
drop index if exists idx_products_category;
CREATE INDEX idx_products_category ON products (category_id);

drop index if exists idx_products_brand;
CREATE INDEX idx_products_brand ON products (brand_id);
