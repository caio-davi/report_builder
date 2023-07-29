import os, xmltodict, json
import pandas as pd

FOLDER = "/root/Workspace/report_builder/Faturamento_maio/Faturamento-04.05.2023/XML/"

receipts = []

lines = []
col = ["ID","Operacao","Emissao","CNPJ","Cliente","MWh","Unidade","Total"]

for root, dirs, files in os.walk(FOLDER, topdown=False):
  for name in files:
    with open(os.path.join(root, name), 'r') as f:
      receipt = xmltodict.parse(f.read())
      line = []
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["@Id"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["ide"]["natOp"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["ide"]["dhEmi"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["dest"]["CNPJ"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["dest"]["xNome"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["det"]["prod"]["qCom"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["det"]["prod"]["vUnCom"])
      line.append(receipt["nfeProc"]["NFe"]["infNFe"]["total"]["ICMSTot"]["vNF"])
      lines.append(line)

df = pd.DataFrame(lines,columns=col)
df.to_csv("Faturadas-04.05.2023-OB1.csv")