import sys
sys.path.append("../../")
import json
from script.tools.coin_maker import CoinMaker

if __name__ == "__main__":
    config_file_path = sys.argv[1]
    config_file = open(config_file_path, "r")
    config = json.load(config_file)
    config_file.close()

    coin_file = config["coin_file"]
    accounts_info = config["accounts_info"]
    total_amount = config["total_amount"]
    out_path = config["out_path"]

    coin_maker = CoinMaker()
    result = coin_maker.make_coins(coin_file, accounts_info, total_amount)
    # print(json.dumps(result))

    out_file = open(out_path, "w")
    json.dump(result, out_file)
    out_file.close()

    
