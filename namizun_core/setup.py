from setuptools import setup, find_packages

setup(name='namizun_core',
      version='1.4.0',
      description='namizun main functions',
      author='SinaEs',
      author_email='sina.eskandari0937@gmail.com',
      py_modules=['ip', 'database', 'time', 'network', 'log', 'udp'],
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']
      )
