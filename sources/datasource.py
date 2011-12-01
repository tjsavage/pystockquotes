
class DataSourceAbstract(object):
	def __init__(self):
		pass
	
	def current_price(self, symbol):
		raise NotImplementedError("Datasource hasn't implemented current_price")

	def get_all(self, symbol):
		raise NotImplementedError("Datasource hasn't implemented get_all.")
