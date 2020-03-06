var tds = document.getElementById('countit').getElementsByTagName('td');
  var sum = 0;
  for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'count-me') {
      sum += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    sm = sum.toFixed(2);
  }
  document.getElementById('countit').innerHTML += '<tr><th>Total - ' + sm + " €" + '</th></tr>';