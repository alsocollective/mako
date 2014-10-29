var data = [{
	var1: 20,
	var2: 5,
	deg: 50
}, {
	var1: 25,
	var2: 15,
	deg: 90
}]

var svgContainer = d3.select(".forshow").append("svg")
svgContainer
	.attr("width", 200)
	.attr("height", 200);

var circles = svgContainer.selectAll("circle")
	.data(data)
	.enter()
	.append("circle");

var circleAttributes = circles
	.attr("cx", function(d, i) {
		return (i + 1) * 50;
	})
	.attr("cy", function(d, i) {
		return (i + 1) * 50;
	})
	.attr("r", function(d) {
		return d.var1;
	})
	.attr("fill", "#fc0")