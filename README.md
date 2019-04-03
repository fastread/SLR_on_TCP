## A systematic literature review on test case prioritization: 40-hour work by one graduate student with FASTREAD

Search (8349, 1 hour for refining search string) -> Screen (211/300, 2 hours to reach 95% estimated recall with FASTREAD) -> full-text review (37 hours)

### Search

 - IEEE Xplore: 
   + Keywords: (software AND test AND (rank OR optimi* OR prioriti*))
   + Number: 8349 = 8381 - 32(not research paper)
   + Url: 
```
https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&searchField=Search_All&queryText=(software%20AND%20test%20AND%20(rank%20OR%20optimi*%20OR%20prioriti*))&highlight=true&returnType=SEARCH&refinements=ContentType:Conferences&refinements=ContentType:Journals%20.AND.%20Magazines&returnFacets=ALL&rowsPerPage=100
```

### Screen

Rule:
 + about test prioritization (sometimes with test selection and test generation) (sometimes test optimization in the title includes test selection and prioritization)
 + NOT: only about test selection/reduction
 + NOT: only about test generation
 + NOT: about fault localization

Cost:
 + 1 hour to screen 158/192
 + 2 hours to screen 211/300 (8349) Estimated Number of Relevant Studies: 222

### Full-text review

Cost:
 + 37 hours to review 211 full-text papers.

Input type:
 - 176 white-box
 - 31 black-box [59, 183] (source code, coverage information not available)

Prioritization goals:
 - 170 early fault detection
    + 149 APFD (including APFDc)
 - 28 max coverage (better coverage does not mean early fault detection [176])
 - 4 early failure exposing [59, 183, 199, 200]

Method type:
 - 130 unsupervised (using only coverage, source code, change information)
   + search-based (e.g. GA, ACO, PSO)
   + total coverage [167]: descending order of number of elements covered
   + additional coverage [167]: one test case cover largest number of elements -> test cases furthest to the ones already scheduled -> iterate until no more elements can be covered
   + clustering
 - 68 supervised (using failure information from previous runs or mutation testing information)
   + machine learning (LR, SVM)
   + frequency-based (simple count)
   + fault-exposing-potential [167], need coverage info, if one element is covered, how likely it will expose a fault based on previous execution results.
   + reinforcement learning from run to run
 - 9 active learning (using failure information from current run)
    
### Relation to automated UI testing:

 - Input type:
   + automated UI testing (system-level), a type of black-box testing. 
   + do not have access to source code or change information.
   + **only have test description and history failure information**.

 - Prioritization goal:
   + not coverage
     - most coverage information (statement, requirement, branch, function, etc.) is not available due to black-box testing.
     - better coverage does not mean early fault detection [176].
   + not APFD
     - cannot utilize mutation faults since black-box testing.
     - no knowledge of failure-fault mapping
   + **early failure** (can use similar calculation as APFD)

 - Method type:
   + **active learning**
     - failure information in current run reflects what has been changed
     - failure information in previous runs or test case descriptions can be used to find relationship between test cases. 
