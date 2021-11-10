from pytest import fixture
import product.models as p_models
from datetime import datetime
from pytest_factoryboy import register
from factories import CategoryFactory, ProductFactory
from typing import List
from faker import Faker

# registering to use these factories 
# category_factory
register(CategoryFactory)
# product_factory
register(ProductFactory)
fake = Faker()

# fixtures are reusable components for tests
# a fixture for a category (default - Furniture)
@fixture
def new_category_1(db, category_factory) -> p_models.Category:
    return category_factory.create()

# a fixture for a product
@fixture
def new_product_1(db, new_category_1, product_factory) -> p_models.Product:
    return product_factory.create()

# a fixture for a list of products
@fixture
def multiple_products(db, new_category_1, product_factory) -> List[p_models.Product]:
    clothes_cat = p_models.Category.objects.create(name="Clothes", slug="clothes")
    items = {
        "Multicolored Sneakers",
        "Red Sneakers",
        "Gray Wool Socks",
        "Christmas Socks",
        "VA RVCA Hat",
        "Wool Knit Sweater"
    }
    products = []
    for item in items:
        products.append(
            p_models.Product.objects.create(
                name = item,
                slug = item.lower(),
                category = clothes_cat,
                price=10.00,
                description=fake.text()
            )
        )
    
    return products

@fixture
def base_url():
    return '/api/v1'