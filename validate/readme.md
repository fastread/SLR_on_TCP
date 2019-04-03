validate.csv summarizes the validation process.

pior: 
  + Keywords: (software AND test AND prioriti*)
  + Number: 783
  + file: prior.csv

ZY (3 hours): 242/470 (8349), in prior: 237/(237+81=318), not in prior: 5/389

Manual review (6 people each 2 hours): 293/783 (783*2+174=1740)

Full-text validation (40 hours) on (ZY=yes OR Manual review=yes), label: 276/309


ZY vs Manual review (Majority Vote)
	TP: 223 (ZY=yes AND Majority Vote=yes)
	TN: 476=49+427 (ZY=no AND Majority Vote=no)+(ZY=undetermined AND Majority Vote=no)
	FP: 14 (ZY=yes AND Majority Vote=no)
	FN: 70=32+38 (ZY=no AND Majority Vote=yes)+(ZY=undetermined AND Majority Vote=yes)
	Precision: 0.94
	Recall: 0.76

ZY vs Full-text validation (label)
	TP: 234
	TN: 500=66+434
	FP: 3
	FN: 46=15+31
	Precision: 0.99
	Recall: 0.84

Manual review (Majority Vote) vs Full-text validation (label)
	TP: 266
	TN: 476
	FP: 27
	FN: 14
	Precision: 0.91
	Recall: 0.95





