# Clase para manejar el árbol binario de búsqueda de usuarios.

class Nodo:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, usuario, contrasena):
        def _insertar(nodo, usuario, contrasena):
            if nodo is None:
                return Nodo(usuario, contrasena)
            if usuario < nodo.usuario:
                nodo.izquierda = _insertar(nodo.izquierda, usuario, contrasena)
            else:
                nodo.derecha = _insertar(nodo.derecha, usuario, contrasena)
            return nodo

        self.raiz = _insertar(self.raiz, usuario, contrasena)

    def buscar(self, usuario, contrasena):
        def _buscar(nodo, usuario, contrasena):
            if nodo is None:
                return False
            if nodo.usuario == usuario and nodo.contrasena == contrasena:
                return True
            if usuario < nodo.usuario:
                return _buscar(nodo.izquierda, usuario, contrasena)
            return _buscar(nodo.derecha, usuario, contrasena)

        return _buscar(self.raiz, usuario, contrasena)