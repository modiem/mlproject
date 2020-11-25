from mlproject.tools import imp_haversine
from mlproject.distance import haversine

def test_haversine():
    assert haversine(48.865, 2.380, 48.235, 2.393) == imp_haversine(48.865, 2.380, 48.235, 2.393)

