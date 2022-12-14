provider "aws" {
#   profile = "default"
  region  = "${var.region}"
}

data "aws_availability_zones" "available" {}

module "aws_vpc" {
  source = "./modules/networking_comp" 
}

module "aws_db_instance" {
  source = "./modules/rds"
  private_subnet = module.aws_vpc.private_subnets
}


