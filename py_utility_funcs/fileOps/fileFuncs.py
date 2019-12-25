from os import listdir
from os.path import isfile, join

def find_file(dirPath = '.', regex='.txt'):
	'''
	Find Files in a directory by applying regular expression.

	Usage
	----------
	
	.. code-block:: python

		import py_utility_funcs.fileOps as puf

		found_files = puf.find_file(dirPath = '.', regex= '.py')
     
	
	Parameters
	----------
	dirPath: str
		Path of the directory (Relative or Absolute)
		(Default is path of directory from where the python script is executed)
	regex: str, optional 
		Regular Expression (Regex) to applied to search files (Default is /txt Files).

	Returns
	-------
	matchedFiles: file list 
		file list matching the regex search
		
	'''
	
	allFiles = [f for f in listdir(dirPath) if isfile(join(dirPath, f)) if regex in f]#f.endswith(regex)]
	matchedFiles=[dirPath+x for x in allFiles]
	return matchedFiles
	
	
def file2list(file,dtype=None):
	'''
	Read a file and get its content to a list

	Usage
	----------
	
	.. code-block:: python

		import py_utility_funcs.fileOps as puf

		mylist = puf.file2list(file = 'your_file.txt')
     
	
	Parameters
	----------
	file: str
		Path/Name of the File (Relative or Absolute)


	Returns
	-------
	listy: list
		contents of the input file in a list
		
	'''
	listy=[]
	with open(file) as fp:
		for lin in fp:
			cLine=lin.rstrip() if dtype==None else float(lin.rstrip())
			listy.append(cLine)
	fp.close()
	return listy