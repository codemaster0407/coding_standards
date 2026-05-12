### Summary of chunk 1
- Structure the monorepo with top-level directories: `apps/` for runnable applications, `libs/` for shared runtime code, and `packages/` for tooling and shared configurations.
- Utilize npm workspaces for dependency resolution between internal packages and root-level script execution.
- For internal TypeScript packages, configure `package.json` to point directly to source files (`"main": "src/index.ts"`) to avoid a separate build step.
- Ensure `tsconfig.json` compiler options include `"verbatimModuleSyntax": true`, `"allowImportingTsExtensions": true`, and `"rewriteRelativeImportExtensions": true` for direct source file consumption.
- Use `NodeNext` module resolution for modern Node.js environments.
- Implement type-safe API contracts by exporting types from backend packages (e.g., Hono app types) and importing them into the frontend for type-safe client requests.
- Share common linting, formatting, and TypeScript configurations by creating packages in the `packages/` directory (e.g., `@example/eslint-config`, `@example/prettier-config`, `@example/tsconfig`).
- Configure Prettier with consistent settings (e.g., `semi: true`, `trailingComma: "all"`, `singleQuote: true`, `printWidth: 120`).
- Configure ESLint to extend shared base configurations and allow for workspace-specific overrides.
- Use `lint-staged` and Husky for pre-commit hooks to enforce formatting and linting.
- Adopt conventional commits for Git history, using scopes (e.g., `feat(api):`, `fix(client):`) to indicate the affected part of the monorepo.
- Use `commitlint` to enforce conventional commit message structure.
- Leverage Turborepo for efficient CI by using the `--affected` flag to run tasks only on changed packages.
- Utilize `turbo prune` to create optimized Docker images containing only necessary code and dependencies for each application.
- Consider using code generation tools (e.g., Plop) for repetitive tasks like creating new packages to ensure consistency and reduce manual errors.
- For database interactions, use Drizzle ORM with Neon-hosted PostgreSQL. Define schemas in Drizzle and generate migrations.
- For frontend and API development, use React and Next.js.
- For testing, utilize React Testing Library for frontend components and Jest/Vitest for backend logic and API endpoints.
- Ensure `tsconfig.json` compiler options include `"noEmit": true` when not requiring compiled output for internal packages.
- When using TypeScript Project References, ensure `composite: true` is set in `tsconfig.json` and use `tsc --build` for compilation and type checking.
- For package managers, prefer using `npm workspaces` or equivalent (pnpm, yarn workspaces) for managing local package linking.
- When using workspaces, configure `package.json` `exports` to directly point to TypeScript source files for internal packages, enabling direct import of `.ts` files.
- If publishing packages externally, pre-compilation to `dist/` is necessary, and `package.json` `exports` should point to compiled artifacts.

### Summary of chunk 2
*   **API Versioning:** Use `/api/v1`, `/api/v2` in API routes to manage breaking changes.
*   **API Documentation:** Generate live, interactive API documentation using Swagger (e.g., `swagger-ui-express`, `swagger-jsdoc`). Add JSDoc comments to routes for auto-generation.
*   **Environment Variables:** Never hardcode secrets or configuration values. Use `.env` files and the `dotenv` package for managing environment variables. Access them via `process.env.VARIABLE_NAME`.
*   **Build Process:** Ensure your TypeScript code is compiled to JavaScript for production. The `npm run build` command should generate output in a `dist/` folder, and the `start` script should execute `node dist/index.js`.
*   **Code Formatting:** Utilize Prettier for consistent code formatting across the project.
*   **Monorepo Structure:** Organize the project using a monorepo structure for better code sharing and dependency management.
*   **Database Interaction:** Use Drizzle ORM for interacting with the Neon-hosted PostgreSQL database.
*   **Testing:** Employ React Testing Library for frontend component testing.
*   **Server Components (Next.js App Router):** Default to Server Components for backend logic, direct database access, and to prevent sensitive data exposure.
*   **Client Components (Next.js App Router):** Use `"use client";` directive only when components require browser APIs, event handlers, or React state/effects.
*   **Composition Pattern:** Render Server Components within Client Components to minimize the client-side JavaScript footprint.
*   **Streaming and Suspense:** Leverage `Suspense` boundaries and `loading.js` files for progressive rendering and improved perceived performance, especially for data-dependent sections.
*   **Skeleton Design:** Implement skeleton components that precisely match the dimensions and layout of the content they replace to prevent layout shifts.
*   **Parallel Routes:** Utilize the `@` folder convention for parallel routes to render multiple pages or UI segments concurrently, enabling compositional resilience.
*   **Intercepting Routes:** Combine parallel routes with intercepting routes to implement modal UIs that function correctly with both client-side navigation and direct URL access.
*   **Server Actions:** Use Server Actions for mutations and form submissions, allowing them to be called directly from Client Components or used as form actions for seamless progressive enhancement.
*   **Metadata API:** Employ the typed, composable Metadata API in Next.js for managing `<head>` elements, supporting both static and dynamic metadata that merges down the route hierarchy.
*   **Caching Strategies:** Understand and implement caching at four layers: Request Memoization (automatic `fetch` deduplication), Data Cache (indefinite by default, controllable via revalidation), Full Route Cache (static routes at build time, dynamic on request), and Router Cache (client-side route caching).
*   **Error Handling:** Implement granular error handling using `error.tsx` files at each route segment for robust application resilience.
*   **Security (Taint APIs):** Utilize React's taint APIs (`taintObjectReference`, `taintUniqueValue`) and configure `experimental.taint: true` in `next.config.js` to prevent sensitive data from being unintentionally exposed to the client.

