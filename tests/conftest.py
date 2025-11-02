import os, sys

# Add project root (the folder containing 'app/') to sys.path for imports like 'from app import ...'
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
