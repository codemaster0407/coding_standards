# Coding Standards and Engineering Guidelines

## 1. Introduction

Welcome to the Engineering Guidelines document. As our Product Agency scales and we manage multiple teams augmenting client capabilities, we must maintain a unified, high-quality approach to software development. This document serves as the foundational source of truth for coding standards across all four engineering teams.

By standardizing our approaches, we aim to:
- **Accelerate Delivery:** Eliminate stylistic debates during pull request (PR) reviews.
- **Improve Onboarding:** Provide clear, documented expectations for new engineers.
- **Ensure Quality:** Establish baseline standards for testing, documentation, and architecture.
- **Foster Collaboration:** Create a frictionless environment for code reviews.

This document is a living artifact. While it establishes the initial baseline, the expectation is that the engineering team will continuously contribute and refine these standards over time.

---

## 2. Tech Stack Overview

Our standard technology stack across projects consists of:
- **Backend:** TypeScript / Node.js
- **Frontend / APIs:** React / Next.js
- **Database:** Postgres (Hosted on Neon)
- **ORM / Types:** Drizzle
- **Testing:** React Testing Library (for frontend) and Jest (or standard test runner for backend)
- **Formatting:** Prettier
- **Architecture:** Monorepo

---

## 3. General Coding & Style Guidelines

To avoid reinventing the wheel and to leverage industry best practices, we adopt **Google's TypeScript Style Guide** as our baseline for TypeScript and JavaScript code.

### 3.1. TypeScript Core Principles
- **Strict Typing:** Always use strong typings. Avoid using `any`; prefer `unknown` if the type is truly not known ahead of time.
- **Const & Let:** Always use `const` or `let`. Never use `var`. Prefer `const` unless the variable needs to be reassigned.
- **Interfaces vs. Types:** Prefer `interface` for object definitions over `type` aliases, as they provide better error messages and performance in the TypeScript compiler.
- **Exporting:** Use named exports (`export const Foo`) rather than default exports (`export default Foo`) to ensure consistent naming across imports and refactoring safety.

### 3.2. Code Formatting
- **Prettier:** We use Prettier as the ultimate authority on code formatting. All projects must include a `.prettierrc` configuration file.
- **Automation:** Prettier should be integrated into your IDE to format on save, and enforced via a pre-commit hook (e.g., Husky + lint-staged). This eliminates all manual debates over spacing, quotes, and line breaks.

---

## 4. Frontend & Backend Specifics

### 4.1. React / Next.js (Frontend & API)
- **Functional Components:** Use functional components and React Hooks exclusively. Avoid class-based components.
- **Next.js Routing:** Follow the Next.js App Router conventions (or Pages Router if maintaining an older app) strictly. Separate server components from client components clearly.
- **Data Fetching:** For Next.js APIs, ensure proper error handling and status codes. For client-side data fetching, rely on robust caching and synchronization libraries (like SWR or React Query) unless Server Actions are appropriate.

### 4.2. Node.js Backend & Database (Neon + Drizzle)
- **Drizzle ORM:** Define schemas clearly in a dedicated database folder. Use Drizzle's migration tools to keep database changes tracked in version control.
- **Connection Management:** Ensure proper pooling when connecting to Neon Serverless Postgres to avoid connection exhaustion in serverless API routes.
- **Type Generation:** Rely on Drizzle's generated types to ensure end-to-end type safety between the database and the API layers.

---

## 5. Testing Standards

Quality is non-negotiable. Tests act as executable documentation and guardrails for future refactoring.

### 5.1. React Testing Library
- **Behavior-Driven Testing:** Test the application from the user's perspective. Avoid testing internal component state or implementation details.
- **Querying Elements:** Prioritize querying by accessible roles (e.g., `getByRole`, `getByLabelText`) rather than `test-ids` or CSS classes.
- **Coverage:** Aim to cover the critical paths and edge cases of a feature. 100% line coverage is not the goal; 100% confidence in the feature's behavior is.

### 5.2. API & Backend Testing
- Write integration tests for API endpoints to ensure the routing, database interaction (using a test DB or mocks), and response payload adhere to the expected contract.

---

## 6. Version Control & Pull Requests

A streamlined review process starts before the PR is even opened. Adhering to strict naming and message guidelines makes history traversable and code reviews faster.

### 6.1. Branch Naming
Branch names should be descriptive and categorized by the type of work. Use the following format:
`[type]/[ticket-id]-[short-description]`

**Types:**
- `feat/`: For new features (e.g., `feat/ENG-123-user-login-flow`)
- `fix/`: For bug fixes (e.g., `fix/ENG-124-button-alignment`)
- `chore/`: For maintenance, dependency updates, or configuration changes.
- `docs/`: For documentation updates.

### 6.2. Commit Messages
We follow the **Conventional Commits** specification. This allows us to automate changelogs and versioning in the future.
Format: `type(scope): description`

**Examples:**
- `feat(auth): implement JWT token refresh mechanism`
- `fix(ui): correct padding on mobile navigation bar`
- `test(api): add integration tests for user endpoints`

### 6.3. Pull Request Guidelines
- **Title:** The PR title should match the commit message standard (e.g., `feat(auth): implement JWT token refresh mechanism`).
- **Description:** Provide context. What does this PR do? Why is this approach taken? Include screenshots or screen recordings for UI changes.
- **Size:** Keep PRs small and focused on a single concern. If a PR takes longer than 20 minutes to review, it is likely too large and should be broken down.
- **Self-Review:** The author must review their own code before requesting a review from peers.

---

## 7. Documentation

Clear documentation accelerates onboarding and reduces context switching.

- **README:** Every monorepo package or app must have a `README.md` explaining how to build, run, and test it.
- **Code Comments (JSDoc):** Use JSDoc (`/** ... */`) to document the *why* of complex logic or non-obvious algorithms, not the *what*. For exported functions and APIs, document parameters and return types if they are not explicitly clear from the TypeScript signatures.
- **Architecture Decisions:** Use Architecture Decision Records (ADRs) to document significant infrastructure or library choices (e.g., choosing a specific state management library over another).

---

*Draft Version 1.0 - Pending VP of Engineering Review.*
