import curses
from malla.celdas import celda

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
        lista que contienen los valores de las celdas de inicio y fin respectivamente en el eje X
    rango_y : list
        lista que contienen los valores de las celdas de inicio y fin respectivamente en el eje Y
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
    largo_y: int
        Ancho medida en lineas de la terminal
    ventana : curses.Window
        Objeto ventana del módulo curses
    atrib_ventana : list
        lista de atributos que se pasan como parametros al método attron() del objeto curses.window
    fondo_ventana : int
        Número de color de fondo, debe corresponder a algun init_color()
        
    Métodos:
    ________
    refrescar
        refresca la ventana
    actualizar_malla
        Actualiza el tamaño de la ventana con relacion a las nuevas proporciones de la malla
    generar_ventana
        Genera un objeto curses.Window dentro del objeto
    refrescar_fondo
        Refresca el fondo de la ventana
    cambiar_fondo
        Cambia el valor de fondo_ventana y refresca el fondo
    agregar_propiedad
        Recibe un atributo que es pasado como parametro a curses.window.attron()
    eliminar_propiedad
        Elimina un elemento de atrib_ventana si es que existe y se pasa como parametro a curses.window.attroff()
    """
    def __init__(self, malla, cel_inicio_x, cel_inicio_y, cel_fin_x, cel_fin_y):
        self.malla = malla
        self.rango_x = [cel_inicio_x, cel_fin_x]
        self.rango_y = [cel_inicio_y, cel_fin_y]
        self.inicio_x = int
        self.inicio_y = int
        self.fin_x = int
        self.fin_y = int
        self.ancho_x = int
        self.largo_y= int
        self.ventana = curses.window
        self.atrib_ventana = []
        self.fondo_ventana = 0
        self.__actualizar_posiciones()
        self.generar_ventana()
    
    def __obtener_posicion_x(self):
        """Define la posicion de inicio y fin del área en X"""
        self.inicio_x = int(self.__obtener_posicion(self.malla.celdas_x, self.rango_x[celda.INICIO], celda.INICIO))
        self.fin_x = int(self.__obtener_posicion(self.malla.celdas_x, self.rango_x[celda.FIN], celda.FIN))

    def __obtener_posicion_y(self):
        """Define la posicion de inicio y fin del área en Y"""
        self.inicio_y = int(self.__obtener_posicion(self.malla.celdas_y, self.rango_y[celda.INICIO], celda.INICIO))
        self.fin_y = int(self.__obtener_posicion(self.malla.celdas_y, self.rango_y[celda.FIN], celda.FIN))

    def __obtener_posicion(self, celdas, celda, inicio_fin):
        return celdas[celda][inicio_fin]
    
    def __calcular_anchos(self):
        """Define las dimensiones del área"""
        self.ancho_x = self.fin_x - self.inicio_x
        self.largo_y= self.fin_y - self.inicio_y
        
    def __actualizar_posiciones(self):
        """Actualiza las posicion de inicio y fin del área así como sus dimensiones"""
        self.__obtener_posicion_x()
        self.__obtener_posicion_y()
        self.__calcular_anchos()
            
    def __aplicar_propiedades(self):
        """Aplica los atributos que se encuentran en self.atrib_ventana a self.ventana"""
        for atributo in self.atrib_ventana:
            self.ventana.attron(atributo)
        self.refrescar()
            
    def agregar_propiedad(self, propiedad):
        """Agrega una propiedad por el método attron del objeto self.ventana y tambien es agregado al self.atrib_ventana"""
        if self.atrib_ventana.count(propiedad) == 0:
            self.atrib_ventana.append(propiedad)
            self.ventana.attron(propiedad)
            self.refrescar()
        
    def eliminar_propiedad(self, propiedad):
        """Elimina un elemento de atrib_ventana y del objeto self.ventana utilizando el método attroff"""
        self.atrib_ventana.pop(propiedad)
        self.ventana.attroff(propiedad)
        self.ventana.refresh()
        
    def definir_propiedades(self, propiedades=[]):
        """
        Define el valor de atrib_ventana el cual tiene que ser una lista de elementos aplicables a una ventana
        aplicables por medio de curses.window.attron() y son aplicados a la misma
        """
        self.atrib_ventana = propiedades
        self.__aplicar_propiedades()
        
    def cambiar_fondo(self, fondo):
        """Cambia el valor de self.fondo_ventana y actualiza el fondo de la ventana"""
        self.fondo_ventana = fondo
        self.refrescar_fondo()

    def refrescar_fondo(self):
        """Asigna el fondo por medio de curses.window.bkgd() y refresca la ventana"""
        self.ventana.bkgd(' ', curses.color_pair(self.fondo_ventana))
        self.ventana.refresh()
        
    def generar_ventana(self):
        """Genera un objeto curses.Window por medio del método curses.newwin()"""
        self.ventana = curses.newwin(self.largo_y, self.ancho_x, self.inicio_y, self.inicio_x)
        self.refrescar_fondo()
        self.__aplicar_propiedades()

    def actualizar(self):
        """Intenta actualizar la posicion y dimensiones de la ventana, si no, la destruye y crea una con nueva posicion y dimensiones"""
        try:
            self.ventana.resize(self.largo_y, self.ancho_x)
            self.ventana.mvwin(self.inicio_y, self.inicio_x)
        except:
            self.generar_ventana()

    def __actualizar_area(self):
        """Actualiza la posicion y las dimensiones de la ventana, luego llama a la funcion self.actualizar()"""
        self.__actualizar_posiciones()
        self.actualizar()
        
    def mover_celda_x(self, x):
        """Mueve el área a una celda X de la malla"""
        distancia = x - self.rango_x[celda.INICIO]
        celdas = len(self.malla.celdas_x) - 1
        if (distancia <= celdas):
            self.rango_x[celda.INICIO] = x
            self.rango_x[celda.FIN] = self.rango_x[celda.FIN] + distancia if (self.rango_x[celda.FIN] + distancia) <= celdas else celdas
            self.__actualizar_area()
            
    def mover_celda_y(self, y):
        """Mueve el área a una celda Y de la malla"""
        distancia = y - self.rango_y[celda.INICIO]
        celdas = len(self.malla.celdas_y) - 1
        if (distancia <= celdas):
            self.rango_y[celda.INICIO] = y
            self.rango_y[celda.FIN] = self.rango_y[celda.FIN] + distancia if self.rango_y[celda.FIN] + distancia <= celdas else celdas
            self.__actualizar_area()
            
    def refrescar(self):
        """Refresca la ventana"""
        self.ventana.refresh()
    
    def actualizar_malla(self, malla):
        """Actualiza la malla"""
        self.malla = malla
        self.__actualizar_area()