i. Boosting Bug-Report-Oriented Fault Localization
with Segmentation and Stack-Trace Analysis
Chu-Pan Wong, Yingfei Xiong, Hongyu Zhangy, Dan Hao, Lu Zhang, and Hong Mei

ii.
   1. **Motivating Examples** 
    
    C4.5 is a decision tree algorithm; it is an extension to ID3 algorithm.  Very popular algorithm.

   2. **K-NN**

   k-nearest neighbors algorithm is another classifiation algorithm, used in pattern mathcing. K-NN algorithm is used for regression as well.

   3. **Accuracy:**

   The tp + tn divided by tp+tn+fp+fn is the accurracy, which is a good measure of performance of the system. This in addition to other parameters will be usefull for the reasonable performance measure of the system.

   4. **ROC curve:**

   ROC Curves are another tools to compare the classifiers. Sensitivity is the measure of tp against total actual positives.  Specificity is measure on the other hand the number of true negatives against to actual negatives. 1-specificity gives the false positives against actual negatives. ROC curves  plotted between "hit rate", "recall rate" or "power", a.k.a sensitivity against "1-specificity" a.k.a false alaram rate. 
   
iii.

   2. **Information Visualisations :**
   Some figures on the methodlogy of the paper mentions which show the preprocessing, textual and categorical comparision (shown in fig 2 as well, with various kinds of comparisions applied across the features on the document), some examples of the duplicate  bug reports drawn from the data sets

   ![fig1](https://raw.githubusercontent.com/tnkteja/fss16ntadiko/hw5/read/5/.images/fig1.png)

   ![fig2](https://raw.githubusercontent.com/tnkteja/fss16ntadiko/hw5/read/5/.images/fig2.png)


   3. **Baseline Results :**

   ROC curve shows the results of applying KNN to various data set of the bug reports.

   ![fig2](https://raw.githubusercontent.com/tnkteja/fss16ntadiko/hw5/read/5/.images/fig34.png)

   4. **Related Work :**

   The paper shows various related works on information retrieval in software engineering, bug report deduplication, 

   5. **Data Sets :**

   The data sets used arebugs submitted for android between november 2007 and septtember 2012. The effective number of bug report after the filter of the improper bug reports is around 37200, out of which the duplicates are only 1063.

   6. **Future Work :**

iv.
  1.  The duplicates in the data set is quite low, the authors  could have chosen a good data, which has sufficient number of duplicates, making the learners more tuned for after training.
