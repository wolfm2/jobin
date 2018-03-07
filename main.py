import papermill as pm
import os

nbk_path = "minibook/amazon/_00_split.ipynb" # RELATIVE to repo base!
ret_files = ['sc.pkl', 'hv.pkl', 'lgs.pkl']
#ret_files = []
prep_files = False  # prep files before sending

def main():
  pm.execute_notebook(
    os.path.basename(nbk_path),
    'output.ipynb',
    #parameters = dict(alpha=0.6, ratio=0.1)
  )

# sz_90m = 90 * (1024 ** 2)

#zip multipart broken
#tar cvjf - '/home/ich/GIT/Amazon.csv'  | split --bytes=50MB - dataIn.
#cat dataIn.?? | tar -jxv --keep-newer-files

# unzip large files
def unpack():
  path = os.path.expanduser("~/jobin/") + os.path.dirname(nbk_path) + '/dataIn'
  if not os.path.exists(path + '.aa'):
    return
  #print ('cat ' + path + '.?? | tar -jxv --keep-newer-files')
  os.system('cat ' + path + '.?? | tar -jxv --keep-newer-files')
  #os.system('/usr/bin/zip -FF ' + path + ' --out out.zip')
  #os.system('/usr/bin/unzip -u ./out.zip -d .')
  #os.system('rm ./out.zip')

# zip large files
def pack(fn, zName): 
  if not len(fn):
    return
  args = ""
  #os.system('rm ' + zName + '.z*') # can't append split archives, so remove
  #zcall = '/usr/bin/zip ' + zName + '.zip -s 50m'
  call = 'tar cvjf - {} | split --bytes=50MB - dataIn.'
  for f in fn: 
    args += " '" + f + "'"
  os.system(call.format(args))
  #os.system('git add ' + zName + '.z*')

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
