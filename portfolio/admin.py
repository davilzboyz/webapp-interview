from django.contrib import admin
from .models import Stocks, StockReturns, Portfolios


admin.site.register(Stocks)
admin.site.register(StockReturns)
admin.site.register(Portfolios)
