# AWS CLI Lab (LocalStack)
- Used LocalStack to simulate AWS cloud locally.
- Configured AWS CLI to point to LocalStack endpoint (`http://localhost:4566`).
- Created an S3 Bucket: `aws --endpoint-url=http://localhost:4566 s3 mb s3://ganesh-devops-bucket`
- Verified bucket: `aws --endpoint-url=http://localhost:4566 s3 ls`
