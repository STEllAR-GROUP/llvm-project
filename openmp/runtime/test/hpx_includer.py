# hpx_includer: Takes a file and one of two flags, add or remove, and adds or removes the HPX include from the file.

if __name__ == "__main__":
    import argparse
    import os
    import sys

    parser = argparse.ArgumentParser(description="Add or remove HPX include from a file")
    parser.add_argument("action", choices=["add", "remove"], help="Action to perform")
    parser.add_argument("file", help="File to modify")

    args = parser.parse_args()

    if args.action == "add":
        with open(args.file, "r") as f:
            lines = f.readlines()
        with open(args.file, "w") as f:
            f.write("#include <hpxc/threads.h>\n")
            for line in lines:
                f.write(line)
        # # print the file to stdout
        # with open(args.file, "r") as f:
        #     print(f.read())
    elif args.action == "remove":
        with open(args.file, "r") as f:
            lines = f.readlines()
        with open(args.file, "w") as f:
            for line in lines:
                if line.strip() != "#include <hpxc/threads.h>":
                    f.write(line)
    else:
        print("Invalid action " + args.action, file=sys.stderr)
        sys.exit(1)
    sys.exit(0)