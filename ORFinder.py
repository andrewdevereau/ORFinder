import Bioadd

in_file = Bioadd.read_fasta("/home/jovyan/elab/Shared/U15422.fasta")
for name, seq in in_file.items():
    print (name)
    print(seq[0:40], "...")