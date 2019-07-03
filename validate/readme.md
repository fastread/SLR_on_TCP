**Data files:**
 - validate.csv summarizes the validation process.
 - full-text_for_missing.csv records the full-text review labels for the missing files (ZY=yes OR Manual review=yes).
 - test_prior_missing.xlsx analyzes the distributions in missing files as well as in the early full-text reviewed files + missing files.

**Lessions learned from screening**: most relevant papers found contain the keyword prioriti* in the title or abstract (237/242). Therefore we use a smaller set of candidate papers to validate the FASTREAD screening result.
  + Keywords: (software AND test AND prioriti*)
  + Number: 783
  + file: prior.csv

**Three set of labels**:

 - FASTREAD (ZY 3 hours): 242/470 (8349), in prior: 237/(237+81=318), not in prior: 5/389

 - Manual review (6 people each 2 hours): 293/783 (783*2+174=1740)

 - Full-text validation (6 hours, full-text_for_missing.csv) on (ZY=yes OR Manual review=yes), label: (274-237)/(307-237) = 37/70

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





