# stdlibs import
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re
import time
import urllib2

# core django imports
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class Base(object):
    pass


class Saham(Base):

    url = 'http://finance.yahoo.com/q/hp?s=%5EJKSE+Historical+Prices'

    def download_csv(self):
        html = urllib2.urlopen(self.url).read()
        pattern = re.compile(r'http://real-chart.*=\.csv"')
        m = re.search(pattern, html).group()

        with open('table.csv', 'wb') as f:
            f.write(urllib2.urlopen(m).read())


class DataSaham(Base):

    # def get_df(self):
    #     df = pd.read_csv('table.csv', index_col='Date', parse_dates=True)
    #     df = df.sort_index(ascending=True)
    #     df = df.tail(80)
    #     return df
        pass


class DataProcessing(Base):

    # ds = DataSaham()
    # df = ds.get_df()
    
    # def macd(self):
    #     # MACD analysis
    #     macdjson = pd.rolling_mean(self.df['Adj Close'], 12).to_json()
    #     return macdjson

    # def bollingerbands(self):
    #     pass
    pass


class IndexView(View):

    template_name = 'index.html'

    def get(self, request):
        """Regular get method.
        TODO:
        - check if 'usia' table.csv > 1 hari, download again.
        """
        # dp = DataProcessing()
        # data = dp.macd()
        # return render(request, self.template_name, {'macd': self.process_csv})
        # return HttpResponse(data, content_type='application/json')
        # return HttpResponse('hello django!')
        return render(request, self.template_name, {'name': 'django!'})
