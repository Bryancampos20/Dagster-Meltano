from dotenv import load_dotenv
import os

from dagster import Definitions, job, resource
from dagster_meltano import meltano_resource, meltano_run_op

# Carga variables de entorno desde el archivo .env
load_dotenv()

# Accede a la variable de entorno
meltano_project_dir = os.getenv("MELTANO_PROJECT_DIR")

@job(resource_defs={"meltano": meltano_resource.configured({"project_dir": meltano_project_dir})})
def run_elt_job():
   tap_done = meltano_run_op("tap-csv target-csv")()

defs = Definitions(jobs=[run_elt_job])
