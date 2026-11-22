# Auditor Técnico de Sistemas Operativos — EPS Salud Integral

Prototipo desarrollado en **Python** como complemento práctico para el estudio de caso de **Administración de Sistemas Operativos**.

# 📋 Funcionalidades del Sistema
1. **Validador de Especificaciones Técnicas:** Verifica si una estación de trabajo (`cliente`) o un `servidor` cumple con los requisitos mínimos de CPU, RAM, almacenamiento, arquitectura de 64 bits y tabla de particiones GPT antes de instalar el SO.
2. **Administrador de Recursos (Control de Acceso RBAC):** Simula la autenticación de usuarios de la EPS (`medico`, `recepcion`, `soporte_ti`) y asigna permisos delimitados según el rol.
3. **Monitor de Interrupciones y Excepciones:** Simula la detección de eventos de hardware (IRQ) y software (Trap), aplica el protocolo de contención del *kernel* y registra cada incidente con fecha y hora en el archivo `bitacora_eps.log`.

## 🚀 Cómo ejecutarlo
1. tener **Python 3** instalado.
2. Clona este repositorio o descarga `auditor_eps.py`.
3. Ejecuta en terminal:
   ```bash
   python auditor_eps.py