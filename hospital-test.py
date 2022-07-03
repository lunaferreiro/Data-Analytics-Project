import unittest

from hospital import Hospital

####################################################################
h1: Hospital = Hospital('HOSP. ODONTOLOGICO CARRILLO', 'SANCHEZ DE BUSTAMANTE', "2529", 'C1425DUY', -34.5845283357505, -58.4027276547828)
h2: Hospital = Hospital('HOSP. MOYANO', 'BRANDSEN', "2570", 'C1287ABJ', -34.6394041316484, -58.3851559118889)
h3: Hospital = Hospital('HOSP. UDAONDO', 'CASEROS', "2061", 'C1264AAA', -34.6341535760002, -58.3913114406535)
h4: Hospital = Hospital('INST. PASTEUR', 'DIAZ VELEZ', "4821", 'C1405DCD', -34.6084721257413, -58.4349433479819)
h5: Hospital = Hospital('HOSP. FERRER', 'DOCTOR ENRIQUE FINOCHIETTO', "849", 'C1272AAA', -34.6302112044495, -58.3758433488021)
h6: Hospital = Hospital('HOSP. TOBAR GARCIA', 'DOCTOR RAMON CARRILLO', "315", 'C1275AHG', -34.6357022351559, -58.3823284509488)
h7: Hospital = Hospital('HOSP. BORDA', 'DOCTOR RAMON CARRILLO', "375", 'C1275AHG', -34.6364350546569, -58.3821283746958)

class TestHospital(unittest.TestCase):

    def test_nombre_de_hospital(self):
        self.assertEqual(h1.nombre, 'HOSP. ODONTOLOGICO CARRILLO')
        self.assertEqual(h2.nombre, 'HOSP. MOYANO')
        self.assertEqual(h3.nombre, 'HOSP. UDAONDO')
        self.assertEqual(h4.nombre, 'INST. PASTEUR')
        self.assertEqual(h5.nombre, 'HOSP. FERRER')
        self.assertEqual(h6.nombre, 'HOSP. TOBAR GARCIA')
        self.assertEqual(h7.nombre, 'HOSP. BORDA')

    def test_calle_nombre_de_hospital(self):
        self.assertEqual(h1.calle_nombre, 'SANCHEZ DE BUSTAMANTE')
        self.assertEqual(h2.calle_nombre, 'BRANDSEN')
        self.assertEqual(h3.calle_nombre, 'CASEROS')
        self.assertEqual(h4.calle_nombre, 'DIAZ VELEZ')
        self.assertEqual(h5.calle_nombre, 'DOCTOR ENRIQUE FINOCHIETTO')
        self.assertEqual(h6.calle_nombre, 'DOCTOR RAMON CARRILLO')
        self.assertEqual(h7.calle_nombre, 'DOCTOR RAMON CARRILLO')
        
    def test_calle_altura_de_hospital(self):
        self.assertEqual(h1.calle_altura, "2529")
        self.assertEqual(h2.calle_altura, "2570")
        self.assertEqual(h3.calle_altura, "2061")
        self.assertEqual(h4.calle_altura, "4821")
        self.assertEqual(h5.calle_altura, "849")
        self.assertEqual(h6.calle_altura, "315")
        self.assertEqual(h7.calle_altura, "375")

    def test_cpa_de_hospital(self):
        self.assertEqual(h1.cpa, 'C1425DUY')
        self.assertEqual(h2.cpa, 'C1287ABJ')
        self.assertEqual(h3.cpa, 'C1264AAA')
        self.assertEqual(h4.cpa, 'C1405DCD')
        self.assertEqual(h5.cpa, 'C1272AAA')
        self.assertEqual(h6.cpa, 'C1275AHG')
        self.assertEqual(h7.cpa, 'C1275AHG')

    def test_latitud_de_hospital(self):
        self.assertEqual(h1.latitud, -34.5845283357505)
        self.assertEqual(h2.latitud, -34.6394041316484)
        self.assertEqual(h3.latitud, -34.6341535760002)
        self.assertEqual(h4.latitud, -34.6084721257413)
        self.assertEqual(h5.latitud, -34.6302112044495)
        self.assertEqual(h6.latitud, -34.6357022351559)
        self.assertEqual(h7.latitud, -34.6364350546569)
        
    def test_longitud_de_hospital(self):
        self.assertEqual(h1.longitud, -58.4027276547828)
        self.assertEqual(h2.longitud, -58.3851559118889)
        self.assertEqual(h3.longitud, -58.3913114406535)
        self.assertEqual(h4.longitud, -58.4349433479819)
        self.assertEqual(h5.longitud, -58.3758433488021)
        self.assertEqual(h6.longitud, -58.3823284509488)
        self.assertEqual(h7.longitud, -58.3821283746958)

    def test_direccion_de_hospital(self):
        self.assertEqual(h1.direccion(), 'SANCHEZ DE BUSTAMANTE 2529 (C1425DUY)')
        self.assertEqual(h2.direccion(), 'BRANDSEN 2570 (C1287ABJ)')
        self.assertEqual(h3.direccion(), 'CASEROS 2061 (C1264AAA)')
        self.assertEqual(h4.direccion(), 'DIAZ VELEZ 4821 (C1405DCD)')
        self.assertEqual(h5.direccion(), 'DOCTOR ENRIQUE FINOCHIETTO 849 (C1272AAA)')
        self.assertEqual(h6.direccion(), 'DOCTOR RAMON CARRILLO 315 (C1275AHG)')
        self.assertEqual(h7.direccion(), 'DOCTOR RAMON CARRILLO 375 (C1275AHG)')
        
    def test_repr_hospital(self):
         self.assertEqual(str(h1), 'HOSP. ODONTOLOGICO CARRILLO--SANCHEZ DE BUSTAMANTE 2529 (C1425DUY)')
         self.assertEqual(str(h2), 'HOSP. MOYANO--BRANDSEN 2570 (C1287ABJ)')
         self.assertEqual(str(h3), 'HOSP. UDAONDO--CASEROS 2061 (C1264AAA)')
         self.assertEqual(str(h4), 'INST. PASTEUR--DIAZ VELEZ 4821 (C1405DCD)')
         self.assertEqual(str(h5), 'HOSP. FERRER--DOCTOR ENRIQUE FINOCHIETTO 849 (C1272AAA)')
         self.assertEqual(str(h6), 'HOSP. TOBAR GARCIA--DOCTOR RAMON CARRILLO 315 (C1275AHG)')
         self.assertEqual(str(h7), 'HOSP. BORDA--DOCTOR RAMON CARRILLO 375 (C1275AHG)')


    
####################################################################

unittest.main()
