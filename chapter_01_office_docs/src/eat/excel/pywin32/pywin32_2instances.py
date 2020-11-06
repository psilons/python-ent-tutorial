import win32com.client as win32

# There is only one instance
excel_a = win32.Dispatch("Excel.Application")
excel_b = win32.Dispatch("Excel.Application")

excel_a.Visible = True
excel_b.Visible = True

excel_a.Quit()
excel_b.Quit()

# This is the way to get two instances, use ...Ex version
excel_a = win32.DispatchEx("Excel.Application")
excel_b = win32.DispatchEx("Excel.Application")

# now check to see whether we get two windows
excel_a.Visible = True
excel_b.Visible = True

print(excel_a.__module__)
print(excel_b.__module__)

print("two excel windows")
input("Press ENTER to exit")

# use ftype command to check the association
# if you don't see two windows. Check this:
#   Windows Explorer --> Tools -->Options --> File Types
#   find xls/xlsx, select Advanced button, click Open in the action window,
#   then click edit button, add "%1" (with quotes) to the end of the second
#   line.

excel_a.Quit()
excel_b.Quit()
