from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", min=1, max=100, value=1),
    ui.input_action_button("compute", "Compute!"),
    ui.output_text_verbatim("result", placeholder=True),
)

def server(input, output, session):

    @output
    @render.text
    def result():
        input.compute()        # Take a dependency on the button

        with reactive.isolate():
            # Inside this block, we can use input.n() without taking a
            # dependency on it.
            return f"Result: {input.n()}"

app = App(app_ui, server)
