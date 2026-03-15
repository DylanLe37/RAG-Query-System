import json

eval_set = []

question = {}
question['question'] = 'What is the eGFR threshold at which metformin is contraindicated?'
question['expected_answer'] = 'Metformin is contraindicated in patients with severe renal impairment defined as eGFR below 30 mL/min/1.73 m2.'
question['expected_drug'] = 'Metformin Hydrochloride'
question['expected_sections'] = ['contraindications']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Are there any risks with using metformin for diabetic patients?'
question['expected_answer'] = 'There is an increased risk of hypoglycemia when metformin is used in combination with insulin and/or insulin secretagogues'
question['expected_drug'] = 'Metformin Hydrochloride'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is there any risk in giving meloxicam to a patient with asthma? '
question['expected_answer'] = 'History of asthma as an allergic-type reaction after taking aspirin or other NSAIDs is contraindicated with Meloxicam'
question['expected_drug'] = 'meloxicam'
question['expected_sections'] = ['contraindications']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'At what age does pravastatin become a risk factor?'
question['expected_answer'] = 'Pravastatin is a risk factor for patients of age 65 years or greater.'
question['expected_drug'] = 'pravastatin sodium'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What are the side effects for ziprasidone?'
question['expected_answer'] = 'Ziprasidone has been observed to have common adverse reactions in patients with Schizophrenia as well as Manic and Mixed Episodes associated with Bipolar Disorder.'
question['expected_drug'] = 'ziprasidone hydrochloride'
question['expected_sections'] = ['adverse_reactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What are the effects of ziprasidone on patients with heart conditions?'
question['expected_answer'] = 'Ziprasidone has many contraindications related to myocardial health. It should not be used in patients with known history of QT prolongation, recent acute myocardial infarctions, uncompensated heart failure, or in combination with other drugs that have demonstrated QT prolongation.'
question['expected_drug'] = 'ziprasidone hydrochloride'
question['expected_sections'] = ['contraindications','indications_and_usage','warnings_and_cautions','drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is it ok to give ramipril to a diabetic patient?'
question['expected_answer'] = 'Ramipril should not be co-administered with aliskiren in patients with diabetes.'
question['expected_drug'] = 'Ramipril'
question['expected_sections'] = ['contraindications']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What CrCL threshold is considered safe to administer ranolazine?'
question['expected_answer'] = 'It is recommended to monitor renal function both initially and periodically in patients with moderate to severe renal impairment, measured at a CrCL of less than 60mL/min.'
question['expected_drug'] = 'Ranolazine'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Are there any issues with using repaglinide with clopidogrel?'
question['expected_answer'] = 'It is recommended to avoid concomitant use of Clopidogrel with Repaglinide. If they are used concomitantly, then Repaglinide should be initiated at 0.5mg before each meal and limited to a total daily dose of 4mg.'
question['expected_drug'] = 'Repaglinide'
question['expected_sections'] = ['drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is pregabalin ok to give to children?'
question['expected_answer'] = 'Common adverse reactions in pediatric patients for the treatment of partial-onset seizures are increased weight and appetite.'
question['expected_drug'] = 'Pregabalin'
question['expected_sections'] = ['adverse_reactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is there any issue with prescribing Paroxetine to patients with epilepsy?'
question['expected_answer'] = 'It is recommended to use Paroxetine cautiously in patients with a history of seizures or conditions that potentially lower seizure threshold.'
question['expected_drug'] = 'Paroxetine'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is oxybutynin fine to use in a patient on anticholinergics?'
question['expected_answer'] = 'No, it is not recommended. Patients co-administered Oxybutynin Chloride with other anticholinergic drugs may increase frequency and/or severity of anticholinergic-like effects. Additionally, pre-existing dementia symptoms can become aggravated when administered to patients treated with cholinesterase inhibitors.'
question['expected_drug'] = 'Oxybutynin Chloride'
question['expected_sections'] = ['warnings_and_cautions','drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What tyrosine levels are considered safe to use with Orfadin?'
question['expected_answer'] = 'Orfadin can increase patient tyrosine levels, and it is highly recommended to obtain slit-lamp examination prior to and regularly during treatment. Reexamination is recommended if tyrosine levels are >500 micromol/L or if symptoms develop.'
question['expected_drug'] = 'Orfadin'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What complications should we consider in administering mirabegron to patients with hypertension?'
question['expected_answer'] = 'Mirabegron can increase blood pressure in both adult and pediatric patients. It is not recommended in patients with severe uncontrolled hypertension.'
question['expected_drug'] = 'Mirabegron'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is metaxalone safe for patients with liver disease?'
question['expected_answer'] = 'No, severe renal and hepatic impairment are contraindications for Metaxalone.'
question['expected_drug'] = 'Metaxalone'
question['expected_sections'] = ['contraindications']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is Mesalamine safe for patients with renal conditions?'
question['expected_answer'] = 'No, it is recommended to asses renal function at the beginning of and periodically during treatment, as Mesalamine could potentially lead to renal impairment. Mesalamine also increases risks of nephrotoxicity when used with nephrotoxic agents, such as NSAIDs'
question['expected_drug'] = 'Mesalamine'
question['expected_sections'] = ['warnings_and_cautions','drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is it fine to prescribe Lorbrena to a patient who is also ona CYP3A related drug?'
question['expected_answer'] = 'No, Lorbrena is contraindicated with strong CYP3A inducers, and it is strongly recommended to discontinue strong CYP3A inducers for 3 plasma half-lives of the strong CYP3A inducer prior to initiating Lorbrena.'
question['expected_drug'] = 'Lorbrena'
question['expected_sections'] = ['contraindications','warnings_and_cautions','drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What complications exist for smokers taking iclevia?'
question['expected_answer'] = 'Iclevia is contraindicated in women over 35 who smoke, and cigarette smoking increases the risk of serious cardiovascular events from combination oral contraceptive use.'
question['expected_drug'] = 'Iclevia'
question['expected_sections'] = ['warnings']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What are potential drug interactions that may arise in a patient taking Guanfacine?'
question['expected_answer'] = 'The primary drug interactions for Guanfacine are related to CYP3A4 inhibitors and inducers. CYP3A4 inhibitors may increase guanfacine exposure, whereas CYP3A4 inducers may decrease the exposure.'
question['expected_drug'] = 'Guanfacine'
question['expected_sections'] = ['drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is it ok to prescribe cyclobenzaprine to patients also taking antidepressants?'
question['expected_answer'] = 'No, Cyclobenzaprine is structurally related to tricyclic antidepressants which have been reported to produce adverse cardiovascular effects.'
question['expected_drug'] = 'Cyclobenzaprine Hydrochloride'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'Is cyclobenzaprine safe to use in someone who has recently given birth?'
question['expected_answer'] = 'The Cyclobenzabrine label does not list any complications related to pregnancy or childbirth.'
question['expected_drug'] = 'Cyclobenzaprine Hydrochloride'
question['expected_sections'] = []
question['question_type']='negative'
eval_set.append(question)

question = {}
question['question'] = 'Is clozapine safe to use along with any other anticholinergics?'
question['expected_answer'] = 'No, it is recommended to avoid use with other anticholinergic drugs and use Clozapine with caution in patients with any conditions in which anticholinergic effects can lead to significant adverse reactions due to risk of anticholinergic toxicity.'
question['expected_drug'] = 'Clozapine'
question['expected_sections'] = ['warnings_and_cautions','drug_interactions']
question['question_type']='positive'
eval_set.append(question)

question = {}
question['question'] = 'What are the complications from giving Allopurinol to diabetic patients?'
question['expected_answer'] = 'There are no references to diabetes or insulin complications on the label for Allopurinol.'
question['expected_drug'] = 'Allopurinol'
question['expected_sections'] = []
question['question_type']='negative'
eval_set.append(question)

question = {}
question['question'] = 'What are the risks of prescribing Dronabinol to patients also taking CYP3A3 inhibitors?'
question['expected_answer'] = 'There are no references to CYP3A3 related drugs on the label for Dronabinol. There are, however, interactions with CYP2C9 and CYP3A4.'
question['expected_drug'] = 'Dronabinol'
question['expected_sections'] = []
question['question_type']='partial_negative'
eval_set.append(question)
question = {}
question['question'] = 'Is there any risk to prescribing entecavir to a patient with heart complications?'
question['expected_answer'] = 'There are no listed references to any cardiovascular complications on the drug label for Entecavir'
question['expected_drug'] = 'Entecavir'
question['expected_sections'] = []
question['question_type']='negative'
eval_set.append(question)

question = {}
question['question'] = 'Is it ok to use eszopiclone in patients with Hepatitis C?'
question['expected_answer'] = 'There are no listed references to any form of hepatitis on the drug label for Eszopiclone.'
question['expected_drug'] = 'Eszopiclone'
question['expected_sections'] = []
question['question_type']='negative'
eval_set.append(question)

question = {}
question['question'] = 'What are the risks of using Lamotrigine for a patient older than 65?'
question['expected_answer'] = 'There are no specific references to risks or warnings for patients older than 65 on the label for Lamotrigine.'
question['expected_drug'] = 'Lamotrigine'
question['expected_sections'] = []
question['question_type']='negative'
eval_set.append(question)

question = {}
question['question'] = 'Is levetiracetam safe to administer to patients with narcolepsy?'
question['expected_answer'] = 'There are no references to nacrolepsy on the drug label for Levetiracetam. However, there are warnings to monitor for somnolence and fatigue in patients until they have gained sufficient experience on levetiracetam.'
question['expected_drug'] = 'Levetiracetam'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='partial_negative'
eval_set.append(question)

question = {}
question['question'] = 'What considerations should be made for administering Maxalt to a patient on anticholinergics?'
question['expected_answer'] = 'No references are made to anticholinergic drugs on the label for Maxalt, though there is a warning to discontinue administration of Maxalt if serotonin syndrome occurs.'
question['expected_drug'] = 'Maxalt'
question['expected_sections'] = ['warnings_and_cautions']
question['question_type']='partial_negative'
eval_set.append(question)

question = {}
question['question'] = 'What complications would arise from using Ozempic in diabetic populations?'
question['expected_answer'] = None
question['expected_drug'] = None
question['expected_sections'] = []
question['question_type']='gate_trigger'
eval_set.append(question)

question = {}
question['question'] = 'What is the tyrosine risk threshold for a patient on phenyalanine?'
question['expected_answer'] = None
question['expected_drug'] = None
question['expected_sections'] = []
question['question_type']='gate_trigger'
eval_set.append(question)

question = {}
question['question'] = 'Is it safe to administer anavar to children?'
question['expected_answer'] = None
question['expected_drug'] = None
question['expected_sections'] = []
question['question_type']='gate_trigger'
eval_set.append(question)

question = {}
question['question'] = 'Are there complications from prescribing trenbolone to a patient with diabetes?'
question['expected_answer'] = None
question['expected_drug'] = None
question['expected_sections'] = []
question['question_type']='gate_trigger'
eval_set.append(question)

question = {}
question['question'] = 'What are the risks of GamerSups on a patient with heart complications?'
question['expected_answer'] = None
question['expected_drug'] = None
question['expected_sections'] = []
question['question_type']='gate_trigger'
eval_set.append(question)

with open('eval/eval_set.json', 'w') as f:
    json.dump(eval_set, f, indent=2)

print(f'Written {len(eval_set)} questions')