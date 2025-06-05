from enum import Enum


class IngredientType(Enum):
    """Tags for ingredients fields."""
    salt_percentage = "Salt (%)"
    oil_percentage = "Oil (%)"
    yeast_type = "Yeast Type"
    hydration = "Hydration (%)"
    number_of_balls = "Number of Balls"
    ball_weight = "Ball Weight (g)"


class ItemType(Enum):
    flour = "Flour"
    sauce = "Sauce"
    topping = "Topping"


class TabItem(Enum):
    flour = "Flour"
    quantities = "Quantities"
    balls = "Ball(s)"


