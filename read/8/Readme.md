i. Panichella, A., Dit, B., Oliveto, R., Di Penta, M., Poshyvanyk, D., & De Lucia, A. (2016, March). Parameterizing and Assembling IR-based Solutions for SE Tasks using Genetic Algorithms. In 2016 IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER) (Vol. 1, pp. 314-325). IEEE.

ii.
   1. **GA - Information retrieval** 
   It is a task independent, unsupervised method which is combination of inormation retireval and genetic algorithms. GA-IR uses on a simple GA with elitism of two individuals.
   
   2. **Genetic Algorithm**

    It is stochastic optimizing method to find the optimal solution by mutating the solutions and keeping solutions which are fit using some fitness function. Final generation which is obtained as a result of the algorithm run over several genrations is considerred as optimal or close to optimal solution.

   3. **Accuracy:**

   The tp + tn divided by tp+tn+fp+fn is the accurracy, which is a good measure of performance of the system. This in addition to other parameters will be usefull for the reasonable performance measure of the system.

   4. **ROC curve:**

   ROC Curves are another tools to compare the classifiers. Sensitivity is the measure of tp against total actual positives.  Specificity is measure on the other hand the number of true negatives against to actual negatives. 1-specificity gives the false positives against actual negatives. ROC curves  plotted between "hit rate", "recall rate" or "power", a.k.a sensitivity against "1-specificity" a.k.a false alaram rate. 
   
iii.
  
   3. **Baseline Results :**
   
   The paper recall rate for the GA-IR method on short corpus is perfect in accuracy. it acieves 2-7% higher accuracy when compared to VSm and LSI techniques. With the corpus twice the short corpus length, it achieves almost 98% accuracy. Overall it outperforms VSM and LSI algorithsms by 2-16%.
   
   4. **Related Work :**
   
   Various methods are used to detec the duplicate bug report detection. For example REP, which is an advanced IR technique which relies  on high textual imilarity among duplicate bug reports.

   5. **Data Sets :**
   The paper used the data sets from Eclipse project.  which had two kinds, first is termed as shrt and cotains only the bug report tiel and the second termed 2Shortlong which contains th ebug report title and description.

   6. **Future Work :**

iv.
  1. The data set is quite low, the authors  could have chosen a good data, which has sufficient number of bug reports with various natures, making the learners more tuned for after training. Suppose data sets from arious projects been used , the results would have been much more interesting. 
