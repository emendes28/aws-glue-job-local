# remote

terraform {
  backend "s3" {
    bucket = "backend-terraform"
    key    = "state"
    region = "sa-east-1"
  }
}

provider "aws" {
  region = "sa-east-1"
}

module "foo-bar" {
  source   = "../foo-bar"
  env_name = terraform.workspace
}