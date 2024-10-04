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
    function_selector = mo.ui.dropdown(functions)
    function_selector
    return function_selector, functions


@app.cell
def __(function_selector, mo):
    alphafold_functions = ['UniProt ID', 'AlphaFold DB ID']
    if function_selector.value == 'AlphaFold':
        alphafold_selector = mo.ui.dropdown(alphafold_functions)
        alphafold_selector
    return alphafold_functions, alphafold_selector


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
