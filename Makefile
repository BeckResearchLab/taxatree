# run the tree gen pipeline


ALL = 16s_seq.fna 16s_seq.afna

all: $(ALL)

16s_seq.fna: taxa.csv
	./csvtofasta.py --input $< --output $@

16s_seq.afna: 16s_seq.fna
	muscle -super5 $< -output $@

clean:
	rm $(ALL)
