from enum import Enum


class Category(str, Enum):
    HEALTH = "Salud y bienestar"
    TRANSPORT = "Transporte"
    HOME = "Hogar"
    TECHNOLOGY = "Tecnología"
    FEEDING = "Alimentación"
    ENTERTAINMENT = "Entretenimiento"
    EDUCATION = "Educación"
    OTHER = "Otra"
    FAMILIA = "Familia"
    IMPUESTOS = "Impuestos"
    FECHAS_ESPECIALES = "Fechas especiales"
    VACACIONES = "Vacaciones"