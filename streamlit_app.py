import quantstats as qs
stock = qs.utils.download_returns('0P000073QD.TO')
qs.reports.full(stock, "SPY")
