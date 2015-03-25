$('#submit').click(function(){
	alert("AJAX");
	$.post('/vidpop/submit_score/', {'score': score, 'correct': correct, 'videos_seen': videos_seen}, function(data){
		alert("Score submitted");
		$('#submit').attr("value", "Score submitted!");
	});
});