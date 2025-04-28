# Python Clean Arch

Projeto Python criado para estudar Clean Architecture.
Este repositório está em constante mudança e as mesmas ocorrem sem nenhum aviso prévio, visto que é um repositório de estudo.
O mesmo pode ser usado como base para outros projetos da forma que for desejada, mas sem responsabilidade de minha parte.
**Lembre-se, é um projeto de estudo.**

Ideias, sugestões, melhorias, dicas, críticas, enfim, tudo é bem vindo desde que seja para contribuir.

Contato diretamente comigo: giovani.lima@rede.ulbra.br
## Ideia

Como base de inspiração para esse projeto, foi utilizado o desafio de programação backend do PicPay.
 - [Desafio Backend PicPay](https://github.com/PicPay/picpay-desafio-backend)

## Stack utilizada

**Back-end:** Python, FastApi, SqlModel, SQLite

## Rodando localmente

Clone o projeto

```bash
git clone https://github.com/everthefullstack/python-clean-arch
```

Instale o UV seguindo o tutorial do repositório

```bash
https://github.com/astral-sh/uv
```

Instale a versão 3.13 do python

```bash
uv python install 3.13
```

Crie uma VENV

```bash
uv venv
```

Ative a VENV

```bash
.venv\Scripts\activate
```

Instale os pacotes necessários

```bash
uv pip install -r pyproject.toml
```

Rode o projeto

```bash
fastapi main.py
```

## Funcionalidades

- Criar Cadastro (70% pronto)
- Buscar Cadastro (Em construção)
- Fazer Transferência (Em construção)

**O projeto utiliza o Swagger como documentação/testes, logo, para testar a aplicação, acesse: http://127.0.0.1:8000/swagger**
## Referências

 - [Programador Lhama Clean Arch](https://github.com/programadorLhama/CleanArch)
 - [Rodrigo Branas Live Clean Architecture](https://github.com/rodrigobranas/live_clean_architecture_fullcycle)
 - [Clean Architecture Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

