import json

class Dot:
  def __init__(self, s):
    self.str = s.split()
    self.str = ''.join(self.str)
    
  def get(self):
    s = self.str.split()
    s = ''.join(s).split(';')
    s = [i.split('=') for i in s]
    del s[-1]
    result = {i[0]: i[1] for i in s}
    return result
  
  def add(self, key, data):
    self.str += f'{key}={data};'
    
  def save(self, file, mode):
    try:
      with open(file, mode) as f:
        f.write(self.str)
      return 1
    except:
      return 0
      
  def save_json(self, file, mode):
    try:
      with open(file, mode) as f:
        s = '{'
        for i in self.get():
          s += f'"{i}":"{self.get()[i]}",'
        s = list(s)
        del s[-1]
        s = ''.join(s)
        s += '}'
        s = json.loads(s)
        json.dump(s, f)
      return 1
    except:
      return 0