import os

def get_dir_size(path = '.', display = False):
	'''Get Size of a Directory

	.. code-block:: python

		import py_utility_funcs.fileOps as puf

		dir_size = puf.get_dir_size(path = '.', display = False')
		puf.get_dir_size(path = '.', display = True')
		
	Parameters
	----------
	path: str
		Path of the directory (Relative or Absolute)
		(Default is path of directory from where the python script is executed)
	display: bool, optional 
		A flag used to print the size to the console (Default is False).

	Returns
	-------
	size: integer
		Total Size of the directory
	'''
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			if not os.path.islink(fp):
				try:
					total_size += os.path.getsize(fp)
				except:
					total_size += 0
	return total_size
	
def get_subdir_sizes(dirName = '.'):
	'''Print/Get Sizes of each sub folders in a Directory. (No recursion)
	Sizes are automatically displayed in KB/MB/GB/TB
	
	.. code-block:: python

		import py_utility_funcs.fileOps as puf

		subdir_sizes = puf.get_subdir_sizes(dirName = '.')
	
	Parameters
	----------
	dirName: str
		Path of the directory [Relative or Absolute]
		(Default is path of directory from where the python script is executed)

	Returns
	-------
	None
		All the sub directory/folder sizes are displayed on terminal 
	'''
	for x in  os.listdir(dirName):
		poi = os.path.join(dirName,x)
		if os.path.isdir(poi):
			total_size = get_dir_size(poi)

			if total_size> 1024 and total_size< 1024**2:
				print('{} : {} KB'.format(x,int(total_size/1024)))
			elif total_size> 1024**2 and total_size< 1024**3:
				print('{} : {} MB'.format(x,int(total_size/1024**2)))
			elif total_size> 1024**3 and total_size< 1024**4:
				print('{} : {} GB'.format(x,int(total_size/1024**3)))
			elif total_size> 1024**4:
				print('{} : {} TB'.format(x,int(total_size/1024**4)))
			else:
				print('{} : {} bytes'.format(x,total_size))

import pandas as pd			  
def get_subdir_sizes_in_dataframe(dirName = '.', display_df=True):
	'''Print/Get Sizes of each sub folders in a Directory sorted by size in descending order. (No recursion)
	Sizes are automatically displayed in MB. A pandas dataframe is also returned.

	.. code-block:: python

		import py_utility_funcs.fileOps as puf

		subdir_sizes_df = puf.get_subdir_sizes_in_dataframe(dirName = '.', display_df=True)
		
	Parameters
	----------
	dirName: str
		Path of the directory [Relative or Absolute].
		(Default is path of directory from where the python script is executed).
	display_df: bool, optional  
		Flag to indicate whether to display the dataframe in terminal (Default is True).

	Returns
	-------
	None
		All the sub directory/folder sizes are displayed on terminal 
	'''
	sDict = {}
	for x in  os.listdir(dirName):
		poi = os.path.join(dirName,x)
		if os.path.isdir(poi):
			total_size = get_dir_size(poi)
			sDict[x] = int(total_size)
	df = pd.DataFrame(list(sDict.items()),columns=['Dir Name', 'Size (MB)'])
	df['Size (MB)']= df['Size (MB)']/1024**2
	df = df.sort_values(by=['Size (MB)'],ascending =False)
	if display_df:
		print(df)
	return df

'''	
if __name__ == '__main__':
	
	print('Function --> {} <-- Result: {} \n\n'.format(get_dir_size.__name__, get_dir_size()))
	print('Function --> {}'.format(get_subdir_sizes.__name__))
	get_subdir_sizes()
	print('Function --> {}'.format(get_subdir_sizes_in_dataframe.__name__, ))
	get_subdir_sizes_in_dataframe()
'''