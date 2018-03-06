

function processJSONToTable(json_string){
   //response
    json_pitch = JSON.parse(json_string);
    trans_list = json_pitch["response"];

    var tbl = "<table class='table'>" +
              "<tr><th scope='col'>Transaction Hash</th>\
              <th scope='col'>Inputs</th>\
              <th scope='col'>Outputs</th></tr>"

    var tbl_end = "</table>"
    innerString = ""

    for (var i = 0; i < trans_list.length; i++){
      innerString += "<tr > <td scope='col'> <a href='"+
      trans_list[i]["link"]+
      "'>" +
      trans_list[i]["txHash"] +
      "</td> <td scope='col'><div class='cap-cell'>" +
      JSON.stringify(trans_list[i]["inputs"]) +
      "</div></td> <td scope='col'><div class = 'cap-cell'>" +
      JSON.stringify(trans_list[i]["outputs"])+
       "</div></td></tr>"
    }

    final_tbl = tbl + innerString + tbl_end;

    return final_tbl;
}

function getLargeBTC(){
    var endpoint = "/btc_recent_big_trans";
    var val = $(".btcinput").val()

    if(typeof(val) != "undefined") {
      endpoint += "?tolerance=" + String(val)
    }

    $(".loaderbtc").show();
    $.ajax({url: endpoint, success : function(result) {
        var final_table = processJSONToTable(result);
        $("#btc-lg").html(String(final_table));
        $(".loaderbtc").hide();
}})};

function getLargeETH(){

   var endpoint = "/eth_recent_big_trans";
   var val = $(".ethinput").val()

   if(typeof(val) != "undefined") {
     endpoint += "?tolerance=" + String(val)
   }
    $(".loadereth").show();

    $.ajax({url: endpoint, success : function(result) {
          var final_table = processJSONToTable(result);
          $("#eth-lg").html(String(final_table));
          $(".loadereth").hide();
}})};
