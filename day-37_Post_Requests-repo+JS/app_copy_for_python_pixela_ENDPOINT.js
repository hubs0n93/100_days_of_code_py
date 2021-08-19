const express = require("express");
const request = require("request");
const bodyParser = require("body-parser");
const https = require("https");

const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: false}));


app.get("/", function(req, res){
  res.sendFile(__dirname + "/signup.html");
});

app.post("/", function(req, res){
  var firstName = req.body.firstName;
  var secondName = req.body.secondName;
  var email = req.body.email;

  var data = {
    date: "20210802",
    quantity: "5",
  };
  console.log(data)
  var jsonData = JSON.stringify(data);
  const url = "https://pixe.la/v1/users/hubson93/graphs/graph1";
  const options = {
    method: "POST",
    headers: {"X-USER-TOKEN": "lkj435sdlkj34"}
  }

  const request = https.request(url, options, function(response){
    response.on("data", function(data){
      console.log(JSON.parse(data));
    });
  });

  request.write(jsonData);
  request.end();

})

app.listen(3000, function(){
  console.log("Server is running at port 3000");
});


// hs2LnreXxCMaH3E4HpK10w
