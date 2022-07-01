import requests, sys

if len(sys.argv) != 2:
    print("Uses:\npython request_csv.py [FILE]")
    sys.exit(1)

file=sys.argv[1]
file_content=[]
with open(file) as content:
    for line in content:
        try:
            line=line.replace("\n","")
            request=requests.get(line)
            file_content.append(f"{line},{request.status_code},{request.elapsed.total_seconds()}\n")
        except Exception as a:
            print(a)

with open("request_result.csv", "w") as output:
    output.writelines(file_content)
