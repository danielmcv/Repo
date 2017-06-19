$(document).ready(function(){
	$("#modal_publication").click(function(){
		$.ajax({
			url: '/publications/post/add/',
			type: 'get',
			datatype: 'json',
			beforeSend: function(){
				$('#post_modal').modal('show');
			}
		})
	});
});