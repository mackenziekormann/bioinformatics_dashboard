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
def __(alphafold_input_types, blast_input_types, function_selector, mo):
    if function_selector.value == 'AlphaFold':
        alphafold_selector = mo.ui.dropdown(alphafold_input_types, label="Select AlphaFold Function")

    if function_selector.value == 'BLAST':
        blast_selector = mo.ui.dropdown(blast_input_types, label="Select BLAST Function")
    return alphafold_selector, blast_selector


if __name__ == "__main__":
    app.run()
