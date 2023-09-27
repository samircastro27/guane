token = {
    "kind": "identitytoolkit#VerifyPasswordResponse",
    "localId": "user_id",
    "email": "guane@example.com",
    "displayName": "",
    "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVhNTA5ZjAxOWY3MGQ3NzlkODBmMTUyZDFhNWQzMzgxMWFiN2NlZjciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20va3lya2d1YW5lIiwiYXVkIjoia3lya2d1YW5lIiwiYXV0aF90aW1lIjoxNjc1ODAxMjE1LCJ1c2VyX2lkIjoiSzgwbnZ6YWN1bmNsYUU2Q2psNDFEemdLUVNhMiIsInN1YiI6Iks4MG52emFjdW5jbGFFNkNqbDQxRHpnS1FTYTIiLCJpYXQiOjE2NzU4MDEyMTUsImV4cCI6MTY3NTgwNDgxNSwiZW1haWwiOiJzaW1vbmdhcmNpYTM2NDBAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInNpbW9uZ2FyY2lhMzY0MEBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.ShUuxBdJz2AkPnm1c0tOese8XdwcEueqGaKmew4jabx3ELoZ1qjnwVnu939B3lK7I8htoefnPV9g2gg44eea5ns-Dhbb2f2XdplxcjRuRo4wnZaO9gFG0NBLaCLZrPFnoL7-Lnbuk5afiKrMtRMEcq-oaAJSnI78AYhGmY0nPvRAP4TIgx8VnJTOww41NIgeFr6_NF-HvIUfE2Komxv9fJx3gCDAqwV8_XK1MXqkWWzxtLN5AwW5i0ZAYbLAaMWcSBz4YEhbmT016RaFBHNJR6pCCJpQ8lYFcX8g1J0arv2NhsCd70CVZj22MesoEEjgm1QpzrsN6U6l-311eWmoiw",
    "registered": True,
    "refreshToken": "APJWN8ei5ALOPiu0uFVr3BFRO2KIa09JVGnaiaOKDTLwUY-WJeJTSY8ArrIJ9-rdNeDjtohZGmMbYM4jYCnFs3T9m6vTB1wkEqb9C2JDxbjyF-_vZy2t1I-WLEUBoS7oLqOv3bOsBh6BYz5j3AFsMSNLhcwAJ2TKBQ4OHB0i5CIV50O482Jyg_gC1dvx2WhIgQr7DGqizBbvefZ9yXhcvyGA1T6EH0VOmQ",
    "expiresIn": "3600",
}


decoded_token = {
    "iss": "https://securetoken.google.com/kyrkguane",
    "aud": "kyrkguane",
    "auth_time": 167512337,
    "user_id": "id_of_user",
    "sub": "id_of_user",
    "iat": 1671234237,
    "exp": 1671234837,
    "email": "guane@example.com",
    "email_verified": False,
    "firebase": {
        "identities": {"email": ["guane@example.com"]},
        "sign_in_provider": "password",
    },
    "uid": "id_of_user",
}

# User
user_post = {
    "uid": "fakeuidfromfirebase",
    "email": "user_1@example.com",
    "name": "fake user name",
    "photo_url": "https://fake-url/photo.png",
    "status": "active",
    "ocupation": "Empleado",
}

user_1_update = {"city_id": 1}

user_response = {
    "uid": "fakeuidfromfirebase2",
    "email": "user_2@example.com",
    "name": "fake user name 2",
    "photo_url": "https://fake-url/photo.png",
    "status": "active",
    "id": 0,
    "city_id": 0,
    "ocupation": "Empleado",
    "other_city": "string",
    "created_at": "2023-02-08T14:44:08.489Z",
    "last_modified": "2023-02-08T14:44:08.489Z",
}

# Income
income_post = {
    "name": "income",
    "type": "single",
    "amount": 19999,
    "user_id": 1,
    "frequency": 1,
    "date": "2023-02-08",
    "inflation": True,
    "end_date": "2025-02-08",
}

income_update = {"name": "income updated"}

