Q1: Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. Specifically:

Setup:

Create two EC2 instances.

Tag one of them as Auto-Stop and the other as Auto-Start.

Lambda Function Creation:

Set up an AWS Lambda function.

Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.

Coding:

Using Boto3 in the Lambda function:

Detect all EC2 instances with the Auto-Stop tag and stop them.

Detect all EC2 instances with the Auto-Start tag and start them.

Testing:

Manually invoke the Lambda function.

Confirm that the instance tagged Auto-Stop stops and the one tagged Auto-Start starts.

Instructions:

EC2 Setup:

Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).

Tag the first instance with a key Action and value Auto-Stop.

Tag the second instance with a key Action and value Auto-Start.

Lambda IAM Role:

In the IAM dashboard, create a new role for Lambda.

Attach the AmazonEC2FullAccess policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)

Lambda Function:

Navigate to the Lambda dashboard and create a new function.

Choose Python 3. x as the runtime.

Assign the IAM role created in the previous step.

Write the Boto3 Python script to:

Initialize a boto3 EC2 client.
Describe instances with Auto-Stop and Auto-Start tags.
Stop the Auto-Stop instances and start the Auto-Start instances.
Print instance IDs that were affected for logging purposes.
Manual Invocation:

After saving your function, manually trigger it.

Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.

Solution:

Created two ec2 instances with tag - tag: Auto-Start and tag: Auto-Stop
Made Sure that the instances are running
Navigated to IAM, created a role, and attached AmazonEc2FullAccess
Created a Lambda Function with Python 3. x and attached the role that was created.
Wrote te code using boto3 module, and https://boto3.amazonaws.com/v1/documentation
Manually tested the function
The function is stopping the ec2 instance with the tag Auto-Stop and starting the instances with the tag Auto-Start
Attached Screenshots
Also, the code is well documented with comments.
