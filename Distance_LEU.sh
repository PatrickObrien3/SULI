for filename in LEU*
do
echo $filename >> listofnames.txt
~/Install/mmtsb/perl/mindist.pl 10 13 $filename >> 10_13_dist.txt 
~/Install/mmtsb/perl/mindist.pl 10 14 $filename >> 10_14_dist.txt 
~/Install/mmtsb/perl/mindist.pl 10 17 $filename >> 10_17_dist.txt
~/Install/mmtsb/perl/mindist.pl 10 30 $filename >> 10_30_dist.txt 
~/Install/mmtsb/perl/mindist.pl 10 33 $filename >> 10_33_dist.txt 
~/Install/mmtsb/perl/mindist.pl 10 39 $filename >> 10_39_dist.txt 
~/Install/mmtsb/perl/mindist.pl 13 14 $filename >> 13_14_dist.txt 
~/Install/mmtsb/perl/mindist.pl 13 17 $filename >> 13_17_dist.txt 
~/Install/mmtsb/perl/mindist.pl 13 30 $filename >> 13_30_dist.txt
~/Install/mmtsb/perl/mindist.pl 13 33 $filename >> 13_33_dist.txt
~/Install/mmtsb/perl/mindist.pl 13 39 $filename >> 13_39_dist.txt 
~/Install/mmtsb/perl/mindist.pl 14 17 $filename >> 14_17_dist.txt 
~/Install/mmtsb/perl/mindist.pl 14 30 $filename >> 14_30_dist.txt 
~/Install/mmtsb/perl/mindist.pl 14 33 $filename >> 14_33_dist.txt 
~/Install/mmtsb/perl/mindist.pl 14 39 $filename >> 14_39_dist.txt 
~/Install/mmtsb/perl/mindist.pl 17 30 $filename >> 17_30_dist.txt 
~/Install/mmtsb/perl/mindist.pl 17 33 $filename >> 17_33_dist.txt 
~/Install/mmtsb/perl/mindist.pl 17 39 $filename >> 17_39_dist.txt 
~/Install/mmtsb/perl/mindist.pl 30 33 $filename >> 30_33_dist.txt 
~/Install/mmtsb/perl/mindist.pl 30 39 $filename >> 30_39_dist.txt 
~/Install/mmtsb/perl/mindist.pl 33 39 $filename >> 33_39_dist.txt
done
#10, 13, 14,17,30,33,39
