import re
import os
import pandas as pd

DIR = r"D:\SteamLibrary\steamapps\common\FPSAimTrainer\FPSAimTrainer\stats"
BENCHMARKS = [
    "Pasu Voltaic Easy", "B180 Voltaic Easy", "Popcorn Voltaic Easy",
    "ww3t Voltaic", "1w4ts Voltaic", "6 Sphere Hipfire Voltaic",
    "Smoothbot Voltaic Easy", "Air Angelic 4 Voltaic Easy", "PGTI Voltaic Easy",
    "FuglaaXYZ Voltaic Easy", "Ground Plaza Voltaic Easy", "Air Voltaic Easy",
    "patTS Voltaic Easy", "psalmTS Voltaic Easy", "voxTS Voltaic Easy",
    "kinTS Voltaic Easy", "B180T Voltaic Easy", "Smoothbot TS Voltaic Easy"
]
DYNAMIC = {"Pasu Voltaic Easy", "B180 Voltaic Easy", "Popcorn Voltaic Easy", "Pasu Voltaic", "B180 Voltaic", "Popcorn Voltaic"}
STATIC = {"ww3t Voltaic", "1w4ts Voltaic", "6 Sphere Hipfire Voltaic"}
PRECISE = {"Smoothbot Voltaic Easy", "Air Angelic 4 Voltaic Easy", "PGTI Voltaic Easy", "Smoothbot Voltaic", "Air Angelic 4 Voltaic", "PGTI Voltaic"}
REACTIVE = {"FuglaaXYZ Voltaic Easy", "Ground Plaza Voltaic Easy", "Air Voltaic Easy", "FuglaaXYZ Voltaic", "Ground Plaza Voltaic", "Air Voltaic"}
SPEED = {"patTS Voltaic Easy", "psalmTS Voltaic Easy", "voxTS Voltaic Easy", "patTS Voltaic", "psalmTS Voltaic", "voxTS Voltaic"}
EVASIVE = {"kinTS Voltaic Easy", "B180T Voltaic Easy", "Smoothbot TS Voltaic Easy", "kinTS Voltaic", "B180T Voltaic", "Smoothbot TS Voltaic"}


def collect_data(easy=True) -> pd.DataFrame:
    if not easy:
        bench = [i.strip(" Easy") for i in BENCHMARKS]
    else:
        bench = BENCHMARKS

    # initialize important containers
    scenario_names = []
    accompaning_score = []
    dates = []
    scenario_type = []
    sub_type = []

    # iterate over the directory that has kovaaks scenario data
    for file in os.listdir(DIR):
        for name in bench:
            # if the scenario is one of the voltaic benchmarks
            if file.startswith(f'{name} - Challenge'):
                # find the name, score, date and save them
                date = file.split()[-2]
                with open(f"{DIR}\\{file}", "r") as f:
                    score = re.search("Score:,(.*)\n", f.read()).group().strip().split(',')[-1]
                    # here im just making sure the re result is a number
                    if score.replace('.','',1).isdigit():
                        # im checking what type of scenario this is
                        # this is mostly for coloring and grouping so less important
                        if name in DYNAMIC or  name in STATIC:
                            scenario_type.append('Clicking')
                            if name in DYNAMIC:
                                sub_type.append('Dynamic')
                            else:
                                sub_type.append('Static')
                        elif name in PRECISE or name in REACTIVE:
                            scenario_type.append('Tracking')
                            if name in PRECISE:
                                sub_type.append('Precise')
                            else:
                                sub_type.append('Reactive')
                        else:
                            scenario_type.append('Switching')
                            if name in SPEED:
                                sub_type.append('Speed')
                            else:
                                sub_type.append('Evasive')
                        scenario_names.append(name)
                        accompaning_score.append(score)
                        dates.append(date) 
                        # not casting now because i would have to cast again
                        # when all data in df to verify data integrity
    return pd.DataFrame.from_dict({
        'scenario_name': scenario_names, 'score': accompaning_score, 
        'date': dates, 'scenario_type': scenario_type, 'sub_type': sub_type,
    })


def play_with_df(df: pd.DataFrame) -> tuple:
    # enforce types because there will be data manipulation and no more data collection
    df.score = df.score.astype('float')
    df.date = pd.to_datetime(df.date, format=r"%Y.%m.%d-%H.%M.%S")

    groups = df.groupby("scenario_name")
    # for scenario in df.scenario_name.unique():
    #     print(f"{scenario} max: {groups.get_group(scenario).score.max()}, Scenario Type: {groups.get_group(scenario).scenario_type.iloc[0]}")
    return df, groups


def main(easy=True):
    return play_with_df(collect_data(easy))


if __name__ == "__main__":
    main()
