provider "aws"{
    region = "eu-central-1"
    access_key = "COLOQUE AQUI"
    secret_key = "COLOQUE AQUI"
}

resource "aws_instance" "web" {
  ami           = "ami-0000000000"
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}