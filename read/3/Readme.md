i. Towards More Accurate Retrieval of Duplicate Bug Reports Chengnian Sun, David Lo†, Siau-Cheng Khoo, Jing Jiang† School of Computing, National University of Singapore †School of Information Systems, Singapore Management University suncn@comp.nus.edu.sg, davidlo@smu.edu.sg, khoosc@comp.nus.edu.sg, jingjiang@smu.edu.sg

ii.
   1. **Master - Duplicate :** 
     Multiple bug report on same bugs results in a situation, so the first one is called *Master* and rest are *duplicate*. The idea is to separate the repition of same kind of bugs.
   2. **BM25F :**
     It is an effective textual similarity function for structured document retrieval (i.e document with several fields). It is a ranking function used in information retrieval.

   3. **Term Frequency-Inverse document frequency :**
    It is a numerical statistic that is intened to reflect how important a word is to a document in a ccollection or corpus.
   
   4. **Topic Proportion :**
     Describes the proportion of each topic corresponding to each position in the document. And parameter descrription table with initial values and example is shown.

iii.

   2. **Information Visualisations :**
     Figures showing the overall workflow of the duplicate bug report retrieval is shown. And a summary of the textual features.

     ![overallworkflow](https://rawgit.com/tnkteja/fss16ntadiko/hw3_v1.0-alpha-hotfix0/read/3/.images/overallworkflow.png)

     ![featuresinretrievalfuntion](https://rawgit.com/tnkteja/fss16ntadiko/hw3_v1.0-alpha-hotfix0/read/3/.images/featuresinretrievalfunction.png)

   3. **Baseline Results :**
     The paper shows the extended BM25F technique results in 10-27% improvement relative to recall rate and 17-23% in mean average precision over the then existing state-of-art techniques at  the time of this paper.

   4. **Related Work :**
     The paper presents the previous works using the nlp making feature value comparisions, on bug reports from Sony Ericsson Mobile Communications, with 40% detection. Another feature vector Construction approach with classification technique.

   5. **Data Sets :**
     The data sets were taken from the open source projects Mozilla browser and Thunderbird, Eclipse,OpenOffice. The paper claims that it has the large dataset than any contemporary studies.

   6. **Future Work :**
      The paper mentions abobut their plan to build indexing structure of bug report repository to increase the speed for the retrieval pocess. They also mentioned their plan to integrate their technique to Bugzilla.

iv.
  1. The paper mentions about using features ither than textual, like version no. product component id e.t.c but not all of which can be well generalised from project to project. Only using generalised features for comparsion could have been made.

  2. The paper could have added the associated source code files as another textual feature as whole to the bug report. 
  
  3.  Some developer comment on the  bug reports which also contain key inforamtion that can be used to retrieve bugs, the paper could have mentioned about the comments.