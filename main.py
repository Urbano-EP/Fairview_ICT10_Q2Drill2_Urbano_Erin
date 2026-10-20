from pyscript import display, document

def add_member(e):
    document.getElementById('output1').innerHTML =""

    grade7_members = {'John Jones', 'Jane Smith'}
    grade8_members = {'Doe Johnson', 'Alice Walker'}
    grade9_members = {'Bob Martinez', 'Charlie Brown'}
    grade10_members = {'Diana Prince', 'Evan Wright'}

    input_member = document.getElementById('FirstName').value
    input_member2 = document.getElementById('LastName').value
    #assign the value to set variable
    new_member_set = {input_member + " " + input_member2}
     
    all_members = grade7_members | grade8_members | grade9_members | grade10_members | new_member_set

    total_members = len(all_members)

    member_list = "<br>".join(sorted(all_members))

    #display
    document.getElementById('output1').innerHTML = f'All members: <br> {member_list}'
    display(f'Total members: {total_members}', target= "output1")