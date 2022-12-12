# plotnine plotting theme

# plotnine imports
from plotnine import ggplot, geom_point, geom_line, geom_histogram, geom_bar
from plotnine import aes, theme, themes, element_blank, element_line, element_text, mapping, xlab, ylab, ggtitle
from plotnine.geoms import geom_vline, geom_boxplot
from plotnine.scales import scale_x_discrete, scale_y_discrete, scale_x_continuous, scale_y_continuous
from plotnine.options import figure_size

# plotnine theme
def theme_tufte_func(base_size=19, base_family="sans", rotate=True, figure_size=None):
    ''' Plotnine plotting theme. '''
    thm = themes.theme_bw(base_size=base_size, base_family = base_family) + \
        theme(
            legend_background = element_blank(),
            legend_key = element_blank(),
            panel_background = element_blank(),
            panel_border = element_blank(),
            strip_background = element_blank(),
            plot_background = element_blank(),
            panel_grid = element_blank(),
            axis_line = element_line(colour = "black", size = 1),
            axis_text_y = element_text(colour = "black")
        )

    if rotate:
        thm += theme(axis_text_x=element_text(rotation=45, hjust=1, size=4))
    if figure_size is not None:
        thm += theme(figure_size=figure_size)

    return thm