### Summary of chunk 3
(summarisation failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}})

### Summary of chunk 4
*   **Error Handling:** Implement robust error handling for asynchronous operations using `try...catch` blocks to prevent application crashes and improve debugging.
*   **React Hooks:** Leverage new React 19 hooks like `use()`, `useOptimistic()`, `useActionState()`, and `useFormStatus()` for simplified data fetching, optimistic UI updates, and cleaner form handling. Utilize `useDeferredValue()` and `useTransition()` from React 18 for improved UI responsiveness and perceived performance.
*   **Next.js Data Fetching:** Differentiate between static data fetching (at build time) for content that doesn't change often (e.g., blogs, product listings) and dynamic data fetching (on request) for real-time or user-specific content (e.g., dashboards, user profiles). Utilize Next.js's built-in `fetch` API for automatic server-side data caching with configurable revalidation (`revalidate`) or opting out with `cache: 'no-store'`.
*   **React Suspense:** Employ React Suspense for non-blocking asynchronous operations like data fetching, improving user experience by preventing UI freezes. Use fallback components for loading states and integrate with libraries like React Query or SWR.
*   **Monorepo Migration Management:** For Drizzle ORM migrations within a monorepo, maintain migrations within a shared library and execute them as part of the startup routine of a backend service that consumes the library. Consider discussing specific strategies with Drizzle maintainers for complex monorepo setups.
*   **Drizzle ORM Configuration:**
    *   Define a `drizzle.config.ts` file specifying `strict: true`, `verbose: true`, an `out` directory for migrations, the `dialect` (e.g., "postgresql"), the `schema` path, and `dbCredentials` including the `DATABASE_URL`.
    *   Use a `Pool` from `pg` for database connections in Node.js environments.
    *   For Neon serverless environments, use the `@neondatabase/serverless` driver and `neon()` function.
*   **Drizzle ORM Schema Definition:** Define database schemas using Drizzle's type-safe schema definition language, leveraging functions like `pgTable`, `serial`, `text`, `integer`, `timestamp`, and `references`.
*   **Drizzle ORM Migrations:**
    *   Generate migrations using `drizzle-kit generate`.
    *   Apply migrations using `drizzle-kit push` or programmatically via `migrate(db, { migrationsFolder: 'drizzle' })`.
    *   Utilize `drizzle-kit studio` for visual database management.
*   **Drizzle ORM Querying:** Write type-safe database queries using Drizzle's SQL-like syntax, for example, `db.select().from(users)`.
*   **Drizzle ORM Seeding:** Implement seeding scripts to populate the database with initial data, using `db.insert(tableName).values([...])`.
*   **Neon Database Connection:** Retrieve and use the direct (non-pooled) database connection string from the Neon Console for running migrations. Use pooled connection strings for application runtime.

### Summary of chunk 5
*   **TypeScript/Node.js Backend:**
    *   Use `dotenv` for managing environment variables.
    *   Employ `Hono.js` for building API endpoints.
    *   Integrate `Drizzle ORM` for database interactions.
    *   Connect to `Neon-hosted PostgreSQL` using `@neondatabase/serverless`.
    *   Define database schemas in TypeScript files as the single source of truth.
    *   Utilize Drizzle's migration tools (`drizzle-kit generate`, `drizzle-kit migrate`) for schema management.
    *   Consider a codebase-first approach for migrations, where TypeScript schema definitions drive database changes.
    *   Implement database logic within dedicated libraries or modules in a monorepo structure.
    *   Use `env()` adapter in Hono for accessing environment variables within route handlers.
    *   Ensure database connection details are securely managed via environment variables.

