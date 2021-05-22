import express from 'express';

const routes = require('./routes/index');

const app = express();
const hostname = '127.0.0.1';
const port = 1245;

app.use('/', routes);
app.use('/students', routes);
app.use('/students/:major', routes);

app.listen(port, () => {
  console.log(`Example app listening at http://${hostname}:${port}`);
});

export default app;
