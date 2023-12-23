# Humberto Barrera Martinez
# Fecha 06/09/2023
# Descripcion: Programa en Python que resuelve un sistema de EDOs usando el metodo de Euler
# En esta ocasion, el programa calcula la concentracion salina a traves del tiempo en un lago dulce conectado a un lago salado.

# Funcion para imprimir un espacio en blanco
def blank():
    print(f' ')

# Funcion para resolver un sistema de EDOs usando el metodo de Euler
def euler(cs0, cd0, vs, vd, f0, dt, num_pasos):
    # Se inicializan las listas para guardar los valores de las concentraciones
    valores_cs = [cs0]
    valores_cd = [cd0]

    # Se utiliza un ciclo for para calcular los valores de las concentraciones usando el metodo de Euler
    for i in range(num_pasos):
        cs_n = valores_cs[-1]
        cd_n = valores_cd[-1]

        # Se calculan las derivadas de las concentraciones
        dcs_dt = -cs_n / vs * f0
        dcd_dt = (cs_n / vs - cd_n / vd) * f0

        # Se calculan los nuevos valores de las concentraciones y se actualizan las variables
        nuevo_cs = cs_n + dcs_dt * dt
        nuevo_cd = cd_n + dcd_dt * dt

        # Se agregan los nuevos valores a las listas
        valores_cs.append(nuevo_cs)
        valores_cd.append(nuevo_cd)

    # Se regresan los valores de las concentraciones
    return valores_cs, valores_cd

# Funcion principal
if __name__ == "__main__":
    # Se le solicita al usuario que ingrese los valores de las variables con las unidades deseadas
    cs0 = float(input("Ingrese la concentracion inicial en el lago salado (cs0 en kg/m^3): "))
    cd0 = float(input("Ingrese la concentracion inicial en el lago dulce (cd0 en kg/m^3): "))
    vs = float(input("Ingrese el volumen del lago salado (vs en m^3): "))
    vd = float(input("Ingrese el volumen del lago dulce (vd en m^3): "))
    f0 = float(input("Ingrese la tasa de flujo (f0 en m^3/s): "))
    dt = float(input("Ingrese el paso de tiempo (dt en segundos): "))
    num_pasos = int(input("Ingrese el numero de pasos de tiempo a simular: "))

    # Se manda llamar a la funcion euler para resolver el sistema de EDOs
    valores_cs, valores_cd = euler(cs0, cd0, vs, vd, f0, dt, num_pasos)

    # Se imprimen los resultados
    blank()
    print("Resultados:")
    for t, (cs, cd) in enumerate(zip(valores_cs, valores_cd)):
        print(f"Paso {t}: Concentracion Salada = {cs} kg/m^3, Concentracion Dulce = {cd} kg/m^3")

