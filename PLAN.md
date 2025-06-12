Start the project to have something to upload

Pick a cloud platform (AWS/GCP/Azure). / Softuni


-- System and backend performance -- 
Load balancing: NGINX (also consider cloud-based solutions like AWS ALB/ELB)
Queues: Celery, RabbitMQ (good for most async tasks), Kafka (better for high-throughput event streaming)
Cashing: Redis (also useful for rate limiting & session storage)
CDN caching (Cloudflare, Fastly) for static assets
Throughput, Latency, Rate limiting, Connection pools, Read replicas: ?
App: messaging system


-- AI & LLM integration --  (LangCHain, Ollama, LlamaIndex)
Prompt chaining / multistep workflows
Token limits and context window
System prompts vs user prompts
Memory strategies: MangCHain memory or vector memory
RAG (Retrieval-Augmented Generation) to fetch data before prompting
LLM Training on data. TensorFlow, Pytorch, Hugging Face
App: Pdf Q&A Bot


-- Deployment --
Docker and Containerization, Kubernetes for orchestrating docker containers
Deploy with Vercel and Render
CI/CD: GitHub Actions
Environment variables
Monitoring and logging tools: Sentry, LogRocket, Grafana
Profiling tools to spot performance issues: C Profile, py-spy, chrome performance tab
Rollback and recovery strategies, recovering data
Orchestration: Airflow, Perfect


-- API Integration and Design -- 
REST vs GraphQL, gRPC for internal microservices
Design: naming, versioning, HTTP status codes
Authentication / Authorization: API keys, JWT tokens, OAuth 2.0
Pagination, rate limiting, backoff and retries


-------------------------------------------------------------------------
Done:
Programming Is NOT Enough | Add these 5 skills: https://www.youtube.com/watch?v=bZa2uicOTAE&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=4&ab_channel=TechWithTim

Ongoing:
How to Build a Local AI Agent With Python (Ollama, LangChain & RAG): https://www.youtube.com/watch?v=E4l91XKQSgw&ab_channel=TechWithTim
Build Anything with MCP Agents… Here’s How: https://www.youtube.com/watch?v=L94WBLL0KjY&ab_channel=TechWithTim (4:39)
React DnD: https://www.youtube.com/watch?v=DVqVQwg_6_4&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=5&ab_channel=CosdenSolutions


