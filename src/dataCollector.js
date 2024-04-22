const { Pool } = require('pg');

// Configurações de conexão com o banco de dados PostgreSQL
const pool = new Pool({
  user: 'seu_usuario',
  host: 'localhost',
  database: 'monitoramento_saude_urbana',
  password: 'sua_senha',
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

// Função para inserir dados de qualidade da água no banco de dados
async function inserirDadosQualidadeAgua(ph, cloro, fluor) {
  const query = {
    text: `INSERT INTO qualidade_agua (ph, cloro, fluor)
           VALUES ($1, $2, $3)`,
    values: [ph, cloro, fluor],
  };

  try {
    await pool.query(query);
    console.log('Dados de qualidade da água inseridos com sucesso!');
  } catch (error) {
    console.error('Erro ao inserir dados de qualidade da água:', error);
  }
}

// Função para inserir dados de ruído urbano no banco de dados
async function inserirDadosRuidoUrbano(nivelDecibeis) {
  const query = {
    text: `INSERT INTO ruido_urbano (nivel_decibeis)
           VALUES ($1)`,
    values: [nivelDecibeis],
  };

  try {
    await pool.query(query);
    console.log('Dados de ruído urbano inseridos com sucesso!');
  } catch (error) {
    console.error('Erro ao inserir dados de ruído urbano:', error);
  }
}

module.exports = {
  inserirDadosPoluicaoAr,
  inserirDadosQualidadeAgua,
  inserirDadosRuidoUrbano,
};