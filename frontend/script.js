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

      for (const metric in data) {
        const profit = data[metric][0];
        const buyDate = data[metric][1];
        const sellDate = data[metric][2];

        const p = document.createElement("p");
        p.textContent = `Metric: ${metric}, Max Profit: ${profit}, Buy Date: ${buyDate}, Sell Date: ${sellDate}`;
        resultDiv.appendChild(p);
      }
    })
    .catch((error) => console.error("Error:", error));
}
