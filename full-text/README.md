Test case type: manual, unit, generated, ui, service
Input type: source code, abstract, description, history, code change, requirements
Prioritization goal: max coverage, early fault detection, max feature, severity
Method type: supervised, unsupervised, semi-supervised, active learning, reinforcement learning





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
    


classification of TCP types: Regression testing minimization, selection and prioritization: a survey