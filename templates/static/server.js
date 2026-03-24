const express = require('express');
const app = express();

// API route
app.get('/api/predict', (req, res) => {
    res.json({
        prediction: "BUY",
        confidence: "89%"
    });
});

// Start server
app.listen(3000, () => {
    console.log("Server running on port 3000");
});