Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks =pd.read_csv(\"NFLX.csv\")\n",
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks=pd.read_csv(\"DJI.csv\")\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "5    2017-01-10  131.270004  132.220001  129.289993  129.889999  129.889999   \n",
      "6    2017-01-11  130.910004  131.500000  129.250000  130.500000  130.500000   \n",
      "7    2017-01-12  130.630005  130.850006  128.500000  129.179993  129.179993   \n",
      "8    2017-01-13  131.149994  133.929993  130.580002  133.699997  133.699997   \n",
      "9    2017-01-17  135.039993  135.399994  132.089996  132.889999  132.889999   \n",
      "10   2017-01-18  133.210007  133.649994  131.059998  133.259995  133.259995   \n",
      "11   2017-01-19  142.009995  143.460007  138.250000  138.410004  138.410004   \n",
      "12   2017-01-20  139.360001  140.789993  137.660004  138.600006  138.600006   \n",
      "13   2017-01-23  138.649994  139.490005  137.309998  137.389999  137.389999   \n",
      "14   2017-01-24  138.110001  140.929993  137.029999  140.110001  140.110001   \n",
      "15   2017-01-25  140.800003  141.389999  139.050003  139.520004  139.520004   \n",
      "16   2017-01-26  140.449997  141.210007  138.509995  138.960007  138.960007   \n",
      "17   2017-01-27  139.460007  142.490005  139.000000  142.449997  142.449997   \n",
      "18   2017-01-30  141.770004  141.970001  138.800003  141.220001  141.220001   \n",
      "19   2017-01-31  140.550003  141.830002  139.699997  140.710007  140.710007   \n",
      "20   2017-02-01  141.199997  142.410004  139.300003  140.779999  140.779999   \n",
      "21   2017-02-02  140.610001  141.039993  139.050003  139.199997  139.199997   \n",
      "22   2017-02-03  139.509995  140.639999  139.100006  140.250000  140.250000   \n",
      "23   2017-02-06  140.000000  141.000000  139.160004  140.970001  140.970001   \n",
      "24   2017-02-07  141.490005  144.279999  141.050003  144.000000  144.000000   \n",
      "25   2017-02-08  143.570007  145.070007  142.559998  144.740005  144.740005   \n",
      "26   2017-02-09  144.979996  145.089996  143.580002  144.139999  144.139999   \n",
      "27   2017-02-10  144.679993  145.300003  143.970001  144.820007  144.820007   \n",
      "28   2017-02-13  145.190002  145.949997  143.050003  143.199997  143.199997   \n",
      "29   2017-02-14  143.199997  144.110001  140.050003  140.820007  140.820007   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "221  2017-11-16  194.330002  197.699997  193.750000  195.509995  195.509995   \n",
      "222  2017-11-17  195.740005  195.949997  192.649994  193.199997  193.199997   \n",
      "223  2017-11-20  193.300003  194.320007  191.899994  194.100006  194.100006   \n",
      "224  2017-11-21  195.039993  197.520004  194.970001  196.229996  196.229996   \n",
      "225  2017-11-22  196.580002  196.750000  193.630005  196.320007  196.320007   \n",
      "226  2017-11-24  196.649994  196.899994  195.330002  195.750000  195.750000   \n",
      "227  2017-11-27  195.559998  195.850006  194.000000  195.050003  195.050003   \n",
      "228  2017-11-28  195.339996  199.679993  194.009995  199.179993  199.179993   \n",
      "229  2017-11-29  198.910004  199.029999  184.320007  188.149994  188.149994   \n",
      "230  2017-11-30  190.309998  190.860001  186.679993  187.580002  187.580002   \n",
      "231  2017-12-01  186.990005  189.800003  185.000000  186.820007  186.820007   \n",
      "232  2017-12-04  189.360001  189.720001  178.380005  184.039993  184.039993   \n",
      "233  2017-12-05  183.500000  188.139999  181.190002  184.210007  184.210007   \n",
      "234  2017-12-06  183.380005  186.479996  182.880005  185.300003  185.300003   \n",
      "235  2017-12-07  185.710007  187.339996  183.220001  185.199997  185.199997   \n",
      "236  2017-12-08  186.500000  189.419998  186.300003  188.539993  188.539993   \n",
      "237  2017-12-11  187.850006  189.419998  185.910004  186.220001  186.220001   \n",
      "238  2017-12-12  186.009995  187.850006  184.820007  185.729996  185.729996   \n",
      "239  2017-12-13  186.100006  188.690002  185.410004  187.860001  187.860001   \n",
      "240  2017-12-14  187.979996  192.639999  187.199997  189.559998  189.559998   \n",
      "241  2017-12-15  189.610001  191.429993  188.009995  190.119995  190.119995   \n",
      "242  2017-12-18  191.199997  191.649994  188.899994  190.419998  190.419998   \n",
      "243  2017-12-19  190.179993  190.300003  185.750000  187.020004  187.020004   \n",
      "244  2017-12-20  187.940002  189.110001  185.259995  188.820007  188.820007   \n",
      "245  2017-12-21  189.440002  190.949997  187.580002  188.619995  188.619995   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "5     5985800      Q1  \n",
      "6     5615100      Q1  \n",
      "7     5388900      Q1  \n",
      "8    10515000      Q1  \n",
      "9    12183200      Q1  \n",
      "10   16168600      Q1  \n",
      "11   23203400      Q1  \n",
      "12    9497400      Q1  \n",
      "13    7433900      Q1  \n",
      "14    7754700      Q1  \n",
      "15    7238100      Q1  \n",
      "16    6038300      Q1  \n",
      "17    8323900      Q1  \n",
      "18    8122500      Q1  \n",
      "19    4411600      Q1  \n",
      "20    6033400      Q1  \n",
      "21    3462400      Q1  \n",
      "22    3512600      Q1  \n",
      "23    3552100      Q1  \n",
      "24    8573500      Q1  \n",
      "25    6887100      Q1  \n",
      "26    4555100      Q1  \n",
      "27    6171900      Q1  \n",
      "28    4790400      Q1  \n",
      "29    8355000      Q1  \n",
      "..        ...     ...  \n",
      "221   5678400      Q4  \n",
      "222   3906300      Q4  \n",
      "223   3827500      Q4  \n",
      "224   4787300      Q4  \n",
      "225   5895400      Q4  \n",
      "226   2160500      Q4  \n",
      "227   3210100      Q4  \n",
      "228   6981100      Q4  \n",
      "229  14202700      Q4  \n",
      "230   6630100      Q4  \n",
      "231   6219500      Q4  \n",
      "232   9069800      Q4  \n",
      "233   5783700      Q4  \n",
      "234   5490100      Q4  \n",
      "235   4659500      Q4  \n",
      "236   4987300      Q4  \n",
      "237   5298600      Q4  \n",
      "238   4265900      Q4  \n",
      "239   4710000      Q4  \n",
      "240   7792800      Q4  \n",
      "241   7285600      Q4  \n",
      "242   5011000      Q4  \n",
      "243   7033000      Q4  \n",
      "244   6545400      Q4  \n",
      "245   4729800      Q4  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly=pd.read_csv(\"NFLX_daily_by_quarter.csv\")\n",
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#months for nflx and dji, daily for nflx_daily_by_quarter. There is an additional column for the quarter the date is in."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df =pd.read_csv(\"NFLX.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.rename(columns={'Adj Close' : 'Price'}, inplace=True)\n",
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dowjones_stocks.rename(columns={'Adj Close' : 'Price'}, inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns={'Adj Close' : 'Price'}, inplace=True)\n",
    "dowjones_stocks.head()\n",
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax=sns.violinplot(data=netflix_stocks_quarterly, x=\"Quarter\", y=\"Price\")\n",
    "ax.set_title(\"Distribution of Netflix Stock Prices by Quarter for 2017\")\n",
    "ax.set_ylabel(\"Closing Stock Price\")\n",
    "ax.set_xlabel(\"Business Quarters in 2017\")\n",
    "\n",
    "plt.savefig(\"Price_Dist_Violin.png\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "\n",
    "plt.scatter(chart_labels , earnings_actual, color=\"red\", alpha=0.5)\n",
    "plt.scatter(chart_labels , earnings_estimate, color=\"blue\", alpha=0.5)\n",
    "plt.legend([\"Actual\",\"Estimate\"])\n",
    "\n",
    "plt.xticks(range(len(earnings_actual)),chart_labels)\n",
    "plt.title(\"Earnings Per Share 2017: Actual Vs Estimates\")\n",
    "plt.xlabel(\"Quarters\")\n",
    "plt.ylabel(\"Cents Per Share\")\n",
    "\n",
    "plt.minorticks_on()\n",
    "plt.grid()\n",
    "\n",
    "plt.savefig(\"EPS.png\")\n",
    "\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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5s+fz+zZs9l88827Ohwza1KrRdPWkiVL6N+/v5PISpJE//79fSZnZoWsFokEcBJpJ9ebmRW12iQSMzPrGqvFNZJqw07+bYdOb+YZH221TLdu3dh6661ZunQpm2++OVdffTX9+vXr0DjMzFZFq2Ui6Qq9evVi6tT0GugjjzySCy64gG9961tdHJXZ6qWjDxJXVlsOKtdEbtoqwS677MKzz779Suazzz6bHXfckW222YbvfCe9dfeb3/wmF1544fIy48aN4wc/+EHd8jNnzmSrrbbi2GOPZcSIEey1114sXpyeyD569Ojlj42ZN28eLc8iW7ZsGV//+teXT+viiy8ufdnNbM3jRNLBli1bxh//+EcOPPBAAG699VZmzJjB/fffz9SpU5kyZQp33303Y8eOZcKE5W8J5rrrruOwww6rWx5gxowZfOlLX+LRRx+lX79+XH/99Q1jueyyy+jbty8PPPAADzzwAJdeeilPP/10eQtvZmskN211kMWLFzNy5EhmzpzJDjvswEc+8hEgJZJbb72V7bbbDoCFCxcyY8YMjj76aF588UWee+455s6dywYbbMCmm27KeeedV7P8pptuyuabb87IkSMB2GGHHZg5c2bDmG699VYefvhhJk6cCMCCBQuYMWOG/2fEzDqUE0kHablGsmDBAvbff38uuOACTjjhBCKCU045hc997nPvGGfMmDFMnDiR559/nrFjxwLULT9z5kzWWWed5d3dunVb3rTVvXt33nrrLYAV/ickIvjJT37C3nvv3eHLa2bWwk1bHaxv376cd955nHPOObz55pvsvffeXH755SxcuBCAZ599lhdffBGAsWPHcu211zJx4kTGjBkD0LB8PcOGDWPKlCkAy88+Wqb105/+lDfffBOAxx9/nEWLFnXsApvZGm+1PCPp6jsrtttuO7bddluuvfZaPvWpTzF9+nR22WUXAHr37s3Pf/5zNtpoI0aMGMFrr73GkCFDGDRoEAB77bVXzfLdunWrO7+vfe1rHH744Vx99dXsvvvuy/sfc8wxzJw5k+23356IYODAgdx4440lLrmZrYma7p3to0aNiuoXW02fPp2tttqqiyJqfq4/axa+/bf9JE2JiFFlTLu0pi1JPSXdL+khSY9KOr1GmaMkzZU0NX+OKSseMzMrR5lNW28Au0fEQkk9gHsk/S4i7q0qNyEiji8xDjMzK1FpiSRSm9nC3Nkjf5qrHc3MzFpV6l1bkrpJmgq8CNwWEffVKHaopIclTZS0SZ3pHCdpsqTJc+fOLTNkMzNbSaUmkohYFhEjgaHATpLeX1XkJmBYRGwD3A5cWWc6l0TEqIgYNXDgwDJDNjOzldQp/0cSEa8AdwL7VPWfHxFv5M5LgR06Ix4zM+s4pV0jkTQQeDMiXpHUC9gTOLOqzKCImJM7DwSmd8jMx/XtkMm8Pb0FrRZpeYx8i7Fjx3LyyScXnvVzzz3HCSecsMI/GpqZrUrKvGtrEHClpG6kM5/rIuJmSeOByRExCThB0oHAUuAl4KgS4ylV5WPkV9bSpUvp3r32TzF48GAnETNbpZV519bDwHY1+p9W8f0U4JSyYlgVjB8/nptuuonFixez6667cvHFFyOJ0aNHs+uuu/KXv/yFAw88kEceeYT111+fyZMn8/zzz3PWWWcxZswYZs6cyf7778+0adO44oormDRpEq+//jpPPvkkhxxyCGeddRaQnvR75plnMnjwYLbcckvWWWcdzj//fH71q19x+umn061bN/r27bv8ScJmZh3Fz9rqIC1P/235tDwi/vjjj+eBBx5g2rRpLF68mJtvvnn5OK+88gp33XUXJ510EgBz5szhnnvu4eabb67bLDZ16lQmTJjAI488woQJE5g1axbPPfcc3/3ud7n33nu57bbbeOyxx5aXHz9+PH/4wx946KGHmDRpUok1YGZrqtXyWVtdoV7T1h133MFZZ53F66+/zksvvcSIESM44IADAPj4xz++QtmDDz6YtdZai+HDh/PCCy/UnM8ee+xB377pGtDw4cN55plnmDdvHh/+8IfZcMMNATjssMN4/PHHAdhtt9046qijOPzww/nYxz7WYctrZtbCZyQlWrJkCV/84heZOHEijzzyCMcee+wKj3lfb731Vihf+Zj4es9Aq36U/NKlS+uWBbjooov43ve+x6xZsxg5ciTz589v7+KYmdXkRFKilqQxYMAAFi5cWNpF85122om77rqLl19+maVLl67w5sQnn3ySnXfemfHjxzNgwABmzZpVSgxmtuZaPZu22nC7bkdruUbSYp999uGMM87g2GOPZeutt2bYsGHsuOOOpcx7yJAhnHrqqey8884MHjyY4cOHL2/++vrXv86MGTOICPbYYw+23XbbUmIwszWXHyO/mli4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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "plt.bar(bars1_x, revenue_by_quarter)\n",
    "\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "plt.bar(bars2_x, earnings_by_quarter)\n",
    "\n",
    "\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.legend(labels)\n",
    "\n",
    "plt.title(\"Revenue and Earnings: Can Strong Margin Growth Continue?\")\n",
    "plt.xlabel(\"Quarters\")\n",
    "plt.ylabel(\"Billion USD\")\n",
    "\n",
    "\n",
    "plt.savefig(\"Revenue_Earnings.png\")\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1) Revenue Growing.\n",
    "# 2) Earnings Growing.\n",
    "# 3) Roughly Between 2% and 8%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "\n",
    "netflix_stocks =pd.read_csv(\"NFLX.csv\")\n",
    "df.rename(columns={'Adj Close' : 'Price'}, inplace=True)\n",
    "#df.head()\n",
    "\n",
    "ax1=plt.subplot(1, 2, 1)\n",
    "ax1=plt.plot(netflix_stocks['Date'], netflix_stocks['Adj Close'], color='red')\n",
    "\n",
    "#months= range(12)\n",
    "#ax1.set_xticks(months)\n",
    "\n",
    "plt.title(\"Netflix\")\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Stock Price')\n",
    "\n",
    "\n",
    "\n",
    "plt.savefig(\"Netflix_Stock_Chart.png\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "\n",
    "ax2=plt.subplot(1,2,2)\n",
    "ax2=plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])\n",
    "\n",
    "plt.title(\"Dow Jones\")\n",
    "plt.xlabel(\"Date\")\n",
    "plt.ylabel(\"Index Value\")\n",
    "\n",
    "plt.subplots_adjust(wspace= 1)\n",
    "\n",
    "plt.savefig(\"Dow_Jones_Stock_Chart.png\")\n",
    "\n",
    "plt.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
