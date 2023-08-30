"""Simple protein translation function"""
def proteins(strand: str):
    """ Translates a protein strand into its component proteins

    :param strand: str - a protein strand.
    :return: list[str] - a list of proteins found in the input
    """
    proteins = {}
    proteins["AUG"] = "Methionine"
    proteins["UUU"] = "Phenylalanine"
    proteins["UUC"] = "Phenylalanine"
    proteins["UUA"] = "Leucine"
    proteins["UUG"] = "Leucine"
    proteins["UCU"] = "Serine"
    proteins["UCC"] = "Serine"
    proteins["UCA"] = "Serine"
    proteins["UCG"] = "Serine"
    proteins["UAU"] = "Tyrosine"
    proteins["UAC"] = "Tyrosine"
    proteins["UGU"] = "Cysteine"
    proteins["UGC"] = "Cysteine"
    proteins["UGG"] = "Tryptophan"
    proteins["UAA"] = "STOP"
    proteins["UAG"] = "STOP"
    proteins["UGA"] = "STOP"

    translated_strand = []
    strand_length = len(strand)
    for i in range(0,strand_length,3):
        protein = proteins[strand[i:i+3]]
        if protein == "STOP":
            break
        translated_strand.append(protein)

    return translated_strand
