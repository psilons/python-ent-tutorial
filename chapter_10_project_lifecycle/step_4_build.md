### Package Builds
A setup.py is needed in the source folder, with packages and install_requires
specified. (Need to specify packages and all submodules to be included). Then
we can build the packages in several ways:
1. Update needed tools: pip install --upgrade setuptools wheel
2. To build package with source code: python setup.py sdist
3. To build package with wheel binaries: python setup.py bdist_wheel
4. To build package with egg binaries: python setup.py bdist_egg
5. To build package without source code: python setup.py bdist_egg 
--exclude-source-files  

There are four tools that need dependency.  
1. Conda
2. Pip
3. setup.py
4. IDE

The package is in the dist folder.

Sometimes, due to security reason, we cannot reach internet. So we have to 
download packages to disks and bring them over.

go to download folder
pip download <package1> <package2>
pip download -r environment.txt
The download should download both the named packages and dependencies

or specify the target save fold
pip download -d <dir> <package1> <package2>
pip download -d <dir> -r environment.txt

To install from local:
pip install --no-index --find-links="/path/to/downloaded/dependencies" packagename
pip install --no-index --find-links="/path/to/downloaded/packages" -r requirements.txt


PyInstaller is a good tool to convert Python code to binary executables, for
performance and obfuscation. Cython is another tool to compile Python code to
shared libraries.


scripts in bin folder are reusable without modification
