from celdas import celda

class Magnitudes:
    def __init__(self, magnitudes):
        self.unidades_est = 0 # Rango en el que se deben dividir las magnitudes relativas
        self.magnitud_est = 0
        self.magnitud_rel = 0
        
        self.data = []
        
        for magnitud in magnitudes:
            if magnitud[1] == True:
                self.magnitud_est += 1
                self.unidades_est += magnitud[celda.VALOR]
            else:
                self.magnitud_rel += 1
            self.data.append([magnitud[celda.VALOR],magnitud[celda.TIPO]])
            
    def calc_magnitud_bruta(self, unidades):
        """
        Cálcula la magnitud de las celdas en base a su dimension relativa
        """
        rango = (unidades - self.unidades_est)
        magnitudes_brutas = []
        residuo = 0.0
        
        for magnitud in self.data:
            if magnitud[celda.TIPO] == celda.TIPO_ESTATICO:
                magnitudes_brutas.append(magnitud[celda.VALOR])
            else:
                valor_f = rango * magnitud[celda.VALOR]
                valor_r = round(valor_f + residuo)
                residuo = valor_f - valor_r
                magnitudes_brutas.append(valor_r)
                
        return magnitudes_brutas