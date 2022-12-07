##############################################################################
#                                   RDS
###############################################################################

# Create RDS subnet group

resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "${var.rds_subnet_name}"
  subnet_ids = var.private_subnets
  tags = {
    Name = "RDS Subnet Group"
  }
}

# Create RDS instance 

resource "aws_db_instance" "rds" {
  allocated_storage    = "${var.rds_storage}"
  engine               = "${var.rds_engine}"
  instance_class       = "${var.rds_instance_class}"
  name                 = "${var.rds_name}"
  username             = "${var.rds_username}"
  password             = "${var.rds_password}"
  db_subnet_group_name = "${var.rds_subnet_name}"
  depends_on = ["aws_db_subnet_group.rds_subnet_group"]
}
