document.getElementById('rec-form').addEventListener('submit', function(ev) {
    ev.preventDefault();
    const formData = new FormData(ev.target);
    fetch('/recommend', { method: 'POST', body: formData })
        .then(resp => resp.json())
        .then(data => drawChart(data));
});

function drawChart(data) {
    d3.select('#chart').selectAll('*').remove();
    const width = 500;
    const height = 300;
    const margin = {top: 20, right: 20, bottom: 30, left: 40};

    const svg = d3.select('#chart').append('svg')
        .attr('width', width)
        .attr('height', height);

    const x = d3.scaleBand()
        .domain(data.map(d => d.product_id))
        .range([margin.left, width - margin.right])
        .padding(0.1);

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.rating)])
        .range([height - margin.bottom, margin.top]);

    svg.append('g')
        .attr('fill', 'steelblue')
      .selectAll('rect')
      .data(data)
      .join('rect')
        .attr('x', d => x(d.product_id))
        .attr('y', d => y(d.rating))
        .attr('height', d => y(0) - y(d.rating))
        .attr('width', x.bandwidth());

    svg.append('g')
        .attr('transform', `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x));

    svg.append('g')
        .attr('transform', `translate(${margin.left},0)`)
        .call(d3.axisLeft(y));
}
