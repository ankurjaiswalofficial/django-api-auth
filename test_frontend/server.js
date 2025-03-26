const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 4000;

// CORS for API calls to external hosts
// app.use(cors());

// Serve static HTML
app.use(express.static(path.join(__dirname, 'public')));

app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
