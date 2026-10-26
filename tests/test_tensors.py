import numpy as np
from src.structural.tensors import coordinates_to_numpy_array, compute_distance_tensor, compute_contact_map

def test_coordinates_to_numpy_array():
    mock_coords = [(0.0, 0.0, 0.0), (3.0, 4.0, 0.0)]
    arr = coordinates_to_numpy_array(mock_coords)
    
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)

def test_compute_distance_tensor():
    # Points at (0,0,0) and (3,4,0) -> distance should be 5.0
    mock_coords = np.array([[0.0, 0.0, 0.0], [3.0, 4.0, 0.0]])
    dist_matrix = compute_distance_tensor(mock_coords)
    
    assert dist_matrix[0, 1] == 5.0
    assert dist_matrix[0, 0] == 0.0

def test_compute_contact_map():
    # Point 0 and 1 are 5.0 units apart. Threshold is 6.0 -> should be contact (1).
    # If threshold is 4.0 -> should NOT be contact (0).
    mock_coords = np.array([[0.0, 0.0, 0.0], [3.0, 4.0, 0.0]])
    
    contact_map_close = compute_contact_map(mock_coords, threshold=6.0)
    assert contact_map_close[0, 1] == 1
    
    contact_map_far = compute_contact_map(mock_coords, threshold=4.0)
    assert contact_map_far[0, 1] == 0