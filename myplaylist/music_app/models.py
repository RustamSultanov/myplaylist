from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import BaseUserManager
from audiofield.models import AudioFile

class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, profile_picture=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.profile_picture = profile_picture
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):    
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(upload_to='user_data/profile_picture', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Track(AudioFile):
	artist = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='upload/audiofiles_img', null=True, blank=True)
	
# # Create your models here.
# # def get_custom_username(self):
# # 	return f"Компания: {self.username}, сотрудник: {self.first_name} {self.last_name}"
# # User.add_to_class("__str__",get_custom_username)

# GOV_CHOICE = ((0, 'Россия'),(1, 'Украина'),(2, 'Абхазия'),(3, 'Австралия'),(4, 'Австрия'),(5, 'Азербайджан'),(6, 'Албания'),(7, 'Алжир'),(8, 'Ангола'),(9, 'Ангилья'),(10, 'Андорра'),(11, 'Антигуа и Барбуда'),(12, 'Антильские о-ва'),(13, 'Аргентина'),(14, 'Армения'),(15, 'Арулько'),(16, 'Афганистан'),(17, 'Багамские о-ва'),(18, 'Бангладеш'),(19, 'Барбадос'),(20, 'Бахрейн'),(21, 'Беларусь'),(22, 'Белиз'),(23, 'Бельгия'),(24, 'Бенин'),(25, 'Бермуды'),(26, 'Болгария'),(27, 'Боливия'),(28, 'Босния/Герцеговина'),(29, 'Ботсвана'),(30, 'Бразилия'),(31, 'Британские Виргинские о-ва'),(32, 'Бруней'),(33, 'Буркина Фасо'),(34, 'Бурунди'),(35, 'Бутан'),(36, 'Валлис и Футуна о-ва'),(37, 'Вануату'),(38, 'Великобритания'),(39, 'Венгрия'),(40, 'Венесуэла'),(41, 'Восточный Тимор'),(42, 'Вьетнам'),(43, 'Габон'),(44, 'Гаити'),(45, 'Гайана'),(46, 'Гамбия'),(47, 'Гана'),(48, 'Гваделупа'),(49, 'Гватемала'),(50, 'Гвинея'),(51, 'Гвинея-Бисау'),(52, 'Германия'),(53, 'Гернси о-в'),(54, 'Гибралтар'),(55, 'Гондурас'),(56, 'Гонконг'),(57, 'Гренада'),(58, 'Гренландия'),(59, 'Греция'),(60, 'Грузия'),(61, 'Дания'),(62, 'Джерси о-в'),(63, 'Джибути'),(64, 'Доминиканская республика'),(65, 'Египет'),(66, 'Замбия'),(67, 'Западная Сахара'),(68, 'Зимбабве'),(69, 'Израиль'),(70, 'Индия'),(71, 'Индонезия'),(72, 'Иордания'),(73, 'Ирак'),(74, 'Иран'),(75, 'Ирландия'),(76, 'Исландия'),(77, 'Испания'),(78, 'Италия'),(79, 'Йемен'),(80, 'Кабо-Верде'),(81, 'Казахстан'),(82, 'Камбоджа'),(83, 'Камерун'),(84, 'Канада'),(85, 'Катар'),(86, 'Кения'),(87, 'Кипр'),(88, 'Кирибати'),(89, 'Китай'),(90, 'Колумбия'),(91, 'Коморские о-ва'),(92, 'Конго (Brazzaville)'),(93, 'Конго (Kinshasa)'),(94, 'Коста-Рика'),(95, 'Кот-д`Ивуар'),(96, 'Куба'),(97, 'Кувейт'),(98, 'Кука о-ва'),(99, 'Кыргызстан'),(100, 'Лаос'),(101, 'Латвия'),(102, 'Лесото'),(103, 'Либерия'),(104, 'Ливан'),(105, 'Ливия'),(106, 'Литва'),(107, 'Лихтенштейн'),(108, 'Люксембург'),(109, 'Маврикий'),(110, 'Мавритания'),(111, 'Мадагаскар'),(112, 'Македония'),(113, 'Малави'),(114, 'Малайзия'),(115, 'Мали'),(116, 'Мальдивские о-ва'),(117, 'Мальта'),(118, 'Мартиника о-в'),(119, 'Мексика'),(120, 'Мозамбик'),(121, 'Молдова'),(122, 'Монако'),(123, 'Монголия'),(124, 'Марокко'),(125, 'Мьянма (Бирма)'),(126, 'Мэн о-в'),(127, 'Намибия'),(128, 'Науру'),(129, 'Непал'),(130, 'Нигер'),(131, 'Нигерия'),(132, 'Нидерланды (Голландия)'),(133, 'Никарагуа'),(134, 'Новая Зеландия'),(135, 'Новая Каледония о-в'),(136, 'Норвегия'),(137, 'Норфолк о-в'),(138, 'О.А.Э.'),(139, 'Оман'),(140, 'Пакистан'),(141, 'Панама'),(142, 'Папуа Новая Гвинея'),(143, 'Парагвай'),(144, 'Перу'),(145, 'Питкэрн о-в'),(146, 'Польша'),(147, 'Португалия'),(148, 'Пуэрто Рико'),(149, 'Реюньон'),(150, 'Руанда'),(151, 'Румыния'),(152, 'США'),(153, 'Сальвадор'),(154, 'Самоа'),(155, 'Сан-Марино'),(156, 'Сан-Томе и Принсипи'),(157, 'Саудовская Аравия'),(158, 'Свазиленд'),(159, 'Святая Люсия'),(160, 'Святой Елены о-в'),(161, 'Северная Корея'),(162, 'Сейшеллы'),(163, 'Сен-Пьер и Микелон'),(164, 'Сенегал'),(165, 'Сент Китс и Невис'),(166, 'Сент-Винсент и Гренадины'),(167, 'Сербия'),(168, 'Сингапур'),(169, 'Сирия'),(170, 'Словакия'),(171, 'Словения'),(172, 'Соломоновы о-ва'),(173, 'Сомали'),(174, 'Судан'),(175, 'Суринам'),(176, 'Сьерра-Леоне'),(177, 'Таджикистан'),(178, 'Тайвань'),(179, 'Таиланд'),(180, 'Танзания'),(181, 'Того'),(182, 'Токелау о-ва'),(183, 'Тонга'),(184, 'Тринидад и Тобаго'),(185, 'Тувалу'),(186, 'Тунис'),(187, 'Туркменистан'),(188, 'Туркс и Кейкос'),(189, 'Турция'),(190, 'Уганда'),(191, 'Узбекистан'),(192, 'Уругвай'),(193, 'Фарерские о-ва'),(194, 'Фиджи'),(195, 'Филиппины'),(196, 'Финляндия'),(197, 'Франция'),(198, 'Французская Гвинея'),(199, 'Французская Полинезия'),(200, 'Хорватия'),(201, 'Чад'),(202, 'Черногория'),(203, 'Чехия'),(204, 'Чили'),(205, 'Швейцария'),(206, 'Швеция'),(207, 'Шри-Ланка'),(208, 'Эквадор'),(209, 'Экваториальная Гвинея'),(210, 'Эритрея'),(211, 'Эстония'),(212, 'Эфиопия'),(213, 'ЮАР'),(214, 'Южная Корея'),(215, 'Южная Осетия'),(216, 'Ямайка'),(217, 'Япония'))


