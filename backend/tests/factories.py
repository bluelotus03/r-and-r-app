import factory
from faker import Faker

import product.models as p_models

# Faker is used to generate fake text automatically
fake = Faker()

def sanitize_slug(slug: str) -> str:
    return slug.lower().replace(' ', '-')

# a factory is an abstract usage of the models.py file
# these are default values for usage inside of the tests
# Meta tells it which model to use
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = p_models.Category

    name = "Furniture"
    slug = sanitize_slug(name)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = p_models.Product

    name = "Black Chair"
    slug = sanitize_slug(name)
    description = fake.text()
    price = 10.00
    category = factory.SubFactory(CategoryFactory)
