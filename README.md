**BLOXS challenge**

<pre>
API que simula transações bancárias básicas, como criação de conta, saque, depósito,
consulta a saldo e extrato das transações.
O intuito foi criar as operações de conta, portanto os usuários que efetuam as
operações são criados no momento da montagem do docker. 
As informações dos usuários são as seguintes:

{
    'id': 1
    'name': 'Roberto', 
    'cpf': '12345678900', 
    'birthDate': '2001/01/15'
},
{
    'id': 2
    'name': 'Simone', 
    'cpf': '12345678999', 
    'birthDate': '1996/07/25'
}

Endpoints:

OPERAÇÕES REFERENTAS A CONTA CORRENTE:

POST - /api/accounts/create/<user_id> - criação da conta
GET  - /api/accounts - listagem das contas correntes criadas
DELETE - /api/accounts/<account_id> - deleção da conta
PUT - /api/accounts/<account_id>/block - bloqueio da conta

TRANSAÇÕES DE CONTA

POST - /api/transactions/create/<account_id>/deposit - criação de transação de depósito
GET - /api/transactions/<account_id>/balance - retorna o saldo da conta
POST - /api/transactions/create/<account_id>/withdraw - saque na conta
GET - /api/transactions/<account_id>/extract - extrato das transações efetuadas na conta


Descrição dos endpoints da aplicação:

- Criação da conta

Exemplo de corpo de requisição:

{	
    "balance": 1000,
    "daily_withdraw_limit": 150,
    "account_type": 1
}

Resposta esperada: 201-CREATED

{
    "account_id": 1,
    "user_id": 1,
    "balance": 1000.0,
    "daily_withdraw_limit": 150.0,
    "is_active": true,
    "account_type": 1,
    "created_at": "Thu, 14 Jul 2022 12:49:38 GMT"
}


- Listagem de contas:

Sem corpo de requisição.

Resposta esperada: 200-OK

[
    {
        "account_id": 2,
        "user_id": 2,
        "balance": 1000.0,
        "daily_withdraw_limit": 150.0,
        "is_active": true,
        "account_type": 1,
        "created_at": "Thu, 14 Jul 2022 12:49:38 GMT"
    },
    {
        "account_id": 1,
        "user_id": 1,
        "balance": 1000.0,
        "daily_withdraw_limit": 150.0,
        "is_active": true,
        "account_type": 1,
        "created_at": "Thu, 14 Jul 2022 12:49:32 GMT"
    }
]


- Deleção da conta:

Sem corpo de requisição.

Resposta esperada: 204-No Content

Sem corpo de resposta.



- Bloqueio da conta

Sem corpo de requisição.

Resposta esperada: 204-No Content

Sem corpo de resposta.



- Operação de depósito:

Exemplo de corpo de requisição:

{
    "value": 200
}

Resposta esperada: 201-CREATED

{
    "transaction_id": 1,
    "account_id": 1,
    "value": 200.0,
    "transaction_date": "Tue, 12 Jul 2022 17:03:59 GMT"
}


- Obtenção do saldo da conta

Sem corpo de requisição.

Resposta esperada: 200-OK

{
    "saldo": "1000.00",
    "user": {
        "user_id": 1,
        "name": "Roberto",
        "cpf": "12345678900",
        "birthDate": "Mon, 15 Jan 2001 00:00:00 GMT"
    }
}


- Operação de saque

Exemplo de corpo de requisição:

{
    "value": 700
}

Resposta esperada: 201-CREATED

{
    "transaction_id": 1,
    "account_id": 1,
    "value": -700.0,
    "transaction_date": "Thu, 14 Jul 2022 12:37:20 GMT"
}

Mensagens de erro:

1 - Tentativa de saque acima do limite diário: 401-Unauthorized

{
    "message": "Value above daily withdraw limit."
}


2 - Segundo saque que passa o limite diario: 401-Unauthorized

{
    "message": "Daily withdraw limit reached. You can withdraw 100.00"
}


- Extrato da conta

Sem corpo de requisição.

Resposta esperada: 200-OK

{
    "user": {
        "user_id": 1,
        "name": "Roberto",
        "cpf": "12345678900",
        "birthDate": "Mon, 15 Jan 2001 00:00:00 GMT"
    },
    "account": {
        "account_id": 1,
        "user_id": 1,
        "balance": 0.0,
        "daily_withdraw_limit": 150.0,
        "is_active": true,
        "account_type": 1,
        "created_at": "Tue, 12 Jul 2022 17:03:00 GMT"
    },
    "extract": [
        {
            "transaction_id": 1,
            "account_id": 1,
            "value": "50.00",
            "date": "Tue, 12 Jul 2022 17:03:59 GMT"
        },
        {
            "transaction_id": 2,
            "account_id": 1,
            "value": "-50.00",
            "date": "Tue, 12 Jul 2022 17:04:33 GMT"
        },
        {
            "transaction_id": 3,
            "account_id": 1,
            "value": "-80.00",
            "date": "Tue, 12 Jul 2022 17:05:00 GMT"
        }
    ]
}



</pre>