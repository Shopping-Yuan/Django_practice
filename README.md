my_website是整個網站資料夾
作為練習用的資料是來自genius_invokation卡牌遊戲的卡片相關資訊，
使用mysql系統，將資料儲存在genius_invokation資料庫裡的all_card表中，
每一筆資料代表一張(種)卡片，存入編號、名稱、類型共三項屬性。

目前網站的功能有:
1.在後台檢視、新增、刪除mysql資料庫中的資料
當網址為 http://127.0.0.1:8000/admin/ 時，透過my_web中的urls.py，
將請求轉發給catalog/admin.py，而admin.py將會import資料夾下的models.py，
用all_card物件的屬性，呈現資料庫中的資料(可能有用到Django的預設的後台網頁模板)

2.在網站首頁檢視目前mysql資料庫中的所有資料
當進入首頁時，透過mysite以及catalog資料夾中的urls.py，將請求轉到views.py中，
views.py由mysql資料庫抓取資料，並藉由template.py中的index.html模板生成網頁。

3.接下來要實作的功能是在網頁上輸入資料並存入mysql資料庫中，需要為model.py下的
all_card類別新增新的method，以及新增view和template以顯示網頁。
