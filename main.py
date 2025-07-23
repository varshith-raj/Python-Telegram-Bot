import os
import telebot

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['dash'])
def dash(message) :
  bot.send_message(message.chat.id, "Hello.")
@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, """Hello! Welcome To CollegeInfoBot! 
Click on /menu for state wise college Information""")
@bot.message_handler(commands=['help']) 
def help(message):
  bot.reply_to(message, "Hey! Hows it going..")
@bot.message_handler(commands=['menu'])
def menu(message):
  bot.reply_to(message, """Here is the menu
  select your State:
  /Telangana -> Telangana colleges
  /Andhra -> Andhra Pradesh colleges
  /Karnataka -> Karnataka colleges
  /Tamilnadu -> Tamil Nadu colleges
  /Kerala -> Kerala colleges
  /Maharashtra -> Maharashtra colleges
  
               """)
@bot.message_handler(commands=['Telangana'])
def Telangana(message):
  bot.reply_to(message, """Here are the colleges in Telangana:
  1.IIT Hyderabad - Indian Institute of Technology - [IITH], Hyderabad,Telangana, India
  2.NIT Warangal, Warangal
  3.International Institute of Information Technology - [IIIT], Hyderabad
  4.Jawaharlal Nehru Technological University - [JNTUH], Hyderabad
  5.University College of Engineering, Osmania University - [UCE], 
    Hyderabad
  6.Chaitanya Bharathi Institute of Technology - [CBIT], Hyderabad
  7.Vallurupalli Nageswara Rao Vignana Jyothi Institute of Engineering 
    and Technology - [VNR VJIET], Hyderabad
  8.CVR College of Engineering, Ibrahimpatnam, Rangareddy
  9.Institute of Aeronautical Engineering - [IARE], Hyderabad
  10. BV Raju Institute of Technology - [BVRIT], Hyderabad""")    
@bot.message_handler(commands=['Andhra'])
def Andhra(message):
  bot.reply_to(message, """Here are the colleges in Andhra Pradesh:
1.KL University Guntur - Koneru Lakshmaiah Education Foundation, Guntur
2.IIT Tirupati - Indian Institute of Technology Tirupati
3.Vignan's Foundation for Science Technology and Research, Guntur
4.Andhra University College of Engineering, Visakhapatnam
5.JNTUK Kakinada - Jawaharlal Nehru Technological University, Kakinada
6.GITAM University - GITAM University, Visakhapatnam
7.MB College of Engineering and Technology, Mohan Babu University, Tirupati
8.JNTUA Anantapur - Jawaharlal Nehru Technological University, Anantapur
9.SVU Tirupati - Sri Venkateswara University, Tirupati
10.Velagapudi Ramakrishna Siddhartha Engineering College (VRSEC), 
  Vijayawada""")
@bot.message_handler(commands=['Karnataka'])
def Karnataka(message):
  bot.reply_to(message, """Here are the colleges in Karnataka:
  1.NIT Surathkal (NITK) - National Institute of Technology Karnataka 
    Surathkal
  2.Visvesvaraya Technological University, Belagavi
  3.M0IT Manipal - Manipal Institute of Technology, Manipal
  4.IIIT Bangalore - International Institute of Information Technology 
    Bangalore
  5.MSRIT Bangalore - Ramaiah Institute of Technology, Bangalore
  6.IIT Dharwad - Indian Institute of Technology Dharwad
  7.RVCE Bangalore - RV College of Engineering, Bangalore
  8.SIT Tumkur - Siddaganga Institute of Technology, Tumkur
  9.NMAM Institute of Technology, Karkala Taluk
  10.BMSCE Bangalore - BMS College of Engineering, Bangalore""")
@bot.message_handler(commands=['Tamilnadu'])
def Tamilnadu(message):
  bot.reply_to(message, """Here are the colleges in Tamil Nadu:
  1.IIT Madras - Indian Institute of Technology Madras
  2.NIT Trichy - National Institute of Technology Tiruchirappalli
  3.VIT Vellore - Vellore Institute of Technology, Vellore
  4.Amrita Vishwa Vidyapeetham, Coimbatore
  5.SRM University Chennai - SRM Institute of Science and Technology, 
    Chennai
  6.SASTRA University Thanjavur - Shanmugha Arts Science Technology
  7.Kalasalingam Academy of Research and Education, Virudhunagar
  8.Sri Sivasubramaniya Nadar College of Engineering, Kalavakkam
  9.PSG Tech Coimbatore - PSG College of Technology, Coimbatore
  10.SIMATS Chennai - Saveetha Institute of Medical and Technical 
     Sciences,chennai""")
@bot.message_handler(commands=['Kerala'])
def Kerala(message):
  bot.reply_to(message, """Here are the colleges in Kerala:
  1. NIT Calicut - National Institute of Technology
  2. IIST - Indian Institute of Space Science and Technology
  3. IIT Palakkad - Indian Institute of Technology
  4. College of Engineering, Trivandrum
  5.IIIT Kottayam - Indian Institute of Information Technology, Kottayam
  6.Sree Buddha College of Engineering, Alappuzha
  7.MACE Kothamangalam - Mar Athanasius College of Engineering
  8.Mar Baselios Institute of Technology and Science, Ernakulam
  9.MBCET - Mar Baselios College of Engineering and Technology
  10.Marian Engineering College, Thiruvananthapuram""")
@bot.message_handler(commands=['Maharashtra'])
def Maharashtra(message):
  bot.reply_to(message, """Here are the colleges in Maharashtra:
 r""")
  

bot.polling()
