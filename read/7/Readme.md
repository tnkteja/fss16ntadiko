i. Automated prediction of bug report priority using multi-factor analysis Yuan Tian, David Lo, Xin Xia and Chengnian Sun

ii.
   1. **Blocking bugs** 
    
    Bugs which are to be fixed first, so that other bugs or features can be fixed/develped without any dependencies. And take 2-3 times more time for completion incomparision to non-blocking bugs. The proportion of blocking bugs from other  bugs is less, which is known as class imbalance phenomenon.

   2. **Priority prediction**
   A bug triager needs to fix the priority of the bug assigned to him, from several priority levels. The bug proiority prediction can help the developer save time in assigning the priority  of bug after analysis but can schedule it based on the apredicted priority given in the bug report.
  
   3. **Multi-factor Analysis:**
   Takeing into account several factor for the bug report prediction is multifactor analysis. The features can be in several dimensions like temporal, textual, author, related-report, severity, and product.

   
iii.

   1. Motivational Statements:
   The paper takes off after two research questions, which are whether  a predition model built on an ensemble of classsifiers which inturn are buiilt on subsets of the training bug reports achieve better performance compared to a model that is built sing all of the bug reports ? Another one is whether different decision boundaries or thresholds results in significantly different prediction performances?
  
   4. **Related Work :**
     The paper provided some study on the time needed to fix the bugs . Some statistics like average bug fixing time, bg fixing time distribution, files with highest fixing time. It also shows some work about automated approach that predicts the number of developer hours needed to fix a bug. They plan to test with ore bug reporsts and improve upon their accuracy.

   6. **Future Work :**
   The tool is potentially regarded for the developers as recommender system to prioritize bugs to be fixed. The work is planned for integration with bugzilla.

iv.
  1.  The data could be from various projects which could have improved the training efficiency and prediction as well.
