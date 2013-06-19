~/Install/mmtsb/perl/loopModel.pl -models 200 -loop 1:PNRSISPS 150.pdb > modeller.scores
~/Install/mmtsb/perl/checkin.pl -dir ens model model.?.pdb model.??.pdb model.???.pdb
~/Install/mmtsb/perl/setprop.pl -dir ens -f modeller.scores -inx 3 model score
~/Install/mmtsb/perl/enscluster.pl -kclust -l 151:155 -nolsqfit -radius 4 -dir ens model
~/Install/mmtsb/perl/bestcluster.pl -dir -ens -prop score mod
