from scipy import stats

def teste_normal_hipotese(dados):
    alpha = float(input("Digite o valor de alpha que será usado neste teste de normalidade, um número entre 0 e 1: "))

    stat, p = stats.normaltest(dados)
    media = (sum(dados) / len(dados))
    curtose = (stats.scoreatpercentile(dados, 75) - stats.scoreatpercentile(dados, 25)) / (2 * (stats.scoreatpercentile(dados, 90)-stats.scoreatpercentile(dados, 10)))
    
    print(f"A quantidade de dados da amostra é: {len(dados)}")
    print(f"A média aritmética dos dados é: {media}")
    print(f"A mediana dos dados é: {stats.scoreatpercentile(dados, 50)}")
    print(f"O menor valor da amostra é: {min(dados)}")
    print(f"O menor valor da amostra é: {max(dados)}")
    print(f"O desvio padrão é : {stats.tstd(dados)}")
    print(f"A variância é: {stats.tvar(dados)}")
    print(f"O primeiro quartil é: {stats.scoreatpercentile(dados, 25)}")
    print(f"O segundo quartil é: {stats.scoreatpercentile(dados, 50)}")
    print(f"O terceiro quartil é: {stats.scoreatpercentile(dados, 75)}")
    print(f"O quarto quartil é: {stats.scoreatpercentile(dados, 100)}")
    print(f"A curtose do gráfico dos dados é: {curtose}")
    print(f"O erro padrão é: {stats.sem(dados)}")
    print(f"O P valor é: {p}")
    print(f"O indicador de normalidade é: {stat}")

    if p <= alpha:
        print(f"O P-valor é ({p}) e ele é menor que alpha({alpha}), então a amostra não segue uma distribuição normal.")
    else:
        print(f"O P-valor é ({p}) e ele é maior que alpha({alpha}), então a amostra segue uma distribuição normal.")

def teste_t_hipotese(dados, media_populacional):
    alpha = float(input("Digite o valor de alpha que será usado neste teste T, um número entre 0 e 1: "))

    stat, p = stats.ttest_1samp(dados, media_populacional)

    if p <= alpha:
        print(f"O P-valor é ({p}) e ele é menor que alpha({alpha}), então rejeitamos a hipótese nula (H0). A média da amostra é significativamente diferente da média da população.")
    else:
        print(f"O P-valor é ({p}) e ele é maior que alpha({alpha}), então não podemos rejeitar a hipótese nula (H0). Não há evidências suficientes para concluir que a média da amostra é significamente diferente da média da população.")    


with open('MEMORY.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

amostra = []
for linha in linhas:
    numero = float(linha.strip().replace(',', '.'))
    amostra.append(numero)

print("As informações sobre a amostra são:")
teste_normal_hipotese(amostra)

hipotese_media = float(input("Digite a hipótese da média populacional: "))
teste_t_hipotese(amostra, hipotese_media)