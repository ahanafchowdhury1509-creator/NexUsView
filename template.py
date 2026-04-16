import os
from pathlib import Path
import logging

logging.basicConfig(

    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s] : %(message)s"
)
while True:
    proj_name=input("Input project name: ")
    if proj_name!="":
        break
    else:
        logging.info("Project name can't be empty")

list_of_files=[
  ".github/workflows/.gitkeep ",
      f"src/{proj_name}/__init__.py",
      f"tests/__init__.py",
      f"tests/unit/__init__.py",
      f"tests/integration/__init__.py",
      "requirments.txt",
      "Requirment_dev.txt",
      "setup.py",
      "pyproject.toml",
      "setup.cfg",
      "tox.ini"

]

for file in list_of_files:
    file=Path(file)
    filedir,filename=os.path.split(file)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    if(not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,"w") as fp:
            pass
            logging.info(f"Creating file: {file}")
    else:
        logging.info(f"{filename} already exists")