provider "aws"{
    region = var.aws_region
    access_key = var.instance_access_key
    secret_key = var.instance_secret_key
}

resource "aws_instance" {
  ami           = var.instance_ami
  instance_type = var.instance_intance_type

  tags = var.instance_tag
}