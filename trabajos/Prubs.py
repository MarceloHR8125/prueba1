"""""
test driven develovement

desarrolllo basadoo en pruebas

Escribe una prueba para caracteristicas nuevas o que falle

escribe codigo para hacer que pase la prueba

refactorizar el codigo como sea necesario

 herramienta para poder testear codigos de forma automatica  pgtest
"""""
from realizados import repetidos
import pytest

def te_bas():
    assert repetidos([1, 2, 3, 1]) == True
    assert repetidos([1, 2, 3]) == False


@pytest.mark.parametrize("nums, res",
                         [([1,2,3,1], True),
                          ([1,2,3], False),
                          ([1,3,3,4], True), ])

def te_basmetrik(nums, res):
    assert repetidos(nums) == res
