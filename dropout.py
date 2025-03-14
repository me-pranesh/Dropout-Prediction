{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "582bc632",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ab91e12",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "4d82eb3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "0344f9ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('drop.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "03d3a448",
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
       "      <th>access</th>\n",
       "      <th>tests</th>\n",
       "      <th>tests_grade</th>\n",
       "      <th>exam</th>\n",
       "      <th>project</th>\n",
       "      <th>project_grade</th>\n",
       "      <th>assignments</th>\n",
       "      <th>result_points</th>\n",
       "      <th>result_grade</th>\n",
       "      <th>graduate</th>\n",
       "      <th>year</th>\n",
       "      <th>acad_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1256</td>\n",
       "      <td>57.00</td>\n",
       "      <td>A</td>\n",
       "      <td>19</td>\n",
       "      <td>91.54</td>\n",
       "      <td>A</td>\n",
       "      <td>40.0</td>\n",
       "      <td>189.92</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>2019</td>\n",
       "      <td>2019/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>985</td>\n",
       "      <td>42.87</td>\n",
       "      <td>B</td>\n",
       "      <td>19</td>\n",
       "      <td>75.96</td>\n",
       "      <td>A</td>\n",
       "      <td>13.7</td>\n",
       "      <td>189.43</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>2017/2018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1455</td>\n",
       "      <td>54.50</td>\n",
       "      <td>A</td>\n",
       "      <td>16</td>\n",
       "      <td>96.79</td>\n",
       "      <td>A</td>\n",
       "      <td>40.0</td>\n",
       "      <td>188.91</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>2019</td>\n",
       "      <td>2019/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>998</td>\n",
       "      <td>54.50</td>\n",
       "      <td>A</td>\n",
       "      <td>16</td>\n",
       "      <td>93.36</td>\n",
       "      <td>A</td>\n",
       "      <td>40.0</td>\n",
       "      <td>186.85</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>2019</td>\n",
       "      <td>2019/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1347</td>\n",
       "      <td>55.00</td>\n",
       "      <td>A</td>\n",
       "      <td>16</td>\n",
       "      <td>92.86</td>\n",
       "      <td>A</td>\n",
       "      <td>39.0</td>\n",
       "      <td>186.38</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>2019</td>\n",
       "      <td>2019/2020</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   access  tests tests_grade  exam  project project_grade  assignments  \\\n",
       "0    1256  57.00           A    19    91.54             A         40.0   \n",
       "1     985  42.87           B    19    75.96             A         13.7   \n",
       "2    1455  54.50           A    16    96.79             A         40.0   \n",
       "3     998  54.50           A    16    93.36             A         40.0   \n",
       "4    1347  55.00           A    16    92.86             A         39.0   \n",
       "\n",
       "   result_points result_grade  graduate  year  acad_year  \n",
       "0         189.92            A         1  2019  2019/2020  \n",
       "1         189.43            A         1  2017  2017/2018  \n",
       "2         188.91            A         1  2019  2019/2020  \n",
       "3         186.85            A         1  2019  2019/2020  \n",
       "4         186.38            A         1  2019  2019/2020  "
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "72bf7e6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "access           0\n",
       "tests            0\n",
       "tests_grade      0\n",
       "exam             0\n",
       "project          0\n",
       "project_grade    0\n",
       "assignments      0\n",
       "result_points    0\n",
       "result_grade     0\n",
       "graduate         0\n",
       "year             0\n",
       "acad_year        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "9b2645a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 261 entries, 0 to 260\n",
      "Data columns (total 12 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   access         261 non-null    int64  \n",
      " 1   tests          261 non-null    float64\n",
      " 2   tests_grade    261 non-null    object \n",
      " 3   exam           261 non-null    int64  \n",
      " 4   project        261 non-null    float64\n",
      " 5   project_grade  261 non-null    object \n",
      " 6   assignments    261 non-null    float64\n",
      " 7   result_points  261 non-null    float64\n",
      " 8   result_grade   261 non-null    object \n",
      " 9   graduate       261 non-null    int64  \n",
      " 10  year           261 non-null    int64  \n",
      " 11  acad_year      261 non-null    object \n",
      "dtypes: float64(4), int64(4), object(4)\n",
      "memory usage: 24.6+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "164b6289",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A', 'B', 'C', 'E', 'D', 'FX', '0'], dtype=object)"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['tests_grade'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "3d253678",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A', 'B', 'C', 'D', 'E', 'FX'], dtype=object)"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['result_grade'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "5ee1ad4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A', 'C', 'D', 'FX', 'B', 'E', '0'], dtype=object)"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['project_grade'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "00de6ae4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2019/2020', '2017/2018', '2018/2019', '2016/2017'], dtype=object)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['acad_year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "4d931025",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.tests_grade.replace(('A', 'B', 'C', 'E', 'D', 'FX', '0'),(1,2,3,4,5,6,7),inplace=True)\n",
    "data.project_grade.replace(('A', 'B', 'C', 'E', 'D', 'FX', '0'),(1,2,3,4,5,6,7),inplace=True)\n",
    "data.result_grade.replace(('A', 'B', 'C', 'E', 'D', 'FX'),(1,2,3,4,5,6),inplace=True)\n",
    "data.acad_year.replace(('2019/2020', '2017/2018', '2018/2019', '2016/2017'),(1,2,3,4),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "54205b65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 261 entries, 0 to 260\n",
      "Data columns (total 12 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   access         261 non-null    int64  \n",
      " 1   tests          261 non-null    float64\n",
      " 2   tests_grade    261 non-null    int64  \n",
      " 3   exam           261 non-null    int64  \n",
      " 4   project        261 non-null    float64\n",
      " 5   project_grade  261 non-null    int64  \n",
      " 6   assignments    261 non-null    float64\n",
      " 7   result_points  261 non-null    float64\n",
      " 8   result_grade   261 non-null    int64  \n",
      " 9   graduate       261 non-null    int64  \n",
      " 10  year           261 non-null    int64  \n",
      " 11  acad_year      261 non-null    int64  \n",
      "dtypes: float64(4), int64(8)\n",
      "memory usage: 24.6 KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "a58498c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = data.drop(['access','graduate'], axis = 1)\n",
    "y = data['graduate']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "9ffef232",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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55u6deuaatWqOd5HycnJ5umnnzaSzNKlSx19pKSkZPueunz5somOjjb+/v7mtddeM+vWrTMvvPCC8fT0NJ07d85y/CIjI03jxo3Nhx9+aFavXm1at25tPD09ncY+O6dPnzblypUzZcqUMTNmzDBr1641Q4YMMZLMk08+aYwxJiUlxXz11VcmJCTENG/e3FH7lStXsu3zq6++Mr6+vqZz586Odfft22eMMebEiRMmPDzcREREmH/9619mw4YN5qWXXjJ2u908+uijjj4++OADx8/junXrzIYNG8yMGTPM0KFDc3VMspOQkGBGjhxpPvroI5OQkGCWLVtm7r//fuPr62u+//57x3qZ7+fIyEjTt29f88knn5gPPvjAVKhQwVSpUsVcv37dse6YMWOMJPPEE0+YNWvWmJkzZ5py5cqZkJAQp+OZk4iICBMTE+MY57lz5xpJ5h//+Idjn5KTk3N8/TfffGN8fHxMdHS0WbRokVmxYoXp3LmziYyMNJLMkSNHnLYVGhpqKlasaObMmWM2bdpkvv76a2OMMcOHDzfTp083a9euNRs3bjRvvPGGKV26tHnsscectpfb/b148aKpV6+eKV26tJk8ebLZsGGDmTJliilRooS57777TEZGxi3HBrePAHOHOHPmjLn33nuNJCPJeHl5mWbNmpn4+Hjzyy+/OK2bU4CpW7euSU9Pd7S/+eabRpLp3r270+uHDRtmJDn+8zLmt18uNpvN7Nmzx2nd9u3bm+LFi5uLFy86bev3AaZjx46mfPnyTv0ZY8yQIUOMj4+POXfu3E33XZIpUaJElvVy22/mL/wGDRo4/WJKSkoyXl5epn///o62mJgYI8nMmTPHqc/M/7A+/vhjp/bt27cbSWbatGnGGGM++ugjIynLOOWlL2N+G3cfHx9z9OhRR9vly5dNqVKlzMCBAx1tS5YsMZLMpk2bctyuMcZkZGSYa9eumaNHjxpJ5t///rdj2auvvprlP5VMN76nZsyYYSSZDz/80Gm9l19+2Ugy69atc7RJMmXLljWpqamOtpMnT5pixYqZ+Pj4m9Y7atQoI8ls27bNqf3JJ580NpvNHDhwwNEWERFhunTpctP+Mvn7+zv+Y/69gQMHmoCAAKfxNsaY1157zUhyBJ0hQ4aYu+6666bbyO0xycn169fN1atXTZUqVczw4cMd7Znv5xuD4ocffmgkma+++soYY8z58+eNj4+P6dmzp9N6//nPf4wklwOMMf97j/7+5/tmevfubfz9/c3PP//saEtPTzc1a9bMNsB4eHg4HdPspKenm2vXrpkFCxYYDw8Px8+5K/sbHx9vihUrZrZv3+60bubP7+rVq3O1f7g9XEK6QwQFBenzzz/X9u3bNWnSJPXo0UM//PCDYmNjVadOHafLATnp3Lmz0+WmGjVqSJK6dOnitF5m+7Fjx5zaa9Wqpbp16zq1PfTQQ0pNTdWuXbuy3eaVK1f02WefqWfPnvLz89P169cdU+fOnXXlyhVt3br1lrXfd999Klmy5G31+9BDD8lmsznmIyIi1KxZM23atCnL9nr16uU0v2rVKt11113q1q2b07bq1aunkJAQx6WWevXqydvbW3/96181f/58HT58OEvfue0rU7169VShQgXHvI+Pj6pWraqjR4/ectwk6fTp0xo0aJDCw8Pl6ekpLy8vRURESJK+++67XPVxo40bN8rf318PPPCAU3vm5YbPPvvMqb1NmzYKDAx0zJctW1bBwcG33IeNGzeqZs2aaty4cZbtGGO0cePGPNWfk1WrVqlNmzYKCwtzOjadOnWSJCUkJEiSGjdurAsXLujBBx/Uv//971z9/N3K9evXNXHiRNWsWVPe3t7y9PSUt7e3Dh48mO1x6t69u9N8dHS0JDnG9KuvvtKVK1fUt29fp/WaNWvmOP4FLSEhQffdd59Kly7taCtWrJj+/Oc/Z7t+dHS0qlatmqV99+7d6t69u4KCguTh4SEvLy898sgjSk9P1w8//CDJtf1dtWqVateurXr16jkd544dOzpdOkXBIsDcYRo1aqTnnntOS5Ys0U8//aThw4crKSkpy4282SlVqpTTvLe3903br1y54tQeEhKSpc/MtrNnz2a7zbNnz+r69et666235OXl5TR17txZknL1y//GJ0ry0m9O9d9Yu5+fn9OTF5J06tQpXbhwQd7e3lm2d/LkSce2KlWqpA0bNig4OFiDBw9WpUqVVKlSJU2ZMsXlvjIFBQVlqdtut+vy5cu3GjZlZGSoQ4cOWrp0qf7+97/rs88+09dff+0Id7npIztnz55VSEiIUyCUpODgYHl6emYZ07zuw9mzZ7N9migsLMyxPD+dOnVKK1euzHJcatWqJel/76l+/fppzpw5Onr0qHr16qXg4GA1adJE69evz/O2R4wYoRdeeEH333+/Vq5cqW3btmn79u2qW7dutuN045ja7XZJ/zummWNzs5/bgnb27FmVLVs2S3t2bVLWn3Pptz+kWrRooePHj2vKlCmOP+Qy73XLy/6eOnVKe/fuzXKcAwMDZYzJl0CKW+MppDuYl5eXxowZozfeeEPffvttgW/v5MmTObZl9x+UJJUsWVIeHh7q16+fBg8enO06UVFRt9z2jf9R5qXfnOq/sfYbtyVJpUuXVlBQkNauXZvttn5/dqFFixZq0aKF0tPTtWPHDr311lsaNmyYypYtqz59+rjU1+369ttv9c0332jevHmKiYlxtB86dOi2+g0KCtK2bdtkjHEar9OnT+v69etOf3Hf7nZOnDiRpf2nn36SpHzbTqbSpUsrOjpaEyZMyHZ5ZnCSfruR9bHHHtPFixe1ZcsWjRkzRl27dtUPP/yQpzMcCxcu1COPPKKJEyc6tZ85cybLY+25kfm+zul9XxiPdgcFBenUqVPZbj872f3sLV++XBcvXtTSpUudxvXGz6JxZX9Lly4tX19fp5vhfy+/31fIHgHmDnHixIls/zrJPLX8+1+sBWXfvn365ptvnC4jvf/++woMDFSDBg2yfY2fn5/atGmj3bt3Kzo62nF253blpd8PPvhAI0aMcPySPHr0qL788ks98sgjt3xt165dtWjRIqWnp6tJkya5qtHDw0NNmjRR9erV9d5772nXrl3q06dPnvq6lRv/+s6Uua+ZyzP961//ynUf2Wnbtq0+/PBDLV++XD179nS0L1iwwLE8P7Rt21bx8fHatWuX03tswYIFstlsatOmTZ76zensT9euXbV69WpVqlTJ6ZLlzfj7+6tTp066evWq7r//fu3bt08REREujaf027G68Th98sknOn78uCpXrpyrPn7vnnvukY+Pj9577z2nS6Jffvmljh49mqcA4+o+tWrVSqtXr9aZM2ccoSAjI0NLlizJ9Tazew8bYzRr1iyn9VzZ365du2rixIkKCgrK1R9QKBgEmDtEx44dVb58eXXr1k3Vq1dXRkaG9uzZo9dff10BAQF65plnCryGsLAwde/eXWPHjlVoaKgWLlyo9evX6+WXX77p56RMmTJF9957r1q0aKEnn3xSkZGR+uWXX3To0CGtXLkyz/cxuNrv6dOn1bNnTw0YMEApKSkaM2aMfHx8FBsbe8tt9enTR++99546d+6sZ555Ro0bN5aXl5f++9//atOmTerRo4d69uypGTNmaOPGjerSpYsqVKigK1euOP7Ka9eunUt9uaJ27dqSpJkzZyowMFA+Pj6KiopS9erVValSJY0aNUrGGJUqVUorV67M9lJHnTp1HOMaExMjLy8vVatWLdszQo888ojefvttxcTEKCkpSXXq1NEXX3yhiRMnqnPnzo59vV3Dhw/XggUL1KVLF40bN04RERH65JNPNG3aND355JPZ3i+RG3Xq1NHmzZu1cuVKhYaGKjAwUNWqVdO4ceO0fv16NWvWTEOHDlW1atV05coVJSUlafXq1ZoxY4bKly+vAQMGyNfXV82bN1doaKhOnjyp+Ph4lShRwvGocU7HJKezlV27dtW8efNUvXp1RUdHa+fOnXr11VdVvnz5PO1jyZIl9eyzz2r8+PHq37+/evfureTkZI0dOzbPl5AqVaokX19fvffee6pRo4YCAgIUFhaW4x9Qo0eP1sqVK9W2bVuNHj1avr6+mjFjhuNR5Rs/AiI77du3l7e3tx588EH9/e9/15UrVzR9+nSdP38+z/s7bNgwffzxx2rZsqWGDx+u6OhoZWRk6NixY1q3bp1GjhyZb39c4CbcegsxCs3ixYvNQw89ZKpUqWICAgKMl5eXqVChgunXr5/Zv3+/07o5PYX0+8edjfnf0wxLlixxas98VPL3d+hnPuHx0UcfmVq1ahlvb28TGRlpJk+e7PTa7J5Cymx//PHHTbly5YyXl5cpU6aMadasmRk/fvwt912SGTx4cLbLctNv5n6+++67ZujQoaZMmTLGbrebFi1amB07djj1FxMTY/z9/bPd1rVr18xrr71m6tata3x8fExAQICpXr26GThwoDl48KAx5rdHdHv27GkiIiKM3W43QUFBplWrVmbFihUu92VMzk/W3HiMjfntqbKoqCjj4eHhdAz2799v2rdvbwIDA03JkiVN7969zbFjx4wkM2bMGKc+YmNjTVhYmClWrJjTEzTZbe/s2bNm0KBBJjQ01Hh6epqIiAgTGxub5fHlnI7fjU+45OTo0aPmoYceMkFBQcbLy8tUq1bNvPrqq05P1N1srLKzZ88e07x5c+Pn55flCZWff/7ZDB061ERFRRkvLy9TqlQp07BhQzN69Gjz66+/GmOMmT9/vmnTpo0pW7as8fb2NmFhYebPf/6z2bt3r9N2cjom2Tl//rx54oknTHBwsPHz8zP33nuv+fzzz7OMfU4/t9n97GVkZJj4+HgTHh5uvL29TXR0tFm5cmW2xzM72R2jDz74wFSvXt14eXll+x660eeff26aNGli7Ha7CQkJMX/7298cT6tduHDBaVs5Hb+VK1c6flbKlStn/va3v5k1a9ZkecrLlf399ddfzT/+8Q9TrVo14+3t7fhIhuHDh5uTJ0/ecmxw+2zGGFPoqQl3nMjISNWuXTvXHz5WlGzevFlt2rTRkiVLsjw1A6DwdejQQUlJSY4niHBn4hISAKDIGjFihOrXr6/w8HCdO3dO7733ntavX6933nnH3aXBzQgwAIAiKz09XS+++KJOnjwpm82mmjVr6t1339XDDz/s7tLgZlxCAgAAlsMH2QEAAMshwAAAAMshwAAAAMux9E28GRkZ+umnnxQYGJjtR0gDAICixxijX375RWFhYbn6QMLsWDrA/PTTTwoPD3d3GQAAIA+Sk5Pz/GnRlg4wmR9RnpycnOXbfwEAQNGUmpqq8PDw2/ryWUsHmMzLRsWLFyfAAABgMbdz+wc38QIAAMshwAAAAMshwAAAAMshwAAAAMshwAAAAMshwAAAAMshwAAAAMshwAAAAMshwAAAAMshwAAAAMtxa4CJjIyUzWbLMg0ePNidZQEAgCLOrd+FtH37dqWnpzvmv/32W7Vv3169e/d2Y1UAAKCoc2uAKVOmjNP8pEmTVKlSJbVq1cpNFQEAACsoMvfAXL16VQsXLtTjjz9+W99OCQAA/vjcegbm95YvX64LFy7o0UcfzXGdtLQ0paWlOeZTU1MLoTIAAFDUFJkA884776hTp04KCwvLcZ34+HjFxcUVWk2Roz7Jtj1pUpdCqwEAAGRVJC4hHT16VBs2bFD//v1vul5sbKxSUlIcU3JyciFVCAAAipIicQZm7ty5Cg4OVpcuNz+zYbfbZbfbC6kqAABQVLn9DExGRobmzp2rmJgYeXoWiTwFAACKOLcHmA0bNujYsWN6/PHH3V0KAACwCLef8ujQoYOMMe4uAwAAWIjbz8AAAAC4igADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAshwADAAAsx+0B5vjx43r44YcVFBQkPz8/1atXTzt37nR3WQAAoAjzdOfGz58/r+bNm6tNmzZas2aNgoOD9eOPP+quu+5yZ1kAAKCIc2uAefnllxUeHq65c+c62iIjI91XEAAAsAS3XkJasWKFGjVqpN69eys4OFj169fXrFmzclw/LS1NqampThMAALjzuPUMzOHDhzV9+nSNGDFCzz//vL7++msNHTpUdrtdjzzySJb14+PjFRcX54ZK/1giR32S47KkSV3ctv3C2Pat5Gdtt9vXzV6f38fQ1Vpvtv0bX5/bdfPLjTUX9vZdURTe84BVufUMTEZGhho0aKCJEyeqfv36GjhwoAYMGKDp06dnu35sbKxSUlIcU3JyciFXDAAAigK3BpjQ0FDVrFnTqa1GjRo6duxYtuvb7XYVL17caQIAAHcetwaY5s2b68CBA05tP/zwgyIiItxUEQAAsAK3Bpjhw4dr69atmjhxog4dOqT3339fM2fO1ODBg91ZFgAAKOLcGmDuvvtuLVu2TB988IFq166tl156SW+++ab69u3rzrIAAEAR59ankCSpa9eu6tq1q7vLAAAAFuL2rxIAAABwFQEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYDgEGAABYjlsDzNixY2Wz2ZymkJAQd5YEAAAswNPdBdSqVUsbNmxwzHt4eLixGgAAYAVuDzCenp6cdQEAAC5x+z0wBw8eVFhYmKKiotSnTx8dPnw4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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#relation between test and test_grade\n",
    "test = data['tests']\n",
    "t_grade = data['tests_grade']\n",
    "plt.bar(test, t_grade)\n",
    "plt.xlabel('Tests')\n",
    "plt.ylabel('Test Grade')\n",
    "plt.title('Simple representation of test and it grade')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "52f1f40e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAioAAAHFCAYAAADcytJ5AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA+lUlEQVR4nO3deVzU1f7H8ffIMmyuuCCogFoqKq5luZtmi1tW5laS1S1NLSUrzbpqqZiW5e0WZotmWma5/FzKxFRaXDMsl9IsFSzN1ATFRITz+6MHcx0BZXBgvsrr+XjM48H3zJnz/cz5zsCb7zJjM8YYAQAAWFApTxcAAACQH4IKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLILKFWrTpk3q2bOnatSoIbvdripVqujGG2/UE0884dSvffv2at++vUdq3L9/v2w2m2bPnu2R9ZdUu3bt0rhx47R///5Cj7F+/XqNGzdOJ06cyHWfJ19TBbV//3516dJFFSpUkM1m0/Dhw/PtGxERIZvN5rgFBQWpRYsWmjNnjltrmj17tmw222Vtl4txx3YvKgV9zUREROj+++93LP/+++8aN26ctm3bVmS1FYUr4T1yJfH2dAFw3YoVK9S9e3e1b99eU6ZMUdWqVXXo0CF9++23mj9/vl5++WVH3zfeeMODlcITdu3apfHjx6t9+/aKiIgo1Bjr16/X+PHjdf/996tcuXJO910Jr6kRI0Zo06ZNevfddxUSEqKqVatetH+rVq300ksvSZIOHjyol156STExMUpPT9fgwYPdUlOXLl20YcOGS9ZSWO7Y7p62ePFilSlTxrH8+++/a/z48YqIiFDjxo09Vxg8iqByBZoyZYoiIyP1+eefy9v7f5uwT58+mjJlilPfqKio4i6vWBljdObMGfn7+xfL+k6fPq2AgIBiWZdVXQmvqR07duj666/XHXfcUaD+5cqV0w033OBY7tSpk8LDwzVt2rR8g0pWVpbOnTsnu91eoHVUqlRJlSpVKlDfkqpJkyYeXf/ff/9dbL9LUHAc+rkCHTt2TBUrVnQKKTlKlXLepBfugsw5HDN16lS9+OKLioiIkL+/v9q3b689e/YoMzNTo0aNUmhoqMqWLauePXvqyJEjTmNGRESoa9euWrx4saKjo+Xn56eaNWvqP//5T4Hq//nnn9WvXz9VrlxZdrtd9erV0+uvv16gx9psNg0dOlQzZsxQvXr1ZLfb9d577xV43HXr1slms2nu3LmKjY1VSEiI/P391a5dOyUlJTn1vf/++xUUFKTt27erc+fOKl26tDp27ChJOnv2rCZMmKC6devKbrerUqVKGjhwoP7880+nMdasWaP27dsrODhY/v7+qlGjhu666y6dPn3a0aegY+XM+8qVK9W0aVP5+/urbt26evfddx19Zs+erV69ekmSOnTo4DickXP4LSEhQT169FC1atXk5+en2rVr65FHHtHRo0cdY4wbN05PPvmkJCkyMtIxxrp16yTlvVv7+PHjevTRRxUWFiZfX1/VrFlTY8aMUUZGRp7b7/3331e9evUUEBCgRo0aafny5Xlv8AskJyfr3nvvddrGL7/8srKzsyX9b/vu3btXn332maN2Vw+HlCtXTnXq1NGBAwck/e99M2XKFE2YMEGRkZGy2+1au3atJGnp0qW68cYbFRAQoNKlS+vmm2/Whg0bnMbM79DP6tWr1bFjR5UpU0YBAQFq1aqVvvjii1w1/fTTT+rbt6+qVKkiu92uGjVqaMCAAcrIyLjkds/L3r17NXDgQF1zzTUKCAhQWFiYunXrpu3btzv1y5nTDz/8UGPGjFFoaKjKlCmjTp06affu3U59jTGaMmWKwsPD5efnp6ZNm+qzzz4r0JxLzod+1q1bp+uuu06SNHDgQMdzGjdu3EXH+Prrr3XjjTfKz89PYWFheu655/T222/nmvuc99OiRYvUpEkT+fn5afz48ZKk119/XW3btlXlypUVGBiohg0basqUKcrMzCz0801LS9PIkSMVGRkpX19fhYWFafjw4UpPTy/w/JRYBlechx56yEgyw4YNMxs3bjRnz57Nt2+7du1Mu3btHMv79u0zkkx4eLjp1q2bWb58uZk7d66pUqWKufbaa819991nHnjgAfPZZ5+ZGTNmmKCgINOtWzenMcPDw01YWJipUaOGeffdd82nn35q+vfvbySZqVOn5lrXrFmzHG07d+40ZcuWNQ0bNjRz5swxq1atMk888YQpVaqUGTdu3CWfuyQTFhZmoqOjzQcffGDWrFljduzYUeBx165daySZ6tWrmx49ephly5aZuXPnmtq1a5syZcqYX375xdE3JibG+Pj4mIiICBMXF2e++OIL8/nnn5us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r83VnpSUpO7duys4OFheXl7y8fHRgAEDlJWVpT179khy7fkuX75cDRo0UOPGjZ229S233OJ0WBV542TaK1jz5s3VvHlzSVJmZqaefvppvfLKK5oyZUquk2ovVKFCBadlX1/fi7afOXPGqT0kJCTXmDltx44dy3Odx44d07lz5/Taa6/ptddey7NPQULWhVdNFGbc/Or//vvvndoCAgKcrkKQpD/++EMnTpxwzE1+66pVq5ZWr16tKVOmaMiQIUpPT1fNmjX12GOP6fHHH3dprBzBwcG5+tjtdv399995Pv582dnZ6ty5s37//Xc999xzatiwoQIDA5Wdna0bbrihQGPk5dixYwoJCXEKfpJUuXJleXt753o9FPY5HDt2LM+rWUJDQx33F1br1q31yiuvyGazKSAgQLVq1cpzm+T12surPaeu7Oxs/fXXX3megP3HH39IUq6Ad77jx4+rVKlSysrKUrVq1Vx6TpcSGxur119/XU8//bTatWun8uXLq1SpUnrooYfy3BYXbreck4hz+ubMxcV+NxS1Y8eOqUqVKrna82qT8t5uycnJatOmjerUqaPp06crIiJCfn5+2rx5s4YMGVKo5/vHH39o7969TiH3fAX5vVeSEVSuEj4+Pho7dqxeeeUV7dixo8jXd/jw4Xzb8vpDJEnly5eXl5eX7rvvPg0ZMiTPPpGRkZdc94V/EAszbn71X1j7heuSpIoVKyo4OFgrV67Mc13n7y1o06aN2rRpo6ysLH377bd67bXXNHz4cFWpUkV9+vRxaazLtWPHDn3//feaPXu2YmJiHO179+69rHGDg4O1adMmGWOc5uvIkSM6d+6c03+3l7ueQ4cO5Wr//fffJemy1lO2bFlH6L+YC18POa+X/OoqVaqU096/8+XU+9prrzldcXS+KlWqKCsrS15eXjp48OAl63PF3LlzNWDAAE2aNMmp/ejRo7kuSS+InLnI771VHJdMBwcHOwLghevPS17v7yVLlig9PV2LFi1y2jNy4We5uPJ8K1asKH9/f6cT38/nrvfI1YqgcgU6dOhQnv8J5OyuzfkPsyjt3LlT33//vdPhnw8++EClS5dW06ZN83xMQECAOnTooKSkJEVHR+e7F8FVhRn3ww8/VGxsrOMX1YEDB7R+/XoNGDDgko/t2rWr5s+fr6ysLLVo0aJANXp5ealFixaqW7eu5s2bp++++059+vQp1FiXcuF/ujlynuuFl9O++eabBR4jLx07dtSCBQu0ZMkS9ezZ09Ge84FpOVdKXa6OHTsqLi5O3333ndNrbM6cObLZbOrQoYNb1uOKOnXqKCwsTB988IFGjhzpmOP09HQtXLjQcSVQXlq1aqVy5cpp165dGjp06EXX065dO3388ceaOHFivn/UXNlm0j+vhwtfCytWrNBvv/2m2rVrF2iM891www3y8/PTvHnznA6Xrl+/XgcOHChUUHH1ObVr106ffvqpjh496pin7OxsffzxxwVeZ17vE2OM3nrrLad+rjzfrl27atKkSQoODi7QP2NwRlC5At1yyy2qVq2aunXrprp16yo7O1vbtm3Tyy+/rKCgIMdhhaIUGhqq7t27a9y4capatarmzp2rhIQEvfjiixf9nJHp06erdevWatOmjQYPHqyIiAidPHlSe/fu1bJlywp9noGr4x45ckQ9e/bUv/71L6Wmpmrs2LHy8/PT6NGjL7muPn36aN68ebr99tv1+OOP6/rrr5ePj48OHjyotWvXqkePHurZs6dmzJihNWvWqEuXLqpRo4bOnDnj+I+qU6dOLo3ligYNGkiSZs6cqdKlS8vPz0+RkZGqW7euatWqpVGjRskYowoVKmjZsmVKSEjINUbDhg0d8xoTEyMfHx/VqVMnzz08AwYM0Ouvv66YmBjt379fDRs21Ndff61Jkybp9ttvdzzXyzVixAjNmTNHXbp00fPPP6/w8HCtWLFCb7zxhgYPHpznuQZFrVSpUpoyZYr69++vrl276pFHHlFGRoamTp2qEydOaPLkyfk+NigoSK+99ppiYmJ0/Phx3X333apcubL+/PNPff/99/rzzz8VHx8vSZo2bZpat26tFi1aaNSoUapdu7b++OMPLV26VG+++aZKly6d73bPbw9n165dNXv2bNWtW1fR0dHaunWrpk6dWuhDTOXLl9fIkSM1YcIEPfTQQ+rVq5dSUlI0bty4Qh/6qVWrlvz9/TVv3jzVq1dPQUFBCg0NzfefsTFjxmjZsmXq2LGjxowZI39/f82YMcNxCfCFH9+Ql5tvvlm+vr7q27evnnrqKZ05c0bx8fH666+/Cv18hw8froULF6pt27YaMWKEoqOjlZ2dreTkZK1atUpPPPGE2/5RuSp59lxeFMZHH31k+vXrZ6655hoTFBRkfHx8TI0aNcx9991ndu3a5dQ3v6t+zr+M2Jj/ndn/8ccfO7XnXKlw/tnqOVdUfPLJJ6Z+/frG19fXREREmGnTpjk9Nq+rfnLaH3jgARMWFmZ8fHxMpUqVTMuWLc2ECRMu+dwlmSFDhuR5X0HGzXme77//vnnsscdMpUqVjN1uN23atDHffvut03gxMTEmMDAwz3VlZmaal156yTRq1Mj4+fmZoKAgU7duXfPII4+Yn3/+2RhjzIYNG0zPnj1NeHi4sdvtJjg42LRr184sXbrU5bGMyf9Klgu3sTH/XMUVGRlpvLy8nLbBrl27zM0332xKly5typcvb3r16mWSk5ONJDN27FinMUaPHm1CQ0NNqVKlnK4myWt9x44dM4MGDTJVq1Y13t7eJjw83IwePTrXZcH5bb8Lr/bIz4EDB0y/fv1McHCw8fHxMXXq1DFTp051uuLmYnOVl4L0ze99k2PJkiWmRYsWxs/PzwQGBpqOHTuab775xqlPzntp//79Tu2JiYmmS5cupkKFCsbHx8eEhYWZLl265Hov7tq1y/Tq1csEBwcbX19fU6NGDXP//fc7zXF+2z0vf/31l3nwwQdN5cqVTUBAgGndurX56quvcm3f/H435PX+zs7ONnFxcaZ69erG19fXREdHm2XLluX5mslLXq+DDz/80NStW9f4+Pjk+Tq90FdffWVatGhh7Ha7CQkJMU8++aTjCrQTJ044rSu/7b5s2TLH+zEsLMw8+eST5rPPPst1VZUrz/fUqVPm2WefNXXq1DG+vr6Oj1MYMWKEOXz48CXnpiSzGWNMcYcjXNkiIiLUoEGDAn9Il5WsW7dOHTp00Mcff3zRkxgBd5s+fbqGDx+ukydPKigoyNPllCidO3fW/v37HVfs4MrCoR8AKEKpqanasGGDZs+erQYNGhBSilhsbKyaNGmi6tWr6/jx45o3b54SEhL0zjvveLo0FBJBBQCKUFJSknr27Kno6Gj+WBaDrKws/fvf/9bhw4dls9kUFRWl999/X/fee6+nS0MhcegHAABYFp9MCwAALIugAgAALIugAgAALOuKPpk2Oztbv//+u0qXLp3nRyEDAADrMcbo5MmTCg0NveQH8V3RQeX3339X9erVPV0GAAAohJSUlEt+GvIVHVRyPs47JSUl1zfcAgAAa0pLS1P16tUL9MWrV3RQyTncU6ZMGYIKAABXmIKctsHJtAAAwLIIKgAAwLIIKgAAwLIIKgAAwLIIKgAAwLIIKgAAwLIIKgAAwLIIKgAAwLIIKgAAwLIIKgAAwLI8GlQiIiJks9ly3YYMGeLJsgAAgEV49Lt+tmzZoqysLMfyjh07dPPNN6tXr14erAoAAFiFR4NKpUqVnJYnT56sWrVqqV27dh6qCAAAWIllzlE5e/as5s6dqwceeKBA36YIAACufh7do3K+JUuW6MSJE7r//vvz7ZORkaGMjAzHclpaWjFUBgAAPMUyQeWdd97RbbfdptDQ0Hz7xMXFafz48cVWU8SoFY6f90/uUmzrBQAA/7DEoZ8DBw5o9erVeuihhy7ab/To0UpNTXXcUlJSiqlCAADgCZbYozJr1ixVrlxZXbpcfK+F3W6X3W4vpqoAAICneXyPSnZ2tmbNmqWYmBh5e1siNwEAAIvweFBZvXq1kpOT9cADD3i6FAAAYDEe34XRuXNnGWM8XQYAALAgj+9RAQAAyA9BBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWBZBBQAAWJbHg8pvv/2me++9V8HBwQoICFDjxo21detWT5cFAAAswNuTK//rr7/UqlUrdejQQZ999pkqV66sX375ReXKlfNkWQAAwCI8GlRefPFFVa9eXbNmzXK0RUREeK4gAABgKR499LN06VI1b95cvXr1UuXKldWkSRO99dZb+fbPyMhQWlqa0w0AAFy9PLpH5ddff1V8fLxiY2P1zDPPaPPmzXrsscdkt9s1YMCAXP3j4uI0fvx4D1QKq4gYtcLx8/7JXQrdB4Vz/txK1ppfd2x3XjuA9Xh0j0p2draaNm2qSZMmqUmTJnrkkUf0r3/9S/Hx8Xn2Hz16tFJTUx23lJSUYq4YAAAUJ48GlapVqyoqKsqprV69ekpOTs6zv91uV5kyZZxuAADg6uXRoNKqVSvt3r3bqW3Pnj0KDw/3UEUAAMBKPBpURowYoY0bN2rSpEnau3evPvjgA82cOVNDhgzxZFkAAMAiPBpUrrvuOi1evFgffvihGjRooBdeeEGvvvqq+vfv78myAACARXj0qh9J6tq1q7p27erpMgAAgAV5/CP0AQAA8kNQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAlkVQAQAAluXRoDJu3DjZbDanW0hIiCdLAgAAFuLt6QLq16+v1atXO5a9vLw8WA0AALASjwcVb29v9qIAAIA8efwclZ9//lmhoaGKjIxUnz599Ouvv+bbNyMjQ2lpaU43AABw9fLoHpUWLVpozpw5uvbaa/XHH39owoQJatmypXbu3Kng4OBc/ePi4jR+/HgPVAoAlxYxakWe7fsnd3H5MZd63MUe7+rj8up/qfsL0t/VMYC8eHSPym233aa77rpLDRs2VKdOnbRixT8v6vfeey/P/qNHj1ZqaqrjlpKSUpzlAgCAYubxc1TOFxgYqIYNG+rnn3/O83673S673V7MVQEAAE/x+Dkq58vIyNCPP/6oqlWreroUAABgAR4NKiNHjlRiYqL27dunTZs26e6771ZaWppiYmI8WRYAALAIjx76OXjwoPr27aujR4+qUqVKuuGGG7Rx40aFh4d7siwAAGARHg0q8+fP9+TqAQCAxVnqHBUAAIDzEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlEVQAAIBlFSqo/PLLL3r22WfVt29fHTlyRJK0cuVK7dy5063FAQCAks3loJKYmKiGDRtq06ZNWrRokU6dOiVJ+uGHHzR27Fi3FwgAAEoul4PKqFGjNGHCBCUkJMjX19fR3qFDB23YsMGtxQEAgJLN5aCyfft29ezZM1d7pUqVdOzYMbcUBQAAIBUiqJQrV06HDh3K1Z6UlKSwsDC3FAUAACAVIqj069dPTz/9tA4fPiybzabs7Gx98803GjlypAYMGFAUNQIAgBLK5aAyceJE1ahRQ2FhYTp16pSioqLUtm1btWzZUs8++2xR1AgAAEoob1cf4OPjo3nz5un5559XUlKSsrOz1aRJE11zzTVFUR8AACjBXA4qOWrVqqVatWq5sxYAAAAnBQoqsbGxBR5w2rRphS4GAADgfAUKKklJSU7LW7duVVZWlurUqSNJ2rNnj7y8vNSsWTP3VwgAAEqsAgWVtWvXOn6eNm2aSpcurffee0/ly5eXJP31118aOHCg2rRpUzRVAgCAEsnlq35efvllxcXFOUKKJJUvX14TJkzQyy+/7NbiAABAyeZyUElLS9Mff/yRq/3IkSM6efKkW4oCAACQChFUevbsqYEDB+qTTz7RwYMHdfDgQX3yySd68MEHdeeddxZFjQAAoIRy+fLkGTNmaOTIkbr33nuVmZn5zyDe3nrwwQc1depUtxcIAABKLpeDSkBAgN544w1NnTpVv/zyi4wxql27tgIDA4uiPgAAUIIV+gPfAgMDFR0d7c5aAAAAnBQqqGzZskUff/yxkpOTdfbsWaf7Fi1a5JbCAAAAXD6Zdv78+WrVqpV27dqlxYsXKzMzU7t27dKaNWtUtmzZoqgRAACUUC4HlUmTJumVV17R8uXL5evrq+nTp+vHH3/UPffcoxo1ahRFjQAAoIRyOaj88ssv6tKliyTJbrcrPT1dNptNI0aM0MyZM91eIAAAKLlcDioVKlRwfLBbWFiYduzYIUk6ceKETp8+7d7qAABAiebyybRt2rRRQkKCGjZsqHvuuUePP/641qxZo4SEBHXs2LEoagQAACWUy0Hlv//9r86cOSNJGj16tHx8fPT111/rzjvv1HPPPef2AgEAQMnl0qGfc+fOadmyZSpV6p+HlSpVSk899ZSWLl2qadOmOX1Roavi4uJks9k0fPjwQo8BAACuLi4FFW9vbw0ePFgZGRluLWLLli2aOXMmHyAHAACcuHwybYsWLZSUlOS2Ak6dOqX+/fvrrbfeuqw9MgAA4Orj8jkqjz76qJ544gkdPHhQzZo1y/UdP67uFRkyZIi6dOmiTp06acKECa6WAwAArmIuB5XevXtLkh577DFHm81mkzFGNptNWVlZBR5r/vz5+u6777Rly5YC9c/IyHA67JSWllbgdQEAgCuPy0Fl3759bllxSkqKHn/8ca1atUp+fn4FekxcXJzGjx/vlvUDuHpEjFrhsfH3T+5yyfVHjFqh/ZO7FFtNwNXE5aASHh7ulhVv3bpVR44cUbNmzRxtWVlZ+vLLL/Xf//5XGRkZ8vLycnrM6NGjFRsb61hOS0tT9erV3VIPAACwngIHlezsbO3cuVMNGzaUJM2YMcPpm5O9vLw0ePBgx6XLl9KxY0dt377dqW3gwIGqW7eunn766VwhRfrnI/vtdntBSwYAAFe4AgeV+fPn680331RiYqIk6cknn1S5cuXk7f3PEEePHpWfn58efPDBAo1XunRpNWjQwKktMDBQwcHBudoBAEDJVODLk2fNmqVBgwY5tSUmJmrfvn3at2+fpk6dqrlz57q9QAAAUHIVeI/Kjz/+qKioqHzvb9eunZ555pnLKmbdunWX9XgAAHB1KXBQOXr0qIKCghzLv/76q4KDgx3LPj4+Sk9Pd291AACgRCvwoZ8qVapo9+7djuVKlSo5nTj7448/KiQkxL3VAQCAEq3AQaVjx46aOHFinvcZYxQXF6eOHTu6rTAAAIACH/oZM2aMmjZtqhYtWmjkyJG69tprZbPZ9NNPP+mll17S7t27NWfOnKKsFQAAlDAFDiq1atVSQkKC7r//fvXu3Vs2m03SP3tT6tatq1WrVql27dpFVigAACh5XPpk2uuvv167du3Stm3btGfPHknSNddcoyZNmhRJcQAAoGRz+SP0Jalx48Zq3Lixm0sBAABwVuCTaQEAAIobQQUAAFgWQQUAAFiWy0ElOTlZxphc7cYYJScnu6UoAAAAqRBBJTIyUn/++Weu9uPHjysyMtItRQEAAEiFCCrGGMdnqJzv1KlT8vPzc0tRAAAAkguXJ8fGxkqSbDabnnvuOQUEBDjuy8rK0qZNm7hkGQAAuFWBg0pSUpKkf/aobN++Xb6+vo77fH191ahRI40cOdL9FQIAgBKrwEFl7dq1kqSBAwdq+vTpKlOmTJEVBQAAIBXiHJVXX31V586dy9V+/PhxpaWluaUoAAAAqRBBpU+fPpo/f36u9gULFqhPnz5uKQoAAEAqRFDZtGmTOnTokKu9ffv22rRpk1uKAgAAkAoRVDIyMvI89JOZmam///7bLUUBAABIhQgq1113nWbOnJmrfcaMGWrWrJlbigIAAJBcuOonx8SJE9WpUyd9//336tixoyTpiy++0JYtW7Rq1Sq3FwgAAEoul/eotGrVShs2bFC1atW0YMECLVu2TLVr19YPP/ygNm3aFEWNAACghHJ5j4okNW7cWB988IG7awEAAHDi8h4VSfrll1/07LPPql+/fjpy5IgkaeXKldq5c6dbiwMAACWby0ElMTFRDRs21KZNm7Rw4UKdOnVKkvTDDz9o7Nixbi8QAACUXC4HlVGjRmnChAlKSEhw+r6fDh06aMOGDW4tDgAAlGwuB5Xt27erZ8+eudorVaqkY8eOuaUoAAAAqRBBpVy5cjp06FCu9qSkJIWFhbmlKAAAAKkQQaVfv356+umndfjwYdlsNmVnZ+ubb77RyJEjNWDAgKKoEQAAlFAuB5WJEyeqRo0aCgsL06lTpxQVFaW2bduqZcuWevbZZ4uiRgAAUEK5/DkqPj4+mjdvnp5//nklJSUpOztbTZo00TXXXFMU9QEAgBKsUB/4Jkm1atVSrVq13FkLAACAkwIFldjYWL3wwgsKDAxUbGzsRfsGBQWpfv36uvvuu+Xl5eWWIgEAQMlUoKCSlJSkzMxMx88Xk5GRoenTp2vFihWaM2fO5VcIAABKrAIFlbVr1+b5c36+/fZbxzcrAwAAFFahvusnhzFGxphc7dHR0exNAQAAl61QQWXOnDlq2LCh/P395e/vr+joaL3//vuO+319fdWjRw+3FQkAAEoml6/6mTZtmp577jkNHTpUrVq1kjFG33zzjQYNGqSjR49qxIgRRVEnAAAogVwOKq+99pri4+OdPoW2R48eql+/vsaNG0dQAQAAbuPyoZ9Dhw6pZcuWudpbtmyZ53cAXUx8fLyio6NVpkwZlSlTRjfeeKM+++wzV0sCAABXKZeDSu3atbVgwYJc7R999JHLn05brVo1TZ48Wd9++62+/fZb3XTTTerRo4d27tzpalkAAOAq5PKhn/Hjx6t379768ssv1apVK9lsNn399df64osv8gwwF9OtWzen5YkTJyo+Pl4bN25U/fr1XS0NAABcZVwOKnfddZc2b96sadOmacmSJTLGKCoqSps3b1aTJk0KXUhWVpY+/vhjpaen68Ybb8yzT0ZGhjIyMhzLaWlphV4fAACwPpeCSmZmph5++GE999xzmjt3rlsK2L59u2688UadOXNGQUFBWrx4saKiovLsGxcXp/Hjx7tlvQBQnCJGrXBa3j+5S4Efs39yl1yPd2Vdl1vb5Y5XGOePcX49lxo7p29+/Qoy77AWl85R8fHx0eLFi91aQJ06dbRt2zZt3LhRgwcPVkxMjHbt2pVn39GjRys1NdVxS0lJcWstAADAWlw+mbZnz55asmSJ2wrw9fVV7dq11bx5c8XFxalRo0aaPn16nn3tdrvjCqGcGwAAuHq5fI5K7dq19cILL2j9+vVq1qyZAgMDne5/7LHHLqsgY4zTeSgAAKDkcjmovP322ypXrpy2bt2qrVu3Ot1ns9lcCirPPPOMbrvtNlWvXl0nT57U/PnztW7dOq1cudLVsgAAwFXI5aCyb98+t638jz/+0H333adDhw6pbNmyio6O1sqVK3XzzTe7bR0AAODK5XJQOV/ONyfbbLZCPf6dd965nNUDAICrXKG+Pfmdd95RgwYN5OfnJz8/PzVo0EBvv/22u2sDAAAlnMt7VJ577jm98sorGjZsmOOD2TZs2KARI0Zo//79mjBhgtuLBAAAJZPLQSU+Pl5vvfWW+vbt62jr3r27oqOjNWzYMIIKAABwG5cP/WRlZal58+a52ps1a6Zz5865pSgAAACpEEHl3nvvVXx8fK72mTNnqn///m4pCgAAQCrkVT/vvPOOVq1apRtuuEGStHHjRqWkpGjAgAGKjY119Js2bZp7qgQAACWSy0Flx44datq0qSTpl19+kSRVqlRJlSpV0o4dOxz9CnvJMgAAQA6Xg8ratWuLog4AAIBcCvU5KgAAAMWBoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACyLoAIAACzLo0ElLi5O1113nUqXLq3KlSvrjjvu0O7duz1ZEgAAsBCPBpXExEQNGTJEGzduVEJCgs6dO6fOnTsrPT3dk2UBAACL8PbkyleuXOm0PGvWLFWuXFlbt25V27ZtPVQVAACwCo8GlQulpqZKkipUqJDn/RkZGcrIyHAsp6WlFUtdAADAMywTVIwxio2NVevWrdWgQYM8+8TFxWn8+PHFXBkAlCwRo1YUy5j7J3fJ8/7z291dT37rubA9v3rdUcuFzw8XZ5mrfoYOHaoffvhBH374Yb59Ro8erdTUVMctJSWlGCsEAADFzRJ7VIYNG6alS5fqyy+/VLVq1fLtZ7fbZbfbi7EyAADgSR4NKsYYDRs2TIsXL9a6desUGRnpyXIAAIDFeDSoDBkyRB988IH+7//+T6VLl9bhw4clSWXLlpW/v78nSwMAABbg0XNU4uPjlZqaqvbt26tq1aqO20cffeTJsgAAgEV4/NAPAABAfixz1Q8AAMCFCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyCCoAAMCyPBpUvvzyS3Xr1k2hoaGy2WxasmSJJ8sBAAAW49Ggkp6erkaNGum///2vJ8sAAAAW5e3Jld9222267bbbPFkCAACwMI8GFVdlZGQoIyPDsZyWlubBagAAQFG7ooJKXFycxo8f7+kyAABuEDFqhUvtlzOmO9Z/OXUVxTjn2z+5S5GP7SlX1FU/o0ePVmpqquOWkpLi6ZIAAEARuqL2qNjtdtntdk+XAQAAiskVtUcFAACULB7do3Lq1Cnt3bvXsbxv3z5t27ZNFSpUUI0aNTxYGQAAsAKPBpVvv/1WHTp0cCzHxsZKkmJiYjR79mwPVQUAAKzCo0Glffv2MsZ4sgQAAGBhnKMCAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsi6ACAAAsy+NB5Y033lBkZKT8/PzUrFkzffXVV54uCQAAWIRHg8pHH32k4cOHa8yYMUpKSlKbNm102223KTk52ZNlAQAAi/BoUJk2bZoefPBBPfTQQ6pXr55effVVVa9eXfHx8Z4sCwAAWITHgsrZs2e1detWde7c2am9c+fOWr9+vYeqAgAAVuLtqRUfPXpUWVlZqlKlilN7lSpVdPjw4Twfk5GRoYyMDMdyamqqJCktLa1IaszOOO34uajWAdcUZJuw3YrO+XMrWWd+3VVXfq+dC8e/cF0Xu/9ij7vU2Je7DpQcrryeCjt2UYxpjLl0Z+Mhv/32m5Fk1q9f79Q+YcIEU6dOnTwfM3bsWCOJGzdu3Lhx43YV3FJSUi6ZFzy2R6VixYry8vLKtffkyJEjufay5Bg9erRiY2Mdy9nZ2Tp+/LiCg4Nls9ncXmNaWpqqV6+ulJQUlSlTxu3j4x/Mc/FgnosH81w8mOfiUVTzbIzRyZMnFRoaesm+Hgsqvr6+atasmRISEtSzZ09He0JCgnr06JHnY+x2u+x2u1NbuXLlirJMSVKZMmV4IxQD5rl4MM/Fg3kuHsxz8SiKeS5btmyB+nksqEhSbGys7rvvPjVv3lw33nijZs6cqeTkZA0aNMiTZQEAAIvwaFDp3bu3jh07pueff16HDh1SgwYN9Omnnyo8PNyTZQEAAIvwaFCRpEcffVSPPvqop8vIk91u19ixY3MdboJ7Mc/Fg3kuHsxz8WCei4cV5tlmTEGuDQIAACh+Hv+uHwAAgPwQVAAAgGURVAAAgGURVAAAgGURVC7ijTfeUGRkpPz8/NSsWTN99dVXni7pihYXF6frrrtOpUuXVuXKlXXHHXdo9+7dTn2MMRo3bpxCQ0Pl7++v9u3ba+fOnR6q+MoXFxcnm82m4cOHO9qYY/f47bffdO+99yo4OFgBAQFq3Lixtm7d6rifeb58586d07PPPqvIyEj5+/urZs2aev7555Wdne3owzy77ssvv1S3bt0UGhoqm82mJUuWON1fkDnNyMjQsGHDVLFiRQUGBqp79+46ePBg0RR8WV/YcxWbP3++8fHxMW+99ZbZtWuXefzxx01gYKA5cOCAp0u7Yt1yyy1m1qxZZseOHWbbtm2mS5cupkaNGubUqVOOPpMnTzalS5c2CxcuNNu3bze9e/c2VatWNWlpaR6s/Mq0efNmExERYaKjo83jjz/uaGeOL9/x48dNeHi4uf/++82mTZvMvn37zOrVq83evXsdfZjnyzdhwgQTHBxsli9fbvbt22c+/vhjExQUZF599VVHH+bZdZ9++qkZM2aMWbhwoZFkFi9e7HR/QeZ00KBBJiwszCQkJJjvvvvOdOjQwTRq1MicO3fO7fUSVPJx/fXXm0GDBjm11a1b14waNcpDFV19jhw5YiSZxMREY4wx2dnZJiQkxEyePNnR58yZM6Zs2bJmxowZnirzinTy5ElzzTXXmISEBNOuXTtHUGGO3ePpp582rVu3zvd+5tk9unTpYh544AGntjvvvNPce++9xhjm2R0uDCoFmdMTJ04YHx8fM3/+fEef3377zZQqVcqsXLnS7TVy6CcPZ8+e1datW9W5c2en9s6dO2v9+vUequrqk5qaKkmqUKGCJGnfvn06fPiw07zb7Xa1a9eOeXfRkCFD1KVLF3Xq1MmpnTl2j6VLl6p58+bq1auXKleurCZNmuitt95y3M88u0fr1q31xRdfaM+ePZKk77//Xl9//bVuv/12ScxzUSjInG7dulWZmZlOfUJDQ9WgQYMimXePfzKtFR09elRZWVm5vsW5SpUqub7tGYVjjFFsbKxat26tBg0aSJJjbvOa9wMHDhR7jVeq+fPn67vvvtOWLVty3cccu8evv/6q+Ph4xcbG6plnntHmzZv12GOPyW63a8CAAcyzmzz99NNKTU1V3bp15eXlpaysLE2cOFF9+/aVxOu5KBRkTg8fPixfX1+VL18+V5+i+BtJULkIm83mtGyMydWGwhk6dKh++OEHff3117nuY94LLyUlRY8//rhWrVolPz+/fPsxx5cnOztbzZs316RJkyRJTZo00c6dOxUfH68BAwY4+jHPl+ejjz7S3Llz9cEHH6h+/fratm2bhg8frtDQUMXExDj6Mc/uV5g5Lap559BPHipWrCgvL69cyfDIkSO5UiZcN2zYMC1dulRr165VtWrVHO0hISGSxLxfhq1bt+rIkSNq1qyZvL295e3trcTERP3nP/+Rt7e3Yx6Z48tTtWpVRUVFObXVq1dPycnJkngtu8uTTz6pUaNGqU+fPmrYsKHuu+8+jRgxQnFxcZKY56JQkDkNCQnR2bNn9ddff+Xbx50IKnnw9fVVs2bNlJCQ4NSekJCgli1beqiqK58xRkOHDtWiRYu0Zs0aRUZGOt0fGRmpkJAQp3k/e/asEhMTmfcC6tixo7Zv365t27Y5bs2bN1f//v21bds21axZkzl2g1atWuW6tH7Pnj2Ob37ntewep0+fVqlSzn+mvLy8HJcnM8/uV5A5bdasmXx8fJz6HDp0SDt27CiaeXf76blXiZzLk9955x2za9cuM3z4cBMYGGj279/v6dKuWIMHDzZly5Y169atM4cOHXLcTp8+7egzefJkU7ZsWbNo0SKzfft207dvXy41vEznX/VjDHPsDps3bzbe3t5m4sSJ5ueffzbz5s0zAQEBZu7cuY4+zPPli4mJMWFhYY7LkxctWmQqVqxonnrqKUcf5tl1J0+eNElJSSYpKclIMtOmTTNJSUmOj98oyJwOGjTIVKtWzaxevdp899135qabbuLyZE94/fXXTXh4uPH19TVNmzZ1XEaLwpGU523WrFmOPtnZ2Wbs2LEmJCTE2O1207ZtW7N9+3bPFX0VuDCoMMfusWzZMtOgQQNjt9tN3bp1zcyZM53uZ54vX1pamnn88cdNjRo1jJ+fn6lZs6YZM2aMycjIcPRhnl23du3aPH8Xx8TEGGMKNqd///23GTp0qKlQoYLx9/c3Xbt2NcnJyUVSr80YY9y/nwYAAODycY4KAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAACwLIIKAEuaPXu2ypUr5+kyAHgYQQXAZbv//vtls9lks9nk4+OjmjVrauTIkUpPTy/0mL1799aePXvcViPBB7gyeXu6AABXh1tvvVWzZs1SZmamvvrqKz300ENKT09XfHy8U7/MzEz5+Phccjx/f3/5+/sXVbkArhDsUQHgFna7XSEhIapevbr69eun/v37a8mSJRo3bpwaN26sd999VzVr1pTdbpcxRsnJyerRo4eCgoJUpkwZ3XPPPfrjjz8c4+W1B2TZsmVq1qyZ/Pz8VLNmTY0fP17nzp1z3H/ixAk9/PDDqlKlivz8/NSgQQMtX75c69at08CBA5WamurY8zNu3LhimhkAl4M9KgCKhL+/vzIzMyVJe/fu1YIFC7Rw4UJ5eXlJku644w4FBgYqMTFR586d06OPPqrevXtr3bp1eY73+eef695779V//vMftWnTRr/88osefvhhSdLYsWOVnZ2t2267TSdPntTcuXNVq1Yt7dq1S15eXmrZsqVeffVV/fvf/9bu3bslSUFBQUU/CQAuG0EFgNtt3rxZH3zwgTp27ChJOnv2rN5//31VqlRJkpSQkKAffvhB+/btU/Xq1SVJ77//vurXr68tW7bouuuuyzXmxIkTNWrUKMXExEiSatasqRdeeEFPPfWUxo4dq9WrV2vz5s368ccfde211zr65ChbtqxsNptCQkKK9LkDcC8O/QBwi+XLlysoKEh+fn668cYb1bZtW7322muSpPDwcEdIkaQff/xR1atXd4QUSYqKilK5cuX0448/5jn+1q1b9fzzzysoKMhx+9e//qVDhw7p9OnT2rZtm6pVq+YIKQCuDuxRAeAWHTp0UHx8vHx8fBQaGup0wmxgYKBTX2OMbDZbrjHya5ek7OxsjR8/XnfeeWeu+/z8/DjxFrhKEVQAuEVgYKBq165doL5RUVFKTk5WSkqKY6/Krl27lJqaqnr16uX5mKZNm2r37t35riM6OloHDx7Unj178tyr4uvrq6ysrAI+GwBWQVABUOw6deqk6Oho9e/fX6+++qrjZNp27dqpefPmeT7m3//+t7p27arq1aurV69eKlWqlH744Qdt375dEyZMULt27dS2bVvdddddmjZtmmrXrq2ffvpJNptNt956qyIiInTq1Cl98cUXatSokQICAhQQEFDMzxyAqzhHBUCxs9lsWrJkicqXL6+2bduqU6dOqlmzpj766KN8H3PLLbdo+fLlSkhI0HXXXacbbrhB06ZNU3h4uKPPwoULdd1116lv376KiorSU0895diL0rJlSw0aNEi9e/dWpUqVNGXKlCJ/ngAun80YYzxdBABc6M0339QLL7yggwcPeroUAB7EHhUAlpOSkqJPP/1U9evX93QpADyMc1QAWE7Tpk0VFham2bNne7oUAB7GoR8AAGBZHPoBAACWRVABAACWRVABAACWRVABAACWRVABAACWRVABAACWRVABAACWRVABAACWRVABAACW9f+hB1F2vU6QcgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#relation between progect and project_grade\n",
    "test = data['project']\n",
    "t_grade = data['project_grade']\n",
    "plt.bar(test, t_grade)\n",
    "plt.xlabel('Project')\n",
    "plt.ylabel('project Grade')\n",
    "plt.title('Simple representation of Project and it grade')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "1bc37802",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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X3jhBWOz2czBgwcdbRmFj8yEh4eb9u3bm+TkZMf66NOnj/H29jZr1qxxTJeT4347QcUYY2rUqOE0BrciyRQqVMicOXPG0Xb9+nVTtWpVU7FiRUdbt27djN1uNydOnHB6frt27Yyfn5+5cOHCLeucOHGi03P79etnfH19nbY3f39/ExUV5XL9N0pJSTHJyclm7NixJjg42KlfV7eRrl27Zro+shNUjHFvTNauXWskmRkzZji1x8TEZBpURo0adct+r1+/bi5dumT8/f3N22+/7Wh3dXlPnDhhvLy8zMCBA536vXjxogkJCTFdunRxafnyAg795LLg4GB99dVX2rFjh8aPH6/OnTvr559/1ogRI1SrVi2n3fiZad++vdNhomrVqklSupPj0tpPnDjh1F6jRg3VqVPHqa179+5KSEjQ7t27M5xnYmKiNmzYoEcffVR+fn66fv2649a+fXslJiZq+/btt6z9oYceUtGiRW+r3+7duzvtug0PD1fjxo21adOmdPN7/PHHne6vWbNGRYoUUadOnZzmVbduXYWEhDh259etW1c+Pj7661//qgULFujIkSPp+na1rzR169ZVuXLlHPd9fX1VuXLlDHf1ZuTs2bPq27evypYtKy8vL3l7eys8PFyS9OOPP7rUx802btwof39/PfHEE07tPXv2lCRt2LDBqb1FixYKCAhw3C9VqpRKlix5y2XYuHGjqlevrvvuuy/dfIwx2rhxY7bql6TPPvtM3t7ejvUxa9Ysvfvuu07bQ06Ouyc8/PDDKlWqlON+wYIF1bVrVx0+fFi//PKLpD/X8cMPP6yyZcs6Pbdnz566cuVKuhNIM/LII4843a9du7YSExPTHUJ2x8aNG9WyZUsFBQWpYMGC8vb21qhRo3Tu3Ll0/bqyjWzatCnT9XEnbNmyRZLUpUsXp/annnoq0+fc/D4kSZcuXdIrr7yiihUrysvLS15eXipcuLAuX77stD27urzr1q3T9evX9eyzzzq9xn19fdWsWbN070d5GUHlDmnQoIFeeeUVLVu2TKdOndKQIUN07NixdCfUZqRYsWJO9318fLJsT0xMdGoPCQlJ12da27lz5zKc57lz53T9+nW9++67jg+FtFv79u0lyaWQFRoaetv9Zlb/zbX7+fkpMDDQqe23337ThQsX5OPjk25+Z86cccyrQoUKWr9+vUqWLKn+/furQoUKqlChgt5++223+0oTHBycrm673a6rV6/earUpNTVVrVu31vLly/X3v/9dGzZs0LfffusIca70kZFz584pJCQk3eWaJUuWlJeXV7p1mt1lOHfuXLqxl6SwsDDH49nVtGlT7dixQ9u3b9eHH36oiIgIDRgwQF9//bVjmpwcd09wZZvNiXV88/ja7XZJ2X99ffvtt2rdurUkadasWfrPf/6jHTt2aOTIkRn268rrK+01e7OM2nLDuXPn5OXlle799sYgcbOMxqV79+6aNm2aevfurXXr1unbb7/Vjh07VKJEiWwtb9o5Wffee2+61/jSpUtden/OK7jqxwO8vb01evRovfXWW9q/f3+uz+/MmTOZtmX0RiFJRYsWVcGCBfXMM8+of//+GU4TGRl5y3nf/IGYnX4zq//m2m+elyQVL15cwcHBio2NzXBeN+4teOCBB/TAAw8oJSVFO3fu1LvvvqvBgwerVKlS6tatm1t93a79+/dr7969mj9/vqKiohzthw8fvq1+g4OD9c0338gY47S+zp49q+vXr6t48eK31f+N8zl9+nS69lOnTknSbc0nKChIDRo0kCQ1bNhQDRs2VJ06ddSvXz/t2bNHBQoUyNFx9/X1laR0Jxvn5geBK9tsbq7j7FqyZIm8vb21Zs0ax3qTdFuXNwcHB2e5PnJbcHCwrl+/rvPnzzuFlazmf/N7UXx8vNasWaPRo0dr+PDhjvakpCSdP38+3fxcWd608f3Xv/7l2NN6t2KPSi7L6I1E+r9d92n/+8lNBw4c0N69e53aPv74YwUEBKhevXoZPsfPz08tWrTQd999p9q1a6tBgwbpbpmFnKxkp9/Fixc7XTFw/Phxbd261aUvMuvYsaPOnTunlJSUDOdVpUqVdM8pWLCgGjZs6LgKKe3wWHb6upXM/geb9kaX9niamTNnutxHRh5++GFdunQp3QfHwoULHY/nhIcfflg//PBDukOLCxculM1mU4sWLXJkPpJUqVIl/f3vf9e+ffsc302Uk+OedkXI999/7zT9qlWrXKrP1b1oN9qwYYPTVUwpKSlaunSpKlSo4LjU9uGHH9bGjRsdwSTNwoUL5efnl2OXJLtTv81mk5eXlwoWLOhou3r1qj788MNsz79FixaZro/scmeZmjVrJknp5pfRVViZsdlsMsak255nz56tlJQUpzZXl7dNmzby8vLSf//73wxf42lh/m7AHpVc1qZNG5UpU0adOnVS1apVlZqaqj179ujNN99U4cKF9eKLL+Z6DWFhYXrkkUc0ZswYhYaG6qOPPlJcXJwmTJiQ5fX9b7/9tpo2baoHHnhAL7zwgiIiInTx4kUdPnxYq1evzvZ5Bu72e/bsWT366KPq06eP4uPjNXr0aPn6+mrEiBG3nFe3bt20aNEitW/fXi+++KLuu+8+eXt765dfftGmTZvUuXNnPfroo3r//fe1ceNGdejQQeXKlVNiYqLjMsmWLVu61Zc7atasKUn64IMPFBAQIF9fX0VGRqpq1aqqUKGChg8fLmOMihUrptWrVysuLi5dH7Vq1XKs16ioKHl7e6tKlSoZ7uF59tln9d577ykqKkrHjh1TrVq19PXXX+uNN95Q+/btHct6u4YMGaKFCxeqQ4cOGjt2rMLDw7V27VpNnz5dL7zwgipXrpwj80nz0ksv6f3331d0dLS6dOmSo+MeEhKili1bKiYmRkWLFlV4eLg2bNig5cuXu1RbrVq1tGTJEi1dulTly5eXr6+vY8wyU7x4cT300EN69dVX5e/vr+nTp+unn35y+nAcPXq01qxZoxYtWmjUqFEqVqyYFi1apLVr12rixIkKCgrK5tpMX//mzZu1evVqhYaGKiAgINNQ3qFDB02ZMkXdu3fXX//6V507d06TJ09O9wHtjn/+859atWqVHnroIY0aNUp+fn567733dPny5Wz36c6YtG3bVk2aNNGwYcOUkJCg+vXra9u2bY5wf/PXTGQkMDBQDz74oCZNmqTixYsrIiJCW7Zs0Zw5c1SkSJFsLW9ERITGjh2rkSNH6siRI2rbtq2KFi2q3377Td9++638/f0VHR2dvRVkNR49lTcfWLp0qenevbupVKmSKVy4sPH29jblypUzzzzzjPnhhx+cps3sqp8bLyM25v+uQrjxUkVjjJk3b56RZHbs2OFoS7ui4l//+pepUaOG8fHxMREREWbKlClOz83oyoC09l69epnSpUsbb29vU6JECdO4cWMzbty4Wy67JNO/f/8MH3Ol37Tl/PDDD82gQYNMiRIljN1uNw888IDZuXOnU39RUVHG398/w3klJyebyZMnmzp16hhfX19TuHBhU7VqVfO3v/3NHDp0yBjz52WYjz76qAkPDzd2u90EBwebZs2amVWrVrnd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P5xuZ8+eVWxsrO6991598cUXuVEjAADIp9zeo3LjF72ladWqlex2u4YMGaJdu3blSGEAAABu71HJTIkSJXTw4MGc6g4AAMD9PSrff/+9031jjE6fPq3x48erTp06OVYYAACA20Glbt26stlsMsY4td9///2aO3dujhUGAADgdlA5evSo0/0CBQqoRIkS8vX1zbGiAAAApGwElfDw8HRtFy5cIKgAAIAc5/bJtBMmTNDSpUsd97t06aJixYqpdOnS2rt3b44WBwAA8je3g8rMmTMdPwQYFxenuLg4xcbGql27dnr55ZdzvEAAAJB/uX3o5/Tp046gsmbNGnXp0kWtW7dWRESEGjZsmOMFAgCA/MvtPSpFixbVyZMnJUmxsbFq2bKlpD8vU3bn6/MBAABuxe09Ko899pi6d++uSpUq6dy5c2rXrp0kac+ePapYsWKOFwgAAPIvt4PKW2+9pYiICJ08eVITJ05U4cKFJf15SKhfv345XiAAAMi/3A4q3t7eeumll9K1Dx48OCfqAQAAcMjWb/18+OGHatq0qcLCwnT8+HFJ0tSpU/Xpp5/maHEAACB/czuozJgxQ0OHDlW7du104cIFxwm0RYoU0dSpU3O6PgAAkI+5HVTeffddzZo1SyNHjlTBggUd7Q0aNNC+fftytDgAAJC/uR1Ujh49qnvuuSddu91u1+XLl3OkKAAAACkbQSUyMlJ79uxJ1/7555+revXqOVETAACApGxc9fPyyy+rf//+SkxMlDFG3377rRYvXqyYmBjNnj07N2oEAAD5lNtB5bnnntP169f197//XVeuXFH37t1VunRpvf322+rWrVtu1AgAAPIpt4OKJPXp00d9+vTR77//rtTUVJUsWVKS9Ouvv6p06dI5WiAAAMi/svU9KmmKFy+ukiVL6syZMxo4cCBfoQ8AAHKUy0HlwoUL6tGjh0qUKKGwsDC98847Sk1N1ahRo1S+fHlt375dc+fOzc1aAQBAPuPyoZ9//OMf+vLLLxUVFaXY2FgNGTJEsbGxSkxM1Oeff65mzZrlZp0AACAfcjmorF27VvPmzVPLli3Vr18/VaxYUZUrV+bbaAEAQK5x+dDPqVOnHN+TUr58efn6+qp37965VhgAAIDLQSU1NVXe3t6O+wULFpS/v3+uFAUAACC5cejHGKOePXvKbrdLkhITE9W3b990YWX5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bjmtx4KKj4+P6tevr7i4OD366KOO9ri4OHXu3DnD59jtdtntdqe2IkWK5GaZkqTAwMC77kWZ5m5eNunuXr67edkkli8vu5uXTbq7l+9OLltQUJBL03ksqEjS0KFD9cwzz6hBgwZq1KiRPvjgA504cUJ9+/b1ZFkAAMAiPBpUunbtqnPnzmns2LE6ffq0atasqc8++0zh4eGeLAsAAFiER4OKJPXr10/9+vXzdBkZstvtGj16dLrDTXeDu3nZpLt7+e7mZZNYvrzsbl426e5ePisvm80YV64NAgAAuPM8/ls/AAAAmSGoAAAAyyKoAAAAyyKoAAAAyyKoZGL69OmKjIyUr6+v6tevr6+++srTJbktJiZG9957rwICAlSyZEn95S9/0cGDB52m6dmzp2w2m9Pt/vvv91DF7hkzZky62kNCQhyPG2M0ZswYhYWFqVChQmrevLkOHDjgwYrdExERkW75bDab+vfvLylvjd2XX36pTp06KSwsTDabTStXrnR63JWxSkpK0sCBA1W8eHH5+/vrkUce0S+//HIHlyJzWS1fcnKyXnnlFdWqVUv+/v4KCwvTs88+q1OnTjn10bx583Tj2a1btzu8JOndauxceR3m1bGTlOE2aLPZNGnSJMc0Vh07Vz4D8sK2R1DJwNKlSzV48GCNHDlS3333nR544AG1a9dOJ06c8HRpbtmyZYv69++v7du3Ky4uTtevX1fr1q11+fJlp+natm2r06dPO26fffaZhyp2X40aNZxq37dvn+OxiRMnasqUKZo2bZp27NihkJAQtWrVShcvXvRgxa7bsWOH07LFxcVJkp588knHNHll7C5fvqw6depo2rRpGT7uylgNHjxYK1as0JIlS/T111/r0qVL6tixo1JSUu7UYmQqq+W7cuWKdu/erVdffVW7d+/W8uXL9fPPP+uRRx5JN22fPn2cxnPmzJl3ovws3WrspFu/DvPq2ElyWq7Tp09r7ty5stlsevzxx52ms+LYufIZkCe2vdv8bcG70n333Wf69u3r1Fa1alUzfPhwD1WUM86ePWskmS1btjjaoqKiTOfOnT1X1G0YPXq0qVOnToaPpaammpCQEDN+/HhHW2JiogkKCjLvv//+HaowZ7344oumQoUKJjU11RiTd8dOklmxYoXjvitjdeHCBePt7W2WLFnimObXX381BQoUMLGxsXesdlfcvHwZ+fbbb40kc/z4cUdbs2bNzIsvvpi7xd2mjJbtVq/Du23sOnfubB566CGntrwwdsak/wzIK9see1Rucu3aNe3atUutW7d2am/durW2bt3qoapyRnx8vCSpWLFiTu2bN29WyZIlVblyZfXp00dnz571RHnZcujQIYWFhSkyMlLdunXTkSNHJElHjx7VmTNnnMbRbrerWbNmeXIcr127po8++ki9evVy+gHOvDx2aVwZq127dik5OdlpmrCwMNWsWTNPjmd8fLxsNlu63ypbtGiRihcvrho1auill17KM3v/snod3k1j99tvv2nt2rV6/vnn0z2WF8bu5s+AvLLtefybaa3m999/V0pKSrpfcC5VqlS6X3rOS4wxGjp0qJo2baqaNWs62tu1a6cnn3xS4eHhOnr0qF599VU99NBD2rVrlyW/ofBGDRs21MKFC1W5cmX99ttvGjdunBo3bqwDBw44xiqjcTx+/Lgnyr0tK1eu1IULF9SzZ09HW14euxu5MlZnzpyRj4+PihYtmm6avLZdJiYmavjw4erevbvTj7/16NFDkZGRCgkJ0f79+zVixAjt3bvXccjPqm71Orybxm7BggUKCAjQY4895tSeF8Yuo8+AvLLtEVQyceP/WqU/B/nmtrxkwIAB+v777/X11187tXft2tXxd82aNdWgQQOFh4dr7dq16TZGq2nXrp3j71q1aqlRo0aqUKGCFixY4DiZ724Zxzlz5qhdu3ZOP4mel8cuI9kZq7w2nsnJyerWrZtSU1M1ffp0p8f69Onj+LtmzZqqVKmSGjRooN27d6tevXp3ulSXZfd1mNfGTpLmzp2rHj16yNfX16k9L4xdZp8BkvW3PQ793KR48eIqWLBguqR49uzZdKkzrxg4cKBWrVqlTZs2qUyZMllOGxoaqvDwcB06dOgOVZdz/P39VatWLR06dMhx9c/dMI7Hjx/X+vXr1bt37yyny6tj58pYhYSE6Nq1a/rjjz8yncbqkpOT1aVLFx09elRxcXFOe1MyUq9ePXl7e+e58bz5dXg3jJ0kffXVVzp48OAtt0PJemOX2WdAXtn2CCo38fHxUf369dPtsouLi1Pjxo09VFX2GGM0YMAALV++XBs3blRkZOQtn3Pu3DmdPHlSoaGhd6DCnJWUlKQff/xRoaGhjt2wN47jtWvXtGXLljw3jvPmzVPJ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/9utD8Dt49APACfNmzdXjRo19MYbb2jatGkaM2aMBg0apMDAQLVr105JSUnauXOn/vjjDw0dOlRvvfWWQkNDVbduXRUoUEDLli1TSEiIihQpogIFCuj+++/X+PHjFRERod9//13//Oc/s5x/RESELl26pA0bNqhOnTry8/OTn59fhtP6+voqKipKkydPVkJCggYNGqQuXbo4zh95+eWXNXr0aFWoUEF169bVvHnztGfPHi1atCjb6yciIkJHjx7Vnj17VKZMGQUEBMhut2e7PwBZY48KgHSGDh2qWbNm6eTJk+rdu7dmz56t+fPnq1atWmrWrJnmz5/v2KNSuHBhTZgwQQ0aNNC9996rY8eO6bPPPnMc9pk7d66Sk5PVoEEDvfjiixo3blyW827cuLH69u2rrl27qkSJEpo4cWKm01asWFGPPfaY2rdvr9atW6tmzZpOl04PGjRIw4YN07Bhw1SrVi3FxsZq1apVqlSpUrbXzeOPP662bduqRYsWKlGihBYvXpztvgDcms3cePAYAPKIMWPGaOXKlXz9PXCXY48KAACwLIIKAACwLA79AAAAy2KPCgAAsCyCCgAAsCyCCgAAsCyCCgAAsCyCCgAAsCyCCgAAsCyCCgAAsCyCCgAAsCyCCgAAsKz/B8upQX4P+nYnAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#relation between test and test_grade\n",
    "test = data['result_points']\n",
    "t_grade = data['result_grade']\n",
    "plt.bar(test, t_grade)\n",
    "plt.xlabel('Result point')\n",
    "plt.ylabel('Result Grade')\n",
    "plt.title('Simple representation of Result point and it grade')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "884f0af1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71f77b5c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "23deab1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import MinMaxScaler\n",
    "scaler = MinMaxScaler()\n",
    "X_train = scaler.fit_transform(x_train)\n",
    "X_test = scaler.transform(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "9717c1ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "53576036",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Support Vector Machine:\n",
      "Accuracy: 0.8491\n",
      "K-Nearest Neighbors:\n",
      "Accuracy: 0.9811\n",
      "Extra Trees:\n",
      "Accuracy: 0.9434\n"
     ]
    }
   ],
   "source": [
    "\n",
    "models = {\n",
    "    'Support Vector Machine': SVC(),\n",
    "    'K-Nearest Neighbors': KNeighborsClassifier(),\n",
    "    'Extra Trees': ExtraTreeClassifier(),\n",
    "} \n",
    "\n",
    "from sklearn.metrics import accuracy_score\n",
    "for name, model in models.items():\n",
    "    model.fit(x_train, y_train)\n",
    "    y_pred = model.predict(x_test)\n",
    "    acc = accuracy_score(y_test, y_pred)\n",
    "    print(f'{name}:\\nAccuracy: {acc:.4f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "d9ef6095",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.9811320754716981\n"
     ]
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier()\n",
    "model.fit(x_train, y_train)\n",
    "y_pred = model.predict(x_test)\n",
    "\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"Accuracy:\", accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "06e417f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the test mark : 80\n",
      "Enter the test grade : A\n",
      "Enter the exam : 18\n",
      "Enter project : 145\n",
      "Enter project grade : A\n",
      "Enter the assignments : 100\n",
      "Enter result points : 189\n",
      "Enter result grade : A\n",
      "Enter year : 2018\n",
      "Enter academic year : 2018/2019\n",
      "Prediction is :  [1]\n",
      "--------------------------------\n",
      "------------Graduate------------\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "tg = {'A':1, 'B':2, 'C':3, 'E':4, 'D':5, 'FX':6, '0':7}\n",
    "pg = {'A':1, 'B':2, 'C':3, 'E':4, 'D':5, 'FX':6, '0':7}\n",
    "rg = {'A':1, 'B':2, 'C':3,'E':4, 'D':5, 'FX':6}\n",
    "ay = {'2019/2020':1, '2017/2018':2, '2018/2019':3, '2016/2017':4}\n",
    "\n",
    "\n",
    "tests = float(input('Enter the test mark : '))\n",
    "tests_grade = input('Enter the test grade : ')\n",
    "exam = int(input('Enter the exam : '))\n",
    "project = float(input('Enter project : '))\n",
    "project_grade = input('Enter project grade : ')\n",
    "assignments = int(input('Enter the assignments : '))\n",
    "result_points = float(input('Enter result points : '))\n",
    "result_grade = input('Enter result grade : ')\n",
    "year = int(input('Enter year : '))\n",
    "acad_year = input('Enter academic year : ')\n",
    "\n",
    "user_input = pd.DataFrame({'tests':[tests],'tests_grade':[tests_grade],'exam':[exam],'project':[project],'project_grade':[project_grade],'assignments':[assignments],'result_points':[result_points],'result_grade':[result_grade],'year':[year],'acad_year':[acad_year]})\n",
    "\n",
    "user_input['tests_grade'] = user_input['tests_grade'].map(tg)\n",
    "user_input['project_grade'] = user_input['project_grade'].map(pg)\n",
    "user_input['result_grade'] = user_input['result_grade'].map(rg)\n",
    "user_input['acad_year'] = user_input['acad_year'].map(ay)\n",
    "\n",
    "prediction = model.predict(user_input)\n",
    "print('Prediction is : ',prediction)\n",
    "if prediction == 1:\n",
    "    print('--------------------------------')\n",
    "    print('------------Graduate------------')\n",
    "    print('--------------------------------')\n",
    "else:\n",
    "    print('---------------------------------')\n",
    "    print('-----------Not Graduate----------')\n",
    "    print('---------------------------------')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2489386",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "837be981",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e33158a0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "827ded6a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}