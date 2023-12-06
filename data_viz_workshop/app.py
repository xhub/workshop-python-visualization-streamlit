import streamlit as st
import pandas as pd
import plotly.express as px

# This must be the first streamlit call!!
st.set_page_config(layout="wide")

st.title("Interact with Gapminder Data")

df = pd.read_csv("gapminder_tidy.csv")
continent_list = list(df.continent.unique())
metric_list = list(df.metric.unique())


metric_labels = {"gdpPercap": "GDP per Capita", "lifeExp": "Average life expectancy", "pop": "Population"}
metric2labels = lambda x: metric_labels[x]

continent = 'Europe'
metric = 'gdpPercap'

show_data = True

# widgets
with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list, format_func=metric2labels)



new_query = f"continent == '{continent}' & metric == '{metric}'"

metric_nice = metric_labels[metric]

df_filtered = df.query(new_query)



title = f"{metric_nice} in {continent}"

fig = px.line(df_filtered, x = "year", y = "value", color = 'country', labels={"value": metric_nice, "country": "Country"}, title = title)
fig.update_traces(mode='markers+lines')

#st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:. So cool')

st.plotly_chart(fig, use_container_width=True)

st.markdown(f"This plot shows the {metric_nice} for countries in {continent}")

st.markdown(f"Pandas dataframe for query '{new_query}'")


if show_data:
    st.dataframe(df_filtered, use_container_width=True)