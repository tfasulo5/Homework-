// from data.js
var tableData = data;
var tbody = d3.select("tbody");


function buildtable(data) {
  data.forEach(function(aliensReport) {
    console.log(aliensReport);
    var row = tbody.append("tr");
    Object.entries(aliensReport).forEach(function([key, value]) {
      console.log(key, value);
      // Append a cell to the row for each value
      // in the weather report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
}
buildtable(data)
// Select the button
var button = d3.select("#filter-btn");

button.on("click", function() {
  console.log("it works")
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");
  
  console.log(inputValue);
  var filteredData = data.filter(row => row.datetime === inputValue);

  console.log(filteredData)
  tbody.html("")
  buildtable(filteredData)
})

 
  