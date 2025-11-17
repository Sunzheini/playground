# kubectl commands
"""
kubectl create -f .\nginx-pod-definition.yml            # create a pod from the definition file
kubectl get pods                                        # list all pods
kubectl get pods -o wide                                # list all pods with more details
kubectl describe pod myapp-pod                          # describe the pod in detail
kubectl logs myapp-pod                                  # get the logs from the pod
kubectl delete pod myapp-pod                            # delete the pod

kubectl exec -it myapp-pod -- /bin/bash                 # Access pod's terminal
curl localhost:8000                                     # Check if nginx serves on port 8000

kubectl run my-nginx --image=nginx:latest --port=80     # create and run a pod with nginx image

kubectl get all                                         # list all resources (pods, services, etc.)
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

"""


















