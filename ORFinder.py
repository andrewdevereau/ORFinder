import Bioadd

in_file = Bioadd.read_fasta("/home/jovyan/elab/Shared/U15422.fasta")
for name, seq in in_file.items():
    for i in range(3):
        print(i, "Forward")
        print(Bioadd.translate(seq[i:]))
        print(i, "Reverse")
        print(Bioadd.translate(Bioadd.reverse_complement(seq[i:])))

