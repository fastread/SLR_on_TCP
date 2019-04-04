# A systematic literature review on test case prioritization: 44-hour work by one graduate student with FASTREAD

FASTREAD: Search (8349, 1 hour for refining search string) -> Screen (242/470, 3 hours to reach 90% estimated recall with FASTREAD) -> full-text review (40 hours)

Validation: Search (783 containing 237/318 of the FASTREAD screening result) -> Screen (293/783 * 2, 2 * 6 hours) 

## [Search](https://github.com/fastread/SLR_on_TCP/tree/master/search)

 - IEEE Xplore: 
   + Keywords: (software AND test AND (rank OR optimi* OR prioriti*))
   + Number: 8349 = 8381 - 32(not research paper)
   + Url: 
```
https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&searchField=Search_All&queryText=(software%20AND%20test%20AND%20(rank%20OR%20optimi*%20OR%20prioriti*))&highlight=true&returnType=SEARCH&refinements=ContentType:Conferences&refinements=ContentType:Journals%20.AND.%20Magazines&returnFacets=ALL&rowsPerPage=100
```
 - Result: 
   + [search/ieeexplore.csv](https://github.com/fastread/SLR_on_TCP/blob/master/search/ieeexplore.csv)


## [Screen](https://github.com/fastread/SLR_on_TCP/tree/master/screen)

Rule:
 + about test prioritization (sometimes with test selection and test generation) (sometimes test optimization in the title includes test selection and prioritization)
 + NOT: only about test selection/reduction
 + NOT: only about test generation
 + NOT: about fault localization

Cost:
 + 1 hour to screen 158/192
 + 2 hours to screen 211/300 (8349) Estimated Number of Relevant Studies: 280
 + 3 hours to screen 242/470 (8349) Estimated Number of Relevant Studies: 266 (90% recall)

Result:
 + [screen/test_prior_90.csv](https://github.com/fastread/SLR_on_TCP/blob/master/screen/test_prior_90.csv)

## [Full-text review](https://github.com/fastread/SLR_on_TCP/tree/master/full-text)

Cost:
 + 40 hours to review 242 full-text papers.

Result:
 + [full-text/test_prior_90.xlsx](https://github.com/fastread/SLR_on_TCP/blob/master/full-text/test_prior_90.xlsx)

**Input type**:
 - 198 white-box
 - 36 black-box [59, 183] (source code, coverage information not available)

**Prioritization goals**:
 - 182 early fault detection
    + 156 APFD (including APFDc)
 - 32 max coverage (better coverage does not mean early fault detection [176])
 - 7 early failure exposing [59, 183, 199, 200]

**Method type**:
 - 137 unsupervised (using only coverage, source code, change information)
   + search-based (e.g. GA, ACO, PSO)
   + total coverage [167]: descending order of number of elements covered
   + additional coverage [167]: one test case cover largest number of elements -> test cases furthest to the ones already scheduled -> iterate until no more elements can be covered
   + clustering
 - 71 supervised (using failure information from previous runs or mutation testing information)
   + machine learning (LR, SVM)
   + frequency-based (simple count)
   + fault-exposing-potential [167], need coverage info, if one element is covered, how likely it will expose a fault based on previous execution results.
   + reinforcement learning from run to run
 - 10 active learning (using failure information from current run)
    
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
   
## [Validation](https://github.com/fastread/SLR_on_TCP/tree/master/validate)

Result:
 + [validate/validate.csv](https://github.com/fastread/SLR_on_TCP/blob/master/validate/validate.csv)

**Lessions learned from screening**: most relevant papers found contain the keyword prioriti* in the title or abstract (237/242). Therefore we use a smaller set of candidate papers to validate the FASTREAD screening result.
  + Keywords: (software AND test AND prioriti*)
  + Number: 783
  + file: prior.csv

**Three set of labels**:

 - FASTREAD (ZY 3 hours): 242/470 (8349), in prior: 237/(237+81=318), not in prior: 5/389

 - Manual review (6 people each 2 hours): 293/783 (783*2+174=1740)

 - Full-text validation (40 hours) on (ZY=yes OR Manual review=yes), label: 280/307

**FASTREAD (ZY) vs Manual review (Majority Vote)**

	+ TP: 223 (ZY=yes AND Majority Vote=yes)
	+ TN: 476=49+427 (ZY=no AND Majority Vote=no)+(ZY=undetermined AND Majority Vote=no)
	+ FP: 14 (ZY=yes AND Majority Vote=no)
	+ FN: 70=32+38 (ZY=no AND Majority Vote=yes)+(ZY=undetermined AND Majority Vote=yes)
	+ Precision: 0.94
	+ Recall: 0.76

**FASTREAD (ZY) vs Full-text validation (label)**

	+ TP: 234
	+ TN: 500=66+434
	+ FP: 3
	+ FN: 46=15+31
	+ Precision: 0.99
	+ Recall: 0.84=0.89*0.94

**Manual review (Majority Vote) vs Full-text validation (label)**

	+ TP: 266
	+ TN: 476
	+ FP: 27
	+ FN: 14
	+ Precision: 0.91
	+ Recall: 0.95
