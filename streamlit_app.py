import quantstats as qs
qs.extend_pandas()
stock = qs.utils.download_returns('0P000073QD.TO')
qs.reports.html(stock, "SPY")
