**Test case type**: manual, unit, generated, ui, service

**Input type**: source code, abstract, description, history, code change, requirements

**Prioritization goal**: max coverage, early fault detection, max feature, severity

**Method type**: supervised, unsupervised, semi-supervised, active learning, reinforcement learning





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
    

