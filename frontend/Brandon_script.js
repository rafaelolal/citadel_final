function fetchData(event) {
  event.preventDefault(); // prevent the form from submitting normally

  const ticker = document.querySelector("#ticker").value;
  const startDate = document.querySelector("#start-date").value;
  const endDate = document.querySelector("#end-date").value;

  const url = `http://127.0.0.1:8000/core/max_profit/?ticker=${ticker}&start=${startDate}&end=${endDate}`; // replace with your API URL

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const resultDiv = document.querySelector("#result");
      resultDiv.innerHTML = ""; // clear the div

      const result2Div = document.querySelector("#result2");
      result2Div.innerHTML = "";

      // Create table element
      const table = document.createElement("table");
      table.classList.add("result-table");

      // Create table header
      const headerRow = document.createElement("tr");
      const headers = ["Metric", "Profit", "Buy Date", "Sell Date"];
      headers.forEach((headerText) => {
        const headerCell = document.createElement("th");
        headerCell.textContent = headerText;
        headerRow.appendChild(headerCell);
      });
      table.appendChild(headerRow);

      // Populate table with data
      for (const metric in data) {
        const profit = data[metric][0].toFixed(2);
        const buyDate = data[metric][1];
        const sellDate = data[metric][2];

        const row = document.createElement("tr");
        const cells = [metric, profit, buyDate, sellDate];
        cells.forEach((cellData) => {
          const cell = document.createElement("td");
          cell.textContent = cellData;
          row.appendChild(cell);
        });
        table.appendChild(row);
      }

      // Append table to resultDiv
      resultDiv.appendChild(table);

      // Display the stock graph
      const tradingViewContainer = document.createElement("div");
      tradingViewContainer.classList.add("tradingview-widget-container");
      const tradingViewScript = document.createElement("script");
      tradingViewScript.setAttribute("type", "text/javascript");
      tradingViewScript.setAttribute(
        "src",
        "https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
      );
      tradingViewScript.setAttribute("async", "");
      tradingViewScript.textContent = `
        {
          "width": "100%",
          "height": "610",
          "symbol": "NASDAQ:${ticker}",
          "interval": "D",
          "timezone": "Etc/UTC",
          "theme": "light",
          "style": "1",
          "locale": "en",
          "allow_symbol_change": true,
          "calendar": false,
          "support_host": "https://www.tradingview.com"
        }
      `;
      tradingViewContainer.appendChild(tradingViewScript);
      result2Div.appendChild(tradingViewContainer);
      

      getInsights(
        "You are not allowed to use the '*' character and must respond in paragraphs only. Your response should be brief and make a short argument on why each indicator generated the given profit in comparison to others" +
          JSON.stringify(data)
      );
      populateGallery();

      const modalButton = document.getElementById('modalButton');
      modalButton.removeAttribute('hidden');
  })
  .catch((error) => console.error("Error:", error));
}

function populateGallery() {
  // "p1.jpg", "p2.jpg", "p3.jpg", "p4.jpg", "p5.jpg"
  const imageFileNames = [];
  for (let i = 1; i <= 100; i++) {
    imageFileNames.push(`p${i}.jpg`);
  }

  const galleryDiv = document.querySelector("#gallery");
  galleryDiv.innerHTML = ""; // clear the div

  for (const fileName of imageFileNames) {
    const img = document.createElement("img");
    img.src = `images/${fileName}`;
    img.onerror = function () {
      console.error(`File not found: images/${fileName}`);
      this.remove(); // remove the img element if the file doesn't exist
    };
    galleryDiv.appendChild(img);
  }
}

function getInsights(text) {
  const url = `http://127.0.0.1:8000/core/llm/?text=${text}`;
  const insightsDiv = document.querySelector("#insights");
  insightsDiv.innerHTML = "Fetching results..."; // clear the div
  fetch(url)
    .then((response) => response.json())
    .then((data) => {

      // remove all the * from the string
      data = data.replace("*", "");
      paragraphs = data.split("\n");

      insightsDiv.innerHTML = ""; // clear the div
      paragraphs.forEach((cur) => {
        const p = document.createElement("p");
        p.textContent = cur;
        insightsDiv.appendChild(p);
      });
    });
}
