# EVA5B2



# S9

# CIFAR 10 with RESNET With Albumentation(CUTOUT, and GRADCAM 

**Target**

Train CIFAR 10 with below constraints

**CONSTRAINT**


**CIFAR 10 RESNET CONSTRAINT  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S8/Resources/TASK.PNG" align="center" height="500" width="600" ></a>

**ALBUMENTATION SAMPLE :**

Albumentation used :

            PadIfNeeded(min_height=36, min_width=36),
			
            RandomCrop(32, 32),
			
            HorizontalFlip(),
			
            Cutout(num_holes=4)
			
			Normalize 
			
			Totensor 
			

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/TASK_SESSSION-9.PNG" align="center" height="500" width="600" ></a>


**PARAMETER AND RECEPTIVE FIELD**

PARAMETER :11,173,962(RESNET 18 )

EPOCHS : 20

MAX TRAIN ACCURACY :95.63

MAX TEST ACCURACY: 91.53


** CONCLUSION USING ALBUMENTATION **

LESS OVERFITTING 


**Link to the Code**


Attempted in jupyter notebook file 

https://github.com/jitendramishra1024/EVA5B2/blob/main/S8/CIFAR10_JITENDRA_RESNET_CORRECT.ipynb



**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/TRAIN_TEST_ACCURACY.png" align="center" height="500" width="600" ></a>

**PER CLASS ACCURACY :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/perclassaccuracy.PNG" align="center" height="500" width="600" ></a>

**MISCLASSIFIED IMAGE SAMPLE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/MISCALSSIFIED.PNG" align="center" height="500" width="600" ></a>

**ALBUMENTATION  SAMPLE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/ALBUMENTATION_SAMPLE.PNG" align="center" height="500" width="600" ></a>

**GRADCAM OF USER PROVIDED IMAGE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/GRADCAMOFUSERDEFINED.PNG" align="center" height="500" width="600" ></a>


**GRADCAM OF USER PROPERLY CLASSIFIED  IMAGE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/GRADCAMOFCLASSIFIED.PNG" align="center" height="500" width="600" ></a>

**GRADCAM OF MISCALSSIFIED  IMAGE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/GRADCAMOFMISCLASSIFIED.PNG" align="center" height="500" width="600" ></a>








