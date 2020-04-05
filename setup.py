'''

https://github.com/1hef001/createProject/blob/master/README.md

'''


from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

dependencies = []
setup(
    name='createProject',
    version='0.0.1',
    url='https://github.com/1hef001/createProject',
    long_description_content_type='text/markdown',
    license='MIT',
    author='S Ashwin',
    author_email='ashwins1211@gmail.com',
    description='create repo w/o hassle, both locally and in github. Let the module create it for you',
    long_description=long_description,
    packages=['createProject'],
    keywords=['git','github', 'create', 'project', 'createProject'],
    download_url='https://github.com/1hef001/createProject/archive/v0.0.1.tar.gz',
    # package_dir={'': os.getcwd()},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    scripts=['./createProject/createProject.py', './createProject/createRepo.py', './createProject/cred.py'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'createProject = createProject.createProject:main',
        ]
    },
    

    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
