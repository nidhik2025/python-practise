from pathlib import Path
path = Path(r"C:\nivzen technologies\modules.py")
print(path.is_dir())
print(path.is_file())
print(path.exists())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = Path("BASICS")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("sales2")

# print(path.iterdir())
for p in path.iterdir():
    print(p)

# paths = [p for p in path.iterdir()]
# print(paths)
# py_files = [ p for p in path.glob("*.py") ]
py_files = [ p for p in path.rglob("*.py") ]
print(py_files)

# DATE AND TIME
import datetime
x = datetime.datetime.now()
print(x)

from pathlib import Path
from zipfile import ZipFile

with ZipFile("myzip.zip","w") as zip:
    for path in Path("BASICS").rglob("*.*"):
        zip.write(path)