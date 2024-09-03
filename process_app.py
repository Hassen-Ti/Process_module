import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd
import math
# Ma superbe application pour visualiser
def visual(df):
  output = widgets.Output()
  
  def on_button_hist(b):
      with output:
          clear_output()  
          histograme(df)
  
  def on_button_boxplot(b):
        with output:
            clear_output()
            boxplote(df)
  
  def on_button_pairplot(b):
      with output:
          clear_output()
          sns.pairplot(df)
          plt.show()
  

          
  button_hist = widgets.Button(description="Histogram")
  button_boxplot = widgets.Button(description="Boxplot")
  button_pairplot = widgets.Button(description="Pairplot")


  button_hist.on_click(on_button_hist)
  button_boxplot.on_click(on_button_boxplot)
  button_pairplot.on_click(on_button_pairplot)


  buttons_row1 = widgets.HBox([button_hist, button_boxplot, button_pairplot])
 
  buttons_layout = widgets.VBox([buttons_row1])

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
    output = widgets.Output()
    lien_url = widgets.Text(value="Insérez l'URL", description="URL")
    mon_df = widgets.Text(value="Insérez le nom de votre DF", description="Nom DataFrame")

    display(lien_url, mon_df)

    def on_button_1(btn):
        url = lien_url.value
        df_name = mon_df.value
        try:
            df = pd.read_csv(url)
            globals()[df_name] = df
            print(f"votre df a été créé avec succès sous le nom de {df_name}")
            preprocessing(df)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier CSV: {e}")

    bouton_1 = widgets.Button(description="Votre DF")
    bouton_1.on_click(on_button_1)
    display(bouton_1)
    
    
    
# Interactive function for boxplot
def boxplote(df):
    output = widgets.Output()
    
    # Grouping widgets
    title_widget = widgets.Text(value='Box Plot', description='Title:')
    x_column_widget = widgets.Dropdown(options=df.columns, description='X Axis:')
    y_column_widget = widgets.Dropdown(options=df.columns, description='Y Axis:')
    hue_widget = widgets.Dropdown(options=[None] + list(df.columns), description='Hue:')
    figsize_widget_a = widgets.Text(value='5', description='Width:')
    figsize_widget_b = widgets.Text(value='5', description='Height:')
    save_widget = widgets.Checkbox(value=False, description='Save Figure')
    filename_widget = widgets.Text(value='boxplot.png', description='Filename:')
    
    # Organizing widgets in HBox
    title_hbox = widgets.VBox([title_widget, x_column_widget, y_column_widget])
    hue_figsize_hbox = widgets.VBox([hue_widget, figsize_widget_a, figsize_widget_b])
    save_hbox = widgets.VBox([save_widget, filename_widget])
    all_v_box = widgets.HBox([title_hbox, hue_figsize_hbox, save_hbox])
    # Displaying the widgets
    display(all_v_box)
    
    def on_button_click(b):
        with output:
            clear_output()
            try:
                width = int(figsize_widget_a.value)
                height = int(figsize_widget_b.value)
            except ValueError:
                print("Please enter valid numbers for figsize.")
                return
            
            title = title_widget.value
            x_column = x_column_widget.value
            y_column = y_column_widget.value
            hue = hue_widget.value
            save_option = save_widget.value
            filename = filename_widget.value if save_option else ""
            
            plt.figure(figsize=(width, height))
            sns.boxplot(x=x_column, y=y_column, data=df, hue=hue if hue != 'None' else None)
            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            
            if save_option and filename:
                plt.savefig(filename)
                print(f"Figure saved as {filename}")
            
            plt.show()
    
    # Button to generate the plot
    button = widgets.Button(description="Generate Box plot")
    button.on_click(on_button_click)
    display(button, output)

# my interactive function for plot "histogram"
def histograme(df):
    output = widgets.Output()
    
    columns_widget = widgets.SelectMultiple(options=df.columns, description='Columns:')
    bins_widget = widgets.IntSlider(value=10, min=1, max=50, step=1, description='Bins:')
    color_widget = widgets.ColorPicker(value='blue', description='Color:')
    figsize_widget_a = widgets.Text(value='5', description='Width:')
    figsize_widget_b = widgets.Text(value='5', description='Height:')
    title_widget = widgets.Text(value='Histogram', description='Title:')
    save_widget = widgets.Checkbox(value=False, description='Save Figure')
    filename_widget = widgets.Text(value='histogram.png', description='Filename:')
    
    title_hbox = widgets.VBox([title_widget, columns_widget, bins_widget])
    hue_figsize_hbox = widgets.VBox([color_widget, figsize_widget_a, figsize_widget_b])
    save_hbox = widgets.VBox([save_widget, filename_widget])
    all_v_box = widgets.HBox([title_hbox, hue_figsize_hbox, save_hbox])
    display(all_v_box)
    
    def on_button_click(b):
        with output:
            clear_output()
            try:
                width = int(figsize_widget_a.value)
                height = int(figsize_widget_b.value)
            except ValueError:
                print("Please enter valid numbers for figsize.")
                return
            
            selected_columns = list(columns_widget.value)
            bins = bins_widget.value
            color = color_widget.value
            title = title_widget.value
            save_option = save_widget.value
            filename = filename_widget.value if save_option else ""
            
            if not selected_columns:
                print("Please select at least one column.")
                return
            
            # Check and factorize non-numeric columns pd (pandas), api.types() is module from pandas, and it's works with pandas types (df or series)
            # is numeric_dtype it's a function that return a booelan, true if there is numeric value false if not
            for col in selected_columns:
                if not pd.api.types.is_numeric_dtype(df[col]):
                    df[col] = df[col].astype('category').cat.codes
                    print(f"Column '{col}' has been factorized.")

            df[selected_columns].hist(bins=bins, color=color, figsize=(width, height))
            plt.suptitle(title)
            
            if save_option and filename:
                plt.savefig(filename)
                print(f"Figure saved as {filename}")
            
            plt.show()
    
    button = widgets.Button(description="Generate Histogram")
    button.on_click(on_button_click)
    display(button, output)
