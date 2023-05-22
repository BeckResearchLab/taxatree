# run the tree gen pipeline


ALL = 16s_seq.fna 16s_seq.afna 16s_seq.afna.raxml.reduced.phy 16s_seq.afna.raxml.reduced.phy.raxml.rba

all: $(ALL)

16s_seq.fna: taxa.csv
	./csvtofasta.py --input $< --output $@

16s_seq.afna: 16s_seq.fna
	muscle -super5 $< -output $@

16s_seq.afna.raxml.reduced.phy: 16s_seq.afna
	raxml-ng --check --msa $< --model GTR+G
	# run it again to complete the check
	raxml-ng --check --msa $@ --model GTR+G

16s_seq.afna.raxml.reduced.phy.raxml.rba: 16s_seq.afna.raxml.reduced.phy
	raxml-ng --parse --msa 16s_seq.afna.raxml.reduced.phy --model GTR+G
	# a previous run of the above suggested 9 cpus

test:
	raxml-ng --msa 16s_seq.afna.raxml.reduced.phy.raxml.rba --model GTR+G --prefix Tree --threads 9 --seed 42 --tree pars{25},rand{25}

clean:
	rm $(ALL)
