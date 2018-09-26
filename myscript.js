function getData(year){
    var url = `project.py?year=${year}`
    $.getJSON(url, function(data) {
        console.log(data)
        data = JSON.parse(data);
        $('#sl').val(data.sl)
        $('#in').val(data.in)
        $('#pr').val(data.pr)
    })
}

$(document).ready(function() {
    $('#btn').click(function() {
        getData($('#year').val());
    })
})