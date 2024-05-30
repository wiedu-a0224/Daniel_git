// 點及最上層的圖片後後會執行main.js的function
// document.querySelector('#overlay img').addEventListener('click', function() {
//     // 送去後端的文字
//     // const query = "龍虎相隨在深山，君爾何須背後看，不知此去相愛愉，他日與我卻無干"; // replace with your actual query
//     const query = value_1; // replace with your actual query
//     fetch("http://localhost:8000/chain", {
//       // replace with your actual server URL
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ query }),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         // Assuming the data is a string or can be converted to a string
//         const textNode = document.createTextNode(data);

//         // Assuming you have a div with id 'result' in your HTML
//         // <div id="result"></div>
//         const resultDiv = document.getElementById("result");
//         resultDiv.appendChild(textNode);
//       })
//       .catch((error) => {
//         console.error("Error:", error);
//       });
// });
document.querySelector('#overlay img').addEventListener('click', function() {
  const query = value_1;
  console.log('Sending query:', query); // Log the query being sent

  fetch("http://localhost:8000/chain", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  })
    .then((response) => {
      console.log('Received response:', response); // Log the received response
      return response.json();
    })
    .then((data) => {
      console.log('Received data:', data); // Log the received data

      const textNode = document.createTextNode(data);
      const resultDiv = document.getElementById("result");
      resultDiv.appendChild(textNode);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});