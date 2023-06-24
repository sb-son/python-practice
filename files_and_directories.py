import os.path
import os
import datetime


def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)

    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  date = datetime.datetime.fromtimestamp(timestamp).date()
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{:%Y-%m-%d}".format(date))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd