function handleAction(action) {
    let result = document.getElementById("prediction");

    if (action === "BUY") {
        result.innerText = "You selected BUY 📈";
    } 
    else if (action === "SELL") {
        result.innerText = "You selected SELL 📉";
    } 
    else {
        result.innerText = "You selected HOLD ⚖";
    }
}
document.getElementById('searchBtn').addEventListener('click', () => {
    const symbol = document.getElementById('stockInput').value.toUpperCase();
    if(symbol === "") return alert("Please enter a stock symbol!");

    // Replace YOUR_API_KEY with your actual API key
    fetch(`https://finnhub.io/api/v1/quote?symbol=${symbol}&token=YOUR_API_KEY`)
        .then(response => response.json())
        .then(data => {
            if(data.c === undefined) {
                alert("Stock not found!");
            } else {
                displayStockData(symbol, data);
            }
        })
        .catch(err => console.error(err));
});

function displayStockData(symbol, data) {
    const resultDiv = document.getElementById('stockResult');
    resultDiv.innerHTML = `
        <h3>${symbol}</h3>
        <p>Current Price: $${data.c}</p>
        <p>High: $${data.h}</p>
        <p>Low: $${data.l}</p>
        <p>Open: $${data.o}</p>
        <p>Previous Close: $${data.pc}</p>
    `;
}