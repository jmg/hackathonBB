function selectAdd() {
    document.getElementById('page-add').style.display = 'block';
    document.getElementById('page-edit').style.display = 'none';
		document.getElementById('page-reports').style.display = 'none';  
		document.getElementById('page-config').style.display = 'none';  
}

function selectEdit() {
    document.getElementById('page-add').style.display = 'none';
    document.getElementById('page-edit').style.display = 'block';
		document.getElementById('page-reports').style.display = 'none';  
		document.getElementById('page-config').style.display = 'none';  
}

function selectReports() {
    document.getElementById('page-add').style.display = 'none';
    document.getElementById('page-edit').style.display = 'none';
		document.getElementById('page-reports').style.display = 'block';  
		document.getElementById('page-config').style.display = 'none';  
}

function selectConfig() {
    document.getElementById('page-add').style.display = 'none';
    document.getElementById('page-edit').style.display = 'none';
		document.getElementById('page-reports').style.display = 'none';  
		document.getElementById('page-config').style.display = 'block';  
}

