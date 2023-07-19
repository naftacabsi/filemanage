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
	
	def overwrite(self, content, encoding: str = "utf-8"):
		"""Clears the file and writes to it."""
		with open(self.path, "w+", encoding=encoding) as f:
			f.write(content)
		return File(self.path)
	
	def write(self, content, encoding: str = "utf-8"):
		"""Does not clear the file and writes to it."""
		with open(self.path, "a+", encoding=encoding) as f:
			f.write(content)
		return File(self.path)
	
	def create(self):
		"""Creates a file. If the file exists it will be cleared."""
		with open(self.path, "w+") as f:
			f.close()
		return File(self.path)
	
	def clear(self):
		"""Clears a file. If the file does not exist None is returned."""
		if not os.path.isfile(self.path): return None
		with open(self.path, "w") as f:
			f.truncate()
		return File(self.path)