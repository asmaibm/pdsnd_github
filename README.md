# *EXPLORE US BIKESHARE DATA*

# Project Title
**EXPLORE US BIKESHARE DATA**

# Description
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles for short trips, typically 30 minutes or less. due to the rise in informations technologies, it is easy for a user of this system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

  > We will perform an exploratory analysis on data provided by [Motivate] (https://www.motivateco.com ), a bike-share system provider for many major cities in the United States. We will compare the system usage between three large cities: New York City, Chicago, and Washington.
  > This project, will allow the user to explore an US bikeshare system database and retrieve statistics information. The user is able filter the information by city, month and weekday, in order to visualize statistics information related to a specific subset of data.

# Running the program:
You can input **bikeshare.py** on your terminal to run this program.

# Program Details:
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (from January to June), and day for which the user wants to view data.
Upon receiving the user input, the DataFrame for the analysis is created.
it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:
  - Most popular month
  - Most popular day
  - Most popular hour
  - Most popular start station
  - Most popular end station
  - Most popular combination of start and end stations
  - Total trip duration
  - Average trip duration
  - Types of users by number
  - Types of users by gender (if available)
  - The oldest user (if available)
  - The youngest user (if available)
  - The most common birth year amongst users (if available)
Finally, the user is prompted with the choice of restarting the program or not.


# Project Data:
Stored in the data folder:
- **chicago.csv** file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity. 
- **new_york_city.csv** - Dataset containing all bikeshare information for the city of New York provided by Udacity. 
- **washington.csv** - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data. 

# Built with / Requirements::
- [Python 3.6.6](https://www.python.org/downloads/release/python-366/) or above We use the following libraries :
  - [pandas](https://pandas.pydata.org) - One of the libraries used for this.
  - [numpy](https://numpy.org) - One of the libraries used for this.
  - [time] (https://docs.python.org/2/library/time.html)- One of the libraries used for this.
I am using MACBOOK AIR as machine for this work .

# Author:

* [Asma Benotsmane](https://github.com/asmaibm) - author for this program.


# Acknowledgements:

1. [Udacity](https://www.udacity.com) - Udacity's Data Analyst Nanodegree program and their instructors were extremely helpful.
2. [stackoverflow](https://stackoverflow.com/questions)
       -  Python datetime formatting without zero-padding
       -  Get month name from number
       -  How to keep repeating a program until a specific input is obtained ?
       -  create a Python function with optional arguments
       -  How to convert seconds to hours, minutes and seconds ?
       -  Native Python function to remove NoneType elements from list
3. for plot :
       - (https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5559011-realisez-de-beaux-graphiques-avec-seaborn)
        - (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html)
        - (https://python-graph-gallery.com/all-charts/)
        - (https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline)
        - (https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html)
