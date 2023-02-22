import os
import json
import shutil
import yaml

def setup_path(file : str):
   folder = os.path.dirname(file)
   if folder != "" and not os.path.isdir(folder):
      os.makedirs(folder)

def delete_folder(folder : str):
   if os.path.isdir(folder):
      shutil.rmtree(folder)

def delete_file(file : str):
   if os.path.exists(file):
      os.remove(file)

def copy_file(filefrom : str, fileto : str):
   setup_path(fileto)
   shutil.copyfile(filefrom, fileto)

def move_file(filefrom : str, fileto : str):
   setup_path(fileto)
   shutil.move(filefrom, fileto)

def write_yaml(y, path : str):
   setup_path(path)
   with open(path, "w", encoding="utf-8") as file:
      yaml.dump(y, file, default_flow_style=False, sort_keys=False, allow_unicode=True)

def write_json(j, path : str, mini=False):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      if mini:
         json.dump(j, file, separators=(',',':'))
      else:
         json.dump(j, file, indent=3)

def write_lines(lines : list[str], path : str):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      for line in lines:
         file.write(line+"\n")

def write_text(text : str, path : str):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      file.write(text)

def write_lang(pairs : dict[str,str], path : str):
   setup_path(path)
   with open(path, "w", encoding="utf8") as file:
      for k,v in pairs.items():
         file.write(f"{k}={v}\n")

def read_yaml(path : str):
   with open(path, "r", encoding="utf-8") as file:
      return yaml.load(file, yaml.CLoader)

def read_json(path : str):
   with open(path, "r", encoding="utf-8") as file:
      return json.loads(file.read())

def read_lines(path : str):
   with open(path, "r", encoding="utf8") as file:
      return [line.rstrip('\n') for line in file]

def read_text(path : str):
   with open(path, "r", encoding="utf8") as file:
      return file.read()

def get_items(folder : str, recursive=False):
   for file in os.listdir(folder):
      full = os.path.abspath(os.path.join(folder, file))
      if recursive and os.path.isdir(full):
         yield from get_items(full, True)
      yield full

def get_files(folder : str, recursive=False):
   for file in os.listdir(folder):
      full = os.path.abspath(os.path.join(folder, file))
      if os.path.isfile(full):
         yield full
      elif recursive:
         yield from get_files(full, True)

def get_folders(folder : str, recursive=False):
   for file in os.listdir(folder):
      full = os.path.abspath(os.path.join(folder, file))
      if os.path.isdir(full):
         yield full
         if recursive:
            yield from get_folders(full, True)

def base_name(filename : str):
   return remove_extension(os.path.basename(filename))

def extension(filename : str):
   return os.path.splitext(filename)[1]

def remove_extension(filename : str):
   return os.path.splitext(filename)[0]

def path_list(filename : str):
   first, second = os.path.split(filename)
   if first == "":
      yield second
   elif second == "":
      yield first
   else:
      yield from path_list(first)
      yield second
