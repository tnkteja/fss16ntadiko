i. A Discriminative Model Approach for Accurate Duplicate Bug Report Retrieval Chengnian Sun1, David Lo2, Xiaoyin Wang3, Jing Jiang2, Siau-Cheng Khoo1 1School of Computing, National University of Singapore 2School of Information Systems, Singapore Management University
3Key laboratory of High Confidence Software Technologies (Peking University), Ministry of Education suncn@comp.nus.edu.sg, davidlo@smu.edu.sg, wangxy06@sei.pku.edu.cn, jingjiang@smu.edu.sg, khoosc@comp.nus.edu.sg

ii.
   1. **Support Vector Machine :** 
     It is a discrimintative model or classifier on labelled vectors, which separtes the  vectors into different classes with largest margin.

     ![iv1.png](https://rawgit.com/tnkteja/fss16ntadiko/hw4_v1.0-alpha-hotfix1/read/4/.images/iv1.png)
    
   2. **Term Frequency- Inverse Document Frequency:**
     Common term-weighting scheme. Term frequency is local to document. IDF is global importance measure.

   3. **Recall rate:**
    Recall rate is also called the sensitivity. It is the rate of true positives rate that we encounter in the dectection porcess, usually used to analyzie the accuracy of prediction for a learning model.
   
   4. **Similarity Measures - Cosine, Dice, Jacard**
    Two vectors can measured for similarity, cosine, dice and jacard are the techniques used to get the measures. Cosine measure gives the closeness in angular distance between the vectors. Dice index is also known as F1 score is also a similarity measure. Jacard index  measures the similartiy by measuring the number of dimension same in both vectors to the total remaing combination of dimensions. 

iii.

   2. **Information Visualisations :**
     Figures showing overall framework of the approach, repository organization into the bucket structure and flow diagram for the training model of the discriminative approach are shown. 
     
     ![iv2.png](https://rawgit.com/tnkteja/fss16ntadiko/hw4_v1.0-alpha-hotfix1/read/4/.images/iv2.png)

     And also feature extraction.
     
     ![iv3.png](https://rawgit.com/tnkteja/fss16ntadiko/hw4_v1.0-alpha-hotfix1/read/4/.images/iv1.png)
   

   3. **Baseline Results :**
     The baseline results show the recall rate over experiment on 3 datasets. The paper clamis that the improvement is achieved in their run, due to the 54 features and duscriminative approach they used. They show that the results putperform the previous works by 17-31%, 22-26% and 35- 43% on open office, Firefox, and Eclipse datasets respectively.

   4. **Related Work :**
     This paper presents some approachs previously used define vector spaces such as using TF and using measure like  - cosine , dice and jaccard for distance. Further iprovements of using TF and IDF for creating vectors, and additionally some clustering and classification techniques. And presents how the authors work improves on the previous works. It also presented about the statisticl study results and how they were used to predict the quality of the report.

   5. **Data Sets :**
     The data sets were taken from the open source projects Mozilla browser, Eclipse,OpenOffice. 

   6. **Future Work :**
      The paper talks about their technique to extract technical paraphrases and are working on improving their detectio accuracy using this additional technique.
iv.
  1.  The paper could have considered the source code files associated with bug reports and used them to improve the accuracy.

  2.  Although the training sets were enough for the model, date sets over more time frame would have been improved the accuracy of model prediction.
  
 
