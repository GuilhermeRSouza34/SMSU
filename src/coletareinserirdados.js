const { inserirDadosPoluicaoAr, inserirDadosQualidadeAgua, inserirDadosRuidoUrbano } = require('./dataCollector');

const { coletarDadosPoluicaoAr, coletarDadosQualidadeAgua, coletarDadosRuidoUrbano } = require('./dataCollectorFunction');

// Função para coletar e inserir dados no banco de dados
async function coletarEInserirDados() {
  // Coletar dados de poluição do ar
  const dadosPoluicaoAr = coletarDadosPoluicaoAr();
  await inserirDadosPoluicaoAr(dadosPoluicaoAr.particulasPM25, dadosPoluicaoAr.particulasPM10, dadosPoluicaoAr.ozonio, dadosPoluicaoAr.dioxidoNitrogenio, dadosPoluicaoAr.dioxidoEnxofre);

  // Coletar dados de qualidade da água
  const dadosQualidadeAgua = coletarDadosQualidadeAgua();
  await inserirDadosQualidadeAgua(dadosQualidadeAgua.ph, dadosQualidadeAgua.cloro, dadosQualidadeAgua.fluor);

  // Coletar dados de ruído urbano
  const dadosRuidoUrbano = coletarDadosRuidoUrbano();
  await inserirDadosRuidoUrbano(dadosRuidoUrbano.nivelDecibeis);

  console.log('Dados coletados e inseridos com sucesso!');
}

// Chamar a função para coletar e inserir dados no banco de dados
coletarEInserirDados();