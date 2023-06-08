from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.panel_title("Simulate a normal distribution"),
    ui.layout_sidebar(
      ui.panel_sidebar(
        ui.input_slider("n", "Sample size", 0, 1000, 250),
        ui.input_numeric("mean", "Mean", 0),
        ui.input_numeric("std_dev", "Standard deviation", 1),
        ui.input_slider("n_bins", "Number of bins", 0, 100, 20),
      ),

      ui.panel_main(
        ui.output_plot("plot")
      ),
    ),
)

def server(input, output, session):
    
    @output
    @render.plot(alt="A histogram")
    def plot() -> object:
        x = np.random.normal(input.mean(), input.std_dev(), input.n())
        fig, ax = plt.subplots()
        ax.hist(x, input.n_bins(), density=True)
        return fig

app = App(app_ui, server)
