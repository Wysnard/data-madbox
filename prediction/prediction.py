# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
from fbprophet import Prophet
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'prediction'))
    print(os.getcwd())
except:
    pass
# %% [markdown]
# # Data Analysis and Prediction Notebook
# %% [markdown]
# ## Import library

# %%
from sqlalchemy import create_engine
import pandas as pd
import os
import matplotlib.pyplot as plt
import itertools
import statsmodels.api as sm
import datetime as dt
import time

# %% [markdown]
# ## Establish the Database connection

# %%
# wait for the databases and injector to be ready
time.sleep(30)

env_var = 'MY_SQL_IP'
database = "localhost" if env_var not in os.environ else os.environ['MY_SQL_IP']
db_connection_str = f"mysql+pymysql://vlay:123@{database}:3306/madbox"

# Retry to connect until we connect to the database
for i in range(20):
    try:
        db_connection = create_engine(db_connection_str)

        # Retrieve data from a select *
        sql_str = """
        SELECT * FROM madbox_api
        """

        # Put the data into a dataframe
        df = pd.read_sql(sql_str, db_connection)\
            .reset_index()\
            .assign(
            cmp=lambda x: x['spend'] / x['nb_impressions'],
            gpm=lambda x: x['profit'] / x['nb_impressions'],
            day_name=lambda x: x['date'].dt.weekday_name,
        )\
            .set_index(['date'])\
            .drop(['index'], axis='columns')
    except Exception as e:
        time.sleep(5)
        print(e)

df.assign(
    # recomputation of the metrics to understand how it works
    profit_calculated=lambda x: x['revenue'] - x['spend'],
    margin_calculated=lambda x: x['profit'] / x['revenue'],
    ecpm_calculated=lambda x: x['revenue'] / x['nb_impressions'] * 1000,
)


# %%
df.plot(subplots=True, figsize=(20, 20))
plt.show()


# %%
f = plt.figure(figsize=(19, 15))
plt.matshow(df.corr(), fignum=f.number)
plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=45)
plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)

# %% [markdown]
# ## Keeping only relevant data

# %%
df = df[['spend', 'revenue', 'nb_impressions']]

# %% [markdown]
# ## Facebook Prophet Model
# %% [markdown]
# ### Look for the optimal parameters

# %%

revenue = df['revenue'].reset_index().rename(
    columns={'date': 'ds', 'revenue': 'y'})
model = Prophet()
model.fit(revenue)
revenue_forecast = model.make_future_dataframe(periods=120, freq='D')
revenue_forecast = model.predict(revenue_forecast)
plt.figure(figsize=(30, 10))
model.plot(revenue_forecast, xlabel='Date', ylabel='revenue')
plt.title('Revenue Forecast')


# %%
revenue_forecast


# %%
model.plot_components(revenue_forecast)
plt.title('Revenue Forecast Components')


# %%
plt.figure(figsize=(20, 8))
plt.plot(revenue['ds'], revenue['y'], 'b-', label='observed')
plt.plot(revenue_forecast['ds'],
         revenue_forecast['yhat'], 'r-', label='predicted')
plt.plot(revenue_forecast['ds'],
         revenue_forecast['trend'], 'g-', label='trend')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.title('Revenue Graph')
plt.legend()

# %% [markdown]
# # Prediction

# %%
pred_lst = []
for col in list(df.columns):
    data = df[col].reset_index().rename(columns={'date': 'ds', col: 'y'})
    model = Prophet()
    model.fit(data)
    data_forecast = model.make_future_dataframe(periods=120, freq='D')
    data_forecast = model.predict(data_forecast)
    data_forecast = data_forecast                        .rename(
        {'ds': 'date', 'yhat': col, 'trend': col + '_trend'}, axis='columns')                        .set_index(['date'])[[col, col + '_trend']]
    pred_lst.append(data_forecast)

pred_df = pd.concat(pred_lst, axis='columns')
pred_df


# %%
trend_df = pred_df[:len(df)].drop(
    df.columns, axis='columns')            .assign(category='observed')
df = pd.concat([df, trend_df], axis='columns')

df


# %%
pred_df = pred_df[len(df):]            .assign(category='prediction')
pred_df


# %%
df = pd.concat([df, pred_df], axis='rows', sort=True)        .sort_index()
df


# %%
df.dtypes

# %% [markdown]
# # DataFrame into DataBase

# %%
df.to_sql('metrics', db_connection, if_exists='replace')
