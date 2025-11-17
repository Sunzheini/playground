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
"""