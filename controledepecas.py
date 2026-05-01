pecas = []
caixas = []
caixa_atual = []


def validar_peca(peso, cor, comprimento):
    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão")
    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão")
    if len(motivos) == 0:
        return True, "Aprovada"
    else:
        return False, ", ".join(motivos)


def cadastrar_peca():
    try:
        id_peca = input("ID da peça: ")
        for p in pecas:
            if p["id"] == id_peca:
                print("Erro: já existe uma peça com esse ID.")
                return
        peso = float(input("Peso (g): "))
        cor = input("Cor: ")
        comprimento = float(input("Comprimento (cm): "))
        aprovada, motivo = validar_peca(peso, cor, comprimento)
        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "status": "Aprovada" if aprovada else "Reprovada",
            "motivo": motivo
        }
        pecas.append(peca)
        if aprovada:
            caixa_atual.append(peca)
            if len(caixa_atual) == 10:
                caixas.append(caixa_atual.copy())
                caixa_atual.clear()
                print("📦 Caixa fechada com 10 peças!")
        print(f"Peça {peca['status']}!")
    except ValueError:
        print("Erro: peso e comprimento devem ser números.")


def listar_pecas():
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return
    for p in pecas:
        print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | "
              f"Comprimento: {p['comprimento']}cm | Status: {p['status']}")


def remover_peca():
    id_remover = input("Digite o ID da peça para remover: ")
    for p in pecas:
        if p["id"] == id_remover:
            if p["status"] == "Aprovada":
                if p in caixa_atual:
                    caixa_atual.remove(p)
                else:
                    print(
                        "Aviso: peça já está em uma caixa fechada e não pode ser removida da caixa.")
            pecas.remove(p)
            print("Peça removida.")
            return
    print("Peça não encontrada.")


def listar_caixas():
    if not caixas and not caixa_atual:
        print("Nenhuma caixa utilizada ainda.")
        return
    for i, caixa in enumerate(caixas, start=1):
        print(f"Caixa {i} (fechada): {len(caixa)} peças")
    if caixa_atual:
        print(f"Caixa {len(caixas) + 1} (em aberto): {len(caixa_atual)} peças")


def relatorio():
    aprovadas = [p for p in pecas if p["status"] == "Aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "Reprovada"]
    total_caixas = len(caixas) + (1 if caixa_atual else 0)

    print("\n📊 RELATÓRIO FINAL")
    print(f"Total de peças aprovadas: {len(aprovadas)}")
    print(f"Total de peças reprovadas: {len(reprovadas)}")

    if reprovadas:
        print("\nMotivos de reprovação:")
        for p in reprovadas:
            print(f"  ID {p['id']}: {p['motivo']}")

    print(f"\nCaixas utilizadas: {total_caixas}")


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar nova peça")
        print("2. Listar peças")
        print("3. Remover peça")
        print("4. Listar caixas")
        print("5. Gerar relatório")
        print("0. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            relatorio()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


menu()