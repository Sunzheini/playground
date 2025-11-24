# kubectl commands
"""
kubectl create -f pod-definition.yml                    # create a pod from the definition file
kubectl get pods                                        # list all pods
kubectl get pods -o wide                                # list all pods with more details
kubectl describe pod myapp-pod                          # describe the pod in detail
kubectl logs myapp-pod                                  # get the logs from the pod
kubectl edit pod myapp-pod                              # edit the pod definition in your default editor
kubectl delete pod myapp-pod                            # delete the pod

kubectl run nginx-pod --image=nginx:latest --port=80    # create and run a pod with nginx image

kubectl exec -it myapp-pod -- /bin/bash                 # Access pod's terminal
curl localhost:8000                                     # Check if nginx serves on port 8000

kubectl run my-nginx --image=nginx:latest --port=80     # create and run a pod with nginx image

kubectl get all                                         # list all resources (pods, services, etc.)
kubectl get all --all-namespaces                        # list all resources in all namespaces
kubectl api-resources                                   # list all available API resources
"""

# Replication Controller commands
"""
kubectl create -f rc-definition.yml                     # create a replication controller
kubectl get rc                                          # list all replication controllers
kubectl describe rc myapp-rc                            # describe the replication controller
kubectl scale rc myapp-rc --replicas=5                  # scale the replication controller to 5 replicas
kubectl delete rc myapp-rc                              # delete the replication controller
"""

# ReplicaSet commands (newer version of Replication Controller)
"""
kubectl create -f rs-definition.yml                     # create a replica set
kubectl get rs                                          # list all replica sets
kubectl describe rs myapp-rs                            # describe the replica set
kubectl scale rs myapp-rs --replicas=4                  # scale the replica set to 4 replicas
kubectl delete rs myapp-rs                              # delete the replica set
"""

# Deployment commands (creates ReplicaSets and manages them)
"""
kubectl create -f dp-definition.yml                     # create a deployment
kubectl get deployments                                 # list all deployments
kubectl describe deployment myapp-dp                    # describe the deployment
kubectl scale deployment myapp-dp --replicas=6          # scale the deployment to
kubectl delete deployment myapp-dp                      # delete the deployment
"""

# Namespace commands
"""
kubectl create namespace my-namespace                   # create a new namespace
kubectl get namespaces                                  # list all namespaces
kubectl delete namespace my-namespace                   # delete the namespace
kubectl get pods -n my-namespace                        # list pods in the specified namespace
kubectl config set-context --current --namespace=my-namespace     # set the default namespace for current context
"""

# Service commands
"""
kubectl create -f service-definition.yml                # create a service
kubectl get services                                    # list all services
kubectl describe service myapp-service                  # describe the service
kubectl delete service myapp-service                    # delete the service, you must delete the pods separately

curl http://localhost:30008                             # access the service from outside
"""

# ConfigMap commands
"""
kubectl create -f config-map.yml                        # create a ConfigMap
kubectl get configmaps                                  # list all ConfigMaps
kubectl describe configmap myapp-config                 # describe the ConfigMap
kubectl delete configmap myapp-config                   # delete the ConfigMap
"""

# Secret commands (storing sensitive data encoded in base64)
"""
kubectl create -f secret-definition.yml                 # create a Secret
kubectl get secrets                                     # list all Secrets
kubectl describe secret myapp-secret                    # describe the Secret
kubectl delete secret myapp-secret                      # delete the Secret
"""

# Other useful commands
"""
# Labels and Selectors commands
kubectl label pods myapp-pod env=production            # add a label to a pod
kubectl get pods --selector=env=production             # list pods with the specified label
"""

# Job commands
"""
kubectl create -f job-definition.yml                    # create a job
kubectl get jobs                                       # list all jobs
kubectl describe job myapp-job                          # describe the job
kubectl delete job myapp-job                            # delete the job
"""

# CronJob commands
"""
kubectl create -f cronjob-definition.yml                # create a cron job
kubectl get cronjobs                                   # list all cron jobs
kubectl describe cronjob myapp-cronjob                  # describe the cron job
kubectl delete cronjob myapp-cronjob                    # delete the cron job

# Network Policies commands
kubectl create -f network-policy.yml                    # create a network policy
kubectl get networkpolicies                            # list all network policies
kubectl describe networkpolicy myapp-network-policy     # describe the network policy
kubectl delete networkpolicy myapp-network-policy       # delete the network policy
"""


















