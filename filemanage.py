import os

class File():
	def __init__(self, path: str) -> None:
		self.path = path
		actp = path.replace("\\", "/").split("/")
		self.filename = "".join(actp[len(actp)-1:])
		actf = self.filename.split(".")
		self.ext = "".join(actf[len(actf)-1:])
	
	def read(self, encoding: str = "utf-8"):
		"""Returns the contents of the file. If the file does not exist None is returned."""
		if not os.path.isfile(self.path): return None
		with open(self.path, "r", encoding=encoding) as f:
			return f.read()
	
	def readlines(self, encoding: str = "utf-8"):
		"""Returns the lines of the file. If the file does not exist None is returned."""
		if not os.path.isfile(self.path): return None
		with open(self.path, "r", encoding=encoding) as f:
			return f.readlines()
	
	def rewrite(self, content, encoding: str = "utf-8"):
		"""Clears the file and writes to it"""
		with open(self.path, "w+") as f:
			f.write(content)
		return File(self.path)
	
	def write(self, content, encoding: str = "utf-8"):
		"""Does not clear the file and writes to it"""
		with open(self.path, "w+") as f:
			f.write(content)
		return File(self.path)
	
	def create(self):
		"""Creates a file. If the file exists it will be cleared"""
		with open(self.path, "w+") as f:
			f.close()
		return File(self.path)

# Everything below is meaningless, don't use it. Don't use filemanage at all
def fw(path, content):
	with open(path, "a+") as f:
		f.write(content)

def fwae(path, content):
	with open(path, "w+") as f:
		f.write(content)

def fc(path):
	with open(path, "w+") as f:
		pass

def fe(path):
	with open(path, "w+") as f:
		f.truncate()

def fr(path):
	with open(path, "r", encoding="utf-8") as f:
		return f.read()

def frl(path):
	with open(path, "r", encoding="utf-8") as f:
		return f.readlines()

def getlen(file):
    with open(file, "r+", encoding='utf-8') as f:
        len = 0
        for i in f:
            len+=1
        return len
