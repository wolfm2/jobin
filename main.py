import papermill as pm
import os

os.chdir("minibook/test")

pm.execute_notebook(
   'intro_python.ipynb',
   'output.ipynb',
   #parameters = dict(alpha=0.6, ratio=0.1)
)

