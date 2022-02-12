class Team:
    __teams = []

    def __init__(self, name, project=None):
        self.name = name
        self.project = [project] if project else []
        self.employees = []
        Team.__teams.append(self)

    def add_employee(self, employee):
        try:
            if not employee.team:
                self.employees.append(employee)
                employee.team = self
            else:
                raise Exception(
                    f"\n{employee.name} already in {employee.team.name} Team")
        except Exception as e:
            print(e)

    @classmethod
    def details(cls):
        for team in cls.__teams:
            print(f"""\n
            Team : {team.name}
            Projects : {[project.name for project in team.project]}
            Employees : {[member.name for member in team.employees]} 
            """)

    def __str__(self):
        return f"""\n
        Name : {self.name}
        Project : {[project.name for project in self.project]}
        Employees : {[member.name for member in self.employees]}
        """
