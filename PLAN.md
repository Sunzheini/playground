
-- Prototype (W1/9) --
1. Purpose
2. User stories
3. Models: auditor, audit, report
4. Django MVP (minimum viable product), main pages in django templates, leave some of the user stories for later
5. Wireframes w/ navigation between pages and functions
6. Future of the project. incl. scaling
7. Define the architecture and components of the app: frontend, backend, db, etc.
8. Picking the stack: django, react, postgres, langchain, gcp
9. Develop the MVP (make it as a template for the future)
10. Deploy: Render
11. Deploy: GCP


-- System and backend performance (W2/9) -- 
Load balancing: NGINX (also consider cloud-based solutions like AWS ALB/ELB)
Queues: Celery, RabbitMQ (good for most async tasks), Kafka (better for high-throughput event streaming)
Cashing: Redis (also useful for rate limiting & session storage)
CDN caching (Cloudflare, Fastly) for static assets
Throughput, Latency, Rate limiting, Connection pools, Read replicas: ?
App: messaging system


-- AI & LLM integration (W3/9) --  (LangChain, Ollama, LlamaIndex, Langflow)
Prompt chaining / multistep workflows
Token limits and context window
System prompts vs user prompts
Memory strategies: MangCHain memory or vector memory
RAG (Retrieval-Augmented Generation) to fetch data before prompting
LLM Training on data. TensorFlow, Pytorch, Hugging Face
App: Pdf Q&A Bot


-- Deployment (W4/9) --
Docker and Containerization, Kubernetes for orchestrating docker containers
Deploy with Vercel and Render
CI/CD: GitHub Actions
Environment variables
Monitoring and logging tools: Sentry, LogRocket, Grafana
Profiling tools to spot performance issues: C Profile, py-spy, chrome performance tab
Rollback and recovery strategies, recovering data
Orchestration: Airflow, Perfect


-- API Integration and Design (W5/9) -- 
REST vs GraphQL, gRPC for internal microservices
Design: naming, versioning, HTTP status codes
Authentication / Authorization: API keys, JWT tokens, OAuth 2.0
Pagination, rate limiting, backoff and retries


-- Python (W6/9) + alternatives to pip --


-- Django + Postgres (W7/9) --


-- React (W8/9) --


-- Python algorithms (W9/9) --


-------------------------------------------------------------------------
Done:
Programming Is NOT Enough | Add these 5 skills: https://www.youtube.com/watch?v=bZa2uicOTAE&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=4&ab_channel=TechWithTim

Ongoing:
How to Build a Local AI Agent With Python (Ollama, LangChain & RAG): https://www.youtube.com/watch?v=E4l91XKQSgw&ab_channel=TechWithTim
Build Anything with MCP Agents… Here’s How: https://www.youtube.com/watch?v=L94WBLL0KjY&ab_channel=TechWithTim (4:39)
React DnD: https://www.youtube.com/watch?v=DVqVQwg_6_4&list=PLP1wVgC2olQhENJhh7OuCHfujQ92GDqoJ&index=5&ab_channel=CosdenSolutions


