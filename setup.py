from setuptools import setup

setup(    name="mipaquete",
          version="1.0",
          description="mi primer paquete redistribuible",
          author="Franco",
          packages=["paquete"],
    
)
# Lo activo con python setup.py sdist
# Si voy a recibir un paquete que es el comprimido de dist debo hacer un pip istall "Nombre del paquete"
# tambien es necesario que me pasen el egg info para ver que contiene ese paquete

