import py_utility_funcs.fileOps as puf
import pytest
import pandas as pd

def test_get_dir_size():
	v = puf.get_dir_size()
	assert isinstance(v, int) , "get_dir_size without args FAILED to return size"
	v = puf.get_dir_size(path='.',display = True)
	assert isinstance(v, int) , "get_dir_size with all args FAILED to return size"
	puf.get_dir_size(display = True)
	assert isinstance(v, int) , "get_dir_size with display set to TRUE FAILED to return size"
	puf.get_dir_size(display = False)
	assert isinstance(v, int) , "get_dir_size with display set to FALSE FAILED to return size"

def test_get_subdir_sizes():
	try:
		puf.get_subdir_sizes()
		assert "get_subdir_sizes PASS"
	except:
		assert "get_subdir_sizes FAILED"

def test_get_subdir_sizes_in_dataframe():
	v = puf.get_subdir_sizes_in_dataframe(dirName='.', display_df=True)
	assert isinstance(v, pd.DataFrame) , "get_subdir_sizes_in_dataframe with all args FAILED to return DataFrame"
	v = puf.get_subdir_sizes_in_dataframe(display_df=True)
	assert isinstance(v, pd.DataFrame) , "get_subdir_sizes_in_dataframe with Display = True FAILED to return DataFrame"
	v = puf.get_subdir_sizes_in_dataframe(display_df=False)
	assert isinstance(v, pd.DataFrame) , "get_subdir_sizes_in_dataframe with Display = False FAILED to return DataFrame"