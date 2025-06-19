import pytest


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone", "brand": "apple", "price": "100", "rating": "1"},
        {"name": "galaxy", "brand": "samsung", "price": "200", "rating": "2"},
        {"name": "redmi", "brand": "xiaomi", "price": "300", "rating": "3"},
        {"name": "poco", "brand": "xiaomi", "price": "400", "rating": "4"},
    ]
