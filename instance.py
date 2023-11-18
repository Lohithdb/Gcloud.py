import subprocess

def create_instance(project_id, zone, instance_name, machine_type, image_family, image_project):
    # gcloud command to create a GCP instance
    command = [
        'gcloud', 'compute', 'instances', 'create', instance_name,
        '--project', project_id,
        '--zone', zone,
        '--machine-type', machine_type,
        '--image-family', image_family,
        '--image-project', image_project,
    ]

    try:
        # Run the gcloud command
        subprocess.run(command, check=True)
        print(f"Instance '{instance_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating instance: {e}")

# Replace these values with your own
project_id = 'gcloud-112233'
zone = 'us-east1-b'
instance_name = 'instance1'
machine_type = 'n1-standard-1'
image_family = 'debian-10'
image_project = 'debian-cloud'

create_instance(project_id, zone, instance_name, machine_type, image_family, image_project)
