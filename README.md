Microsoft Cloud App Security Alerts - Jira Issues
================================================================================

**Table of Contents**

<div id="Table of Contents1" dir="ltr">


| List | Details |
| ---- | ---------|
1.0 | Purpose
2.0 | Instructions
3.0 | Usage scenario
4.0 | Comments and considerations



1.0. Purpose
=============

Given the need to manage more than one tenant promptly, and
also, keep our records in a Help Desk platform that later on can be 
used for reports (daily, weekly, monthly) within cyber security alerts,
we can rely on some automation to get this done efficiently. 

For that, this program relies on rest API via the following tools:


|                  |            |
|------------------|------------|
| Tool             | Authentication |
| Microsoft Cloud App Security | Token-based  | 
| Abuseipdb  | Token-based  |         |
| Jira | Basic auth |


2.0. Instructions
================

The program must be executed with Python 3, where you might have to install the "requests" module:

-   pip3 install requests

To run it:
-   git clone https://github.com/pahennig/Alerts-to-Jira-Tickets
-   python3 $path/Alerts-to-Jira-Tickets/script/status.py

To allow the program to run accordingly, ensure to generate a token from Microsoft Cloud App Security, and Abuseipdb. 
After this step, you should be able to replace the MCAS token within "status.py" (refer to the function "choices"),
and Abuseipdb token within "abuseip.py".

Ensure to also place your username and password for the basic auth on Jira side - file: jira.py.

As these configuration settings should be modified before you run the program, ensure there's no dollar sign ($) in the below files:
- status.py (MCAS token)

- abuse.py (abuseipdb token)

- jira.py (basic auth)

The following guidelines are also useful in order to adjust the program according to your preferences:
- [MCAS API](https://docs.microsoft.com/en-us/cloud-app-security/investigate-activities-api)
- [Abuseipdb API](https://docs.abuseipdb.com/#introduction)
- [Jira Server platform REST API reference](https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/)

When the tickets are created on Jira, it uses the application's custom fields to map:
- Alert URL
- Alert summary
- Alert Description
- Affected User
- IP
- Reported IPs

With that in mind, ensure to also change the custom field ID to match your instance's details.


3.0 Usage scenario
=======================
It's Monday, and you just started your work shift. To check your environment's security status, you open Microsoft Cloud App Security
and realize that you have 15 alerts across three different tenants created on the weekend. As part of the routine and procedures in place,
the alerts should be raised at Jira, so that you can add the analysis, and other steps (e.g., remediation, recovery, post-incident) 
until closing the ticket. Therefore, you follow:

1. Run the script
2. The 15 alerts are created at Jira automatically, where it's also observable through the terminal output.
   - If there are no network problems to retrieve and post the information, this step should be done within seconds.
![<Insert Diagram>](https://github.com/pahennig/Alerts-to-Jira-Tickets/blob/master/images/terminal.png) 
3. All tickets are created correctly, and it's visible on your queue screen:
![<Insert Diagram>](https://github.com/pahennig/Alerts-to-Jira-Tickets/blob/master/images/jiraqueue.png)
4. As the script uses regex to filter for certain details, we'll be able to see additional information as per the following example, such as "affected user", "IP report", and other ones as the given list in the above section:
![<Insert Diagram>](https://github.com/pahennig/Alerts-to-Jira-Tickets/blob/master/images/affected_user.png)
5. This is how the ticket above looks like from MCAS:
![<Insert Diagram>](https://github.com/pahennig/Alerts-to-Jira-Tickets/blob/master/images/tor_mcas.png)
6. We can confirm the IP, and report by checking abuseipdb's website:
![<Insert Diagram>](https://github.com/pahennig/Alerts-to-Jira-Tickets/blob/master/images/abuseipdb.png)
7. After taking the correct actions upon the issue, you freeze or close the ticket that can later be used for log management of cyber security incidents and reporting.



4.0. Comments and considerations
=============

#### Security
For this program's purpose, the tokens and basic auth should be placed under the code,
where you can run this from your laptop or cron. However, a solution such as Azure Key Vault
is a good approach in order to avoid the handle of secrets within our code.

#### Alert Types
The alerts from Cloud App Security will be generated according to your configuration settings (e.g., data connectors, policies configuration). 
With that, you can customize the function "tenanturl" according to your preferences. For instance, if a "leaked credentials" is triggered and
the user belongs to a Staff group - then a Jira ticket should be raised with the highest priority.

To check a few alerts with additional details, kindly refer to the following link:
- [Managing Alerts](https://docs.microsoft.com/en-us/cloud-app-security/managing-alerts)

#### Jira data
For the examples I've shown, I'm using the default workflow from Jira. However, you might want to consider a specific one, corresponding
 to your methodology, as NIST incident/response cycle, including categories and sub-categories (e.g., information gathering, compromised user/app/server, spam, DDoS, escalation of privileges):
 ![<Insert Diagram>](https://github.com/pahennig/Alerts-to-Jira-Tickets/blob/master/images/nist.png)

