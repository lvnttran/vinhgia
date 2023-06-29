var list_tree = [];
var treeInstance = null;
async function openDialog(dialogId, roleId = None) {

    const dialog = document.getElementById(dialogId)
    

    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");
    var dataSource = [];
    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };

    data = await fetch("/api/router/resources", requestOptions)
    if (data.status === 200){
        dataSource = await data.json()
        
    }
    dataSource = customizeDataSource(dataSource);
    list_tree = list_per_to_list_tree(dataSource)
    tree = document.getElementById('tree');
    if (!treeInstance){
        var treeInstance = $(tree).tree({
            uiLibrary: 'bootstrap4',
            dataSource: dataSource,
            checkboxes: true
        });
    }
    


    treeInstance.expandAll();
    var checkboxes = treeInstance.find('input[type="checkbox"]');
    // console.log(checkboxes);
    checkboxes.prop('checked', false);
    
    if (roleId){
        const edit_permisson = dialog.querySelector('#edit-permisson')
        edit_permisson.value = roleId
        var myHeaders = new Headers();
        myHeaders.append("accept", "application/json");

        var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
        };

        data = await fetch(`/api/rolepermisssion/${roleId}`, requestOptions)
        var checkboxes = dialog.querySelectorAll('input[type="checkbox"]');
        for (var i = 0; i < checkboxes.length; i++) {
             // Chọn từng checkbox
          }
        // console.log(checkboxes);
        if (data.status===200){
            list_checked = await data.json();
            list_checked.forEach(function(value) {
                id = parseInt(list_tree.indexOf(value['permission_id']));
                checkboxes[id].click();
               
            }); 
        }

}
    dialog.showModal();
}
function customizeDataSource(data) {
    var customizedData = [];

    // Duyệt qua từng đối tượng trong mảng data và tạo đối tượng tùy chỉnh
    for (var i = 0; i < data.length; i++) {
        var item = data[i];
        var customizedItem = {
            text: item.name,
            id: item.id,
            children: []
        };

        // Duyệt qua từng quyền trong mảng permissions và tạo đối tượng tùy chỉnh cho mỗi quyền
        for (var j = 0; j < item.permissions.length; j++) {
            var permission = item.permissions[j];
            var customizedPermission = {
                text: permission.name,
                id: permission.id
            };

            // Thêm quyền vào mảng children của đối tượng cha
            customizedItem.children.push(customizedPermission);
        }

        // Thêm đối tượng tùy chỉnh vào mảng customizedData
        customizedData.push(customizedItem);
    }
    return customizedData;
}

async function get_data_permisson(){
    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };

    data = await fetch("/api/router/resources", requestOptions)
    if (data.status === 200){
        data = await data.json()
        return data;
    }
    return [];
    
}


function closeDialog(dialogId) {
    const dialog = document.getElementById(dialogId)
    dialog.close();
}


function list_per_to_list_tree(data){
    list = [];
    for (var i = 0; i < data.length; i++){
        list.push(-100)
        childrens = data[i]['children']
        for (var j = 0; j < childrens.length; j++){
            children = childrens[j]
            list.push(children['id'])
        }
    }
    return list;
}