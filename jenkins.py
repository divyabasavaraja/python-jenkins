#Login to UGnode, pull finley docker image from cumulus repo, re-tag it to latest and terminate the latest kubectl pod

from pexpect import pxssh
import configFile
from logging import error
import time


class UGnodeFinleyDockerPull():

    global UGNODE
    global IISNODE
    global IISPORT
    UGNODE = configFile.UGnode
    IISNODE = configFile.IISnode
    IISPORT = configFile.port

    def ugnode_finley_pull_latest_docker_image(self):

        USERNAME = configFile.user
        USERPASSWORD = configFile.rootPassword

        s = pxssh.pxssh()
        if not s.login(UGNODE, USERNAME, USERPASSWORD):
            print ("SSH session failed on login.")
            print (str(s))
        else:
             try:
                 print ("SSH session login successful")
                 s.sendline('docker login na.cumulusrepo.com -u token -p 7fe5089c76edc3bfc161da36ebeb689d')
                 s.prompt()
                 s.sendline('docker pull na.cumulusrepo.com/finley/finley')
                 s.prompt()
                 s.sendline('docker images | grep finley')
                 s.prompt()
                 finley_docker_details =str((s.before.splitlines()[1:])).split()
                 docker_tag = (finley_docker_details[1])
                 s.sendline('docker tag na.cumulusrepo.com/finley/finley:'+docker_tag +' na.cumulusrepo.com/finley/finley:latest')
                 s.prompt()
                 s.sendline('kubectl get pod| grep finley-ml')
                 s.prompt()
                 finleypod_details = str((s.before.splitlines()[1:])).split()
                 finleypod =(finleypod_details[0])[3:30]
                 print(finleypod)
                 s.sendline('kubectl delete pods '+finleypod+'')
                 s.prompt()
                 time.sleep(20)
                 s.sendline('exit')
             except:
                 error("Error pulling latest finley docker image on UGnode")

