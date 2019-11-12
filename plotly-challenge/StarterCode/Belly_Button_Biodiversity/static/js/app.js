function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel
  var sample_metadata_url = `/metadata/${sample}`;
  d3.json(sample_metadata_url).then(function (data) {
    var sample_metadata = d3.select("#sample-metadata");
    
// Fetch the JSON data and console log it

  // d3.json(url2).then((data1) => { console.log(data) });

console.log(Object.entries(data));
// Use `d3.json` to fetch the metadata for a sample
// Use d3 to select the panel with id of `#sample-metadata`


// Use `.html("") to clear any existing metadata
sample_metadata.html("");
// Use `Object.entries` to add each key and value pair to the panel
// Hint: Inside the loop, you will need to use d3 to append new
// tags for each key-value in the metadata.
Object.entries(data).forEach(function ([key, value]) {
 sample_metadata.append("h6").text(`${key}:${value}`);
});

// BONUS: Build the Gauge Chart
// buildGauge(data.WFREQ);
});
};
function buildCharts(sample) {
  var sample_samples_url = `/samples/${sample}`;


  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(sample_samples_url).then(function (data) {
    // var sample_samples = d3.select("#sample-samples");

    // @TODO: Build a Bubble Chart using the sample data    

    var trace1 = {
      x: data.otu_ids,
      y: data.sample_values,
      type: "scatter",
      mode: 'markers',
      marker: {
        color: data.otu_ids,
        size: data.sample_values
        // sizemode: 'area'
      },
      text: data.otu_labels
    }
    var layout = {
      title: "OTU ID",
      showlegend: true,
      height: 600,
      width: 1600,
  }
  
  var bubblechart = [trace1];
  //var bubbleid = d3.select("#bubble");
  Plotly.plot('bubble', bubblechart, layout);
});
// @TODO: Build a Pie Chart
// HINT: You will need to use slice() to grab the top 10 sample_values,
// otu_ids, and labels (10 each).
var sample_samples_url = `/samples/${sample}`;
d3.json(sample_samples_url).then(function (data) {
  var values = data.sample_values.slice(0, 10);
  var labels = data.otu_ids.slice(0, 10);
  // var display = data.otu_labels.slice(0, 10);


  var pie_chart = [{
    values: values,
    labels: labels,
    // display: data.otu_labels,
    type: "pie"
  }];
  
  Plotly.plot('pie', pie_chart);
});
};

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
