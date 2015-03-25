$('#submit').click(function(){
	$.post('/app/submit_score/', {'score': score, 'correctAnswers': correctAnswers, 'videosSeen': videosSeen}, function(data){
		$('#submit').attr("value", "Score submitted!");
	});
});