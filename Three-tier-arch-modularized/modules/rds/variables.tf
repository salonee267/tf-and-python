variable "rds_subnet_name" {
  description = "Name of the RDS subnet group"
  default     = "rds_group"
}

variable "private_subnets" {
  description = "private_subnets"
  // default     = "10"
}

variable "rds_storage" {
  description = "RDS storage space"
  default     = "10"
}

variable "rds_engine" {
  description = "RDS engine type"
  default     = "mysql"
}

variable "rds_instance_class" {
  description = "RDS instance class"
  default     = "db.t2.micro"
}

variable "rds_name" {
  description = "Name of the RDS"
  default     = "mysql_rds"
}

variable "rds_username" {
  description = "Username of the RDS"
  default     = "mysql_terraform"
}

variable "rds_password" {
  description = "Password of the RDS"
  default     = "terraformrds"
}
