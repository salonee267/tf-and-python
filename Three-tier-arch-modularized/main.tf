provider "aws" {
#   profile = "default"
  region  = "${var.region}"
}

data "aws_availability_zones" "available" {}

module "aws_vpc" {
  source = "./modules/networking_comp" 
}

module "aws_subnet" {
  source = "./modules/networking_comp"
}

module "aws_internet_gateway" {
  source = "./modules/networking_comp"
}

module "aws_route_table" {
  source = "./modules/networking_comp"
}

module "aws_eip" {
  source = "./modules/networking_comp"
}

module "aws_nat_gateway" {
  source = "./modules/networking_comp"
}

module "aws_db_subnet_group" {
  source = "./modules/rds"
  private_subnets = var.private_subnets
}

module "aws_db_instance" {
  source = "./modules/rds"
  private_subnets = var.private_subnets
}

module "aws_security_group" {
  source = "./modules/networking_comp"
  // vpc_id = var.vpc_id
}

module "aws_instance" {
  source = "./modules/networking_comp"
  // vpc_id = var.vpc_id
}

module "aws_lb" {
  source = "./modules/networking_comp"
  // vpc_id = var.vpc_id
}

module "aws_lb_target_group" {
  source = "./modules/networking_comp"
  // vpc_id = var.vpc_id
}

module "aws_lb_listener" {
  source = "./modules/networking_comp"
  // vpc_id = var.vpc_id
}

module "aws_lb_listener_rule" {
  source = "./modules/networking_comp"
  // vpc_id = var.vpc_id
}



