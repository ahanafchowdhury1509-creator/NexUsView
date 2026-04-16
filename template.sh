export PROJECT_NAME="NEXUSVIEW"

mkdir  -p .github/workflows src/$PROJECT_NAME tests/unit tests/integration


touch .github/workflows/.gitkeep \
      src/$PROJECT_NAME/__init__.py \
      tests/__init__.py\
      tests/unit/__init__.py\
      tests/integration/__init__.py\
      requirments.txt\
      Requirment_dev.txt\
      setup.py\
      pyproject.toml\
      setup.cfg\
      tox.ini\

       