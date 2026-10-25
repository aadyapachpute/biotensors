from src.ncbi.parser import parse_fasta_string, calculate_gc_content

def test_parse_fasta_string():
    mock_fasta = ">TP53_mRNA\nATCGATCG\nCGATCGAT"
    result = parse_fasta_string(mock_fasta)
    
    assert result["header"] == "TP53_mRNA"
    assert result["sequence"] == "ATCGATCGCGATCGAT"

def test_calculate_gc_content():
    # 4 Gs, 4 Cs out of 16 bases = 50.0% GC content
    mock_seq = "GGGGCCCCAAAATTTT"
    gc = calculate_gc_content(mock_seq)
    
    assert gc == 50.0