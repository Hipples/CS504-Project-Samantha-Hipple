# Submission 4

## IP4: Software Metrics

### Instructions
Software metrics are an important component for quality assurance, management, performance and overall estimation of costs of a software. The overall quality of a software may depend on the software metrics of that software or the other dependencies and Application Programming Interface (APIs) used in the design of the software.  

Some common metrics for assessing API’s include: 
+ Availability
+ Error code
+ Response time
+ Latency 

Common metrics for assessing software include: 
+ Maintainability Index
+ Cyclomatic Complexity
+ Depth of Inheritance
+ Class Coupling
+ Lines of Source code
+ Lines of Executable code 
 
There are certain tools to assist with measuring such metrics. Code Metrics and Code Clone Analysis are available through Visual Studio for software metrics. SonarQube is an automated code review tool for code quality and code security checks. SonarQube can be installed on a docker container very easily or on a server for wider accessibility. 

Each student will develop metrics for the validation and acceptance testing of the system designed in previous assignments. The student will describe how he or she collect and evaluate each metric. The student will describe why each of the metrics has been selected and what the effect of the metric is on the overall project quality. Students can use any of the suggested tools or any other tools based on their specific use case.  

#### Start Date
May 20, 2022 11:59 PM
#### Due Date
Jun 5, 2022 11:59 PM

### Brainstroming How to Start
Look into Code Metrics and Code Clone Analysis via Visual Studio?
Use the Tic Tac Toe program again since I need to be working to improve it anyway. 
What even are the common metrics above? What do they mean? What is the difference between source and executable code?
Is this all in our textbook? Some of it looks familiar. 
I don't understand docker containers or how to set up a sever still, so SonarQube is out. 
Need to come up with an intro about software metrics and their importance

### Initial Findings
The Visual Studio code analysis is for dotnet application, C# and others -- not python.
Python has a bunch of libraries available for this type of metrics analsys
So far Radon and Pylint is giving me metrics to work with for this paper, maybe test a couple more from the list

Radon provides:

Pylint provides: 

### Research References
https://www.fullstackpython.com/code-metrics.html
https://www.mantidproject.org/How_to_run_Pylint.html#To_Run_Pylint
https://radon.readthedocs.io/en/latest/index.html