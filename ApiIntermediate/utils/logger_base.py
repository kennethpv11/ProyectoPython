import logging as log
from dotenv import load_dotenv
from os import getenv

load_dotenv()
LEVEL = getenv("LEVEL_LOG")

log.basicConfig(level=LEVEL,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.StreamHandler()
                ]
                )
