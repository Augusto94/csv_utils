# csv_utils
Biblioteca python que deixa mais amigável a leitura e escrita em arquivos .CSV.

## Utilizando a biblioteca

As principais funcionalidades da biblioteca estão nas funções `csv_to_list` e `list_to_csv`. 

#### csv_to_list(path_file, header=False)
Como o nome sugere, a função `csv_to_list` insere em uma lista python todo o conteúdo de um arquivo csv. Aceita dois argumentos: `path_file` e `header`.
`path_file` refere-se ao caminho local do arquivo que se deseja ler o conteúdo. É um argumento obrigatório no formato de string.
O argumento `header` refere-se ao cabeçalho do arquivo que está sendo lido. É do tipo booleano e por padrão seu valor é False, assumindo o arquivo não possui cabeçalho e é retornada uma lista. Caso o arquivo tenha cabeçalho e o argumento `header` seja passado como True, a função retorna uma `order_dict` onde as keys são os campos do cabeçalho e os values são as demais linhas do arquivo.

**Exemplo de uso da função (Sem cabeçalho):**
```
In [1]: from csv_utils.core import csv_to_list

In [2]: path = 'names_without_header.csv'
In [3]: content = csv_to_list(path)

In [4]: content
Out[4]:
[
 .
 .
 .
 ['Maria', 'Ribeiro'],
 ['Mariano', 'Mascareñas'],
 ['Marisa', 'Sardinha'],
 ['Martim', 'Cysneiros'],
 ['Martim', 'Franco'],
 ['Martim', 'Malafaia'],
 ['Mateus', 'Monte'],
 ['Morgana', 'Ramalho'],
 ['Mário', 'Aldea'],
 ['Napoleão', 'Paiacã'],
 ['Nicolas', 'Rolim'],
 ['Paulina', 'Mendoça'],
 ['Quintino', 'Colaço'],
 ['Quirina', 'Peláez'],
 ['Rafael', 'Homem'],
 .
 .
 .
]
```

**Exemplo de uso da função (Com cabeçalho):**
```
In [1]: from csv_utils.core import csv_to_list

In [2]: path = 'names_with_header.csv'
In [3]: content = csv_to_list(path, True)

In [4]: content
Out[4]:
[
 .
 .
 .
 OrderedDict([('nome', 'Maria'), ('sobrenome', 'Ribeiro')]),
 OrderedDict([('nome', 'Mariano'), ('sobrenome', 'Mascareñas')]),
 OrderedDict([('nome', 'Marisa'), ('sobrenome', 'Sardinha')]),
 OrderedDict([('nome', 'Martim'), ('sobrenome', 'Cysneiros')]),
 OrderedDict([('nome', 'Martim'), ('sobrenome', 'Franco')]),
 OrderedDict([('nome', 'Martim'), ('sobrenome', 'Malafaia')]),
 OrderedDict([('nome', 'Mateus'), ('sobrenome', 'Monte')]),
 OrderedDict([('nome', 'Morgana'), ('sobrenome', 'Ramalho')]),
 OrderedDict([('nome', 'Mário'), ('sobrenome', 'Aldea')]),
 OrderedDict([('nome', 'Napoleão'), ('sobrenome', 'Paiacã')]),
 OrderedDict([('nome', 'Nicolas'), ('sobrenome', 'Rolim')]),
 OrderedDict([('nome', 'Paulina'), ('sobrenome', 'Mendoça')]),
 OrderedDict([('nome', 'Quintino'), ('sobrenome', 'Colaço')]),
 OrderedDict([('nome', 'Quirina'), ('sobrenome', 'Peláez')]),
 OrderedDict([('nome', 'Rafael'), ('sobrenome', 'Homem')]),
 .
 .
 .
]
```

***Atenção:*** Só utilize o argumento `header` como True se tiver certeza que o arquivo esta estruturado em formato de tabela e todas as linhas possuem a mesma quantidade de valores que o cabeçalho.
