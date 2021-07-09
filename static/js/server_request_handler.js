$("#add_button").click(function(e) {
    e.preventDefault(); // prevents page refreshing
    var first_number_value = $("#first_number").val();
    var second_number_value = $("#second_number").val();
    var condition1 = first_number_value == "";
    var condition2 = second_number_value == "";
    if (condition1 || condition2) {
        console.log("Empty values")
    } else {
        console.log("Values are not empty!");
        $.ajax({
              type : 'POST',
              url : "/summation",
              data : {'number1':first_number_value, 'number2': second_number_value},
              success: function(response) {
                console.log(response);
                Materialize.toast('Summation Prediction: ' + response['prediction'].toString(), 5000)
              },
              error: function(error) {
                console.log(error);
              }
        });
    }

});

$("#substruction_button").click(function(e) {
    e.preventDefault(); // prevents page refreshing
    var first_number_value = $("#first_number_subtraction").val();
    var second_number_value = $("#second_number_subtraction").val();
    var condition1 = first_number_value == "";
    var condition2 = second_number_value == "";
    if (condition1 || condition2) {
        console.log("Empty values")
    } else {
        console.log("Values are not empty!");
        $.ajax({
              type : 'POST',
              url : "/substruction",
              data : {'number1':first_number_value, 'number2': second_number_value},
              success: function(response) {
                console.log(response);
                Materialize.toast('Subtraction Prediction: ' + response['prediction'].toString(), 5000)
              },
              error: function(error) {
                console.log(error);
              }
        });
    }

});