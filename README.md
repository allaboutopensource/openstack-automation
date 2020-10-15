# Openstack-Project Automation
How to create a project and link it to the AD group in Openstack and how can we add user to the group so that user can have access to the Project.

We need to create a Jenkins pipeline for this project. This Jenkin build is a parametrized job where the parameters are : project_name, Group_name, Cost_center.

We need to have 2 slave nodes connected to the master node: 

1) windows-node: To run the powershell commands in 1st stage
2) openstack-node: To run the openstack commands in 2nd stage

windows-node: You should have imported the AD module on to the node using the command: Import-Module Active Directory

Linux-node: You need to install the openstack-cli package and source the RC file before running the openstack command on the slave node. 

====================================================================================

Alternatively, you can achieve this with the single slave (Centos/Linux Node) where you need to first add the slave to Active Directory using adcli tool. 

adcli is a command line tool that help us to integrate or join Linux systems such as RHEL & CentOS to Microsoft Windows Active Directory (AD) domain. It’s allow us to use the same AD login credential to access Linux machine.

You need to aware of the basic adcli commands in this case like:

adcli create-group --description=<group desription> --domain=example.com --login-user=test-user --domain-ou="OU=example,DC=com" test-group
  
adcli delete-group test-group --domain=example.com

adcli add-member --domain=example.com test-group test-user --login-user=<user>
  
adcli remove-member --domain=example.com test-user
