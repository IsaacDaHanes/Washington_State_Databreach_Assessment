# Washington State Databreach Assessment

<p align="left">
  <img src="images/Headerimg.png" width = 800 height = 250>
</p>

## Introduction

This project is an exploration into data breaches on organizations in Washington State, which those organizations are legally responsible for reporting to the state if the breach affects Washington residents in excess of 500 people. The organizations may optionally report if the number of affected residents falls below that range. That goes to say that not all of the organizations listed are based in Washington State and is important to keep in mind moving ahead in looking at the data.

### Purpose
The purpose of this project is to ask questions about the data and leverage those questions to draw useful statistical conclusions. The purpose is not to make conclusions on what to do with the information, or how it should be handled, though I will, with some hesitation, point out some inferences which could help strenghten the database in the future and allow for more definite conclusions to be drawn. This could assist State actors and agencies in making corrections and taking action, and may also serve as an example for others who would collect or analyze data.

### Database: Initial Exploratory Data Analysis
The Data Breach Notifications Affecting Washington Residents database contains 945 rows, and 24 columns, four of those columns, including: 'Id', 'YearText', 'Year', and 'EndedOnDayDiscovered' have been dropped. The first three of those 4 were already represented in functionality by other columns, while the 'EndedOnDayDiscovered' column did not provide information as expected because the contained True or False values didn't logically account for the differences between when an attack ended before being discovered, or ended after being discovered, and in no way indicates whether an organization had any influence in stopping the attack.

The CyberattackType column has been modified where any DataBreachCause entry states "Cyberattack" and CyberattackType states "NaN" to be better represented by "Unreported", as it cannot fall into an existing category since the definitions of those categories are not made explicit by the author. I have done this to make that data usable and be able to fully represent statistics involving Cyber Attacks.

Here are some basic statistics about the database:

<p align="left">
  <img src="images/data_stats.png" width = 700 height = 850>
</p>

There are numerous categorical columns which make the data highly organizable and readable, which accounts for the missing values in some columns, as not every event will fit into every category. However, many of the missing values are due to input on part of the organizations responsible for submitting their reports. I was still able to draw a reasonable interpretation from the data.
### Minimum Viable Product

At a minimum I will provide the organization, display, and description of most pertinent collections of information contained in the database, as well as provide access to my tools and methods for doing so.

## Conclusive information

Below is the results of my exploration and analysis in graphical form, along with descriptions. The charts can be located as image files in the image directory, the method of collection is located in the src directory. All of the steps, and testing for which is layed out in the notebooks directory.

### Statistical Discoveries

<p align="center">
  <img src="images/Causes of Data Breaches.png" width = 400 height = 400>
</p>

The above image illustrates, from the database, the percentages relative to the number of each type of data breach cause. Cyberattacks is the main cause, which is good in a way, because physical security, by law, should be high enough to protect against unauthorized access or theft, and mistakes should be prevented by training and policy.

Let's take a deeper look into Cyberattacks, what types there are, and how common each of them are:

<p align="center">
  <img src="images/Types of Cyber Attacks.png" width = 400 height = 400>
</p>

As you can see there is an Unreported section, near 9% of the total events, these are attacks which when reported the type was not selected by the reporter, so I have taken the liberty of grouping them, where they would not fit in anywhere else. To continue, it is good news that Phishing is relatively low on the chart, considering that most organizations do, or should, have training to prevent Phishing scams that are usually preventable. Ransomware seems to be the approach of choice for attackers, with Malware not being too far behind.

<p align="center">
  <img src="images/Industries Most Affected.png" width = 400 height = 400>
</p>

The most affected industry is business, and though I think with commmon sense the reason is easy to surmise I will not speculate here. The fact remains that almost 50% of breaches are in the business industry. While the breaches distributed across other industries are relatively low in comparison. Let's take a look at what types of businesses are affected.

<p align="center">
  <img src="images/Businesses Most Affected.png" width = 400 height = 400>
</p>


### Patterns

Charts that indicate verifiable patterns in the data that could be actioned upon will go here

### Outliers and Major Discoveries

Any major discoveries such as the Feb 7th attacks, and anything that sticks out in the data as interesting or surprising can go here

## Closing

This is where the summation will go and the final conclusion statements.