$('#submit').click(function(){
	$.post('/app/submit_score/', {'score': score, 'correct': correct, 'videos_seen': videos_seen}, function(data){
		alert("SCore submitted");
		$('#submit').attr("value", "Score submitted!");
	});
});