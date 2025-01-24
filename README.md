# intelligent-tutor-system


![Django Logo](https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg)

**intelligent-tutor-system** es un sistema de tutor inteligente basado en la materia de programación. Este sistema utiliza Python, Django, y tecnologías avanzadas como redes neuronales para ofrecer una experiencia personalizada de aprendizaje. 

---

## Características principales

- **Inicio de sesión y registro de usuarios**.
- Panel de usuario con progreso del estudiante.
- Examen inicial para determinar el nivel del usuario.
- Lecciones, pruebas y ejercicios personalizados.
- Estadísticas de rendimiento y progreso del usuario.

---

## Requisitos del sistema

### Software necesario

- **Python 3.9 o superior**
- **Pip** (administrador de paquetes de Python)
- **Django 4.x**
- **XAMPP** (o una base de datos MySQL alternativa)

---

## Configuración del entorno

### En Linux (Ubuntu)

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/intelligent-tutor-system.git
   cd intelligent-tutor-system
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   - Asegúrate de que XAMPP (o MySQL) esté instalado y ejecutándose.
   - Crea una base de datos llamada `sistema`.
   - Configura las credenciales de tu base de datos en el archivo `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'sistema',
             'USER': 'tu_usuario',
             'PASSWORD': 'tu_contraseña',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Aplicar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Iniciar el servidor**
   ```bash
   python manage.py runserver
   ```

7. **Acceder al sistema**
   - Abre tu navegador y ve a [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### En Windows

1. **Clonar el repositorio**
   ```cmd
   git clone https://github.com/tu-usuario/intelligent-tutor-system.git
   cd intelligent-tutor-system
   ```

2. **Crear y activar un entorno virtual**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar las dependencias**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   - Asegúrate de que XAMPP (o MySQL) esté instalado y ejecutándose.
   - Crea una base de datos llamada `sistema`.
   - Configura las credenciales de tu base de datos en el archivo `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'sistema',
             'USER': 'tu_usuario',
             'PASSWORD': 'tu_contraseña',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Aplicar migraciones**
   ```cmd
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Iniciar el servidor**
   ```cmd
   python manage.py runserver
   ```

7. **Acceder al sistema**
   - Abre tu navegador y ve a [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para cualquier mejora o corrección.

---

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).

---

### ¡Gracias por usar intelligent-tutor-system!
