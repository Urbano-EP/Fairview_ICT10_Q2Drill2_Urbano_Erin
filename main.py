from pyscript import display, document

def add_member(e):
    document.getElementById('output1').innerHTML =""

    members={'John', 'Jane', 'Doe'}

    input_member = document.getElementById('FirstName').value
    input_member2 = document.getElementById('LastName').value

    #assign the value to set variable
    new_member_set = {input_member, input_member2} 

    all_members = members | new_member_set

    total_members = len(members | new_member_set)

    member_list = "<br>".join(sorted(all_members))

    #display
    document.getElementById('output1').innerHTML = f'All members: <br> {member_list}'
    display(f'Total members: {total_members}', target= "output1")