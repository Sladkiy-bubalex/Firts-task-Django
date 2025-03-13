import pytest
from rest_framework.test import APIClient 
from logistic.models import Product, Stock
from model_bakery import baker


BASE_URL = 'http://localhost:8000/api/v1'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def product_factory():
    def factory(*args, **kwargs):
        return baker.make(Product, *args, **kwargs)

    return factory

@pytest.fixture
def stock_factory():
    def factory(*args, **kwargs):
        return baker.make(Stock, *args, **kwargs)
    
    return factory


@pytest.mark.django_db
def test_create_product(client, product_factory):
    products = product_factory(_quantity=3)
    response = client.get(f'{BASE_URL}/products/{products[1].id}/')
    data = response.json()

    assert data['title'] == products[1].title