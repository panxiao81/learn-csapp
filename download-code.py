#!/usr/bin/python3
# (C) Pan Xiao 2022

import argparse
import os
import shutil
import tarfile
import urllib.request

if __name__ == '__main__':
    args = argparse.ArgumentParser(description="Download CS:APP source code")
    args.add_argument("-s", "--save", help="Don't delete tarball automatically", action="store_true")
    args.add_argument("-f", "--force", help="Force download the source code.", action="store_true")
    argv = args.parse_args()
    if os.path.exists("code"):
        if not argv.force:
            print("The source code exists, exit...")
            exit(0)
        else:
            print("The source code exists, redownload it...")
            shutil.rmtree("code", ignore_errors=True)
    web = "http://csapp.cs.cmu.edu/3e/code-all.tar"
    if not os.path.exists("code-all.tar"):
        print("Downloading ", "code-all.tar")
        urllib.request.urlretrieve(web, "code-all.tar")
    print("Download complete, unpack it...")
    # unpack and delete the tar file
    with tarfile.open("code-all.tar") as f:
        f.extractall()
        f.close()
    if not argv.save:
        print("Delete ", "code-all.tar")
        os.remove("code-all.tar")