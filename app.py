#Open Weather Maps kulcs: 8896cf78c022c0ec61fac18730502f42

import json
from omw_api import Owm
import files

weather = Owm("demecser", "8896cf78c022c0ec61fac18730502f42")
actualWeather = weather.get_weather().json()
testFile = files.Files("test.json")
print(testFile.get_json_file())
