# Chicago Pedestrian Traffic Accidents
### _by Zarak Tariq_
____________________________

**Introduction:** As of the 2020 US Census, the population of Chicago was 2,740,076 people.
Even though Chicago is a city with extensive public transit 
(especially by American standards), many Chicagoans still depend on walking or driving to get around.
In the era of the CAFE
standards, one must wonder about the effects of large cars driving in proximity to pedestrians.
To provide insight into 
this question, I propose to work on a combination of datasets,
with an aim to determine a correlation between the size of 
vehicles and pedestrian hospitalization rates.
Subsequently, this data will be correlated with a map of speed cameras in
the city,
in an attempt to determine if there is a substantial correlation between those cameras and the accident rates in a
+/- &frac14; mile radius.
Ultimately I propose to shed light on the pedestrian landscape and its dangers.

**Dataset Description and Significance:** There are the datasets proposed for consideration:
1. [Red Light Camera Locations](https://data.cityofchicago.org/Transportation/Map-Red-Light-Camera-Locations/7mgr-iety) 
2. [Traffic Crashes – Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/data_preview)
3. [Traffic Crashes – Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3/data_preview)
4. [Traffic Crashes – People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d/about_data)

The union of these datasets allows us to observe the effect of traffic crashes on the city population.
The Crashes dataset
displays details relating to every traffic incident that occurs within city limits.
We can then extract the make and model
of the car involved in the traffic incident from the Vehicles dataset.
Then we can take this information and bring it to the 
People dataset.
In doing so, we can learn about the effect of the car's crash on the pedestrian.
One of the data fields in
the People dataset is the hospital they were sent to.
Using these three pieces of information, I hope to determine if there
is a correlation between the size of the vehicle involved and the odds of a grave injury being sustained.
Finally, we can 
plot the accidents on the map of red light camera locations.
This will hopefully show us if there is a meaningful increase 
in accidents, in the vicinity of the cameras. 

**Importance:** The narrative from this data analysis aims to see if there is a statistically significant correlation between
the size of a car and the damage it may impart to passersby. The study addresses the challenge of accommodating both walking
and driving in a city with narrow streets. By examining statistical connections, the goal is to discern whether larger cars 
pose a significant risk to pedestrians, while automates are pushed to design larger cars. This exploration aims to 
shed light on the delicate balance required for safe and sustainable urban mobility.

**Deliverables:** By the end of February, the deliverables for this project will include:
1. Connection to the API and a basic understanding of its use.
   I hope to be able to access the data in all 4 portals reliably.
   Further than that I hope to be able to demonstrate a basic analysis of the data under consideration. 

Further deliverables will include:
1. Comprehensive Data Analysis Report: This report will include an examination of the datasets described above. The aim will be to provide a statistical analysis, complete with a visual component to be determined later.
2. Data Visualization: This would allow regular users to view crashes, hopefully by location, car type, and severity.
3. Academic paper: This would allow for a more in-depth explanation of the findings of this project to those with decision-making ability. 

**Resource and Assistance Requirements:** This project will be done using the Python-based tools ``pandas``, ``matplotlib.pyplot``, and JetBrains, ``Pycharm``. Access to data will be established via the Socrata API, supported by the Chicago Data Portal. There will also be a potential need to use the services of Google Maps. I will be using the help of the course instructor at length. 

**Work Schedule:** Every week I intend to put 10 hours into the project.
At the conclusion of every hour, I will record questions and stumbling blocks,
with the aim of bringing these issues to the course instructor.
These 10 hours will primarily be used to write the code of the data mining and the analysis.
However, I am also aware that much of the time will be spent reading documentation,
course material, or other supplemental aid.

**In conclusion** this proposal aims to analyze Chicago pedestrian traffic accidents,
exploring correlations between vehicle size, pedestrian injuries, and the proximity of speed cameras.
The deliverables include a comprehensive data analysis report, data visualization tools, and an academic paper,
contributing valuable insights to urban safety.
Utilizing Python tools, Socrata API, and potential Google Maps integration, the project ensures a systematic approach.
The commitment to weekly hours, collaboration with the instructor,
and structured problem-solving underline the dedication to a rigorous and impactful analysis.

