# check the book Python Programming on Win32, chapter 12

import win32com.client as win32
import os

msword = win32.Dispatch('Word.Application')
# When msword is launched, it's from windows/systems directory.
cwd = os.getcwd()
doc = msword.Documents.Open(cwd + '/test_doc.docx')
print(doc.Content.Text)
input('waiting')
msword.Quit()
