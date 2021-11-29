import Bioadd

in_file = Bioadd.read_fasta("/home/jovyan/elab/Shared/U15422.fasta")
translations = {}
for name, seq in in_file.items():
    for i in range(3):
        translations[str(i) + " Forward"] = Bioadd.translate(seq[i:])
        translations[str(i) + " Reverse"] = Bioadd.translate(Bioadd.reverse_complement(seq)[i:])
for name, seq in translations.items():
    print(name, seq[:30])