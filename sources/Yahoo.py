import pystockquotes.sources.lib.ystockquote as ystockquote
from datasource import DataSourceAbstract

class DataSourceYahoo(DataSourceAbstract):
	
	def current_price(self, symbol):
		return ystockquote.get_price(symbol)

	def get_all(self, symbol):
		return ystockquote.get_all(symbol)
