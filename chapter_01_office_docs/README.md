In the enterprise world, office docs(word, excel, and ppt) and pdfs are 
unavoidable. We populate timely data from various data sources to document
templates, in forms of raw data, generated images, or others.

For pdfs, we need to generate images by ourselves. Office docs can generate
images and tables with populated data. So office docs often serve as
templates with dynamic data "holes".

Java has Apache POI lib.

Platform neutral.

There are many libs for excel:
https://www.excelpython.org/
plus pywin32 on windows platform only.

Word and Excel has open hooks to allow refresh on open, PPT 2013 does not have.
Maybe PPT 2016 has.
 
Latex based docs are not under consideration since there is no such need in
practice
