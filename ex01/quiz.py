import random

def main():
    collect=shutsudai()
    kaitou(collect)

def shutsudai():
    ex1=[
        {"q":"サザエの旦那の名前は？","a":["ますお","マスオ"]},
        {"q":"カツオの妹の名前は？","a":["わかめ","ワカメ"]},
        {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}
    ]
    rq=random.randint(0,2)
    print("問題:")
    print(ex1[rq]["q"])
    return ex1[rq]["a"]

def kaitou(collect):
    ans=input("答えるんだ:")
    if ans in collect:
        print("正解！！！")
    else:
        print("出直してこい")


if __name__ == "__main__":
    main()
    