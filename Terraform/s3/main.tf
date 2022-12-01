# https://registry.terraform.io/providers/hashicorp/aws/latest/docs
    #profile="PROFILE QUE SETEI AIS CONFIGURACES NO AWS CLI" caso utilize ela para configurar a chave de acesso

# Inserir uma versao fixa para o terrafor
# terraform { required_version = "0.14.4" }
# required_providers { aws = {source = "hashicorp/aws" version = "3.23.0"}}

provider "aws"{
    region = "eu-central-1"
    access_key = "COLOQUE AQUI"
    secret_key = "COLOQUE AQUI"
}

resource "aws_s3_bucket" "NOME DO BUCKET" {
  bucket     = "nome-do-bucket-1234232323"
  acl = "private"
  tags = {
    Name = "My bucket"
    Environment = "Dev"
    Managedby = "Terraform" #informar por onde esta sendo gerenciado
  }
}