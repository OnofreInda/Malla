import curses
from malla_package.celdas import celda

class Area:
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