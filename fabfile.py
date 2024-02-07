import sys
from fabric import SerialGroup

args = sys.argv[1]

conn = SerialGroup("ubuntu@100.25.10.250", "ubuntu@100.25.155.18")
conn.put(args, "~/")
results = conn.run("ls -la", hide=True)

for result in results.values():
    print(result.stdout)