# class UserAccept(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	company = models.CharField(max_length=100,blank=True)
# 	position = models.CharField(max_length=100,blank=True)
# 	phone_number = PhoneNumberField(null=True)
# 	avatar= models.ImageField(blank=True)
# 	imp = models.BooleanField(blank=True,default=False)
# 	date_birth = models.DateField(blank=True,null=True)
# 	gov = models.IntegerField(choices=GOV_CHOICE, default=0)
# 	social_net = models.URLField(max_length=200,blank=True)
# 	RATING_CHOICE = (
#         (1, "Ужасно"),
#         (2, "Плохо"),
#         (3, "Нормально"),
#         (4, "Хорошо"),
#         (5, "Отлично"),
#     )
# 	rating = models.IntegerField(choices=RATING_CHOICE, default=5)
# 	def __str__(self):
# 		return f"{self.user}"



# class Competence(MPTTModel):
#     competence_name = models.CharField(max_length=256)
#     name = models.CharField(max_length=256, unique=True,)
#     owner = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

#     class MPTTMeta:
#         order_insertion_by = ['name']

#     def __str__(self):
#         return f"#{self.id} {self.competence_name}; Создал: {self.owner.username}"




# class Comment(models.Model):

# 	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='user')
# 	competence = models.ManyToManyField(Competence)
# 	implementer = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='implementer')
# 	customer = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='customer')
# 	init_user = models.ForeignKey(on_delete=models.CASCADE,to=User,related_name='init_user')
# 	implementer_flag = models.BooleanField(blank=True,default=False)
# 	customer_flag = models.BooleanField(blank=True,default=False)
# 	recipient_user = models.ManyToManyField(User)
# 	adition_user = models.ManyToManyField(User,related_name='adition_user',blank=True,)
# 	employee = models.ManyToManyField(User,related_name='employee_list',blank=True)
# 	another_employee = models.ManyToManyField(User,related_name='another_employee',blank=True)
# 	comment_text = models.TextField()
# 	date_update = models.DateTimeField(auto_now=True,blank=True,null=True)
# 	date_create = models.DateTimeField(auto_now_add=True)
# 	accept=models.BooleanField(blank=True,default=False)
# 	hide=models.BooleanField(blank=True,default=False)
# 	failure=models.BooleanField(blank=True,default=False)
# 	failure_text = models.TextField(blank=True,null=True)
# 	RATING_CHOICE = (
#         (1, "Ужасно"),
#         (2, "Плохо"),
#         (3, "Нормально"),
#         (4, "Хорошо"),
#         (5, "Отлично"),
#     )
# 	rating = models.IntegerField(choices=RATING_CHOICE, default=5)
# 	rating_competence = models.IntegerField(choices=RATING_CHOICE, default=4)
# 	rating_employee = models.IntegerField(choices=RATING_CHOICE, default=4)
# 	files = models.FileField(blank=True)
# 	def __str__(self):
# 		return f"автор: {self.user}, дата: {self.date_create}"

