# openstack-automation
How to create a project in Openstack and link it to the AD group in Openstack

We need to create a Jenkins pipeline for this project. We need to have 2 slave nodes connected to the master node: 

windows-node: To run the powershell commands in 1st stage
openstack-node: To run the openstack commands in 2nd stage

This Jenkin build is a parametrized job where the parameters are : project_name, Group_name, Cost_center.

You need to source the RC file before running the openstack command on the slave node. 
