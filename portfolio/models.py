from django.db import models


class StockReturns(models.Model):
	ticker = models.ForeignKey('Stocks', null=False, blank=False, on_delete=models.CASCADE)
	date = models.DateField()
	return_pct = models.FloatField()

	class Meta:
		unique_together = ('ticker', 'date')


class Stocks(models.Model):
	ticker = models.CharField(primary_key=True, max_length=6)
	name = models.CharField(max_length=100)


class Portfolios(models.Model):
	name = models.CharField(max_length=200)
	annual_rtn = models.FloatField()
	tickers = models.ManyToManyField(Stocks)
