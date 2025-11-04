import os

from cProfile import label
import matplotlib.pyplot as plt
import seaborn as sns

FEATURES_DIR = "features"   # folder to export figures to
COLOR_LIST = ["#A5D7E8", "#576CBC", "#19376D", "#0b2447"]

os.makedirs(FEATURES_DIR, exist_ok=True)    # Ensure the folder exists


def plot_count_pairs(data_df, feature, title, hue="set"):
    f, ax = plt.subplots(1, 1, figsize=(8, 4))
    sns.countplot(x=feature, data=data_df, hue=hue, palette=COLOR_LIST)
    plt.grid(color="black", linestyle="-.", linewidth=0.5, axis="y", which="major")
    ax.set_title(f"Number of passengers / {title}")

    file_path = os.path.join(FEATURES_DIR, f"{feature}_countplot.png")
    plt.savefig(file_path, bbox_inches="tight")
    print(f"Saved figure to {file_path}")

    plt.show()


def plot_distribution_pairs(data_df, feature, title, hue="set"):
    f, ax = plt.subplots(1, 1, figsize=(8, 4))
    for i, h in enumerate(data_df[hue].unique()):
        g = sns.histplot(
            data_df.loc[data_df[hue] == h, feature], color=COLOR_LIST[i], ax=ax, label=h
        )
    ax.set_title(f"Number of passengers / {title}")
    g.legend()

    file_path = os.path.join(FEATURES_DIR, f"{feature}_distribution.png")
    plt.savefig(file_path, bbox_inches="tight")
    print(f"Saved figure to {file_path}")
    
    plt.show()



def plot_categorical_survival(data_df, categorical_cols, target='Survived',
                              figsize=(15, 5), color="skyblue", edgecolor="black"):
    """
    Plots barplots of the mean target value for multiple categorical columns.

    Parameters
    ----------
    data_df : pd.DataFrame
        The dataframe containing the data.
    categorical_cols : list of str
        List of categorical columns to plot.
    target : str, default='Survived'
        The target column to plot against.
    figsize : tuple, default=(15, 5)
        Figure size.
    color : str, default='skyblue'
        Bar color.
    edgecolor : str, default='black'
        Bar edge color.
    """
    n_cols = len(categorical_cols)
    fig, axes = plt.subplots(1, n_cols, figsize=figsize)
    
    # If only one column, axes is not an array
    if n_cols == 1:
        axes = [axes]
    
    for ax, col in zip(axes, categorical_cols):
        sns.barplot(data=data_df, x=col, y=target, color=color, edgecolor=edgecolor, ax=ax)
        ax.set_title(f"{target} by {col}")

    file_path = os.path.join(FEATURES_DIR, "vis1.png")
    plt.savefig(file_path, bbox_inches="tight")
    print(f"Saved figure to {file_path}")
    
    plt.tight_layout()
    plt.show()