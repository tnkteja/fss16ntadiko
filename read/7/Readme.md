i. ELBlocker: Predicting blocking bugs with ensemble imbalance learning Xin Xia a, David Lo b, Emad Shihab c, Xinyu Wang a,⇑, Xiaohu Yang a

ii.
   1. **Blocking bugs** 
    
    Bugs which are to be fixed first, so that other bugs or features can be fixed/develped without any dependencies. And take 2-3 times more time for completion incomparision to non-blocking bugs. The proportion of blocking bugs from other  bugs is less, which is known as class imbalance phenomenon.

   2. **Random Forest Classifier**

   Random forests is a ensemble learning  method for classification, regression using various decision trees. They out the class which can be mode of the all classes or mean of the indiviual trees. They are good for avoiding overfiiting on their data set.

   3. **Accuracy:**

   The tp + tn divided by tp+tn+fp+fn is the accurracy, which is a good measure of performance of the system. This in addition to other parameters will be usefull for the reasonable performance measure of the system.

   4. **ROC curve:**

   ROC Curves are another tools to compare the classifiers. Sensitivity is the measure of tp against total actual positives.  Specificity is measure on the other hand the number of true negatives against to actual negatives. 1-specificity gives the false positives against actual negatives. ROC curves  plotted between "hit rate", "recall rate" or "power", a.k.a sensitivity against "1-specificity" a.k.a false alaram rate. 
   
iii.

   1. Motivational Statements:
   The paper takes off after two research questions, which are whether  a predition model built on an ensemble of classsifiers which inturn are buiilt on subsets of the training bug reports achieve better performance compared to a model that is built sing all of the bug reports ? Another one is whether different decision boundaries or thresholds results in significantly different prediction performances?

   2. **Information Visualisations :**
   Some figures on the methodlogy of the paper mentions which show the preprocessing, textual and categorical comparision (shown in fig 2 as well, with various kinds of comparisions applied across the features on the document), some examples of the duplicate  bug reports drawn from the data sets

   ![fig1](https://raw.githubusercontent.com/tnkteja/fss16ntadiko/hw5/read/5/.images/fig1.png)

   ![fig2](https://raw.githubusercontent.com/tnkteja/fss16ntadiko/hw5/read/5/.images/fig2.png)


   3. **Baseline Results :**

   

   ![fig2](https://raw.githubusercontent.com/tnkteja/fss16ntadiko/hw5/read/5/.images/fig34.png)

   4. **Related Work :**

   The paper shows various related works on information retrieval in software engineering, bug report deduplication, 

   5. **Data Sets :**

   The data sets come from 6 big open source projects - Freedesktop, Chromium, Mozilla, OpenOffice and Eclipse, with total of 402,962 bugs.

   6. **Future Work :**

iv.
  1.  The duplicates in the data set is quite low, the authors  could have chosen a good data, which has sufficient number of duplicates, making the learners more tuned for after training.
