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

## Analysis03
In this analysis we analyze the on-time performance of the flights in the the United States for the month of January 2017. The goal is to reveal pattern of flight delay due to airport characteristics, carrier and date and time of travel

![1](https://cloud.githubusercontent.com/assets/25044649/25306413/b26f3d9a-275a-11e7-98aa-17a881b0c521.png)

Data from 50 most busy airports according to number of total incoming and outgoing domestic flights

![2](https://cloud.githubusercontent.com/assets/25044649/25306414/b4879e7e-275a-11e7-868e-bd0569dc36a8.png)
![4](https://cloud.githubusercontent.com/assets/25044649/25306424/e84d0b9a-275a-11e7-96c0-c19b9074f5bf.png)
* The graph in upper left corner displays the on-time performance of flights based on Carriers. According to the graph, Hawaiian         Airlines, Alaska Airlines and American Airlines are the ones whose flights are on-time as Y-axis depicts delay ratio
* The graph in upper right corner displays the total number of flights each carrier had in the month of January in the year 2017
* The graph at bottom display the ratio of number of flights according to delay ratio

![3](https://cloud.githubusercontent.com/assets/25044649/25306415/b63374b4-275a-11e7-9e5b-9e271de392d1.png)

In the map above, airport locations are shown with circles color coded accordinf to on-time performance. The area of each circle is proportional to the total number of flights at that airport

## Analysis04
We will look at flight data for the month of December for years 1987, 1997 and 2016. We will try and analyze to find out in what ways airline travel has become better.

![1](https://cloud.githubusercontent.com/assets/25044649/25306444/5f8490d4-275b-11e7-86ee-c3ae90c7bcdc.png)
From above bar graph we can conclude that number of carriers were more in 1987 than 1997 and 2016
(1987 - 14) (1997 - 10) (2016 - 12)

![2](https://cloud.githubusercontent.com/assets/25044649/25306447/612c0a8e-275b-11e7-9bf3-6bda9135e7e4.png)
From above bar graph we can conclude that number of airports are more in 2016 than 1987 and 1997
(1987 - 234) (1997 - 202) (2016 - 297)

![3](https://cloud.githubusercontent.com/assets/25044649/25306448/62b9e164-275b-11e7-859c-89cdc9d0bdaf.png)
From above bar graph we can conclude that number of flights are more in 2016 than 1987 and 1997
(1987 - 440392) (1997 - 450889) (2016 - 460937)

![4](https://cloud.githubusercontent.com/assets/25044649/25306449/64679e16-275b-11e7-8dcb-5ddb2865e3ae.png)
From above bar graph we can conclude that number of flights per airport are more in 1997 than 1987 and 2016
(1987 - 1882) (1997 - 2232) (2016 - 1551)

![5](https://cloud.githubusercontent.com/assets/25044649/25306451/65cd08e0-275b-11e7-81aa-673fca857410.png)
In above graph we can see the count of number of flights per state for years 1987, 1997 and 2016 for the month of December. We can see there is significant increase in number of flights as the year progresses in the state of California and Florida

![6](https://cloud.githubusercontent.com/assets/25044649/25306453/67b32a36-275b-11e7-92f6-aae81c38cff1.png)
We can conclude from above airports from California state that Los Angeles, San Francisco, San Diego has most air traffic and the number of flights increase yearly

## Analysis05
In this Analysis, we will use delay data for flights and plot the delayed routes on map of the United States by using destination and origin using latitude and longitude of airports and also plot routes for delta airways and United airlines on map for the year 2016 and for the month January

![1](https://cloud.githubusercontent.com/assets/25044649/25306479/cff40570-275b-11e7-8a4d-aaae5916109a.png)
From above map we can see all the routes having delayed flights for the month of January in the year 2016

![2](https://cloud.githubusercontent.com/assets/25044649/25306481/d1f695f4-275b-11e7-9e9d-4aa9a560a88f.png)
Above map displays all the routes for Delta airways in the year 2016 for the month January. Also as Delta headquarters is in Atlanta, most of the flight routes are crowded near Atlanta

![3](https://cloud.githubusercontent.com/assets/25044649/25306483/e3225020-275b-11e7-9dc1-3bb717dd8fe7.png)
Above map displays all the routes for United airlines in the year 2016 for the month January. Also as United headquarters is in Chicago, most of the flight routes are crowded near Chicago
