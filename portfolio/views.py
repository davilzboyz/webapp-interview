from django.shortcuts import render
from .models import Portfolios, StockReturns, Stocks
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockSerializer, PortfolioSerializer


class PortfolioViews(APIView):
	def get(self, request):
		portfolios = Portfolios.objects.all()
		serializer = PortfolioSerializer(portfolios, many=True)

		# portfolio_list = []
		# for p in portfolios:
		# 	row_data = {
		# 		'portfolioName': p.name,
		# 		'annualReturn': p.annual_rtn
		# 		# 'tickers': p.tickers
		# 	}
		# 	portfolio_list.append(row_data)

		return Response(serializer.data)

class SimilarPercentReturnViews(APIView):
	def get(self, request):
		ret_val = {
			'belowFive': {},
			'fiveToTen': {},
			'aboveTen': {}
		}
		portfolios_info = {}
		portfolios = Portfolios.objects.all().prefetch_related('tickers__portfolios_set')
		for p in portfolios:
			tickers = p.tickers.all()
			for t in tickers:
				portfolios_info[p.name] = {}
				total = 0
				count = 0
				ticker_return = StockReturns.objects.filter(ticker=t)
				for tr in ticker_return:
					total = total + tr.return_pct
					count = count + 1
				avg = total / count
				portfolios_info[p.name][t.ticker] = avg
				if avg < 5:
					if p.name not in ret_val['belowFive']:
						ret_val['belowFive'][p.name] = [{
							"ticker": t.ticker,
							"avg_return": avg}]
					else:
						ret_val['belowFive'][p.name].append({
							"ticker": t.ticker,
							"avg_return": avg})
				elif 5 <= avg < 10:
					if p.name not in ret_val['fiveToTen']:
						ret_val['fiveToTen'][p.name] = [{
							"ticker": t.ticker,
							"avg_return": avg}]
					else:
						ret_val['fiveToTen'][p.name].append({
							"ticker": t.ticker,
							"avg_return": avg})
				else:
					if p.name not in ret_val['aboveTen']:
						ret_val['aboveTen'][p.name] = [{
							"ticker": t.ticker,
							"avg_return": avg}]
					else:
						ret_val['aboveTen'][p.name].append({
							"ticker": t.ticker,
							"avg_return": avg})

		return Response(ret_val)
