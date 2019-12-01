# Yumu-akGe

NLP.py

class User:
  def add_event: user objesinin katıldığı etkinlikleri listeye kaydeder.

class Society:
  def add_event: society'nin hazırladığı etkinlikleri listeye kaydeder.

class Event:
  def add_user_rate: userların etkinlik hakkında görüş puanlarını etkinlik objesine kaydeder.

class Database:
  def fetch_from: web sitesinden etkinlik verilerini çeker ve Event objesi listesi olarak return eder.
  
  def import_data: aldığı Event objelerinin bilgilerini kullanarak gerekli formlarda kaydeder.
  
  def calculate_rates: userların etkinlikler hakkındaki görüş puanlarını düzenler.
  
  def recommend: kullanıcının daha önce katıldığı etkinlikleri referans alarak, yeni duyurusu yapılmış bir etkinliğe tahmini bir beğenme puanı verir.
  
  def classify: yeni bir etkinliği, daha önceki etkinliklerin açıklama metinlerinin benzerliği yönünde, hangi topluluk tarafından oluşturulduğunu tahmin eder.
  
  def predict_point: kullanıcıların etkinlikler hakkında yaptığı yorumları değerlendirerek 0-5 arasında beğeni puanı verir.
  
  
  
GUI.py
  
  def add_child_page: ikinci argümanda verilen sayfaları, birinci argümanın alt sayfaları olarak kaydeder.
