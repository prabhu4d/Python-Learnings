class Project:
    __projects = []

    def __init__(self, name, description, owned_by):
        self.name = name
        self.description = description
        self.owned_by = owned_by
        self.teams = []
        owned_by.projects.append(self)
        Project.__projects.append(self)

    def add_team(self, team):
        self.teams.append(team)
        team.project.append(self)

    @classmethod
    def details(cls):
        for project in cls.__projects:
            print(f"""\n
            Project: {project.name},
            Description: {project.description}
            Owned By: {project.owned_by.name}
            Teams : {[team.name for team in project.teams]}
            """)

    def __str__(self):
        teams = [team.name for team in self.teams]
        return f"""
        Name : {self.name}
        Description : {self.description}
        Owned By : {self.owned_by.name}
        Team : {teams}
        """
