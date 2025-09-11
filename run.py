import warnings
from uvicorn import run
import multiprocessing

warnings.filterwarnings("ignore", category=DeprecationWarning)
cpu_count = multiprocessing.cpu_count()

if __name__ == "__main__":
    run("src.main:app", host="0.0.0.0", port=5100, reload=True)