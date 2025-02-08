import os
import sys
import logging
from rdkit import Chem

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s:%(name)s: %(message)s'
)

# Keep consistent references to the project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

def get_data_path(*subpaths) -> str:
    """
    Join subpaths onto the known data directory inside the project root.
    """
    return os.path.join(PROJECT_ROOT, 'data', *subpaths)

def mol_from_spaced_smiles(spaced: str) -> Chem.Mol:
    """
    Convert 'C C ( C ) C' to a proper RDKit Mol object for 'CC(C)C'.
    """
    compact = spaced.replace(" ", "")
    return Chem.MolFromSmiles(compact)
