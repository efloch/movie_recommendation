from src.params import *
from src.config import *
import src.process_data as input


def viz_distrib_scores(df_reviews, list_of_names):
    plt.figure(figsize=(8, 4))
    count_liunards = len(list_of_names)
    rows = count_liunards
    columns = 1
    for i, name in enumerate(list_of_names):
        plt.subplot(rows, columns, i+1)
        if f"{name} score" in df_reviews:
            df_reviews[f"{name} score"].dropna(inplace=True)
            sns.distplot(df_reviews[f"{name} score"])
    plt.show()


def ridgeplot(df_reviews, list_of_names):

    df_reviews = input.melted_reviews()
    print(df_reviews.head())

    # # Initialize the FacetGrid object
    # pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
    # g = sns.FacetGrid(df_reviews, row=LIUNARDS, hue="g",
    #                   aspect=15, height=.5, palette=pal)
    #
    # # Draw the densities in a few steps
    # g.map(sns.kdeplot, "x", clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
    # g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw=.2)
    # g.map(plt.axhline, y=0, lw=2, clip_on=False)
    #
    # # Define and use a simple function to label the plot in axes coordinates
    #
    # def label(x, color, label):
    #     ax = plt.gca()
    #     ax.text(0, .2, label, fontweight="bold", color=color,
    #             ha="left", va="center", transform=ax.transAxes)
    #
    # g.map(label, "x")
    #
    # # Set the subplots to overlap
    # g.fig.subplots_adjust(hspace=-.25)
    #
    # # Remove axes details that don't play well with overlap
    # g.set_titles("")
    # g.set(yticks=[])
    # g.despine(bottom=True, left=True)


if __name__ == '__main__':
    df_reviews = input.clean_reviews()
    # viz_distrib_scores(df_reviews, LIUNARDS)
    ridgeplot(df_reviews, LIUNARDS)
