def main():
    import pandas as pd
    import json

    # abrindo o arquivo json do ecommerce
    with open(r'ecommerce.json') as json_file:
        data = json.load(json_file)

    # criando o dataframe com os dados desejados do ecommerce
    hits = data['hits']['hits']
    hits_list = []

    for hit in hits:
        hit_data = hit['_source']
        hits_list.append(hit_data)

    df_ecommerce = pd.DataFrame(hits_list)

    # criando o dataframe de regras baseado no arquivo rules.txt
    columns = ['id_rule',
               'nm_rule',
               'ds_rule',
               'ds_rule_aux']
    
    df_rules = pd.read_csv(r'rules.txt',
                           skiprows=1,
                           index_col=False,
                           names=columns)

    # unindo os dados da coluna ds_rule que foram separados pela vírgula
    df_rules['ds_rule'] = df_rules['ds_rule']+','+df_rules['ds_rule_aux']

    # tratando as cláusulas do campo ds_rule para realização da query
    df_rules['ds_rule'] = df_rules['ds_rule'].str.replace('in',' in ').str.replace('not',' not').str.replace('&',' and ')
    df_rules['ds_rule'] = df_rules['ds_rule'].str.replace('`','').str.replace("'",'"')

    # excluindo a coluna auxiliar usada na importação do dataframe
    df_rules.drop('ds_rule_aux',
                  axis=1,
                  inplace=True)

    # adicionando as colunas do dataframe de regras ao dataframe de ecommerce
    for _, rule in df_rules.iterrows():
        rule_condition = rule['ds_rule']
        rule_id = rule['id_rule']
        rule_name = rule['nm_rule']
        filtered_df_ecommerce = df_ecommerce.query(rule_condition)
        filtered_df_ecommerce['id_rule'] = rule_id
        filtered_df_ecommerce['nm_rule'] = rule_name
        if rule_id == 1:
            result_df = filtered_df_ecommerce
        else:
            result_df = pd.concat([result_df, filtered_df_ecommerce])

    # criando o dataframe final apenas com as colunas desejadas
    df = result_df[['order_date',
                    'order_id',
                    'id_rule',
                    'nm_rule']].sort_index()

    # exportando o dataframe final para .csv
    df.to_csv('ecommerce_with_rules', 
              sep=',',
              index=False)

main()