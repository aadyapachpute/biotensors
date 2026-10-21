import os

def test_repository_structure():
    """Verify core directories exist in the project architecture."""
    assert os.path.exists("src"), "Source directory 'src' is missing."
    assert os.path.exists("data"), "Data directory 'data' is missing."
    assert os.path.exists("reports"), "Reports directory 'reports' is missing."

def test_basic_assertion():
    """Sanity check for pytest execution."""
    assert 1 + 1 == 2