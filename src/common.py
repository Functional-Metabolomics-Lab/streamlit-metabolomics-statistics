import streamlit as st
import pandas as pd
import io
import uuid


def page_setup():
    # streamlit configs
    st.set_page_config(
        page_title="Statistics for Metabolomics",
        page_icon="assets/icon.png",
        # layout="wide",
        initial_sidebar_state="auto",
        menu_items=None,
    )
    # initialize global session state variables if not already present
    # DataFrames
    for key in ("md", "data"):
        if key not in st.session_state:
            st.session_state[key] = pd.DataFrame()
    if "data_preparation_done" not in st.session_state:
        st.session_state["data_preparation_done"] = False

    m = st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: #0d6efd;
            color:#ffffff;
            border-color: #0d6efd;
        }
        div.stButton > button:hover {
            background-color: #ffffff;
            color:#FF4B4B;
            border-color: #FF4B4B;
            }
        </style>""",
        unsafe_allow_html=True,
    )


def v_space(n, col=None):
    for _ in range(n):
        if col:
            col.write("")
        else:
            st.write("")


def open_df(file):
    separators = {"txt": "\t", "tsv": "\t", "csv": ","}
    try:
        if type(file) == str:
            ext = file.split(".")[-1]
            if ext != "xlsx":
                df = pd.read_csv(file, sep=separators[ext])
            else:
                df = pd.read_excel(file)
        else:
            ext = file.name.split(".")[-1]
            if ext != "xlsx":
                df = pd.read_csv(file, sep=separators[ext])
            else:
                df = pd.read_excel(file)
        # sometimes dataframes get saved with unnamed index, that needs to be removed
        if "Unnamed: 0" in df.columns:
            df.drop("Unnamed: 0", inplace=True, axis=1)
        return df
    except:
        return pd.DataFrame()


def show_table(df, title="", col="", download=True):
    if col:
        col = col
    else:
        col = st
    if title:
        col.markdown(f"**{title}**")
    if download:
        col.download_button(
            f"Download Table",
            df.to_csv(sep="\t").encode("utf-8"),
            title.replace(" ", "-") + ".tsv",
            key=uuid.uuid1(),
        )
    col.dataframe(df)


def download_plotly_figure(fig, filename="", col=""):
    buffer = io.BytesIO()
    fig.write_image(file=buffer, format="png")

    if col:
        col.download_button(
            label=f"Download Figure",
            data=buffer,
            file_name=filename,
            mime="application/png",
        )
    else:
        st.download_button(
            label=f"Download Figure",
            data=buffer,
            file_name=filename,
            mime="application/png",
        )
