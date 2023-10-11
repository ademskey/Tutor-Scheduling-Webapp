# Software Requirements Specification

## Your Project Title
--------
Prepared by:

* `Adam Caudle`,`WSU team Tylenol >`
* `<author1>`,`<organization>`
* `<author1>`,`<organization>`
* `<author1>`,`<organization>`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

This project titled “VCEA Tutoring Portal” is meant to provide a useful web-portal for students utilizing the VCEA tutoring services to schedule appointments with tutors. It will help streamline student to tutor appointments and reduce wasted time spent for both students and tutors in the VCEA tutoring center.

## 1.1 Document Purpose

The purpose of this document is to outline the requirements necessary for completion of all deliverables associated with the project. In short it outlines the idea, design, and scope needed and used to complete the VCEA Tutoring Portal.

## 1.2 Product Scope

The VCEA Tutoring portal is the product deliverable which has the software requirements outlined in this document. This product will be a web-app which streamlines appointments set up with the VCEA tutoring center. Students, Tutors, and Teachers will be able to set up appointments with each other through the web app without having to physically travel to the VCEA. The benefits in this is that students, teachers, and tutors waste less time in their daily lives and spend more of it being productive. The objective of this is to make the software easy to use, and efficient. The ultimate goal being implementation of a useful software into the VCEA to improve efficiency of the tutoring center.

## 1.3 Document Overview

The rest of the document contains the requirements in section 2, the user interface in section 3, the product backlog and references in section 4. Section 2 (requirements) contains all the required test cases as well as non functional requirements. Section 3 contains our mock-up of the User Interface (UI) which our application will use. And section four contains the backlog and references for use in documentation of the completion of our project.


----
# 2. Requirements Specification

This software will require computing power necessary to run the web-app. As well, it will need to be hosted online such that prospective students can visit it to make appointments and such that professors can interact with students on it. Therefore it must do this all within a reasonable budget affordable by the VCEA. It must have a secure admin structure such that there is only one super admin who assigns new admins who assign tutors who interacts with (gets subscribed) to students. This organization will allow correct workflow and security within the system.

## 2.1 Customer, Users, and Stakeholders

The customer using our application will be the VECA tutoring center at WSU as well as the students that utilize the tutoring services. The stakeholders are the VCEA tutoring center, professor Sakire, as well as the dean of the VCEA. 

The users of our software include students, tutors, professors, admin, and a super admin.

----
## 2.2 Use Cases

This section will include the specification for your project in the form of use cases. The section should start with a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.

This section includes the specification for the VCEA tutoring software in the form of use cases. 
The actors included in this app will include:
Super-Admin
Admin
Tutor
Student (Tutee)

| Use case # 1      |   |
| ------------------ |--|
| Name              | Register  |
| Users             | All Users  |
| Rationale         | In order to access the portal, users will need to login to the database. However, if no account is created in the database, then login would prove to be useless.  |
| Triggers          | Click the register submit button on the registration form.  |
| Preconditions     | User filled out the user information form.  |
| Actions           | Enter and Submit Account Info |
| Alternative paths | Logout - Register Link  |
| Postconditions    | User is redirected back to login page.  |
| Acceptance tests  | Database successfully updates with new user  |
| Iteration         | Iteration 1  |

| Use case # 2      |   |
| ------------------ |--|
| Name              | Log In  |
| Users             | All Users  |
| Rationale         | All users must log in to access the web application  |
| Triggers          | Open website  |
| Preconditions     | The user is registered |
| Actions           | Input username and password, hit submit  |
| Alternative paths | Log Out  |
| Postconditions    | Send user to homepage  |
| Acceptance tests  | Make sure the user is logged in and sent to the homepage  |
| Iteration         | Iteration 1  |

| Use case # 3     |   |
| ------------------ |--|
| Name              | Logout  |
| Users             | All Users |
| Rationale         | User should be able to sign in under different profile if necessary  |
| Triggers          | Logout button  |
| Preconditions     | User is logged in  |
| Actions           | Logs user out, redirects to login page  |
| Alternative paths | Close Browser  |
| Postconditions    | The user is sent back to the login page. |
| Acceptance tests  | User successfully returns to login page and is logged out |
| Iteration         | Iteration 1 |


| Use case # 4     |   |
| ------------------ |--|
| Name              | View Schedule  |
| Users             | All Users |
| Rationale         | Users need to be able to access and view the schedule in order to know when they can book appointments, have appointments scheduled, etc.  |
| Triggers          | View Schedule button  |
| Preconditions     | User is logged in  |
| Actions           | User navigates to view schedule section  |
| Alternative paths | None  |
| Postconditions    | The schedule for the user is displayed. |
| Acceptance tests  | Schedule successfully loads and is displayed |
| Iteration         | Iteration 3 |

| Use case # 5     |   |
| ------------------ |--|
| Name              | View Tutor Profile  |
| Users             | All Users |
| Rationale         | Users may want to learn more about the tutor.   |
| Triggers          | Click on view tutor profile button  |
| Preconditions     | User is logged in  |
| Actions           | User navigates to tutor profile page via button?  |
| Alternative paths | None  |
| Postconditions    | The profile for the tutor is displayed. |
| Acceptance tests  | Tutor profile successfully loads and is displayed |
| Iteration         | Iteration 1 |

