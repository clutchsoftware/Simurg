from distutils.core import setup
setup(
  name = 'clutch-simurg',
  packages = ['clutch-simurg'],
  version = '0.1',
  license='MIT',
  description = 'Türkçe için yazım yardımcısı.',
  author = 'Clutch Software',
  author_email = 'clutchsoftwareteam@gmail.com',
  url = 'https://github.com/clutchsoftware/Simurg',
  download_url = 'https://github.com/clutchsoftware/Simurg/archive/0.1.tar.gz',
  keywords = ['turkish', 'nlp', 'natural language processing', 'yazım denetimi', 'simurg', 'clutch', 'pyqt5', 'python', 'turkce dil isleme'],
  install_requires=[
          'pandas',
          'numpy',
          'trnlp',
          'PyQt5'
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
