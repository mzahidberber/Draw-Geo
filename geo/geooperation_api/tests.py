from django.test import TestCase
from geooperation_api.geometric import GeometricOperation

class GeoTest(TestCase):
    
    def test_geo_convert_degree_slope(self):
        geo=GeometricOperation
        slope=geo.dereceyiRadyanaCevirme(45)
        self.assertEqual(geo.acidanEgimBulma(slope),"Egim Bulundu")
