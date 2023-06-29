async function loadTableRole(){
    clearTableRole();
    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };

    const roles = await fetch("/api/role/allowed", requestOptions)
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

function clearTableRole() {
   
    var table = document.getElementById("group-table");
    var tbody = table.querySelector("tbody");
    var rows = tbody.querySelectorAll("tr");
    for (var i = rows.length - 1; i > 0; i--) {
        tbody.removeChild(rows[i]);
    }
}

async function editPermission(dialogId, roleId){
   const dialog = document.getElementById(dialogId);
  const tree = dialog.querySelector('#tree'); // Lấy cây từ dialog

  const permissions = [];

  // Lặp qua từng node trong cây
  tree.querySelectorAll('[data-role="node"]').forEach(node => {
    const checkbox = node.querySelector('input[type="checkbox"]');

    // Kiểm tra node có được chọn không
    if (checkbox.checked) {
      const nodeId = node.getAttribute('data-id');
      id = parseInt(nodeId)-1
      if (list_tree[id]>-1){
        permissions.push(list_tree[id]);
      }
    }
  });
  
    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "role_id": roleId,
    "permissions": permissions
    });

    var requestOptions = {
    method: 'PUT',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    editPermission = await fetch("/api/rolepermisssion/", requestOptions)
    if (editPermission.status===202){
        closeDialog('edit-role-dialog');
    }

}



   