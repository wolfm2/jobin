import papermill as pm
import os

nbk_path = "minibook/test/intro_python.ipynb" # RELATIVE to repo base!
ret_files = []
prep_files = True  # prep files before sending

def main():
  pm.execute_notebook(
    os.path.basename(nbk_path),
    'output.ipynb',
    #parameters = dict(alpha=0.6, ratio=0.1)
  )

sz_90m = 90 * (1024 ** 2)
sz_90m = 90 * (1024 ** 1)

# unzip large files
def unpack(): # zip -FF dataIn.zip --out y.zip
  relpath = os.path.dirname(nbk_path)
  os.system('/usr/bin/zip -FF ~/jobin/' + relpath + '/dataIn.zip --out out.zip')
  os.system('/usr/bin/unzip -u ./out.zip -d .')
  os.system('rm ./out.zip')

# zip large files
def pack(fn, zName): 
  if not len(fn):
    return
  os.system('rm ' + zName + '.z*') # can't append split archives, so remove
  zcall = '/usr/bin/zip ' + zName + '.zip -s 50m'
  for f in fn: 
    zcall += " '" + f + "'"
  os.system(zcall)
  os.system('git add ' + zName + '.z*')

# preps large files before sending.
def preSend():
  print("Prepping files...\n")
  paths  = []
  for top, dirs, files in os.walk('.'):
    for nm in files:
      fn = os.path.join(top, nm)
      if os.path.getsize(fn) > sz_90m:
        print ("Adding: " + fn + "\n")
        paths.append(fn)
        
  pack(paths, 'dataIn')
  
if __name__ == '__main__':

  os.chdir(os.path.dirname(nbk_path))
  if prep_files:
    preSend()
    exit()
    
  unpack()
  main()
  pack(ret_files, 'dataOut')
