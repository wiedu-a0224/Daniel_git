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
        selectedValues[0] = ageSelect.value+"歲";
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
        const randomIndex = Math.floor(Math.random() * 60) + 1; // Correctly generate a random index from 1 to 60
        fortuneButton.textContent = randomIndex;
        const img = document.getElementById('fortune-image');
        img.src = `pics/stickpic/${randomIndex}.png`;
        img.alt = `Fortune Stick ${randomIndex}`;
        document.getElementById('overlay').style.display = 'flex';
   
        // Fetch stick poetry data
        fetch('stickPoetry.json')
            .then(response => response.json())
            .then(data => {
                // Ensure the random index matches the array's structure
                const randomData = data[randomIndex - 1];

                // Assign values
                values_1 = randomData['stick_poetry'];
                console.log(values_1);
                values_2 = randomData['stick_9'];
                console.log(values_2);
            })
            .catch(error => {
                console.error('Error fetching stick poetry data:', error);
            });
    });

    document.getElementById('overlay').addEventListener('click', function() {
        this.style.display = 'none';
    });

    document.querySelector('#overlay img').addEventListener('click', function() {
        const query = selectedValues + values_1 + values_2;

        console.log('Sending query:', query); // Log the query being sent
      
        fetch("http://localhost:8000/chain", {
        // fetch("http://metaproot.com:8000/chain", {    
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ query }),
        })
          .then(response => {
            console.log('Received response:', response); // Log the received response
            return response.json();
          })
          .then(data => {
            console.log('Received data:', data); // Log the received data
      
            const textNode = document.createTextNode(JSON.stringify(data));
            const resultDiv = document.getElementById("result");
            resultDiv.textContent = ''; // Clear previous results
            resultDiv.appendChild(textNode);
          })
          .catch(error => {
            console.error("Error:", error);
          });
    });    
});
