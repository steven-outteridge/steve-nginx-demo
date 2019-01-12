Interview Assignment  
Jan 12th 2019 
Deploying Enginer - steveoutteridge@hotmail.co.uk
GitRepo -  "git clone https://github.com/steven-outteridge/steve-nginx-demo.git"  


Pre-requisits
------------
The assignment was carried out on a Mac OS X 18.2.0
Dependent packages
 ansible
 virtualbox
 vagrant


Overview and install  
--------------------------

A vagrant CentOS virtual host is created using virtulbox provisioned via ansible.
The provison includes:
 installing and starting docker and docker-compose, 
 copying Dockerfile docker-compose.yml and basic index.html to the virt
 starting the nginx:alpine micro service and exposing port 8080

Once the repo has been cloned this can be implemented using:
 "vagrant up --provision"

Example Output in can be seen at the end of the README
















Expected behaviour:

  
