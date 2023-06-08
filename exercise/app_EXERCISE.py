# There are 5 missing values to correct in the code below
# Missing values have been replaced with XXXX and their rows are commented with  # <- missing value here
from math import ceil
from typing import List
from datetime import date
from pathlib import Path
import numpy as np
import pandas as pd
from io import StringIO

from XXXX import App, reactive, render, ui # <- missing value here

# A card component wrapper.
def ui_card(title, *args):
    return (
        ui.div(
            {"class": "card mb-4"},
            ui.div(title, class_="card-header"),
            ui.div({"class": "card-body"}, *args),
        ),
    )


app_ui = ui.XXXX( # <- missing value here
    ui_card(
        "CSV File Upload",
        ui.input_file("file1", "Choose CSV file to upload:", multiple=True),
        ui.output_text_verbatim("csv_shape", placeholder=True),
        ui.input_numeric("n_rows", "Rows to preview", 5),
        ui.input_action_button("show_df", "Display contents as DF"),
        ui.output_table("csv_table"),
        ui.input_action_button("add_dummy_col", "Add Dummy Column"),
        ui.XXXX("add_dummy_button_feedback", placeholder=True), # <- missing value here
    ),
    ui_card(
        "Export",
        ui.download_button("download_df", "Download CSV"), 
    ),  
)

def XXXX(input, output, session):  # <- missing value here
    MAX_SIZE = 50000

    # Helper function to check if a file is loaded yet
    def file_loaded_chk(input):
        file_infos = input.file1()
        if not file_infos:
            return False
        else:
            return True


    # Helper function converting loaded CSV to DF
    def csv2df(input):
        file_infos = input.file1()
        if file_loaded_chk(input):
            global df
            out_str = ""
            for file_info in file_infos:
                with open(file_info["datapath"], "r") as f:
                    out_str += f.read(MAX_SIZE)
            data = list(map(lambda x: x.split(','),out_str.split("\n")))
            df = pd.DataFrame(data[1:], columns=data[0])
            return df




    # Return the shape of the CSV once loaded (and not before!)
    @XXXX # <- missing value here
    @render.text
    def csv_shape():
        if file_loaded_chk(input):
             df = csv2df(input)
             rows_cols = df.shape
             return f"The loaded CSV has {rows_cols[1]} cols and {rows_cols[0]} rows"


    # Display a preview (head) of DF from loaded CSV
    @output
    @render.table
    @reactive.event(input.show_df)
    def csv_table():
        if file_loaded_chk(input):
            file_infos = input.file1()
            out_str = ""
            for file_info in file_infos:
                with open(file_info["datapath"], "r") as f:
                    file_text = StringIO(f.read())
                    df = pd.read_csv(file_text)
            n_rows = input.n_rows()
            return df.head(n_rows)

    
    # Create a dummy column in the DF, if it exists
    @output
    @render.text
    @reactive.event(input.add_dummy_col)
    def add_dummy_button_feedback():
        if file_loaded_chk(input):
             df['dummy'] = 1
             return "Dummy column added"

  
    # Export/ download CSV
    @session.download(
        filename=lambda: f"data-{date.today().isoformat()}-{np.random.randint(100,999)}.csv"
    )
    def download_df():
        yield df.to_string(index=False)

app = App(app_ui, server)
