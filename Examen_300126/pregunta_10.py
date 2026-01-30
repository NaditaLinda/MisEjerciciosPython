import pandas as pd
import os

# --- 1. CONFIGURACIÓN ---
BASE_PATH = os.path.dirname(__file__)
FILES = {
    'fincas': ('fincas.csv', ['id_finca', 'superficie_m2']),
    'propietarios': ('propietarios.csv', ['id_propietario', 'nombre_completo']),
    'titularidad': ('titularidad.csv', ['id_finca', 'id_propietario', 'porcentaje_propiedad']),
    'cargas': ('cargas.csv', ['id_finca', 'tipo_carga'])
}

def ejecutar_produccion():
    print("🚀 Iniciando proceso de generación de informes...")
    dfs = {}

    # --- 2. VALIDACIÓN AL ARRANCAR ---
    for key, (name, cols) in FILES.items():
        path = os.path.join(BASE_PATH, name)
        if not os.path.exists(path):
            print(f"❌ ERROR CRÍTICO: No se encuentra el archivo {name}")
            return
        
        df = pd.read_csv(path)
        # Verificamos que las columnas necesarias existan
        missing = [c for c in cols if c not in df.columns]
        if missing:
            print(f"❌ ERROR: Al archivo {name} le faltan columnas: {missing}")
            return
        
        dfs[key] = df
    print("✅ Validación completada con éxito.")

    # --- 3. GENERACIÓN DE INFORMES ---

    # Informe 1: Fincas con cargas (excluyendo "Libre de cargas")
    print("📊 Generando informe de cargas...")
    inf_cargas = dfs['cargas'][dfs['cargas']['tipo_carga'] != 'Libre de cargas'].copy()
    inf_cargas.to_csv(os.path.join(BASE_PATH, 'informe_fincas_con_cargas.csv'), index=False)

    # Informe 2: Fincas con varios propietarios (Copropiedad)
    print("📊 Generando informe de copropiedad...")
    coprop = dfs['titularidad'].groupby('id_finca').size().reset_index(name='num_propietarios')
    inf_coprop = coprop[coprop['num_propietarios'] > 1]
    inf_coprop.to_csv(os.path.join(BASE_PATH, 'informe_varios_propietarios.csv'), index=False)

    # Informe 3: Ranking de propietarios por superficie
    print("📊 Generando ranking de propietarios...")
    # Mapeamos superficie a titularidad para cálculo ponderado
    map_superficie = dfs['fincas'].set_index('id_finca')['superficie_m2'].to_dict()
    df_tit = dfs['titularidad'].copy()
    df_tit['m2_propiedad'] = df_tit.apply(
        lambda x: (x['porcentaje_propiedad'] / 100) * map_superficie.get(x['id_finca'], 0), axis=1
    )
    
    ranking = df_tit.groupby('id_propietario')['m2_propiedad'].sum().reset_index()
    # Mapeamos nombres para el informe final
    map_nombres = dfs['propietarios'].set_index('id_propietario')['nombre_completo'].to_dict()
    ranking['nombre_completo'] = ranking['id_propietario'].map(map_nombres)
    
    inf_ranking = ranking.sort_values(by='m2_propiedad', ascending=False)
    inf_ranking.to_csv(os.path.join(BASE_PATH, 'informe_ranking_propietarios.csv'), index=False)

    # --- CIERRE ---
    print("\n" + "="*40)
    print("✨ PROCESO FINALIZADO ✨")
    print(f"- Cargas detectadas: {len(inf_cargas)}")
    print(f"- Fincas en copropiedad: {len(inf_coprop)}")
    print(f"- Propietario líder: {inf_ranking.iloc[0]['nombre_completo']} ({inf_ranking.iloc[0]['m2_propiedad']:.2f} m²)")
    print("="*40)

if __name__ == "__main__":
    ejecutar_produccion()