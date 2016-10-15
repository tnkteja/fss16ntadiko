i. AA Statistical Semantic Language Model for Source Code , Tung Thanh Nguyen, Anh Tuan Nguyen, Hoan Anh Nguyen, Tien N. Nguyen, Electrical and Computer Engineering Department Iowa State University, Ames, IA 50011, USA

ii.
   1. **C4.5** 
    
    C4.5 is a decision tree algorithm; it is an extension to ID3 algorithm.  Very popular algorithm.

   2. **K-NN**

   k-nearest neighbors algorithm is another classifiation algorithm, used in pattern mathcing. K-NN algorithm is used for regression as well.

   3. **Accuracy:**

   The tp + tn divided by tp+tn+fp+fn is the accurracy, which is a good measure of performance of the system. This in addition to other parameters will be usefull for the reasonable performance measure of the system.

   4. **ROC curve:**

   ROC Curves are another tools to compare the classifiers. Sensitivity is the measure of tp against total actual positives.  Specificity is measure on the other hand the number of true negatives against to actual negatives. 1-specificity gives the false positives against actual negatives. ROC curves  plotted between "hit rate", "recall rate" or "power", a.k.a sensitivity against "1-specificity" a.k.a false alaram rate. 
   
   4. ****

iii.

   2. **Information Visualisations :**
   Some figures on the methodlogy of the paper mentions which show the preprocessing, textual and categorical comparision (shown in fig 2 as well, with various kinds of comparisions applied across the features on the document), some examples of the duplicate  bug reports drawn from the data sets

   ![fig1](https://rawgit.com/tnkteja/fss16ntadiko/tree/hw5/read/5/.images/fig1.png)

   ![fig2](https://rawgit.com/tnkteja/fss16ntadiko/tree/hw5/read/5/.images/fig2.png)


   3. **Baseline Results :**


   4. **Related Work :**

   5. **Data Sets :**

   The data sets used arebugs submitted for android between november 2007 and septtember 2012. The effective number of bug report after the filter of the improper bug reports is around 37200, out of which the duplicates are only 1063.

   6. **Future Work :**

iv.
  1.  The paper could have considered the source code files associated with bug reports and used them to improve the accuracy.

  2.  Although the training sets were enough for the model, date sets over more time frame would have been improved the accuracy of model prediction.
  
  3.  