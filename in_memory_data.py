ITEMS = [
    {
        "name": "bread",
        "price": 1.05,
        "discount": 0
    },
    {
        "name": "beer",
        "price": 1.5,
        "discount": 0.33
    },
    {
        "name": "cheese",
        "price": 1.95,
        "discount": 0.1
    }
]

DISCOUNTED_COMBOS = [
    {
        "name": "Bread and cheese (20% SALE)",
        "discount": 0.4,
        "items": [ITEMS[0], ITEMS[2]]
    }
]

ITEMS_BY_BATCH = [
    {
        "referenced_item": ITEMS[1],
        "name": "6x Beer Pack",
        "quantity": 6,
        "discount": 0.5
    }
]
