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
        
    __inicio_x : int
    __inicio_y : int
        esquina superior izquierda de la terminal por dónde iniciará la malla (por defecto es el punto 0,0)
        estos atributos solo son modificables desde una clase heredada
    """
    def __init__(self, magnitud_filas, magnitud_columnas, unidades_lineas, unidades_columnas):
        self.magnitud_rel = [magnitud_filas, magnitud_columnas] # Pienso cambiar esto pronto
        self.columnas = unidades_columnas # Cantidad de columnas en la terminal
        self.lineas = unidades_lineas # Cantidad de lineas en la terminal
        self.celdas_y = []
        self.celdas_x = []
        self.__inicio_y = 0
        self.__inicio_x = 0
        
        self.__calcular_celdas()
    
    def __calcular_celdas(self):
        """Define la posicion de inicio y fin en la terminal por cada celda en ambos ejes"""
        self.__calcular_celdas_y(); self.__calcular_celdas_x()
    
    def __calcular_celdas_y(self):
        """Define la posicion de inicio y fin de las celdas en el eje Y"""
        self.celdas_y.clear()
        magnitudes = Magnitudes(self.magnitud_rel[0]).calc_magnitud_bruta(self.lineas)
        
        fin_ant = self.__inicio_y
        inicio_act = 0
        fin_act = 0
        
        for magnitud in magnitudes:
            inicio_act = fin_ant
            fin_act = fin_ant + magnitud
            fin_ant = fin_act
            self.celdas_y.append([inicio_act,fin_act])
            
    def __calcular_celdas_x(self):
        """Define la posicion de inicio y fin de las celdas en el eje X"""
        self.celdas_x.clear()
        magnitudes = Magnitudes(self.magnitud_rel[1]).calc_magnitud_bruta(self.columnas)
        
        fin_ant = self.__inicio_x
        inicio_act = 0
        fin_act = 0
        
        for magnitud in magnitudes:
            inicio_act = fin_ant
            fin_act = fin_ant + magnitud
            fin_ant = fin_act
            self.celdas_x.append([inicio_act,fin_act])
    
    def __actualizar_columnas(self, columnas):
        """Actualiza las proporciones de las columnas en la malla solo si el ancho de la malla es distinto al ancho actual"""
        if (columnas != self.columnas):
            self.columnas = columnas
            self.__calcular_celdas_x()
            
    def __actualizar_lineas(self, lineas):
        """Actualiza las proporciones de las filas en la malla solo si el alto de la malla es distinto al alto actual"""
        if (lineas != self.lineas):
            self.lineas = lineas
            self.__calcular_celdas_y()

    def __set_puntos_inicio(self, x,y):
        """Define la posicion de la esquina superior izquierda de la malla"""
        self.__inicio_x = x
        self.__inicio_y = y
        self.__calcular_celdas()
            
    def redimensionar(self, unidades_lineas, unidades_columnas):
        """
        Actualiza las dimensiones de las celdas en proporcion a su magnitud establecida.
        Se reciben como parametros la nueva cantidad de lineas y columnas de la terminal
        """
        self.__actualizar_columnas(unidades_columnas)
        self.__actualizar_lineas(unidades_lineas)
        
class MallaArea(Malla):
    """Permite crear una malla "dentro" de un objeto área"""
    def __init__(self, magnitud_filas, magnitud_columnas, unidades_lineas, unidades_columnas, area):
        self.area = area
        super().__init__(magnitud_filas, magnitud_columnas, unidades_lineas, unidades_columnas)
        super().__set_puntos_inicio(self.area.inicio_x, self.area.inicio_y)
        
    def redimensionar(self, unidades_lineas, unidades_columnas):
        super().__set_puntos_inicio(self.area.inicio_x, self.area.inicio_y)
        super().redimensionar(unidades_lineas, unidades_columnas)