import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd
# Ma superbe application pour visualiser
def visual(df):
  output = widgets.Output()
  def on_button_hist(b):
      with output:
          clear_output()
          df.hist(figsize=(10, 8))
          plt.show()
  
  def on_button_boxplot(b):
      with output:
          clear_output()
          df.plot(kind='box', subplots=True, layout=(3, 3), figsize=(14, 12))
          plt.show()
  
  def on_button_pairplot(b):
      with output:
          clear_output()
          sns.pairplot(df)
          plt.show()
  
  def on_button_missing_heatmap(b):
      with output:
          clear_output()
          plt.figure(figsize=(10, 8))
          sns.heatmap(df.isna(), cbar=False, cmap='viridis')
          plt.title('Heatmap of Missing Values')
          plt.show()
          
  button_hist = widgets.Button(description="Histogram")
  button_boxplot = widgets.Button(description="Boxplot")
  button_pairplot = widgets.Button(description="Pairplot")
  button_missing_heatmap = widgets.Button(description="Missing Heatmap")

  button_hist.on_click(on_button_hist)
  button_boxplot.on_click(on_button_boxplot)
  button_pairplot.on_click(on_button_pairplot)
  button_missing_heatmap.on_click(on_button_missing_heatmap)

  buttons_row1 = widgets.HBox([button_hist, button_boxplot, button_pairplot])
  buttons_row2 = widgets.HBox([button_missing_heatmap])  
  buttons_layout = widgets.VBox([buttons_row1, buttons_row2])

  display(buttons_layout, output)
  
  
  

# ma superbe application pour explorer le dataframe
def preprocessing(df):
    output = widgets.Output()
    
    def on_button_info(b):
        with output:
            clear_output()
            df.info()
    
    def on_button_describe(b):
        with output:
            clear_output()
            display(df.describe(include='all'))
    
    def on_button_head(b):
        with output:
            clear_output()
            display(df.head())
    
    def on_button_tail(b):
        with output:
            clear_output()
            display(df.tail())
    
    def on_button_shape(b):
        with output:
            clear_output()
            display(df.shape)
    
    def on_button_columns(b):
        with output:
            clear_output()
            display(df.columns)
    
    def on_button_nunique(b):
        with output:
            clear_output()
            display(df.nunique())
    
    def on_button_dtypes(b):
        with output:
            clear_output()
            display(df.dtypes)
    
    def on_button_isna(b):
        with output:
            clear_output()
            display(df.isna().sum())
    
    def on_button_duplicate(b):
        with output:
            clear_output()
            display(df.duplicated().sum())

    button_info = widgets.Button(description="Info")
    button_describe = widgets.Button(description="Describe")
    button_head = widgets.Button(description="Head (5 rows)")
    button_tail = widgets.Button(description="Tail (5 rows)")
    button_shape = widgets.Button(description="Shape")
    button_columns = widgets.Button(description="Columns")
    button_nunique = widgets.Button(description="Nunique")
    button_dtypes = widgets.Button(description="Dtypes")
    button_isna = widgets.Button(description="Isna")
    button_duplicate = widgets.Button(description="Duplicated")

    button_info.on_click(on_button_info)
    button_describe.on_click(on_button_describe)
    button_head.on_click(on_button_head)
    button_tail.on_click(on_button_tail)
    button_shape.on_click(on_button_shape)
    button_columns.on_click(on_button_columns)
    button_nunique.on_click(on_button_nunique)
    button_dtypes.on_click(on_button_dtypes)
    button_isna.on_click(on_button_isna)
    button_duplicate.on_click(on_button_duplicate)

    
    buttons_row1 = widgets.HBox([button_info, button_describe, button_head, button_tail, button_dtypes])
    buttons_row2 = widgets.HBox([button_shape, button_columns, button_nunique, button_duplicate, button_isna])
    buttons_layout = widgets.VBox([buttons_row1, buttons_row2])

    display(buttons_layout, output)
    
    # Mon SUPER generateur de HEATMAP *==HASSENE==*

def heatmap_gen_Hass(df):
    title_widget = widgets.Text(value='Heatmap of Correlation Matrix', description='Title:')
    columns_widget = widgets.Text(value='', description='Columns:')
    save_widget = widgets.Checkbox(value=False, description='Save Figure')
    filename_widget = widgets.Text(value='heatmap.png', description='Filename:')
    
    display(title_widget, columns_widget, save_widget, filename_widget)
    
    def on_button_click(b):
        title = title_widget.value
        columns = columns_widget.value
        save_option = save_widget.value
        filename = filename_widget.value if save_option else ""
        
        if columns:
            columns = [col.strip() for col in columns.split(',')]
            correlation_matrix = df[columns].corr()
        else:
            correlation_matrix = df.corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title(title)
        
        if filename:
            plt.savefig(filename)
            print(f"Figure sauvegardée sous le nom {filename}")
        
        plt.show()
    
    button = widgets.Button(description="Generate Heatmap")
    button.on_click(on_button_click)
    display(button)
    
    
    def url_df():
    lien_url = widgets.Text(value="Insérez l'URL", description="URL")
    mon_df = widgets.Text(value="Insérez le nom de votre DF", description="Nom DataFrame")

    display(lien_url, mon_df)

    def on_button_1(btn):
        url = lien_url.value
        df_name = mon_df.value
        try:
            df = pd.read_csv(url)
            globals()[df_name] = df
            print(f"votre DataFrame a été créé avec succès sous le nom de {df_name}")
            pa.preprocessing(df)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier CSV: {e}")

    bouton_1 = widgets.Button(description="Votre DF")
    bouton_1.on_click(on_button_1)
    display(bouton_1)