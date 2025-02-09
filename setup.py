# setup.py

from setuptools import setup, find_packages

setup(
    name='datavalidator',
    version='0.1.0',
    description='A simple data validation library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='o_frun',
    url='https://github.com/yourusername/datavalidator',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
