
const express = require('express');
const bodyParser = require('body-parser');


const app = express();
app.use(bodyParser.json());

// Raqamlarni qo'shish
app.post('/add', (req, res) => {
  const { num1, num2 } = req.body;
  const result = num1 + num2;
  res.json({ result });
});

// Raqamlar yeg'indisi
app.get('/result', (req, res) => {
  // Bu o'zgartirilishi kerak: result ni serverda saqlash kerak
  // Masalan: let result = 0;
  // So'rovni ishlovchi kodi yozing
  res.json({ result });
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server ishga tushdi: http://localhost:${port}`);
});
