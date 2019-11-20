// @TODO: YOUR CODE HERE!
// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, 
//and shift the latter by left and top margins.
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// to the margins set in the "chartMargin" object.
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Load data from data.csv
d3.csv("./assets/data/data.csv").then(function(statedata) {

  statedata.forEach(d => {
    d.poverty = +d.poverty;
    d.income = +d.income;
  });
  var xLinear = d3.scaleLinear()
    .domain([0, d3.max(statedata, d => d.poverty)])
    .range([0, width]);

  var yLinear = d3.scaleLinear()
    .domain([d3.min(statedata, d => d.income)*0.9, d3.max(statedata, d => d.income)*1.2])
    .range([height, margin.top]);

  // Step 6: Create Axes
  // =============================================
  
  var bottomAxis = d3.axisBottom(xLinear);
  var leftAxis = d3.axisLeft(yLinear);

 

    // Step 7: Append the axes to the chartGroup
  // ==============================================
  // Add bottomAxis
  chartGroup.append("g").attr("transform", `translate(0, ${height})`).call(bottomAxis);

  // Add leftAxis to the left side of the display
  chartGroup.append("g")
    .attr("stroke", "green")
    .call(leftAxis);
  
  svg.selectAll("circle")
    .data(statedata)
    .enter()
    .append("circle")
    .attr("cx", (d, i) => xLinear(d.poverty))
    .attr("cy", d => yLinear(d.income))
    .attr("r", 10);

    chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 20)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("Poverty");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .text("Income");
});


