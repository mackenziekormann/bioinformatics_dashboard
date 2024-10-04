import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import requests
    return mo, requests


@app.cell
def __():
    base_url = "https://alphafold.ebi.ac.uk/api"
    return (base_url,)


if __name__ == "__main__":
    app.run()
