# AWS Auto-Healing Compliance Monitoring System

## Project Overview

This project is an automated AWS monitoring and compliance remediation system designed to continuously monitor AWS resources and automatically remediate security or compliance violations.

The system detects configuration changes in AWS resources, validates them against compliance rules, and performs automated corrective actions when deviations are identified.

## Problem Statement

Manual monitoring of AWS infrastructure is time-consuming and error-prone. Misconfigured resources can create security risks and compliance violations.

This project automates:
- Monitoring
- Compliance validation
- Alerting
- Auto-remediation


## AWS Services Used

- AWS Lambda
- Amazon CloudWatch
- Amazon SNS
- Amazon S3
- AWS IAM
- Amazon EC2

## Key Features

- Real-time monitoring of AWS resources
- Automated compliance validation
- Auto-healing remediation system
- Event-driven serverless architecture
- Security group validation
- SNS notifications for alerts
- Infrastructure compliance enforcement.


## Workflow

1. User creates or modifies AWS resources
2. CloudWatch detects infrastructure changes
3. Lambda function gets triggered automatically
4. Compliance checks are performed
5. Violations are identified
6. Auto-remediation actions are executed
7. SNS notifications are generated


## Compliance Validation Logic

The Lambda function validates:
- Unauthorized inbound IP ranges
- Security group compliance
- Resource configuration deviations
- Infrastructure security policies

If non-compliance is detected, the system automatically remediates the affected resource configuration.



## Future Enhancements

- Terraform integration
- Kubernetes compliance monitoring
- Multi-account AWS monitoring
- Slack integration
- AI-powered anomaly detection


## Author

siri
