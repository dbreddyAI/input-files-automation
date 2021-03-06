from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get(url):
	"""
		This function checks for a valid API URL
		and returns the python object of the converted API JSON data;
		else, returns None
		Raises an exception in case of issues connecting to endpoints
	"""
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.json()
			else:
				return None
		
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
		
def is_good_response(resp):
	"""
	"""
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200
			and content_type is not None
			and len(resp.json()) > 2
			)
			
def log_error(e):
	"""
	"""
	print(e)