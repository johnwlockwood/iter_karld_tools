import os
import sys
import uuid

try:
    from setuptools import find_packages
    from setuptools import setup
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    packages = ['iter_karld_tools', 'iter_karld_tools.tests']

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read(fname):
    """
    Open and read a filename in this directory.
    :param fname: `str` file name in this directory

    Returns contents of file fname
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    import imp

    with open('iter_karld_tools/_meta.py', 'rb') as fp:
        mod = imp.load_source('_meta', 'iter_karld_tools', fp)

    return mod.version


def get_requirements(filename):
    """
    Get requirements from a file and
    convert to a list of strings.

    :param filename:
    :return:
    """
    with open(filename) as f:
        return list(f)


def get_test_requires():
    return get_requirements('requirements_dev.txt')


try:
    license_info = open('LICENSE').read()
except:
    license_info = 'APACHE 2.0'

setup_args = dict(
    name="iter_karld_tools",
    version=get_version(),
    author="John W Lockwood IV",
    author_email="john@tackletronics.com",
    description="More tools for iterators",
    license=license_info,
    keywords="data",
    url="https://github.com/johnwlockwood/iter_karld_tools",
    package_dir={'iter_karld_tools': 'iter_karld_tools'},
    packages=packages,
    tests_require=get_test_requires(),
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
