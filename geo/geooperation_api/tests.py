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
        nokta=geo.merkezveYaricapBul(Point(10,0,1),Point(5,5,1),Point(3,10,1))
        print(nokta[0].X,"----",nokta[0].Y,"---",nokta[1])
        # self.assertEqual(nokta.to_Dict(),1)
