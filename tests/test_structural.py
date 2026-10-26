from src.structural.parser import parse_pdb_atom_lines, compute_euclidean_distance

def test_compute_euclidean_distance():
    p1 = (0.0, 0.0, 0.0)
    p2 = (3.0, 4.0, 0.0)
    assert compute_euclidean_distance(p1, p2) == 5.0

def test_parse_pdb_atom_lines():
    mock_pdb = (
        "ATOM      1  CA  MET A   1      0.000   0.000   0.000  1.00  20.00           C\n"
        "ATOM      2  CA  VAL A   2      3.000   4.000   0.000  1.00  20.00           C\n"
    )
    coords = parse_pdb_atom_lines(mock_pdb)
    assert len(coords) == 2
    assert coords[0] == (0.0, 0.0, 0.0)
    assert coords[1] == (3.0, 4.0, 0.0)