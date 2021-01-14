# EVA5B2





# S5

# ATTEMPT01

**Target :**
Ignore constraint make the model to get the skeleton correct
Achieve Model accuracy 99.4 at least 1 times in 15 epochs

**Constraint :**

Use less than 10 k paramter
Use less than 15 epochs 


**Parameters used :**104762

**Technique :**
INPUT SIZE Remark/Operation  OUTPUTSIZE  RF
28 		#1st conv			  26         3	
26		#2nd conv   		  24         5	
24		#1X1 conv			  24         5	
24		#maxpool			  12         6	
12		#3rd conv			  10         10	
10		#4th conv			   8         14	
8		#5th conv			   6         18	
6		#avg pool			   1         28	
1		#1X1 conv			   1         28	

Input output receptive field calculation 
https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/RF_calculator.xlsx

In all attempt we will use the same structure just difference will be channels
to reduce number of parametrer

**Extra Added :**
Batch Norm 

**Link to the Code **
https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_01.ipynb

**Result :**
BEST TRAIN ACCURACY :99.91

BEST TEST ACCURACY :99.43

**CONCLUSION :**

1. Still  Model has a lot of parameter 


**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/images/DRILL_01_IMG_99.4.png" align="center" height="500" width="600" ></a>



# ATTEMPT02

**Target :**

Follow model1 and make it small Achieve Model accuracy 99.4 at least 1 times in 15 epochs

**Constraint :**

Use less than 10 k paramter
Use less than 15 epochs 

**Parameters used :**
9862

**Technique :**
 Technique same as s5_Drill_01.ipynb
 https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_01.ipynb


**Extra Added :**
None . Just reduced channel size to reduce parameter

**Link to the Code **
https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_02.ipynb

**Result :**
BEST TRAIN ACCURACY :99.51

BEST TEST ACCURACY :99.31

**CONCLUSION :**

1. overfitting observed 


**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/images/DRILL_02_IMG_99.3.png" align="center" height="500" width="600" ></a>




# ATTEMPT03

**Target :**

Model accuracy 99.4 at least 5 times in 15 epochs

**Constraint :**

Use less than 10 k paramter
Use less than 15 epochs 

**Parameters used :**
9862

**Technique :**
 Technique same as s5_Drill_01.ipynb
 https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_01.ipynb


**Extra Added :**

Applied LR scheduler 
Applied Image Augmentation 

**Link to the Code **
https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_03.ipynb

**Result :**

BEST TRAIN ACCURACY :99.32

BEST TEST ACCURACY :99.49

**CONCLUSION :**

1. overfitting observed 


**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/images/DRILL_03_IMG_99.49.png" align="center" height="500" width="600" ></a>



# ATTEMPT04

**Target :**

Model accuracy 99.4 at least 1 times in 15 epochs with less than 8k parameter

**Constraint :**

Use less than 8 k paramter
Use less than 15 epochs 

**Parameters used :**
9862

**Technique :**
 Technique same as s5_Drill_01.ipynb
 https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_01.ipynb


**Extra Added :**

Same as attempt 03 
New thing added Tried with different step size in LR step
in step=10 we are able to get test accuracy 99.49

**Link to the Code **
https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/S5_Drill_04.ipynb

**Result :**

BEST TRAIN ACCURACY :99.35

BEST TEST ACCURACY :99.48 (99.4 more than 6 times out of 15 times)

**CONCLUSION :**

1. overfitting observed 


**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S5/ASSIGNMENT_CORRECT_SOLUTION/images/DRILL_04_IMG_99.41_LR_10.png" align="center" height="500" width="600" ></a>
