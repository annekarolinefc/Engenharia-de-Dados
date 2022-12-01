# O que é o Terraform

Terraform é uma ferramenta para construir, alterar e criar versões de infraestrutura com segurança e eficiência através de código

* Infraestrutura como código (IaC)
    * Open source e declarativo
    * Permite versionamento (evolução da infraestrutura e automação)
    * Idempotente
    * Sistaxe high-level e reusável
* Planos de Execução
    * Segurança e previsibilidade
    * Separação de planejamento e aplicação

[Playlist no YouTube](https://www.youtube.com/playlist?list=PLWQmZVQayUUIgSmOj3GPH2BJcn0hOzIaP)

## Casos de Uso
* Criar ou provisionar uma nova infraestrutura
* Gerenciar a infraestrutura existente
* Replicar a infraestrutura

Providers:
* IaaS: AWS, GPC, Azure
* PaaS: Kubernets, Heroku e Digital Ocean

# Como Instalar?
Acessar o [site](https://www.terraform.io/).
Realizar o download, mover arquivo pro disco C e criar a variável de ambiente.
Para visualizar as versões, use o [tfenv](https://github.com/tfutils/tfenv). No windows basta visualizar no cmd. Exemplo de uso: terraform -v

# Extensão para Visual Studio
Uma das opções de extensão é a [HashiCorp Terraform] (https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)

# Configurar a AWS para utilizar o Terraform

Necessário acessar o IAM Dashboard na AWS. 
Criar um Novo Usuário e nomea-lo de Terraform. Dar acesso programático visto que não é necessário acessar ao Console da AWS. A permissão deverá ser de fullAcess (Criar um grupo chamado Administrador). 
Salvar o download do csv (Chave de acesso) gerada. Precisa guardar, pois nao sera exibida novamente.

Realizar download da AWS CLI e configurar os acessos:
aws configure --profile "INSIRA UM NOME FACIL"
Após dar enter, informar a chave e a senha. Informar uma região e output json

# Criar um S3
É basicamente semelhante a uma pasta em nosso computador, onde armazenamos alguns arquivos. 

1) Criar no Console de forma manual.
2) Criar com o Terraform. [Documentação Terraform s3](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* Criar código
[Visualizar código de criação](./Terraform/s3/main.tf)
* Acessar diretório do codigo pelo terminal
* Digitar 
```Terraform init```
* Abrir o arquivo criado: .terraform.lock.hcl que contem version e hashes
* Executar o comando 
```Terraform plan```
que ira planejar o que ira fazer
* Executar o comando 
```Terraform apply```
Pergunta se quer seguir em frente ou não. Ao falar que sim, ele exibe o identificador o bucket. Basta ir na aws e verificar se foi criado.

# Excluir um s3

```
terraform destroy
```

# Criar um EC2
Uso de variáveis para facilitar e tornar o código reutilizavel.

```
terraform init
```

```
terraform plan
```

```
terraform apply
```

ou 

```
terraform apply -auto-approve
```


# Excluir um EC2
```
terraform destroy
```

# https://www.youtube.com/watch?v=yP3Ak_06x6I&list=PLWQmZVQayUUIgSmOj3GPH2BJcn0hOzIaP&index=13