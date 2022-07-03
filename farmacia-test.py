import unittest

from farmacia import Farmacia

####################################################################
f1:Farmacia = Farmacia('AV LOPE DE VEGA', '1397', 'C1407BNM', -34.6268150764954, -58.5080720511654)
f2:Farmacia = Farmacia('AV JUAN B. JUSTO', '4995', 'C1416DKD', -34.6117065912837, -58.4689759825657)
f3:Farmacia = Farmacia('GUEMES', '3002', 'C1425BKD', -34.5917612010672, -58.4093052805893)
f4:Farmacia = Farmacia('CARHUE', '40', 'C1408GBB', -34.6396159502234, -58.5248211025968)
f5:Farmacia = Farmacia('AV ALVAREZ JONTE', '4886', 'C1407GPP', -34.6204290376584, -58.5066499006764)
f6:Farmacia = Farmacia('AV JUAN B. JUSTO', '5391', 'C1416DKH', -34.6147341624871, -58.4730685276207)
f7:Farmacia = Farmacia('AV ELCANO', '3901', 'C1427CHD', -34.5819643320509, -58.4607373411615)

class TestFarmacia(unittest.TestCase):
    def test_calle_nombre_de_farmacia(self):
        self.assertEqual(f1.calle_nombre, 'AV LOPE DE VEGA')
        self.assertEqual(f2.calle_nombre, 'AV JUAN B. JUSTO')
        self.assertEqual(f3.calle_nombre, 'GUEMES')
        self.assertEqual(f4.calle_nombre, 'CARHUE')
        self.assertEqual(f5.calle_nombre, 'AV ALVAREZ JONTE')
        self.assertEqual(f6.calle_nombre, 'AV JUAN B. JUSTO')
        self.assertEqual(f7.calle_nombre, 'AV ELCANO')
        
    def test_calle_altura_de_farmacia(self):
        self.assertEqual(f1.calle_altura, '1397')
        self.assertEqual(f2.calle_altura, '4995')
        self.assertEqual(f3.calle_altura, '3002')
        self.assertEqual(f4.calle_altura, '40')
        self.assertEqual(f5.calle_altura, '4886')
        self.assertEqual(f6.calle_altura, '5391')
        self.assertEqual(f7.calle_altura, '3901')
    
    def test_cpa_de_farmacia(self):
        self.assertEqual(f1.cpa, 'C1407BNM')
        self.assertEqual(f2.cpa, 'C1416DKD')
        self.assertEqual(f3.cpa, 'C1425BKD')
        self.assertEqual(f4.cpa, 'C1408GBB')
        self.assertEqual(f5.cpa, 'C1407GPP')
        self.assertEqual(f6.cpa, 'C1416DKH')
        self.assertEqual(f7.cpa, 'C1427CHD')
        
    def test_latitud_de_farmacia(self):
        self.assertEqual(f1.latitud, -34.6268150764954)
        self.assertEqual(f2.latitud, -34.6117065912837)
        self.assertEqual(f3.latitud, -34.5917612010672)
        self.assertEqual(f4.latitud, -34.6396159502234)
        self.assertEqual(f5.latitud, -34.6204290376584)
        self.assertEqual(f6.latitud, -34.6147341624871)
        self.assertEqual(f7.latitud, -34.5819643320509)

    def test_longitud_de_farmacia(self):
        self.assertEqual(f1.longitud, -58.5080720511654)
        self.assertEqual(f2.longitud, -58.4689759825657)
        self.assertEqual(f3.longitud, -58.4093052805893)
        self.assertEqual(f4.longitud, -58.5248211025968)
        self.assertEqual(f5.longitud, -58.5066499006764)
        self.assertEqual(f6.longitud, -58.4730685276207)
        self.assertEqual(f7.longitud, -58.4607373411615)

    def test_direccion_de_farmacia(self):
        self.assertEqual(f1.direccion(), 'AV LOPE DE VEGA 1397 (C1407BNM)')
        self.assertEqual(f2.direccion(), 'AV JUAN B. JUSTO 4995 (C1416DKD)')
        self.assertEqual(f3.direccion(), 'GUEMES 3002 (C1425BKD)')
        self.assertEqual(f4.direccion(), 'CARHUE 40 (C1408GBB)')
        self.assertEqual(f5.direccion(), 'AV ALVAREZ JONTE 4886 (C1407GPP)')
        self.assertEqual(f6.direccion(), 'AV JUAN B. JUSTO 5391 (C1416DKH)')
        self.assertEqual(f7.direccion(), 'AV ELCANO 3901 (C1427CHD)')
    
    def test_distancia_de_farmacia(self):
        self.assertAlmostEqual(f1.distancia(-34.6102617943773, -58.3988675193096), 10161.22, places=1)
        self.assertAlmostEqual(f2.distancia(-34.6102617943773, -58.3988675193096), 6418.1, places=1)
        self.assertAlmostEqual(f3.distancia(-34.6102617943773, -58.3988675193096), 2268.18, places=1)
        self.assertAlmostEqual(f4.distancia(-34.6102617943773, -58.3988675193096), 11978.20, places=1)
        self.assertAlmostEqual(f5.distancia(-34.6102617943773, -58.3988675193096), 9927.94, places=1)
        self.assertAlmostEqual(f6.distancia(-34.6102617943773, -58.3988675193096), 6808.68, places=1)
        self.assertAlmostEqual(f7.distancia(-34.6102617943773, -58.3988675193096), 6478.56, places=1)
    
    def test_repr_farmacia(self):
        self.assertEqual(str(f1), 'FARMACIA:AV LOPE DE VEGA 1397 (C1407BNM)')
        self.assertEqual(str(f2), 'FARMACIA:AV JUAN B. JUSTO 4995 (C1416DKD)')
        self.assertEqual(str(f3), 'FARMACIA:GUEMES 3002 (C1425BKD)')
        self.assertEqual(str(f4), 'FARMACIA:CARHUE 40 (C1408GBB)')
        self.assertEqual(str(f5), 'FARMACIA:AV ALVAREZ JONTE 4886 (C1407GPP)')
        self.assertEqual(str(f6), 'FARMACIA:AV JUAN B. JUSTO 5391 (C1416DKH)')
        self.assertEqual(str(f7), 'FARMACIA:AV ELCANO 3901 (C1427CHD)')
        



        

        

        

        


    



## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
