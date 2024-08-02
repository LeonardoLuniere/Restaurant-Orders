from src.models.ingredient import Restriction, Ingredient


def test_ingredient():
    ingrediente_testado = Ingredient("presunto")
    assert ingrediente_testado.name == "presunto"
    assert ingrediente_testado.restrictions == {
            Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT
            }
    assert ingrediente_testado.__hash__() == hash("presunto")
    assert ingrediente_testado.__eq__(Ingredient("presunto"))
    assert not ingrediente_testado.__eq__(Ingredient("queijo"))
    assert ingrediente_testado.__repr__() == "Ingredient('presunto')"
