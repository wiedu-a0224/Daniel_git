// 送去後端的文字
const query = "your query here"; // replace with your actual query

fetch("http://localhost:8000/chain", {
  // replace with your actual server URL
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ query }),
})
  .then((response) => response.json())
  .then((data) => {
    // Assuming the data is a string or can be converted to a string
    const textNode = document.createTextNode(data);

    // Assuming you have a div with id 'result' in your HTML
    // <div id="result"></div>
    const resultDiv = document.getElementById("result");
    resultDiv.appendChild(textNode);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
