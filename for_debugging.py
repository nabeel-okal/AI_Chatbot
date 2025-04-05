
# --> This piece of for debugging purposes only

import transformers
print(transformers.__version__)


import sys
print(f"Python path: {sys.executable}")
print(f"Python version: {sys.version}")
try:
    import transformers
    print(f"Transformers version: {transformers.__version__}")
except ImportError:
    print("Transformers not found in this environment")
