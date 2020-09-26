#from deeppavlov.utils.telegram import interact_model_by_telegram
from deeppavlov import build_model

model = build_model("rusentiment_elmo_twitter_cnn", download=True)
model(['Привет, хорошая погода сегодня!'])
#interact_model_by_telegram(model_config="rusentiment_elmo_twitter_cnn", token="1398003417:AAEvwrq9O7H-OFeUh5GwGkEuxvpkWMlFl-s")