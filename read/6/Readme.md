i. Boosting Bug-Report-Oriented Fault Localization
with Segmentation and Stack-Trace Analysis
Chu-Pan Wong, Yingfei Xiong, Hongyu Zhangy, Dan Hao, Lu Zhang, and Hong Mei

ii.
   1. **C4.5** 
    
    C4.5 is a decision tree algorithm; it is an extension to ID3 algorithm.  Very popular algorithm.

   2. **K-NN**

   k-nearest neighbors algorithm is another classifiation algorithm, used in pattern mathcing. K-NN algorithm is used for regression as well.

   3. **Accuracy:**

   The tp + tn divided by tp+tn+fp+fn is the accurracy, which is a good measure of performance of the system. This in addition to other parameters will be usefull for the reasonable performance measure of the system.

   4. **ROC curve:**

   ROC Curves are another tools to compare the classifiers. Sensitivity is the measure of tp against total actual positives.  Specificity is measure on the other hand the number of true negatives against to actual negatives. 1-specificity gives the false positives against actual negatives. ROC curves  plotted between "hit rate", "recall rate" or "power", a.k.a sensitivity against "1-specificity" a.k.a false alaram rate. 
   
iii.
   1. **Motivating Examples**
   The paper presents two examples, one an example bug from Eclipse project, which contains information about the source of the bug,
   but not sufficient information for use with the Information Reteieval System to identify the bug. Another exaample is about some bug reports which consists of stack trace information, which when observed is likely that a bug resides in the one of the top ten functions.
   
   Another example was showing the underutilization of the stack trace information in bug report in which often at top 10 function call the bug source would be found most of the times.
   
   ![fig3](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/fig3.png)
   
   
   2. **Information Visualisations :**
   The paper shows how one source file is picked over the other file even though the other file was containing the source cause of the bug. Out of the six segments shown in the figure are of the other file and two are of the former file. Here scores from the segment B of the former file are dominating all other segments from the other file.

   ![fig3](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/fig2.png)
   
   3. **Baseline Results :**
   table 2 shows overall effictiveness of the Bug Locator and BRTracer,donot show good results for both the buglocator and BRTracer due to fuzzy nature of different descriptions in different bug reports.
   
   table 3 shows overall effectiveness of BRTracer considering similar bug reports. 
   ![table23](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/table23.png)
   
   ![table45](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/table45.png)
   
   Table 6 depicts the effectiveness of segmentation without considering similar bug reports. table 7 depicts the effectiveness of using only segmentation.
   
   ![table67](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/table67.png)
   
   4. **Related Work :**
   
   The paper shows some related work about the contemporary proposals, that improve IR-based bug localization with different kind of heuristics.  Some of them which proposed various heuristics. Some methods combined several feaures like  textual similarities between bug reports and source files, similarities of bug reports, number of previous bugs, stack trace informations. Some other approaches which  share same database as the project BLUiR, which had highest boost over BugLocator. About other lines of work on bug-report-oriented fault localization, which uses textual description of the fault to localize the fault, which may not totally solve the probelm of pointing oto the exact source file, but gives the eveloper some information about files potentially could contain the bugs.
   
   5. **Data Sets :**
   
   Data related to the source code files and to the bug reports are downloaded from Eclipse and SWT project. And for ASpectJ, the source code is downloaded from iBUGS. And for each subject project, the authors collected set of fixed bug reports from its tracking syste, and mined the links between bug reports and cource code files. In total the data set consisted of 3459 bug reports and links to their source code files.
   
   6. **Future Work :**

iv.
  1.  The duplicates in the data set is quite low, the authors  could have chosen a good data, which has sufficient number of duplicates, making the learners more tuned for after training.