income_response = {
    "name": "income",
    "type": "single",
    "amount": 19999,
    "user_id": 1,
    "frequency": 1,
    "date": "2023-02-08",
    "inflation": False,
    "end_date": "2025-02-08",
    "id": 2,
    "created_at": "2023-02-09T00:03:59.884116+00:00",
    "last_modified": "2023-02-09T00:03:59.884134+00:00",
}

# Expenditure
expenditure_post = {
    "name": "string",
    "type": "single",
    "amount": 9765512,
    "user_id": 1,
    "frequency": 1,
    "date": "2023-02-09",
    "inflation": False,
    "end_date": "2024-02-09",
}

expenditure_update = {"name": "expenditure updated"}

expenditure_response = {
    "name": "string",
    "type": "single",
    "amount": 9765512,
    "user_id": 1,
    "frequency": 1,
    "date": "2023-02-09",
    "inflation": False,
    "end_date": "2024-02-09",
    "id": 2,
    "created_at": "2023-02-09T00:03:59.884116+00:00",
    "last_modified": "2023-02-09T00:03:59.884134+00:00",
}


# Saving
saving_post = {
    "name": "string",
    "amount": 12342315,
    "rate": 1.8,
    "months": 11,
    "type": "Risk Free",
    "status": "Option",
    "rate_type": "e.m.",
}

saving_update = {"name": "saving updated"}

saving_response = {
    "name": "string",
    "amount": 123213421,
    "rate": 1.8,
    "months": 11,
    "type": "Risk Free",
    "id": 3,
    "created_at": "2023-02-15T19:50:22.736258+00:00",
    "last_modified": "2023-02-15T19:50:22.736276+00:00",
    "user_id": 1,
}

# Target
target_post = {
    "name": "Carro",
    "amount": 100000000,
    "unemployment_insurance": True,
    "expected_date": "2023-02-17",
    "initial": 0,
}

target_update = {"name": "Mazda 3"}

target_response = {
    "name": "Carro",
    "amount": 100000000,
    "unemployment_insurance": True,
    "expected_date": "2023-02-17",
    "initial": 0,
    "user_id": 1,
    "id": 1,
    "created_at": "2023-02-17T20:19:52.387Z",
    "last_modified": "2023-02-17T20:19:52.387Z",
}
# Loan
loan_post = {
    "name": "Tarjeta crédito",
    "amount": 1,
    "rate": 0.40,
    "months": 6,
    "existent": True,
    "type": "Simple",
    "rate_type": "e.a.",
}

loan_update = {"name": "Tarjeta crédito updated"}

loan_response = {
    "name": "Tarjeta crédito",
    "amount": 1,
    "rate": 0.40,
    "months": 6,
    "existent": True,
    "type": "Simple",
    "rate_type": "e.a.",
    "user_id": 1,
    "id": 1,
    "created_at": "2023-03-21T19:47:57.292173+00:00",
    "last_modified": "2023-03-21T19:47:57.292220+00:00",
}

# Plan
plan_post = {"name": "Plan de ahorros"}

plan_update = {"name": "Plan updated"}

plan_response = {
    "name": "Plan de ahorros",
    "user_id": 1,
    "id": 1,
    "created_at": "2023-02-17T04:38:13.478Z",
    "last_modified": "2023-02-17T04:38:13.478Z",
}

plan_details = {"income_ids": [1, 2]}

plan_full_create = {
    "new_plan": plan_post,
    "incomes": [income_post],
    "expenditures": [expenditure_post],
    "savings": [saving_post],
    "targets": [target_post],
    "loans": [loan_post],
}

plan_detailed = {
    "name": "Plan de ahorros",
    "user_id": 1,
    "id": 1,
    "created_at": "2023-02-17T04:50:18.429566+00:00",
    "last_modified": "2023-02-17T04:50:18.429646+00:00",
    "details": {
        "incomes": [
            {
                "name": "string",
                "type": "single",
                "amount": 0,
                "frequency": 1,
                "date": "2023-02-17",
                "inflation": False,
                "end_date": "2023-02-17",
                "id": 1,
                "created_at": "2023-02-17T04:50:09.303496+00:00",
                "last_modified": "2023-02-17T04:50:09.303541+00:00",
                "user_id": 1,
            }
        ],
        "expenditures": [],
        "savings": [],
    },
}

