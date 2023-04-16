from yaml import safe_load, dump

class Configurations(object):
	"""
	Configuations class for loading the yaml configurations file, used for managing the bot and database connection data
	the default configurations file is at config/config.yml, you can use a base to mount yours it's config/example.yml
	"""

	CONFIG_FILE = "config/config.yml"
	
	def __init__(self):
		"""
		Basic class constructor, defines the structure of the configurations that will be read by the class
		"""
		with open(self.CONFIG_FILE, "r") as config:
			self.config = safe_load(config)
	
	@property
	def bot_token(self):
		return self.config['bot']['token']
	
	@property
	def db_host(self):
		return self.config['database']['host']
	
	@property
	def db_user(self):
		return self.config['database']['username']
	
	@property
	def db_passwd(self):
		return self.config['database']['password']
	
	@property
	def db_dbname(self):
		return self.config['database']['dbname']
