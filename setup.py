from setuptools import setup
from TwitterSearch import __version__

def readme():
    with open('README.md') as f:
        return f.read()

def requirements():
    req = []
    for line in open('requirements.txt','r'):
        req.append(line.split()[0])
    return req

setup(name='TwitterSearch',
      version=__version__,
      description='A library to easily iterate tweets found by the Twitter Search API',
      long_description=readme(),
      url='http://github.com/ckoepp/TwitterSearch',
      author='Christian Koepp',
      author_email='christian.koepp@tum.de',
      license='MIT',
      packages=['TwitterSearch'],
      keywords='twitter api search',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
      ],
      install_requires=requirements(),
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3', 'httpretty']
      )
