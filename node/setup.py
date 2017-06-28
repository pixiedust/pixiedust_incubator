from setuptools import setup, find_packages

setup(name='pixiedust_node',
      version='0.1',
      description='Pixiedust extension for Node',
      url='https://github.com/ibm-watson-data-lab/pixiedust_incubator/tree/master/node',
      install_requires=['pixiedust'],
      author='David Taieb, Glynn Bird',
      author_email='david_taieb@us.ibm.com',
      license='Apache 2.0',
      packages=find_packages(),
      include_package_data=False,
      zip_safe=False)