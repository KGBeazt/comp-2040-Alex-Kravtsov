# messy data string
data = "employee_name: Sarah, department: HR, roles: recruiter, trainer | employee_name: Mike , department: Engineering , roles: developer, team lead | employee_name: Alice , department: HR , roles: recruiter"

# expected output
[
    {
        'employee_name': 'Sarah',
        'department': 'HR',
        'roles': ['recruiter', 'trainer']
    },
    {
        'employee_name': 'Mike',
        'department': 'Engineering',
        'roles': ['developer', 'team lead']
    },
    {
        'employee_name': 'Alice',
        'department': 'HR',
        'roles': ['recruiter']
    }
]