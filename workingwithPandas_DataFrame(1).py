{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Virat Kohli</td>\n",
       "      <td>RCB</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M S Dhoni</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Rohit Sharma</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Samson</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kane Williamson</td>\n",
       "      <td>Sun Risers Hyderabad</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 0                     1\n",
       "0      Virat Kohli                   RCB\n",
       "1        M S Dhoni   Chennai Super Kings\n",
       "2     Rohit Sharma        Mumbai Indians\n",
       "3           Samson      Rajasthan Royals\n",
       "4  Kane Williamson  Sun Risers Hyderabad"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# DataFrame is 2 dimensional.\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "ipl_teams_with_captains = pd.DataFrame([[\"Virat Kohli\",\"RCB\"],\n",
    "                                        [\"M S Dhoni\", \"Chennai Super Kings\"],\n",
    "                                        [\"Rohit Sharma\",\"Mumbai Indians\"],\n",
    "                                        [\"Samson\",\"Rajasthan Royals\"],\n",
    "                                        [\"Kane Williamson\",\"Sun Risers Hyderabad\"]\n",
    "                                        \n",
    "    \n",
    "])\n",
    "\n",
    "ipl_teams_with_captains"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>Captain name</th>\n",
       "      <th>Team</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Virat Kohli</td>\n",
       "      <td>RCB</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M S Dhoni</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Rohit Sharma</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Samson</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kane Williamson</td>\n",
       "      <td>Sun Risers Hyderabad</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Captain name                  Team\n",
       "0      Virat Kohli                   RCB\n",
       "1        M S Dhoni   Chennai Super Kings\n",
       "2     Rohit Sharma        Mumbai Indians\n",
       "3           Samson      Rajasthan Royals\n",
       "4  Kane Williamson  Sun Risers Hyderabad"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "ipl_teams_with_captains = pd.DataFrame([[\"Virat Kohli\",\"RCB\"],\n",
    "                                        [\"M S Dhoni\", \"Chennai Super Kings\"],\n",
    "                                        [\"Rohit Sharma\",\"Mumbai Indians\"],\n",
    "                                        [\"Samson\",\"Rajasthan Royals\"],\n",
    "                                        [\"Kane Williamson\",\"Sun Risers Hyderabad\"]],\n",
    "                                      columns = [\"Captain name\",\"Team\"])\n",
    "\n",
    "ipl_teams_with_captains"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
