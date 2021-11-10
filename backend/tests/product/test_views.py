from pytest import mark, fixture
from django.urls import reverse, path
from django.contrib import admin
from product import views
import product.models as p_models


class Category_Tests:
    @fixture
    def category_base(self, base_url):
        return f'{base_url}/products'

    # testing the url of the category to check api is working as expected
    def test_category(self, client, category_base, new_category_1):
        response = client.get(f'{category_base}/{new_category_1.slug}/')
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == new_category_1.name
        assert data["get_absolute_url"] == f'/{new_category_1.slug}/'

    # checking that is getting more than one object 
    def test_multiple(self, client, category_base, multiple_products):
        response = client.get(f'{category_base}/{multiple_products[0].category.slug}/')
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0

class Latest_Products_Tests:
    @fixture
    def latest_base(self, base_url):
        return f'{base_url}/latest-products/'
    
    @fixture
    def product_base(self, base_url):
        return f'{base_url}/products'

    def test_single_product_list_latest(self, client, latest_base, new_product_1):
        response = client.get(latest_base)
        assert response.status_code == 200
        data = response.json()[0]
        assert data["name"] == new_product_1.name
        assert data["get_absolute_url"] == f'/{new_product_1.category.slug}/{new_product_1.slug}/'
    
    def test_multiple_product_list(self, client, latest_base, multiple_products):
        all_db_stuff = p_models.Product.objects.all()
        assert len(all_db_stuff) == 6

    # checks the details of a single product 
    def test_single_product(self, client, product_base, new_product_1):
        response = client.get(f'{product_base}/{new_product_1.category.slug}/{new_product_1.slug}/')
        assert response.status_code == 200
        data = response.json()
        
        assert data["name"] and (len(data["name"]) > 0)
        assert float(data["price"]) >= 0
        assert data["description"] and (len(data["description"]) > 0)

class Search_Tests:

    @fixture
    def search_base(self, base_url):
        return f'{base_url}/products/search'

    def test_search(self, client, search_base, new_product_1):
        response = client.post(f'{search_base}/', { 'query': 'chair'})
        assert response.status_code == 200
        data = response.json()
        # ensures that something was returned from search
        assert len(data) > 0

    def test_fail_search(self, client, search_base, new_product_1):
        response = client.post(f'{search_base}/', { 'query': 'pencil'})
        assert response.status_code == 200
        data = response.json()
        # ensures that nothing was returned from search
        assert len(data) == 0