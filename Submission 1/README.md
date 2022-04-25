
## IP01 Instructions:
Configuration Management is a very widely used process in managing complex systems, and software lifecycle is no exception. This process is integral for establishing and maintaining the consistency of the product throughout its life cycle. Software Configuration Management systems track and monitor changes to a software system's configuration metadata. This goes hand in hand with Version Control and Continuous Integration/Continuous Delivery which includes the build function as well. 

One of the most challenging parts of designing a solution is choosing the platform and dependencies. There are certain services to assist with comparing different tools and making decisions. [G2](https://www.g2.com/) is a peer-reviewing service for evaluating business software. [Software Advice](https://www.softwareadvice.com/) is another tool from a research and analyst company for reviewing software. [StackOverflow Insights](https://insights.stackoverflow.com/survey) and [StackShare](https://stackshare.io/) can also be used to gain better clarity on the technologies and services being used. 

Students can use any form of documentation or any of the popular options for CMS systems. Some options may include: 

**Enterprise Level:**  
- [IBM Rational ClearCase](https://www.ibm.com/products/rational-clearcase)   
- [Azure DevOps Server](https://azure.microsoft.com/en-us/services/devops/server/)  
- [Puppet Enterprise](https://puppet.com/products/puppet-enterprise/)   
- [Chef Enterprise Automation Stack](https://www.chef.io/products/enterprise-automation-stack)  
- [Perforce](https://www.perforce.com/)   

**Open Source:**  
- [Open Source Puppet](https://puppet.com/docs/puppet/7/puppet_index.html)   
- [Open Source Chef](https://www.chef.io/)  
    - [Chef Infra](https://www.chef.io/products/chef-infra)     
    - [Chef Habitat](https://www.chef.io/products/chef-habitat)   
    - [Chef Automate](https://www.chef.io/products/chef-automate)   
- [Azure DevOps Server Express](https://go.microsoft.com/fwlink/?LinkId=2041269&clcid=0x409)   
- [Red Hat Ansible](https://github.com/ansible/ansible)   

Each student will implement and demonstrate test cases in a Configuration Management System (CMS) of their choice. Specific instructions may be provided upon request in addition to the documentation of the CMS selected. Once the CMS has been implemented, the student will create at least two accounts in the system, including one with applicable administrative rights. The student will create test cases to demonstrate how the following situations are handled in the CMS. Below is a suggestion for the processes: 

- Code checkout (or Git Clone) 
- Code checkin (or Git Commit) 
- Code Pull request 
- Code Merge 
- Code snapshot (or release point) 
- Code in development by two users, 
    - first one checks out code, 
    - second checks out code, makes changes and checks in, 
    - first makes changes and needs to check in. 
- Code changes need to be rolled back to a previous version (revert). 
- One developer is working on a new version, one is fixing bugs in a previous release (Git fork). 
- Define runtime variable for your software 
- Deploy the software on your local machine or a cloud  
- Write a CMS playbook (configuration file) to change the runtime variable in the configuration file.  

Each process must be documented. 
##### 04/15/2022

<br>
<br>  
<br>

## IP01 Notes
This IP will be focusing on the overall development of a [freeCodeCamp.org](https://www.freecodecamp.org/) project called [Code a Discord Both with Python - Host for Free in the Cloud](https://www.youtube.com/watch?v=SPTfmiYiuok). 

The Content Management System (CMS) for this project includes [GitHub](https://github.com/Hipples/CS504-Project-Samantha-Hipple), [Repl.it](https://replit.com/) - which is a "free, collaborative, in-browser IDE" according to the site's homepage - and potentially [GitHub Actions](https://github.com/features/actions). 

<br>

### The main tasks for this initial IP include: 
+ **Set up CMS and coding environment:**
    + create a replit account
    + manually update GitHub repository as project is updated locally
    + connect replit and github
    + explore github actions
    + have a second github account for CMS testing purposes

<br>

+ **Create a discord bot account:**
    + go to the [Discord Developer Portal](https://discord.com/developers/applications)
    + select **New Application**, enter a name for the bot, click **Create**
        + 'Dissident Bot'
    + click on new bot application icon, then select **OAuth2** and **URL Generator** from the side-panel menu
    + check **bot** under *SCOPES* and the various *BOT PERMISSIONS* that the bot will use:
        + Text Permissions:
            + send messages
            + send messages in threads
            + embed links
            + attach files
            + read message history
            + use external emojis
            + use external stickers
            + add reactions
        + General Permissions:
            + read messages/view channels
    + copy the *GENERATED URL* and past into your web browser  

<br>  

+ **Invite the bot to the DBG discord:**
    + choose server and authorize the bot to join
    + check that the bot has joined the server (will be in the offline member list)

<br>

images? need to learn how to add them to .md files

<br>

+ **Create test cases for the CMS:**
    + use updating this project for IP01 test cases (e.g., committing and pushing this updated file can count as a code check-in)
    + install [github desktop](https://desktop.github.com/) application

<br>

+ **Author paper on content managment to submit by 04/24/22 11:59PM**
##### 04/23/2022

<br>
<br>
<br>

### CMS Test Cases

**Code checkout:** 
- Code checkin (or Git Commit) 
- Code Pull request 
- Code Merge 
- Code snapshot (or release point) 
- Code in development by two users, 
    - first one checks out code, 
    - second checks out code, makes changes and checks in, 
    - first makes changes and needs to check in. 
- Code changes need to be rolled back to a previous version (revert). 

- One developer is working on a new version, one is fixing bugs in a previous release (Git fork). 
- Define runtime variable for your software 
- Deploy the software on your local machine or a cloud  
- Write a CMS playbook (configuration file) to change the runtime variable in the configuration file.