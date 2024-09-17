import malla
import malla.areas
import malla.mallas

class ManejadorAreas:
    """
    Clase ManejadorAreas
    Un objeto de esta clase permite crear y gestionar areas dentro de una sola malla
    las areas reciben un nombre y se pueden mover, actualizar, cambiar propiedades y eliminar
    existen métodos para redimensionar/actualizar las posiciones y dimensiones de todas las areas
    contenidas por el objeto o para refrescar las porpiedades de las mismas
    
    Parametros:
    ___________
    p_malla : malla
        La malla en la que serán creadas las áreas
    ventana_padre : curse.window\n
        Debe ser la misma ventana sobre la que está la malla
        
    Atributos:
    __________
    ventana_padre : curse.window
        Ventana sobre la que está la malla
    areas : dictionary
        Diccionario que contiene las áreas asociadas a un nombre
    malla : malla
        malla sobre la que se gestionarán las áreas
    """
    def __init__(self, p_malla, ventana_padre):
        self.ventana_padre = ventana_padre
        self.areas = {}
        self.malla = p_malla
        
    def crear(self, nombre, inicio_x, inicio_y, fin_x, fin_y):
        """Crea un objeto de tipo malla.areas.Area() le asigna un nombre y lo agrega al diccionario"""
        self.areas.update({
            nombre: malla.areas.Area(self.malla, inicio_x, inicio_y, fin_x, fin_y)
        })
        return self.areas[nombre]
        
    def eliminar(self, nombre):
        """Borra la ventana y elimina su referencia del diccionario"""
        self.areas[nombre].ventana.erase()
        self.areas.pop(nombre)

    def mover_x(self, nombre, x):
        """Mueve el área con ese nombre a la celda x de la malla"""
        self.areas[nombre].mover_celda_x(x)
        
    def mover_y(self, nombre, y):
        """Mueve el área con ese nombre a la celda y de la malla"""
        self.areas[nombre].mover_celda_y(y)
        
    def get_area(self, nombre):
        """Retorna el area con ese nombre"""
        return self.areas[nombre]

    def get_ancho_x(self, nombre):
        """Retrona el ancho del area con ese nombre"""
        return self.areas[nombre].ancho_x
    
    def get_largo_y(self, nombre):
        """Retorna el largo del area con ese nombre"""
        return self.areas[nombre].largo_y

    def get_ventana(self, nombre):
        """Retorna la ventana del area con ese nombre"""
        return self.areas[nombre].ventana
        
    def actualizar_todo(self):
        """Actualiza las posiciones y tamaños de todas las areas, luego refresca las áreas"""
        self.redimensionar_todo()
        self.refrescar_todo()
        
    def agregar_propiedad(self, nombre, propiedad):
        """Agrega una propiedad de attron() a una ventana del area con ese nombre"""
        self.ventana_padre.refresh()
        self.areas[nombre].agregar_propiedad(propiedad)
        
    def definir_propiedades(self, nombre, propiedades):
        """Define las propiedas en areas.Area.definir_propiedades() del area con ese nombre"""
        self.ventana_padre.refresh()
        self.areas[nombre].definir_propiedades(propiedades)
        
    def redimensionar_todo(self):
        """Actualiza las posiciones y dimensiones de las ventanas"""
        yx = self.ventana_padre.getmaxyx()
        self.malla.redimensionar(yx[0], yx[1])
        for area in self.areas.values():
            area.actualizar_malla(self.malla)
            
    def cambiar_fondo(self, nombre, fondo):
        """Cambia el fondo de la ventana del area con ese nombre"""
        self.areas[nombre].cambiar_fondo(fondo)
            
    def refrescar_todo(self):
        """Refresca todas las ventanas"""
        for area in self.areas.values():
            area.ventana.refresh()