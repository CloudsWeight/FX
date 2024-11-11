const express = require('express');
const path = require('path');
const { spawn } = require('child_process');
const app = express();
const PORT = 43451;

app.use(express.json()); // Parse JSON bodies

// Start the server
app.listen(PORT, (error) => {
  if (!error) console.log('Listening on port', PORT);
  else console.log('Error Found in Application:', error);
});

// In-memory storage for data intake
const data = [];

// POST endpoint to add new data to the 'data' array
app.post('/intake', (req, res) => {
  const newItem = req.body;
  data.length = 0;
  data.push(newItem);
  console.log(`Received data: ${req.body}`); // Use backticks if you need template literals
  res.status(201).json(newItem); // Use `res.status`, not `req.status`
});

// GET endpoint to retrieve the stored data
app.get('/data', (req, res) => {
  res.json(data);
});

// Static assets folder
app.use("/assets", express.static(__dirname + "/assets"));

// Serve specific files
app.get("/assets/get_waves.js", (req, res) => {
  res.sendFile(path.join(__dirname, '/assets/get_waves.js'));
});

app.get("/assets/test", (req, res) => {
  res.sendFile(path.join(__dirname, '/assets/test.html'));
});

// Endpoint to interact with Python script for rates
app.get('/api/getRates', (req, res) => {
  const pyProc = spawn('python', ['./assets/OandaFile.py']);
  pyProc.stdout.on('data', (data) => {
  	
    console.log(data.toString());
    res.json(data.toString());
  });
  pyProc.stderr.on('data', (data) => {
    console.error(data.toString());
    res.status(500).json(data.toString());
  });
  pyProc.on('close', () => {
    console.log('Python script closed');
  });
});

// Endpoint to interact with Python script for news
app.get('/api/getNews', (req, res) => {
  const pyProc = spawn('python', ['./assets/get_news.py']);
  pyProc.stdout.on('data', (data) => {
    console.log(data.toString());
    // Uncomment to send data in response if needed
    // res.json(data.toString());
  });
  pyProc.stderr.on('data', (data) => {
    console.error(data.toString());
    res.status(500).json(data.toString());
  });
  pyProc.on('close', () => {
    console.log('Python script closed');
  });
});

// Root route to serve index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/assets/index.html'));
});

// Serve favicon
app.get('/favicon.ico', (req, res) => {
  res.sendFile(path.join(__dirname, '/assets/favicon.ico'));
});

