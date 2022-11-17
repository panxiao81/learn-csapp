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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(f)
        f.close()
    if not argv.save:
        print("Delete ", "code-all.tar")
        os.remove("code-all.tar")