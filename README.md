# Ecommerce Merge
## O problema

- Cenário: Um ecommerce armazena suas vendas em um banco de dados chave-valor, deste banco foi extraído um arquivo JSON `ecommerce.json` com uma amostra das vendas. Será necessário classificar as vendas de acordo com as regras armazenadas em um outro arquivo denominado `rules.txt`. O resultado esperado é a criação de um novo arquivo csv contendo 4 campos separados por vírgula: `order_date`, `order_id`, `id_rule`, `nm_rule`. Sendo que os campos `order_date` e `order id` são do arquivo JSON e os campos `id_rule` e `nm_rule` são do arquivo txt.

- Desafio: entender a estrutura do JSON, criar um script python para aplicar dinamicamente as regras contidas no campo `ds_rule` no arquivo `rules.txt` e retornar um novo arquivo `.csv` contendo os campos necessários, conforme exemplo amostral abaixo:

  | order_date |  order_id |  id_rule |  nm_rule |
  | :---: | :---: | :---: | :---: |
  | 2023-03-18T14:13:55+00:00 | 563365 | 3 | women_weekend |
  | 2023-03-21T05:26:53+00:00 | 566979 | 4 | women_week |
  | 2023-03-12T14:26:53+00:00 | 555248 | 1 | men_weekend |
  | 2023-03-17T04:13:26+00:00 | 561472 | 2 | men_week |

## Orientações

- Realizar a instalação das dependências através do comando `pip install -r requirements.txt`.

- O script `main.py` realiza toda a transformação necessária para criação do arquivo final. A análise exploratória para desenvolvimento do script pode ser visualizada através do notebook `ecommerce_merge_eda.ipynb`.

- O resultado final da transformação dos dados está armazenado no arquivo `ecommerce_dataframe_with_rules.csv`.
