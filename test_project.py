import pytest
from project import FridgeFreezer, Cupboard, Recipie

@pytest.fixture
def fridge():
    return FridgeFreezer()

@pytest.fixture
def cupboard():
    return Cupboard()

@pytest.fixture
def recipie():
    return Recipie('Pancakes')

def test_food_item(fridge):
    item = {'Item': 'Milk', 'Quantity': 1, 'Measurment': 'liter'}
    fridge.foodItem = item
    items = fridge.FetchItems()
    assert len(items) == 1
    assert items[0] == item

def test_save_load_content(fridge):
    item1 = {'Item': 'Eggs', 'Quantity': 12, 'Measurment': 'ind'}
    item2 = {'Item': 'Butter', 'Quantity': 200, 'Measurment': 'grams'}
    fridge.foodItem = item1
    fridge.foodItem = item2
    fridge.SaveContent()
    fridge_loaded = FridgeFreezer()
    fridge_loaded.LoadContent()
    loaded_items = fridge_loaded.FetchItems()
    assert len(loaded_items) == 2
    assert loaded_items[0] == item1
    assert loaded_items[1] == item2

def test_check_ingredients(fridge):
    item1 = {'Item': 'Flour', 'Quantity': 500, 'Measurment': 'grams'}
    item2 = {'Item': 'Sugar', 'Quantity': 200, 'Measurment': 'grams'}
    item3 = {'Item': 'Milk', 'Quantity': 1, 'Measurment': 'liter'}
    fridge.foodItem = item1
    fridge.foodItem = item2
    assert fridge.checkIngredients('Flour', 400)
    assert not fridge.checkIngredients('Sugar', 300)
    assert not fridge.checkIngredients('Milk', 2)
    assert not fridge.checkIngredients('Salt', 100)

def test_subtract_ingredients(fridge):
    item1 = {'Item': 'Flour', 'Quantity': 500, 'Measurment': 'grams'}
    item2 = {'Item': 'Sugar', 'Quantity': 200, 'Measurment': 'grams'}
    fridge.foodItem = item1
    fridge.foodItem = item2
    fridge.subtractIngredients('Flour', 100)
    fridge.subtractIngredients('Sugar', 150)
    items = fridge.FetchItems()
    assert items[0]['Quantity'] == 400
    assert items[1]['Quantity'] == 50


if __name__ == '__main__':
    pytest.main()
