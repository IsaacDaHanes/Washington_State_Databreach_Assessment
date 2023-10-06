# Washington State Databreach Assessment

<p align="left">
  <img src="images/Headerimg.png" width = 800 height = 250>
</p>

## Table of Contents
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Database: Initial Exploratory Data Analysis](#database:-initial-exploratory-data-analysis)
  - [Minimum Viable Product](#minimum-viable-product)
- [Conclusive information](#Conclusive-information)
  - [Statistical Discoveries](#Statistical-Discoveries)
  - [Patterns](#Patterns)
  - [Outliers and Major Discoveries](#Outliers-and-Major-Discoveries)
- [Closing](#Closing)
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

This is where the charts and their descriptions will go

### Patterns

Charts that indicate verifiable patterns in the data that could be actioned upon will go here

### Outliers and Major Discoveries

Any major discoveries such as the Feb 7th attacks, and anything that sticks out in the data as interesting or surprising can go here

## Closing

This is where the summation will go and the final conclusion statements.