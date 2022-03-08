from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ParseMode, KeyboardButton, CallbackQuery



button_hi = KeyboardButton('/start')
oblast_choise_button = KeyboardButton('Выбрать область')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_hi, oblast_choise_button)

with_cyty = KeyboardButton('Выбрать город/район')
without_cyty = KeyboardButton('Продолжить без города')
withorwithout = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(with_cyty, without_cyty)

wiew_results = KeyboardButton('Показать результаты')
wiew_results_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(wiew_results)


all_bel_button = InlineKeyboardButton('Вся Беларусь', callback_data='oblAllBelarus')
minsk_button = InlineKeyboardButton('Минск', callback_data='oblMinsk')
brestskaja_button = InlineKeyboardButton('Брестская', callback_data='oblBrestskaja')
gomelskaja_button = InlineKeyboardButton('Гомельская', callback_data='oblGomelskaja')
grodnenskaja_button = InlineKeyboardButton('Гродненская', callback_data='oblGrodnenskaja')
mogilevskaja_button = InlineKeyboardButton('Могилёвская', callback_data='oblMogilevskaja')
minskaja_button = InlineKeyboardButton('Минская', callback_data='oblMinskaja')
vitebskaja_batton = InlineKeyboardButton('Витебская', callback_data='oblVitebskaja')
oblast_button = InlineKeyboardMarkup(row_width=2).add(all_bel_button,minsk_button,brestskaja_button,gomelskaja_button,
                                                      grodnenskaja_button,mogilevskaja_button,minskaja_button,
                                                      vitebskaja_batton)
#Минск

centralny = InlineKeyboardButton('Центральный', callback_data='mcityCentralny')
sovetsky = InlineKeyboardButton('Советский', callback_data='mcitySovetsky')
pervomajsky = InlineKeyboardButton('Первомайский', callback_data='mcityPervomajsky')
partizansky = InlineKeyboardButton('Партизанский', callback_data='mcityPartizansky')
zavodskoy = InlineKeyboardButton('Заводской', callback_data='mcityZavodskoy')
leninsky = InlineKeyboardButton('Ленинский', callback_data='mcityLeninsky')
octiabrsky = InlineKeyboardButton('Октябрьский', callback_data='mcityOctiabrsky')
moskowsky = InlineKeyboardButton('Московский', callback_data='mcityMoskowsky')
frunzensky = InlineKeyboardButton('Фрунзенский', callback_data='mcityFrunzensky')

obl_minsk_city_button = InlineKeyboardMarkup(row_width=2).add(centralny, sovetsky, pervomajsky, partizansky, zavodskoy,
                                                              leninsky, octiabrsky, moskowsky, frunzensky)

#Брест

brest = InlineKeyboardButton('Брест', callback_data='brcityBrest')
baranovichi = InlineKeyboardButton('Барановичи', callback_data='brcityBaranovichi')
bereza = InlineKeyboardButton('Береза', callback_data='brcityBereza')
beloozersk = InlineKeyboardButton('Белоозёрск', callback_data='brcityBeloozersk')
gancevichi = InlineKeyboardButton('Ганцевичи', callback_data='brcityGancevichi')
drogichin = InlineKeyboardButton('Дрогичин', callback_data='brcityDrogichin')
zabinka = InlineKeyboardButton('Жабинка', callback_data='brcityZabinka')
ivanovo = InlineKeyboardButton('Иваново', callback_data='brcityIvanovo')
ivancevichi = InlineKeyboardButton('Ивацевичи', callback_data='brcityIvancevichi')
kamenec = InlineKeyboardButton('Каменец', callback_data='brcityKamenec')
kobrin = InlineKeyboardButton('Кобрин', callback_data='brcityKobrin')
luninech = InlineKeyboardButton('Лунинец', callback_data='brcityLuninech')
liachovichi = InlineKeyboardButton('Ляховичи', callback_data='brcityLiachovichi')
malorita = InlineKeyboardButton('Малорита', callback_data='brcityMalorita')
pinsk = InlineKeyboardButton('Пинск', callback_data='brcityPinsk')
prudjany = InlineKeyboardButton('Пружаны', callback_data='brcityPrudjany')
stolin = InlineKeyboardButton('Столин', callback_data='brcityStolin')
othercitys = InlineKeyboardButton('Другие города', callback_data='brcityOthercitys')

obl_brest_city_button = InlineKeyboardMarkup(row_width=2).add(brest,baranovichi,bereza,beloozersk,gancevichi,drogichin,
                                                              zabinka,ivanovo,ivancevichi,kamenec,kobrin,luninech,
                                                              liachovichi,malorita,pinsk,prudjany,stolin,othercitys)


#Гомель

pervomajsky = InlineKeyboardButton('', callback_data='gomcity')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')
pervomajsky = InlineKeyboardButton('', callback_data='city')



