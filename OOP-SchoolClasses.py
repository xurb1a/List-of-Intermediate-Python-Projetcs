class School:
    def __init__(self, name, numberOfStudents, level=None):
        self.name = name
        self.level = level if level is not None else ['primary', 'middle', 'high']
        self.numberOfStudents = numberOfStudents

    # Getters
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    # Setters
    def set_numberOfStudents(self, value):
        self.numberOfStudents = value

    # Representation method
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."


# Subclasses
class Primary(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, numberOfStudents, level=['primary'])
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr} Pickup Policy: {self.pickupPolicy}"


class Middle(School):
    pass


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams=None):
        super().__init__(name, numberOfStudents, level=['high'])
        self.sportsTeams = sportsTeams if sportsTeams is not None else []

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        parent_repr = super().__repr__()
        sports_teams_info = ", ".join(self.sportsTeams) if self.sportsTeams else "No sports teams"
        return f"{parent_repr} Sports Teams: {sports_teams_info}"


# # Creating a PrimarySchool object
# primary_school = Primary("Greenwood Primary", 300, "Pickup after 3pm")

# # Verifying the constructor, getter, and __repr__ method
# print(primary_school)  # A ['primary'] school named Greenwood Primary with 300 students. Pickup Policy: Pickup after 3pm
# print(primary_school.get_pickupPolicy())  # Pickup after 3pm


# high_school = HighSchool("Sunnydale High", 500, sportsTeams=["Basketball", "Soccer", "Tennis"])

# # Verifying the constructor, getter, and __repr__ method
# print(high_school)  # Should display information including sports teams
# print(high_school.get_sportsTeams())  # Should return the list of sports teams
