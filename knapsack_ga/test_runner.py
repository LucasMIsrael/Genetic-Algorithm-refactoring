import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from utils import gerar_instancia
from genetic_algorithm import algoritmo_genetico
import time

def testar_algoritmo_genetico(tamanhos, num_geracoes=100):
    resultados = []
    for tam in tamanhos:
        pesos, valores, capacidade = gerar_instancia(tam)
        inicio = time.time()
        resultado = algoritmo_genetico(pesos, valores, capacidade, tam_pop=50, num_geracoes=num_geracoes)
        fim = time.time()
        
        # Organizando os dados
        resultado["num_itens"] = tam
        resultado["valor_total"] = resultado["valor_total"]
        resultado["peso_total"] = resultado["peso_total"]
        resultado["tempo_execucao_seg"] = round(fim - inicio, 3)
        resultado["geracoes"] = num_geracoes  # Pode ser alterado conforme a variável num_geracoes
        
        # Adiciona o resultado à lista
        resultados.append(resultado)
    return resultados

def salvar_resultados_excel(resultados, filename="results/benchmarks.xlsx"):
    """
    Salva os resultados em um arquivo Excel com melhor formatação visual.
    """
    # Criando um novo workbook e uma planilha
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Resultados"

    # Definindo os títulos das colunas
    fieldnames = [
        "Número de Itens", "Valor Total", "Peso Total", "Tempo de Execução (segundos)", "Número de Gerações"
    ]

    # Adicionando os títulos das colunas na primeira linha
    for col_num, header in enumerate(fieldnames, 1):
        cell = sheet.cell(row=1, column=col_num)
        cell.value = header
        # Aplicando formatação (negrito, centralizado)
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center', vertical='center')

    # Adicionando os dados na planilha
    for row_num, resultado in enumerate(resultados, 2):
        sheet.cell(row=row_num, column=1, value=resultado["num_itens"])
        sheet.cell(row=row_num, column=2, value=resultado["valor_total"])
        sheet.cell(row=row_num, column=3, value=resultado["peso_total"])
        sheet.cell(row=row_num, column=4, value=resultado["tempo_execucao_seg"])
        sheet.cell(row=row_num, column=5, value=resultado["geracoes"])

    # Ajustar a largura das colunas
    for col_num in range(1, len(fieldnames) + 1):
        max_length = 0
        column = openpyxl.utils.get_column_letter(col_num)
        for row in sheet.iter_rows(min_col=col_num, max_col=col_num):
            for cell in row:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column].width = adjusted_width

    # Adicionando bordas nas células
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    for row in sheet.iter_rows(min_row=1, max_row=len(resultados) + 1, min_col=1, max_col=len(fieldnames)):
        for cell in row:
            cell.border = border

    # Salvando o arquivo Excel
    wb.save(filename)

if __name__ == "__main__":
    tamanhos_teste = [5, 10, 1000, 10000]
    resultados = testar_algoritmo_genetico(tamanhos_teste)
    for r in resultados:
        print(r)
    
    # Salvar os resultados em Excel
    salvar_resultados_excel(resultados)
