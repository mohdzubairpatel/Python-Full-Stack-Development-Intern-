def read_large_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line

for line in read_large_file("xyz.txt"):
    print(line)

# With Keyword:

# Resource management
# Automatic cleanup
# Closing files automatically