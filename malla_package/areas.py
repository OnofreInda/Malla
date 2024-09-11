import curses
from malla_package.celdas import celda

class Area:
    """
    La clase área permite crear una ventana en un rango de celdas que son creadas por la clase malla.
    
    Parámetros:
    ___________
    malla : Malla
        Recibe el objeto malla
    cel_inicio_x : int
        Posicion de inicio del area en las celdas del eje X
    cel_inicio_y : int
        posición de inicio del area en las celdas del eje Y
    cel_fin_x : int
        posición de fin del área en las celdas del eje X
    cel_fin_y : int
        posición de fin del área en las celdas del eje Y
        
    Atributos:
    __________
    rango_x : list
        lista que contienen los valores de inicio y fin respectivamente en el eje X
    rango_y : list
        lista que contienen los valores de inicio y fin respectivamente en el eje Y
    inicio_x : int
        Columna de la terminal dónde inicia la ventana
    inicio_y : int
        Linea de la terminal dónde inicia la ventana
    fin_x : int
        Columna de la terminal dónde finaliza la ventana
    fin_y : int
        Linea de la terminal dónde finaliza la ventana
    ancho_x : int
        Ancho medido en columnas de la terminal
    ancho_y : int
        Ancho medida en lineas de la terminal
    ventana : curses.Window
        Objeto ventana del módulo curses
        
    Métodos:
    ________
    obtener_ventana : curses.Window
        Retorna un objeto ventana del módulo curses, con las dimensiones del área
    refrescar
        refresca la ventana
    actualizar_malla
        Actualiza el tamaño de la ventana con relacion a las nuevas proporciones de la malla
    """
    def __init__(self, malla, cel_inicio_x, cel_inicio_y, cel_fin_x, cel_fin_y):
        self.rango_x = [cel_inicio_x, cel_fin_x]
        self.rango_y = [cel_inicio_y, cel_fin_y]
        self.inicio_x = 0
        self.inicio_y = 0
        self.fin_x = 0
        self.fin_y = 0
        
        self.__obtener_posicion_xy(malla)
        
        self.ancho_x = self.fin_x - self.inicio_x
        self.ancho_y = self.fin_y - self.inicio_y
        self.ventana = self.obtener_ventana()
    
    def __obtener_posicion_xy(self, malla):
        self.inicio_x = int(self.__obtener_posicion(malla.celdas_x, self.rango_x[celda.INICIO], celda.INICIO))
        self.inicio_y = int(self.__obtener_posicion(malla.celdas_y, self.rango_y[celda.INICIO], celda.INICIO))
        self.fin_x = int(self.__obtener_posicion(malla.celdas_x, self.rango_x[celda.FIN], celda.FIN))
        self.fin_y = int(self.__obtener_posicion(malla.celdas_y, self.rango_y[celda.FIN], celda.FIN))
        
    def __obtener_posicion(self, celdas, celda, inicio_fin):
        return celdas[celda][inicio_fin]
    
    def obtener_ventana(self):
        return curses.newwin(self.ancho_y, self.ancho_x, self.inicio_y, self.inicio_x)
        
    def refrescar(self):
        self.ventana.refresh()
    
    def actualizar_malla(self, malla):
        self.__obtener_posicion_xy(malla)
        self.ancho_x = self.fin_x - self.inicio_x
        self.ancho_y = self.fin_y - self.inicio_y
        self.ventana.resize(self.ancho_y, self.ancho_x)
        self.ventana.mvwin(self.inicio_y, self.inicio_x)
        self.ventana.refresh()