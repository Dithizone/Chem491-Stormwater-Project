# Chem491-Stormwater-Project
This is the repository for the stormwater data mining project at CSU Channel Islands! We can imagine this project in a few discrete stages &mdash; Data acquisition, data cleaning and arranging, data exploration (e.g., PCA, covariance, etc.), and then the pretty graphs and charts.

### Data acquisition
This will employ something like PyPDF2 to pull the data from the PDF and probably a lot of regular expressions. It's important that we're confident we got everything, and that we got everything correctly.

### Data cleaning and arranging
I imagine the structure will be ```index='dates'``` and ```header=pollutants``` for covariance tests and a transpose will need to be done for PCA. It may be necessary to express pollutants by both the pollutant name and by the sampling station location.

One option for arranging: we could create a 3-way tensor ```(sampling date, pollutant name, sampling location)``` if I get proficient enough in that soon.

Things to consider:
- Are there typos in pollutant names?
- Are there holes in the data (e.g., sampling days/stations missing)?
- \<update with more\>

### Data exploration
Clustering in PCA will reveal if certain pollutants are related and correlate with each other, especially in wildfire-relevant times, as will covariance. NMF may be valuable if some pollutant behaviors are wildfire-dependant and others are not.

Anyway, this is where the fun begins! We'll just have to get creative.

### PG;NP
Maybe determining a non-wildfire rhythm and subtracting it out (i.e. graphing only the pollutants' deviation from typical behavior) will be the most elegant way of making pretty pictures. We'll see what the exploration stage shows, though!
