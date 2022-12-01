variable "aws_region"{
    type = string
    description = ""
    default = "eu-central-1"
}

variable "instance_access_key"{
    type = string
    description = ""
    default = "x"
}

variable "instance_secret_key"{
    type = string
    description = ""
    default = "x"
}


variable "instance_ami"{
    type = string
    description = ""
    default = "x"
}


variable "instance_intance_type"{
    type = string
    description = ""
    default = "t3.micro"
}


variable "instance_tag"{
    type = map(string)
    description = ""
    default = {
        Name = "Instancia EC2 com variaveis"
        Project = "Exemplo Instancia EC2 com variaveis"
    }
}