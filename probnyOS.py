import os

os.environ["API_TOKEN"] = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZDc1MTkwZTg2M2JhNDU2YmNmMWQ2Y2YwMTZhMzU1ZiIsInN1YiI6IjYxZTg0Nzg5YmM4NjU3MDA0MzE3MTNiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lj9a6DFtw3zXyN2g6zRpcCwChtMtgsjoVojUSaEI_zw"
api_key = os.environ.get("API_TOKEN")

print(api_key)git