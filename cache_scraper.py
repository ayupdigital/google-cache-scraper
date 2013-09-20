import twill, sys, os, errno
from bs4 import BeautifulSoup
from StringIO import StringIO
from time import sleep

#
# CONFIGURATION
#
sleep_time      = 5
domain_name     = "http://www.example.com/"
data_store      = "pages/"
url_source      = "data.txt"

#
# START of script
#
base_url        = "http://webcache.googleusercontent.com/search?q=cache:"
url_data        = []
screen_output   = sys.stdout
data_output     = StringIO()
filename_exts   = [".html", ".htm", ".php", ".asp"]

def init():

  global url_source, url_data

  # Load all of the URLs into a list
  with open(url_source, 'r') as f:
    url_data = [line.strip() for line in f]

  # Start scraping at the beginning of the list
  for item in url_data:
    _scrape_cache(item)


def _scrape_cache(url):

  global url_data

  # Separate folders and filename from URL
  path      = _get_folder_and_filename(url)
  full_path = data_store + path[0] + "/" + path[1]

  # Check file does not exist (don't want to download files that we already have)
  try:
    with open(full_path): pass
    print "Skipped " + full_path

  except IOError:

    data = ""

    # Grab remote URL HTML data
    data = _grab_remote_html(url)

    # Make sure the dir exists, if not then create it
    _make_sure_path_exists(data_store + path[0]);

    # Parse HTML
    parsed_html = BeautifulSoup(data.getvalue(), "lxml")

    # Extract just the article section
    data = parsed_html.body.find('article', attrs={'class':'node'})

    if data is not None:

      # Ensure unicode chars are converted
      data = data.prettify(formatter="html")

      # Save the extract to disk
      _save_data(full_path, data)

      print "Saved " + full_path

    else:

      print "No article at " + full_path

    # Wait "sleep_time" seconds before doing anything else
    sleep(sleep_time)

#
# Grab HTML data
#
def _grab_remote_html(url):

  global base_url, data_output, screen_output

  twill.commands.clear_cookies()
  twill.commands.agent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.65 Safari/537.36')
  twill.commands.go(base_url + url)

  # Ensure we get a 200 http status code back
  try:
    code_response = twill.commands.code(200)
  except:
    code_response = ""

  # Step into the html and extract the links
  if code_response is None:

    # Reset buffer
    data_output.seek(0)
    data_output.truncate(0)

    # Change sys output to capture output in a variable
    sys.stdout = data_output
    twill.set_output(data_output)

    # Grab the HTML data which will be stored in data_reponse
    twill.commands.show()

    # Change the sys output back to the screen, now we have captured the data
    sys.stdout = screen_output
    twill.set_output(screen_output)

  return data_output

#
# Saves given data to a given path
#
def _save_data(path, data):

  f = open(path, 'w')
  f.write(data.encode('utf-8'))
  f.close()


#
# Return an array with two values, one with an array folders to be created, the other with the filename to be used
#
def _get_folder_and_filename(url):

  global filename_exts, domain_name

  validExtension = None

  # Remove protocol, domain and tld
  url = url.replace(domain_name, "")

  # Spit url structure into "folders"
  folders = url.split("/")

  # Ensure there is no trailing slash, if so, delete it
  if len(folders[-1:][0]) == 0:
    filename = folders[-2:][0]
  else:
    # The last item in the url split will be the "filename"
    filename = folders[-1:][0]

  # Remove the filename from the folders list
  folders = folders[:-1]

  # Join folders back up into a string
  folders = "/".join(folders)

  # Check if filename ends with a valid extension
  for ext in filename_exts:
    if filename.endswith(ext):
      validExtension = True
      break

  # Add .html to the end of the page name if no extension is present
  if validExtension == None:
    filename = filename + ".html"

  return [folders, filename]


#
# Try to create directory structure
# http://stackoverflow.com/a/5032238
#
def _make_sure_path_exists(path):

  try:
    os.makedirs(path)
  except OSError as exception:
    if exception.errno != errno.EEXIST:
      raise


# Lets kick this shit off
init()

#
# END of script
#