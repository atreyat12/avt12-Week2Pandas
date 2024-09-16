import pandas as pd
import matplotlib.pyplot as plt

data1 = "NBA_Data.csv"


def load_dataset(data):
    df = pd.read_csv(data)
    return df


def nba_summary(data):
    return data.describe()


def histogram_ast(data):
    df = load_dataset(data)
    plt.figure(figsize=(10, 6))
    plt.hist(df["AST"], bins=20)
    plt.title("Assists in 2023-24 Season-1")
    plt.xlabel("NBA Players")
    plt.ylabel("%")
    plt.savefig("assists.png")
    return plt.show()


def bar_chart_points(data):
    df = pd.read_csv(data)
    plt.figure(figsize=(10, 6))
    plt.bar(df["Pos"], df["AST"], color="maroon", width=0.4)
    plt.savefig("points_by_position1.png")
    plt.show()


def g_describe(data):
    g = load_dataset(data)
    return nba_summary(g)


def grab_mean(data, col):
    return data[col].mean()


def grab_median(data, col):
    return data[col].median()


def grab_stdev(data, col):
    return data[col].std()


def stat_update(data, col):
    df = load_dataset(data)
    mean1 = grab_mean(df, col)
    median1 = grab_median(df, col)
    stdev1 = grab_stdev(df, col)
    df1 = pd.DataFrame([mean1, median1, stdev1])
    return df1


histogram_ast(data1)
bar_chart_points(data1)


def save_to_md(data):
    test = g_describe(data)
    test2 = stat_update(data, "AST")
    mkdown = test.to_markdown()
    mkdown2 = test2.to_markdown()
    with open("nbastats.md", "a", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(mkdown)
        file.write("Summarize:\n")
        file.write(mkdown2)
        file.write("n\n")
        file.write("![NBA_1](points_by_position1.png)\n")
        file.write("n\n")
        file.write("![NBA_2](assists.png)\n")


if __name__ == "__main__":
    save_to_md(data1)
