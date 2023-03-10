from setuptools import setup

setup(
    name = 'dwlib',
    version='0.0.1',
    description='Personal library to compute and draw',
    url ='https://github.com/dowoonlee/dwlib.git',
    author='dwlee',
    author_email='',
    license='dwlee',
    packages=['dwlib'],
    zip_safe=False,
    install_requires=[
        'numpy==1.22.3',
        'matplotlib==3.5.2',
        'astropy==5.1',
        'scipy==1.7.3',
        'pandas==1.4.3',
        'imageio==2.19.3'
    ]
)