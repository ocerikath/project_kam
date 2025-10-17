from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to="products/", verbose_name="Картинка")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Lead(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    phone = models.CharField("Номер телефона", max_length=50)
    email = models.EmailField("Почта", blank=True, null=True)
    comment = models.TextField("Комментарий к заказу", blank=True)

    # Опциональная связь с товаром
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт (опционально)",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="leads"
    )
    # Снимок названия продукта (на случай удаления/изменения товара)
    product_name = models.CharField("Название продукта (снимок)", max_length=255, blank=True)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        if self.product_name:
            return f"{self.full_name} — {self.product_name}"
        return f"{self.full_name} — {self.phone}"