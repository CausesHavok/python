"""Translates from DNA to RNA"""
def to_rna(dna_strand: str):
    """Translates from DNA to RNA
    :param dna_strand: str - a strand of dna
    :return: str - stand of rna"""
    return dna_strand.replace("G", "X").replace("C", "G").replace("X", "C").replace("A", "U").replace("T", "A")

