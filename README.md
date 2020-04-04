# Chem491-Stormwater-Project
(Current as of 2020.4.3)

This is the repository for the stormwater data mining project at 
CSU Channel Islands!We can imagine this project in a few discrete 
stages &mdash; Data acquisition, data wrangling and arranging, 
data exploration (e.g., PCA, covariance), and then the pretty 
graphs and charts.

### Data acquisition (Complete for F and G data)
The text from each PDF was extracted by ctrl-A and pasted into text files 
(see, e.g., ```data/raw/2019fg```). Text was then separated by whether or 
not it was F or G data (see ```data/precsv```) or non-data 
(see ```data/precsv/garbagefg.txt```). This was done with **historical/ExtractingData.py**.

### Data wrangling (F and G data complete)
Behold! ```data/TheFDataComplete.csv``` and ```data/TheGDataComplete.csv```.

Lines of data were separated by ```\n``` and ```' '``` and pieced back together 
in a .csv format using **historical/FDataGathering.py** and **historical/GDataGathering.py**, 
after which a LOT of cleaning had to be done to make names consistent and do band-aid 
fixes of errors due to my extracting method (e.g. ```y,Blank (HNO3||me equip blank``` 
had to be converted to ```Carboy Blank (HNO3||methanol),equip blank```). 
These fixes can be seen in **historical/FixingFData.py** and **historical/FixingGData.py**.

Presently (2020.4.3), the data is arranged exactly as it is in the PDFs, but will 
be more useful with pollutants along one axis and dates along another 
(and maybe sampling station along a third).

### Data arranging (About to start)
I imagine the structure will be ```index='Sample Dates'``` and ```header='Constituents'``` 
for covariance tests and a transpose will need to be done for PCA. Pollutants 
and analysis method will need to be combined (e.g., "Copper (LCS)" and "Copper 
(Matrix Spike)") so the ```Result``` column can be used as the values after 
doing the ```pandas.DataFrame.pivot_table()``` thing.

One option for arranging: we could create a 3-way tensor 
```(sampling date, pollutant name, sampling location)``` if I get proficient 
enough in that soon. Alternatively, a 2-way tensor ```(sampling date, pollutant name)``` 
can be created for each sample station individually, which might be more manageable 
in Excel.

### Data exploration
Clustering in PCA will reveal if certain pollutants are related and 
correlate with each other, especially in wildfire-relevant times, as 
will covariance. NMF may be valuable if some pollutant behaviors are 
wildfire-dependant and others are not.

Anyway, this is where the fun begins! We'll just have to get creative.

### PG;NP
Maybe determining a non-wildfire rhythm and subtracting it out (i.e. 
graphing only the pollutants' deviation from typical behavior) will 
be the most elegant way of making pretty pictures. We'll see what the 
exploration stage shows, though!
