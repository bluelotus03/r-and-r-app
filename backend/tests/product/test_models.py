from django.test import TestCase
import product.models as p_models
from pytest import mark


class Category_Tests:

    def test_name(self, new_category_1):
        assert new_category_1.name == "Furniture"

    def test_slug(self, new_category_1):
        assert new_category_1.slug == 'furniture'

    def test_get_absolute_url(self, new_category_1):
        assert p_models.Category.get_absolute_url(new_category_1) == '/furniture/'

class Product_Tests:

    def test_name(self, new_product_1):
        assert new_product_1.name == "Black Chair"

    def test_slug(self, new_product_1):
        assert new_product_1.slug == "black-chair"


# @mark.product_product
# def test_product_get_absolute_url(new_product_1):
#     new_product_1.
#     assert f'/{new_product_1.category.slug}/{new_product_1.slug}/' == "/furniture/chair/"