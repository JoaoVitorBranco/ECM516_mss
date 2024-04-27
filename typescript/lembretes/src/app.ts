import express from 'express'
import axios from 'axios'
const app = express()
app.use(express.json())

/*
  {
    "1": {
      "id": "1",
      "texto": "Fazer café"
    },
    "2": {
      "id": "2",
      "texto": "Natação"
    }
  }
*/

interface Lembrete{
  id: string;
  texto: string;
}
let id: string = "1";
const lembretes: Record<string, Lembrete> = {
  
}

app.get('/lembretes', (req, res) => {
  res.json(lembretes)
})

app.post('/lembretes', (req, res) => {
  const { texto } = req.body
  console.log(texto)
  const lembrete: Lembrete = {
    id: id,
    texto: texto
  }
  lembretes[id] = lembrete
  id = (+id + 1).toString()
  res.json(lembrete)
})

const PORT: number = 4000
app.listen(PORT, () => console.log(`Lembretes. Porta ${PORT}.`))