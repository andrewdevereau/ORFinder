import Bioadd
MIN_SIZE = 50
in_file = Bioadd.read_fasta("/home/jovyan/elab/Shared/U15422.fasta")


for name, seq in in_file.items():
    print("Seqeunce name = ", name)
    print("Length = ", len(seq))
    translations = {}
    for i in range(3):
        translations["Forward_" + str(i)] = Bioadd.translate(seq[i:])
        translations["Reverse_" + str(i)] = Bioadd.translate(Bioadd.reverse_complement(seq)[i:])

    for trans_name, aa_seq in translations.items():
        for orf_name, orf in Bioadd.longORF(aa_seq).items():
            if len(orf) > MIN_SIZE:
                print("_".join([name.split()[0].strip(">"), trans_name, str(orf_name)]))
                print(orf)