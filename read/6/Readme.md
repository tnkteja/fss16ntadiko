i. Boosting Bug-Report-Oriented Fault Localization
with Segmentation and Stack-Trace Analysis
Chu-Pan Wong, Yingfei Xiong, Hongyu Zhangy, Dan Hao, Lu Zhang, and Hong Mei

ii.
   1. **VSM , rVSM** 
   
   It is an algrbraic model for representing text documents as vectors of identifiers, like index terms. Used in information retrievl, indexing and relevancy rankings. rVSM is revised Vector Space mdel which considers the length of similarity score and length score by a ength function.
   
   2. **Top N Rank of Files (TNRF)**
   
   Top N ranked files give the percentage of bugs whose related files are listed in top N ( which is set to 1,5, and 10 in our evaluation) of returned fies.
   
   
   3. **Mean Reciprocal Rank ( MRR ):**
   The MRR metric measures overall effectiveness of retrieval for a set of bug reports.
   
   ![eq6](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/eq8.png)
   
   4. **Mean Average Precision ( MAP )**
   The MAP metric provides a way to meaasure the quality of retrieved files, when there are ore than one related file retrieved for the bug report.
   
   ![eq6](https://rawgit.com/tnkteja/fss16ntadiko/hw6/read/6/.images/eq9.png)
   
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
  1.  Some times the bugs not just from the souce code bug they are mere implementations of the technical report documents that come along during the development cycle. So when we use the technical specification reports also in the bug retrieval, even if we cannot point to the source file, we can find the relevant feature report and work our way down from there.
