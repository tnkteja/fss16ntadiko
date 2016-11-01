i. ELBlocker: Predicting blocking bugs with ensemble imbalance learning Xin Xia a, David Lo b, Emad Shihab c, Xinyu Wang a,⇑, Xiaohu Yang a

ii.
   1. **Blocking bugs** 
    
    Bugs which are to be fixed first, so that other bugs or features can be fixed/develped without any dependencies. And take 2-3 times more time for completion incomparision to non-blocking bugs. The proportion of blocking bugs from other  bugs is less, which is known as class imbalance phenomenon.

   2. **Priority prediction**
   A bug triager needs to fix the priority of the bug assigned to him, from several priority levels. The bug proiority prediction can help the developer save time in assigning the priority  of bug after analysis but can schedule it based on the apredicted priority given in the bug report.
  
   3. **Multi-factor Analysis:**
   Takeing into account several factor for the bug report prediction is multifactor analysis. The features can be in several dimensions like temporal, textual, author, related-report, severity, and product.
   
   4. **ROC curve:**

   ROC Curves are another tools to compare the classifiers. Sensitivity is the measure of tp against total actual positives.  Specificity is measure on the other hand the number of true negatives against to actual negatives. 1-specificity gives the false positives against actual negatives. ROC curves  plotted between "hit rate", "recall rate" or "power", a.k.a sensitivity against "1-specificity" a.k.a false alaram rate. 
   
iii.

   1. Motivational Statements:
   The paper takes off after two research questions, which are whether  a predition model built on an ensemble of classsifiers which inturn are buiilt on subsets of the training bug reports achieve better performance compared to a model that is built sing all of the bug reports ? Another one is whether different decision boundaries or thresholds results in significantly different prediction performances?

   2. **Information Visualisations :**


   3. **Baseline Results :**

  
   4. **Related Work :**

   5. **Data Sets :**


   6. **Future Work :**

iv.
  1.  The duplicates in the data set is quite low, the authors  could have chosen a good data, which has sufficient number of duplicates, making the learners more tuned for after training.
