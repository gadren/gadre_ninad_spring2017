# US Domestic Flight Analysis

Data source is the U.S. DoT Bureau of Transportation Statistics:
http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time

As I have used Basemap module for doing a few analysis, you may have to download the module on your system.
You need to run with administrator rights "Anaconda Prompt" and in "Anaconda Prompt" run following command:

**conda install -c conda-forge basemap-data-hires=1.0.8.dev0**

, it will show new packages that you need to install and will ask you to install it - say 'Yes'.
After that new packages will be installed

Air travel in the United States has improved over the years with increase in the number of airports per state or with increase in the number of carriers or increase in the number of flights and various such things. Also, due to increase in air traffic, number of flight cancellations and delay have increased. By taking all these things into considerations, we will try and analyze the improvements in the US domestic air travel. We will also use the data from recent years, just to analyze various reasons behind flight delay and cancellations.

## Analysis01
In this analysis we look at the number and fraction of delayed and cancelled flights for all airports across the United States for 3 different months namely May, August and December in the year 2016. In this analysis we will have insights over statistical difference in fractions of delayed and cancelled flights between May, August and December in the year 2016.

![1](https://cloud.githubusercontent.com/assets/25044649/25306221/e14ed3f4-2756-11e7-9557-8734c92e2ea8.png)
* **Graph1** : Overall number of flights cancelled is more in the month of August than May and December.
* **Graph2** : Overall number of flights delayed is more in the month of August than May and December.
* **Graph3** : Fraction of cancelled flights is more in month of December than May and August.
* **Graph4** : Fraction of delayed flights is more in month of May than December and August.

![2](https://cloud.githubusercontent.com/assets/25044649/25306224/e5991a78-2756-11e7-9160-2d35e7d653d4.png)
* **Map1** : In month of May flight cancellation and delay have been relatively low as weather is mostly sunny.
* **Map2** : In month of August flight cancellation and delay have been high in few areas especially in Texas, Nevada, Florida and New York as it        is usually considered to be the busiest period of the year for air travel.
* **Map2** : In the month of December flight cancellation and delay is relatively high in high altitude areas like Central America due to snow          and high winds.
