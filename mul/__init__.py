import os
import sys
import azure.functions as func

# ensure src is on path
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, 'src')
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from handlers.mul import main as handler_main

def main(req: func.HttpRequest) -> func.HttpResponse:
    return handler_main(req)
