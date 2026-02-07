provider "aws"{
    region = "us-east-1"
}

resource 'aws_instance' 'demo' {
    ami = "ami-ahsasakj"
    instance_type = "t2.micro"
}

output "instance_id" {
    value = aws_instance.demo.id
}

provider "aws"{
    region = "us-east-1"
    
}

resource "aws_s3_bucket" "test-bucket" {

}


variable "region " {
    default = "us-east-1"
}

variable "instance_type"{
    default = "t3.micro"
}

provider "aws"{
    region = var.region
}
resource "aws_instance" "test_instance"{
    instance_type = var.instance_type
    ami = "ami-xxxxxxxxx"
}

output "instance_id"{
    value = aws_instance.test_instance.id
}

resource "aws_s3_bucket" "name"{
    bucket_name = "name"
}
resource "aws_vpc" "vpc1"{
    cidr_block = "10.0.0.112/32"
}