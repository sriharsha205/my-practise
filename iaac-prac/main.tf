terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.23.0"
    }
  }
}
#Create a S3 Bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucket1"

  tags = {
    Name        = "My 1st-bucket"
    Environment = "test"
  }
}
