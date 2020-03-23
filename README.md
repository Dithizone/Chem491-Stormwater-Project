# Chem491-Stormwater-Project
This is the repository for the stormwater data mining project at CSU Channel Islands! We can imagine this project in a few discrete stages &mdash; Data acquisition, data cleaning and arranging, data exploration (e.g., PCA, covariance), and then the pretty graphs and charts.

### Data acquisition (in progress)
There are quite a few Python libraries which deal with PDFs, but they either haven't been maintained or require lots of additional installs like Visual Studio C++, so the text from each PDF was extracted by ctrl-A and pasted into text files (see, e.g., ```data/raw/2019fg```). The data tables were then extracted and separated by whether they came from Appendix F or G (*F data* and *G data*, respectively), and molded into a .csv format.

The F data is complete and the G data is still in progress. Presently, the data is arranged exactly as it is in the PDFs, but will be more useful with pollutants along one axis and dates along another (and maybe sampling station along a third).

### Data cleaning and arranging
I imagine the structure will be ```index='dates'``` and ```header=pollutants``` for covariance tests and a transpose will need to be done for PCA. It may be necessary to express pollutants by both the pollutant name and by the sampling station location.

One option for arranging: we could create a 3-way tensor ```(sampling date, pollutant name, sampling location)``` if I get proficient enough in that soon.

Things to consider:
- Are there typos in pollutant names?
- Are there holes in the data (e.g., sampling days/stations missing)?
- Do the dates actually line up between stations and pollutants?
- \<update with more\>

### Data exploration
Clustering in PCA will reveal if certain pollutants are related and correlate with each other, especially in wildfire-relevant times, as will covariance. NMF may be valuable if some pollutant behaviors are wildfire-dependant and others are not.

Anyway, this is where the fun begins! We'll just have to get creative.

### PG;NP
Maybe determining a non-wildfire rhythm and subtracting it out (i.e. graphing only the pollutants' deviation from typical behavior) will be the most elegant way of making pretty pictures. We'll see what the exploration stage shows, though!
