from setuptools import setup,find_packages

about = {}
with open("py_utility_funcs/__about__.py") as fp:
    exec(fp.read(), about)


with open('README.rst') as readme_file:
	readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()
	
setup(name='py_utility_funcs',
      version=about['__version__'],
      description='Python Utility Wrapper Functions for Daily Use',
      url='https://github.com/achdF16/mars',
      author=about['__author__'],
      author_email='vj338@nyu.edu',
      license=about['__license__'],
      #install_requires=['h5py', 'silx', 'keras','opencv-python', 'mtcnn', 'tensorflow'],
	  install_requires=['pandas'],
      packages=find_packages(),
	  include_package_data=True,
	  package_data={
	  '': ['*.pyd',
			#'*.pyc', 
			'*.h5', '*.json','*.txt' ],
	  },
	  long_description=readme + history,
      classifiers=[
          'Development Status :: 1 - Development/Stable',
          'Intended Audience :: Science/Research',
          'Topic :: General/Engineering',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      zip_safe=True,
	  python_requires='>=3',
      extras_require={
          'test': ['pytest'],
      },
	  )
