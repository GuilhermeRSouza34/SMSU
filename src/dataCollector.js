const { Pool } = require('pg');

// Configurações de conexão com o banco de dados PostgreSQL
const pool = new Pool({
  user: 'guilherme',
  host: 'localhost',
  database: 'monitoramento_saude_urbana',
  password: '1234',
  port: 5432,
});

// Função para inserir dados de poluição do ar no banco de dados
async function inserirDadosPoluicaoAr(particulasPM25, particulasPM10, ozonio, dioxidoNitrogenio, dioxidoEnxofre) {
  const query = {
    text: `INSERT INTO poluicao_ar (particulas_pm25, particulas_pm10, ozonio, dioxido_nitrogenio, dioxido_enxofre)
           VALUES ($1, $2, $3, $4, $5)`,
    values: [particulasPM25, particulasPM10, ozonio, dioxidoNitrogenio, dioxidoEnxofre],
  };

  try {
    await pool.query(query);
    console.log('Dados de poluição do ar inseridos com sucesso!');
  } catch (error) {
    console.error('Erro ao inserir dados de poluição do ar:', error);
  }
}

// Função para verificar valores ausentes nas medidas de poluição do ar
function verificarValoresAusentesPoluicaoAr(dadosPoluicaoAr) {
  const valoresAusentes = {};

  for (const [key, value] of Object.entries(dadosPoluicaoAr)) {
    if (value === null || value === undefined || isNaN(value)) {
      valoresAusentes[key] = true;
    }
  }

  return valoresAusentes;
}

// Função para preencher valores ausentes com a média ou mediana dos valores existentes
function preencherValoresAusentesPoluicaoAr(dadosPoluicaoAr) {
  const valoresPreenchidos = { ...dadosPoluicaoAr };
  
  const valoresValidos = Object.values(dadosPoluicaoAr).filter(value => !isNaN(value));
  const media = valoresValidos.reduce((acc, curr) => acc + curr, 0) / valoresValidos.length;
  // Ou, se preferir, use a mediana:
  // const mediana = valoresValidos.sort((a, b) => a - b)[Math.floor(valoresValidos.length / 2)];

  for (const key in valoresPreenchidos) {
    if (isNaN(valoresPreenchidos[key])) {
      valoresPreenchidos[key] = media; // Ou mediana, se preferir
    }
  }

  return valoresPreenchidos;
}

module.exports = {
  inserirDadosPoluicaoAr,
  verificarValoresAusentesPoluicaoAr,
  preencherValoresAusentesPoluicaoAr
};