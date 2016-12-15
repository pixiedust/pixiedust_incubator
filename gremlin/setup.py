from setuptools import setup

setup(name='pixiedust_gremlin',
      version='0.1',
      description='Pixiedust extension for Gremlin',
      url='https://github.com/ibm-cds-labs/pixiedust_incubator/tree/master/gremlin',
      install_requires=['pixiedust','ibm_graph'],
      author='Alaa Mahmoud',
      author_email='mahmouda@us.ibm.com',
      license='Apache 2.0',
      packages=['pixiedust_gremlin'],
      include_package_data=False,
      zip_safe=False)