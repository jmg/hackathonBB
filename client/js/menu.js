function selectAdd() {
    document.getElementById('page-add').style.display = 'block';
    document.getElementById('page-edit').style.display = 'none';
    document.getElementById('page-tag').style.display = 'none';
		document.getElementById('pag-config').style.display = 'none';  
}

function selectEdit() {
    document.getElementById('page-add').style.display = 'none';
    document.getElementById('page-edit').style.display = 'block';
    document.getElementById('page-tag').style.display = 'none';
		document.getElementById('pag-config').style.display = 'none';  
}

function selectTag() {
    document.getElementById('page-add').style.display = 'none';
    document.getElementById('page-edit').style.display = 'none';
    document.getElementById('page-tag').style.display = 'block';
		document.getElementById('pag-config').style.display = 'none';  
}

function selectConfig() {
    document.getElementById('page-add').style.display = 'none';
    document.getElementById('page-edit').style.display = 'none';
    document.getElementById('page-tag').style.display = 'none';
		document.getElementById('pag-config').style.display = 'block';  
}