| Use case # 6     |   |
| ------------------ |--|
| Name              | Edit Tutor Profile  |
| Users             | Tutor and Admin |
| Rationale         | Tutors may want to update their information/profile as needed.   |
| Triggers          | Click on edit profile button  |
| Preconditions     | Tutor user is logged in  |
| Actions           | Tutor user navigates to edit profile page  |
| Alternative paths | None  |
| Postconditions    | The editable profile for the tutor is displayed. |
| Acceptance tests  | Editable tutor profile successfully loads and is displayed |
| Iteration         | Iteration 1 |

| Use case # 7     |   |
| ------------------ |--|
| Name              | Submit Tutor Review Form  |
| Users             | Student |
| Rationale         | Tutors need to be reviewed by the students.   |
| Triggers          | Click on submit button at bottom of review form  |
| Preconditions     | Student user is logged in  |
| Actions           | Student user navigates to review form  |
| Alternative paths | None  |
| Postconditions    | Review form is submitted and the student is redirected to the dashboard. |
| Acceptance tests  | Review form is successfully added to the database |
| Iteration         | Iteration 3 |

| Use case # 8     |   |
| ------------------ |--|
| Name              | Create Tutor Profile  |
| Users             | Admin |
| Rationale         | Admins need to be able to create new tutors as new ones are hired.   |
| Triggers          | Click on create tutor button  |
| Preconditions     | Admin user is logged in  |
| Actions           | Admin user navigates to create tutor tab  |
| Alternative paths | None  |
| Postconditions    | A new tutor added in the database and admin is redirected to the dashboard. |
| Acceptance tests  | Tutor is successfully added to the database |
| Iteration         | Iteration 2 |

| Use case # 9     |   |
| ------------------ |--|
| Name              | Delete Tutor Profile  |
| Users             | Admin |
| Rationale         | Admins need to be able to delete tutors as they stop working there.   |
| Triggers          | Click on delete tutor button |
| Preconditions     | Admin user is logged in  |
| Actions           | Admin user navigates to delete tutor tab |
| Alternative paths | None  |
| Postconditions    | The tutor is deleted in the database and admin is redirected to the dashboard. |
| Acceptance tests  | Tutor is successfully deleted from the database |
| Iteration         | Iteration 2 |

| Use case # 10     |   |
| ------------------ |--|
| Name              | Schedule Tutor Times  |
| Users             | Admin |
| Rationale         | Admins need to be able to schedule the times that tutors are available.   |
| Triggers          | Click on schedule tutor button  |
| Preconditions     | Admin user is logged in and tutor exists in database  |
| Actions           | Admin user navigates to schedule tutor tab  |
| Alternative paths | None  |
| Postconditions    | The tutor is scheduled at specific times and the admin returns to the dashboard. |
| Acceptance tests  | Tutor is successfully associated with a timeslot? |
| Iteration         | Iteration 2 |

| Use case # 11     |   |
| ------------------ |--|
| Name              | Add classes  |
| Users             | Admin |
| Rationale         | Admins need to be able to add classes for tutoring.   |
| Triggers          | Click on add class button  |
| Preconditions     | Admin user is logged in  |
| Actions           | Admin user navigates to add class tab  |
| Alternative paths | None  |
| Postconditions    | The class is added to the database and admin is redirected to dashboard. |
| Acceptance tests  | The class is successfully added to the database |
| Iteration         | Iteration 2 |

| Use case # 12     |   |
| ------------------ |--|
| Name              | Delete classes  |
| Users             | Admin |
| Rationale         | Admins need to be able to delete classes from the tutoring list.   |
| Triggers          | Click on delete class button  |
| Preconditions     | Admin user is logged in  |
| Actions           | Admin user navigates to delete class tab |
| Alternative paths | None  |
| Postconditions   | The class is deleted from the database and admin is redirected to the dashboard. |
| Acceptance tests  | The class is successfully deleted from the database |
| Iteration         | Iteration 2 |

| Use case # 13     |   |
| ------------------ |--|
| Name              | Create Admin  |
| Users             | Super Admin |
| Rationale         | Super Admin needs to create new admins to manage the program.   |
| Triggers          | Click on create admin button  |
| Preconditions     | Super Admin user is logged in  |
| Actions           | Super Admin user navigates to create admin tab  |
| Alternative paths | None  |
| Postconditions    | A new admin is added in the database and the super admin is redirected to dashboard?. |
| Acceptance tests  | A new admin is successfully added to the database |
| Iteration         | Iteration 1 |

| Use case # 14     |   |
| ------------------ |--|
| Name              | Display Statistics  |
| Users             | Admins |
| Rationale         | Admins want to display statistics about what classes are being tutored most frequently and what times of the day are most busy   |
| Triggers          | Click on display statistics button  |
| Preconditions     | Admin user is logged in  |
| Actions           | Admin user navigates to display statistics tab  |
| Alternative paths | None  |
| Postconditions    | The statistics are properly displayed to the page |
| Acceptance tests  | Statistics are properly displayed |
| Iteration         | Iteration 2 |


