#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1: Stock Analysis Using Python 
#step 1:import the necessary libraries:

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt



#step 2: Get historical stock data for Boeing Co. (BA)

symbol = 'BA'
start_date = '2015-01-01'
end_date = '2019-12-31'

ba_data = yf.download('BA', start='2015-01-01', end='2019-12-31', interval='1mo') #as we are looking for monthly log returns, I put the interval for 1 month

#step 3: Calculate Monthly Log Returns and Annualised Return:

#Log returns: 
ba_data['Log_Returns'] = np.log(ba_data['Adj Close'] / ba_data['Adj Close'].shift(1))
ba_data = ba_data.dropna()

# Subplots
fig, axs = plt.subplots(2, sharex=True, figsize=(10, 6))
fig.suptitle('Boeing Co Indices monthly (Jan 2015 - Dec 2019)')

# Plotting S&P 500
axs[0].plot(ba_data['Adj Close'], label='Boeing Co.', color='blue')
axs[0].set_ylabel('Price')
axs[0].legend()

# Plotting VIX
axs[1].plot(ba_data['Log_Returns'], label='LOG', color='red')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Log')
axs[1].legend()

plt.show()
#Annualised return: 
annualised_return = ba_data['Log_Returns'].mean() * 12
print(f"The annualised return of the BA stock is: {annualised_return:.4f}")


#step 4: Calculate Annualised Volatility 
annualised_volatility = ba_data['Log_Returns'].std() * np.sqrt(12)
print(f"The annualised volacity of the BA stock is: {annualised_volatility:.4f}")


#step 5: Download ESG Data and Handle Missing Values

ESG_data = yf.download('ESG', start='2015-01-01', end='2019-12-31', interval='1mo')

ESG_data['Log_Returns'] = np.log(ESG_data['Adj Close'] / ESG_data['Adj Close'].shift(1))
correlation = ESG_data['Log_Returns'].corr(ba_data['Log_Returns'])

# Create figure and subplot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting BA Index
color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('BA', color=color)  # Y label for BA
ax1.plot(ba_data['Close'], color=color)  # BA plot
ax1.tick_params(axis='y', labelcolor=color)  # Color for BA Y-axis labels

# Create a second Y-axis for plotting ESG
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('ESG', color=color)  # Y label for ESG
ax2.plot(ESG_data['Close'], color=color)  # ESG plot
ax2.tick_params(axis='y', labelcolor=color)  # Color for ESG Y-axis labels

# Adding title and displaying the plot
plt.title('BA and ESG Indices (Jan 2015 - Dec 2019)')
plt.show()
#Print the correlation coefficient
print(f"The correlation coefficient between the stock price and ESG score is: {correlation:.4f}")








# In[4]:


#Question 2: Climate Analysis Based on Birthplace

#step 1: importing necessary libraries
from meteostat import Point, Daily
from datetime import datetime
#step 2: Setting the Time Period

#Define the location for Lausanne, my birth place
latitude = 46.5197
longitude = 6.6323
altitude = 526
location = Point(latitude, longitude, altitude)  # Altitude is approximately 526 meters
T_base = 18 #Generally 18°C is used as base
#Define the time span for my birth month in 2022, for the CDD calculation
start = datetime(2022, 9, 1)
end = datetime(2022, 9, 30) #I was born in September

#Get daily data for Lausanne
data = Daily(location, start, end)
data = data.fetch()

#Plotting the Temperature Data
data.plot(y=['tavg'])
plt.title('Average Daily Temperatures for September 2022 in Lausanne')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()
#Calculate CDD september:
data['CDD'] = data['tavg'].apply(lambda x: max(x - T_base, 0))
total_CDD = data['CDD'].sum()



#Print the total CDD for my birthmonth:
print(f"Total Cooling Degree Days (CDD) for Lausanne in September 2022: {total_CDD:2f}")


start = datetime(2022, 4, 1)
end = datetime(2022,9, 30)

data = Daily(location, start, end)
data = data.fetch()


cdds = []
for temp in data.tavg:
    if not np.isnan(temp):
        cdds.append(max(temp - T_base, 0))
total_cdd = sum(cdds)



#Print the total CDD:
print(f"Total Cooling Degree Days (CDD) for Lausanne between April and September 2022: {total_cdd:2f}")


start = datetime(2022, 1, 1)
end = datetime(2022,3, 31)

data = Daily(location, start, end)
data = data.fetch()

data['tavg'].fillna(method='ffill', inplace=True)

#Print the total HDD:
hdds = []
for temp in data.tavg:
    if not np.isnan(temp):
        hdds.append(min(temp - T_base, 0))
total_hdd = sum(hdds)

print(f"Total HDD for Lausanne between January and April 2022: {total_hdd:2f}")

start = datetime(2022, 10, 1)
end = datetime(2022,12, 31)

data = Daily(location, start, end)
data = data.fetch()

hdds = []
for temp in data.tavg:
    if not np.isnan(temp):
        hdds.append(min(temp - T_base, 0))
total_hdd = sum(hdds)

print(f"Total HDD for Lausanne between October and December 2022: {total_hdd:2f}")


# In[ ]:


#Question 3:Critical Analysis on Cryptocurrencies and Environment 
#find the analysis on the word document

