project name: use -

top package name: replace - with _ in project name
This has to be unique globally because Python does not merge packages from
different libraries. It will use the first found.

There is a gap in the current project setup process. The simple utils project
has a fix for this.
- Create dep_setup.py to specify dependencies, and add hooks to the setup.py.
    - copy dep_setup_utils.py
    
- Create src folder. When creating top package name, replace - in the project
  name with _. This has to be unique globally because Python does not merge 
  packages from different libraries. It will use the first found. Java has the
  merge, which is convenient.
  
- create test folder
    - copy __init__.py for the source hook
    
- copy bin folder - this is reusable component, no need to change.

- copy .gitignore

- create setup.py 

- create README.md and docs

