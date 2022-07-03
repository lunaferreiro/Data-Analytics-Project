import unittest

from dataset import DataSetSanitario
from hospital import Hospital
from farmacia import Farmacia

####################################################################
d1:DataSetSanitario = DataSetSanitario(farmacias_filename='farmacias_test.csv', hospitales_filename='hospitales_test.csv')


class TestDataSetSanitario(unittest.TestCase):

    def test_lista_farmacias(self):
        self.assertEqual(str(d1.farmacias), '[FARMACIA:AV LOPE DE VEGA 1397 (C1407BNM), FARMACIA:AV JUAN B. JUSTO 4995 (C1416DKD), FARMACIA:GUEMES 3002 (C1425BKD), FARMACIA:CARHUE 40 (C1408GBB), FARMACIA:AV ALVAREZ JONTE 4886 (C1407GPP), FARMACIA:AV JUAN B. JUSTO 5391 (C1416DKH), FARMACIA:AV ELCANO 3901 (C1427CHD), FARMACIA:AV MONROE 3195 (C1428BMA), FARMACIA:DOBLAS 228 (C1424BLF)]')
    
    def test_lista_hospitales(self):
        self.assertEqual(str(d1.hospitales), '[HOSP. DE ELIZALDE--MANUEL A. MONTES DE OCA 40 (C1270AAN), HOSP. GUTIERREZ--GALLO 1330 (C1425EFD), HOSP. ODONTOLOGICO CARRILLO--SANCHEZ DE BUSTAMANTE 2529 (C1425DUY), HOSP. MOYANO--BRANDSEN 2570 (C1287ABJ), HOSP. UDAONDO--CASEROS 2061 (C1264AAA), INST. PASTEUR--DIAZ VELEZ 4821 (C1405DCD), HOSP. FERRER--DOCTOR ENRIQUE FINOCHIETTO 849 (C1272AAA), HOSP. TOBAR GARCIA--DOCTOR RAMON CARRILLO 315 (C1275AHG), HOSP. BORDA--DOCTOR RAMON CARRILLO 375 (C1275AHG)]')
   
    def test_nombres_de_hospitales(self):
        self.assertEqual(d1.nombres_de_hospitales(), ['HOSP. BORDA', 'HOSP. DE ELIZALDE', 'HOSP. FERRER', 'HOSP. GUTIERREZ', 'HOSP. MOYANO', 'HOSP. ODONTOLOGICO CARRILLO', 'HOSP. TOBAR GARCIA', 'HOSP. UDAONDO', 'INST. PASTEUR'])
    
    def test_hospital_por_nombre(self):
        self.assertEqual(str(d1.hospital_por_nombre('HOSP. DE ELIZALDE')), 'HOSP. DE ELIZALDE--MANUEL A. MONTES DE OCA 40 (C1270AAN)')
        self.assertEqual(str(d1.hospital_por_nombre('HOSP. BORDA')), 'HOSP. BORDA--DOCTOR RAMON CARRILLO 375 (C1275AHG)')
        self.assertEqual(str(d1.hospital_por_nombre('HOSP. FERRER')), 'HOSP. FERRER--DOCTOR ENRIQUE FINOCHIETTO 849 (C1272AAA)')
        self.assertEqual(str(d1.hospital_por_nombre('HOSP. GUTIERREZ')), 'HOSP. GUTIERREZ--GALLO 1330 (C1425EFD)')
        self.assertEqual(str(d1.hospital_por_nombre('HOSP. MOYANO')), 'HOSP. MOYANO--BRANDSEN 2570 (C1287ABJ)')
    
    def test_farmacia_mas_cercana(self):
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[0])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[1])), 'FARMACIA:GUEMES 3002 (C1425BKD)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[2])), 'FARMACIA:GUEMES 3002 (C1425BKD)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[3])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[4])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[5])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[6])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[7])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        self.assertEqual(str(d1.farmacia_mas_cercana(d1.hospitales[8])), 'FARMACIA:DOBLAS 228 (C1424BLF)')
        
    def test_farmacia_por_hospital(self):
        self.assertAlmostEqual(str(d1.farmacia_por_hospital()), '{HOSP. DE ELIZALDE--MANUEL A. MONTES DE OCA 40 (C1270AAN): (FARMACIA:DOBLAS 228 (C1424BLF), 5030.634724190659), HOSP. GUTIERREZ--GALLO 1330 (C1425EFD): (FARMACIA:GUEMES 3002 (C1425BKD), 370.27815066753567), HOSP. ODONTOLOGICO CARRILLO--SANCHEZ DE BUSTAMANTE 2529 (C1425DUY): (FARMACIA:GUEMES 3002 (C1425BKD), 1004.6841274120635), HOSP. MOYANO--BRANDSEN 2570 (C1287ABJ): (FARMACIA:DOBLAS 228 (C1424BLF), 4782.788938434082), HOSP. UDAONDO--CASEROS 2061 (C1264AAA): (FARMACIA:DOBLAS 228 (C1424BLF), 4018.4894417998003), INST. PASTEUR--DIAZ VELEZ 4821 (C1405DCD): (FARMACIA:DOBLAS 228 (C1424BLF), 1229.3681749832713), HOSP. FERRER--DOCTOR ENRIQUE FINOCHIETTO 849 (C1272AAA): (FARMACIA:DOBLAS 228 (C1424BLF), 5217.096103913466), HOSP. TOBAR GARCIA--DOCTOR RAMON CARRILLO 315 (C1275AHG): (FARMACIA:DOBLAS 228 (C1424BLF), 4840.980778377542), HOSP. BORDA--DOCTOR RAMON CARRILLO 375 (C1275AHG): (FARMACIA:DOBLAS 228 (C1424BLF), 4889.439319116645)}')
        
####################################################################

unittest.main()
