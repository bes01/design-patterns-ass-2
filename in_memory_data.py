ITEMS = {
    {
        "id": 0,
        "name": "bread",
        "price": 1.05,
        "discount": 0
    },
    {
        "id": 1,
        "name": "beer",
        "price": 1.5,
        "discount": 0
    },
    {
        "id": 2,
        "name": "cheese",
        "price": 1.95,
        "discount": 0.1
    }
}

DISCOUNTED_COMBOS = [
    {
        "discount_name": "Bread and cheese - 20% SALE",
        "discount": 0.2,
        "items": [ITEMS[0], ITEMS[2]]
    }
]

ITEMS_BY_BATCH = [
    {
        "referenced_item": ITEMS["beer"],
        "pack_name": "6x Beer Pack",
        "quantity": 6,
        "discount": 0.1
    }
]
