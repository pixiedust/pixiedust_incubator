window.Pixiedust = window.Pixiedust || {};
window.Pixiedust.twitterdemo = window.Pixiedust.twitterdemo || {};

(function(pix, d3) {
  var color = d3.scale.category20();

  pix.twitterdemo.groupedchart = function(selector, chartdata, sentimentcolors) {
    var data = chartdata || [];
    color = sentimentcolors ? sentimentcolors : color;

    var groupKeys = data[0];
    groupKeys = groupKeys.slice(1);

    data.shift();
    data = data.map(function(dt) {
      var g = { key: dt[0] };
      g.groups = groupKeys.map(function(key, index) {
        return {
          key: key,
          value: dt[index+1]
        }
      });
      return g;
    });

    data = [data];

    var selection = d3.select(selector);
    var margin = {top: 20, right: 155, bottom: 55, left: 50};
    var box = selection.node().getBoundingClientRect();
    var width = box.width - margin.left - margin.right - 5;
    var height = box.height - margin.top - margin.bottom - 5;

    // setup the svg element
    var svg = selection.selectAll('svg').data([data]);
    svg.enter().append('svg');
    svg.attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom);
    svg.exit().remove();

    // setup series graph for each series
    var sGraph = svg.selectAll('g.series').data(data);
    sGraph.enter().append('g')
        .attr('class', 'series')
    sGraph.attr('transform', function(d, i) {
      return 'translate(' + margin.left + ',' + margin.top + ')';
    })
    sGraph.exit().remove();

    sGraph.each(function(sData, index) {
      var graph = d3.select(this);

      var xScale = d3.scale.ordinal().rangeRoundBands([0, width], .1);
      var groupScale = d3.scale.ordinal();
      var yScale = d3.scale.linear().range([height, 0]);

      // define the axis
      var xAxis = d3.svg.axis().scale(xScale).orient('bottom');
      var yAxis = d3.svg.axis().scale(yScale).orient('left').tickFormat(d3.format('.2s'));

      // scale the data
      xScale.domain(sData.map(function(d) { return d.key; }));
      groupScale.domain(groupKeys).rangeRoundBands([0, xScale.rangeBand()]);
      yScale.domain([0, d3.max(sData, function(d) { return d3.max(d.groups, function(d) { return d.value; }); })]);

      // setup the x axis
      var xaxis = graph.selectAll('g.x').data([sData]);
      xaxis.enter().append('g')
        .attr('class', 'x axis')
        .style('font-size', '0.8rem')
      xaxis.transition()
        .attr('transform', 'translate(0,' + height + ')')
        .attr('opacity', 1)
        .call(xAxis)
        .selectAll('text')
          .attr('y', 10)
          .attr('x', 3)
          .attr('dy', '.35em')
          .attr('transform', 'rotate(15)')
          .style('text-anchor', 'start');
      xaxis.exit().remove();

      // setup the y axis
      var yaxis = graph.selectAll('g.y').data([sData]);
      yaxis.enter().append('g')
        .attr('class', 'y axis')
        .style('font-size', '0.8rem')
      yaxis.transition()
        .attr('opacity', 1)
        .call(yAxis);
      yaxis.exit().remove();

      // style the axis
      graph.selectAll('.axis path')
        .style('fill', 'none')
        .style('stroke', '#152935');
      graph.selectAll('.axis line')
        .style('fill', 'none')
        .style('stroke', '#152935');
      xaxis.selectAll('path')
        .style('stroke', 'none')

      var group = graph.selectAll('.group').data(sData);
      // add new groups
      group.enter().append('g')
        .attr('class', 'group')
        .attr('opacity', 0);
      // update groups
      group.transition()
        .attr('opacity', 1)
        .attr('transform', function(d) { return 'translate(' + xScale(d.key) + ',0)'; });
      // remove old groups
      group.exit().transition()
        .attr('opacity', 0)
        .remove();

      var bars = group.selectAll('rect.bar').data(function(d) { return d.groups; });
      // add new bars
      bars.enter().append('rect')
        .attr('opacity', 0);
      // update bars
      bars.transition()
        .attr('class', function(d, i) { return 'bar bar-'+d.key.replace(/\s+/g, ''); })
        .attr('opacity', 1)
        .attr('width', groupScale.rangeBand())
        .attr('x', function(d) { return groupScale(d.key); })
        .attr('y', function(d) { return d.value ? yScale(d.value) : height; })
        .attr('height', function(d) { return d.value ? height - yScale(d.value) : 0; })
        .style('fill', function(d) { return color(d.key); })

      // remove old bars
      bars.exit().transition()
        .attr('opacity', 0)
        .attr('width', 0)
        .remove();
    });

    // legend key
    var legendkey = svg.selectAll('rect.legend').data(groupKeys);

    // add new keys
    legendkey.enter().append('rect')
      .attr('class', 'legend');

    // update keys
    legendkey
      .style('fill', function(d) { return color(d); })
      .attr('x', width + margin.left + 15)
      .attr('y', function(d, i) { return i*18; })
      .attr('width', 15)
      .attr('height', 15);

    // remove old keys
    legendkey.exit().transition()
      .attr('opacity', 0)
      .remove()

    // legend label
    var legendlabel = svg.selectAll('text.legend').data(groupKeys);

    // add new labels
    legendlabel.enter().append('text')
      .attr('class', 'legend');

    // update labels
    legendlabel
      .text(function(d) { return d; })
      .attr('x', width + margin.left + 35)
      .attr('y', function(d, i) { return (i*18 + 7); })
      .attr('dy', '.35em')
      .on('mouseover', function(d, i) {
        d3.select(this)
          // .style('cursor', 'pointer')
          .style('font-weight', 'bold')
        d3.selectAll('.bar:not(.bar-'+d.replace(/\s+/g, '')+')')
          .attr('opacity', 0);
      })
      .on('mouseout', function(d, i) {
        d3.select(this)
          // .style('cursor', null)
          .style('font-weight', null)
        d3.selectAll('.bar:not(.bar-'+d.replace(/\s+/g, '')+')')
          .attr('opacity', 1);
      });

    // remove old labels
    legendlabel.exit().transition()
      .attr('opacity', 0)
      .remove();
  }
})(window.Pixiedust, window.d3);