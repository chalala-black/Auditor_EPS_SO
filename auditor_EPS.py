import datetime

#import datetime es de PY. es para leer la fecha y hora del sistema operativo. Por que? porque cada error se debe guardar con fecha y hora para poder hacer un seguimiento de los errores.
print ("============================================")
print ("AUDITOR TECNICO DE SO - EPS SALUD INTEGRAL  ")
print ("============================================")
#print se usa para mostrar en pantalla el mensaje. En este caso es un mensaje de bienvenida al auditor tecnico de SO de EPS SALUD INTEGRAL.

#1. Datos de especificaciones minimas exigidas por EPS SALUD INTEGRAL
REQUISITOS={
    "cliente": {"cpu_nucleos": 4, "ram_gb": 8, "disco_gb": 120, "arquitectura": 64, "particion": "GPT"},
    "servidor": {"cpu_nucleos": 8, "ram_gb": 32, "disco_gb": 500, "arquitectura": 64, "particion": "GPT"},
}
#con REQUISITOS se define un diciionario (una estructura que guarda datos etiquetados) guardando las reglas tecnicas que se definen para la EPS

print("config base cargada correctamente")

#2. funcion para validar si el hardware cumple con los requisitos de la EPS 
def validar_especificaciones():
    print("/n--- VALIDACION DE ESPECIFICACIONES TECNICAS ---")
    #input(...): Pausa el programa y espera que se escriba algo en la terminal
    type=input("Tipo de equipo (cliente/servidor): ").strip().lower()
#def validar_especificaciones(): Crea una función (un bloque reutilizable con nombre propio). Todo lo que está metido hacia la derecha (indentado con 4 espacios) pertenece a esta función
    if type not in REQUISITOS:
        print("Tipo de equipo no valido. Debe ser 'cliente' o 'servidor'.")
        return
#.strip().lower(): Limpia espacios accidentales al inicio/final (.strip()) y pasa todo a minúsculas (.lower()), así si se escribe "Cliente " o "CLIENTE", Python lo entiende igual

    #Pedimos los datos del equipo tecnico al usuario
    nucleos = int(input("Ingrese el numero de nucleos de CPU: "))
    ram = int(input("Ingrese la cantidad de RAM en GB: "))
    disco = int(input("Ingrese la capacidad del disco de almacenamiento SSD/HDD en GB: "))
    arq=int (input("arquitectura del equipo (32 o 64 bits): "))
    particion=input("tipo de particion del disco (GPT o MBR): ").strip().upper()
#int(...): Convierte lo que se escribe en un número entero, porque por defecto input() lee texto y no se podría comparar si "8" es menor que 16 sin convertirlo a número

    reglas = REQUISITOS[type]
    errores = []

    #comparamos cada dato del equipo contra las reglas minimas de la EPS
    if nucleos < reglas["cpu_nucleos"]:
        errores.append(f"CPU insuficiente: tiene {nucleos} nucleos, se requieren {reglas['cpu_nucleos']} nucleos.")
    if ram < reglas["ram_gb"]:
        errores.append(f"RAM insuficiente: tiene {ram} GB, se requieren {reglas['ram_gb']} GB.")
    if disco < reglas["disco_gb"]:
        errores.append(f"Disco insuficiente: tiene {disco} GB, se requieren {reglas['disco_gb']} GB.")
    if arq != reglas["arquitectura"]:
        errores.append(f"Arquitectura incorrecta: tiene {arq} bits, se requiere {reglas['arquitectura']} bits.")
    if particion != reglas["particion"]:
        errores.append(f"Tipo de particion no recomendado: tiene {particion}, debe usar {reglas['particion']}.")
        #se muestra el veredicto tecnico
        if len(errores) == 0:
            print(f"/n[APROBADO] El equipo ({type.upper()}) cumple con las especificaciones para instalar el SO.")
        else:
            print(f"/n[RECHAZADO] El equipo ({type.upper()}) no cumple con las especificaciones para instalar el SO.")
            for error in errores:
                print(f"- {error}")
#se prueba la funcion llamandola
#if tipo not in REQUISITOS:: Verifica si escribiste algo distinto a cliente o servidor. Si te equivocas, muestra un aviso y usa return para salir de la función sin que el programa se rompa
#errores = []: Crea una lista vacía donde iremos metiendo los fallos que encontremos
#Los cinco if seguidos: Comparan cada dato real del equipo contra las reglas que guardamos en REQUISITOS (usando < para "menor que" y != para "diferente de"). Si algo falla, .append(...) mete el mensaje de error dentro de la lista errores
#if len(errores) == 0:: Cuenta cuántos errores quedaron en la lista (len = longitud). Si hay 0 errores, aprueba el equipo; si hay 1 o más, recorre la lista con for err in errores: y los imprime uno por uno

