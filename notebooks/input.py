import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import requests
    return mo, requests


@app.cell
def __(mo):
    functions = ['AlphaFold', 'BLAST']
    function_selector = mo.ui.dropdown(functions, label="Select Function")
    function_selector
    return function_selector, functions


@app.cell
def __(function_selector, mo):
    alphafold_input_types = []
    blast_input_types = []
    secondary_selecter = None

    if function_selector.value == 'AlphaFold':
        secondary_selecter = mo.ui.dropdown(alphafold_input_types, label="Select AlphaFold Function")

    if function_selector.value == 'BLAST':
        secondary_selecter = mo.ui.dropdown(blast_input_types, label="Select BLAST Function")

    secondary_selecter
    return alphafold_input_types, blast_input_types, secondary_selecter


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
