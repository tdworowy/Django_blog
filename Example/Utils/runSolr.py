import os

def runSolr():
    path = "D:\Solr\solr-6.5.1\\bin"
    commend = "D: && cd " + path + " && solr.cmd start"
    print(commend)
    os.system(commend)

runSolr()

# TypeError: context must be a dict rather than Context.
#TODO str 98
# probably need to change models > Post