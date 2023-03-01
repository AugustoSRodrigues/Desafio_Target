import pandas as pd

def main():
    df = pd.read_json('data/dados.json').set_index('dia')
    df_limpo = df[df.valor!=0]
    
    print()
    print(f'Maior valor:R${df.loc[df.valor.idxmax()].valor}')
    print(f'Menor valor:R${df.loc[df.valor.idxmin()].valor}')
    print()
    print(f"Faturmaneto médio:R${df_limpo.valor.mean():.2f}")
    faturamento_supeior = df_limpo[df_limpo.valor>=df_limpo.valor.mean()]
    print(f'Quantidade de dias com faturamento superior à média: {faturamento_supeior.shape[0]}')
    print(faturamento_supeior)

if __name__ == '__main__':
    main()