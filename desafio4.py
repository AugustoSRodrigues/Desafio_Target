
def percentual_representacao(faturamento):
   soma = sum(faturamento.values())
   d = 0
   for i in faturamento.keys():
       prc = (faturamento[i]/soma)*100
       d+=prc
       print(f'{i}:{prc:.2f}%')


def main():
    faturamento = {'SP':67836.43,'RJ':36678.66,'MG':29229.88,"ES":27165.48,'Outros':19849.53}
    percentual_representacao(faturamento)

if __name__=='__main__':
    main()