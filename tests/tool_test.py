# -*- coding: UTF-8 -*-
import mlproject
from mlproject.tools import haversine_2
import pytest

def test_haversine_2():
    lat1, lat2, lon1, lon2 = 48.865070, 2.380009, 48.235070, 2.393409
    distance = haversine_2(lat1, lat2, lon1, lon2)
    assert distance == 70.00789153218594
