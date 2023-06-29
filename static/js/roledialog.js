async function openDialog(dialogId, roleId = None) {

    const dialog = document.getElementById(dialogId)
    dialog.showModal();
    workshop_selection =dialog.querySelector('#workshop-selection');
    clearWorkshopSelection(workshop_selection);
    loadWorkshopSelection(workshop_selection);
    if (roleId){
        var myHeaders = new Headers();
        myHeaders.append("accept", "application/json");

        var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
        };

        role = await fetch(`/api/role/${roleId}`, requestOptions)
        if (role.status ===200){
            data = await role.json()
            workshop_selection.value = data['workshop_id']
            dialog.querySelector('#role-id').value =data['id'];
            dialog.querySelector('#role-name').value =data['name'];
        }
    }

}

function closeDialog(dialogId) {
    const dialog = document.getElementById(dialogId)
    dialog.close();
}

async function loadWorkshopSelection(select){
    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };
    const factorys = await fetch("/api/factory/factorys", requestOptions)
    if (factorys.status ===200){
        const data = await factorys.json();
       
        for (let i = 0; i < data.length; i++){
            factory = data[i]
            var optgroup = document.createElement('optgroup');
            optgroup.label = factory['name'];
            workshops= factory['workshops']
            for (let j = 0; j < workshops.length; j++){
                workshop = workshops[j]
                var option = document.createElement('option');
                option.value = workshop.id;
                option.textContent = workshop.name;
                optgroup.appendChild(option);
            }
            select.appendChild(optgroup);
        }
    }
    
}

function clearWorkshopSelection(select){
    while (select.firstChild) {
    select.removeChild(select.firstChild);
    }
}