def read_fasta (filename):
#read a fasta file into a dict
    with open(filename) as f:
        seqs = {}
        name = ""
        body = ""
        for line in f:
            if ">" in line:   #if this is the start of a fasta record
                if body != "":  #if there is sequence data this must be the end of a record
                    seqs[name] = body   #add the record to the dict
                    body = ""       #reset the seq data to start a new record
                name = line.strip() #get the first line of the fasta record which is the name
            else:
                body += line.strip()  #if this is the record body add the data to the sequence
    seqs[name] = body  #if this is the end of file add the current record to the dict
    return seqs

standard_code = {
    'TTT': 'F',
    'TTC': 'F',
    'TTA': 'L',
    'TTG': 'L',
    'CTT': 'L',
    'CTC': 'L',
    'CTA': 'L',
    'CTG': 'L',
    'ATT': 'I',
    'ATC': 'I',
    'ATA': 'I',
    'ATG': 'M',
    'GTT': 'V',
    'GTC': 'V',
    'GTA': 'V',
    'GTG': 'V',
    'TCT': 'S',
    'TCC': 'S',
    'TCA': 'S',
    'TCG': 'S',
    'CCT': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'ACT': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'GCT': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'TAT': 'Y',
    'TAC': 'Y',
    'TAA': '*',
    'TAG': '*',
    'CAT': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'AAT': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'GAT': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'TGT': 'C',
    'TGC': 'C',
    'TGA': '*',
    'TGG': 'W',
    'CGT': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AGT': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GGT': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}

def translate(seq, translation_table=standard_code):  #include a translation table as parameter
    translation = ""
    last_codon_len = len(seq)%3  #divide the sequence length by 3 and see how many bases remain
    if last_codon_len != 0:  #if there are remaining bases, i.e. the sequence length is not a multiple of 3
        print('Warning, truncating sequence by', last_codon_len)  #provide a warning that remaining bases will be removed
        seq = seq[:-last_codon_len]   #truncate the sequence to remove remaining bases
    for i in range(0, len(seq), 3):  #loop through the sequence in steps of 3
        try:    #use a try block to catch errors
            codon = seq[i:i+3].upper()  #get the codon as a variable
            translation += translation_table[codon]  #take each three bases, uppercase and translate to AA using dict
        except KeyError:  #KeyError means the translation table does not have the key we have asked for
            print("Warning, codon \'" + codon + "\' not found, stopping translation")     #could not find the codon in the dict.
            return translation           #stop translating and return the current translation
    return translation

def complement(seq, reverse=False):
    #another method using a dict instead of if block
    seq = seq.lower()
    comp = {
        'a': 't',
        't': 'a',
        'g': 'c',
        'c': 'g'
    }
    result = ""
    if reverse:
        step = -1
    else:
        step = 1
    for s in seq[::step]:
        result += comp[s]
    return result

def reverse_complement(seq):
    return complement(seq, reverse=True)