# Importar metodo abstracto de ABC
from abc import ABC, abstractmethod

# Crear clase abstracta Membresia (define el esqueleto del tipo de membresia)
class Membresia(ABC):
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """Metodo contructor para inicializar una instancia de Membresia
        Args:
        correo_suscriptor (str): correo electronico del suscriptor
        numero_tarjeta (str): numero de tarjeta del suscriptor
        """ 
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    # Getter para correo_suscriptor (mostrar)
    @property
    def correo_suscriptor(self):
        """ Obtiene el correo electronico del suscriptor"""
        return self.__correo_suscriptor

    # Getter para numero_tarjeta (mostrar)
    @property
    def numero_tarjeta(self):
        """ Obtiene el numero de tarjeta del suscriptor"""
        return self.__numero_tarjeta

    # Metodo abstracto para cambiar el tipo de membresía
    @abstractmethod
    def cambiar_suscripcion(self, tipo_membresia: int):
        pass

    # Metodo protected para crear tipo de membresia
    def _crear_nueva_membresia(self, tipo_membresia: int):
        """Crear una nueva membresia de acuerdo a las condiciones descritas.
        Args:
        nueva_membresia (int): número escogido segun el tipo de membresia 
        Returns:
        Instancia de la clase Membresia, creada segun la eleccion de nueva_membresia
        """ 

        if tipo_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

# Crear clase gratis, subclase de Membresia
class Gratis(Membresia):
    # Atributos de la clase
    costo = 0
    cantidad_dispositivos = 1

    # Metodo para cambiar suscripcion de acuerdo al tipo de membresia
    def cambiar_suscripcion(self, tipo_membresia: int):
        """Cambiará el tipo de suscripcion desde gratis a alguna de las otras opciones
        Args:
        tipo_membresia (int): tipo de membresia al cual se cambiará
        Returns:
        Si el valor no está entre 1 y 4 retornará la instancia gratuita, y si el valor está dentro de las opciones retornará la nueva membresia.
        """

        if tipo_membresia < 1 or tipo_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(tipo_membresia)

# Crear clase básica subclase de clase Membresia
class Basica(Membresia):
    # Atributos de la clase
    costo = 3000
    cantidad_dispositivos = 2

    # Metodo constructor heredado de clase Membresia, para inicializar una instancia de la clase Basica
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        """ Verificar si la instancia actual pertenece a una u otra clase y condicionar los dias de regalo de acuerdo a cual clase pertenezca"""
        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7

        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    # Metodo para cancelar la suscripcion 
    def cancelar_suscripcion(self):
        """ Returns: instancia de la clase gratis si cancela suscripción"""
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia: int):
        """Cambiará el tipo de suscripción desde basica a alguna de las otras opciones
        Args:
        tipo_membresia (int): tipo de membresia escogida
        Returns:
        Si el valor no está entre 2 y 4 retornará la instancia básica, y si el valor está dentro de las opciones retornará la nueva membresia.
        """
        if tipo_membresia < 2 or tipo_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(tipo_membresia)

# Clase familiar, subclase de la clase Basica
class Familiar(Basica):
    # Atributos de la clase
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, tipo_membresia: int):
        """Cambiará el tipo de suscripción desde Familiar a alguna de las otras opciones
        Args:
        tipo_membresia (int): tipo de membresia escogida
        Returns:
        Si el valor no es 1, 3 o 4 retornará la instancia Familiar, y si el valor está dentro de las opciones retornará la nueva membresia.
        """
        if tipo_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(tipo_membresia)

    # Crear clase para que los padres controlen el uso de los niños
    def modificar_control_parental(self):
        pass

# Crear clase SinConexion, subclase de clase Basica
class SinConexion(Basica):
    # Atributo de la clase
    costo = 3500

    def cambiar_suscripcion(self, tipo_membresia: int):
        """Cambiará el tipo de suscripcion desde SinConexion a alguna de las otras opciones
        Args:
        nueva_membresia (int): tipo de membresia al cual se cambiará
        Returns:
        Si el valor no es 1, 2 o 4 retornará la instancia SinConexion, y si el valor está dentro de las opciones retornará la nueva membresia.
        """
        if tipo_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(tipo_membresia)

    def incrementar_cantidad_maxima_offline(self):
        pass

# Crear clase Pro, subclase de Familiar y SinConexion
class Pro(Familiar, SinConexion):
    # Atributos de la clase 
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, tipo_membresia: int):
        """Cambiará el tipo de suscripcion desde Pro a alguna de las otras opciones
        Args:
        tipo_membresia (int): tipo de membresia escogida
        Returns:
        Si el valor no está entre 1 y 3 retornará la instancia Pro, y si el valor está dentro de las opciones retornará la nueva membresia.
        """
        if tipo_membresia < 1 or tipo_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(tipo_membresia)


g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
