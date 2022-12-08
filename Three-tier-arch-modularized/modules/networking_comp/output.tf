output "private_subnets" {
#  description = "The address of the RDS instance"
 value = aws_subnet.private.*.id
}
