def read_json(path):
   with open(path,"r") as file:
      return json.loads(file.read())

def setup_path(file):
   folder=os.path.dirname(file)
   if folder!="" and not os.path.isdir(folder):
      os.makedirs(folder)

def delete_folder(folder):
   if os.path.isdir(folder):
      shutil.rmtree(folder)

def delete_file(file):
   if os.path.exists(file):
      os.remove(file)

def copy_file(filefrom, fileto):
   setup_path(fileto)
   shutil.copyfile(filefrom, fileto)

def write_json(j, path, mini=False):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      if mini:
         file.write(json.dumps(j, separators=(',',':')))
      else:
         file.write(json.dumps(j, indent=3))

def write_lines(path, lines):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      for line in lines:
         file.write(line+"\n")

def write_lang(path, pairs):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      for k,v in pairs.items():
         file.write(f"{k}={v}\n")
