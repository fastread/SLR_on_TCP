# A systematic literature review on test case prioritization: 44-hour work by one graduate student with FASTREAD

FASTREAD: Search (8349, 1 hour for refining search string) -> Screen (242/470, 3 hours to reach 90% estimated recall with FASTREAD) -> full-text review (40 hours)

Validation: Search (783 containing 237/318 of the FASTREAD screening result) -> Screen (293/783 * 2, 2 * 6 hours) -> full-text validation for missing papers ((274-237)/(307-237) = 37/70, 6 hours)

## Cite As:
```
@ARTICLE{2019arXiv190907249Y,
       author = {{Yu}, Zhe and {Carver}, Jeffrey C. and {Rothermel}, Gregg and
         {Menzies}, Tim},
        title = "{Searching for Better Test Case Prioritization Schemes: a Case Study of AI-assisted Systematic Literature Review}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Software Engineering},
         year = "2019",
        month = "Sep",
          eid = {arXiv:1909.07249},
        pages = {arXiv:1909.07249},
archivePrefix = {arXiv},
       eprint = {1909.07249},
 primaryClass = {cs.SE},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019arXiv190907249Y},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

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

 - Full-text validation (40 hours) on (ZY=yes OR Manual review=yes), label: 274/307

**FASTREAD (ZY) vs Manual review (Majority Vote)**

	+ TP: 223 (ZY=yes AND Majority Vote=yes)
	+ TN: 476=49+427 (ZY=no AND Majority Vote=no)+(ZY=undetermined AND Majority Vote=no)
	+ FP: 14 (ZY=yes AND Majority Vote=no)
	+ FN: 70=32+38 (ZY=no AND Majority Vote=yes)+(ZY=undetermined AND Majority Vote=yes)
	+ Precision: 0.94
	+ Recall: 0.76

**FASTREAD (ZY) vs Full-text validation (label)**

	+ TP: 234
	+ TN: 507=69+438 (ZY=no AND Full-text=no)+(ZY=undetermined AND Full-text=no)
	+ FP: 3
	+ FN: 39=12+27 (ZY=no AND Full-text=yes)+(ZY=undetermined AND Full-text=yes)
	+ Precision: 0.99 (ZY precision)
	+ Recall: 0.85=0.90*0.95 (FASTREAD recall * ZY recall)

**Manual review (Majority Vote) vs Full-text validation (label)**

	+ TP: 259
	+ TN: 476
	+ FP: 34
	+ FN: 14
	+ Precision: 0.88
	+ Recall: 0.95
