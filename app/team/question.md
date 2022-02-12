# Team

## Characters and Scenario

- Clients give projects to Company
- Company
  - have only one owner
  - many employees
  - many projects given by client
  - employees are grouped by teams
  - projects done by many teams, one team can have many projects
  - employee belongs to only one team
  - create a owner, teams, employees
  - add employees to teams
  - add teams to projects

## Implementation Guide

- create a abstract person class

  - name, age, email, location attributes
  - tell_about_yourself abstract class

- create Employee, Owner, Client classes which inherit Person class

  - tell_about_yourself just print statement about the object
    - for example the employee object should print
      - Hi I am employee_name, My Team is team_name
  - only one object can be instantiated for Owner class
  - Attributes
    - Employee : team
    - Owner : company
    - Client : company, projects

- class Project

  - attributes
    - name, description, owned_by (client object), teams
  - add_team method

- class Team

  - attributes
    - name, projects, employees
  - add_employee method

- create details method for Employee, Client, Project, Team
  - it should print details about their objects
  - example:
    - Employee.details() should print all the employees name and team

## Output

- print(example_team)
  - it should print the team name, employees, and the projects
- Team.details()
  - should print all the team details
- print(example_employee), print(example_client), print(example_project)
- Employee.details(), Client.details(), Project.details()
