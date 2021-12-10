import os
from pprint import pprint
import os
import subprocess
import json
import logging
import re
import time


## call lilke
## (stderr, stdout, ret_code, check_ret_cd) = git_tag(x,y,w)
def git_tag(git_exe, project_dir, tag_name, sha_id):
    os.chdir(project_dir)

    process = subprocess.run([ git_exe, "tag", tag_name, sha_id],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return(stderr, stdout, ret_code, check_ret_cd)

# git.exe submodule add   -- "D:/work/sm.git" "b/y"

def git_add_sm(git_exe, project_dir, sm_repo_path, sm_dir):
    os.chdir(project_dir)

    process = subprocess.run([git_exe, "submodule", "add", sm_repo_path, sm_dir],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return (stderr, stdout, ret_code, check_ret_cd)

def git_init(git_exe, project_dir ):
    os.chdir(project_dir)

    process = subprocess.run([git_exe, "init"],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return (stderr, stdout, ret_code, check_ret_cd)

#git remote add origing D:\work\root_of_all_Evil.git
def git_remote_add_origin(git_exe, project_dir, origin_path ):
    os.chdir(project_dir)

    process = subprocess.run([git_exe,  "remote",  "add", "origin", origin_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return (stderr, stdout, ret_code, check_ret_cd)

#  git push --set-upstream origin master
def git_push_origin_master(git_exe, project_dir ):
    os.chdir(project_dir)

    process = subprocess.run([git_exe, "push", "--set-upstream", "origin", "master"],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return (stderr, stdout, ret_code, check_ret_cd)



def git_add_all(git_exe, project_dir ):
    os.chdir(project_dir)

    process = subprocess.run([git_exe, "add", "."],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return (stderr, stdout, ret_code, check_ret_cd)


def git_commit(git_exe, project_dir ):
    os.chdir(project_dir)

    process = subprocess.run([git_exe, "commit", "-m", "\"initial commit - auto done\""],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             universal_newlines=True
                             )

    stderr = process.stdout
    stdout = process.stderr
    ret_code = process.returncode
    check_ret_cd = process.check_returncode

    return (stderr, stdout, ret_code, check_ret_cd)


def dict_recurse (root_dir, out_list, submodule_list, sub_dict):

    for key, val in sub_dict.items():
        if isinstance(val, dict):
            dict_recurse(os.path.join(root_dir, key), out_list, submodule_list, val)
        else:
            # if isinstance(val,list):
            for v in val:
                ## tuples are used when adding sumbodules
                if isinstance(v,tuple):
                    # out_list.append(  os.path.join(root_dir, key, v[0]) )
                    submodule_list.append((os.path.join(key, v[0]), v[1]))
                else:
                    out_list.append(os.path.join(root_dir, key, v))

    return (out_list, submodule_list)



#------------------------------------#------------------------------------#------------------------------------
git_exe = r"D:\Program Files\Git\bin\git.exe"


root= r"D:\work\root_of_all_Evil"
origin_location = r"D:\work\root_of_all_Evil.git"

filename = "a.txt"



dir_str0 = {
    "_a": ["_x", "_x1"],
    "_b": [("_y", "D:\work\sm.git")],
    "_c": {
        "_c1":["_sss", "s2"]
    },
}

dir_list =[]
submodule_list = []
sumbmodule_pair = ()
(dir_list, submodule_list) = dict_recurse(root, dir_list , submodule_list, dir_str0)

pprint (dir_list)

pprint (submodule_list)


# initialising root dir as git repo
# (stderr, stdout, ret_code, check_ret_cd) = git_init(git_exe, root)

for el in dir_list:
    el = el + "\\" +  filename
    print (el)
    os.makedirs(os.path.dirname(el))
    with open(el, "w") as f:
        f.write("FOOBAR")



## adding sumbodules in repo
for el in submodule_list:
    # project_dir, sm_repo_path, sm_dir
    (stderr, stdout, ret_code, check_ret_cd)  = git_add_sm(git_exe,root, el[1], el[0] )

    print (stderr, stdout, ret_code, check_ret_cd)
    # print ("creating dir " + el[0] + " as submodule from "+ el[1])


# add origin
(stderr, stdout, ret_code, check_ret_cd) = git_remote_add_origin(git_exe,root, origin_location)


(stderr, stdout, ret_code, check_ret_cd) = git_add_all(git_exe, root)
(stderr, stdout, ret_code, check_ret_cd) = git_commit(git_exe, root)


# first push to origin
(stderr, stdout, ret_code, check_ret_cd) = git_push_origin_master  (git_exe, root)