# 	class Meta:
# 		verbose_name = 'Отзыв'
# 		verbose_name_plural = 'Отзывы'


# class Disputs(models.Model):

# 	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='user_disput')
# 	comment = models.ForeignKey(on_delete=models.CASCADE,to=Comment,related_name='comment')
# 	text = models.TextField()
# 	date_create = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return f"{self.comment}"

# 	class Meta:
# 		verbose_name = 'Комментарий'
# 		verbose_name_plural = 'Комментарии'


# class Rubricator(MPTTModel):
#     name = models.CharField(max_length=256, unique=True,)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)

#     class MPTTMeta:
#         order_insertion_by = ['name']

#     def __str__(self):
#         return f"{self.name}"

# class Appeal(models.Model):
# 	size = models.PositiveSmallIntegerField()
# 	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='user_appeal')
# 	accepter = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='accepter_appeal')
# 	accept=models.BooleanField(blank=True,default=False)
# 	failure=models.BooleanField(blank=True,default=False)
# 	rubricator = models.ForeignKey(on_delete=models.CASCADE,to=Rubricator)
# 	text = models.TextField(blank=True)
# 	date_create = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return f"{self.date_create}"


# class MessegesAppeal(models.Model):
# 	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='user_messeges')
# 	accepter = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,related_name='accepter')
# 	appeal = models.ForeignKey(on_delete=models.CASCADE,to=Appeal)
# 	text = models.TextField()
# 	date_create = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return f"{self.date_create}"

# 	class Meta:
# 		verbose_name = 'Сообщение'
# 		verbose_name_plural = 'Сообщения'