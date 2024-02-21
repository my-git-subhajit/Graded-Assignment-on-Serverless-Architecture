import boto3

def create_rds_cluster_snapshot(cluster_identifier):
    # Initialize RDS client
    rds_client = boto3.client('rds')

    try:
        # Take snapshot of the specified RDS cluster
        response = rds_client.create_db_cluster_snapshot(
            DBClusterSnapshotIdentifier=f"{cluster_identifier}-snapshot",
            DBClusterIdentifier=cluster_identifier
        )

        # Print the snapshot ID for logging purposes
        print("Snapshot created successfully. Snapshot ID:", response['DBClusterSnapshot']['DBClusterSnapshotIdentifier'])
    except Exception as e:
        print("Error creating snapshot:", e)

# Replace 'your_rds_cluster_identifier' with your actual RDS cluster identifier
cluster_identifier = "database-1"

# Call function to create cluster snapshot
create_rds_cluster_snapshot(cluster_identifier)

