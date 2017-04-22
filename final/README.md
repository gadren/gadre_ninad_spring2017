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

## Analysis02
This analysis focuses on the relaiability of carrier based on cancellation and also detail reasons behind the cancellation of flights based on carrier for the year 2016 for the month of January 

![1](https://cloud.githubusercontent.com/assets/25044649/25306339/36ed86e6-2759-11e7-8685-b7e5822b1a8a.png)
The graph on left shows the number of successful flights by a particular carrier and the right grph shows the number of flight cancellations a particular carrier had in the month of January in the year 2016

![2](https://cloud.githubusercontent.com/assets/25044649/25306341/38d072fc-2759-11e7-8d5f-0f6061003e91.png)

The above grph is depicts the percentage of flights cancelled in January 2016, from which we can conclude Hawaiian Airlines is the most reliable airline

![3](https://cloud.githubusercontent.com/assets/25044649/25306343/3afbfd6c-2759-11e7-9e70-2dd093240264.png)

The above graph gives the relative frequency for each cancellation reason of flight per carrier. We can conclude from above graph that none of the flight for any carrier was cancelled for security reason in January 2016. Delta Air lines Inc. was the most reliable airliner in January 2016 in terms of cancellations. Most of the flights were cancelled due to weather conditions or the national air system.

![4](https://cloud.githubusercontent.com/assets/25044649/25306344/3cf5ad48-2759-11e7-895b-6a85c99bcb2a.png)

Hawaiian Airlines Inc. is the clear winner, with an average delay of only 3 minutes. From these results it becomes apparent that it has less problems with late aircrafts compared to their competition. Spirit Air Lines has the highest departure delays. If they want to improve their service, they can compensate by lowering their late aircraft delays (by e.g. using more planes) and internal restructuring reducing the carrier delays.

![5](https://cloud.githubusercontent.com/assets/25044649/25306345/3eedb05a-2759-11e7-9015-009c51502d97.png)

From these results we see that most of the delays are of short narture. Security delays are most often of smaller periods compared to weather, late aircrafts, carrier or NAS conditions.

![6](https://cloud.githubusercontent.com/assets/25044649/25306347/4083cb66-2759-11e7-90b8-a8c93d052ebf.png)

We can observe that there are indeed higher delays for the more northern regions, compared to their more southern regions. The highest weather delays are caused between 40 and 50 degrees latitude
