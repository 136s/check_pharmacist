﻿# 薬剤師名簿への登録確認
## このリポジトリについて
- [確認したい名前の CSV](list.csv) を読み込んで、登録年のリストをスクレイプする Python スクリプト
- 出力イメージは [output.csv](output.csv)
- list.csv の名前は [公益社団法人日本薬剤師会](https://www.nichiyaku.or.jp/about/summary/publicationAbout.html) の [役員名簿 [PDF]](https://www.nichiyaku.or.jp/assets/uploads/about/202007_meibo.pdf) の方々の名前をお借りした（2021-04-29 現在）

## 環境準備
- 詳しい説明は @memakura さんの [Python + Selenium で Chrome の自動操作を一通り - Qiita](https://qiita.com/memakura/items/20a02161fa7e18d8a693) を参照されたい
- 簡単に言うと以下の 2 行
```
pip install selenium
pip install chromedriver-binary
```
- ChromeDriver のバージョンが Google Chrome とずれてる場合は、同じバージョンの `chromedriver.exe` を [ここ](https://chromedriver.chromium.org/downloads) からダウンロードして、PATH を通す


## LICENSE
- [CC 0](LICENSE)