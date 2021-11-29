def read_fasta (filename):
#read a fasta file into a dict
    with open(filename) as f:
        seqs = {}
        name = ""
        body = ""
        for line in f:
            if ">" in line:
                if body != "":
                    seqs[name] = body
                    body = ""
                name = line.strip()
            else:
                body += line.strip()
    seqs[name] = body
    return seqs
