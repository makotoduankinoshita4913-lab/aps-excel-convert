import streamlit as st
import pandas as pd

from convert_aps_to_uji_tsv import OUTPUT_HEADERS, rows_from_bytes, rows_to_tsv

st.set_page_config(page_title="APS在庫表 -> UJI TSV", layout="wide")
st.title("APS在庫表をUJI在庫アップロード用TSVに変換")

uploaded = st.file_uploader("APSのExcel（.xlsx）をアップロード", type=["xlsx"])

if uploaded:
    try:
        rows = rows_from_bytes(uploaded.getvalue())
        tsv_text = rows_to_tsv([OUTPUT_HEADERS] + rows)
    except Exception as e:
        st.error(f"変換でエラー: {e}")
    else:
        st.subheader("TSVプレビュー")
        df = pd.DataFrame(rows, columns=OUTPUT_HEADERS)
        st.dataframe(df)

        st.subheader("TSV出力")
        st.text_area("TSV", tsv_text, height=240)

        st.download_button(
            label="TSVをダウンロード",
            data=tsv_text,
            file_name="aps_to_uji.tsv",
            mime="text/tab-separated-values",
        )
else:
    st.info("ファイルを選択してください。")
