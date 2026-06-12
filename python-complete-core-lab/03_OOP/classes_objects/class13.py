"""
This file(module) is Use to show the modification of attribute .
"""
class College:
    """ This class is Use to display information of Device """
    @classmethod
    def xyz_college(cls):
        cls.college_name = "R.N "
        cls.college_location = "Patna"
        return f"College name : {cls.college_name} || College Location : {cls.college_location}"

    @staticmethod
    def abc_college():
        college_name = "S.T"
        college_location = "Road"
        return f"College name : {college_name}  || College Location : {college_location}"

    def __init__(self, name, place):
        """ Use to initialize the attribute  """
        self.c_name = name
        self.c_place = place


    def pqr_college(self):
        return f"College name : {self.c_name}  || College Location : {self.c_place}"


my_college = College("abc", "Anyware")
print(my_college.pqr_college())
print(College.xyz_college())
print(my_college.abc_college())

# ------------------- Modification of attributes in given values-----------------------#
# syntax  object_name.attributes_name = new_value
# syntax class_name.attribute_name = new_value
# ------------------- Modification of attributes in given values-----------------------#
print(my_college.__dict__)        # Before modification
my_college.c_name = "IIT PATNA"  # Modify the attributes
my_college.c_place = "BIHAR"     # Modify the attributes
print(my_college.__dict__)       # After modification
