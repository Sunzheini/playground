-- Prototype --
1. Purpose
2. User stories
3. Models: auditor, audit, report
4. Django MVP (minimum viable product), main pages in django templates, leave some of the user stories for later
5. Wireframes w/ navigation between pages and functions (+ https://getbootstrap.com/)
6. Future of the project. incl. scaling
7. Define the architecture and components of the app: frontend, backend, db, etc.
8. Picking the stack: django, react, postgres, langchain, gcp
9. Develop the MVP (make it as a template for the future)
10. Deploy: Render + postgres


-- Deployment --
Environment variables
Docker and Containerization, docker video: https://softuni.bg/trainings/resources/video/101964/video-16-july-2024-dimo-mitev-containers-and-cloud-july-2024/4524
DOcker Compose for multi-container apps
Kubernetes for orchestrating docker containers
Deploy dockerized app with Vercel and Render
CI/CD: GitHub Actions
Monitoring and logging tools: Grafana


-- System and backend performance (friday) -- 
Load balancing: NGINX (also consider cloud-based solutions like AWS ALB/ELB)
Queues: Celery, RabbitMQ (good for most async tasks), Kafka (better for high-throughput event streaming) + Presentation
Cashing: Redis (also useful for rate limiting & session storage)
CDN caching (Cloudflare, Fastly) for static assets
Throughput, Latency, Rate limiting, Connection pools, Read replicas: ?


-- Python algorithms (last) --


-- Python (Holy1) + alternatives to pip, Pydantic, common libs


-- React (Holy2)
Create React app
Django REST Framework for API: +Django REST Framework presentation


-- React Deployment (Aug1)
GraphQL between React and Django
Create a Dockerfile for React app
Deploy React app to Render
Debug = False
Media files persistence e.g. on Render (last chat) -> db backup and restore, (check ployment and files in erp demo deployment video)
usage of scss, state‑management (React Query, Zustand)
Terraform for infrastructure as code (IaC) - softuni 2xvideos
Deploy: GCP: 
https://www.youtube.com/watch?v=sqUuofLBfFw&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=5&ab_channel=NeuralNine
https://www.youtube.com/watch?v=EBtpgEg7fvw&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=7&ab_channel=ProgrammingKnowledge


-- AI & LLM integration (Aug2) --  (LangChain, Ollama, LlamaIndex, Langflow)
Prompt chaining / multistep workflows
Token limits and context window
System prompts vs user prompts
Memory strategies: MangCHain memory or vector memory
RAG (Retrieval-Augmented Generation) to fetch data before prompting
LLM Training on data. TensorFlow, Pytorch, Hugging Face
App: Pdf Q&A Bot


-------------------------------------------------------------------------
Done:
Programming Is NOT Enough | Add these 5 skills: https://www.youtube.com/watch?v=bZa2uicOTAE&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=4&ab_channel=TechWithTim

Ongoing:
How to Build a Local AI Agent With Python (Ollama, LangChain & RAG): https://www.youtube.com/watch?v=E4l91XKQSgw&ab_channel=TechWithTim
Build Anything with MCP Agents… Here’s How: https://www.youtube.com/watch?v=L94WBLL0KjY&ab_channel=TechWithTim (4:39)
React DnD: https://www.youtube.com/watch?v=DVqVQwg_6_4&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=5&ab_channel=CosdenSolutions