# 3. Administrador de Recursos: Autenticacion y Control de Acceso por Roles (RBAC)
USUARIOS_EPS = {
    "dra.gomez": {"clave": "1234", "rol": "medico", "permisos": ["leer_historia", "escribir_historia", "emitir_formula"]},
    "carlos.r": {"clave": "5678", "rol": "recepcion", "permisos": ["agendar_cita", "consultar_afiliado"]},
    "admin.ti": {"clave": "9999", "rol": "soporte_ti", "permisos": ["configurar_so", "ver_logs", "gestionar_drivers"]}
}
#USUARIOS_EPS: Simula la base de datos de cuentas del Sistema Operativo
def verificar_acceso_usuario():
    print("\n--- ADMINISTRADOR DE RECURSOS: CONTROL DE ACCESO ---")
    usuario = input("Usuario EPS (ej. dra.gomez / carlos.r / admin.ti): ").strip().lower()
    clave = input("Contrasena: ").strip()

    if usuario in USUARIOS_EPS and USUARIOS_EPS[usuario]["clave"] == clave:
        datos = USUARIOS_EPS[usuario]
        print(f"\n[ACCESO CONCEDIDO] Bienvenido/a {usuario} | Rol: {datos['rol'].upper()}")
        print("Permisos autorizados por el SO:", ", ".join(datos["permisos"]))
    else:
        print("\n[ACCESO DENEGADO] Credenciales invalidas. El SO bloquea el acceso a los datos.")
#if usuario in USUARIOS_EPS and ...: Usa and para exigir que ambas condiciones sean verdaderas
# 4. Procedimiento ante Interrupciones (Hardware) y Excepciones (Software)
def gestionar_evento_sistema():
    print("\n--- MONITOR DE INTERRUPCIONES Y EXCEPCIONES ---")
    print("1. Interrupcion de Hardware (ej. fallo de lectura en disco / conflicto IRQ de impresora)")
    print("2. Excepcion de Software (ej. violacion de memoria en aplicativo de soporte)")
    opcion = input("Seleccione el evento detectado (1 o 2): ").strip()

    hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if opcion == "1":
        evento = "INTERRUPCION HARDWARE (IRQ)"
        accion = "1) Aislar dispositivo | 2) Verificar driver firmado | 3) Revisar estado S.M.A.R.T./RAM."
    elif opcion == "2":
        evento = "EXCEPCION SOFTWARE (TRAP)"
        accion = "1) Cerrar proceso en modo protegido sin apagar SO | 2) Leer log/dump | 3) Aplicar parche/permisos."
    else:
        print("Opcion no valida.")
        return

    print(f"\n[ALERTA DEL KERNEL - {hora}] Detectado: {evento}")
    print(f"Protocolo aplicado: {accion}")

    #se guarda el registro real en un archivo .txt (bitacora del SO)
    with open("bitacora_eps.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{hora}] {evento} -> {accion}\n")
    print("Registro guardado en 'bitacora_eps.log'.")
#abre (o crea automáticamente si no existe) un archivo llamado bitacora_eps.log en una carpeta en modo "a" (append = agregar al final sin borrar lo anterior) y escribe el reporte del error con fecha y hora
# 5. Menu principal del programa
while True:
    print("\n================ MENU PRINCIPAL EPS ================")
    print("1. Validar especificaciones tecnicas del equipo")
    print("2. Probar control de acceso por roles (Administrador de Recursos)")
    print("3. Simular interrupcion o excepcion en aplicativo")
    print("4. Salir")
    eleccion = input("Elige una opcion (1-4): ").strip()
#while True: Crea un bucle infinito que mantiene el menú abierto.Hasta que elija la opción "4", donde break rompe el bucle y cierra el programa
    if eleccion == "1":
        validar_especificaciones()
    elif eleccion == "2":
        verificar_acceso_usuario()
    elif eleccion == "3":
        gestionar_evento_sistema()
    elif eleccion == "4":
        print("Cerrando auditor de la EPS. Hasta luego.")
        break
    else:
        print("Opcion incorrecta, intenta de nuevo.")
        