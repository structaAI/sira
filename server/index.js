import express from 'express';
import dotenv from 'dotenv';
import helmet from 'helmet';
import csurf from 'csurf';
import xss from 'xss-clean';

dotenv.config();

const app = express();
const PORT = process.env.PORT;

app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.use(helmet());
app.use(csurf());
app.use(xss());

app.listen(PORT, () => {
  console.log(`Listening at: http://localhost:${PORT}`)
})