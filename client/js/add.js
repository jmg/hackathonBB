function goal(value){
	if(value == 'goal') {
		jQuery('#tag-select').css("display","none");
		console.log('goal');
	} else {
		jQuery('#tag-select').css("display","block");
	}
};
