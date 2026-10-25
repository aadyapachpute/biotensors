"""
First-principles sequence parsing module for biotensors.
Converts raw biological sequence strings into numerical composition metrics.
"""

def parse_fasta_string(fasta_content: str) -> dict:
    """
    Manually parse a FASTA formatted string without black-box abstractions.
    Extracts header and concatenated sequence lines.
    """
    lines = fasta_content.strip().split("\n")
    header = ""
    sequence_chunks = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            header = line[1:]
        else:
            sequence_chunks.append(line)
            
    return {
        "header": header,
        "sequence": "".join(sequence_chunks).upper()
    }

def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content percentage of a nucleotide sequence from first principles.
    Formula: ((Count(G) + Count(C)) / Total Length) * 100
    """
    if not sequence:
        return 0.0
    
    seq_upper = sequence.upper()
    g_count = seq_upper.count('G')
    c_count = seq_upper.count('C')
    total_len = len(seq_upper)
    
    return round(((g_count + c_count) / total_len) * 100, 2)