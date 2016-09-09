i. A Topic-based Approach for Narrowing the Search Space of Buggy Files from a Bug Report Anh Tuan Nguyen, Tung Thanh Nguyen, Jafar Al-Kofahi, Hung Viet Nguyen, Tien N. Nguyen Electrical and Computer Engineering Department Iowa State University {anhnt,tung,jafar,hungnv,tien}@iastate.edu

ii.
   1. **Bug file localization :** 
     The process of finding all the buggy or defective files associated with a particular bug report.
     A developer assigned to a bug performs bug file localization.
   2. **S-Component :**
     The S-Component is a LDA model applied to a source file , which is influenced by the topic distribution parameter and other LDA model parameters.

   3. **B-Component :**
     The B-Component is LDA model applied to the bug report along with all associated buggy files. The topic distribution parameter is derived out of these files.
   
   4. **Topic Proportion :**
     Describes the proportion of each topic corresponding to each position in the document.

iii.
   1. **Motivating Statements :**
     Three Examples of bug reports were given taken from among the 3 year data of the software development. It is shown that while a bug report and source file might contain several technical aspects/topics, they share some topics with each other.


   2. **Information Visualisations :**
     Figures showing the LDA model of the bugreport is provided. And also a BugScout Model is also represented with parameters and dependencies.

   3. **Baseline Results :**
     Accuracy and Sensiticity comparisions were performed. Accuracy comparisions were made on all data sets and contrasted with previous works on *BugLoc*, *VSM+LDA*, *SVM*.

   4. **Sampling Method :**
     Gibbs sampling method is used for the Training Algorithm, which is estimating the parameters iteratively using distribution from other sampled values until they converge.

   5. **Data Sets :**
     The publicaly availbale data sets were collected from several software projects IBM-Jazz, Eclipse, AspectJ, ArgoUML. The data sets all have `Java` in common. Each data set is composed of three parts: *set of bug reports*, *source code files*, *mapping from bug reports*


iv.
  1. The paper only takes into account source code which is well commented, but could also have commented on the accuracy on poorly commented source files. 

  2. The paper assumes only buggy source files, but when the source files are fixed, the fixed version might contain some more comments, as usally developer may choose to add additional comments when fix the bugs. Using these comments also algorithm would have been an nice touch.

  3. Most of the source code generally has the classes, functions, methods, variables named in topics, the paper does not comment on this, any mention of this aspect could be nice.