import matplotlib.pyplot as plt

def stacked_bar(var_1, var_2,data,title=None):

    x = data.groupby(var_1)[var_2].value_counts(normalize=True).unstack()
    x.plot(kind='bar', stacked='True', figsize=(8,6))
    plt.legend(loc=1)
    plt.title(title + var_1)
    plt.xticks(rotation=45)
    plt.show();
