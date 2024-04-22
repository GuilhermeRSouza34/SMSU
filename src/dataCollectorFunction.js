// Função para simular a coleta de dados de poluição do ar
function coletarDadosPoluicaoAr() {
    // Simulação de valores de amostra para os dados de poluição do ar
    const dados = {
      particulasPM25: Math.random() * 100,
      particulasPM10: Math.random() * 100,
      ozonio: Math.random() * 100,
      dioxidoNitrogenio: Math.random() * 100,
      dioxidoEnxofre: Math.random() * 100,
    };
  
    return dados;
  }
  
  // Função para simular a coleta de dados de qualidade da água
  function coletarDadosQualidadeAgua() {
    // Simulação de valores de amostra para os dados de qualidade da água
    const dados = {
      ph: Math.random() * 14,
      cloro: Math.random() * 5,
      fluor: Math.random() * 2,
    };
  
    return dados;
  }
  
  // Função para simular a coleta de dados de ruído urbano
  function coletarDadosRuidoUrbano() {
    // Simulação de valores de amostra para os dados de ruído urbano
    const dados = {
      nivelDecibeis: Math.random() * 120,
    };
  
    return dados;
  }
  
  module.exports = {
    coletarDadosPoluicaoAr,
    coletarDadosQualidadeAgua,
    coletarDadosRuidoUrbano,
  };