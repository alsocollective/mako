var data = [{
	var1: 20,
	var2: 5,
	deg: 50,
	weight: 2
}, {
	var1: 25,
	var2: 15,
	deg: 90,
	weight: 10
}, {
	var1: 10,
	var2: 10,
	deg: 80,
	weight: 5
}]

var svgContainer = d3.select(".forshow").append("svg")
svgContainer
	.attr("width", 200)
	.attr("height", 200);

var group = svgContainer.selectAll("g")
	.data(data)
	.enter()
	.append("g")
	//attributes of each group
	.attr('transform', function(d, i) {
		return "translate(" + ((i + 1) * 50) + "," + ((i + 1) * 50) + ")"
	})

var circles = group.append("circle")
	//attributes of each cirlce
	.attr("r", function(d) {
		return d.var1;
	})
	.attr("fill", "#fc0");

var lines = group.append('line')
	//attributes of each line
	.attr("x1", function(d, i) {
		return d.var1;
	})
	.attr("y1", function(d, i) {
		return 0;
	})
	.attr("x2", function(d, i) {
		return (-1 * d.var1) - d.var2;
	})
	.attr("y2", function(d, i) {
		return 0;
	})
	.attr("transform", function(d, i) {
		return "rotate(" + d.deg + ")";
	})
	.attr("stroke-width", function(d) {
		return d.weight
	})
	.attr("stroke", "black");

var arrowhead = group.append('path')
	.attr('d', function(d) {
		var scale = d.weight * 2;
		return 'M ' + ((-1 * d.var1) - d.var2) + ' ' + -scale + ' l -' + scale + ' ' + scale + ' l ' + scale + ' ' + scale + ' z';
	})
	.attr("transform", function(d, i) {
		return "rotate(" + d.deg + ")";
	})
	.attr("fill", "#000")