import pandas as pd

def limpiar_presupuesto(file):

    df_raw = pd.read_excel(file, header=None)

    # --- detectar header ---
    primera_col = df_raw.iloc[:, 0].astype(str)

    idx_header = primera_col[
        primera_col.str.contains("Código de Programa", case=False, na=False)
    ].index

    if len(idx_header) == 0:
        raise ValueError("No se encontró 'Código de Programa'.")

    idx_header = idx_header[0]

    df = df_raw.loc[idx_header:].reset_index(drop=True)
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    # --- cortar desde MONTOS PROYECTADOS ---
    primera_col = df.iloc[:, 0].astype(str)

    idx_corte = primera_col[
        primera_col.str.contains(
            "MONTOS PROYECTADOS SEGÚN PARTIDA PRESUPUESTARIA",
            case=False,
            na=False
        )
    ].index

    if len(idx_corte) > 0:
        df = df.loc[:idx_corte[0] - 1]

    df = df.dropna(how="all").dropna(axis=1, how="all")

    # --- limpiar montos ---
    def limpiar_monto(valor):
        if pd.isna(valor):
            return 0.0
        valor = str(valor)
        valor = valor.replace("₡", "").replace(" ", "").replace("\xa0", "")
        if "," in valor:
            valor = valor.replace(".", "").replace(",", ".")
        return float(valor)

    columnas_meses = [
        col for col in df.columns
        if isinstance(col, str) and any(
            mes in col.lower() for mes in [
                "enero","febrero","marzo","abril","mayo","junio",
                "julio","agosto","septiembre","octubre","noviembre","diciembre"
            ]
        )
    ]

    for col in columnas_meses:
        df[col] = df[col].apply(limpiar_monto)

    if "Total por indicador" in df.columns:
        df["Total por indicador"] = df["Total por indicador"].apply(limpiar_monto)
    # -----------------------------------------
    # Eliminar fila de total general si existe
    # -----------------------------------------

    if isinstance(df.iloc[-1, 0], str) and "total" in df.iloc[-1, 0].lower():
        df = df.iloc[:-1].reset_index(drop=True)
        
    total_global = df["Total por indicador"].sum()

    return df, total_global