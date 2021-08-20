from rest_framework import serializers
from .models import Stocks, Portfolios


class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stocks
		fields = ('ticker', 'name')


class PortfolioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Portfolios
		fields = ('name', 'annual_rtn', 'tickers')
