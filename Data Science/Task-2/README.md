# Task-2


## Description

- It's called the <strong>#ExactInstructions</strong> challenge. 
- You've to write the exact instructions on how you accomplished what you did. 
- <strong>#ExactInstructions</strong> means that even if somebody is not a data scientist or doesn't even know anything about computers, they should be able to follow the instructions and get the tasks done.
- It literally means that you have to even mention minute things like: 
    - Switch on your laptop by clicking the power button 
    - Open the terminal or command prompt 
    - And so on.
- This <strong>#task</strong> is basically to check how deep you can go into the details of a task. 
- Feel free to be creative while doing this task. 


### Task-2

- Getting Started (ONLY WORKS WITH LINUX OS)
	- Open the lid of the laptop and click the power button
	- Do not forget to connect the charger wire to the laptop
	- Once you're logged in, open a terminal
	- Enter command - jupyter lab
	- If command not found
		- Enter command - pip install jupyterlab
		- If pip command not found
			- Enter command - sudo apt-get install python3-pip python-dev
			- If Python 3 not found
				- Enter command - sudo apt-get install python3.8
	- Now, you'll see a tab opened in your default browser.
	- Create a new python 3 notebook by selecting "Python 3"  from "Notebook" section under "Launcher" tab.
- You can basically copy my code from this [link](https://github.com/JayantUppal/Infinity/blob/master/Data%20Science/Task-1/Task-1.ipynb)
- Below is the basic explanation of code to make you familiar with data analysis and terms used.
	- At first you see, we are importing libraries. So these are basically programs and modules programmed by someone else to make our work easy. For example - Numpy, Pandas, Matplotlib etc.
	- Then, you'll see a class named Analysis. Now a class defines properties and behavior of any object. For example, a dog has properties - color, name, breed as well as behaviors – wagging the tail, barking, eating. So we are using Analysis class as we have different datasets but all of them has same behavior.
		- A term 'datasets' is used! What are datasets? These are basically used to store information. For example, we have a dataset of house prices and what factors affect its prices. Now the factors which affect prices are called columns. And the total number of observations we have, are called rows. Rows and columns together make up the dataset.
	- A class contains variables which defines the properties of the object and it contains functions which defines behavior of the object.
		- Variable basically means a place where we store our values and functions are lines of code which are used multiple times in the program.
	- First you see class variables in class Analysis. These are the common properties which each dataset will have. For example, each dataset has same target variable "Price".
		- Target variables is the one which we have to predict, which is dependent on multiple independent variables. For example, house price depends upon area of house, no. of bedroom etc.
	- Now, below class variables, you see a bunch of functions. First one is "__init__". It basically initializes some properties of the object when an object is made. 
		- Here we are storing the dataset into a dataframe for better analysis and visualization. Dataframe helps us to easily operate on dataset using simple lines of code. 
		- Also we are making a dataframe for numerical attributes only. Numerical attributes ? Numerical means a value within a range and attributes are basically columns. For example, area of house is a numerical attribute.
		- We are also removing duplicate observations and also checking for missing values. These both are done for getting better analysis. For example, if we have missing values in any column, we'll not get accurate analysis.
	- Following functions plots the variables' distribution. We should understand how the variables are distributed that means how frequent our values are, how far are they from each other and mean. 
		- PlotTargetVar function plots a graph to understand the distribution of target variable. i.e. Price.
		- PlotFeatures function plots a graph to understand the distribution of each feature so as to see any relation between them.
	- Following functions tell us how closely our attributes are related to each other.
	    - CorrTarget function gives us strongly related values with our target variable. For example, an increase in area or number of bedrooms, increases the value of the house price.
	    - CorrFeatures function gives us strongly related values among each feature. For instance, the cost of different houses having the same number of gymnasiums and swimming pools is the same. This observation also holds for houses having the same number of lifts and power backup. And many more.
	    - StrongCorrRegplot gives us a line which best fits the relation between target variable and the feature with strong relation.
	- Next we have functions dealing with categorical attributes. These attributes represents discrete values which belong to a specific finite set of categories. For example, grade has three categories - excellent, good and fair. 
	    -  CategoricalFeatures function gives us info about categories of attributes and their frequency.
	    -  CategorialToTarget function tells us the distribution of each category of an attribute to the house price.
	- OutlierAnalysis function detects and removes the outliers. Now what is an outlier? Lets assume, we want to calculate mean of revenues generated by a restaurant in a month. We'll calculate by the formula - sum of all revenues divide by total number of revenues. But what if, on any two or three days of month any rich family visits that restaurant and pays a lot of money. Now revenue generated for that day will increase and thus mean which is average of all values will not give us the exact central value and instead of that we get a value which is deviating more towards higher revenue. Now this mean of revenues generated is the right amount? NO. Now the revenue generated that two or three days will serve as an outlier. Thus we remove outliers when we want a better analysis.
	- TargetAnalysisLoc functiona analyze the house prices based on the location, we get top five locations with highest house prices and lowest house prices.
- To run each cell in the notebook, go to "Kernel" option in top bar and select option "Restart kernel and run all cells".
- Congratulations, you have begin your journey as a data scientist!
