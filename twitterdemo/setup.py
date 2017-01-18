from setuptools import setup

setup(name='pixiedust_twitterdemo',
      version='0.4',
      description='Pixiedust demo of the Twitter Sentiment Analysis tutorials',
      url='https://github.com/ibm-cds-labs/pixiedust_incubator/tree/master/twitterdemo',
      install_requires=['pixiedust'],
      author='David Taieb',
      author_email='david_taieb@us.ibm.com',
      license='Apache 2.0',
      packages=['pixiedust_twitterdemo'],
      include_package_data=True,
      zip_safe=False)