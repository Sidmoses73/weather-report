{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-5-6614100cc0b8>, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-5-6614100cc0b8>\"\u001b[1;36m, line \u001b[1;32m4\u001b[0m\n\u001b[1;33m    API_ Key = 'cb771e45ac79a4e8e2205c0ce66ff633'\u001b[0m\n\u001b[1;37m         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from pprint import pprint\n",
    "\n",
    "API_ Key = 'cb771e45ac79a4e8e2205c0ce66ff633'\n",
    "city = input(\"Enter a cty: \")\n",
    "base_url = \"https://openweathermap.org/data/2.5/weather?appid=\"+API_Key+\"&q=\"+city\n",
    "weather_data = request.get(base_url).json()\n",
    "pprint(weather_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
