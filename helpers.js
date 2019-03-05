advise_url = "https://api.adviceslip.com/advice"
my_api_url = "http://localhost:8080/api/new"
teacher_api = "http://sf-pyw.mosyag.in/m04/api/forecasts"

 $("#header").click( function(){
    
   $.getJSON(teacher_api, function(data){
       hor = data["prophecies"]
       
       set_content_in_divs(hor)
       function set_content_in_divs(paragraphs) {
         $.each(paragraphs, function(i, d) {
           p = $("#p-" + i)
           p.html("<p>" + d + "</p>")    
   })
}})})