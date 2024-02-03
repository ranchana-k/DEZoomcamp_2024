variable "project"{
    description = "My current Project ID"
    default = "terraform-dezoomcamp"
}
variable "region" {
    description = "Region for Resources"
    default = "asia-southeast1"
  
}
variable "location" {
    description = "Project Location"
    default = "asia-southeast1"
  
}
variable "bq_dataset_name"{
    description = "Bigquery Dataset Name"
    default = "demo_dataset"
}

variable "storage_bucket_name" {
    description = "My Storage Bucket Name"
    default = "terraform-dezoomcamp-demo-bucket"
}
variable "gcs_storage_class" {
    description = "Storage Class"
    default = "STANDARD"
  
}
variable "credentials" {
  description = "GOOGLE APPLICATION CREDENTIALS"
  default = "./keys/terraform-dezoomcamp-daa7b576c47a.json"
}