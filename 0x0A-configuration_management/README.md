# Overview #

As the days go by, we're getting close to specilization and this **0x0A. Configuration management** project is very important because it introduces to the concepts of configurations. The importance of cofigurations cannot be overemphasized. This story is here to drive this fact even deeper.<br/><br/>

*When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.<br/><br/>There were 2 pieces of bad news:<ol><li>When MCollective receives *nil* as an argument for its filter method, it takes this to mean ‘all servers’;</li><li>The action I sent was to terminate the selected servers.</li></ol><br/>I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!<br/><br/>Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…<br/><br/>Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.*

<hr/>

<<<<<<< HEAD
<<<<<<< HEAD
=======
## Reference Resources
- (Intro to Configuration Management)[https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management]
- (Puppet resource type: file)[https://www.puppet.com/docs/puppet/5.5/types/file.html] **(check “Resource types” for all manifest types in the left menu)**
- (Puppet’s Declarative Language: Modeling Instead of Scripting)[https://www.puppet.com/blog]
- (Puppet lint)[http://puppet-lint.com/]
- (Puppet emacs mode)[https://github.com/voxpupuli/puppet-mode]

>>>>>>> 7bce759... ci(asd): create 0x0A-config folder and readme
=======
>>>>>>> 0c94af3... docs(asd): update readme
## Folder Details ###
- **Date Created:** Fri 19 Apr. 2024.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Fri Apr. 19, 2024 - 6am.
  - **1st Deadline:** Sat Apr. 20, 2024 - 6am.
  - **Duration:** 24 hrs.
  - **Month** 6, **Week** 2, **Day** 5.

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 0c94af3... docs(asd): update readme


## Dependencies ##
The following installations are needed for completing this project:

#### 1. Installing Puppet ####
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

```
**There's no need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.**

#### 2. Install puppet-lint ####
```
$ gem install puppet-lint
```

## Reference Resources
<<<<<<< HEAD
<<<<<<< HEAD
- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html) **(check “Resource types” for all manifest types in the left menu)**
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)


=======
>>>>>>> 7bce759... ci(asd): create 0x0A-config folder and readme
=======
- (Intro to Configuration Management)[https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management]
- (Puppet resource type: file)[https://www.puppet.com/docs/puppet/5.5/types/file.html] **(check “Resource types” for all manifest types in the left menu)**
- (Puppet’s Declarative Language: Modeling Instead of Scripting)[https://www.puppet.com/blog]
- (Puppet lint)[http://puppet-lint.com/]
- (Puppet emacs mode)[https://github.com/voxpupuli/puppet-mode]
=======
- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html] **(check “Resource types” for all manifest types in the left menu)**
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
>>>>>>> fc647bc... docs(asd) update readme links


>>>>>>> 0c94af3... docs(asd): update readme
## Technologies ##
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- File types can be identified by their extensions
- Code tested on Ubuntu 20.04 LTS.

<<<<<<< HEAD
<<<<<<< HEAD
## File Tree ##
Pending

=======
>>>>>>> 7bce759... ci(asd): create 0x0A-config folder and readme
=======
## File Tree ##
Pending

>>>>>>> 0c94af3... docs(asd): update readme

## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
<<<<<<< HEAD
<<<<<<< HEAD
| 1. | [Coming soon](https://www.github.com) |  |
=======
| 1. | ()[] |  |
>>>>>>> 7bce759... ci(asd): create 0x0A-config folder and readme
=======
| 1. | [Coming soon](https://www.github.com) |  |
>>>>>>> fc647bc... docs(asd) update readme links
