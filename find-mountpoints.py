import commands

# run the command and get its output as a single string
mounts = commands.getoutput('mount -v')

# split the single string into separate lines based on newline
lines = mounts.splitlines()

# convert each line into a list of items and get the 3rd item which
# corresponds to the mount point
# map returns a list
mpoints = map(lambda x: x.split()[2], lines)

print "Mount points: "
for m in mpoints:
    print m
