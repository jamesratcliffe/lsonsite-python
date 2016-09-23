from distutils.core import setup

setup(
    name='lsonsite-python',
    version='1.0',
    description='Requests for Lightspeed OnSite',
    url='https://github.com/jamesratcliffe/lsonsite-python.git',
    author='James Ratcliffe',
    license='OSL',
    packages=['lsonsite'],
    install_requires=['requests (>=2.11.0)', 'xmltodict (==0.10.2)'],
    extras_require={'Photo Example': ['Pillow (==3.3.1)']}
)
