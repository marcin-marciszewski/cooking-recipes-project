// The code was sourced from: http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/

queue()
	.defer(d3.json, "/statistics/recipes")
	.await(makeGraphs);

function makeGraphs(error, recipesJson) {

	//Format data
	var cookingRecipies = recipesJson;
	var dateFormat = d3.time.format("%Y-%m-%d");
	cookingRecipies.forEach(function(d) {
		d["date_posted"] = dateFormat.parse(d["date_posted"]);
		d["date_posted"].setDate(1);
	});

	//Create a Crossfilter instance
	var ndx = crossfilter(cookingRecipies);

	var dateDim = ndx.dimension(function(d) { return d["date_posted"]; });
	var cusineNameDim = ndx.dimension(function(d) { return d["cuisine_name"]; });
	var preparationTimeDim = ndx.dimension(function(d) { return d["preparation_time"]; });
	var cookingTimeDim = ndx.dimension(function(d) { return d["cooking_time"]; });



	var numRecipesByDate = dateDim.group();
	var numRecipesByCuisineName = cusineNameDim.group();
	var numRecipesByPreparationTime = preparationTimeDim.group();
	var numRecipesByCookingTime = cookingTimeDim.group();


	var all = ndx.groupAll();

	var minDate = dateDim.bottom(1)[0]["date_posted"];
	var maxDate = dateDim.top(1)[0]["date_posted"];


	//Charts
	var recipesChart = dc.barChart("#recipes-chart");
	var cuisineNameChart = dc.rowChart("#cuisine-name-chart");
	var preparationTimeChart = dc.rowChart("#preparation-time-chart");
	var cookingTimeChart = dc.rowChart("#cooking-time-chart");

	var totalRecipes = dc.numberDisplay("#total-recipes");

	totalRecipes
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d) { return d; })
		.group(all);

	recipesChart
	.width(600)
	.height(450)
	.margins({top: 10, right: 50, bottom: 30, left: 50})
	.dimension(dateDim)
	.group(numRecipesByDate)
	.transitionDuration(500)
	.x(d3.time.scale().domain([minDate, maxDate]))
	.elasticY(true)
	.xAxisLabel("Year")
	.yAxis().ticks(1);

	cuisineNameChart
		.width(600)
		.height(600)
		.margins({ top: 10, right: 50, bottom: 30, left: 50 })
		.dimension(cusineNameDim)
		.group(numRecipesByCuisineName)
		.xAxis().ticks(5);

	preparationTimeChart
		.width(400)
		.height(400)
		.margins({ top: 10, right: 50, bottom: 30, left: 50 })
		.dimension(preparationTimeDim)
		.group(numRecipesByPreparationTime)
		.xAxis().ticks(5);

	cookingTimeChart
		.width(400)
		.height(400)
		.margins({ top: 10, right: 50, bottom: 30, left: 50 })
		.dimension(cookingTimeDim)
		.group(numRecipesByCookingTime)
		.xAxis().ticks(5);

	dc.renderAll();

};
