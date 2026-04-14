
class Usuario:
    __usuarios_registrados = {}

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    @classmethod
    def registrar(cls, email, password):
        if email in cls.__usuarios_registrados:
            print("El email ya está registrado.")
            return None
        usuario = cls(email, password)
        cls.__usuarios_registrados[email] = usuario
        print("Usuario registrado correctamente.")
        return usuario

    @classmethod
    def login(cls, email, password):
        usuario = cls.__usuarios_registrados.get(email)
        if usuario and usuario.__password == password:
            print("Login exitoso.")
            return True
        else:
            print("Email o contraseña incorrectos.")
            return False

# Ejemplo de uso
if __name__ == "__main__":
    # Registrar usuario de ejemplo
    Usuario.registrar("test@email.com", "1234")

    # Pedir datos para iniciar sesión
    print("Iniciar sesión")
    email = input("Email: ")
    password = input("Contraseña: ")
    Usuario.login(email, password)
