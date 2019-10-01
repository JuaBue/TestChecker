from distutils.core import setup
import py2exe

setup(
        name="TestChecker",
        version="1.0",
        description="SW para parsear las trazas de los Test Unitarios",
        author="Juan Bueno",
        windows=[{"script":'TestChecker.py',
                  "icon_resources": [(1, "logos/crocodile.ico")],
                  "dest_base": "TestChecker"}],
        options={"py2exe":{'compressed': True}
                 }
)
