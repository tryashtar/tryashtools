import os
import json

def read_json(path):
   with open(path, "r") as file:
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

def write_lines(lines, path):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      for line in lines:
         file.write(line+"\n")

def read_lines(path):
   with open(path, "r") as file:
      return [line.rstrip('\n') for line in file]

def write_lang(pairs, path):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      for k,v in pairs.items():
         file.write(f"{k}={v}\n")

def get_files(folder, recursive=False):
   for file in os.listdir(folder):
      full=os.path.join(folder,file)
      if os.path.isfile(full):
         yield full
      elif recursive:
         yield from get_files(full, True)

def get_folders(folder, recursive=False):
   for file in os.listdir(folder):
      full=os.path.join(folder,file)
      if not os.path.isfile(full):
         yield full
         if recursive:
            yield from get_folders(full, True)

def extension(filename):
   return os.path.splitext(filename)[1]

def remove_extension(filename):
   return os.path.splitext(filename)[0]

def path_list(filename):
   first,second=os.path.split(filename)
   if first=="":
      yield second
   elif second=="":
      yield first
   else:
      yield from path_list(first)
      yield second
