terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.14.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = file(var.credentials)
  project = var.project
  region  = var.region
}

resource "google_storage_bucket" "data_lake_bucket" {
  name          = var.storage_bucket_name
  location      = var.location
  storage_class = var.gcs_storage_class
  uniform_bucket_level_access = true
  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  // days
    }
  }

  force_destroy = true
}



