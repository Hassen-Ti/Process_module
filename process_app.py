import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd
import math


def preprocessing(df):
    """
    Interactive widget to explore a pandas DataFrame.
    """
    # Output widget
    output = widgets.Output()

    # Widgets for column selection
    all_columns = df.columns.tolist()

    # Widget for single column selection
    column_select_single = widgets.Dropdown(
        options=all_columns,
        description='Select Column:',
        disabled=False
    )

    # Widgets for filtering data
    filter_column = widgets.Dropdown(
        options=all_columns,
        description='Filter Column:',
        disabled=False
    )
    filter_condition = widgets.Dropdown(
        options=['==', '!=', '>', '<', '>=', '<=', 'contains'],
        description='Condition:',
        disabled=False
    )
    filter_value = widgets.Text(
        value='',
        description='Value:',
        disabled=False
    )

    # Define button actions
    def show_info(_):
        with output:
            clear_output()
            print(df.info())

    def show_describe(_):
        with output:
            clear_output()
            display(df.describe(include='all'))

    def show_head(_):
        with output:
            clear_output()
            display(df.head())

    def show_tail(_):
        with output:
            clear_output()
            display(df.tail())

    def show_shape(_):
        with output:
            clear_output()
            print(f"Shape: {df.shape}")

    def show_columns(_):
        with output:
            clear_output()
            print("Columns:")
            for col in df.columns:
                print(col)

    def show_nunique(_):
        with output:
            clear_output()
            display(df.nunique())

    def show_dtypes(_):
        with output:
            clear_output()
            display(df.dtypes)

    def show_missing_data(_):
        with output:
            clear_output()
            missing_data = df.isna().sum()
            missing_data = missing_data[missing_data > 0]
            if not missing_data.empty:
                print("Missing values per column:")
                display(missing_data)
            else:
                print("No missing data in the DataFrame.")

    def show_duplicates(_):
        with output:
            clear_output()
            duplicates = df[df.duplicated()]
            num_duplicates = duplicates.shape[0]
            print(f"Number of duplicate rows: {num_duplicates}")
            if num_duplicates > 0:
                display(duplicates)

    def show_value_counts(_):
        with output:
            clear_output()
            col = column_select_single.value
            if col:
                display(df[col].value_counts())
            else:
                print("Please select a column.")

    def filter_data(_):
        with output:
            clear_output()
            col = filter_column.value
            cond = filter_condition.value
            val = filter_value.value
            try:
                if col:
                    col_dtype = df[col].dtype

                    # Handle 'contains' separately
                    if cond == 'contains':
                        if pd.api.types.is_string_dtype(col_dtype):
                            filtered_df = df[df[col].str.contains(val, na=False)]
                            display(filtered_df)
                        else:
                            print(f"The 'contains' condition is only applicable to string columns. '{col}' is of type {col_dtype}.")
                    else:
                        # Convert val to appropriate data type
                        if pd.api.types.is_numeric_dtype(col_dtype):
                            val_converted = float(val)
                        elif pd.api.types.is_datetime64_any_dtype(col_dtype):
                            val_converted = pd.to_datetime(val)
                        else:
                            val_converted = val  # Keep as string for object columns

                        # Use @val_converted to pass the value into the query
                        filtered_df = df.query("`{}` {} @val_converted".format(col, cond))
                        display(filtered_df)
                else:
                    print("Please select a column for filtering.")
            except ValueError:
                print(f"Invalid value for the data type of column '{col}'. Please enter a value of type {col_dtype}.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # Create buttons with styles
    button_info = widgets.Button(description="Info", button_style='info')
    button_describe = widgets.Button(description="Describe", button_style='info')
    button_head = widgets.Button(description="Head", button_style='info')
    button_tail = widgets.Button(description="Tail", button_style='info')
    button_shape = widgets.Button(description="Shape", button_style='info')
    button_columns = widgets.Button(description="Columns", button_style='info')
    button_nunique = widgets.Button(description="Nunique", button_style='info')
    button_dtypes = widgets.Button(description="Dtypes", button_style='info')
    button_missing_data = widgets.Button(description="Missing Data", button_style='warning')
    button_duplicates = widgets.Button(description="Duplicates", button_style='warning')
    button_value_counts = widgets.Button(description="Value Counts", button_style='primary')
    button_filter_data = widgets.Button(description="Filter Data", button_style='success')

    # Assign button click events
    button_info.on_click(show_info)
    button_describe.on_click(show_describe)
    button_head.on_click(show_head)
    button_tail.on_click(show_tail)
    button_shape.on_click(show_shape)
    button_columns.on_click(show_columns)
    button_nunique.on_click(show_nunique)
    button_dtypes.on_click(show_dtypes)
    button_missing_data.on_click(show_missing_data)
    button_duplicates.on_click(show_duplicates)
    button_value_counts.on_click(show_value_counts)
    button_filter_data.on_click(filter_data)

    # Layout the widgets
    row1 = widgets.HBox([button_info, button_describe, button_head, button_tail, button_shape])
    row2 = widgets.HBox([button_columns, button_nunique, button_dtypes, button_missing_data, button_duplicates])
    row3 = widgets.HBox([button_value_counts, column_select_single])
    row4 = widgets.HBox([button_filter_data, filter_column, filter_condition, filter_value])

    # Display the interface
    display(widgets.VBox([row1, row2, row3, row4]), output)

    
# under developpement 
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



# Ma superbe fonction interactive pour visualiser
def visual(df):
    output = widgets.Output()

    # List of type of plots, other graphs under developpement 
    list_plot = ['histogram', 'boxplot']  

    # Widget for select a type of plot
    plot_type_widget = widgets.Dropdown(
        options=list_plot,
        description='Plot Type:',
        value=None  # this code for non default selecltion
    )

    # Widgets for histogram
    columns_widget = widgets.SelectMultiple(options=df.columns, description='Select Columns:')
    bins_widget = widgets.IntSlider(value=10, min=1, max=50, step=1, description='Bins:')
    color_widget = widgets.ColorPicker(value='blue', description='Color:')
    figsize_widget_a = widgets.Text(value='5', description='Width:')
    figsize_widget_b = widgets.Text(value='5', description='Height:')
    title_widget = widgets.Text(value='Histogram', description='Title:')
    save_widget = widgets.Checkbox(value=False, description='Save Figure')
    filename_widget = widgets.Text(value='histogram.png', description='Filename:')

    # Widgets for boxplot
    box_title_widget = widgets.Text(value='Box Plot', description='Title:')
    x_column_widget = widgets.Dropdown(options=df.columns, description='X Axis:')
    y_column_widget = widgets.Dropdown(options=df.columns, description='Y Axis:')
    hue_widget = widgets.Dropdown(options=[None] + list(df.columns), description='Hue:')
    box_figsize_widget_a = widgets.Text(value='5', description='Width:')
    box_figsize_widget_b = widgets.Text(value='5', description='Height:')
    box_save_widget = widgets.Checkbox(value=False, description='Save Figure')
    box_filename_widget = widgets.Text(value='boxplot.png', description='Filename:')

    # Fonction executed when we select a type of graph
    def on_plot_type_change(change):
        with output:
            clear_output()  # Efface tout le précédent affichage avant d'afficher les nouveaux widgets
            selected_plot = plot_type_widget.value

            if selected_plot == 'histogram':
                # display histogram's widgets
                display(widgets.HBox([
                    widgets.VBox([columns_widget,title_widget, filename_widget,save_widget]),
                    widgets.VBox([figsize_widget_b,figsize_widget_a,  bins_widget, color_widget])
                ]))
                # generate histogram button
                button = widgets.Button(description="Generate Histogram")
                button.on_click(on_button_click_histogram)
                display(button)
            elif selected_plot == 'boxplot':
                # display boxplot widget
                display(widgets.HBox([
                    widgets.VBox([box_title_widget, x_column_widget, y_column_widget]),
                    widgets.VBox([hue_widget, box_figsize_widget_a, box_figsize_widget_b]),
                    widgets.VBox([box_save_widget, box_filename_widget])
                ]))
                # generate a boxplot button
                button = widgets.Button(description="Generate Box Plot")
                button.on_click(on_button_click_boxplot)
                display(button)

    # Function for generate histogram when boutton is clicked
    def on_button_click_histogram(b):
        with output:
            clear_output()  # clear outputs before each click
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

            # Generate an histogram for each columns
            plt.figure(figsize=(width, height * len(selected_columns)))
            for i, col in enumerate(selected_columns, 1):
                plt.subplot(len(selected_columns), 1, i)
                df[col].hist(bins=bins, color=color)
                plt.title(f"{title} - {col}")
                plt.xlabel(col)
                plt.ylabel('Frequency')

            plt.tight_layout()

            if save_option and filename:
                plt.savefig(filename)
                print(f"Figure saved as {filename}")

            plt.show()

    # Function for generate boxplot when boutton is clicked
    def on_button_click_boxplot(b):
        with output:
            clear_output()
            try:
                width = int(box_figsize_widget_a.value)
                height = int(box_figsize_widget_b.value)
            except ValueError:
                print("Please enter valid numbers for figsize.")
                return
            
            title = box_title_widget.value
            x_column = x_column_widget.value
            y_column = y_column_widget.value
            hue = hue_widget.value
            save_option = box_save_widget.value
            filename = box_filename_widget.value if save_option else ""
            
            plt.figure(figsize=(width, height))
            sns.boxplot(x=x_column, y=y_column, data=df, hue=hue if hue != 'None' else None)
            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            
            if save_option and filename:
                plt.savefig(filename)
                print(f"Figure saved as {filename}")
            
            plt.show()

    # the methode observe is a function which execute the selection when we change a plot automatically without restarting executing the function pa.visual()
    plot_type_widget.observe(on_plot_type_change, names='value')

    # Afficher le widget de sélection du type de graphique
    display(plot_type_widget, output)
# visual v2
def visual_v2(df):
    output = widgets.Output()
    def on_button_hist(b):
        with output:
            clear_output()  
            # Ne pas redéfinir output ici, utiliser celui déjà créé dans visual
        
            # Widgets pour histogramme
            columns_widget = widgets.SelectMultiple(options=df.columns, description='Columns:')
            bins_widget = widgets.IntSlider(value=10, min=1, max=50, step=1, description='Bins:')
            color_widget = widgets.ColorPicker(value='blue', description='Color:')
            figsize_widget_a = widgets.Text(value='5', description='Width:')
            figsize_widget_b = widgets.Text(value='5', description='Height:')
            title_widget = widgets.Text(value='Histogram', description='Title:')
            save_widget = widgets.Checkbox(value=False, description='Save Figure')
            filename_widget = widgets.Text(value='histogram.png', description='Filename:')
            
            title_hbox = widgets.VBox([title_widget, columns_widget, bins_widget])
            color_figsize_hbox = widgets.VBox([color_widget, figsize_widget_a, figsize_widget_b])
            save_hbox = widgets.VBox([save_widget, filename_widget])
            all_v_box = widgets.HBox([title_hbox, color_figsize_hbox, save_hbox])
            display(all_v_box)
        
            def on_button_click(b):
                with output:
                    clear_output()  # Clear previous output before displaying new content
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
                    
                    # Create a copy of the original df
                    df_temp = df.copy()
                    
                    # Factoriser les colonnes non numériques
                    for col in selected_columns:
                        if not pd.api.types.is_numeric_dtype(df_temp[col]):
                            df_temp[col] = df_temp[col].astype('category').cat.codes
                            print(f"Column '{col}' has been factorized.")
                    
                    plt.figure(figsize=(width, height * len(selected_columns)))
                    
                    for i, col in enumerate(selected_columns, 1):
                        plt.subplot(len(selected_columns), 1, i)
                        df_temp[col].hist(bins=bins, color=color)
                        plt.title(f"{title} - {col}")
                        plt.xlabel(col)
                        plt.ylabel('Frequency')
                    
                    plt.tight_layout()

                    if save_option and filename:
                        plt.savefig(filename)
                        print(f"Figure saved as {filename}")

                    plt.show()
        
            button = widgets.Button(description="Generate Histogram")
            button.on_click(on_button_click)
            display(button, output)
  
    button_hist = widgets.Button(description="Histogram")
    button_hist.on_click(on_button_hist)

    # Layout des boutons
    buttons_row1 = widgets.HBox([button_hist])
    buttons_layout = widgets.VBox([buttons_row1])
  
    display(buttons_layout, output)





    
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
    color_figsize_hbox = widgets.VBox([color_widget, figsize_widget_a, figsize_widget_b])
    save_hbox = widgets.VBox([save_widget, filename_widget])
    all_v_box = widgets.HBox([title_hbox, color_figsize_hbox, save_hbox])
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
            
            # Create a copy of the original df.
            df_temp = df.copy()
            # Check and factorize non-numeric columns pd (pandas), api.types() is module from pandas, and it's works with pandas types (df or series)
            # is numeric_dtype it's a function that return a booelan, true if there is numeric value false if not
            for col in selected_columns:
                if not pd.api.types.is_numeric_dtype(df_temp[col]):
                    df_temp[col] = df_temp[col].astype('category').cat.codes
                    print(f"Column '{col}' has been factorized.")
            
            # create a histogram for each columns.
            plt.figure(figsize=(width, height * len(selected_columns)))

            for i, col in enumerate(selected_columns, 1):
                plt.subplot(len(selected_columns), 1, i)  # Créez un subplot pour chaque colonne
                df_temp[col].hist(bins=bins, color=color)
                plt.title(f"{title} - {col}")
                plt.xlabel(col)
                plt.ylabel('Frequency')

            plt.tight_layout()  # Ajuste les espacements entre les subplots

            if save_option and filename:
                plt.savefig(filename)
                print(f"Figure saved as {filename}")

            plt.show()
    
    button = widgets.Button(description="Generate Histogram")
    button.on_click(on_button_click)
    display(button, output)


# fonction historgram pour la fonction visual ""under developpements""
def histograme_v1(df):
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
    color_figsize_hbox = widgets.VBox([color_widget, figsize_widget_a, figsize_widget_b])
    save_hbox = widgets.VBox([save_widget, filename_widget])
    all_v_box = widgets.HBox([title_hbox, color_figsize_hbox, save_hbox])
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
            
            # Create a copy of the original df.
            df_temp = df.copy()
            # Check and factorize non-numeric columns pd (pandas), api.types() is module from pandas, and it's works with pandas types (df or series)
            # is numeric_dtype it's a function that return a booelan, true if there is numeric value false if not
            for col in selected_columns:
                if not pd.api.types.is_numeric_dtype(df_temp[col]):
                    df_temp[col] = df_temp[col].astype('category').cat.codes
                    print(f"Column '{col}' has been factorized.")
            
            # create a histogram for each columns.
            plt.figure(figsize=(width, height * len(selected_columns)))

            for i, col in enumerate(selected_columns, 1):
                plt.subplot(len(selected_columns), 1, i)  # Créez un subplot pour chaque colonne
                df_temp[col].hist(bins=bins, color=color)
                plt.title(f"{title} - {col}")
                plt.xlabel(col)
                plt.ylabel('Frequency')

            plt.tight_layout()  # Ajuste les espacements entre les subplots

            if save_option and filename:
                plt.savefig(filename)
                print(f"Figure saved as {filename}")

            plt.show()
    
    button = widgets.Button(description="Generate Histogram")
    button.on_click(on_button_click)
    display(button)
    # Mon SUPER generateur de HEATMAP *==HASSENE==* ""under developpements""

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
    


# Functions to replace missing values
def fillna_mean(df, inplace=False):
    if inplace:
        df.fillna(df.mean(), inplace=True)
    else:
        return df.fillna(df.mean())

def fillna_af(df, inplace=False):
    if inplace:
        df.fillna(method='ffill', inplace=True)
    else:
        return df.fillna(method='ffill')

def fillna_bf(df, inplace=False):   
    if inplace:
        df.fillna(method='bfill', inplace=True)
    else:
        return df.fillna(method='bfill')

def fillna_mode(df, inplace=False):
    if inplace:
        df.fillna(df.mode().iloc[0], inplace=True)
    else:
        return df.fillna(df.mode().iloc[0])
    
# MY SUPER Function for managing missing values

def missing_value_manager_previous(df):
    # Widget to select columns
    columns_tooltip = widgets.Label(value="Select columns from the list")
    # columns_tooltip = widgets.HTML(
    # value="<span style='color: gray; font-size: 12px;'>Select columns from the list</span>"
    # )
    columns_widget = widgets.SelectMultiple(
        options=df.columns,
        description='Columns:',
        disabled=False
    )
    
    # Buttons with tooltips added





    # Buttons for the different replacement methods with uniform width
    button_mean = widgets.Button(description="Replace with Mean", icon='arrow-right', layout=widgets.Layout(width='230px', height='40px'), tooltip="Select columns first, then replace missing values with the mean.")
    button_af = widgets.Button(description="Replace with Previous Value", layout=widgets.Layout(width='230px', height='40px'), tooltip="Select columns first, then replace missing values with the previous value.")
    button_bf = widgets.Button(description="Replace with Next Value", layout=widgets.Layout(width='230px', height='40px'), tooltip="Select columns first, then replace missing values with the next value.")
    button_mode = widgets.Button(description="Replace with Mode", layout=widgets.Layout(width='230px', height='40px'), tooltip="Select columns first, then replace missing values with the mode.")
    
    # Button to display columns with missing values
    button_isna = widgets.Button(description="Show Missing Values", icon="search", layout=widgets.Layout(width='230px', height='40px'), tooltip="Show missing values and their percentage for each column.")
    
    # FloatSlider to select the percentage of NaN above which to remove columns
    slider_taux = widgets.FloatSlider(value=50, min=0, max=100, step=1, description='NaN Rate (%)', layout=widgets.Layout(width='500px'), tooltip="Select a MAX percentage of missing values above which the columns will be deleted.")
    
    # Button to delete columns with NaN percentage >= the selected threshold
    button_delete = widgets.Button(description="Delete Columns", icon='trash', layout=widgets.Layout(width='230px', height='40px'), tooltip="Delete columns with missing values based on the selected NaN percentage threshold.")
    
    # Widget output to display results
    output = widgets.Output()
    
    # Organizing widgets in rows and columns
    button_row1 = widgets.HBox([button_bf, button_af, button_mean, button_mode])  # Group replacement buttons in one row
    button_row2 = widgets.HBox([button_isna, button_delete])  # Group buttons related to missing values on another row
    
    # Display widgets with clean and spaced layout
    display(widgets.VBox([columns_tooltip,columns_widget, slider_taux, button_row1, button_row2, output]))

    # Function to adjust the success message based on the number of columns
    def display_success_message(operator, selected_columns):
        if len(selected_columns) == 1:
            print(f"{operator} has been successfully applied to the column: {selected_columns[0]}")
        else:
            print(f"{operator} has been successfully applied to the columns: {', '.join(selected_columns)}")

    # Function to apply a replacement method and display the result
    def apply_and_display(replacement_fn, operator):
        selected_columns = list(columns_widget.value)
        
        # Check if replacement_fn is fillna_mean
        if replacement_fn == fillna_mean:
            # Check if all selected columns are numeric
            if not all([pd.api.types.is_numeric_dtype(df[col]) for col in selected_columns]):
                with output:
                    clear_output()
                    print("Error: Please select only numeric columns to apply the mean.")
                return  # Stop execution if a non-numeric column is selected
        
        if selected_columns:
            df[selected_columns] = replacement_fn(df[selected_columns])
            with output:
                clear_output()
                display_success_message(operator, selected_columns)  # Display success message
        else:
            with output:
                clear_output()
                print("No column selected.")
    
    # Function to display columns with missing values
    def show_isna(b):
        with output:
            clear_output()  # Clear previous output
            missing_columns = df.columns[df.isna().sum() > 0]
            if len(missing_columns) > 0:
                result = df.isna().sum()  # Number of NaN per column
                total = len(df)  # Total number of rows
                missing_data = pd.DataFrame({
                    'Number of NaN': result[missing_columns],
                    'Percentage of NaN (%)': (result[missing_columns] / total) * 100
                })
                display(missing_data)
            else:
                print("No missing values in this DataFrame.")
    
    # Function to delete columns with a NaN percentage greater than or equal to the selected threshold
    def delete_columns(b):
        threshold = slider_taux.value  # Get the value from the slider
        result = df.isna().sum()  # Number of NaN per column
        total = len(df)  # Total number of rows
        with output:
            clear_output()
            columns_to_delete = [col for col in df.columns if (result[col] / total) * 100 >= threshold]
            if columns_to_delete:
                for col in columns_to_delete:
                    df.drop(columns=[col], inplace=True)
                    print(f"Column '{col}' deleted (NaN rate >= {threshold}%)")
            else:
                print(f"No column with a NaN rate greater than or equal to {threshold}%")

    # Associate buttons with functions with customized messages
    button_mean.on_click(lambda b: apply_and_display(fillna_mean, "Mean"))
    button_af.on_click(lambda b: apply_and_display(fillna_af, "Previous Value"))
    button_bf.on_click(lambda b: apply_and_display(fillna_bf, "Next Value"))
    button_mode.on_click(lambda b: apply_and_display(fillna_mode, "Mode"))
    button_isna.on_click(show_isna)
    button_delete.on_click(delete_columns)

# seconde version of the missing_value_manager() function
def fillna_method(df, columns, method, value=None):
    """
    Replaces missing values in specified columns using the given method.
    """
    if method in ['mean', 'median', 'mode']:
        fill_values = {}
        for col in columns:
            if method == 'mean':
                fill_values[col] = df[col].mean()
            elif method == 'median':
                fill_values[col] = df[col].median()
            elif method == 'mode':
                mode_series = df[col].mode()
                if not mode_series.empty:
                    fill_values[col] = mode_series.iloc[0]
                else:
                    continue  # If mode is empty, skip filling this column
        df.fillna(value=fill_values, inplace=True)
    elif method == 'ffill':
        df[columns] = df[columns].fillna(method='ffill')
    elif method == 'bfill':
        df[columns] = df[columns].fillna(method='bfill')
    elif method == 'custom':
        df[columns] = df[columns].fillna(value)
    return df

def missing_value_manager(df):
    """
    Interactive widget to manage missing values in a DataFrame.
    """
    # Copy of the original DataFrame
    df_original = df.copy()
    
    # Output widget
    output = widgets.Output()
    
    # Column selection widget
    columns_widget = widgets.SelectMultiple(
        options=df.columns.tolist(),
        description='Columns:',
        disabled=False
    )
    
    # Replacement method selection
    method_widget = widgets.Dropdown(
        options=['Mean', 'Median', 'Mode', 'Forward Fill', 'Backward Fill', 'Custom Value'],
        description='Method:',
        disabled=False
    )
    
    # Custom value input
    custom_value_widget = widgets.Text(
        value='',
        description='Custom Value:',
        disabled=False
    )
    
    # Slider for NaN threshold
    threshold_slider = widgets.FloatSlider(
        value=50,
        min=0,
        max=100,
        step=1,
        description='NaN Threshold (%):',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.0f',
        tooltip='Select the maximum acceptable percentage of missing values; columns exceeding this will be deleted.'
    )
    
    # Buttons
    replace_button = widgets.Button(
        description='Replace Missing Values',
        button_style='success',
        tooltip='Replace missing values in selected columns using the chosen method.'
    )
    
    delete_columns_button = widgets.Button(
        description='Delete Columns',
        button_style='danger',
        tooltip='Delete columns with missing value percentage equal to or above the threshold.'
    )
    
    delete_rows_button = widgets.Button(
        description='Delete Rows',
        button_style='danger',
        tooltip='Delete rows containing any missing values.'
    )
    
    show_missing_button = widgets.Button(
        description='Show Missing Data',
        button_style='info',
        tooltip='Display missing values per column with percentages.'
    )
    
    reset_button = widgets.Button(
        description='Reset DataFrame',
        button_style='warning',
        tooltip='Reset the DataFrame to its original state.'
    )
    
    show_summary_button = widgets.Button(
        description='Show Summary',
        button_style='',
        tooltip='Display summary statistics of the DataFrame.'
    )
    
    # Function to update custom value widget visibility
    def update_custom_value_widget(*args):
        if method_widget.value == 'Custom Value':
            custom_value_widget.layout.display = 'block'
        else:
            custom_value_widget.layout.display = 'none'
    
    method_widget.observe(update_custom_value_widget, 'value')
    update_custom_value_widget()
    
    # Function to replace missing values
    def replace_missing_values(b):
        selected_columns = list(columns_widget.value)
        method = method_widget.value.lower().replace(' ', '')
        custom_value = custom_value_widget.value
        with output:
            clear_output()
            if not selected_columns:
                print("Please select at least one column.")
                return
            try:
                if method == 'customvalue':
                    if custom_value == '':
                        print("Please enter a custom value.")
                        return
                    fill_values = {}
                    for col in selected_columns:
                        col_dtype = df[col].dtype
                        if pd.api.types.is_numeric_dtype(col_dtype):
                            try:
                                fill_values[col] = float(custom_value)
                            except ValueError:
                                print(f"Error: Cannot convert custom value to numeric type for column '{col}'.")
                                return
                        else:
                            fill_values[col] = custom_value
                    df.fillna(value=fill_values, inplace=True)
                    print(f"Missing values in {selected_columns} replaced with custom value '{custom_value}'.")
                else:
                    if method not in ['mean', 'median', 'mode', 'ffill', 'bfill']:
                        print("Invalid method selected.")
                        return
                    # Check data types for mean and median
                    if method in ['mean', 'median']:
                        non_numeric_cols = [col for col in selected_columns if not pd.api.types.is_numeric_dtype(df[col])]
                        if non_numeric_cols:
                            print(f"Cannot apply {method} to non-numeric columns: {non_numeric_cols}")
                            return
                    # Call the updated fillna_method
                    fillna_method(df, selected_columns, method)
                    print(f"Missing values in {selected_columns} replaced using method '{method_widget.value}'.")
            except Exception as e:
                print(f"An error occurred: {e}")
    
    # Function to delete columns based on NaN threshold
    def delete_columns(b):
        threshold = threshold_slider.value
        with output:
            clear_output()
            missing_percent = df.isnull().mean() * 100
            columns_to_drop = missing_percent[missing_percent >= threshold].index.tolist()
            if columns_to_drop:
                df.drop(columns=columns_to_drop, inplace=True)
                print(f"Columns dropped (NaN >= {threshold}%): {columns_to_drop}")
            else:
                print(f"No columns to drop with NaN percentage >= {threshold}%.")
    
    # Function to delete rows with any missing values
    def delete_rows(b):
        with output:
            clear_output()
            initial_shape = df.shape
            df.dropna(inplace=True)
            final_shape = df.shape
            print(f"Rows before deletion: {initial_shape[0]}, after deletion: {final_shape[0]}")
    
    # Function to show missing data using df.isnull().sum()
    def show_missing_data(b):
        with output:
            clear_output()
            missing_data = df.isnull().sum()
            total_rows = df.shape[0]
            missing_percent = (missing_data / total_rows) * 100
            missing_df = pd.DataFrame({
                'Missing Values': missing_data,
                'Percentage of NaN (%)': missing_percent.round(2)
            })
            if missing_data.sum() == 0:
                print("No missing values in the DataFrame.")
            else:
                print("Missing values per column:")
                display(missing_df[missing_df['Missing Values'] > 0])
    
    # Function to reset the DataFrame
    def reset_dataframe(b):
        nonlocal df
        with output:
            clear_output()
            df = df_original.copy()
            print("DataFrame has been reset to its original state.")
    
    # Function to show summary statistics
    def show_summary(b):
        with output:
            clear_output()
            display(df.describe(include='all'))
    
    # Assign functions to button clicks
    replace_button.on_click(replace_missing_values)
    delete_columns_button.on_click(delete_columns)
    delete_rows_button.on_click(delete_rows)
    show_missing_button.on_click(show_missing_data)
    reset_button.on_click(reset_dataframe)
    show_summary_button.on_click(show_summary)
    
    # Layout
    controls = widgets.VBox([
        widgets.HBox([columns_widget, method_widget, custom_value_widget]),
        replace_button,
        widgets.HBox([threshold_slider, delete_columns_button]),
        widgets.HBox([delete_rows_button, show_missing_button, reset_button, show_summary_button]),
    ])
    
    display(controls, output)
