import pandas as pd

def main():
    data = pd.read_csv("pbp_0022501193.csv")
    # print(data)
    data["nemby"] = data["description"].str.split("(Nembhard").str[1]
    print(data["nemby"])

if __name__ == "__main__":
    main()