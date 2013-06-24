BASE_1='/home/jms/1KBH/ANAL/EOM_Complex/Models_'
LIST_1='1','2','3','4','5','6','7','8','9','10'

F=open('EOM_analysis_complex.sh','w')

BASE_2='/home/jms/ACTR/EOM/Models_'
LIST_2='1','2','3''4','5'

G=open('EOM_analysis_actr.sh','w')

run=1 #which GA run # number you are analyzing
for filename in LIST_1:
    print>>F, "cd "+BASE_1+filename+'Data/Selected00'+str(run)
    print>>F, "python2.7 ~/Projects/SULI/EOM_selected_models_chemicalshift.py "
    print>>F, "echo 'Chemical shift on selected models Done' "

    print>>F, "cd",BASE_1+filename+'Data/Selected00'+str(run)+'/Selected00'+str(run)
    print>>F, "python2.7 ~/Projects/SULI/EOM_secstruct_select.py ../GA00"+str(run)+'/bestcurve00'+str(run)+".txt"
    print>>F, "ptraj ~/1KBH/ANAL/1KBH1_ww.prmtop trajin_select_models"
    print>>F, "python2.7 ~/Projects/SULI/EOM_plot_secstruct_compare.py"

for filename in LIST_2:
    print>>G, "cd",BASE_2+filename+'Data/Selected00'+str(run)
    print>>G, "python2.7 ~/Projects/SULI/EOM_selected_models_chemicalshift.py "
    print>>G, "echo 'Chemical shift on selected models Done' "

    print>>G, "cd",BASE_2+filename+'Data/Selected00'+str(run)+'/Selected00'+str(run)
    print>>G, "python2.7 ~/Projects/SULI/EOM_secstruct_select.py ../GA00"+str(run)+"/bestcurve00"+str(run)+".txt" 
    print>>G, "ptraj ~/1KBH/ANAL/1KBH1_ww.prmtop trajin_select_models"
    print>>G,"python2.7 ~/Projects/SULI/EOM_plot_secstruct_compare.py"

		