async function loadTableGroups(){
    clearTableGroups();
    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };

    const roles = await fetch("/api/role/", requestOptions)
    if (roles.status ===200){
        const data = await roles.json();
        table = document.getElementById('group-table');
        var rowTemplate = await table.querySelector('#example-group-row');
        for (let i = 0; i < data.length; i++){
            row = data[i]
            const newRow = rowTemplate.cloneNode(true);
            newRow.id =''
            const serial = newRow.querySelector('#serial');
            const id_group = newRow.querySelector('#id-group');
            const name_group = newRow.querySelector('#name-group');
            const name_factory = newRow.querySelector('#name-factory');
            const name_workshop = newRow.querySelector('#name-workshop');
            const btn_edit = newRow.querySelector('#btn-edit');
            const btn_delete = newRow.querySelector('#btn-delete');
        
            serial.innerText = `${i+1}.`;
            id_group.innerText= row['id']
            name_group.innerText= row['name']
            name_factory.innerText= row['workshop']['factory']['name']
            name_workshop.innerText= row['workshop']['name']
            btn_edit.id  = row['id']
            btn_delete.id = row['id']
            newRow.style.display = '';
            table.querySelector('tbody').appendChild(newRow);
        }
      
    }

}

function clearTableGroups() {
   
    var table = document.getElementById("group-table");
    var tbody = table.querySelector("tbody");
    var rows = tbody.querySelectorAll("tr");
    for (var i = rows.length - 1; i > 0; i--) {
        tbody.removeChild(rows[i]);
    }
}


async function addRole(dialog_id){
    dialog_add_role = document.getElementById(dialog_id);
    const role_name = dialog_add_role.querySelector('#role-name').value;
    workshop_selection =dialog_add_role.querySelector('#workshop-selection').value;
    
    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "name": role_name,
    "workshop_id": workshop_selection
    });

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    const role = await fetch("/api/role/", requestOptions)
    if (role.status === 201){
        closeDialog(dialog_id);
        loadTableGroups();
    }
}


async function deleteRole(role_id) {
    var confirmDeleteRole = confirm(`Bạn có chắc chắn xóa nhóm có id ${role_id} không?`);
    if (confirmDeleteRole) {
        const deleteRole = await fetch('/api/role/' + role_id, {
            method: 'DELETE',
            headers: {
                'Authorization': localStorage.getItem('Authorization'),
                'Accept': 'application/json'
            },
        })
        if (deleteRole.status ===204){
            loadTableGroups();
        }
    }
}

async function editRole(dialog_id){
    dialog_add_role = document.getElementById(dialog_id);
    const role_name = dialog_add_role.querySelector('#role-name').value;
    const role_id = dialog_add_role.querySelector('#role-id').value;
    workshop_selection =dialog_add_role.querySelector('#workshop-selection').value;

    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "name": role_name,
    "workshop_id": workshop_selection,
    "id": role_id
    });

    var requestOptions = {
    method: 'PUT',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    role = await fetch("http://localhost:8080/api/role/", requestOptions)
    if (role.status === 202){
        closeDialog(dialog_id);
        loadTableGroups();
    }
}