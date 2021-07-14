from pathlib import Path
from dotenv import load_dotenv
import os
env_path = Path('Path to the .env file')
print(load_dotenv(dotenv_path=env_path))
print(os.environ.get(''))