# Tokocrypto To CoinTracker CSV

Simple App to convert **Tokocrypto Trade History** (XLS formata) to **CoinTracker (CSV format)**.

## What's Tokocrypto and CoinTracker

**Tokocrypto** is a one of the leading exchange in Indonesia with low fees and backed by Binance.

**CoinTracker** is a crypto portoflio tracker in realtime from your wallet and exchanges using API or CSV.

## Why do you need to use this?

If you use Tokocrypto and CoinTracker, chances are you need to import transaction manually.

Because (At the moment of writing of this) currently CoinTracker hasn't supported the integration to Tokocrypto via API. Which is very unfortunate.

But luckily, CoinTracker does **support importing transaction using CSV**. Which elliminate manual input.

## Prerequisite

- Python
- Pip

## Setup

1. Clone this repository

  ```{bash}
  $ git clone test
  ```

2. Install packages

```{bash}
$ cd tokocrypto-to-cointracker-csv
$ pip install -r requirement.txt
```

## How to use this package

### Get Tokocrypto XLS file

The one of closest list of data you can get is through Trade History

1. Make sure you are logged in
2. Go to [Trade History](https://www.tokocrypto.com/en/usercenter/history/user-trade)
3. Click **Export complete trade history** on the right top of the table
4. Download the file

### Convert file

Convert file straight you just downloaded from Tokocrypto Trade History to CoinTracker CSV.

```{bash}
$ python main.py --source <source> --destination <destination>
```

Example:

```{bash}
$ python main.py --source tokocrypto.xls --destination tokocrypto-cointracker.csv
```

### Upload your file to CoinTracker

1. Make sure you are logged in to CoinTracker
2. Go to [Add wallet CSV](https://www.cointracker.io/add_wallet?t=csv)
3. Drag and drop the file that has been generated
4. Click Import

---

### Want to use Tokocrypto? or CoinTracker?

Please consider using my referal:

- [Tokocrypto](https://www.tokocrypto.com/account/signup?ref=6V38PNT3)
- [CoinTracker (Get $10)](https://www.cointracker.io/i/VbadXEmcWsFH)

---

Made with ❤️ by [JustArya](https://github.com/justarya)
