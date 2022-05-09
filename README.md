# Entrega 10 - Kanvas

<p>
Uma API que tem a finalidade de cadastrar cursos em uma plataforma, criar usuários, promover usuários para instrutores, vincular intrutores para cursos e cadastrar alunos em cursos já criados.
</p>

## Funcionalidades

<ul>
  <li>Registro de usuários.</li>
  <li>Registro de cursos, assim como editar e deletar.</li>
  <li>Provover usuário para instrutor.</li>
  <li>Registrar usuário em um curso.</li>
</ul>

# Endpoints base

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# Como usar os Endpoints

<p>Exite 3 tipos de permissões para acessar os endpoists:</p>

<ul>
  <li>Rotas Livres</li>
  <li>Rotas Estudante</li>
  <li>Rotas Instrutor</li>
</ul>

<p>As rotas livres sera para criação e login do usuario. não é necessario o envio de token de autenticação </br>
Rotas com nivel de permissão de usuario poderá ter acesso aos cursos, criar e editar endereço.É necessario o envio de token de autenticação</br>
Rotas com nivel de permissão de intrutor poderá criar cursos, promover usuarios para instrutor, alterar e deletar cursos alem de vincular alunos aos cursos.É necessario o envio de token de autenticação

<p>Logo abaixo seguem exemplos de cada rota aceita pela aplicação, junto com seu
comportamento esperado, os campos necessários para sua utilização e o que será</p>
retornado pelo servidor.</p>

## Rotas

- [Users](#users)
- [Address](#address)
- [Courses](#courses)

## Users

### POST/api/accounts/

#### Descrição

```
    - Rota livre
    - Registra um novo usuráio
```

_Envio:_

```json
{
  "email": "aluno@hot.com",
  "password": "1234",
  "first_name": "Antonio",
  "last_name": "Foo",
  "is_admin": false
}
```

_Resposta:_

```json
{
  "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
  "is_admin": false,
  "email": "aluno@hot.com",
  "first_name": "Antonio",
  "last_name": "Foo"
}
```

### GET/api/accounts/

#### Descrição

```
    - Rota de Instrutor
    - Retorna uma lista com todos usuários cadastrados
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
[
  {
    "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
    "is_admin": false,
    "email": "aluno@hot.com",
    "first_name": "Antonio",
    "last_name": "Foo"
  },
  {
    "uuid": "07e99feb-4a82-4fc7-9918-7c13db26fafc",
    "is_admin": true,
    "email": "adm2@hot.com",
    "first_name": "adm",
    "last_name": "jr"
  }
]
```

### POST/api/login/

#### Descrição

```
    - Rota livre
    - Loga um usuário
```

_Envio:_

```json
{
  "email": "aluno@hot.com",
  "password": "1234"
}
```

_Resposta:_

```json
{
  "token": "6e3fc83da428579a51677d60a3be4978d255cc14"
}
```

## Address

### PUT/api/address/

#### Descrição

```
    - Registra um endereço á um usuário
```

_Envio:_

```json
{
  "zip_code": "123456789",
  "street": "Rua das Flores",
  "house_number": "123",
  "city": "Curitiba",
  "state": "Paraná",
  "country": "Brasil"
}
```

_Resposta:_

```json
{
  "uuid": "3b573ca6-9bd4-4051-bf0f-3ff526ffc237",
  "street": "Rua das Flores",
  "house_number": 123,
  "city": "Curitiba",
  "state": "Paraná",
  "zip_code": "123456789",
  "country": "Brasil",
  "users": [
    {
      "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
      "is_admin": false,
      "email": "aluno@hot.com",
      "first_name": "Antonio",
      "last_name": "Foo"
    }
  ]
}
```

## Courses

### POST/api/courses/

#### Descrição

```
    - Rota de Instrutor
    - Registra um curso
```

_Envio:_

```json
{
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git"
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": null,
  "students": []
}
```

### GET/api/courses/

#### Descrição

```
    - Rota de Instrutor
    - Retorna a lista de todos os cursos
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
[
  {
    "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
    "name": "Django",
    "demo_time": "9:00",
    "link_repo": "http://django.ts.com/git",
    "instructor": null,
    "students": []
  }
]
```

### GET/api/courses/< id_courses >/

#### Descrição

```
    - Rota de Instrutor
    - Retorna o curso correspondente
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": null,
  "students": []
}
```

### PATCH/api/courses/< id_courses >/

#### Descrição

```
    - Rota de Instrutor
    - Altera um ou mais campos do curso
```

_Envio:_

```json
{
  "demo_time": "05:00"
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "5:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": null,
  "students": []
}
```

### PUT/api/courses/< id_courses >/registrations/instructor/

#### Descrição

```
    - Rota de Instrutor
    - Registra um intrutor ao curso
```

_Envio:_

```json
{
  "instructor_id": "07e99feb-4a82-4fc7-9918-7c13db26fafc"
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": {
    "uuid": "07e99feb-4a82-4fc7-9918-7c13db26fafc",
    "is_admin": true,
    "email": "adm2@hot.com",
    "first_name": "adm",
    "last_name": "jr"
  },
  "students": []
}
```

### PUT/api/courses/< id_courses >/registrations/students/

#### Descrição

```
    - Rota de Instrutor
    - Registra alunos ao curso
```

_Envio:_

```json
{
  "students_id": [
    "97f62170-a9a5-411b-b2ba-d409608fc288",
    "907f6fe1-56c1-4043-beb7-0c8b56cb68b6"
  ]
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": {
    "uuid": "07e99feb-4a82-4fc7-9918-7c13db26fafc",
    "is_admin": true,
    "email": "adm2@hot.com",
    "first_name": "adm",
    "last_name": "jr"
  },
  "students": [
    {
      "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
      "is_admin": false,
      "email": "aluno@hot.com",
      "first_name": "Antonio",
      "last_name": "Foo"
    },
    {
      "uuid": "907f6fe1-56c1-4043-beb7-0c8b56cb68b6",
      "is_admin": false,
      "email": "aluno2@hot.com",
      "first_name": "Francisco",
      "last_name": "Foo"
    }
  ]
}
```

### DELETE/api/courses/< id_courses >/

#### Descrição

```
    - Rota de Instrutor
    - Deleta um curso registrado
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
nocontent
```
