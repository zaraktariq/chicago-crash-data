# Chicago Pedestrian Traffic Accidents
### _by Zarak Tariq_
____________________________

**Introduction:** The current population of Chicago is XX. Even though Chicago is a city with extensive public transit 
(especially by American standards), many Chicagoans still relay on walking or driving to get around. In the era of the ()
standards, one must wonder about the effects of large cars driving in proximity to pedestrians. To provide insight into 
this question, I propose to work on a combination of datasets, with an aim to determine a correlation between the size of 
vehicles and pedestrian hospitalization rates. Subsequently, this data will be correlated with a map of speed cameras in
the city, in an attempt to determine if there is a substantial correlation between those cameras and the accident rates in a
+/- &frac14; mile radius. Ultimately I propose to shed light on the pedestrian landscape and its dangers.

**Dataset Description and Significance:** There are the datasets is propose for consideration:
1. [Red Light Camera Locations](https://data.cityofchicago.org/Transportation/Map-Red-Light-Camera-Locations/7mgr-iety) 
2. [Traffic Crashes – Crases](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/data_preview)
3. [Traffic Crashes – Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3/data_preview)
4. [Traffic Crashes – People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d/about_data)

The union of these datasets allow us to observe the effect of traffic crashes on the city population. The Crashes dataset
displays details relating to every traffic incident that occurs within city limits. We can then extract the make and model
of the car involved the traffic incident from the Vehicles dataset. Then we can take this information and bring it to the 
People dataset. In doing so, we can learn about the effect of the car's crash on the pedestrian. One of the data fields in
the People dataset is the hospital they were sent to. Using these three pieces of information, I hope to determine if there
is a correlation between the size of the vehicle involved and the odds of a grave injury being sustained. Finally, we can 
plot the accidents to the map of red light camera locations. This will hopefully show us if there is a meaningful increase 
in accidents, in the vicinity of the cameras. 

**Importance:** The narrative from this data analysis aims to see if there is a statistically significant correlation between
the size of a car and the damage it may impart on passersby. The study addresses the challenge of accommodating both walking
and driving in a city with narrow streets. By examining statistical connections, the goal is to discern whether larger cars 
pose a significant risk to pedestrians, while automates are pushed to design cars that are larger. This exploration aims to 
shed light on the delicate balance required for safe and sustainable urban mobility.

**Deliverables:** By the end of February, the deliverables for this project will include:
1. Comprehensive Data Analysis Report: This report will include an examination of datasets described above. The aim will be to provide
a statistical analysis, complete with a visual component to be determined later.
2. Data Visualization: This would allow regular uses to view crashes, hopefully by location, car type, and severity. 