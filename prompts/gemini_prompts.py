DATA_EXTRACTION_PROMPT = """
Analyze the provided text and extract a comprehensive list of the technologies, frameworks, libraries, and tools mentioned as part of the 'tech stack'. 
Return only the names of these items as a list of strings. 
Do not include descriptions of their purpose (e.g., extract 'Next.js' instead of 'Next.js for frontend').

For the each tech stack identified, generate the prompt for tavily web search to search for general coding standards to be maintained with that tech stack . 

Example : 
1. Best practices for TypeScript monorepo folder structure and shared packages 2024\n\nNode.js TypeScript backend coding standards for scalable API development\n\nStandardizing package.json and workspace configurations in a TypeScript monorepo
2. Next.js App Router coding standards and component architecture best practices\n\nReact TypeScript component patterns for large scale product agencies\n\nServer Actions vs API Routes: coding guidelines for Next.js data fetching\n 
3. Drizzle ORM best practices for schema management and migrations in a monorepo\n\nOptimizing Neon serverless Postgres connections in Next.js edge functions\n\nStandardizing database naming conventions and type generation with Drizzle
4. Testing React components with React Testing Library: best practices\n\nSnapshot testing vs integration testing strategies for Next.js applications\n\nTest-driven development (TDD) patterns for React component libraries
5. Conventional Commits and PR title standards for high-velocity software teams\n\nBest practices for branch naming conventions in a monorepo multi-team environment\n\nDrafting a pull request template for a Product Agency to reduce review friction
6. Modern TypeScript tech stack coding standards: React, Next.js, Drizzle, and Monorepo\n\nHow to reduce PR review friction in teams using Next.js and TypeScript

"""


SUMMARISE_CONTEXT_PROMPT = """
You are a senior engineering technical writer. You are given raw content scraped from web pages and search results 
about a specific technology's coding standards and best practices.

Your task is to produce a concise, well-structured SUMMARY (300-500 words) of the most important and actionable 
coding standards, best practices, and guidelines found in the raw text.

Focus on:
- Concrete rules and patterns that can be directly adopted by a software team
- Any conventions for naming, structure, or formatting
- Pitfalls and anti-patterns to avoid

Do NOT add any information not present in the raw text.
Do NOT include marketing language, introductions, or conclusions.
Output only the summarised content as plain prose with bullet points where appropriate.

Raw Content:
"""


FINAL_DRAFT_PROMPT = """
You are a senior Engineering Manager at a Product Agency. You have been tasked with writing the official 
Coding Standards document for your four software teams (20 engineers total).

The VP of Engineering wants a single, cohesive document that will become the source of truth for all code reviews.
The core problem is that PR reviews are slow and cause friction because reviewers rely on personal opinion rather 
than documented standards.

Tech Stack: TypeScript/Node (backend), React/Next.js (frontend & APIs), Neon/Postgres (database), 
Drizzle (ORM), React Testing Library (tests), Prettier (formatting), Monorepo structure.

You have been provided with summarised research notes from industry best practices for each area of the tech stack.
Using ONLY the information in these research notes, write a comprehensive coding standards document of approximately 
3000 words.

The document MUST include the following sections:
1. Introduction & Purpose
2. TypeScript & Node.js Standards
3. React & Next.js Standards
4. Database Standards (Drizzle & Neon)
5. Testing Standards (React Testing Library)
6. Code Formatting (Prettier)
7. Monorepo Structure & Package Management
8. Git Workflow: Branch Naming, Commit Messages & PR Standards
9. Documentation Standards

Writing guidelines:
- Use clear headings and sub-headings (h1, h2, h3)
- Use bullet points for rules and guidelines
- Write in an authoritative but accessible tone for software engineers
- Each section must contain actionable rules, not vague advice
- For bullet points, use only single *. Do not use ** for bolding.
- Do not add any extra new lines between bullet points

Research Notes:
"""