| Use case # 15     |   |
| ------------------ |--|
| Name              | Schedule Tutoring Appointment  |
| Users             | Student |
| Rationale         | Students need to schedule appointments with tutors.   |
| Triggers          | Click on the schedule appointment button corresponding to the displayed tutor.  |
| Preconditions     | Student is logged in.  |
| Actions           | Students are redirected to the tutor scheduling page.   |
| Alternative paths | None  |
| Postconditions    | The page to schedule an appointment with a tutor is displayed. |
| Acceptance tests  | Page to schedule appointments is displayed. |
| Iteration         | Iteration 3 |


| Use case # 16     |   |
| ------------------ |--|
| Name              | Admin view tutor stats |
| Users             | Admin  |
| Rationale         | Allow admin to monitor tutor performance.   |
| Triggers          | Admin login and select view stats button |
| Preconditions     | Admin must be logged in  |
| Actions           |  Admin select a specific tutor  |
| Alternative paths | admin can  |
| Postconditions    | The editable profile for the tutor is displayed. |
| Acceptance tests  | Editable tutor profile successfully loads and is displayed |
| Iteration         | Iteration 2 |


| Use case # 17     |   |
| ------------------ |--|
| Name              | Create Admin Account |
| Users             | Super Admin |
| Rationale         | Tutors may want to update their information/profile as needed.   |
| Triggers          | Click on edit profile button  |
| Preconditions     | Tutor user is logged in  |
| Actions           | Tutor user navigates to edit profile page  |
| Alternative paths | None  |
| Postconditions    | The editable profile for the tutor is displayed. |
| Acceptance tests  | Editable tutor profile successfully loads and is displayed |
| Iteration         | Iteration 1 |


| Use case # 18     |   |
| ------------------ |--|
| Name              | Edit Tutor Profile  |
| Users             | Tutor |
| Rationale         | Tutors may want to update their information/profile as needed.   |
| Triggers          | Click on edit profile button  |
| Preconditions     | Tutor user is logged in  |
| Actions           | Tutor user navigates to edit profile page  |
| Alternative paths | None  |
| Postconditions    | The editable profile for the tutor is displayed. |
| Acceptance tests  | Editable tutor profile successfully loads and is displayed |
| Iteration         | Iteration 1 |

| Use case # 19     |   |
| ------------------ |--|
| Name              | Edit Tutor Profile  |
| Users             | Tutor |
| Rationale         | Tutors may want to update their information/profile as needed.   |
| Triggers          | Click on edit profile button  |
| Preconditions     | Tutor user is logged in  |
| Actions           | Tutor user navigates to edit profile page  |
| Alternative paths | None  |
| Postconditions    | The editable profile for the tutor is displayed. |
| Acceptance tests  | Editable tutor profile successfully loads and is displayed |
| Iteration         | Iteration 1 |

| Use case # 20     |   |
| ------------------ |--|
| Name              | Select class |
| Users             | Student |
| Rationale         | Students need to be able to choose a class for tutoring  |
| Triggers          | Click on “select class” button |
| Preconditions     | Student user is logged in  |
| Actions           | Student navigates to page for choosing class they need tutoring in |
| Alternative paths | None  |
| Postconditions    | Class options are displayed |
| Acceptance tests  | Student can select a class and see tutors for that class|
| Iteration         | Iteration 1 |


----
## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. [Enter a Concise Requirement Name]:  [provide a concise description, in clear and easily understandable language to specify the requirement]

----
# 3. User Interface

Here you should include the sketches or mockups for the main parts of the interface.

----
# 4. Product Backlog

Here you should include a link to your GitHub repo issues page, i.e., your product backlog. Make sure to create an issue for each use case. You should also create issues for the initial development tasks that you plan to work on during iteration1. 

----
# 4. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 

| Max Points  | **Content** |
| ----------- | ------- |
| 10          | Do the requirements clearly state the customers’ needs? |
| 5           | Do the requirements avoid specifying a design (note: customer-specified design elements are allowed; non-functional requirements may specify some major design requirements)? |
| | |  
|    | **Completeness** |
| 25 | Are use cases written in sufficient detail to allow for design and planning? |
| 4 | Do use cases have acceptance tests? | 
| 25 | Is your use case model complete? Are all major use cases included in the document? |
| 10 |  Are the User Interface Requirements given with some detail? Are there some sketches, mockups?  |
| | |  
|   | **Clarity** |
| 5 | Is the document carefully written, without typos and grammatical errors? |
| 4 | Is each part of the document in agreement with all other parts? |
|   | Are all items clear and not ambiguous? (Minor document readability issues should be handled off-line, not in the review, e.g. spelling, grammar, and organization). |
|   |   |
|    | **GitHub Issues** |
| 12 | Has the team setup their GitHub Issues page? Have they  generated the list of user stories, use-cases, created milestones, assigned use-cases (issues) to milestones?   Example GitHub repo (check the issues): https://github.com/WSU-CptS322-Fall2022/TermProjectSampleRepo/issues  |

