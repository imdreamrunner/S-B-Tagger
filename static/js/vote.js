var posted = false;

function vote(choice) {
    if (posted) {
        alert("Your vote is being submitted.");
        return;
    }
    posted = true;
    var item_id = parseInt($("#item_id").html());
    console.log('Item ID: ' + item_id);
    console.log('Choice: ' + choice);
    $.ajax({
        url: '/vote/' + item_id,
        method: 'post',
        data: {
            choice: choice
        },
        success: function(ret) {
            alert(ret);
            location.reload();
        },
        error: function(ret) {
            alert(ret);
            location.reload();
        }
    })
}