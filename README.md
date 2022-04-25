# stm-feature-extraction
Paper title: Speed Transition Matrix Feature Extraction for Traffic State Estimation Using Machine Learning Algorithms  
Extracting features from novel traffic data modeling technique called Speed Transition Matrix (STM). After the feature extraction, results are evaluated on different machine learning algorithms using labeled STMs.  
You can learn more about STMs by reading these articles:  
- [Speed Transition Matrix: Novel road traffic data modeling technique](https://medium.com/analytics-vidhya/speed-transition-matrix-novel-road-traffic-data-modeling-technique-d37bd82398d1)
- [Traffic State Estimation and Classification on Citywide Scale Using Speed Transition Matrices](https://www.researchgate.net/publication/344138884_Traffic_State_Estimation_and_Classification_on_Citywide_Scale_Using_Speed_Transition_Matrices)

## Instalation
It is always recommended to use virtual environments and install packages from `requirements.txt`.  
But, you can go ahead with `python -m pip install numpy pandas matplotlib sklearn` if you want.  

## Usage
1. **Input data**  
Data is not provided for this project but, you can contact me to send you some test data.  
Input data is composed of a list of dictionaries that contains STMs and metadata.  
This is the example of one entry in the dictionary:  
```
{
  "stm": (ndarray),   # Two dimensional numpy array.
  "interval": (int),  # Time interval 0 to 7.
  "season": (str),    # If 'summer' data is collected in July and August if 'winter' then other months.
  "day": (str),       # 'working' or 'weekend'
  "origin_id": (int)  # Map-matched origin link id for STM
  "dest_id": (int)    # Map-matched destination link id for STM
}
```

2. **Run**  
Run `python main.py`.

## Results
After running the `main.py`, two functions will run:  
1. `extract_features(data_path, save_path)` will run the feature extraction step. All features will be explained in the article that will be published in Sep 2021.
2. `get_comparison(save_path)` will run the comparison of different ML algorithms. All results will be printed into a terminal.

## How to cite
Text:  
Tišljarić, L., Ribić, F., Majstorović, Ž., Carić, T. (2022). Speed Transition Matrix Feature Extraction for Traffic State Estimation Using Machine Learning Algorithms. In: Petrović, M., Novačko, L., Božić, D., Rožić, T. (eds) The Science and Development of Transport—ZIRP 2021. Springer, Cham. https://doi.org/10.1007/978-3-030-97528-9_5

.bib:  
@Inbook{Tišljarić2022,
author="Ti{\v{s}}ljari{\'{c}}, Leo
and Ribi{\'{c}}, Filip
and Majstorovi{\'{c}}, {\v{Z}}eljko
and Cari{\'{c}}, Ton{\v{c}}i",
editor="Petrovi{\'{c}}, Marjana
and Nova{\v{c}}ko, Luka
and Bo{\v{z}}i{\'{c}}, Diana
and Ro{\v{z}}i{\'{c}}, Tomislav",
title="Speed Transition Matrix Feature Extraction for Traffic State Estimation Using Machine Learning Algorithms",
bookTitle="The Science and Development of Transport---ZIRP 2021",
year="2022",
publisher="Springer International Publishing",
address="Cham",
pages="61--74",
isbn="978-3-030-97528-9",
doi="10.1007/978-3-030-97528-9_5",
url="https://doi.org/10.1007/978-3-030-97528-9_5"
}

## Contact and connect
[Leo Tisljaric](https://www.linkedin.com/in/leo-ti%C5%A1ljari%C4%87-28a56b123/)
