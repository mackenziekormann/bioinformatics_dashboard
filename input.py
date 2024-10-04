import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    functions = ['AlphaFold', 'BLAST']
    function_selecter = mo.ui.dropdown(functions)
    function_selecter
    return function_selecter, functions


app._unparsable_cell(
    r"""
    if function_selecter.value == 'AlphaFold':
        
    """,
    name="__"
)


if __name__ == "__main__":
    app.run()