*   **React/Next.js Frontend & APIs:**
    *   Adopt Test-Driven Development (TDD) for component development.
    *   Follow the Red-Green-Refactor cycle for all new features and bug fixes.
    *   Write focused, minimal failing tests before implementing functionality.
    *   Prioritize testing component behavior from a user's perspective using React Testing Library.
    *   Use Jest as the primary testing framework.
    *   Configure Jest with `jsdom` for testing in a browser-like environment.
    *   Utilize `@testing-library/jest-dom` for custom Jest matchers.
    *   Break down features into small, testable units.
    *   Write unit tests for individual components and functions.
    *   Write integration tests to verify interactions between components and services.
    *   Use `renderHook` from `@testing-library/react-hooks` for testing custom React hooks.
    *   Mock API calls using tools like MSW (Mock Service Worker) for deterministic testing.
    *   Test context providers and global state management (Redux, Zustand, Recoil) by simulating state and interactions.
    *   For React Server Components (RSC), focus on integration tests and mock server-side data fetching.
    *   Use snapshot tests judiciously for static UI elements, avoiding them for highly dynamic components.
    *   Simulate user interactions using `fireEvent` and `user-event` from React Testing Library.
    *   Ensure tests are independent and do not rely on execution order.
    *   Refactor tests alongside production code to maintain clarity and reduce duplication.
    *   Use TypeScript with TDD for enhanced type safety and early error detection.
    *   Integrate TDD into CI/CD pipelines (e.g., GitHub Actions) to automate test execution on every commit.
    *   Parallelize tests to speed up execution in CI/CD.
    *   Enforce code coverage thresholds in CI/CD pipelines to maintain test quality.
    *   Avoid testing implementation details; focus on observable behavior.
    *   Keep tests readable with descriptive names.

*   **Neon-hosted PostgreSQL:**
    *   Use Drizzle ORM for schema definition and migration.
    *   Ensure database connection URLs are managed via environment variables.
    *   Leverage Neon's serverless capabilities for efficient database access.

*   **Drizzle ORM:**
    *   Define database schemas in TypeScript files as the source of truth.
    *   Use `drizzle-kit` for schema generation, migration, and database schema management.
    *   Choose a migration strategy (e.g., codebase-first with `generate` and `migrate`, or `push` for rapid prototyping).
    *   Configure `drizzle-kit` using `drizzle.config.ts` or similar configuration files.
    *   Ensure schema definitions are type-safe and reflect the intended database structure.

*   **Monorepo Structure:**
    *   Encapsulate database logic in dedicated libraries (e.g., `cms-service-database`).
    *   Use Nx or similar tools for managing monorepo libraries and build processes.
    *   Define environment configurations (e.g., `.env.local`) per application within the monorepo.
    *   Ensure `.gitignore` excludes sensitive environment files and local database files.
    *   Configure `project.json` (or equivalent) for build, serve, and migration targets.
    *   Use Fastify plugins to manage database connections and repositories across routes.
    *   Augment `FastifyInstance` types to include decorated properties (e.g., `repository`) for TypeScript awareness.

