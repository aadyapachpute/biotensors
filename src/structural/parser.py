"""
First-principles PDB structural coordinate and distance matrix parser for biotensors.
"""
import math

def parse_pdb_atom_lines(pdb_content: str) -> list:
    """
    Extract Alpha-carbon (CA) atom coordinates (x, y, z) from PDB file lines.
    """
    coordinates = []
    for line in pdb_content.splitlines():
        if line.startswith("ATOM") and line[12:16].strip() == "CA":
            try:
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                coordinates.append((x, y, z))
            except ValueError:
                continue
    return coordinates

def compute_euclidean_distance(coord1: tuple, coord2: tuple) -> float:
    """
    Compute Euclidean distance between two 3D spatial points from first principles.
    """
    return math.sqrt(
        (coord2[0] - coord1[0])**2 +
        (coord2[1] - coord1[1])**2 +
        (coord2[2] - coord1[2])**2
    )

def generate_distance_matrix(coordinates: list) -> list:
    """
    Generate a pairwise Euclidean distance matrix for a list of 3D coordinates.
    """
    n = len(coordinates)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = round(compute_euclidean_distance(coordinates[i], coordinates[j]), 2)
    return matrix