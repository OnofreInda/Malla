import malla
import malla.areas
import malla.mallas
import curses

class ManejadorAreas:
    def __init__(self, p_malla, ventana_padre):
        self.ventana_padre = ventana_padre
        self.areas = {}
        self.malla = p_malla
        
    def crear(self, nombre, inicio_x, inicio_y, fin_x, fin_y):
        self.areas.update({
            nombre: malla.areas.Area(self.malla, inicio_x, inicio_y, fin_x, fin_y)
        })
        
    def eliminar(self, nombre):
        self.areas[nombre].ventana.erase()
        self.areas.pop(nombre)

    def mover_x(self, nombre, x):
        self.areas[nombre].mover_celda_x(x)
        
    def mover_y(self, nombre, y):
        self.areas[nombre].mover_celda_y(y)
        
    def get_area(self, nombre):
        return self.areas[nombre]

    def get_ventana(self, nombre):
        return self.areas[nombre].ventana
        
    def actualizar(self):
        self.redimensionar_todo()
        self.refrescar_todo()
        
    def agregar_propiedad(self, nombre, propiedad):
        self.ventana_padre.refresh()
        self.areas[nombre].agregar_propiedad(propiedad)
        
    def definir_propiedades(self, nombre, propiedades):
        self.ventana_padre.refresh()
        self.areas[nombre].definir_propiedades(propiedades)
        
    def redimensionar_todo(self):
        yx = self.ventana_padre.getmaxyx()
        self.malla.redimensionar(yx[0], yx[1])
        for area in self.areas.values():
            area.actualizar_malla(self.malla)
            
    def refrescar_todo(self):
        for area in self.areas.values():
            area.ventana.refresh()