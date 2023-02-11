from models import Data_Model

def get_raw_data():
    return [
        ["Kontrol", "Motor Sürücü", "200RPM"],
        ["Robot Kol", "1. Eklem Açısı", "43.7"],
        ["Görüntü", "Aktif Kameralar", "3"],
        ["Deney", "Deney Durumu", "İşleniyor..."]
    ]

def send_raw_data(temperature, speed, lidar_state, active_cams, velocity):
    data_model = Data_Model()
    data_model.temperature = temperature
    data_model.speed = speed
    data_model.lidar_state = lidar_state
    data_model.active_cams = active_cams
    data_model.velocity = velocity
    data_model.save()
    print(data_model)
