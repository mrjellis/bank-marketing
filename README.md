# Bank Marketing Success with Classifcation Models


Goals of this Project
------------------------
1. Learn to upload a dataset to postgresql and query from this source. 
2. Work on files structure for projects
3. Work on markdown skills :-)
4. Practice classification models available in sckit-learn. 


### Data source for this project 

https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

### Notes

1. The dataset used in the analysis is queried from a postgresql database. 
The data are not big enough to require this, however it was good practice. 
Alternatively, source data can be found in the `/Data`folder

2. Directions on the appropriate order to run the files are present in the `/Directions` folder text file.

### Classification Models Used
- Logistic Regression
- K Nearest Neighbors
- Random Forrest Classifier

# How to Run this Project

1. The data are contained in csv format `/Data/bank-full.csv` 
*    I loaded it into a postgre database for practice, feel free to just use the data from the file. 
2. Run `/scripts/connect.py` this will run the data load. 
3. Open the Jupyter Notebook file `/Notebooks/Bank-Marketing-Project-EDA` to view the analysis performed on the data before the classification models were run. 
4. Run `/scripts/data-transformation.py` to clean the data into usable format. 
5. Run the various classification models in `/Models/classification models.py`

