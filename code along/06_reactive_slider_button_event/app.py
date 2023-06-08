from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", min=1, max=100, value=1),
    ui.input_action_button("compute", "Compute!"),
    ui.output_text_verbatim("result", placeholder=True),
)

def server(input, output, session):

    @output
    @render.text
    @reactive.event(input.compute) # Take a dependency on the button
    def result():
        # Because of the @reactive.event(), everything in this function is
        # ignored for reactive dependencies.
        return f"Result: {input.n()}"

app = App(app_ui, server)
