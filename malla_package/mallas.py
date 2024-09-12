from magnitudes_package.magnitudes import Magnitudes

class Malla:
    """
    Clase Malla - Permite dividir la ventana de la terminal en celdas, similar a una tabla o un documento de Excel.

    Parámetros:
    ___________
    magnitud_filas : list
        Lista que contiene la cantidad de filas a crear en la terminal. 
        Cada elemento es una lista donde el campo [0] es el valor (en porcentaje o estático) 
        y el campo [1] indica el tipo de valor (True para estático, False para relativo).
        
    magnitud_columnas : list
        Lista que contiene la cantidad de columnas a crear en la terminal. 
        Cada elemento es una lista donde el campo [0] es el valor (en porcentaje o estático) 
        y el campo [1] indica el tipo de valor (True para estático, False para relativo).
        
    unidades_lineas : int
        Cantidad de lineas existentes en la terminal.
        
    unidades_columnas : int
        Cantidad de columnas existentes en la terminal.
        
    Atributos:
    __________
    magnitud_rel : list
        Lista que contiene el valor de los parametros magnitud_filas y magnitud_columnas.
    
    columnas : int
        Cantidad de columnas que contiene la terminal.
        
    lineas : int
        Cantidad de lineas que tiene la terminal.
        
    celdas_y : list
    celdas_x : list
        Es una lista que contiene los valores de inicio y fin para cada celda del eje correspondiente.
        Cada elemento es una lista donde el campo [0] es donde inicia esa celda y el campo [1] es donde termina.
    """
    def __init__(self, magnitud_filas, magnitud_columnas, unidades_lineas, unidades_columnas):
        self.magnitud_rel = [magnitud_filas, magnitud_columnas] # Pienso cambiar esto pronto
        self.columnas = unidades_columnas # Cantidad de columnas en la terminal
        self.lineas = unidades_lineas # Cantidad de lineas en la terminal
        self.celdas_y = 0
        self.celdas_x = 0
        
        self.__calcular_celdas_xy()
    
    def __calcular_celdas_xy(self):
        self.celdas_y = self.__calcular_celdas(self.magnitud_rel[0], self.lineas) # Se calculan las dimensiones de las celdas del eje Y
        self.celdas_x = self.__calcular_celdas(self.magnitud_rel[1], self.columnas) # Se calculan las dimensiones de las celdas del eje X

    def __calcular_celdas(self, magnitud_rel, unidades):
        """
        Cálcula las dimensiones de las celdas
        
        Parámetros:
        ___________
        magnitud_rel : list
            lista que contiene la cantidad de celdas a crear
        
        unidades : int
            cantidad de unidades del eje correspondiente que se van a dividir entre las celdas
        
        Retorna:
        ________
        list
            Una lista en la que cada elemento es otra lista dónde el campo [0] contiene el inicio de la celda y el campo [1] contiene el fin de la misma
        """
        celdas = []
        magnitudes = Magnitudes(magnitud_rel).calc_magnitud_bruta(unidades)
        
        fin_ant = 0
        inicio_act = 0
        fin_act = 0
        
        for magnitud in magnitudes:
            inicio_act = fin_ant
            fin_act = fin_ant + magnitud
            fin_ant = fin_act
            celdas.append([inicio_act,fin_act])
            
        return celdas
    
    def malla_resize(self, unidades_lineas, unidades_columnas):
        """
        Actualiza las dimensiones de las celdas en proporcion a su magnitud establecida.
        Se reciben como parametros la nueva cantidad de lineas y columnas de la terminal
        """
        if (unidades_columnas != self.columnas):
            self.columnas = unidades_columnas
            self.celdas_x = self.__calcular_celdas(self.magnitud_rel[1], unidades_columnas)
            
        if (unidades_lineas != self.lineas):
            self.lineas = unidades_lineas
            self.celdas_y = self.__calcular_celdas(self.magnitud_rel[0], unidades_lineas)