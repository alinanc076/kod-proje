meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "MTA": "Çok Nadir Görüle Bir Mesaj",
            "MINECRAFT": "İlginç bir sonuç",
            "SONOYUNCU": "Bro Çok Klasiksin!",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print(meme_dict[word])
