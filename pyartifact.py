import argparse,hashlib,json
from pathlib import Path
def inspect(path):
 p=Path(path);return {"name":p.name,"size":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 a=argparse.ArgumentParser();a.add_argument("paths",nargs="+");x=a.parse_args()
 print(json.dumps([inspect(p) for p in x.paths if Path(p).is_file()],indent=2))
if __name__=="__main__":main()
