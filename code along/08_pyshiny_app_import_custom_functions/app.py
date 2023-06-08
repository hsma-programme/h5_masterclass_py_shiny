# Necessary Imports
from shiny import App, render, ui
from report_tools import funcs as rt

# Part 1: ui ----
app_ui = ui.page_fluid(
    ui.input_slider("n", "Number Slider-Bar", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_plot("histogram"),
)

# Part 2: server ----
def server(input, output, session):
    @output
    @render.text
    def txt():
        return rt.print_hello(input.n())
    
    @output
    @render.plot(alt="A histogram")
    def histogram():
        rt.chart(input.n())

# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)