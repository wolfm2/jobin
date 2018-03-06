import papermill as pm

pm.execute_notebook(
   'minibook/intro_python.ipynb',
   'out/output.ipynb',
   #parameters = dict(alpha=0.6, ratio=0.1)
)

