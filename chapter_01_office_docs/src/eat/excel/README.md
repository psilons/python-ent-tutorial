There are 2 kinds of libraries when dealing with Excel files:
- pywin32 based: works only on windows. These libs can handle vba
- openxlsx based: This is based on open document standard.
  - xlwt/xlrd
  - xlsxWriter
  - openxlsx
  
Our goals are:
- create new xlsx documents: This needs touch on formatting, but not on
  charting, pivot tables or vba.
- fill data into existing xlsx documents
  We leave vba macro, formatting, charts untouched. When files are open,
  the open-doc hook can be triggered to run vba macros to refresh presentation
  based on new data.


https://python.libhunt.com/compare-xlsxwriter-vs-xlwt
