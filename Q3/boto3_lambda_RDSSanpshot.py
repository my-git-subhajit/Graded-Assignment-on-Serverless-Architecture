import boto3

def lambda_handler(event, context):
    # Initialize RDS client
    rds_client = boto3.client('rds')
    
    # Replace 'your_rds_cluster_identifier' with your actual RDS cluster identifier
    cluster_identifier = "database-1"  # You may replace "database-1" with your actual cluster identifier
    
    try:
        # Take snapshot of the specified RDS cluster
        response = rds_client.create_db_cluster_snapshot(
            DBClusterSnapshotIdentifier=f"{cluster_identifier}-Lambda-invoked-snapshot",
            DBClusterIdentifier=cluster_identifier
        )

        # Print the snapshot ID for logging purposes
        snapshot_id = response['DBClusterSnapshot']['DBClusterSnapshotIdentifier']
        print("Snapshot created successfully. Snapshot ID:", snapshot_id)
        
        return {
            'statusCode': 200,
            'body': f"Snapshot created successfully. Snapshot ID: {snapshot_id}"
        }
    except Exception as e:
        error_message = f"Error creating snapshot: {e}"
        print(error_message)
        
        return {
            'statusCode': 500,
            'body': error_message
        }
