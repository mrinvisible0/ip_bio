
import csv
import Bio.SeqIO as SeqIO

mink_filepath = "metadata/mink_coding_regions.fasta"
pangolin_filepath = "metadata/pangolin_coding_regions.fasta"
nextstrain_filepath = "metadata/nextstrain_ncov_global_metadata.tsv"

GENBANK_INDEX = 11
def filter_genbank():
    tsv_metadata = open(nextstrain_filepath)
    reader = csv.reader(tsv_metadata, delimiter="\t")

    we_need_those = []
    for row in reader:
        if row[GENBANK_INDEX]:
            we_need_those.append(row)
    return we_need_those

def has_non_acgt(fasta):
    for record in fasta:
        seq = record.seq
        for l in seq:
            if l not in ["A", "C", "G", "T"]:
                print(seq)
                print("FAILED FOR LETTER: " + l)
                return True
    return False

def main():
    metadata = filter_genbank()
    pangolin_cov2 = SeqIO.parse(pangolin_filepath, "fasta")
    mink_cov2 = SeqIO.parse(mink_filepath, "fasta")

    if has_non_acgt(pangolin_cov2):
        print("PANGOLIN HAS NON ACGT")
        return

    if has_non_acgt(mink_cov2):
        print("MINK HAS NON ACGT")
        return

    lala = set()
    for row in metadata:
        lala.add(row[GENBANK_INDEX])

    print(lala)

if __name__ == "__main__":
    main()