storage = {
    "created_at": "2023-02-23T21:08:48.535081+00:00",
    "user_id": 1,
    "data": {
        "incomes": [income_post],
        "expenditures": [expenditure_post],
        "savings": [saving_post],
        "targets": [target_post],
    },
    "last_modified": "2023-02-23T22:23:37.171133+00:00",
    "id": 4,
    "step": 2,
}


device_post = {"token": "Token1"}

device_update = {"logged": False}

device_response = {
    "token": "Token1",
    "logged": True,
    "user_id": 1,
    "id": 1,
    "created_at": "2023-03-08T18:57:58.973Z",
    "last_modified": "2023-03-08T18:57:58.973Z",
}

plan_results = {
    "loans": [],
    "mortgages": [],
    "targets": [
        {
            "name": "Moto",
            "planned": 0,
            "stock": 6.9450514,
            "contribution": 0,
            "values": [0, 6.9450514, 0],
            "labels": ["Planeado", "Existente", "Contribución"],
        }
    ],
    "RF_savings": [
        {
            "name": "Ahorro default",
            "months": 6,
            "investment": 0,
            "cashflow": 0,
            "values": [0, 0],
            "labels": ["Inversión", "Flujo de caja"],
        },
        {
            "name": "asdfasdfasd",
            "months": 8,
            "investment": 0,
            "cashflow": 0,
            "values": [0, 0],
            "labels": ["Inversión", "Flujo de caja"],
        },
    ],
    "Per_savings": [
        {
            "name": "Ahorro default, periodico 3 meses\n",
            "months": 3,
            "investment": 0,
            "cashflow": -3.0411189,
            "values": [0, -3.0411189],
            "labels": ["Inversión", "Flujo de caja"],
        },
        {
            "name": "Ahorro default, periodico 9 meses\n",
            "months": 9,
            "investment": 0,
            "cashflow": 0,
            "values": [0, 0],
            "labels": ["Inversión", "Flujo de caja"],
        },
        {
            "name": "Ahorro default, periodico 12 meses",
            "months": 12,
            "investment": 0,
            "cashflow": 0,
            "values": [0, 0],
            "labels": ["Inversión", "Flujo de caja"],
        },
        {
            "name": "Ahorro default, periodico",
            "months": 6,
            "investment": 0,
            "cashflow": 0,
            "values": [0, 0],
            "labels": ["Inversión", "Flujo de caja"],
        },
        {
            "name": "Periodico",
            "months": 6,
            "investment": 0,
            "cashflow": 0,
            "values": [0, 0],
            "labels": ["Inversión", "Flujo de caja"],
        },
    ],
    "debts": [
        {"name": "Crédito de prueba 2 ", "months": 36, "cashflow": 0},
        {"name": "string", "months": 12, "cashflow": 0},
        {"name": "Crédito de prueba", "months": 24, "cashflow": 0},
    ],
    "expenditures": {
        "fixed": 1.735290359812671,
        "variable": [],
        "retirement": 0.14904,
        "healthcare": 0.14904,
        "prepaid_healthcare": 0,
        "values": [
            1.735290359812671,
            0.14904,
            0.14904,
            0,
            0,
            0,
            3.0411189,
            0,
            0,
            0,
            0,
            0,
        ],
        "labels": [
            "Gastos fijos",
            "Pensión",
            "Salud",
            "Salud prepagada",
            "Inversión en Ahorro default",
            "Inversión en asdfasdfasd",
            "Pago en Ahorro default, periodico 3 meses\n",
            "Pago en Ahorro default, periodico 9 meses\n",
            "Pago en Ahorro default, periodico 12 meses",
            "Pago en Ahorro default, periodico",
            "Pago en Periodico",
            "Movimiento a bolsillo de la meta Moto",
        ],
    },
    "incomes": {
        "gross_salary": 3.726,
        "net_salary": 3.4279200000000003,
        "variable_income": [{"name": "Extras", "value": 1.3499999999999999}],
        "prima": 0,
        "last_balance": 1.0192482493689403,
        "values": [
            1.0192482493689403,
            3.726,
            0,
            1.3499999999999999,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        "labels": [
            "Balance mes anterior",
            "Salario neto",
            "Prima",
            "Extras",
            "Retorno de Ahorro default",
            "Retorno de asdfasdfasd",
            "Retorno de Ahorro default, periodico 3 meses\n",
            "Retorno de Ahorro default, periodico 9 meses\n",
            "Retorno de Ahorro default, periodico 12 meses",
            "Retorno de Ahorro default, periodico",
            "Retorno de Periodico",
        ],
    },
    "unemployment_insurance": {
        "stock": 3,
        "income": 0,
        "interest_payment": 0,
        "values": [0, 0],
        "labels": ["Ingreso", "Pago de intereses"],
    },
    "taxes": {
        "rents": 0,
        "discounts": 0,
        "representation_expenditures": 0,
        "dependant_expenditures": 0.3726,
        "exemptions": 0,
        "taxable_income": 0,
        "tax_obligation": 0,
        "positive_balance_with_dian": 0,
        "anticipated_taxes": {
            "wage": 0,
            "riskfree_savings": 0,
            "periodic_savings": 0,
        },
        "payment": 0,
    },
    "accounts": {
        "saving": {"stock": 1.020759},
        "AFC": {"stock": 0, "contributions": 0},
    },
    "financial_map": {
        "comulative_rfs": [
            {"name": "Ahorro default", "total": 0},
            {"name": "asdfasdfasd", "total": 0},
        ],
        "comulative_pers": [
            {
                "name": "Ahorro default, periodico 3 meses\n",
                "total": 329.70606522225756,
            },
            {"name": "Ahorro default, periodico 9 meses\n", "total": 0},
            {"name": "Ahorro default, periodico 12 meses", "total": 0},
            {"name": "Ahorro default, periodico", "total": 0},
            {"name": "Periodico", "total": 0},
        ],
        "values": [329.70606522225756, 6.9450514, 1.020759, 3],
        "labels": [
            "Ahorro default, periodico 3 meses\n",
            "Moto",
            "Cuenta de ahorros",
            "Cesantías",
        ],
    },
    "kpis": {
        "original_interest": 17.17865035688566,
        "total_savings": 8.631603457945664,
        "kyrk_interest": 8.547046898939998,
        "mortgage_savings": [],
        "loan_savings": [
            {
                "name": "Deuda moto",
                "savings": 8.631603457945664,
                "months": 23,
                "original_months": 36,
            }
        ],
        "money_invested_in_savings_options": 171.29969723999997,
        "profits_by_saving_options": 7.283574130000011,
        "saving_account_final_balance": 86.408438,
        "unemployment_insurance_final_balance": 24.617927,
        "feasible_var": {
            "2023": 0.35964266,
            "2024": 0.2500810233333333,
            "2025": 0.3339283108333333,
            "2026": 0.42748333624999996,
            "2027": 0.5318021758333334,
            "2028": 0,
        },
    },
}

# Loans and mortgages
stocks = {
    "loans": [],
    "mortgages": [],
    "debts": [],
    "targets": [
        {
            "name": "Cuota casa",
            "stock": [
                0,
                0,
                0,
                0,
                0,
                2.2589989999999998,
                3.025567857467423,
                3.787750183966457,
                4.545456169813165,
                5.298595002822238,
                6.047074858817506,
                8.275834107324853,
            ],
        }
    ],
    "unemployment_insurance": [
        {"name": "Cesantías", "stock": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    ],
}


# Default savings

dsaving_post = {
    "name": "Davivienda",
    "rate": 0.2,
    "months": 13,
    "type": "Risk Free",
    "bank_id": 1,
}

dsaving_update = {"name": "Davivienda updated"}

dsaving_response = {
    "name": "Davivienda",
    "rate": 0.2,
    "months": 7,
    "type": "Risk Free",
    "id": 1,
    "created_at": "2023-03-23T20:32:05.305767+00:00",
    "last_modified": "2023-03-23T20:32:05.305799+00:00",
}

dsaving_multi_response = {
    "name": "Davivienda",
    "rate": 0.2,
    "months": 7,
    "type": "Risk Free",
    "id": 1,
    "created_at": "2023-03-23T20:32:05.305767+00:00",
    "last_modified": "2023-03-23T20:32:05.305799+00:00",
    "bank": {
        "id": 1,
        "created_at": "2023-04-17T16:32:49.536447+00:00",
        "last_modified": "2023-04-17T16:32:49.536481+00:00",
        "name": "Bancolombia",
        "address": "dirección",
        "phone_number": "1234567890",
        "type": "Commercial",
        "email": "correo@bancolombia.com",
        "nib": "123456",
    },
}

# Default expenditures
dexpenditure_post = {
    "name": "Combustible vehículo/moto",
    "type": "fixed",
    "amount_lower_bound": 80000,
    "amount_upper_bound": 200000,
    "inflation": True,
    "frecuency": 1,
    "category": "Transporte",
}

dexpenditure_update = {"name": "Combustible carro/moto"}

dexpenditure_response =  {
    "name": "Combustible vehículo/moto",
    "type": "fixed",
    "amount_lower_bound": 80000,
    "amount_upper_bound": 200000,
    "inflation": True,
    "frecuency": 1,
    "category": "Transporte",
    "id": 2,
    "created_at": "2023-06-06T21:46:51.875536+00:00",
    "last_modified": "2023-06-06T21:46:51.875551+00:00"
  }

# Case
case_response = {
    "T": 120,
    "minimum_saving": 1,
    "initial_saving": 0.1,
    "prima": True,
    "initial_unemployment_stock": 0,
    "tax_advance_percentage": 0,
    "prepaid_healthcare": 0,
    "representation_cost": False,
    "AnnualTaxPaymentRate": 0.07,
    "include_final_balance": True,
    "unemployment_independent": False,
    "taxAdvanceSavOpt": 0.07,
    "id": 3,
    "annual_target_rate": 0.1,
    "AnnualSavInterest": 0.001,
    "created_at": "2023-03-21T19:47:57.292173+00:00",
    "last_modified": "2023-03-21T19:47:57.292220+00:00",
}

case_update = {"T": 60}

# Loan
loan_post = {
    "name": "Tarjeta crédito",
    "amount": 1,
    "rate": 0.40,
    "months": 6,
    "existent": True,
    "type": "Simple",
    "rate_type": "e.a.",
}

loan_update = {"name": "Tarjeta crédito updated"}

loan_response = {
    "name": "Tarjeta crédito",
    "amount": 1,
    "rate": 0.40,
    "months": 6,
    "existent": True,
    "type": "Simple",
    "rate_type": "e.a.",
    "user_id": 1,
    "id": 1,
    "created_at": "2023-03-21T19:47:57.292173+00:00",
    "last_modified": "2023-03-21T19:47:57.292220+00:00",
}


# Debt
debt_post = {
    "name": "Crédito davivienda",
    "rate": 0.13,
    "months": 24,
    "rate_type": "e.a.",
    "bank_id": 1,
}

debt_update = {"name": "Crédito davivienda actualizado"}

debt_response = {
    "name": "Crédito davivienda",
    "rate": 0.13,
    "months": 24,
    "rate_type": "e.a.",
    "id": 0,
    "created_at": "2023-04-12T15:22:38.193Z",
    "last_modified": "2023-04-12T15:22:38.193Z",
}

debt_multi_response = debt_response.copy()

debt_multi_response.update(
    {
        "bank": {
            "id": 1,
            "created_at": "2023-04-17T16:32:49.536447+00:00",
            "last_modified": "2023-04-17T16:32:49.536481+00:00",
            "name": "Bancolombia",
            "address": "dirección",
            "phone_number": "1234567890",
            "type": "Commercial",
            "email": "correo@bancolombia.com",
            "nib": "123456",
        },
    }
)


# Bank
bank_post = {
    "name": "Bancolombia",
    "address": "dirección",
    "phone_number": "1234567890",
    "type": "Commercial",
    "email": "correo@bancolombia.com",
    "nib": "123456",
}

bank_update = {"name": "Bancolombia actualizado"}

bank_response = {
    "name": "Bancolombia",
    "address": "dirección",
    "phone_number": "1234567890",
    "type": "Commercial",
    "email": "correo@bancolombia.com",
    "nib": "123456",
    "id": 1,
    "created_at": "2023-04-14T17:05:30.491Z",
    "last_modified": "2023-04-14T17:05:30.491Z",
}
