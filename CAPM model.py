#!/usr/bin/env python
# coding: utf-8

# In[ ]:


risk_free_rate = float(input('What is the current long term government bond yeild, in % ? : '))
beta = float(input('What is the stock beta? : '))
market_rate = float(input("what is the current market return, in % (Eg return of S&P 500)? : "))
market_premium = market_rate - risk_free_rate
CAPM_return = risk_free_rate + beta*(market_premium)
print("The required rate for the investor to invest in this stock is {} %".format(CAPM_return))
input()


# In[ ]:




