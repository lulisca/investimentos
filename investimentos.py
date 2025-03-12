def fatorial (num):
    if num ==1:
        return num
    else: 
        return num * fatorial(num-1)
num=10
resultado= fatorial(num)    
print(f"o resultado é {resultado}")


print("_"*60)



def soma(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0]+ soma(lista[1:])
lista=[10,20,30,40]  
resultado= soma(lista)  
print (f"resultado da soma={resultado}")

print("_"*60)

def inverter(palavra):
    if len(palavra)<=1:
        return palavra
    else:
        return palavra[-1]+ inverter(palavra[:-1])
palavra="onibus"    
resultado =inverter(palavra)
print(resultado)
print("_"*60)


def poupanca(montante=0, meses=0, investido=0, marco100k=None):
    rendimento = 0.0005
    while montante < 1000000:
        montante = montante * (1 + rendimento) + 500  
        investido += 500  

        if marco100k is None and montante >= 100000:
            marco100k = (meses + 1, montante, investido)

        meses += 1
        if montante >= 1000000:
            anos = meses // 12  
            meses_finais = meses % 12  
            print(f"Tempo total: {anos} anos e {meses_finais} meses")
            print(f"Total investido: R$ {investido:.2f}")
            print(f"Juros ao atingir R$ 100.000,00: R$ {marco100k[1] - marco100k[2]:.2f}")
            print(f"Juros ao atingir R$ 1.000.000,00: R$ {montante - investido:.2f}")
            break  
poupanca()

print("_"*60)


def investir_bitcoin():
    valor = 0
    btc = 0
    investido = 0
    meses = 0
    marcos = {"100k": None, "1m": None, "1btc": None}
    
    INVESTIMENTO_MENSAL = 250
    
    cotacoes = [
        270000, 280000, 275000, 290000, 300000, 310000,
        305000, 320000, 330000, 340000, 345000, 350000
    ]
    
    while not all(marcos.values()):
        cotacao = cotacoes[meses % 12]  
        
        investido += INVESTIMENTO_MENSAL
        btc += INVESTIMENTO_MENSAL / cotacao 
        
        valor = btc * cotacao
        meses += 1  # Incrementa o mês
        if valor >= 100000 and marcos["100k"] is None:
            marcos["100k"] = {
                "anos": meses // 12,
                "meses": meses % 12,
                "investido": investido,
                "btc": btc,
                "valor": valor
            }
        
        if valor >= 1000000 and marcos["1m"] is None:
            marcos["1m"] = {
                "anos": meses // 12,
                "meses": meses % 12,
                "investido": investido,
                "btc": btc,
                "valor": valor
            }
        
        if btc >= 1 and marcos["1btc"] is None:
            marcos["1btc"] = {
                "anos": meses // 12,
                "meses": meses % 12,
                "investido": investido,
                "btc": btc,
                "valor": valor
            }
    
    return marcos
try:
    resultado = investir_bitcoin()
    
    print(f"\nMarco de R$100.000,00:")
    r = resultado["100k"]
    print(f"Tempo: {r['anos']} anos e {r['meses']} meses")
    print(f"Investido: R${r['investido']:.2f}")
    print(f"Bitcoin: {r['btc']:.8f} BTC ({int(r['btc'] * 100000000)} satoshis)")
    print(f"Valor: R${r['valor']:.2f}")
    
    print(f"\nMarco de R$1.000.000,00:")
    r = resultado["1m"]
    print(f"Tempo: {r['anos']} anos e {r['meses']} meses")
    print(f"Investido: R${r['investido']:.2f}")
    print(f"Bitcoin: {r['btc']:.8f} BTC ({int(r['btc'] * 100000000)} satoshis)")
    print(f"Valor: R${r['valor']:.2f}")
    
    print(f"\nMarco de 1 Bitcoin:")
    r = resultado["1btc"]
    print(f"Tempo: {r['anos']} anos e {r['meses']} meses")
    print(f"Investido: R${r['investido']:.2f}")
    print(f"Bitcoin: {r['btc']:.8f} BTC ({int(r['btc'] * 100000000)} satoshis)")
    print(f"Valor: R${r['valor']:.2f}")
    
except RecursionError:
    print("Erro de recursão. Tente aumentar sys.setrecursionlimit().")

print("_"*60)    

def acoes(montante=0, meses=0, investido=0, dividendos=0, marco100k=None, marco1m=None, max_meses=240):
    investimento_mensal = 80
    rendimento_mensal = 0.01  
    dividendos_mensais = 2  
    cotas = investido / 10  
    
    investido += investimento_mensal
    cotas += investimento_mensal / 10
    dividendos += cotas * dividendos_mensais
    montante = investido + dividendos + (montante * (1 + rendimento_mensal))
    meses += 1
    
    if marco100k is None and montante >= 100000:
        marco100k = (meses // 12, meses % 12, investido, dividendos, montante)
    
    if marco1m is None and montante >= 1000000:
        marco1m = (meses // 12, meses % 12, investido, dividendos, montante)
        
    if marco100k and marco1m:
        print(f"100k: {marco100k[0]} anos e {marco100k[1]} meses, Investido: R${marco100k[2]:.2f}, Div: R${marco100k[3]:.2f}, Total: R${marco100k[4]:.2f}")
        print(f"1M: {marco1m[0]} anos e {marco1m[1]} meses, Investido: R${marco1m[2]:.2f}, Div: R${marco1m[3]:.2f}, Total: R${marco1m[4]:.2f}")
        return
    
    if meses >= max_meses:
        print(f"Terminado após {max_meses} meses.")
        return
    
    acoes(montante, meses, investido, dividendos, marco100k, marco1m, max_meses)
print("AÇÕES")
acoes()
