import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def draw_chart(dataset, polygons, types):
    Y = {'В целевой структуре парка': [], 'Прочие': [], 'Проверить данное ТС': []}
    X = dataset[polygons].unique()
    for poly in X:
        dictionary = (dataset.loc[dataset[polygons] == poly, types].value_counts())
        for key in Y.keys():
            Y[key].append(dictionary.loc[key])

    result = pd.DataFrame(data=X)
    for key in Y.keys():
        result[key] = Y[key]
    result = result.rename(columns={0: polygons})
    result.plot(x=polygons, kind='bar', stacked=True)
    plt.legend(bbox_to_anchor=(1, 0.6))
    plt.show()


def draw_single_chart(dataset, polygons, name, types):
    dataset = dataset[dataset[polygons] == name]
    Y = {'В целевой структуре парка': [], 'Прочие': [], 'Проверить данное ТС': []}
    X = dataset[polygons].unique()
    for poly in X:
        dictionary = (dataset.loc[dataset[polygons] == poly, types].value_counts())
        for key in Y.keys():
            Y[key].append(dictionary.loc[key])

    result = pd.DataFrame(data=X)
    for key in Y.keys():
        result[key] = Y[key]
    result = result.rename(columns={0: polygons})

    total = sum(result[Y.keys()].values[0])
    labels = [f"{n} ({v / total:.1%})" for n, v in zip(Y.keys(), result[Y.keys()].values[0])]
    plt.pie(result[Y.keys()].values[0])
    plt.legend(bbox_to_anchor=(-0.16, 0.45, 0.25, 0.25), loc='best', labels=labels)
    plt.title(name)