import pandas as pd
import typer
import datetime

app = typer.Typer()

def fix_year(date):
  invalid_year = 1900
  this_year = datetime.datetime.now().year
  if date.year == invalid_year:
    date = date.replace(year = this_year)
  return date

def convert_string_to_float(series):
  return series\
    .apply(lambda x: x.replace(',', ''))\
    .astype(float)

@app.command()
def convert(
  source: str = typer.Option(..., help='Source Tokocrypto file'),
  destination: str = typer.Option('./tokocrypto_cointracker.csv', help='Destination CoinTracker CSV file'),
):
  """
  Convert Tokocrypto trade history XLS to CoinTracker CSV format
  """

  df_tko = pd.read_excel(source)
  df_tko['Time'] = pd.to_datetime(df_tko['Time'], format='%m-%d %H:%M:%S')
  df_tko['Time'] = df_tko['Time'].apply(fix_year)
  df_tko[['Pair To', 'Pair From']] = df_tko['Pair'].str.split('/', 1, expand = True)
  df_tko[['Fee Amount', 'Fee Currency']] = df_tko['Trading Fees'].str.split(' ', 1, expand = True)
  df_tko[['Total Amount', 'Total Currency']] = df_tko['Total'].str.split(' ', 1, expand = True)
  df_tko['Price'] = convert_string_to_float(df_tko['Price'])
  df_tko['Total Amount'] = convert_string_to_float(df_tko['Total Amount'])
  df_tko['Fee Amount'] = convert_string_to_float(df_tko['Fee Amount'])

  df_result = pd.DataFrame({
    'Date': df_tko['Time'],
    'Received Quantity': df_tko['Filled'],
    'Received Currency': df_tko['Pair To'],
    'Sent Quantity': df_tko['Total Amount'],
    'Sent Currency': df_tko['Total Currency'],
    'Fee Amount': df_tko['Fee Amount'],
    'Fee Currency': df_tko['Fee Currency'],
    'Tag': ''
  })

  df_result.set_index('Date', inplace=True)

  df_result.to_csv(destination, sep=',', encoding='utf-8')
  print(f'Successfully convert Tokocrypto to Cointracker in {destination}')

if __name__ == "__main__":
  app()
