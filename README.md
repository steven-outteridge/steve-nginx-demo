Interview Assignment  
--------------------
Jan 12th 2019  
Deploying Enginer - steveoutteridge@hotmail.co.uk  
GitRepo -  "git clone https://github.com/steven-outteridge/steve-nginx-demo.git  


Pre-requisits
-------------
The assignment was carried out on a Mac OS X 18.2.0  
Dependent packages:   
-ansible   
-virtualbox   
-vagrant   


Overview and install  
--------------------

A vagrant CentOS virtual host is created using virtulbox with a static private IP of 192.168.0.233 then the nginx microservice provisioned via ansible.  
The provison includes:  
-installing and starting docker and docker-compose  
-copying Dockerfile docker-compose.yml and basic index.html to the virt   
-starting the nginx:alpine micro service and exposing port 8080  

Once the repo has been cloned this can be implemented using:  

$ git clone https://github.com/steven-outteridge/steve-nginx-demo.git  
$ cd steve-nginx-demo
$ vagrant up --provision  

Example Output in can be seen at the end of the README    

Testing the deployment
----------------------

A basic test can be done with curl:  

$ curl 192.168.0.233:8080   
<html>\   
<header><title>Steve Outteridge</title></header>\   
<body>\   
Hello world\    
</body>\   
</html>   

.

Included in the repo is a python script to test the url:  

$ ./urltest.py  
url=192.168.0.233:8080  
192.168.0.233:8080  
Steves URL is up  

Example Output  
--------------   

$ git clone https://github.com/steven-outteridge/steve-nginx-demo.git  
Cloning into 'steve-nginx-demo'...
remote: Enumerating objects: 80, done.
remote: Counting objects: 100% (80/80), done.
remote: Compressing objects: 100% (40/40), done.
remote: Total 80 (delta 11), reused 78 (delta 9), pack-reused 0
Unpacking objects: 100% (80/80), done.

$ cd steve-nginx-demo

$ vagrant up --provision
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'centos/7'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'centos/7' version '1811.02' is up to date...
==> default: Setting the name of the VM: steve-nginx-demo_default_1547320492432_31483
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 (guest) => 2200 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: No guest additions were detected on the base box for this VM! Guest
    default: additions are required for forwarded ports, shared folders, host only
    default: networking, and more. If SSH fails on this machine, please install
    default: the guest additions and repackage the box to continue.
    default: 
    default: This is not an error message; everything may continue to work properly,
    default: in which case you may ignore this message.
==> default: Configuring and enabling network interfaces...
==> default: Rsyncing folder: /private/tmp/steve-nginx-demo/ => /vagrant
==> default: Running provisioner: ansible...
Vagrant has automatically selected the compatibility mode '2.0'
according to the Ansible version installed (2.7.5).

PLAY [Dockerfile] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [default]

TASK [Install Docker] **********************************************************
changed: [default]

TASK [start docker] ************************************************************
changed: [default]

TASK [Install docker-compose] **************************************************
changed: [default]

TASK [Creates directory] *******************************************************
changed: [default]

TASK [Copy docker files] *******************************************************
changed: [default]

TASK [Copy docker compose] *****************************************************
changed: [default]

TASK [Copy index] **************************************************************
	changed: [default]

TASK [Build Image] *************************************************************
changed: [default]

PLAY RECAP *********************************************************************
default                    : ok=9    changed=8    unreachable=0    failed=0   



$ curl 192.168.0.233:8080
<html>
<header><title>Steve Outteridge</title></header>
<body>
Hello world
</body>
</html>

