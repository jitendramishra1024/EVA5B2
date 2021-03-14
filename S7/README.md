# EVA5B2



# S7

# Advanced Convolution 

**Target**

Train CIFAR 10 with below constraints

**CONSTRAINT**

1.change the code such that it uses GPU

2.change the architecture to C1C2C3C40 (basically 3 MPs)

3.total RF must be more than 44

4.one of the layers must use Depthwise Separable Convolution

5.one of the layers must use Dilated Convolution

6.use GAP (compulsory):- add FC after GAP to target #of classes (optional)
achieve 80% accuracy, as many epochs as you want. Total Params to be less than 1M. 
upload to Github

**PARAMETER AND RECEPTIVE FIELD**

PARAMETER :94,218 

EPOCHS : 15 

MAX TRAIN ACCURACY :88.91

MAX TEST ACCURACY: 82.66

RECEPTIVE FIELD  :76 

**Link to the Code**

ATTEMPT 01 :

Attempted in jupyter notebook file 

https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/SOLUTION_PART_01/CIFAR10_JITENDRA.ipynb

COLAB LINK :

https://colab.research.google.com/drive/1FdvbEVLdjn2U-CXfIG7wSoG36gjLvGj6?authuser=1


ATTEMPT 02 :

Attempt after creating a package called SWAG_DNN .Same solution with neat code 

https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/SOLUTION_PART_02/CIFAR10_JITENDRA_OPTTIMIZED.ipynb

**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/Resources/TRAIN_TEST_ACC_LOSS.png" align="center" height="500" width="600" ></a>

**PER CLASS ACCURACY :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/Resources/PER_CLASS_ACCURACY.bmp" align="center" height="500" width="600" ></a>

**RECEPTIVE FIELD IMAGE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/Resources/RF_CALCULATION.bmp" align="center" height="500" width="600" ></a>

**MISCLASSIFIED IMAGE SAMPLE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/Resources/MISCLASSIFIED_IMAGE.png" align="center" height="500" width="600" ></a>

**RECEPTIVE FIELD EXCEL SHEET :**

https://github.com/jitendramishra1024/EVA5B2/blob/main/S7/Resources/RF_calculator_with_dialation_cifar_jitendra.xlsx
