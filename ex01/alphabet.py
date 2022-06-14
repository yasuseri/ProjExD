import random
import datetime
num_base=10
num_route=5
num_los=2

def main():
    st=datetime.datetime.now()   #時間開始
    for i in range(num_route):
        seikai=shutudai()
        f=kaitou(seikai)
        if f==1:
            break
    en=datetime.datetime.now()   #時間終了
    print(f"{(en-st).seconds}かかった。")

def shutudai():
    alphabets=[chr(c+65) for c in range(26)]
    all_rom=random.sample(alphabets,num_base)
    print(f"対象文字:{all_rom}")   #対象文表示
    num_lost=random.sample(all_rom,num_base)
    print(f"欠損文字:{num_lost}")   #欠損文字表示
    att=[c for c in all_rom if c not in num_lost ]
    print(f"表示文字:{att}")     #表示文字表示
    return all_rom

def kaitou(seikai):
    num=int(input("欠損文字はいくつあるか？"))
    if num!=num_los:
        print("不正解")     #文字で不正解
        return 0
    else:
        print("正解です。欠損文字を一つずつ入力してください")
        for i in range(num_los):
            ans=input(f"{i+1}つ目の文字を入力してください:")
            if ans not in seikai:
                print("不正解")    #文字数で不正解
                return 0
        seikai.remove(ans)
        print("正解です。")     #完全正解
        return 1


if __name__ == "__main__":
    main()