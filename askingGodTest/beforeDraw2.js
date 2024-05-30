let values_1;
let values_2;
document.addEventListener('DOMContentLoaded', function() {

    const ageSelect = document.getElementById('age');
    for (let i = 0; i <= 120; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        ageSelect.appendChild(option);
    }

    const selectedValues = [];
    const selectedValuesDiv = document.getElementById('selected-values');

    const updateSelectedValues = () => {
        selectedValuesDiv.textContent = selectedValues.join(', ');
    };

    const ageSelectHandler = () => {
        selectedValues[0] = ageSelect.value;
        updateSelectedValues();
    };

    const genderSelectHandler = () => {
        selectedValues[1] = document.getElementById('gender').value;
        updateSelectedValues();
    };

    const maritalStatusSelectHandler = () => {
        selectedValues[2] = document.getElementById('marital-status').value;
        updateSelectedValues();
    };

    ageSelect.addEventListener('change', ageSelectHandler);
    document.getElementById('gender').addEventListener('change', genderSelectHandler);
    document.getElementById('marital-status').addEventListener('change', maritalStatusSelectHandler);

    const buttons = document.querySelectorAll('.grid-button');
    buttons.forEach((button, index) => {
        button.addEventListener('click', function() {
            buttons.forEach(btn => btn.style.backgroundColor = '#f07070');
            this.style.backgroundColor = '#c71313';
            selectedValues[3] = this.textContent;
            updateSelectedValues();
        });
    });
    
    const fortuneButton = document.querySelector('.fortune-button');
    
    fortuneButton.addEventListener('click', function() {
        
        const randomIndex = Math.floor(Math.random() * 5) + 1;
        fortuneButton.textContent = randomIndex;
        const img = document.getElementById('fortune-image');
        img.src = `pics/stickpic5/${randomIndex}.png`;
        img.alt = `Fortune Stick ${randomIndex}`;
        document.getElementById('overlay').style.display = 'flex';
   
        // 取得籤詩資料
        fetch('stickPoetry.json')
            .then(response => response.json())
            .then(data => {

            // Get a random key from the JSON data
            // const randomIndex = Math.floor(Math.random() * data.length);
                const randomData = data[randomIndex];

            // Print the corresponding value 
                values_1 = randomData['stick_poetry'];
                console.log(values_1);
                values_2 = randomData['stick_9'];
                console.log(values_2);
            });
    });
    document.getElementById('overlay').addEventListener('click', function() {
        this.style.display = 'none';
    });
    document.querySelector('#overlay img').addEventListener('click', function() {
        const query = values_1;
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
    
              
});