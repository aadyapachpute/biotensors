"""
NumPy-powered tensor transformations and contact map generation for biotensors.
"""
import numpy as np

def coordinates_to_numpy_array(coordinates: list) -> np.ndarray:
    """
    Convert a list of (x, y, z) coordinate tuples into a NumPy array of shape (N, 3).
    """
    return np.array(coordinates, dtype=np.float64)

def compute_distance_tensor(coords_array: np.ndarray) -> np.ndarray:
    """
    Compute pairwise Euclidean distance matrix vectorially using NumPy broadcasting.
    Formula: ||u - v||_2
    """
    # Shape of coords_array is (N, 3)
    # Expand dims to compute pairwise differences: (N, 1, 3) - (1, N, 3) -> (N, N, 3)
    diff = coords_array[:, np.newaxis, :] - coords_array[np.newaxis, :, :]
    
    # Compute L2 norm across the coordinate axis
    dist_matrix = np.linalg.norm(diff, axis=-1)
    return dist_matrix

def compute_contact_map(coords_array: np.ndarray, threshold: float = 8.0) -> np.ndarray:
    """
    Generate a binary contact map tensor from 3D coordinates based on a distance threshold (default 8.0 Å).
    Returns a binary numpy array of shape (N, N) where 1 indicates contact, 0 otherwise.
    """
    dist_matrix = compute_distance_tensor(coords_array)
    # Binary thresholding
    contact_map = (dist_matrix <= threshold).astype(int)
    return contact_map