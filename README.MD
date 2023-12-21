# Reconocimiento Facial con Python

Este README proporciona instrucciones detalladas para configurar y ejecutar una aplicación de reconocimiento facial en Python.

## Preparación del Entorno

### 1. Descarga del Repositorio
- Asegúrate de tener Git instalado en tu sistema.
- Clona el repositorio usando: `git clone https://github.com/AndresGaibor/reconocimientofacial.git` o descargando el zip

### 2. Instalación de Python
- Descarga e instala Python 3 desde [Python.org](https://www.python.org/downloads/).

## Configuración de la Red

### Configurar una IP Fija para el Servidor
Establecer una dirección IP estática puede ser necesario para ciertas configuraciones de red.

#### Encontrar la IP del Router
1. Abre la línea de comandos (CMD) y escribe `ipconfig`.
2. Busca la dirección IPv4 del router (generalmente algo como `192.168.0.1`).

#### Asignar una IP Estática
1. Haz clic derecho en el ícono de internet/wifi y selecciona "Configuración de red e Internet".
2. Ve a "Cambiar opciones de adaptador".
3. Haz clic derecho en el adaptador de red relevante (Ethernet o Wifi) y selecciona "Propiedades".
4. Selecciona "Protocolo de Internet versión 4 (TCP/IPv4)" y luego "Propiedades".
5. Elige "Usar la siguiente dirección IP" y asigna los siguientes valores:
   - IP: 192.168.25.121 (o una de tu elección en el mismo rango)
   - Máscara de subred: 255.255.255.0
   - Puerta de enlace predeterminada: [IP del Router]
6. Haz clic en "Aceptar" para aplicar y guardar los cambios.
   - Nota: Después de usar la aplicación, considera cambiar la configuración a "Obtener una dirección IP automáticamente".

## Configuración de Visual Studio Code

### Preparar el Editor para Python
1. Instala Visual Studio Code desde [su sitio web oficial](https://code.visualstudio.com/).
2. Abre Visual Studio Code y ve a la sección de extensiones.
3. Busca y instala la extensión de Python.

### Ejecutar el Servidor
1. Abre la carpeta del repositorio clonado en Visual Studio Code.
2. Si se solicita, acepta instalar las dependencias desde el archivo `requirements.txt`.
3. Abre el archivo `server.py`.
4. Ejecuta el script directamente desde el editor.