*   **Prettier (Code Formatting):**
    *   (Implicitly assumed for consistency, though not explicitly detailed in the provided text, it's a standard practice for product agencies).
    *   Configure Prettier to enforce consistent code style across the entire codebase.
    *   Integrate Prettier into pre-commit hooks and CI pipelines.

### Summary of chunk 6
Here's a concise summary of coding standards and best practices relevant to your tech stack:

*   **Testing Strategy:**
    *   Embrace Test-Driven Development (TDD): Write tests *before* implementing code.
    *   Focus on user behavior: Test components from the perspective of how a user would interact with them, not implementation details.
    *   Prioritize accessible queries: Use `getByRole`, `getByLabelText`, `getByText` etc., over `getByTestId` where possible.
    *   Test `getServerSideProps` and `getStaticProps` in Next.js to validate data fetching and rendering.
    *   Ensure components handle a wide range of inputs using property-based testing (e.g., with `fast-check`).
    *   Catch hydration mismatches early by testing components that rely on dynamic data or time.
    *   Mock providers and stores (e.g., Chakra UI, Datx) in tests using custom render utilities.
    *   Use `__mocks__` directory for manual mocks of modules.
    *   Place tests in the same directory as the code they test, with an exception for `pages` in Next.js (`__tests__/pages`).
    *   Mock child components when testing a parent component if the child's internal logic is not relevant to the parent's test.
    *   Use `beforeEach` to render components once for multiple tests within a `describe` block to reduce redundant renders.
    *   Mock API routes using Mock Service Worker (MSW) for isolated testing.
    *   Test custom hooks using `renderHook` and `act` from `@testing-library/react`.
    *   Mock custom hooks using `jest.spyOn` when testing components that consume them.
    *   Use `next-page-tester` for testing Next.js pages with `getServerSideProps` or `getStaticProps`.
    *   Configure `SWRConfig` in tests to provide isolated caches for each component.

*   **Code Formatting & Quality:**
    *   Use Prettier for consistent code formatting across the project.

*   **Monorepo Structure:**
    *   Organize tests within the same directory as the code they test, except for Next.js `pages`.

*   **TypeScript:**
    *   Ensure type safety by installing `@types/react` and `@types/react-dom` when using TypeScript with React Testing Library.

*   **Database (PostgreSQL):**
    *   (No specific standards extracted from this chunk, but Drizzle ORM would typically imply type-safe database interactions).

*   **Node.js/Backend:**
    *   (No specific standards extracted from this chunk, but testing backend logic would follow similar TDD principles).

### Summary of chunk 7
- Use React Testing Library to test React components by interacting with DOM nodes, mirroring user behavior.
- Prioritize queries that align with user interaction (e.g., by label text, button text) over implementation details.
- Use `data-testid` as an escape hatch for querying elements when other methods are impractical.
- Adhere to the Conventional Commits specification for commit messages and PR titles: `<type>[optional scope]: <description>`.
- Use standard commit types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `build`, `ci`, `revert`.
- Keep commit messages concise, ideally within 50-90 characters for the subject line.
- For bug fixes, reference the issue number in the commit message or PR description (e.g., "Fixes #123").
- Break down large features or fixes into smaller, atomic Pull Requests (PRs). Aim for "1 PR = 1 feature/fix".
- For complex features requiring many changes, utilize stacked PRs where each branch targets the previous one.
- Write clear and informative PR descriptions that explain "What changed," "Why," and "How to review."
- Include relevant context in PR descriptions, such as links to tickets, screenshots for UI changes, and deployment notes.
- Ensure PRs are small enough to be reviewed thoroughly; aim for under 400 lines of change.
- Implement automated checks (CI, linting, type checking) that run on every PR before merging.
- Configure branch protection rules for critical branches (e.g., `main`) to require reviews and passing status checks.
- Use Prettier for consistent code formatting across the project.
- Leverage TypeScript for static typing in Node.js and React applications.
- Structure the project using a monorepo.
- For database interactions, use Drizzle ORM with Neon-hosted PostgreSQL.
- Ensure tests are maintainable and focus on component behavior rather than implementation details.
- When writing tests, prefer user-facing queries provided by React Testing Library.
- Use `git rebase -i` to clean up commit history before merging or releasing.
- For PR titles, follow the Conventional Commits format, especially if using squash merges.
- Consider using AI-assisted code review tools as a first pass to catch mechanical issues before human review.
- When reviewing code, prioritize correctness, security, architecture, and maintainability over style.
- Use prefixes like `blocking:`, `nit:`, `question:`, `suggestion:` in code review comments to clarify intent.
- Define Service Level Agreements (SLAs) for PR turnaround times (e.g., time to first review, time to merge).
- Automate testing pre-merge via CI/CD pipelines.
- Ensure database migrations are backward-compatible and consider rollback paths.
- Document new environment variables or feature flags required for changes.

### Summary of chunk 8
- Use a `main` or `master` branch as the single source of truth for production-ready code.
- Implement a deploy-on-merge pattern for automated deployments to production after successful CI checks and code reviews.
- Configure staging environments for an additional verification step before production deployment.
- Utilize PR templates to standardize pull request descriptions, including sections for purpose, necessity, review guidance, testing, and deployment considerations.
- Enforce a maximum PR size limit (e.g., 400 lines) to encourage smaller, more manageable changes.
- Automate code formatting and style enforcement using tools like Prettier to reserve human review for logic and architecture.
- Establish team agreements or SLAs for review turnaround times to prevent "ghost PRs" and long-lived, unmerged branches.
- Separate refactoring efforts from feature development into distinct PRs to improve review clarity and reduce deployment risk.
- Track PR health metrics such as time to first review, time to merge, PR size, and review comments per PR.
- Use descriptive branch names with clear prefixes (e.g., `feature/`, `hotfix/`, `integration/`) to indicate purpose and facilitate organization.
- Ensure all code pushed to `main`/`master` has passed comprehensive automated testing.
- Leverage Drizzle ORM for type-safe database interactions with PostgreSQL.
- Configure Neon-hosted PostgreSQL with environment variables for database connection strings.
- Define database schemas using Drizzle ORM in `db/schema.ts` and manage migrations with `drizzle-kit`.
- Utilize tRPC for type-safe API communication between frontend and backend, especially within Next.js API routes.
- Implement tRPC providers in the frontend to manage client instances and integrate with React Query for caching and state management.
- Employ React Testing Library for writing unit and integration tests for React components.
- Use `create-next-app` with the `--typescript` flag for project initialization.
- Structure Next.js projects using the App Router for modern features like Server Components and Server Actions.
- Mark Server Actions with the `'use server'` directive to enable client-side invocation.
- Differentiate between Server Components (default) and Client Components (`'use client'` directive) based on interactivity and browser API needs.
- Integrate form handling and validation, potentially using libraries like Zod.
- Consider Docker for containerization of the application.

### Summary of chunk 9
*   **Monorepo Structure:** Utilize monorepo tools like Nx or Turborepo for projects with interdependent applications or shared component libraries.
*   **Code Formatting:** Enforce consistent code style using Prettier. Configure Prettier to format code automatically on save.
*   **Linter Integration:** Integrate ESLint with Prettier (using `eslint-config-prettier`) to enforce code style rules and catch errors.
*   **Import Sorting:** Configure Prettier with `@trivago/prettier-plugin-sort-imports` to sort import declarations consistently (e.g., third-party, alias, relative imports).
*   **Environment Variable Management:** Use Zod for type-safe environment variable validation. Leverage `@t3-oss/env-nextjs` for robust management of client-side and server-side variables in TypeScript/Next.js projects.
*   **Environment Variable Security:** Install and configure `eslint-plugin-n` to disallow direct use of `process.env` and enforce usage of the defined environment variable schema.
*   **Form Handling and Validation:** Employ React Hook Form for efficient and flexible form management. Integrate Zod for schema-based client-side and server-side validation, using `zodResolver` with React Hook Form.
*   **Database Integration (Drizzle ORM):** Use Drizzle ORM for PostgreSQL integration. Define table schemas directly in TypeScript, eliminating the need for separate code generation steps. Leverage Drizzle's built-in Zod validators.
*   **Database Connection:** Initialize Drizzle ORM with a PostgreSQL adapter, connecting to Neon-hosted PostgreSQL instances using the `postgres` driver and the `DATABASE_URL` environment variable.
*   **Database Schema Definition:** Define PostgreSQL schemas using Drizzle's `pgTable` and related functions, including primary keys, constraints, indexes, and relations.
*   **Testing Framework:** Utilize Vitest or Jest as the testing framework. Complement with React Testing Library for rendering components and simulating user interactions.
*   **Authentication:** Implement authentication using Auth.js (formerly NextAuth.js) for secure and simplified authentication flows, supporting providers like Google and email/password credentials.
*   **Session Management:** For Auth.js, configure session strategy to `jwt` for stateless session management using tokens.
*   **Server Component Usage:** Prefer Server Components for database interactions, handling sensitive data (API keys, tokens), and optimizing JavaScript bundle size.
*   **Client Component Usage:** Use Client Components for component state management, event handling, lifecycle methods (`useEffect`), and direct browser API access.
*   **Styling:** Adopt Tailwind CSS for utility-first styling. Consider `shadcn/ui` for pre-built, customizable components that leverage Tailwind CSS.
*   **Docker for Database:** Manage PostgreSQL instances using Docker Compose, defining services, environment variables, ports, and volumes in a `docker-compose.yml` file.
*   **Type Safety:** Utilize TypeScript throughout the project for enhanced type safety and maintainability.
*   **Code Collaboration:** Implement a peer review process for Pull Requests, ensuring code quality, consistency, and knowledge sharing.
*   **Enum Usage:** Prefer enums or frozen constant objects over raw string comparisons for reusable values to prevent runtime errors.
*   **Styling Practices:** Avoid inline styling; use CSS preprocessors like SCSS with variables for reusable colors and theming.