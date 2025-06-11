from django.db import models

MAX_LENGTH = 255

class Genre(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Publisher(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название издательства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

class Author(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя')
    last_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='authors/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Book(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='Название книги')
    price = models.FloatField(verbose_name='Цена')
    cover_image = models.ImageField(upload_to='covers/%Y/%m/%d', null=True, blank=True, verbose_name='Обложка')
    is_available = models.BooleanField(default=True, verbose_name='Доступность')

    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Жанр')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, verbose_name='Издательство')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f"{self.title} - ({self.price} руб.)"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Customer(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя')
    last_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия')
    email = models.EmailField(max_length=MAX_LENGTH, unique=True, verbose_name='Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    total_price = models.FloatField(verbose_name='Общая стоимость')
    status = models.CharField(max_length=MAX_LENGTH, default='В обработке', verbose_name='Статус')
    items = models.TextField(null=True, blank=True, verbose_name='Содержимое заказа')

    def __str__(self):
        return f"Заказ #{self.id}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name='Книга')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена доставки')

    def __str__(self):
        return f"{self.book.title} ({self.quantity} шт.)"

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    rating = models.PositiveIntegerField(verbose_name='Оценка', choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Отзыв на {self.book.title} от {self.customer}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'