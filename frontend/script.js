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

      populateGallery();
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
