from django.test import TestCase
from geooperation_api.models import Point
from geooperation_api.geometric import GeometricOperation

class GeoTest(TestCase):
    
    # def test_geo_convert_degree_slope(self):
    #     geo=GeometricOperation
    #     slope=geo.dereceyiRadyanaCevirme(45)
    #     self.assertEqual(geo.acidanEgimBulma(slope),"Egim Bulundu")

    def test_geo_enyakinnoktayibul(self):
        geo=GeometricOperation
        nokta=geo.enyakinNoktayiBul(Point(0,0,0),[Point(7,8,9),Point(10,10,10),Point(5,4,3)])
        self.assertEqual(nokta.to_Dict(),1)
