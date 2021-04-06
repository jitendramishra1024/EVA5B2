# EVA5B2



# S10

# CIFAR 10 with RESNET LR FINDER

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
			

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S10/RESOURCES/TASK_S10.PNG" align="center" height="500" width="600" ></a>


**PARAMETER AND RECEPTIVE FIELD**

PARAMETER :11,173,962(RESNET 18 )

EPOCHS : 50

MAX TRAIN ACCURACY :97.12

MAX TEST ACCURACY: 91.23


** CONCLUSION USING ALBUMENTATION **

QUICK CONVERGENCE


**Link to the Code**


Attempted in jupyter notebook file 

https://github.com/jitendramishra1024/EVA5B2/blob/main/S10/CIFAR10_JITENDRA_LR_FINDER.ipynb



**LOSS AND ACCURACY OF TRAIN AND TEST  :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S10/RESOURCES/TRAIN_TEST_LOSS_ACC.png" align="center" height="500" width="600" ></a>

**PER CLASS ACCURACY :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S9/RESOURCES/perclassaccuracy.PNG" align="center" height="500" width="600" ></a>

**MISCLASSIFIED IMAGE SAMPLE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S10/RESOURCES/MISCLASSIFIED.PNG" align="center" height="500" width="600" ></a>

**GRADCAM OF MISCALSSIFIED  IMAGE :**

<a href="url"><img src="https://github.com/jitendramishra1024/EVA5B2/blob/main/S10/RESOURCES/MISCLASSIFIED_GRADCAM.PNG" align="center" height="500" width="600" ></a>








