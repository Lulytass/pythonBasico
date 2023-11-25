#clase reserva canchas
class Equipo():
    def  __init__(self, nombre,  max) : # metodo contructor de la clase con el metodo especial __init__()
        self.nombre=nombre   # Al atributo nombre le asigno el nombre que recibi coomo parametro
        self.max_jugadores = max
        self.jugadores = []

    def agregar_jugadores(self, jugador):
        self.jugadores.append(jugador)

    def __str__(self):
        return f"Equipo: {self.nombre}- CantMax: {self.max_jugadores} - Jugadores: {self.jugadores}"

class Reserva():
    def __init__(self, fecha, equipo1, equipo2):
        self.fecha = fecha
        self.equipo1 = equipo1
        self.equipo2 = equipo2
    def __str__(self):
        return f"Fecha: {self.fecha} -  {self.equipo1} vs {self.equipo2}"

#principal

equipo1 = Equipo("prueba", 10)
equipo1.agregar_jugadores("Juan")
equipo1.agregar_jugadores("Lucia")
print(equipo1)

equipo2 = Equipo("contra", 10)
equipo2.agregar_jugadores("Manuel")
equipo2.agregar_jugadores("Florencia")
print(equipo2)

reserva = Reserva("16/11/2023", equipo1, equipo2)
print(reserva)
       