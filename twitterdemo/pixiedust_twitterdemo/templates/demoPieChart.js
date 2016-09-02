window.Pixiedust = window.Pixiedust || {};
window.Pixiedust.twitterdemo = window.Pixiedust.twitterdemo || {};

(function(pix, d3) {
  var percent = d3.format('.0%');
  var color = d3.scale.category10();
  var tooltipselection = d3.select('body')
    .selectAll('.twitter-demo-tooltip')
    .data(['twitter-demo-tooltip']);
  tooltipselection
    .enter()
    .append('div')
    .attr('class', 'twitter-demo-tooltip')
    .style('background-color', 'rgba(21, 41, 53, 0.9)')
    .style('color', '#ffffff')
    .style('font-family', 'HelvNeue,Helvetica,sans-serif')
    .style('font-size', '0.75rem')
    .style('font-weight', '300')
    .style('max-width', '300px')
    .style('padding', '8px')
    .style('position', 'absolute')
    .style('visibility', 'hidden')
    .style('z-index', '100')
    .text('twitter-demo-tooltip')

  pix.twitterdemo.piechart = function(selector, chartdata) {
    var data = (chartdata || []).map(function(d) {
      return {
        key: d[0],
        value: d[1]
      }
    });
    var keys = data.map(function(d) { return d.key });

    data = data.sort(function(a, b) {
      return a.key > b.key ? 1 : (a.key < b.key ? -1 : 0);
    });

    var selection = d3.select(selector);
    var box = selection.node().getBoundingClientRect();
    var width = box.width-10;
    var height = box.height-10;
    var outerRadius = Math.min(height, width) / 2 - 5;
    var innerRadius = outerRadius / 4; //: 1;
    var cornerRadius = 10;

    var arc = d3.svg.arc();
    var pie = d3.layout.pie()
      .padAngle(.005)
      .value(function(d) { return d.value })
      .sort(null);

    color.domain(keys);

    arc.padRadius(outerRadius)
      .innerRadius(innerRadius);

    function arcExplode(outerRadius, delay) {
      d3.select(this).transition().delay(delay).attrTween('d', function(d) {
        var i = d3.interpolate(d.outerRadius, outerRadius);
        return function(t) { d.outerRadius = i(t); return arc(d); };
      });
    }

    function arcResize(a) {
      var i = d3.interpolate(this._current, a);
      this._current = i(0);
      return function(t) {
        return arc(i(t));
      };
    }

    // setup the svg element
    var svg = selection.selectAll('svg').data([data]);
    svg.enter().append('svg');
    svg.attr('width', width)
      .attr('height', height);

    var graph = svg.selectAll('g').data([data]);
    graph.enter().append('g')
    graph.attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');

    // pie chart arcs
    var arcs = graph.selectAll('path').data(pie);

    // add new arcs
    arcs.enter().append('path')
      .each(function(d) {
        d.outerRadius = outerRadius - 5;
        this._current = d;
      })
      .attr('d', arc);

    // update arcs
    arcs.transition().attrTween('d', arcResize)
      .each('end', function(d) {
        d.outerRadius = outerRadius - 5;
        this._current = d;
        d3.select(this)
          .attr('fill', function(d, i) {
            return color(d.data.key);
          })
          // .on('mouseover', function(d, i) {
          //   tooltipselection
          //     .text(function(d) {
          //       return d.key + ': ' + percent(d.value);
          //     })
          //     .style('visibility', 'visible');
          //   arcExplode.call(this, outerRadius, 0);
          // })
          // .on('mousemove', function(d) {
          //   tooltipselection
          //     .style('top', (d3.event.pageY-10)+'px')
          //     .style('left',(d3.event.pageX+10)+'px');
          // })
          // .on('mouseout', function(d, i) {
          //   tooltipselection.style('visibility', 'hidden');
          //   arcExplode.call(this, outerRadius - 5, 150);
          // });
      });

    // remove old arcs
    arcs.exit().transition()
      .style('opacity', 0)
      .remove();

    // legend key
    var legendkey = svg.selectAll('rect.legend').data(keys);

    // add new keys
    legendkey.enter().append('rect')
      .attr('class', 'legend')
      // .attr('opacity', 0)
      .attr('x', 0)
      .attr('y', function(d, i) { return i*20; })
      .attr('width', 18)
      .attr('height', 18);

    // update keys
    legendkey.transition()
      .style('fill', function(d) { return color(d); });

    // remove old keys
    legendkey.exit().transition()
      .attr('opacity', 0)
      .remove()

    // legend label
    var total = d3.sum(data, function(d) { return d.value });
    var legendlabel = svg.selectAll('text.legend').data(keys);

    // add new labels
    legendlabel.enter().append('text')
      .attr('class', 'legend')
      .attr('x', 24)
      .attr('y', function(d, i) { return (i*20 + 9); })
      .attr('dy', '.35em');

    // update labels
    legendlabel.transition()
      .text(function(d) {
        var current = data.filter(function(_d) { return _d.key === d; });
        var v = current.length > 0 ? current[0].value : 0;
        return d + ': ' + percent(v / total); });

    // remove old labels
    legendlabel.exit().transition()
      .attr('opacity', 0)
      .remove();
  }
})(window.Pixiedust, window.d3);