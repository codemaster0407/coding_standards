## Source: https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052

[Skip to content](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#main-content)
Navigation menu [ ![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png) ](https://dev.to/)
Search [ Powered by Algolia Search ](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)
[ Log in ](https://dev.to/enter?signup_subforem=1) [ Create account ](https://dev.to/enter?signup_subforem=1&state=new-user)
## DEV Community
Close
![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg) 2 Add reaction 
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) 1 Like  ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) 0 Unicorn  ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) 0 Exploding Head  ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) 1 Raised Hands  ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg) 0 Fire 
0 Jump to Comments  0 Save  Boost 
More...
Copy link Copy link
Copied to Clipboard
[ Share to X ](https://twitter.com/intent/tweet?text=%22How%20to%20build%20a%20convenient%20typescript%20full-stack%20monorepo%22%20by%20Herman%20Hrand%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Fallohamora%2Fhow-to-build-a-convenient-typescript-full-stack-monorepo-3052) [ Share to LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Fallohamora%2Fhow-to-build-a-convenient-typescript-full-stack-monorepo-3052&title=How%20to%20build%20a%20convenient%20typescript%20full-stack%20monorepo&summary=Hi%2C%20my%20name%20is%20Herman.%20Over%20the%20years%20I%20have%20seen%20many%20teams%20set%20up%20a%20full-stack%20monorepo%2C%20get%20it...&source=DEV%20Community) [ Share to Facebook ](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Fallohamora%2Fhow-to-build-a-convenient-typescript-full-stack-monorepo-3052) [ Share to Mastodon ](https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2Fallohamora%2Fhow-to-build-a-convenient-typescript-full-stack-monorepo-3052)
[Share Post via...](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052) [Share Post via...](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052) [Report Abuse](https://dev.to/report-abuse)
[![Herman Hrand](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3807347%2Fe294fd92-464c-489e-ade7-ecaba741f1ba.png)](https://dev.to/allohamora)
[Herman Hrand](https://dev.to/allohamora)
Posted on 24 Mar
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) 1 ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) 1 ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
#  How to build a convenient typescript full-stack monorepo 
[#javascript](https://dev.to/t/javascript) [#typescript](https://dev.to/t/typescript) [#monorepo](https://dev.to/t/monorepo) [#fullstack](https://dev.to/t/fullstack)
Hi, my name is Herman. Over the years I have seen many teams set up a full-stack monorepo, get it working, and then spend the rest of the project patching rough edges, adding hacks, or delaying improvements because they turn out to be too painful to make. After enough of that, the conclusion is often simple: a monorepo is not worth it.
I do not think the monorepo itself is usually the problem. More often, the problem is a setup that was put together quickly and never made convenient for day-to-day work. In this article, I want to show the approach I use to keep a full-stack monorepo smooth, practical, and close to normal application development.
I am writing this for engineers who want one repository for `client`, `api`, and `shared` typescript code, but do not want the monorepo to complicate day-to-day development. I will use my own repository as the example, not as a universal template, but as a concrete demonstration of decisions and tradeoffs.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#why-i-choose-a-monorepo-for-fullstack-work) Why I choose a monorepo for full-stack work 
I do not think every full-stack application should live in a monorepo. If `api` and `client` can be fully implemented within one framework like astro, or if they barely depend on each other, a monorepo may be unnecessary.
But I often build systems where `api` and `client` are tightly related while still needing to stay separate applications. I may want a dedicated `api` with its own runtime and its own deployment. I may also need websockets or a job queue, which can be awkward to implement inside some full-stack frameworks. In those cases, a monorepo becomes a good middle ground.
It keeps the applications close enough to share contracts and runtime code, but it does not force everything into one structure shaped by a specific framework. In this repository, `api` is a hono app and `client` is a react app built with vite. The `client` can import types from `api` to make type-safe requests, and anything else that should be shared can live in the `shared` library.
The alternative is often more expensive than it seems at first. As soon as I split a tightly connected system into separate repositories, I usually need private package publishing, version coordination, and more complicated ci. In my experience, that often creates more problems than a monorepo, not fewer.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#what-i-actually-want-from-a-fullstack-monorepo) What I actually want from a full-stack monorepo 
Before I choose tools, I define what I want from the monorepo, otherwise it becomes too easy to chase features instead of solving practical problems with minimal setup.
For a full-stack typescript monorepo, my baseline requirements are fairly simple:
  * Clear boundaries between applications, shared runtime code, and tooling.
  * The ability to run scripts from the repository root when that is convenient, while keeping each workspace useful on its own.
  * Shared code without publishing internal packages or rebuilding them after every small change.
  * Dev scripts that react naturally to changes in dependencies.
  * CI that runs checks only where they matter.
  * Docker images that include only what the target application needs.
  * Git history and repository conventions that stay understandable for regular application developers.


##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#simple-workspace-boundaries) Simple workspace boundaries 
The first thing I want from a monorepo is a structure that makes sense as soon as I open it, without any explanation. I do not want top-level folders whose meaning changes from project to project. I want boundaries that tell me what something is before I read its code.
That is why I use a very simple split:  


```
apps/
├── api
└── client

libs/
└── shared

packages/
├── eslint-config
├── prettier-config
└── tsconfig

```

Enter fullscreen mode Exit fullscreen mode
`apps/` contains runnable applications. `libs/` contains shared runtime code. `packages/` contains tooling and shared configuration. This is not a revolutionary structure, but that is exactly why I like it. It scales well, it is easy to scan, and it keeps runtime code separate from tooling concerns.
At the package manager level, I keep the foundation just as simple. Npm workspaces already give me what I need here: dependency resolution between workspaces, symlinked internal packages through `node_modules`, and root-level script execution.  


```
{
  "name": "@example/root",
  "private": true,
  "workspaces": ["apps/*", "libs/*", "packages/*"]
}

```

Enter fullscreen mode Exit fullscreen mode
I know many teams prefer pnpm or yarn, and those are excellent tools, but for my requirements npm is enough and there is no reason to add another tool to the stack without a real need.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#buildless-typescript-internal-packages) Buildless typescript internal packages 
The biggest choice in this setup is how I treat shared internal packages. A lot of monorepo discussions start from the assumption that they should be built first and then consumed as compiled output. That can be the right choice in some environments, but I do not want it by default.
For internal code that lives entirely inside one repository, I prefer the approach that turborepo documentation calls a [just-in-time internal package](https://turborepo.dev/docs/core-concepts/internal-packages#just-in-time-packages). In practice, the package points directly to typescript source files, and the rest of the toolchain consumes them without a separate build step.  


```
{
  "name": "@example/shared",
  "private": true,
  "type": "module",
  "main": "src/index.ts",
  "imports": {
    "#src/*.ts": "./src/*.ts"
  }
}

```

Enter fullscreen mode Exit fullscreen mode
This one decision removes a surprising amount of infrastructure code that usually appears in a monorepo. At the same time, it forbids typescript aliases, because aliases already require a build step.
If I wanted aliases for internal packages, I would have to add a build into `dist/`, then do a post-build rewrite with something like tsc-alias, and also keep separate watch support for rebuilds. With `turbo watch`, that would mean either unnecessary restarts of the dev process or a parallel loop rebuilding dependencies on every change. If I needed finer behavior, where only monorepo dependencies get rebuilt while local changes are still handled by the application's own watcher, I would have to go further. In practice, that usually ends with a custom watch script on top of something like turbowatch and even a separate internal scripts package.
The problem often does not stop at runtime. After a few rebuilds, the typescript server in the editor can stop syncing correctly, so I either restart it manually or patch the setup with `references` without `composite` to keep the ide aligned with the current state. That tradeoff can be justified if the package needs to be published or the toolchain truly requires compiled output, but without a real need I would not do it.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#why-development-stays-smooth) Why development stays smooth 
The buildless package decision works because the runtime and tooling choices support it instead of fighting it.
This repository targets modern node.js with erasable syntax and relies on running typescript entry files directly. The `api` package uses `node src/index.ts` for start and `node --watch src/index.ts` for development. The `shared` library also works directly with source code. That means I can change code in `@example/shared`, and normal tooling picks it up without a separate cycle of rebuilding the package, restarting the application, and updating the editor state.
The typescript configuration is intentionally aligned with that model:  


```
{
  "compilerOptions": {
    "target": "esnext",
    "verbatimModuleSyntax": true,
    "strict": true,
    "erasableSyntaxOnly": true,
    "allowImportingTsExtensions": true,
    "rewriteRelativeImportExtensions": true,
    "module": "NodeNext",
    "noEmit": true
  }
}

```

Enter fullscreen mode Exit fullscreen mode
This matters not only for `api`. Vite and vitest on the `client` side can also work with internal packages directly, so I do not need extra monorepo orchestration on top of the normal workflow.
This is also where the benefit of importing types from `api` shows up:  


```
// apps/api/src/app.ts
export const app = new Hono().get('/ping', (c) => c.text(ping()));
export type App = typeof app;

// apps/client/src/api.ts
import { type App } from '@example/api/app';
import { hc } from 'hono/client';

const api = hc<App>('http://localhost:3000');

// somewhere in the client code
const res = await api.ping.$get();
console.log(await res.text());

```

Enter fullscreen mode Exit fullscreen mode
If I break the server contract with an incompatible change, `client` can fail during typechecking instead of letting the mismatch survive until runtime. When something cannot or should not be exported directly from the server package, I move it into the `shared` library. That keeps the contract between applications close to the code that uses it.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#the-conventions-that-make-daily-work-smoother) The conventions that make daily work smoother 
I keep shared eslint, prettier, and typescript configs in `packages/eslint-config`, `packages/prettier-config`, and `packages/tsconfig`, and I treat them like ordinary workspace packages.
For shared prettier, each workspace adds `@example/prettier-config` and points its `prettier` field to it in `package.json`. `.prettierignore` cannot be shared the same way, so it has to be duplicated in each workspace and at the root.  


```
// packages/prettier-config/src/index.json
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": true,
  "printWidth": 120
}

// apps/api/package.json
{
  "devDependencies": {
    "@example/prettier-config": "*"
  },
  "prettier": "@example/prettier-config"
}

```

Enter fullscreen mode Exit fullscreen mode
For eslint, I usually want the shared package to provide a few obvious base configs like `base` and `node`, while each workspace keeps a small local `eslint.config.mjs`. In this repository, `api` and the `shared` library can simply export `eslintConfig.node`, while `client` has `eslintConfig.base` with additional rules for react and vite.  


```
// packages/eslint-config/src/index.mjs
export const base = defineConfig(
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  eslintPluginPrettierRecommended,
);

// apps/client/eslint.config.mjs
export default defineConfig([...eslintConfig.base, reactHooks.configs.flat.recommended, reactRefresh.configs.vite]);

```

Enter fullscreen mode Exit fullscreen mode
Typescript follows the same pattern, but the package shape is simpler. A shared `tsconfig` package usually just keeps files like `node.json` at the package root, then each workspace extends what it needs. In this repo, `api` and `shared` extend `@example/tsconfig/node.json`, while `client` keeps its own `tsconfig` files because vite has its own constraints.  


```
// packages/tsconfig/node.json
{
  "compilerOptions": {
    "target": "esnext",
    "verbatimModuleSyntax": true,
    "erasableSyntaxOnly": true,
    "module": "NodeNext",
    "noEmit": true
  }
}

// apps/api/tsconfig.json
{
  "extends": "@example/tsconfig/node.json"
}

```

Enter fullscreen mode Exit fullscreen mode
I apply the same thinking to commit hygiene. Husky and lint-staged run fixes before commit, and the nearest config handles the staged files, so the repository root has its own set of checks while apps and libraries keep their own local setup. `apps`, `packages`, and `libs` are ignored for root checks, which keeps root formatting, linting, and typechecking focused on root files.  


```
# .husky/pre-commit
npx --no-install lint-staged

```

Enter fullscreen mode Exit fullscreen mode

```
// package.json
"lint-staged": {
  "*.{js,cjs,mjs,json,yml,md}": "prettier --write",
  "*.ts": "eslint --fix"
}

// apps/client/package.json
"lint-staged": {
  "*.{js,cjs,mjs,json,yml,md,html,css}": "prettier --write",
  "*.{ts,tsx}": "eslint --fix"
}

```

Enter fullscreen mode Exit fullscreen mode
Conventional commits help here too, and commit scopes are especially useful. With `feat(api):` or `fix(client):`, I can see which part of the system changed before opening the diff, while a plain `feat:` usually means the change touches multiple applications or the whole repository. That makes both the history easier to read and the changelog easier to generate through conventional-changelog. It is a small convention, supported by commitlint and husky, but it pays off over time.  


```
# .husky/commit-msg
npx --no-install -- commitlint --edit "$1"

```

Enter fullscreen mode Exit fullscreen mode

```
// .commitlintrc.json
{
  "extends": ["@commitlint/config-conventional"]
}

```

Enter fullscreen mode Exit fullscreen mode

```
// package.json
"scripts": {
  "update:changelog": "conventional-changelog -p conventionalcommits"
}

```

Enter fullscreen mode Exit fullscreen mode
I also find custom pull request labels like `shared`, `api`, or `client` useful, because they let me filter pull requests and understand what was touched before reading the files.
I also simplify the versioning scheme on purpose. This repository uses one version for the root package and all workspaces, so there is no need for separate versions for each package or a more complicated version update process, and `scripts/release.ts` shows a simple example of that release flow.  


```
// scripts/release.ts
const setPackageJsonVersion = async (version: string) => {
  await $`npm version ${version} --commit-hooks false --git-tag-version false`; // root package.json
  await $`npm version ${version} --workspaces --commit-hooks false --git-tag-version false`;
};

const updateChangelog = async () => {
  await $`npm run update:changelog`;
};

const version = await getVersion();

// other actions like create release branch, bump version in .env, make a commit, etc.
await setPackageJsonVersion(version);
await updateChangelog();

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#where-turborepo-earns-its-place) Where turborepo earns its place 
In this setup, turborepo is not mandatory, but in some places it is really useful.
The clearest example is affected ci. I want the repository to understand relationships between packages and run checks only where a change actually matters, and turborepo already does that well enough.  


```
# .github/workflows/affected.yml
env:
  # https://github.com/vercel/turborepo/issues/9320
  TURBO_SCM_BASE: ${{ github.event_name == 'pull_request' && github.event.pull_request.base.sha || github.event.before }}

steps:
  - run: npx turbo run format --affected
  - run: npx turbo run lint --affected
  - run: npx turbo run typecheck --affected
  - run: npx turbo run test --affected

```

Enter fullscreen mode Exit fullscreen mode

```
// turbo.json
"//#format": {
  "cache": false,
  "inputs": ["$TURBO_DEFAULT$", "!apps/**", "!libs/**", "!packages/**"]
}

```

Enter fullscreen mode Exit fullscreen mode
In this example, I set `TURBO_SCM_BASE` explicitly in github actions to help turborepo find the right comparison point when using `--affected`, and those root tasks are there so affected runs can include root files, not just workspace changes.
Docker is the other obvious example. `turbo prune` lets me build an image from only the code and dependencies the target application needs instead of pulling the whole repository into the build context. In this repo, the `Dockerfile` for `api` uses `turbo prune --scope=@example/api --docker` for exactly that reason. That is real value, not abstraction for its own sake.
This is also why I do not use nx here. I think it works well when a repository stays inside its model, but that comes with more abstraction and more magic.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#the-extra-qualityoflife-pieces) The extra quality-of-life pieces 
Once the main workflow is stable, a few smaller choices make the repository nicer to live in.
One of them is code generation. A lot of monorepo work is repetitive: create a package, add scripts, wire shared configs, fill out the basic structure, and make sure no small detail gets missed. In this repo, I use plop for that and show an example of it in the root `generate:package` script. The same approach works anywhere the structure repeats, for example when creating a new microservice together with changes to the terraform schema. It is not a core architectural piece, but it saves me from boring copy-paste mistakes.  


```
// plopfile.ts
export default function configurePlop(plop: NodePlopAPI): void {
  plop.setGenerator('package', {
    description: 'Create a package in packages',
    prompts: [
      {
        type: 'input',
        name: 'name',
      },
    ],
    actions: () => [
      {
        type: 'add',
        path: 'packages/{{name}}/package.json',
        templateFile: 'plop-templates/package/package.json.hbs',
      },
      {
        type: 'add',
        path: 'packages/{{name}}/.prettierignore',
        templateFile: 'plop-templates/package/.prettierignore.hbs',
      },
      async () => {
        await $`npm install`;

        return 'npm install';
      },
    ],
  });
}

```

Enter fullscreen mode Exit fullscreen mode

```
// package.json
{
  "scripts": {
    "generate:package": "plop package"
  }
}

```

Enter fullscreen mode Exit fullscreen mode
Another is how I work with ai agents in the repository. In a monorepo, I prefer running the agent from the repository root. That keeps its state, permissions, and memory in one place instead of scattering them across workspaces. When the agent needs to work inside a nested app or library, it can automatically load the local `AGENTS.md` / `CLAUDE.md` file there. That lets me keep instructions close to specific parts of the repo when I need them.
##  [ ](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052#conclusion) Conclusion 
This approach relies on a few simple decisions that fit together well. Npm workspaces handle local package linking, buildless internal packages remove the endless rebuild cycle, modern node.js simplifies the typescript workflow, and turborepo stays only where it really provides a benefit.
I am not presenting this repository as a perfect template that every team should copy. I am simply showing an idea and a set of tradeoffs. But if you are building a full-stack typescript system and you are tired of monorepos that feel heavier than the product itself, this is the direction I would start with.
Repository: <https://github.com/allohamora/monorepo-example>
##  Top comments (0)
Subscribe
![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)
Personal Trusted User [ Create template ](https://dev.to/settings/response-templates)
Templates let you quickly answer FAQs or store snippets for re-use.
Submit Preview [Dismiss](https://dev.to/404.html)
[Code of Conduct](https://dev.to/code-of-conduct) • [Report abuse](https://dev.to/report-abuse)
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](https://dev.to/allohamora/how-to-build-a-convenient-typescript-full-stack-monorepo-3052). 
Hide child comments as well
Confirm 
For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)
[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3807347%2Fe294fd92-464c-489e-ade7-ecaba741f1ba.png) Herman Hrand  ](https://dev.to/allohamora)
Follow
  * Work 
Empire National 
  * Joined 
5 Mar 2026


###  Trending on [DEV Community](https://dev.to) Hot
[ ![Syed Ahmer Shah profile image](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3021645%2F43b6a034-629c-4334-a57c-67f51255be00.PNG) Stop Letting AI Write Your Database Migrations  #ai #programming #productivity #discuss ](https://dev.to/syedahmershah/stop-letting-ai-write-your-database-migrations-2a26) [ ![FrancisTRᴅᴇᴠ \(っ◔◡◔\)っ profile image](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3711376%2F033bd8c0-e583-42ce-9865-056a9e75e3f8.webp) Welcome to the DEVengers Organization! A group of Extraordinary Individuals that Influenced Dev.to the platform has ever seen! 🚀  #discuss #community #meta #programming ](https://dev.to/devengers/welcome-to-the-devengers-organization-a-group-of-extraordinary-individuals-that-influenced-devto-4ifb) [ ![GDS K S profile image](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3592860%2F7dec468f-4f91-4b1d-9d24-99091e204707.jpg) I built a 200 line AI router in TypeScript. My monthly bill dropped 41%.  #typescript #ai #webdev #tutorial ](https://dev.to/thegdsks/i-built-a-200-line-ai-router-in-typescript-my-monthly-bill-dropped-41-23ok)
💎 DEV Diamond Sponsors 
Thank you to our Diamond Sponsors for supporting the DEV Community 
[ ![Google AI - Official AI Model and Platform Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxjlyhbdqehj3akhz166w.png) ](https://aistudio.google.com/?utm_source=partner&utm_medium=partner&utm_campaign=FY25-Global-DEVpartnership-sponsorship-AIS&utm_content=-&utm_term=-&bb=146443)
Google AI is the official AI Model and Platform Partner of DEV
[ ![Neon - Official Database Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbnl88cil6afxzmgwrgtt.png) ](https://neon.tech/?ref=devto&bb=146443)
Neon is the official database partner of DEV
[ ![Algolia - Official Search Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv30ephnolfvnlwgwm0yz.png) ](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral&bb=146443)
Algolia is the official search partner of DEV
[DEV Community](https://dev.to/) — A space to discuss and keep up software development and manage your software career 
  * [ Home ](https://dev.to/)
  * [ DEV++ ](https://dev.to/++)
  * [ Reading List ](https://dev.to/readinglist)
  * [ Videos ](https://dev.to/videos)
  * [ DEV Education Tracks ](https://dev.to/deved)
  * [ DEV Challenges ](https://dev.to/challenges)
  * [ DEV Help ](https://dev.to/help)
  * [ Advertise on DEV ](https://dev.to/advertise)
  * [ Organization Accounts ](https://dev.to/organizations)
  * [ DEV Showcase ](https://dev.to/showcase)
  * [ About ](https://dev.to/about)
  * [ Contact ](https://dev.to/contact)
  * [ Free Postgres Database ](https://dev.to/free-postgres-database-tier)
  * [ DEV Shop ](https://shop.forem.com/)
  * [ MLH ](https://mlh.io/)


  * [ Code of Conduct ](https://dev.to/code-of-conduct)
  * [ Privacy Policy ](https://dev.to/privacy)
  * [ Terms of Use ](https://dev.to/terms)


Built on [Forem](https://www.forem.com) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to) and other inclusive communities.
Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2026.
![DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)
We're a place where coders share, stay up-to-date and grow their careers. 
[ Log in ](https://dev.to/enter?signup_subforem=1) [ Create account ](https://dev.to/enter?signup_subforem=1&state=new-user)
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)


## Source: https://monorepo.tools/typescript

[monorepo.tools](https://monorepo.tools/)
[Home](https://monorepo.tools/)[AI & Monorepos](https://monorepo.tools/ai)[Synthetic Monorepos](https://monorepo.tools/synthetic-monorepos)[Compare](https://monorepo.tools/compare)[TypeScript](https://monorepo.tools/typescript)
LightDarkSystem
Toggle theme
![cover](https://monorepo.tools/images/monorepo-background.jpg)
# TypeScript Monorepos [](https://monorepo.tools/typescript#understanding-monorepos)
As TypeScript projects increasingly become the standard way of developing Frontend and Backend applications, the need for standardizing project setup has also increased. One way to achieve this is to adopt a monorepo in your organization. With TypeScript projects however, there are unique challenges that can impact your developer experience significantly.
There are many ways to make your TypeScript monorepo experience, so if you have any suggestions and would like to contribute them, [we welcome pull requests to help improve things!](https://github.com/nrwl/monorepo.tools?utm_source=monorepo.tools "Contribute to monorepo.tools!")
## Project Structure
Let's look at strategies for how to best structure a TypeScript Monorepo
[Project Structure →](https://monorepo.tools/typescript#project-structure "Project Structure")
## Path Aliases
Move from long path imports to path aliases for your initial step
[Path Aliases →](https://monorepo.tools/typescript#path-aliases "Path Aliases")
## Workspaces
Manage your monorepo using your package manager's workspace
[Workspaces →](https://monorepo.tools/typescript#workspaces "Use package manager's workspace")
## Project References
How TypeScript can assist in optimizing your monorepo
[Project References →](https://monorepo.tools/typescript#project-references "Project References")
# Project Structure[](https://monorepo.tools/typescript#what-is-a-monorepo)
Starting off from collocated code and moving towards following best practices
## Take your monorepo from just a collection of directories, to well defined modules using Path Aliases, Workspaces, and Project References.
By knowing how each of these concepts works in regards to you TypeScript monorepo, you can better organize your codebase and keep your builds fast.
![typescript monorepo project structure](https://monorepo.tools/images/typescript/project-structure.svg)
## How your code is shared across a monorepo
With each of these approaches, what we're really trying to solve is how the individual packages in your monorepo are made available to each other.
For instance, if you have app "A" and it is trying to import library "B", it can be cumbersome to have to write direct path imports to the library. As a project grows, this can be a challenge to manage, as well as negatively impacting your build times.
In addition to this, each approach can impact how TypeScript understands your project. From being able to find all the references for a symbol across your monorepo, to being able provide speedy code completion in your editor.
![code sharing in monorepos](https://monorepo.tools/images/typescript/code-sharing.svg)
With each of these approaches, what we're really trying to solve is how the individual packages in your monorepo are made available to each other. If your monorepo is rather new or small and the relative connections across each package, you might feel confident with using direct imports (directly importing modules using relative paths), but as your monorepo eventually grows the need for well-defined modules will increase.
# Path Aliases[](https://monorepo.tools/typescript#why-a-monorepo)
Path Aliases allow you to replace long import paths with a user supplied key for imports.
# Mapping to a path[](https://monorepo.tools/typescript#mapping-to-a-path)
In the simplest terms, path aliases are a TypeScript construct that allow you to point to a directory somewhere in your codebase. When you import from `@my-org/lib-a` with path aliases, you actually aren't treating that package as a module.
![typescript path mappings](https://monorepo.tools/images/typescript/path-mappings.svg)
Path aliases tell TypeScript to not treat the import statement as a module to be resolved, but rather use the key of `'@my-org/lib-a'` as a reference to where the module is located. However, if you build and try to run the compile output, you will get an error as the TypeScript compiler doesn't actually replace the import path with the correct path. For this, you'd need an extra tool or build step to find and replace the aliased path with the correct relative path.
![libraries in silos](https://monorepo.tools/images/typescript/lib-silo.svg)
Path Aliases also don't actually change how our monorepo is structured or if we have well defined boundaries, they just address to visual of long import statements. Our code, while collocated, is not isolated in any meaningful way. With this in mind, the use of Path Aliases should be considered a step towards something better.
In fact, the TypeScript team even stated that developers should avoid using path aliases all together. If you are wanting to go full in on monorepos, there are better solutions that can be found in your package managers.
# Workspaces[](https://monorepo.tools/typescript#workspaces)
Workspaces are a mechanism to properly connect the packages in your monorepo as modules.
# At a glance[](https://monorepo.tools/typescript#workspaces-at-a-glance)
Workspaces are a built in feature of most JavaScript packages managers that allow you to tell the package manager a certain directory contains subprojects. Package managers like `npm`, `yarn`, and `pnpm` all provide a way to setup a workspace.
![project workspaces](https://monorepo.tools/images/typescript/workspaces.svg)
With workspaces, when your packages manager reads the `package.json`, it will take any directory in that `workspaces` and link it to your root `node_modules`. When your project is being build, the build tools can treat things as if it was just another packages installed from a package registry. The benefit here is that there is no additional overhead that path aliases would introduce.
Workspaces however, do require an extra step before the packages can be used in your monorepo. Since most packages require some sort of build step before being able to consume the code, the monorepo tool you choose will have a big impact here. For instance, with Nx, you can have the build step of dependent projects be performed before you start up the main process. Alternatively, you'd have to build the packages manually before starting any other process. Check with your monorepo tool to see if they support automatic builds of dependencies.
# Direct Exports ⚔ vs Pre-built Code
With workspaces, we have two options for making our code accessible through out our codebase. We could prebuild our code or we could directly export the TypeScript source. .
## Direct Export
By directly exporting, this means to take your TypeScript source and set it as your exports in a `package.json`
If the modules in your monorepo are for internal use and will never be published to a package registry, this is a valid option.
![direct export of typescript](https://monorepo.tools/images/typescript/direct-export.svg)
## Prebuild
With prebuilding, you're running the build tasks needed for any module in the monorepo ahead of time. You export the compiled and generated code, and provide the generated types.
The benefit here is that everything can be done ahead of time, so you only have one task being run. However, if you need to change the modules being consumed, you need to rerun the build for the affected module. Some monorepo tools, like [Nx](https://nx.dev) provide a way to do this, but other tools might not.
![direct export of typescript](https://monorepo.tools/images/typescript/prebuild.svg)
Either option can work, the major factor would be if you are publishing the libraries for others to use outside of your monorepo.
# Project References[](https://monorepo.tools/typescript#type-references)
Provide deeper understanding of your monorepo's types and speed up TypeScript compilation for large projects.
## References Across Monorepos
With the move to workspaces, one thing that gets left behind is the detailed type information that our projects can provide. Path Aliases also have this issue, as deeply nested imports might not always get the correct type information from TypeScript. We can help TypeScript out here by utilizing Project References.
![typescript path mappings](https://monorepo.tools/images/typescript/reference-404.svg)
Project References are references to nested `tsconfig.json`s that are in a workspace. By providing them, you can inform the TypeScript compiler about any nested projects and the types present in there. Now TypeScript will be able to treat each project as it's own isolated piece of code, and can better optimize how it returns any type information for your editor. In addition to the type benefits, TypeScript can now compile pieces of your codebase in better isolation. In the loosest sense, project references turn the TypeScript compiler into a monorepo tool.
![direct export of typescript](https://monorepo.tools/images/typescript/project-references.svg)
Project references can have some draw back in monorepos that include a lot of types. For instance, trpc can generate type information for every route in your API. Normally this is great, and project references can make sure that type information is available to you. But if you have a large API, you could be dealing with significant delays in your editor when you try to trigger auto-completion or get a symbol's type. This isn't only isolated to trpc, but any monorepo that has a large and complex type setup.
# Performance Benchmarks[](https://monorepo.tools/typescript#type-references)
Understand the performance impact of how you setup your TypeScript monorepo
## Shipping code faster
How you structure your TypeScript monorepo impacts more than your developer experience, it can also impact how fast changes in your repo are built and released to the world. With package linking and project references, the overall build time for your monorepo can be significantly faster. With faster CI times, you can get things shipped faster all while having a better developer experience.
![a figure eight with arrows](https://monorepo.tools/images/typescript/cicd.svg)
In the [following example](https://github.com/nrwl/typecheck-timings), we compare the build times for a TypeScript monorepo using path aliases with a TypeScript monorepo using project references and workspaces. This example uses Nx, but other monorepo tools may have similar results.
Path Aliases
186.53s  cold
References + Workspace
175.52s  cold
25.33s  hot
References + Workspace (incremental updates)
36.33s  1 package
48.21s  5 packages
65.25s  25 packages
80.69s  100 packages
What's worth pointing out here is the difference in time when dealing with incremental updates. With Path Aliases, TypeScript needs to perform full rebuild of every package. However, with project references in place, TypeScript can understand what packages have changed and skip a rebuild if possible, reducing the time needed to rebuild.
# # Resources[](https://monorepo.tools/typescript#monorepo-resources)
Here is a curated list of useful videos and podcasts to go deeper or just see the information in another way.
## Videos & Podcasts[](https://monorepo.tools/typescript#monorepo-videos-podcasts)
Here are some video and podcast about monorepos that we think will greatly support what you just learned.
  * [The Dilemma of TypeScript in Monorepos](https://www.youtube.com/watch?v=RRsttfhg1sA)
  * [Monorepos - What, Why, When and How | Full Stack React + Hono Example](https://www.youtube.com/watch?v=KIgPJT806D0)
  * [TypeScript Monorepos Done Right!](https://www.youtube.com/watch?v=D9D8KNffyBk)
  * [TypeScript Project References Demistified](https://www.youtube.com/watch?v=SDE3cIq28s8)


## Articles[](https://monorepo.tools/typescript#typescript-articles)
Here is a curated list of articles about monorepos that we think will greatly support what you just learned.
  * [TypeScript Project References Doc](https://www.typescriptlang.org/docs/handbook/project-references.html)
  * [TypeScript Paths Doc](https://www.typescriptlang.org/tsconfig/#paths)
  * [Using TypeScript Project References to share common code](https://wallis.dev/blog/typescript-project-references)
  * [Sharing Code in TypeScript and Project References](https://theartofdev.com/2024/11/07/sharing-code-in-typescript-and-project-references/)
  * [Everything you need to know about TypeScript Project Refernces](https://nx.dev/blog/typescript-project-references)
  * [Managing TypeScript Packages in Monorepos](https://nx.dev/blog/managing-ts-packages-in-monorepos)


© 2026 [Nx](https://nx.dev "Nx") and [Contributors](https://monorepo.tools/typescript#monorepo-contributors)


## Source: https://nx.dev/blog/managing-ts-packages-in-monorepos

[](https://nx.dev)[Docs](https://nx.dev/docs/getting-started/intro)[Blog](https://nx.dev/blog)
Solutions
[ For Developers Accelerate your CI with Nx: smart cache sharing, flaky-test auto-retries, parallel runs & dynamic agents. ](https://nx.dev/solutions/engineering)[ Engineering Managers Boost efficiency with powerful monorepos and intelligent CI. Build, test, and deploy faster, freeing teams to innovate. ](https://nx.dev/solutions/management)[ Platform & DevOps Teams Get dependable, out-of-the-box CI that scales effortlessly. Cut costs and boost speed with smart caching, distribution, and enhanced security. ](https://nx.dev/solutions/platform)[ CTOs & VPs of Engineering Supercharge engineering ROI with faster delivery, lower CI costs, and fewer risks. Scale safely and future-proof your stack. ](https://nx.dev/solutions/leadership)[ Nx LabsService From expert training to hands-on engineering support, we meet teams where they are and help them move forward with confidence. ](https://nx.dev/contact/labs)[ Security Protect your codebase from artifact poisoning with infrastructure-first security. ](https://nx.dev/enterprise/security)
Resources
#### Learn
  * [Step By step tutorials](https://nx.dev/docs/getting-started/tutorials)
  * [Newsletter](https://go.nrwl.io/nx-newsletter)
  * [Books](https://nx.dev/resources)
  * [Whitepapers](https://nx.dev/resources)
  * [Case Studies](https://nx.dev/customer-stories)


#### Medias
  * [Nx Video Courses](https://nx.dev/courses)
  * [Nx Live](https://www.youtube.com/playlist?list=PLakNactNC1dE8KLQ5zd3fQwu_yQHjTmR5)
  * [Webinars](https://nx.dev/webinars)


#### Company
  * [About Us](https://nx.dev/company)
  * [Customers](https://nx.dev/customers)
  * [Partners](https://nx.dev/partners)


#### Subscribe
  * [](https://www.youtube.com/@NxDevtools)
  * [](https://x.com/NxDevTools)
  * [](https://discord.com/invite/SWyp4xfGjn)


[Nx Cloud](https://nx.dev/nx-cloud)[Pricing](https://nx.dev/nx-cloud#plans)[Enterprise](https://nx.dev/enterprise)
[Contact](https://nx.dev/contact)[Try Nx Cloud for Free](https://cloud.nx.app/get-started?utm_source=nx-dev&utm_medium=header)
[](https://nx.dev)
[‹ Blog](https://nx.dev/blog)
![Juri Strumpflohner](https://nx.dev/blog/images/Juri%20Strumpfloner.webp)
![Juri Strumpflohner](https://nx.dev/blog/images/Juri%20Strumpfloner.webp)Juri Strumpflohner
[](https://x.com/juristr)[](https://github.com/juristr)
January 28, 2025
# Managing TypeScript Packages in Monorepos
![Managing TypeScript Packages in Monorepos](https://nx.dev/blog/images/articles/bg-managing-typescript-packages.jpg)
TypeScript Project References Series
This article is part of the TypeScript Project References series:
  * [Everything You Need to Know About TypeScript Project References](https://nx.dev/blog/typescript-project-references)
  * **Managing TypeScript Packages in Monorepos**
  * [A new Nx Experience For TypeScript Monorepos and Beyond](https://nx.dev/blog/new-nx-experience-for-typescript-monorepos)


Managing TypeScript packages in a monorepo presents unique challenges. As your monorepo grows, so does the complexity of structuring and resolving dependencies between packages. From using simple relative imports to taking advantage of TypeScript path aliases, project references, and your package manager's workspaces feature, developers have a variety of strategies at their disposal. But which approach is the best fit for you?
Table of Contents
  * 1.[What Does it Mean to Manage and Share TypeScript Code in a Monorepo?](https://nx.dev/blog/managing-ts-packages-in-monorepos#what-does-it-mean-to-manage-and-share-typescript-code-in-a-monorepo)
  * 2.[Using Relative Imports](https://nx.dev/blog/managing-ts-packages-in-monorepos#using-relative-imports)
  * ·[Observations: Relative Imports](https://nx.dev/blog/managing-ts-packages-in-monorepos#observations-relative-imports)
  * 3.[Fixing Relative Imports with TypeScript Path Aliases](https://nx.dev/blog/managing-ts-packages-in-monorepos#fixing-relative-imports-with-typescript-path-aliases)
  * ·[Observations: TypeScript Path Aliases](https://nx.dev/blog/managing-ts-packages-in-monorepos#observations-typescript-path-aliases)
  * 4.[Improving Performance with Project References](https://nx.dev/blog/managing-ts-packages-in-monorepos#improving-performance-with-project-references)
  * ·[Observations: Project References](https://nx.dev/blog/managing-ts-packages-in-monorepos#observations-project-references)
  * 5.[Combining TypeScript Project References and Package Manager Workspaces](https://nx.dev/blog/managing-ts-packages-in-monorepos#combining-typescript-project-references-and-package-manager-workspaces)
  * ·[Do I need to reference dependent packages in the consuming package's package.json?](https://nx.dev/blog/managing-ts-packages-in-monorepos#do-i-need-to-reference-dependent-packages-in-the-consuming-packages-packagejson)
  * ·[Observations: Workspaces and Project References](https://nx.dev/blog/managing-ts-packages-in-monorepos#observations-workspaces-and-project-references)
  * 6.[Using TypeScript Project References, Workspaces and Pre-building Packages](https://nx.dev/blog/managing-ts-packages-in-monorepos#using-typescript-project-references-workspaces-and-pre-building-packages)
  * ·[Observations: Pre-building Packages](https://nx.dev/blog/managing-ts-packages-in-monorepos#observations-pre-building-packages)
  * 7.[Which One Should I Choose?](https://nx.dev/blog/managing-ts-packages-in-monorepos#which-one-should-i-choose)
  * 8.[Are There Any Downsides to TypeScript Project References?](https://nx.dev/blog/managing-ts-packages-in-monorepos#are-there-any-downsides-to-typescript-project-references)
  * 9.[Wrapping Up](https://nx.dev/blog/managing-ts-packages-in-monorepos#wrapping-up)
  * 10.[Learn More](https://nx.dev/blog/managing-ts-packages-in-monorepos#learn-more)


## What Does it Mean to Manage and Share TypeScript Code in a Monorepo?
When you work in a monorepo, the goal is to split logic into separate packages. Why? To create smaller, self-contained, and maintainable units. This approach not only enhances reusability but also helps scale: whether that's scaling teams or optimizing CI pipelines.
As you split logic into packages, you'll inevitably need to somehow connect them together. At the **code level** , this is typically expressed through an import statement on the consumer side—whether that's an application using a package or one package depending on another.

```
import { something } from '@tsmono/mypackage';
```

To have this work we need to be able to resolve the `@tsmono/mypackage` import to the actual file path. This needs to happen during:
  * **Build:** This includes type checking and compilation/transpilation.
  * **Runtime:** This is when the application runs in the browser/on the server.


In this article we'll mostly **focus on the building part, in particular type checking**. In real world applications you'll most often have some sort of bundler in the pipeline where `tsc` is used for type checking and the actual compilation part is being taken care of by the bundler (e.g. esbuild, Rspack, or Vite).
There are several approaches to connect TypeScript packages in a monorepo, each with its own trade-offs. Let's explore them in detail.
## Using Relative Imports
Example: [Stackblitz](https://stackblitz.com/github/juristr/ts-monorepo-linking/tree/relative-imports) - [Github](https://github.com/juristr/ts-monorepo-linking/tree/relative-imports)
The simplest approach to connecting packages is using relative imports. Here's an example of the setup:

```
└─ .
   ├─ apps
   │  └─ myapp
   │     ├─ src
   │     │  └─ index.ts
   │     └─ tsconfig.json
   ├─ packages
   │  └─ lib-a
   │     ├─ src
   │     │  └─ index.ts
   │     └─ tsconfig.json
   └─ tsconfig.base.json

```

Here's the content of the main TypeScript configuration files:
tsconfig.base.json
Starting at the root, the `tsconfig.base.json` looks as follows. It is meant to set some of the base compilation properties which can then be adjusted further by individual projects in your workspace.

```
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "strict": true,
    "moduleResolution": "NodeNext",
    "baseUrl": ".",
    "rootDir": "."
  }
}
```

apps/myapp/tsconfig.json
The application extends from the `tsconfig.base.json` and adds some minor adjustments which are relatively uninteresting for our setup:

```
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "../../dist",
    "declaration": true
  },
  "include": ["src/**/*"]
}
```

packages/lib-a/tsconfig.json
Similarly this is the config for our `lib-a` package. The library package has its own TypeScript configuration:

```
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "../../dist",
    "declaration": true
  },
  "include": ["src/**/*"]
}
```

With this setup, the main application can consume the library **using a relative import** :

```
import { greet } from '../../../packages/lib-a/src/index';

console.log(greet('World'));
```

We can have some scripts in our main `package.json` at the workspace root to run our TypeScript code directly, compile it to JavaScript and for performing type checking.

```
{
  "name": "ts-monorepo-linking",
  "private": true,
  "devDependencies": {
    "typescript": "^5.3.3",
    "tsx": "^4.1.0"
  },
  "scripts": {
    "dev": "tsx apps/myapp/src/index.ts",
    "build": "tsc -p apps/myapp/tsconfig.json",
    "typecheck": "tsc -p apps/myapp/tsconfig.json --noEmit"
  }
}
```

### Observations: Relative Imports
**Dependency resolution:**  
Relative imports are the simplest way to link packages, but they are fragile. Restructuring your codebase will require updating import paths, which can become unmanageable in larger workspaces.
**Modularity:**  
This setup enables modularization at the organizational level. Apps and libraries are placed in separate folders, making the workspace easier to navigate. However, from TypeScript's perspective, the entire workspace is treated as a single, unified project. This means there are no strict boundaries between packages at the type-checking level.
**Performance:**  
Treating the entire workspace as a single TypeScript project generally works for small setups but can become problematic as the workspace grows. Type checking and compilation span the entire repo, which may lead to higher memory usage, slower builds, and sluggish editor responsiveness in larger workspaces.
## Fixing Relative Imports with TypeScript Path Aliases
Example: [Stackblitz](https://stackblitz.com/github/juristr/ts-monorepo-linking/tree/ts-path-aliases) - [Github](https://github.com/juristr/ts-monorepo-linking/tree/ts-path-aliases)
Relative imports are functional but difficult to maintain in larger workspaces. A simple improvement is to use **TypeScript path aliases**. These allow you to create custom paths for imports, making the codebase easier to navigate and refactor.
In the `tsconfig.base.json` you can define a path alias for the `lib-a` package:

```
{
  "compilerOptions": {
    ...
    "paths": {
      "@ts-monorepo-linking/lib-a": ["packages/lib-a/src/index.ts"]
    }
  }
}
```

> Note you can use whatever name you want for the alias. Choosing `@ts-monorepo-linking/lib-a` makes it look like an actual import of an external package, thus closer to a structure we want to achieve.
With this setup, you can simplify the import in your application:

```
import { greet } from '@ts-monorepo-linking/lib-a';

console.log(greet('World'));
```

### Observations: TypeScript Path Aliases
**Dependency resolution:**  
Path aliases eliminate the need for relative imports, resulting in a cleaner and more maintainable structure. If the underlying paths change, you only need to update the alias in `tsconfig.base.json`.
> As a side note: While this article focuses on the build and type-checking phase, it's worth noting that running the transpiled TypeScript code directly wouldn't work out of the box. This is because TypeScript path aliases are purely a compile-time construct—they don't exist in the output JavaScript. To run the application, you'd need a runtime plugin or bundler (like Webpack, esbuild, or Vite) that can resolve these aliases to actual file paths.
**Modularity:**  
This approach doesn't change the modularity from the relative imports setup. TypeScript still treats the entire workspace as one large project, without enforcing strict boundaries between packages.
**Performance:**  
Path aliases don't improve performance compared to relative imports. The entire workspace is still treated as a single TypeScript project, so type checking and compilation remain unchanged. This approach focuses on maintainability and readability rather than optimizing performance.
## Improving Performance with Project References
Example: [Stackblitz](https://stackblitz.com/github/juristr/ts-monorepo-linking/tree/ts-proj-references-simple) - [Github](https://github.com/juristr/ts-monorepo-linking/tree/ts-proj-references-simple)
TypeScript project references let you break a large TypeScript project into smaller, manageable units. This approach aligns with monorepo structures, allowing each package to act as its own TypeScript program while maintaining relationships between them.
To use project references:
  * Add the `references` property in `tsconfig.json` files to point to dependent projects.
  * Enable `composite: true` in `compilerOptions` (this also enables `incremental` and `declaration` by default).
  * Use `tsc --build` (`tsc -b`) for compilation and type checking.


> For a more deep-dive on TypeScript project references, make sure to check out our article on ["Everything You Need to Know About TypeScript Project References"](https://nx.dev/blog/typescript-project-references).
Our workspace structure still remains the same with the exception of adding another root-level `tsconfig.json`:

```
ts-monorepo-linking
   ├─ apps
   │  └─ myapp
   │     ├─ src
   │     │  └─ index.ts
   │     └─ tsconfig.json
   ├─ packages
   │  └─ lib-a
   │     ├─ src
   │     │  └─ index.ts
   │     └─ tsconfig.json
   ├─ tsconfig.base.json
   └─ tsconfig.json
```

This new `tsconfig.json` is the entry point for TypeScript project references, pointing to all individual TypeScript configs of the projects that are part of the monorepo workspace.

```
{
  "files": [],
  "references": [{ "path": "./packages/lib-a" }, { "path": "./apps/myapp" }]
}
```

This is distinct from `tsconfig.base.json`, which is used to share common configurations across the workspace:

```
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "strict": true,
    "moduleResolution": "NodeNext",
    "composite": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "paths": {
      "@ts-monorepo-linking/lib-a": ["packages/lib-a/src/index.ts"]
    }
  }
}
```

Note that in the `tsconfig.base.json` we removed the `rootDir` from our TypeScript configuration (compared to the pure TypeScript path aliases setup). The reason is that we no longer treat the entire workspace as a single TypeScript project. Instead, each project's `tsconfig.json` forms its own TypeScript root and will be processed by TypeScript's project references individually.
The `myapp` and `lib-a` configurations look as follows:
apps/myapp/tsconfig.json

```
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "../../dist/apps/myapp",
    "rootDir": "src",
    "tsBuildInfoFile": "../../dist/apps/myapp/tsconfig.tsbuildinfo"
  },
  "references": [{ "path": "../../packages/lib-a" }],
  "include": ["src/**/*"]
}
```

lib-a TSConfig

```
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "../../dist/packages/lib-a",
    "rootDir": "src",
    "tsBuildInfoFile": "../../dist/packages/lib-a/tsconfig.tsbuildinfo"
  },
  "include": ["src/**/*"]
}
```

Changing the configuration alone isn't enough. If you continue using `tsc` (or `tsc -p`), TypeScript will ignore your project references and treat the workspace as a single large project. To fully leverage project references, you must switch to using the `--build` (`-b`) flag with `tsc`. This mode enables TypeScript to process each project individually, respecting dependencies defined in the references property.

```
{
  "name": "ts-monorepo-linking",
  ...
  "scripts": {
    "dev": "tsx --tsconfig tsconfig.base.json apps/myapp/src/index.ts",
    "build": "tsc --build",
    "clean": "tsc --build --clean",
    "typecheck": "tsc --build --emitDeclarationOnly"
  }
}
```

> Note: `--noEmit` is not compatible with the `--build` flag. Use `--emitDeclarationOnly`.
### Observations: Project References
**Dependency resolution:**  
Imports remain the same, relying on TypeScript path aliases to resolve dependencies. Project references don't change how TypeScript resolves paths; they focus on modularizing type checking and compilation.
**Modularity:**  
Project references create stronger boundaries by treating each package as an independent TypeScript program. This enforces better isolation and ensures dependencies are type-checked at the package level.
**Performance:**  
This approach introduces incremental builds, where only modified packages are recompiled. TypeScript generates `.tsbuildinfo` files to track changes, reducing memory usage and speeding up type checking and compilation. This is particularly beneficial for large workspaces or CI pipelines.
From a TypeScript program structure we now don't have a single TypeScript program, but multiple ones.

```
ts-monorepo-linking
   ├─ apps
   │  └─ myapp
   │     ├─ src
   │     └─ tsconfig.json  <<< myapp TS program
   ├─ packages
   │  └─ lib-a
   │     ├─ src
   │     └─ tsconfig.json  <<< lib-a TS program
   ├─ tsconfig.base.json
   └─ tsconfig.json        <<< root-level solution tsconfig
```

The incremental nature of project references allows TypeScript to track changes and skip unnecessary recompilation, resulting in:
  * **Faster builds:** Only projects affected by changes are recompiled, saving time during development and on CI.
  * **Lower memory usage:** Processing smaller, isolated projects is more memory efficient, which is particularly helpful in large workspaces or resource-constrained environments like CI pipelines.
  * **Improved editor performance:** TypeScript's incremental setup ensures quicker type-checking and autocomplete, even in large monorepos.


## Combining TypeScript Project References and Package Manager Workspaces
Example: [Stackblitz](https://stackblitz.com/github/juristr/ts-monorepo-linking/tree/workspaces-ts-proj-refs) - [Github](https://github.com/juristr/ts-monorepo-linking/tree/workspaces-ts-proj-refs)
Modern package managers like NPM, PNPM, Yarn, and Bun have a so-called "workspaces feature" that allows for a more seamless resolution of local packages that allows for a more seamless resolution of local packages.
NPM/Yarn/Bun Workspaces
For most package managers, you can use the `workspaces` property in the root `package.json` to define the packages that are part of the monorepo.

```
{
  "name": "ts-monorepo-linking",
  ...
  "workspaces": [
    "apps/*",
    "packages/*"
  ]
}

```

PNPM Workspaces
PNPM uses a `pnpm-workspace.yaml` file to define the packages that are part of the monorepo.

```
packages:
  - 'apps/*'
  - 'packages/*'
```

This approach **eliminates the need for TypeScript path aliases for module resolution**.

```
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "strict": true,
    "moduleResolution": "NodeNext",
    "composite": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
  }
}
```

Instead, the package manager's workspaces feature makes sure to link the packages properly such that they can be resolved correctly at build and runtime. This doesn't have any impact on our TypeScript project references setup which cares about type checking and resolves dependencies via the `references` property.
> Note, setting up package resolution with workspaces is the generally recommended approach. More on that later.
In an NPM/Yarn/PNPM workspace packages tend to be more self-contained. As such it is common to have the output directly in a `dist` folder within the package itself. We also adjust the `baseUrl` to be at the package root.
apps/myapp/tsconfig.json

```
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist",
    "rootDir": "src",
    "baseUrl": ".",
    "tsBuildInfoFile": "dist/tsconfig.tsbuildinfo"
  },
  "references": [{ "path": "../../packages/lib-a" }],
  "include": ["src/**/*"]
}
```

packages/lib-a/tsconfig.json

```
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "baseUrl": ".",
    "rootDir": "src",
    "outDir": "dist",
    "tsBuildInfoFile": "dist/tsconfig.tsbuildinfo"
  },
  "include": ["src/**/*"]
}
```

Each package requires to have a `package.json` that defines the contract for its entry points, types, and dependencies on other packages.
Here's our updated `package.json` for `lib-a`:

```
{
  "name": "@ts-monorepo-linking/lib-a",
  ...
  "type": "module",
  "exports": {
    ".": {
      "types": "./src/index.ts",
      "import": "./src/index.ts",
      "default": "./src/index.ts"
    },
    "./package.json": "./package.json"
  },
  "main": "./src/index.ts",
  "types": "./src/index.ts",
  "module": "./src/index.ts"
}
```

Note how it directly exports the `index.ts` file, eliminating the need for pre-compilation. This approach works regardless of whether you use TypeScript project references, as long as the consuming application handles compilation or transpilation. The package manager's workspaces feature makes sure that the packages are properly linked so they can be resolved at runtime (by Node or respective bundler).
### Do I need to reference dependent packages in the consuming package's `package.json`?
For NPM workspaces you don't necessarily have to reference dependent packages in the consuming package's `package.json`. Like in our example, `myapp` has a dependency on `lib-a`, so **we could list it in the`dependencies` section, but we don't have to**:

```
{
  "name": "@ts-monorepo-linking/myapp",
  ...
  "dependencies": {
    "@ts-monorepo-linking/lib-a": "*" // optional for NPM workspaces
  }
}
```

> The `*` version specifier tells the package manager to resolve the dependency locally if available.
There's an exception to this:
  * **publishable packages** : Clearly, if you want to [publish a package](https://nx.dev/docs/features/manage-releases), it needs to have all its dependencies listed properly in the `package.json`.
  * **PNPM workspaces** : Due to how PNPM links packages, you need to reference the dependent packages in the consuming package's `package.json`. To avoid having to manually maintain such dependency in every consumer `package.json` you could resort to declaring such dependencies in the root `package.json` instead.


Also note that [PNPM](https://pnpm.io/workspaces), [Yarn v2+](https://yarnpkg.com/features/workspaces) and [Bun](https://bun.sh/docs/install/workspaces) support a dedicated "Workspaces Protocol" allowing you to prefix local dependencies with `workspace:`. This makes it more evident that the dependency is resolved locally. For example:

```
{
  "name": "@ts-monorepo-linking/myapp",
  ...
  "dependencies": {
    "@ts-monorepo-linking/lib-a": "workspace:*"
  }
}
```

### Observations: Workspaces and Project References
**Dependency resolution:**  
With workspaces we delegate the package resolution to the package manager, making it independent of TypeScript. Unlike the previous solution with TypeScript path aliases, this approach works seamlessly at runtime since the package resolution is handled natively by Node.js or the package manager. This makes the setup more robust and platform-aligned.
**Modularity:**  
Each package's `package.json` defines its public API and dependencies, making the structure explicit and easy to understand. One important detail is that in our example the `package.json` directly exports TypeScript files, making the consumer responsible for transpilation and bundling. As a result, these libraries are primarily intended for local use within the monorepo workspace.
**Performance:**  
Compared to previous solutions, performance remains largely the same in this setup. The TypeScript project references still handle incremental type checking and compilation, which guarantees performance improvements. Package resolution is handled by the package manager's workspaces feature and Node itself, so it doesn't impact TypeScript's performance.
## Using TypeScript Project References, Workspaces and Pre-building Packages
Example: [Stackblitz](https://stackblitz.com/github/juristr/ts-monorepo-linking/tree/workspaces-ts-proj-refs-precompiled) - [Github](https://github.com/juristr/ts-monorepo-linking/tree/workspaces-ts-proj-refs-precompiled)
In the previous setup, the `lib-a` package directly exported TypeScript files through its `package.json`:

```
{
  "name": "@ts-monorepo-linking/lib-a",
  ...
  "type": "module",
  "exports": {
    ".": {
      "types": "./src/index.ts",
      "import": "./src/index.ts",
      "default": "./src/index.ts"
    },
    "./package.json": "./package.json"
  },
  "main": "./src/index.ts",
  "types": "./src/index.ts"
}
```

This configuration works well for local monorepo use cases but delegates the responsibility of bundling to the consumer. To avoid that, you can pre-compile the package. You'll need to:
  * Adjust our `lib-a`'s `package.json` to point to the compiled artifacts in `dist`.
  * Setting up a pre-compilation step.
  * Ensure all projects are compiled in the correct order based on their dependencies.


In our simple setup, the TypeScript project references already establish a dependency graph. Running `tsc --build` from the root of the workspace ensures that projects are compiled in the correct order based on their dependencies.
> In a more complex setup you might need to rely on additional tooling such as Nx that has [a task pipelines functionality](https://nx.dev/docs/concepts/task-pipeline-configuration) built-in.
The resulting structure of the `dist` folder looks like this: (notice the `*.js` and `*.d.ts` files)

```
ts-monorepo-linking
   ├─ apps
   │  └─ myapp
   │     ├─ ...
   │     ├─ package.json
   │     └─ tsconfig.json
   ├─ package.json
   ├─ packages
   │  └─ lib-a
   │     ├─ dist
   │     │  ├─ index.d.ts
   │     │  ├─ index.d.ts.map
   │     │  ├─ index.js
   │     │  ├─ index.js.map
   │     │  └─ tsconfig.tsbuildinfo
   │     ├─ package.json
   │     ├─ src
   │     │  └─ index.ts
   │     └─ tsconfig.json
   ├─ tsconfig.base.json
   └─ tsconfig.json
```

To make the compiled `lib-a` usable for other packages, we need to update its `package.json` to point to the compiled artifacts in `dist`. Here's the updated version:

```
{
  "name": "@ts-monorepo-linking/lib-a",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    },
    "./package.json": "./package.json"
  },
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "module": "./dist/index.js"
}
```

### Observations: Pre-building Packages
**Dependency resolution:**  
Precompiling dependent packages allows the application bundler to rely on prebuilt outputs, avoiding the need to compile package dependencies during application bundling. A [task pipeline](https://nx.dev/docs/concepts/task-pipeline-configuration) ensures that packages are compiled beforehand, streamlining the workflow.
**Modularity:**  
Compared to the previous approach of directly referencing TypeScript source files, this setup slightly increases modularity. Each package is now self-contained, with its compiled outputs and defined entry points in the `package.json`. By precompiling and packaging the library, it can be distributed outside the monorepo if needed, which enhances its modularity and reusability. However, the primary focus remains internal use within the monorepo.
**Performance:**  
This setup can slightly improve type-checking performance, especially within code editors. Since the type information is already generated as `.d.ts` files during precompilation, the editor can directly rely on these instead of processing TypeScript source files through project references. While cached project references can achieve similar speeds, precompiled declaration files might potentially reduce some overhead.
## Which One Should I Choose?
Here are some thoughts on which approach to use.
**TypeScript Path Aliases: A Simple Option**
TypeScript path aliases have been a reliable way to manage package resolution, particularly before package managers introduced the workspaces feature. They're straightforward to set up, requiring only a global `tsconfig.json` without additional. However, there are limitations to consider as they require additional bundling support/alias resolvers at runtime and might come with some performance degradation in large workspaces.
Isn't Nx using TS Path Aliases?
Yes and no. Nx has been around since before package managers introduced workspaces. As a result, the default setup in Nx traditionally leveraged a root-level `tsconfig.base.json` containing path aliases to link packages within the monorepo.
That said, Nx can also be used in combination with NPM/Yarn/PNPM/Bun workspaces, as [shown here](https://nx.dev/docs/guides/adopting-nx/adding-to-monorepo). This led to two distinct setups for monorepos with Nx: one using TypeScript path aliases and the other leveraging workspaces. To address the confusion this created, the Nx team has spent the last year enhancing Nx to unify these approaches. The goal is to align with "the platform" by adopting and promoting package manager workspaces, while updating Nx plugins to fully support it, preserving the developer experience (DX) benefits Nx users have come to love.
If you're currently using the TypeScript path aliases approach, there's no need to worry. The Nx team is working on comprehensive documentation and semi-automated tools to help with migration. Additionally, it's possible to migrate manually and even incrementally, allowing you to adopt the workspaces at your own pace.
**Workspaces: The Recommended Approach**
With widespread support in modern package managers (NPM, PNPM, Yarn, Bun), the workspaces feature has become the preferred method for managing package resolution. It aligns closely with the Node.js platform, leveraging native package resolution mechanisms that also work at runtime. This eliminates the portability issues inherent to TypeScript path aliases.
When combined with **TypeScript project references** , this method becomes even more powerful. Workspaces handles package linking such that Node can resolve them properly, while TypeScript project references optimize type-checking and enable incremental builds (for TypeScript). Together, they improve performance, reduce memory usage, and simplify dependency management in larger workspaces. This combination is the recommended way to structure and manage TypeScript packages in a monorepo.
**To Prebuild or Not to Prebuild?**
Prebuilding packages isn't always necessary. Modern bundlers like Vite and Rspack are optimized for speed, often making in-place compilation sufficient. Some things to consider:
  * **Cost of Prebuilding:** Precompiling packages introduces a small overhead, as each package must be built individually. Tools like Nx mitigate this cost with [computation caching](https://nx.dev/docs/features/cache-task-results), allowing you to skip redundant builds. If cache results are available, builds can be significantly faster.
  * **Selective Prebuilding:** Prebuilding doesn't have to be applied universally. You can start without prebuilding and add it for specific subsets of your projects, such as the leaf nodes in your monorepo's project graph.
  * **External Publishing:** Prebuilding is essential if your packages need to be published outside the monorepo with tools like [Nx release](https://nx.dev/docs/features/manage-releases).


## Are There Any Downsides to TypeScript Project References?
While TypeScript project references offer significant benefits, they can be maintenance-heavy, especially in large workspaces where their incremental type-checking capabilities are most valuable. The challenge lies in keeping the references array in each `tsconfig.json` file up to date, ensuring all project dependencies are correctly linked.
This is where Nx comes in, eliminating much of the manual effort involved in maintaining TypeScript project references:
  * **Automated Setup with Generators:** Nx provides generators for scaffolding applications and library packages. These generators handle the `tsconfig.json` setup automatically, ensuring that TypeScript project references are correctly configured from the start.
  * **Automatic Synchronization:** Nx includes a [sync command](https://nx.dev/docs/concepts/sync-generators) that is automatically triggered before critical operations like building or serving a project. This command verifies whether the TypeScript project references are in sync across the workspace. If discrepancies are found, Nx automatically updates the references arrays, keeping your configuration consistent and accurate without manual intervention.


## Wrapping Up
We've explored various strategies for configuring TypeScript-based packages in a monorepo, starting with relative imports, moving to TS path aliases, and finally leveraging the workspaces in combination with TypeScript project references.
If you want to try these approaches, check out the companion GitHub repository at <https://github.com/juristr/ts-monorepo-linking>, or create a new workspace with Nx:

```
npx create-nx-workspace mymonorepo --workspaces
```

> Note `--workspaces` is a temporary flag to instruct Nx to generate a workspaces based monorepo setup.
Also check out our docs:
  * [TypeScript Project Linking](https://nx.dev/docs/concepts/typescript-project-linking)
  * [Switching to Workspaces and Project References](https://nx.dev/docs/technologies/typescript/guides/switch-to-workspaces-project-references)


* * *
## Learn More
  * 🧠 [Nx Docs](https://nx.dev/docs/getting-started/intro)
  * 👩‍💻 [Nx GitHub](https://github.com/nrwl/nx)
  * 💬 [Nx Official Discord Server](https://go.nx.dev/community)
  * 📹 [Nx Youtube Channel](https://www.youtube.com/@nxdevtools)


[![Nx 22.7 Is Here: Task Sandboxing, 7x Less Memory, and Worktree-Aware Caching](https://nx.dev/blog/images/2026-04-22/header.avif) ![Juri Strumpflohner](https://nx.dev/blog/images/Juri%20Strumpfloner.webp) Nx 22.7 Is Here: Task Sandboxing, 7x Less Memory, and Worktree-Aware Caching ](https://nx.dev/blog/nx-22-7-release)[![How SiriusXM Stays Competitive by Iterating and Getting to Market Fast](https://nx.dev/blog/images/2026-03-06/header.avif) ![Philip Fulcher](https://nx.dev/blog/images/Philip%20Fulcher.webp) How SiriusXM Stays Competitive by Iterating and Getting to Market Fast ](https://nx.dev/blog/siriusxm-success-story)
[![End to End Autonomous AI Agent Workflows with Nx](https://nx.dev/blog/images/articles/local-to-ci-autonomous-agents.avif) ![Juri Strumpflohner](https://nx.dev/blog/images/Juri%20Strumpfloner.webp) End to End Autonomous AI Agent Workflows with Nx ](https://nx.dev/blog/autonomous-ai-workflows-with-nx)[ ![Josh VanAllen](https://nx.dev/blog/images/Josh%20VanAllen.webp) Shift Left Isn't Working: Because We're Shifting the Wrong Thing ](https://nx.dev/blog/shift-left-isnt-working)[![Making It Easier to Import Projects Into Your Monorepo](https://nx.dev/blog/images/articles/agentic-nx-import-hero.avif) ![Juri Strumpflohner](https://nx.dev/blog/images/Juri%20Strumpfloner.webp) Making It Easier to Import Projects Into Your Monorepo ](https://nx.dev/blog/agentic-nx-import)
[](https://nx.dev)
Smart Monorepos · Fast Builds
[](https://go.nx.dev/community)[](https://github.com/nrwl/nx)[](https://x.com/NxDevTools)[](https://bsky.app/profile/nx.dev)[](https://www.youtube.com/@NxDevtools)[](https://www.linkedin.com/company/nxdevtools)[](https://go.nrwl.io/nx-newsletter)
### Quick Links
  * [Nx Cloud](https://nx.dev/nx-cloud)
  * [Pricing](https://nx.dev/nx-cloud#plans)
  * [Docs](https://nx.dev/docs/getting-started/intro)
  * [Blog](https://nx.dev/blog)


### Solutions
  * [Developers](https://nx.dev/solutions/engineering)
  * [Platform & Devops](https://nx.dev/solutions/platform)
  * [Eng. Managers](https://nx.dev/solutions/management)
  * [CTOs & VPs Eng.](https://nx.dev/solutions/leadership)
  * [Security](https://nx.dev/enterprise/security)


### Products
  * [Nx](https://nx.dev)
  * [Nx Cloud](https://nx.dev/nx-cloud)
  * [Nx Enterprise](https://nx.dev/enterprise)
  * [Nx Labs](https://nx.dev/contact/labs)
  * [Status](https://status.nx.app)


### Resources
  * [Tutorials](https://nx.dev/docs/getting-started/tutorials)
  * [Webinars](https://nx.dev/webinars)
  * [Customers](https://nx.dev/customers)
  * [Community](https://nx.dev/community)
  * [Customer Stories](https://nx.dev/customer-stories)


### Company
  * [About us](https://nx.dev/company)
  * [Careers](https://nx.dev/careers)
  * [Brand & Guidelines](https://nx.dev/brands)
  * [Contact Us](https://nx.dev/contact)


Copyright © 2026 – All Right Reserved
[Privacy Policy](https://cloud.nx.app/privacy)[Terms & Conditions](https://cloud.nx.app/terms)
Close
### Autonomous Software Factories: Are We There Yet?
Join Juri Strumpflohner on May 13th. Learn what it takes to build an autonomous software factory — and where the rough edges still are.
[Register here](https://go.nx.dev/autonomous-software-factories-are-we-there-yet?utm_campaign=32000851-2026%20Webinars&utm_source=website&utm_medium=banner "Register here")


## Source: https://maxrohde.com/2021/11/20/the-ultimate-guide-to-typescript-monorepos/

#  Bad gateway Error code 502
Visit [cloudflare.com](https://www.cloudflare.com/5xx-error-landing?utm_source=errorcode_502&utm_campaign=maxrohde.com) for more information. 
2026-05-10 22:27:28 UTC
You
###  Browser 
Working
[ ](https://www.cloudflare.com/5xx-error-landing?utm_source=errorcode_502&utm_campaign=maxrohde.com)
London
###  [ Cloudflare ](https://www.cloudflare.com/5xx-error-landing?utm_source=errorcode_502&utm_campaign=maxrohde.com)
Working
maxrohde.com
###  Host 
Error
## What happened?
The web server reported a bad gateway error.
## What can I do?
Please try again in a few minutes.
Cloudflare Ray ID: **9f9c5f14f95cf4a0** • Your IP: Click to reveal 109.175.226.162 • Performance & security by [Cloudflare](https://www.cloudflare.com/5xx-error-landing?utm_source=errorcode_502&utm_campaign=maxrohde.com)


## Source: http://nodesource.com/blog/scalable-api-with-node.js-and-typescript/

[](https://nodesource.com/)
  * Products 
    * [N|Solid](https://nodesource.com/products/nsolid)
    * [N|Solid Copilot](https://nodesource.com/products/copilot)
    * [N|Solid Runtime](https://nodesource.com/products/runtime)
    * [Node.js Extended Support](https://nodesource.com/products/support)
    * [Node.js Distributions](https://nodesource.com/products/distributions)
    * [Node.js LTS Upgrade](https://nodesource.com/products/nodejs-upgrade)
  * [Services ](https://nodesource.com/services)
    * [Node.js Support](https://nodesource.com/services/support)
    * [Consulting](https://nodesource.com/services/consulting)
    * [Training](https://nodesource.com/services/training)
  * Solutions 
    * [API Integration / Microservices](https://nodesource.com/solutions/api-integration-microservices)
    * [High Performance Applications](https://nodesource.com/solutions/high-performance-applications)
    * [Legacy Application Migration](https://nodesource.com/solutions/legacy-application-migration)
    * [Internet of Things](https://nodesource.com/solutions/iot)
  * Resources 
    * [Blog](https://nodesource.com/blog)
    * [N|Solid Docs](https://docs.nodesource.com)
    * [Knowledge Center](https://nodesource.com/resources)
    * [Partner Program](https://nodesource.com/pages/approved-partner-program.html)
    * [Infrastructure Cost](https://nodesource.com/infrastructure-cost)
  * Company 
    * [Contact Us](https://pages.nodesource.com/contact-us.html)
    * [About](https://nodesource.com/about)
    * [Press](https://nodesource.com/press)


BOOK A DEMO
[SIGN IN/SIGN UP](https://accounts.nodesource.com/sign-in)[CONTACT US](https://nodesource.com/pages/contact-us.html)
  * Products 
    * [N|Solid](https://nodesource.com/products/nsolid)
    * [N|Solid Copilot](https://nodesource.com/products/copilot)
    * [N|Solid Runtime](https://nodesource.com/products/runtime)
    * [Node.js Extended Support](https://nodesource.com/products/support)
    * [Node.js LTS Upgrade](https://nodesource.com/products/nodejs-upgrade)
  * [Services ](https://nodesource.com/services)
    * [Node.js Support](https://nodesource.com/services/support)
    * [Consulting](https://nodesource.com/services/consulting)
    * [Training](https://nodesource.com/services/training)
  * Solutions 
    * [API Integration / Microservices](https://nodesource.com/solutions/api-integration-microservices)
    * [High Performance Applications](https://nodesource.com/solutions/high-performance-applications)
    * [Legacy Application Migration](https://nodesource.com/solutions/legacy-application-migration)
    * [Internet of Things](https://nodesource.com/solutions/iot)
  * Resources 
    * [Blog](https://nodesource.com/blog)
    * [N|Solid Docs](https://docs.nodesource.com)
    * [Knowledge Center](https://nodesource.com/resources)
    * [Partner Program](https://nodesource.com/pages/approved-partner-program.html)
    * [Infrastructure Cost](https://nodesource.com/infrastructure-cost)
  * Company 
    * [Contact Us](https://pages.nodesource.com/contact-us.html)
    * [About](https://nodesource.com/about)
    * [Press](https://nodesource.com/press)


BOOK A DEMO
[SIGN IN/SIGN UP](https://accounts.nodesource.com/sign-in)
[](http://github.com/nodesource)[](http://twitter.com/nodesource)[](https://www.youtube.com/@NodeSourceHQ)[](https://www.linkedin.com/company/nodesource)
[](https://nodesource.com/blog/scalable-api-with-node.js-and-typescript)[](https://nodesource.com/)
# [The NodeSource Blog](https://nodesource.com/blog)
[](https://nodesource.com/blog/rss)
[Previous PostIntroducing NCM v3: AI-Enhanced Security & Performance for Node.js](https://nodesource.com/blog/introudcing-ncmv3-ai-security-and-performance-for-nodejs)
[Next PostHow to Get Security Patches for Legacy Unsupported Node.js Versions](https://nodesource.com/blog/security-patches-for-legacy-unsupported-Node.js-versions)
# [All Posts](https://nodesource.com/blog)
## [Node.js](https://nodesource.com/blog/category/node-js-1)
### Building Scalable APIs with Node.js and TypeScript
by:
![Lizz Parody](https://assets.nodesource.com/strapi-uploads/avatar-liz-parody_801de3cda8.jpg)[Lizz Parody](https://nodesource.com/blog/author/liz-parody)
in [Node.js](https://nodesource.com/blog/category/node-js-1) on Jul 24 2025
Share
[](https://www.twitter.com/intent/tweet?url=https://nodesource.com/blog/scalable-api-with-node.js-and-typescript)[](https://www.linkedin.com/shareArticle?mini=true&url=https://nodesource.com/blog/scalable-api-with-node.js-and-typescript)[](https://www.facebook.com/sharer/sharer.php?u=https://nodesource.com/blog/scalable-api-with-node.js-and-typescript)[](https://plus.google.com/share?url=https://nodesource.com/blog/scalable-api-with-node.js-and-typescript)
If you've ever tried building an API with plain JavaScript and found yourself drowning in bugs, weird errors, or spaghetti code, yo, you're not alone. That’s why so many devs are leveling up their backend game by mixing **Node.js** with **TypeScript**. It's like going from playing Minecraft in creative mode to building actual skyscrapers: more control, better structure, and way less chaos.
In this post, we’re gonna break down how to build **scalable APIs** using Node.js and TypeScript without overcomplicating things. Whether you’re a weekend hacker or just getting into backend development, this guide will show you how to keep your code clean, organized, and ready to grow.
But hold up, before you dive into the building, let’s talk **performance** and **security**. If you're serious about scaling your API and want real-time performance insights, secure observability, and runtime protection without drowning in logs, check out **[N|Solid](https://nodesource.com/products/nsolid)**. It's like having superpowers for your Node.js app, especially when you're heading into production. 💪
Let’s get into it.
## **Why TypeScript with Node.js?**
Adding TypeScript to your Node.js workflow brings significant benefits beyond plain JavaScript, especially as projects grow:
  * **Static Typing:** TypeScript enforces type definitions, catching common bugs like `undefined is not a function` at compile time, leading to more reliable code and fewer runtime errors.
  * **Enhanced Developer Experience:** Features like IntelliSense provide autocomplete and real-time feedback, making coding faster and more intuitive.
  * **Improved Scalability:** Type contracts, clear interfaces, and modular code make large projects easier to manage, onboard new team members, and maintain over time.
  * **Modern Tooling Compatibility:** TypeScript integrates seamlessly with popular tools like ESLint, Prettier, and testing frameworks, streamlining your development environment.


## **Project Setup**
Before we start slinging code, let’s get our dev environment locked and loaded. Setting up a clean, scalable project structure is key when you're trying to avoid future headaches.
### **What You’ll Need**
Here’s the tech stack we’re rolling with:
  * **Node.js** – of course
  * **TypeScript** – static typing goodness
  * **Express.js** – lightweight web framework
  * **ts-node** – to run TypeScript directly


Make sure you’ve got Node.js installed. Then let’s kick things off:
### **Step 1: Initialize the Project**

```
mkdir scalable-api-ts
cd scalable-api-ts
npm init -y

```

### **Step 2: Install Dependencies**

```
npm install express
npm install -D typescript ts-node @types/node @types/express

```

This installs Express, along with TypeScript and all the type defs we’ll need for a smoother experience.
### **Step 3: Create a TypeScript Config**

```
npx tsc --init

```

Now tweak your `tsconfig.json` for a solid dev experience:

```
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "rootDir": "src",
    "outDir": "dist",
    "esModuleInterop": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  }
}

```

### **Step 4: Set Up Folder Structure**
Here’s a basic layout to start with:

```
scalable-api-ts/
├── src/
│   ├── routes/
│   ├── controllers/
│   ├── services/
│   ├── index.ts
├── dist/
├── package.json
├── tsconfig.json

```

This structure separates concerns early—making things way easier to scale and maintain.
### **Step 5: Add Start Scripts**
Update your `package.json` with these scripts:

```
"scripts": {
  "dev": "nodemon src/index.ts",
  "build": "tsc",
  "start": "node dist/index.js"
}

```

Now you can run your app in dev mode with `npm run dev`. Boom, you're set.
## **Creating a Simple API with Express + TypeScript**
Now that we’ve got the project set up, it’s time to build something real. Let’s create a basic Express API that’s fully type-safe and cleanly structured.
### **Step 1: Create the Entry Point**
In `src/index.ts`, start with the barebones server setup:

```
import express, { Application, Request, Response } from 'express';

const app: Application = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req: Request, res: Response) => {
  res.send('API is up and running! 🚀');
});

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

```

### **Step 2: Add Your First Route**
Let’s add a simple route that returns a list of users. Create a file: `src/routes/userRoutes.ts`

```
import { Router } from 'express';
import { getUsers } from '../controllers/userController';

const router = Router();

router.get('/users', getUsers);

export default router;

```

### **Step 3: Build a Type-Safe Controller**
Now, in `src/controllers/userController.ts`:

```
import { Request, Response } from 'express';

interface User {
  id: number;
  name: string;
  email: string;
}

export const getUsers = (req: Request, res: Response) => {
  const users: User[] = [
    { id: 1, name: 'Jane Doe', email: 'jane@example.com' },
    { id: 2, name: 'John Smith', email: 'john@example.com' }
  ];

  res.json(users);
};

```

### **Step 4: Wire Up the Route**
Go back to `src/index.ts` and plug in the user routes:

```
import userRoutes from './routes/userRoutes';
app.use('/api', userRoutes);

```

### **Test It Out**
Run your dev server:

```
npm run dev

```

Then visit: [ http://localhost:3000/api/users   
](http://localhost:3000/api/users) You should see your JSON array of users!
## **Scaling the Architecture**
Okay, we’ve got a basic API running—but what happens when your app grows? More routes, more logic, more chaos. To keep things manageable and scalable, you’ve gotta start thinking in **layers**.
Let’s break it down.
### **Modularize Everything**
Split your code into these core folders:

```
src/
├── routes/        // define routes & route groups
├── controllers/   // handle request logic
├── services/      // business logic layer
├── models/        // data structures or ORM models
├── middlewares/   // custom middleware (auth, error handling, etc)
├── utils/         // helper functions

```

This structure keeps things clean and helps you **follow separation of concerns** , which is just a fancy way of saying “put stuff where it belongs.”
* * *
### **Add a Service Layer**
Let’s move logic out of the controller and into a `userService.ts`:

```
src/services/userService.ts

```

```
interface User {
  id: number;
  name: string;
  email: string;
}

export const getAllUsers = (): User[] => {
  return [
    { id: 1, name: 'Jane Doe', email: 'jane@example.com' },
    { id: 2, name: 'John Smith', email: 'john@example.com' }
  ];
};

```

Now update your controller to use the service:

```
src/controllers/userController.ts

```

```
import { Request, Response } from 'express';
import { getAllUsers } from '../services/userService';

export const getUsers = (req: Request, res: Response) => {
  const users = getAllUsers();
  res.json(users);
};

```

Boom—logic is separated. 🎉
### **Keep It DRY with Reusable Middleware**
Start creating middlewares like `logger.ts`, `auth.ts`, or `errorHandler.ts` in a `middlewares/` folder. These can be used across multiple routes to keep your code DRY (Don't Repeat Yourself).
### **Pro Tips for Scaling:**
  * Use **interfaces or types** for everything—request bodies, responses, database models.
  * Keep routes thin, controllers medium, and services thick. (Like tacos 🌮)
  * Group related files together to keep context tight—e.g. `user.routes.ts`, `user.controller.ts`, `user.service.ts`.


* * *
## **Middleware & Error Handling**
Middlewares in Express are like the bouncers of your app—they run _before_ your route handlers and can do all sorts of useful stuff like logging, validating, authenticating, and error-catching.
Let’s break down how to create clean, reusable middleware and a centralized error handler.
* * *
### **What’s Middleware, Really?**
Think of middleware as a function that has access to:

```
(req, res, next)

```

It does something _before_ the request reaches your controller, and either ends the request or calls `next()` to pass control.
* * *
### **Example: Logger Middleware**
Let’s create a simple request logger.

```
src/middlewares/logger.ts

```

```
import { Request, Response, NextFunction } from 'express';

export const logger = (req: Request, res: Response, next: NextFunction) => {
  console.log(`${req.method} ${req.path}`);
  next();
};

```

Then use it in `index.ts`:

```
import { logger } from './middlewares/logger';

app.use(logger);

```

Now every request logs to the console—nice.
## **Data Persistence Layer**
So far we’ve been using fake data—cool for demos, but now it’s time to get real. Let’s integrate a database and create a clean, type-safe way to handle our data.
* * *
### **Choose Your Database**
You’ve got two solid options:
  * **PostgreSQL** – great for relational data, works with ORMs like Prisma or TypeORM.
  * **MongoDB** – flexible and document-based, great with Mongoose.


For this guide, we’ll roll with **Prisma + PostgreSQL** , but you can totally swap it out based on your vibe.
* * *
### **Step 1: Install Prisma**

```
npm install prisma --save-dev
npx prisma init

```

This creates a `prisma/` folder with a `schema.prisma` file and `.env` for your DB connection.
Update `.env` with your connection string:

```
DATABASE_URL="postgresql://user:password@localhost:5432/yourdb"

```

### **Step 2: Define a Model**
In `prisma/schema.prisma`:
prisma

```
model User {
  id    Int     @id @default(autoincrement())
  name  String
  email String  @unique
}

```

Then run:

```
npx prisma migrate dev --name init

```

Prisma creates your database tables automatically. ✨
* * *
### **Step 3: Use Prisma in Your Project**
Install Prisma Client:

```
npm install @prisma/client

```

Then in `src/services/userService.ts`:

```
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export const getAllUsers = async () => {
  return await prisma.user.findMany();
};

```

And in your controller:

```
export const getUsers = async (req: Request, res: Response) => {
  const users = await getAllUsers();
  res.json(users);
};

```

Now your API is hitting a real database, and Prisma’s types keep everything tight and error-free. 🧠
## **Testing the API**
Alright, you’ve got a clean, scalable API—now let’s make sure it actually works (and keeps working). Testing might sound boring, but it’s your best friend when your app grows or when other devs start collaborating with you.
We’ll use **Jest** (or **Vitest** if you want something faster + modern) for testing, and **Supertest** for making HTTP requests to our Express app.
* * *
### **Step 1: Install Testing Tools**

```
npm install --save-dev jest ts-jest @types/jest supertest @types/supertest
npx ts-jest config:init

```

Update `package.json` with a test script:

```
"scripts": {
  "test": "jest"
}

```

### **Step 2: Basic Test Example**
Create a test file: `tests/user.test.ts`

```
import request from 'supertest';
import app from '../src/app'; // if you separate Express setup from `index.ts`

describe('GET /api/users', () => {
  it('should return a list of users', async () => {
    const res = await request(app).get('/api/users');

    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
});

```

📝 Pro Tip: If your Express setup is tightly coupled to the `listen()` call, move that part to `index.ts` and export your `app` from `app.ts` like so:

```
src/app.ts

```

```
import express from 'express';
import userRoutes from './routes/userRoutes';

const app = express();
app.use(express.json());
app.use('/api', userRoutes);

export default app;

```

Then in `src/index.ts`:

```
import app from './app';
app.listen(3000, () => console.log('Server running'));

```

### **Step 3: Mocking the Database**
You don’t want tests hitting your real database. You can:
  * Use a mock database (e.g., SQLite in-memory for Prisma)
  * Use Jest to mock your service functions


**Example:**

```
jest.mock('../src/services/userService', () => ({
  getAllUsers: jest.fn(() => [
    { id: 1, name: 'Test User', email: 'test@example.com' }
  ])
}));

```

### **Types of Tests to Aim For**
  * **Unit tests** – test individual functions/services.
  * **Integration tests** – test full request-response cycles (routes + middleware).
  * **E2E tests** – simulate actual usage (can come later).


* * *
Testing might feel like extra work now, but trust me—it saves you _so much_ time when things break (and they will 😅).
## **API Versioning & Documentation**
As your API grows and evolves, things will change—endpoints might be renamed, payloads updated, or features removed. But here’s the deal: **you can’t break stuff for existing users.** That’s where **versioning** and **documentation** come in clutch.
* * *
### **API Versioning 101**
Versioning is like keeping the old versions of your mixtape so fans can still vibe, even if your new stuff drops.
#### **🛣 Common Strategies:**
**URI-based** (most popular):
`/api/v1/users`

```
/api/v2/users

```

**Header-based** :
`GET /users`

```
Accept: application/vnd.yourapi.v1+json

```

Stick with URI-based—it’s cleaner and easier to manage.
#### **💡 Setup Example:**

```
app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);

```

You can keep your newer logic in `v2` and still support older apps using `v1`.
* * *
### **API Documentation with Swagger**
If other devs (or future you) are gonna use your API, **Swagger** makes it ridiculously easy to generate docs from your code.
#### **🛠 Step 1: Install Swagger UI**

```
npm install swagger-ui-express swagger-jsdoc

```

#### **📄 Step 2: Create Swagger Config**

```
src/swagger.ts

```

```
import swaggerJSDoc from 'swagger-jsdoc';

export const swaggerSpec = swaggerJSDoc({
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Scalable Node API',
      version: '1.0.0'
    }
  },
  apis: ['./src/routes/*.ts']
});

```

Then in `src/index.ts`:

```
import swaggerUi from 'swagger-ui-express';
import { swaggerSpec } from './swagger';

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

```

Visit: [ http://localhost:3000/api-docs   
](http://localhost:3000/api-docs) Boom—interactive docs. 🧠
* * *
### **Add Comments for Swagger to Parse**
In `routes/userRoutes.ts`:

```
/**
 * @openapi
 * /users:
 *   get:
 *     summary: Get all users
 *     responses:
 *       200:
 *         description: A list of users
 */

```

This lets Swagger auto-generate docs from your code with zero duplication.
* * *
### **TL;DR**
  * Use `/api/v1`, `/api/v2` to manage breaking changes
  * Generate live docs with Swagger for transparency
  * Update docs as part of your dev workflow


## **Deployment & Production Tips**
You’ve built it, tested it, and documented it—now it’s time to ship it. Deploying a Node.js + TypeScript API doesn’t have to be scary. With the right setup, you can go live smoothly and scale without tears.
* * *
### **Environment Variable Management**
Don’t hardcode secrets or config values (like your DB connection string, API keys, etc).
#### **✅ Use `.env` Files + `dotenv`

```
npm install dotenv

```

In `src/index.ts`:

```
import dotenv from 'dotenv';
dotenv.config();

```

Now you can safely use `process.env.PORT`, `process.env.DATABASE_URL`, etc.
* * *
**Build for Production**
Your TypeScript code needs to be compiled before going live.
#### **🔨 Build the App**

```
npm run build

```

This compiles your TS files to JS in the `dist/` folder. Make sure your `start` script runs the compiled code:

```
"start": "node dist/index.js"

```

### **N|Solid for Production-Level Monitoring**
If you’re deploying a mission-critical API, monitoring matters. **N|Solid** gives you pro-level insights like:
  * Real-time performance metrics
  * Security monitoring
  * CPU profiling and memory usage


It’s tailor-made for Node.js apps and way more focused than generic tools. Add it early to catch issues _before_ your users do.
* * *
### **Final Pro Tips for Production**
  * Use a reverse proxy like **Nginx** or **Vercel Edge** for handling HTTPS, routing, etc.
  * Enable request rate-limiting & basic DDoS protection with middleware like `express-rate-limit`.
  * Watch for memory leaks and keep logs centralized (e.g., Logtail, Datadog, etc).


* * *
## **🎉 Final Thoughts**
You just went from zero to production-ready with a **scalable, type-safe Node.js API** —that’s a huge win.
You learned how to:
  * Set up a clean Node + TypeScript project
  * Create modular, maintainable code
  * Add middleware, error handling, and testing
  * Connect to a real database with Prisma
  * Version and document your API like a pro
  * Ship it to the world (and monitor it with tools like N|Solid)


Now you’ve got a real backend stack you can build on—for side projects, freelance gigs, or even your next startup. 💼🔥
#### Featured Articles
  * [Node.js v26 Is Here: What Actually Changed](https://nodesource.com/blog/nodejs-v26-is-here)
In [Node.js](https://nodesource.com/blog/category/node-js) on May 05 2026
  * [DevOps Shifts Left to Developers](https://nodesource.com/blog/devops-shift-left-runtime-intelligence-developer-workflows)
In [Observability](https://nodesource.com/blog/category/observability) on Apr 28 2026
  * [Automatic Sourcemap Retrieval in Production: Debugging Without the Friction](https://nodesource.com/blog/automatic-sourcemap-retrieval-nodejs-production)
In [NodeSource](https://nodesource.com/blog/category/nodesource) on Apr 21 2026


#### Categories
  * [Community](https://nodesource.com/blog/category/community "Community")
  * [Debugging](https://nodesource.com/blog/category/debugging "Debugging")
  * [How To](https://nodesource.com/blog/category/how-to "How To")
  * [Node.js](https://nodesource.com/blog/category/node-js "Node.js")
  * [Node.js](https://nodesource.com/blog/category/node-js-1 "Node.js")
  * [NodeSource](https://nodesource.com/blog/category/nodesource "NodeSource")
  * [Observability](https://nodesource.com/blog/category/observability "Observability")
  * [Product](https://nodesource.com/blog/category/product "Product")
  * [Security](https://nodesource.com/blog/category/security "Security")


The NodeSource platform offers a high-definition view of the performance, security and behavior of Node.js applications and functions.
[Start for Free](https://accounts.nodesource.com/sign-up)
[](https://nodesource.com/)
[](http://github.com/nodesource)[](http://twitter.com/nodesource)[](https://www.youtube.com/@NodeSourceHQ)[](https://www.linkedin.com/company/nodesource)
© 2026 NodeSource
  * What We Do
  * [N|Solid](https://nodesource.com/products/nsolid)
  * [Product Pricing](https://nodesource.com/products/pricing)
  * [NodeSource Services](https://nodesource.com/services)


  * Solutions
  * [Microservices](https://nodesource.com/solutions/api-integration-microservices)
  * [High Traffic](https://nodesource.com/solutions/high-traffic-applications)
  * [Legacy Applications](https://nodesource.com/solutions/legacy-application-migration)
  * [Internet of Things](https://nodesource.com/solutions/iot)


  * Learn
  * [Blog](https://nodesource.com/blog)
  * [Resources](https://nodesource.com/resources)
  * [Support Portal](https://support.nodesource.com)
  * [Documentation](https://docs.nodesource.com)


  * Company
  * [Contact Us](https://pages.nodesource.com/contact-us.html)
  * [About NodeSource](https://nodesource.com/about)
  * [Press](https://nodesource.com/press)
  * [Legal](https://nodesource.com/legal)
  * [Privacy Policy](https://nodesource.com/privacy)




## Source: https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns

[Skip to content](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#geist-skip-nav)
[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns "Go to Vercel homepage")[](https://nextjs.org/ "Go to the homepage")
Search documentation...`CtrlK`Search...`⌘K`
[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns "Go to Vercel homepage")[](https://nextjs.org/ "Go to the homepage")
[Showcase](https://nextjs.org/showcase)[Docs](https://nextjs.org/docs "Documentation")[Blog](https://nextjs.org/blog)[Templates](https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_templates)[Enterprise](https://vercel.com/contact/sales/nextjs?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_enterprise)
Search documentation...`CtrlK`Search...`⌘K`Feedback[Learn](https://nextjs.org/learn)
Menu
App Router 14
Using App Router
Features available in /app
Version 14
14.2.35
  * [Getting Started](https://nextjs.org/docs/14/getting-started)
    * [Installation](https://nextjs.org/docs/14/getting-started/installation)
    * [Project Structure](https://nextjs.org/docs/14/getting-started/project-structure)


  * [Building Your Application](https://nextjs.org/docs/14/app/building-your-application)
    * [Routing](https://nextjs.org/docs/14/app/building-your-application/routing)
      * [Defining Routes](https://nextjs.org/docs/14/app/building-your-application/routing/defining-routes)
      * [Pages and Layouts](https://nextjs.org/docs/14/app/building-your-application/routing/pages-and-layouts)
      * [Linking and Navigating](https://nextjs.org/docs/14/app/building-your-application/routing/linking-and-navigating)
      * [Loading UI and Streaming](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming)
      * [Error Handling](https://nextjs.org/docs/14/app/building-your-application/routing/error-handling)
      * [Redirecting](https://nextjs.org/docs/14/app/building-your-application/routing/redirecting)
      * [Route Groups](https://nextjs.org/docs/14/app/building-your-application/routing/route-groups)
      * [Project Organization](https://nextjs.org/docs/14/app/building-your-application/routing/colocation)
      * [Dynamic Routes](https://nextjs.org/docs/14/app/building-your-application/routing/dynamic-routes)
      * [Parallel Routes](https://nextjs.org/docs/14/app/building-your-application/routing/parallel-routes)
      * [Intercepting Routes](https://nextjs.org/docs/14/app/building-your-application/routing/intercepting-routes)
      * [Route Handlers](https://nextjs.org/docs/14/app/building-your-application/routing/route-handlers)
      * [Middleware](https://nextjs.org/docs/14/app/building-your-application/routing/middleware)
      * [Internationalization](https://nextjs.org/docs/14/app/building-your-application/routing/internationalization)
    * [Data Fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching)
      * [Fetching, Caching, and Revalidating](https://nextjs.org/docs/14/app/building-your-application/data-fetching/fetching-caching-and-revalidating)
      * [Server Actions and Mutations](https://nextjs.org/docs/14/app/building-your-application/data-fetching/server-actions-and-mutations)
      * [Data Fetching Patterns and Best Practices](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns)
    * [Rendering](https://nextjs.org/docs/14/app/building-your-application/rendering)
      * [Server Components](https://nextjs.org/docs/14/app/building-your-application/rendering/server-components)
      * [Client Components](https://nextjs.org/docs/14/app/building-your-application/rendering/client-components)
      * [Composition Patterns](https://nextjs.org/docs/14/app/building-your-application/rendering/composition-patterns)
      * [Edge and Node.js Runtimes](https://nextjs.org/docs/14/app/building-your-application/rendering/edge-and-nodejs-runtimes)
    * [Caching](https://nextjs.org/docs/14/app/building-your-application/caching)
    * [Styling](https://nextjs.org/docs/14/app/building-your-application/styling)
      * [CSS Modules](https://nextjs.org/docs/14/app/building-your-application/styling/css-modules)
      * [Tailwind CSS](https://nextjs.org/docs/14/app/building-your-application/styling/tailwind-css)
      * [CSS-in-JS](https://nextjs.org/docs/14/app/building-your-application/styling/css-in-js)
      * [Sass](https://nextjs.org/docs/14/app/building-your-application/styling/sass)
    * [Optimizing](https://nextjs.org/docs/14/app/building-your-application/optimizing)
      * [Images](https://nextjs.org/docs/14/app/building-your-application/optimizing/images)
      * [Fonts](https://nextjs.org/docs/14/app/building-your-application/optimizing/fonts)
      * [Scripts](https://nextjs.org/docs/14/app/building-your-application/optimizing/scripts)
      * [Metadata](https://nextjs.org/docs/14/app/building-your-application/optimizing/metadata)
      * [Static Assets](https://nextjs.org/docs/14/app/building-your-application/optimizing/static-assets)
      * [Bundle Analyzer](https://nextjs.org/docs/14/app/building-your-application/optimizing/bundle-analyzer)
      * [Lazy Loading](https://nextjs.org/docs/14/app/building-your-application/optimizing/lazy-loading)
      * [Analytics](https://nextjs.org/docs/14/app/building-your-application/optimizing/analytics)
      * [Instrumentation](https://nextjs.org/docs/14/app/building-your-application/optimizing/instrumentation)
      * [OpenTelemetry](https://nextjs.org/docs/14/app/building-your-application/optimizing/open-telemetry)
      * [Third Party Libraries](https://nextjs.org/docs/14/app/building-your-application/optimizing/third-party-libraries)
    * [Configuring](https://nextjs.org/docs/14/app/building-your-application/configuring)
      * [TypeScript](https://nextjs.org/docs/14/app/building-your-application/configuring/typescript)
      * [ESLint](https://nextjs.org/docs/14/app/building-your-application/configuring/eslint)
      * [Environment Variables](https://nextjs.org/docs/14/app/building-your-application/configuring/environment-variables)
      * [Absolute Imports and Module Path Aliases](https://nextjs.org/docs/14/app/building-your-application/configuring/absolute-imports-and-module-aliases)
      * [MDX](https://nextjs.org/docs/14/app/building-your-application/configuring/mdx)
      * [src Directory](https://nextjs.org/docs/14/app/building-your-application/configuring/src-directory)
      * [Draft Mode](https://nextjs.org/docs/14/app/building-your-application/configuring/draft-mode)
      * [Content Security Policy](https://nextjs.org/docs/14/app/building-your-application/configuring/content-security-policy)
    * [Testing](https://nextjs.org/docs/14/app/building-your-application/testing)
      * [Vitest](https://nextjs.org/docs/14/app/building-your-application/testing/vitest)
      * [Jest](https://nextjs.org/docs/14/app/building-your-application/testing/jest)
      * [Playwright](https://nextjs.org/docs/14/app/building-your-application/testing/playwright)
      * [Cypress](https://nextjs.org/docs/14/app/building-your-application/testing/cypress)
    * [Authentication](https://nextjs.org/docs/14/app/building-your-application/authentication)
    * [Deploying](https://nextjs.org/docs/14/app/building-your-application/deploying)
      * [Production Checklist](https://nextjs.org/docs/14/app/building-your-application/deploying/production-checklist)
      * [Static Exports](https://nextjs.org/docs/14/app/building-your-application/deploying/static-exports)
    * [Upgrading](https://nextjs.org/docs/14/app/building-your-application/upgrading)
      * [Codemods](https://nextjs.org/docs/14/app/building-your-application/upgrading/codemods)
      * [App Router Migration](https://nextjs.org/docs/14/app/building-your-application/upgrading/app-router-migration)
      * [Version 14](https://nextjs.org/docs/14/app/building-your-application/upgrading/version-14)
      * [Migrating from Vite](https://nextjs.org/docs/14/app/building-your-application/upgrading/from-vite)


  * [API Reference](https://nextjs.org/docs/14/app/api-reference)
    * [Components](https://nextjs.org/docs/14/app/api-reference/components)
      * [Font](https://nextjs.org/docs/14/app/api-reference/components/font)
      * [<Image>](https://nextjs.org/docs/14/app/api-reference/components/image)
      * [<Link>](https://nextjs.org/docs/14/app/api-reference/components/link)
      * [<Script>](https://nextjs.org/docs/14/app/api-reference/components/script)
    * [File Conventions](https://nextjs.org/docs/14/app/api-reference/file-conventions)
      * [default.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/default)
      * [error.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/error)
      * [layout.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/layout)
      * [loading.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/loading)
      * [not-found.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/not-found)
      * [page.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/page)
      * [route.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/route)
      * [Route Segment Config](https://nextjs.org/docs/14/app/api-reference/file-conventions/route-segment-config)
      * [template.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/template)
      * [Metadata Files](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata)
        * [favicon, icon, and apple-icon](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/app-icons)
        * [manifest.json](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/manifest)
        * [opengraph-image and twitter-image](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/opengraph-image)
        * [robots.txt](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/robots)
        * [sitemap.xml](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/sitemap)
    * [Functions](https://nextjs.org/docs/14/app/api-reference/functions)
      * [cookies](https://nextjs.org/docs/14/app/api-reference/functions/cookies)
      * [draftMode](https://nextjs.org/docs/14/app/api-reference/functions/draft-mode)
      * [fetch](https://nextjs.org/docs/14/app/api-reference/functions/fetch)
      * [generateImageMetadata](https://nextjs.org/docs/14/app/api-reference/functions/generate-image-metadata)
      * [generateMetadata](https://nextjs.org/docs/14/app/api-reference/functions/generate-metadata)
      * [generateSitemaps](https://nextjs.org/docs/14/app/api-reference/functions/generate-sitemaps)
      * [generateStaticParams](https://nextjs.org/docs/14/app/api-reference/functions/generate-static-params)
      * [generateViewport](https://nextjs.org/docs/14/app/api-reference/functions/generate-viewport)
      * [headers](https://nextjs.org/docs/14/app/api-reference/functions/headers)
      * [ImageResponse](https://nextjs.org/docs/14/app/api-reference/functions/image-response)
      * [NextRequest](https://nextjs.org/docs/14/app/api-reference/functions/next-request)
      * [NextResponse](https://nextjs.org/docs/14/app/api-reference/functions/next-response)
      * [notFound](https://nextjs.org/docs/14/app/api-reference/functions/not-found)
      * [permanentRedirect](https://nextjs.org/docs/14/app/api-reference/functions/permanentRedirect)
      * [redirect](https://nextjs.org/docs/14/app/api-reference/functions/redirect)
      * [revalidatePath](https://nextjs.org/docs/14/app/api-reference/functions/revalidatePath)
      * [revalidateTag](https://nextjs.org/docs/14/app/api-reference/functions/revalidateTag)
      * [unstable_cache](https://nextjs.org/docs/14/app/api-reference/functions/unstable_cache)
      * [unstable_noStore](https://nextjs.org/docs/14/app/api-reference/functions/unstable_noStore)
      * [useParams](https://nextjs.org/docs/14/app/api-reference/functions/use-params)
      * [usePathname](https://nextjs.org/docs/14/app/api-reference/functions/use-pathname)
      * [useReportWebVitals](https://nextjs.org/docs/14/app/api-reference/functions/use-report-web-vitals)
      * [useRouter](https://nextjs.org/docs/14/app/api-reference/functions/use-router)
      * [useSearchParams](https://nextjs.org/docs/14/app/api-reference/functions/use-search-params)
      * [useSelectedLayoutSegment](https://nextjs.org/docs/14/app/api-reference/functions/use-selected-layout-segment)
      * [useSelectedLayoutSegments](https://nextjs.org/docs/14/app/api-reference/functions/use-selected-layout-segments)
      * [userAgent](https://nextjs.org/docs/14/app/api-reference/functions/userAgent)
    * [next.config.js Options](https://nextjs.org/docs/14/app/api-reference/next-config-js)
      * [appDir](https://nextjs.org/docs/14/app/api-reference/next-config-js/appDir)
      * [assetPrefix](https://nextjs.org/docs/14/app/api-reference/next-config-js/assetPrefix)
      * [basePath](https://nextjs.org/docs/14/app/api-reference/next-config-js/basePath)
      * [compress](https://nextjs.org/docs/14/app/api-reference/next-config-js/compress)
      * [devIndicators](https://nextjs.org/docs/14/app/api-reference/next-config-js/devIndicators)
      * [distDir](https://nextjs.org/docs/14/app/api-reference/next-config-js/distDir)
      * [env](https://nextjs.org/docs/14/app/api-reference/next-config-js/env)
      * [eslint](https://nextjs.org/docs/14/app/api-reference/next-config-js/eslint)
      * [exportPathMap](https://nextjs.org/docs/14/app/api-reference/next-config-js/exportPathMap)
      * [generateBuildId](https://nextjs.org/docs/14/app/api-reference/next-config-js/generateBuildId)
      * [generateEtags](https://nextjs.org/docs/14/app/api-reference/next-config-js/generateEtags)
      * [headers](https://nextjs.org/docs/14/app/api-reference/next-config-js/headers)
      * [httpAgentOptions](https://nextjs.org/docs/14/app/api-reference/next-config-js/httpAgentOptions)
      * [images](https://nextjs.org/docs/14/app/api-reference/next-config-js/images)
      * [cacheHandler](https://nextjs.org/docs/14/app/api-reference/next-config-js/incrementalCacheHandlerPath)
      * [logging](https://nextjs.org/docs/14/app/api-reference/next-config-js/logging)
      * [mdxRs](https://nextjs.org/docs/14/app/api-reference/next-config-js/mdxRs)
      * [onDemandEntries](https://nextjs.org/docs/14/app/api-reference/next-config-js/onDemandEntries)
      * [optimizePackageImports](https://nextjs.org/docs/14/app/api-reference/next-config-js/optimizePackageImports)
      * [output](https://nextjs.org/docs/14/app/api-reference/next-config-js/output)
      * [pageExtensions](https://nextjs.org/docs/14/app/api-reference/next-config-js/pageExtensions)
      * [Partial Prerendering (experimental)](https://nextjs.org/docs/14/app/api-reference/next-config-js/partial-prerendering)
      * [poweredByHeader](https://nextjs.org/docs/14/app/api-reference/next-config-js/poweredByHeader)
      * [productionBrowserSourceMaps](https://nextjs.org/docs/14/app/api-reference/next-config-js/productionBrowserSourceMaps)
      * [reactStrictMode](https://nextjs.org/docs/14/app/api-reference/next-config-js/reactStrictMode)
      * [redirects](https://nextjs.org/docs/14/app/api-reference/next-config-js/redirects)
      * [rewrites](https://nextjs.org/docs/14/app/api-reference/next-config-js/rewrites)
      * [serverActions](https://nextjs.org/docs/14/app/api-reference/next-config-js/serverActions)
      * [serverComponentsExternalPackages](https://nextjs.org/docs/14/app/api-reference/next-config-js/serverComponentsExternalPackages)
      * [trailingSlash](https://nextjs.org/docs/14/app/api-reference/next-config-js/trailingSlash)
      * [transpilePackages](https://nextjs.org/docs/14/app/api-reference/next-config-js/transpilePackages)
      * [turbo](https://nextjs.org/docs/14/app/api-reference/next-config-js/turbo)
      * [typedRoutes](https://nextjs.org/docs/14/app/api-reference/next-config-js/typedRoutes)
      * [typescript](https://nextjs.org/docs/14/app/api-reference/next-config-js/typescript)
      * [urlImports](https://nextjs.org/docs/14/app/api-reference/next-config-js/urlImports)
      * [webpack](https://nextjs.org/docs/14/app/api-reference/next-config-js/webpack)
      * [webVitalsAttribution](https://nextjs.org/docs/14/app/api-reference/next-config-js/webVitalsAttribution)
    * [create-next-app](https://nextjs.org/docs/14/app/api-reference/create-next-app)
    * [Edge Runtime](https://nextjs.org/docs/14/app/api-reference/edge)
    * [Next.js CLI](https://nextjs.org/docs/14/app/api-reference/next-cli)


  * [Building Your Application](https://nextjs.org/docs/14/pages/building-your-application)
    * [Routing](https://nextjs.org/docs/14/pages/building-your-application/routing)
      * [Pages and Layouts](https://nextjs.org/docs/14/pages/building-your-application/routing/pages-and-layouts)
      * [Dynamic Routes](https://nextjs.org/docs/14/pages/building-your-application/routing/dynamic-routes)
      * [Linking and Navigating](https://nextjs.org/docs/14/pages/building-your-application/routing/linking-and-navigating)
      * [Custom App](https://nextjs.org/docs/14/pages/building-your-application/routing/custom-app)
      * [Custom Document](https://nextjs.org/docs/14/pages/building-your-application/routing/custom-document)
      * [Custom Errors](https://nextjs.org/docs/14/pages/building-your-application/routing/custom-error)
      * [API Routes](https://nextjs.org/docs/14/pages/building-your-application/routing/api-routes)
      * [Internationalization](https://nextjs.org/docs/14/pages/building-your-application/routing/internationalization)
      * [Authenticating](https://nextjs.org/docs/14/pages/building-your-application/routing/authenticating)
      * [Middleware](https://nextjs.org/docs/14/pages/building-your-application/routing/middleware)
    * [Rendering](https://nextjs.org/docs/14/pages/building-your-application/rendering)
      * [Server-side Rendering (SSR)](https://nextjs.org/docs/14/pages/building-your-application/rendering/server-side-rendering)
      * [Static Site Generation (SSG)](https://nextjs.org/docs/14/pages/building-your-application/rendering/static-site-generation)
      * [Automatic Static Optimization](https://nextjs.org/docs/14/pages/building-your-application/rendering/automatic-static-optimization)
      * [Client-side Rendering (CSR)](https://nextjs.org/docs/14/pages/building-your-application/rendering/client-side-rendering)
      * [Edge and Node.js Runtimes](https://nextjs.org/docs/14/pages/building-your-application/rendering/edge-and-nodejs-runtimes)
    * [Data Fetching](https://nextjs.org/docs/14/pages/building-your-application/data-fetching)
      * [getStaticProps](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/get-static-props)
      * [getStaticPaths](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/get-static-paths)
      * [Forms and Mutations](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/forms-and-mutations)
      * [getServerSideProps](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/get-server-side-props)
      * [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/incremental-static-regeneration)
      * [Client-side Fetching](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/client-side)
    * [Styling](https://nextjs.org/docs/14/pages/building-your-application/styling)
      * [CSS Modules](https://nextjs.org/docs/14/pages/building-your-application/styling/css-modules)
      * [Tailwind CSS](https://nextjs.org/docs/14/pages/building-your-application/styling/tailwind-css)
      * [CSS-in-JS](https://nextjs.org/docs/14/pages/building-your-application/styling/css-in-js)
      * [Sass](https://nextjs.org/docs/14/pages/building-your-application/styling/sass)
    * [Optimizing](https://nextjs.org/docs/14/pages/building-your-application/optimizing)
      * [Images](https://nextjs.org/docs/14/pages/building-your-application/optimizing/images)
      * [Fonts](https://nextjs.org/docs/14/pages/building-your-application/optimizing/fonts)
      * [Scripts](https://nextjs.org/docs/14/pages/building-your-application/optimizing/scripts)
      * [Static Assets](https://nextjs.org/docs/14/pages/building-your-application/optimizing/static-assets)
      * [Bundle Analyzer](https://nextjs.org/docs/14/pages/building-your-application/optimizing/bundle-analyzer)
      * [Analytics](https://nextjs.org/docs/14/pages/building-your-application/optimizing/analytics)
      * [Lazy Loading](https://nextjs.org/docs/14/pages/building-your-application/optimizing/lazy-loading)
      * [Instrumentation](https://nextjs.org/docs/14/pages/building-your-application/optimizing/instrumentation)
      * [OpenTelemetry](https://nextjs.org/docs/14/pages/building-your-application/optimizing/open-telemetry)
      * [Third Party Libraries](https://nextjs.org/docs/14/pages/building-your-application/optimizing/third-party-libraries)
    * [Configuring](https://nextjs.org/docs/14/pages/building-your-application/configuring)
      * [TypeScript](https://nextjs.org/docs/14/pages/building-your-application/configuring/typescript)
      * [ESLint](https://nextjs.org/docs/14/pages/building-your-application/configuring/eslint)
      * [Environment Variables](https://nextjs.org/docs/14/pages/building-your-application/configuring/environment-variables)
      * [Absolute Imports and Module Path Aliases](https://nextjs.org/docs/14/pages/building-your-application/configuring/absolute-imports-and-module-aliases)
      * [src Directory](https://nextjs.org/docs/14/pages/building-your-application/configuring/src-directory)
      * [MDX](https://nextjs.org/docs/14/pages/building-your-application/configuring/mdx)
      * [AMP](https://nextjs.org/docs/14/pages/building-your-application/configuring/amp)
      * [Babel](https://nextjs.org/docs/14/pages/building-your-application/configuring/babel)
      * [PostCSS](https://nextjs.org/docs/14/pages/building-your-application/configuring/post-css)
      * [Custom Server](https://nextjs.org/docs/14/pages/building-your-application/configuring/custom-server)
      * [Draft Mode](https://nextjs.org/docs/14/pages/building-your-application/configuring/draft-mode)
      * [Error Handling](https://nextjs.org/docs/14/pages/building-your-application/configuring/error-handling)
      * [Debugging](https://nextjs.org/docs/14/pages/building-your-application/configuring/debugging)
      * [Preview Mode](https://nextjs.org/docs/14/pages/building-your-application/configuring/preview-mode)
      * [Content Security Policy](https://nextjs.org/docs/14/pages/building-your-application/configuring/content-security-policy)
    * [Testing](https://nextjs.org/docs/14/pages/building-your-application/testing)
      * [Vitest](https://nextjs.org/docs/14/pages/building-your-application/testing/vitest)
      * [Jest](https://nextjs.org/docs/14/pages/building-your-application/testing/jest)
      * [Playwright](https://nextjs.org/docs/14/pages/building-your-application/testing/playwright)
      * [Cypress](https://nextjs.org/docs/14/pages/building-your-application/testing/cypress)
    * [Deploying](https://nextjs.org/docs/14/pages/building-your-application/deploying)
      * [Production Checklist](https://nextjs.org/docs/14/pages/building-your-application/deploying/production-checklist)
      * [Static Exports](https://nextjs.org/docs/14/pages/building-your-application/deploying/static-exports)
      * [Multi Zones](https://nextjs.org/docs/14/pages/building-your-application/deploying/multi-zones)
      * [Continuous Integration (CI) Build Caching](https://nextjs.org/docs/14/pages/building-your-application/deploying/ci-build-caching)
    * [Upgrading](https://nextjs.org/docs/14/pages/building-your-application/upgrading)
      * [Codemods](https://nextjs.org/docs/14/pages/building-your-application/upgrading/codemods)
      * [From Pages to App](https://nextjs.org/docs/14/pages/building-your-application/upgrading/app-router-migration)
      * [Version 14](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-14)
      * [Version 13](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-13)
      * [Version 12](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-12)
      * [Version 11](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-11)
      * [Version 10](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-10)
      * [Version 9](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-9)


  * [API Reference](https://nextjs.org/docs/14/pages/api-reference)
    * [Components](https://nextjs.org/docs/14/pages/api-reference/components)
      * [Font](https://nextjs.org/docs/14/pages/api-reference/components/font)
      * [<Head>](https://nextjs.org/docs/14/pages/api-reference/components/head)
      * [<Image>](https://nextjs.org/docs/14/pages/api-reference/components/image)
      * [<Image> (Legacy)](https://nextjs.org/docs/14/pages/api-reference/components/image-legacy)
      * [<Link>](https://nextjs.org/docs/14/pages/api-reference/components/link)
      * [<Script>](https://nextjs.org/docs/14/pages/api-reference/components/script)
    * [Functions](https://nextjs.org/docs/14/pages/api-reference/functions)
      * [getInitialProps](https://nextjs.org/docs/14/pages/api-reference/functions/get-initial-props)
      * [getServerSideProps](https://nextjs.org/docs/14/pages/api-reference/functions/get-server-side-props)
      * [getStaticPaths](https://nextjs.org/docs/14/pages/api-reference/functions/get-static-paths)
      * [getStaticProps](https://nextjs.org/docs/14/pages/api-reference/functions/get-static-props)
      * [NextRequest](https://nextjs.org/docs/14/pages/api-reference/functions/next-request)
      * [NextResponse](https://nextjs.org/docs/14/pages/api-reference/functions/next-response)
      * [useAmp](https://nextjs.org/docs/14/pages/api-reference/functions/use-amp)
      * [useReportWebVitals](https://nextjs.org/docs/14/pages/api-reference/functions/use-report-web-vitals)
      * [useRouter](https://nextjs.org/docs/14/pages/api-reference/functions/use-router)
      * [userAgent](https://nextjs.org/docs/14/pages/api-reference/functions/userAgent)
    * [next.config.js Options](https://nextjs.org/docs/14/pages/api-reference/next-config-js)
      * [assetPrefix](https://nextjs.org/docs/14/pages/api-reference/next-config-js/assetPrefix)
      * [basePath](https://nextjs.org/docs/14/pages/api-reference/next-config-js/basePath)
      * [compress](https://nextjs.org/docs/14/pages/api-reference/next-config-js/compress)
      * [devIndicators](https://nextjs.org/docs/14/pages/api-reference/next-config-js/devIndicators)
      * [distDir](https://nextjs.org/docs/14/pages/api-reference/next-config-js/distDir)
      * [env](https://nextjs.org/docs/14/pages/api-reference/next-config-js/env)
      * [eslint](https://nextjs.org/docs/14/pages/api-reference/next-config-js/eslint)
      * [exportPathMap](https://nextjs.org/docs/14/pages/api-reference/next-config-js/exportPathMap)
      * [generateBuildId](https://nextjs.org/docs/14/pages/api-reference/next-config-js/generateBuildId)
      * [generateEtags](https://nextjs.org/docs/14/pages/api-reference/next-config-js/generateEtags)
      * [headers](https://nextjs.org/docs/14/pages/api-reference/next-config-js/headers)
      * [httpAgentOptions](https://nextjs.org/docs/14/pages/api-reference/next-config-js/httpAgentOptions)
      * [images](https://nextjs.org/docs/14/pages/api-reference/next-config-js/images)
      * [onDemandEntries](https://nextjs.org/docs/14/pages/api-reference/next-config-js/onDemandEntries)
      * [output](https://nextjs.org/docs/14/pages/api-reference/next-config-js/output)
      * [pageExtensions](https://nextjs.org/docs/14/pages/api-reference/next-config-js/pageExtensions)
      * [poweredByHeader](https://nextjs.org/docs/14/pages/api-reference/next-config-js/poweredByHeader)
      * [productionBrowserSourceMaps](https://nextjs.org/docs/14/pages/api-reference/next-config-js/productionBrowserSourceMaps)
      * [reactStrictMode](https://nextjs.org/docs/14/pages/api-reference/next-config-js/reactStrictMode)
      * [redirects](https://nextjs.org/docs/14/pages/api-reference/next-config-js/redirects)
      * [rewrites](https://nextjs.org/docs/14/pages/api-reference/next-config-js/rewrites)
      * [Runtime Config](https://nextjs.org/docs/14/pages/api-reference/next-config-js/runtime-configuration)
      * [trailingSlash](https://nextjs.org/docs/14/pages/api-reference/next-config-js/trailingSlash)
      * [transpilePackages](https://nextjs.org/docs/14/pages/api-reference/next-config-js/transpilePackages)
      * [turbo](https://nextjs.org/docs/14/pages/api-reference/next-config-js/turbo)
      * [typescript](https://nextjs.org/docs/14/pages/api-reference/next-config-js/typescript)
      * [urlImports](https://nextjs.org/docs/14/pages/api-reference/next-config-js/urlImports)
      * [webpack](https://nextjs.org/docs/14/pages/api-reference/next-config-js/webpack)
      * [webVitalsAttribution](https://nextjs.org/docs/14/pages/api-reference/next-config-js/webVitalsAttribution)
    * [create-next-app](https://nextjs.org/docs/14/pages/api-reference/create-next-app)
    * [Next.js CLI](https://nextjs.org/docs/14/pages/api-reference/next-cli)
    * [Edge Runtime](https://nextjs.org/docs/14/pages/api-reference/edge)


  * [Architecture](https://nextjs.org/docs/14/architecture)
    * [Accessibility](https://nextjs.org/docs/14/architecture/accessibility)
    * [Fast Refresh](https://nextjs.org/docs/14/architecture/fast-refresh)
    * [Next.js Compiler](https://nextjs.org/docs/14/architecture/nextjs-compiler)
    * [Supported Browsers](https://nextjs.org/docs/14/architecture/supported-browsers)
    * [Turbopack](https://nextjs.org/docs/14/architecture/turbopack)


  * [Community](https://nextjs.org/docs/14/community)
    * [Contribution Guide](https://nextjs.org/docs/14/community/contribution-guide)


Using App Router
Features available in /app
Version 14
14.2.35
  * [Getting Started](https://nextjs.org/docs/14/getting-started)
    * [Installation](https://nextjs.org/docs/14/getting-started/installation)
    * [Project Structure](https://nextjs.org/docs/14/getting-started/project-structure)


  * [Building Your Application](https://nextjs.org/docs/14/app/building-your-application)
    * [Routing](https://nextjs.org/docs/14/app/building-your-application/routing)
      * [Defining Routes](https://nextjs.org/docs/14/app/building-your-application/routing/defining-routes)
      * [Pages and Layouts](https://nextjs.org/docs/14/app/building-your-application/routing/pages-and-layouts)
      * [Linking and Navigating](https://nextjs.org/docs/14/app/building-your-application/routing/linking-and-navigating)
      * [Loading UI and Streaming](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming)
      * [Error Handling](https://nextjs.org/docs/14/app/building-your-application/routing/error-handling)
      * [Redirecting](https://nextjs.org/docs/14/app/building-your-application/routing/redirecting)
      * [Route Groups](https://nextjs.org/docs/14/app/building-your-application/routing/route-groups)
      * [Project Organization](https://nextjs.org/docs/14/app/building-your-application/routing/colocation)
      * [Dynamic Routes](https://nextjs.org/docs/14/app/building-your-application/routing/dynamic-routes)
      * [Parallel Routes](https://nextjs.org/docs/14/app/building-your-application/routing/parallel-routes)
      * [Intercepting Routes](https://nextjs.org/docs/14/app/building-your-application/routing/intercepting-routes)
      * [Route Handlers](https://nextjs.org/docs/14/app/building-your-application/routing/route-handlers)
      * [Middleware](https://nextjs.org/docs/14/app/building-your-application/routing/middleware)
      * [Internationalization](https://nextjs.org/docs/14/app/building-your-application/routing/internationalization)
    * [Data Fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching)
      * [Fetching, Caching, and Revalidating](https://nextjs.org/docs/14/app/building-your-application/data-fetching/fetching-caching-and-revalidating)
      * [Server Actions and Mutations](https://nextjs.org/docs/14/app/building-your-application/data-fetching/server-actions-and-mutations)
      * [Data Fetching Patterns and Best Practices](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns)
    * [Rendering](https://nextjs.org/docs/14/app/building-your-application/rendering)
      * [Server Components](https://nextjs.org/docs/14/app/building-your-application/rendering/server-components)
      * [Client Components](https://nextjs.org/docs/14/app/building-your-application/rendering/client-components)
      * [Composition Patterns](https://nextjs.org/docs/14/app/building-your-application/rendering/composition-patterns)
      * [Edge and Node.js Runtimes](https://nextjs.org/docs/14/app/building-your-application/rendering/edge-and-nodejs-runtimes)
    * [Caching](https://nextjs.org/docs/14/app/building-your-application/caching)
    * [Styling](https://nextjs.org/docs/14/app/building-your-application/styling)
      * [CSS Modules](https://nextjs.org/docs/14/app/building-your-application/styling/css-modules)
      * [Tailwind CSS](https://nextjs.org/docs/14/app/building-your-application/styling/tailwind-css)
      * [CSS-in-JS](https://nextjs.org/docs/14/app/building-your-application/styling/css-in-js)
      * [Sass](https://nextjs.org/docs/14/app/building-your-application/styling/sass)
    * [Optimizing](https://nextjs.org/docs/14/app/building-your-application/optimizing)
      * [Images](https://nextjs.org/docs/14/app/building-your-application/optimizing/images)
      * [Fonts](https://nextjs.org/docs/14/app/building-your-application/optimizing/fonts)
      * [Scripts](https://nextjs.org/docs/14/app/building-your-application/optimizing/scripts)
      * [Metadata](https://nextjs.org/docs/14/app/building-your-application/optimizing/metadata)
      * [Static Assets](https://nextjs.org/docs/14/app/building-your-application/optimizing/static-assets)
      * [Bundle Analyzer](https://nextjs.org/docs/14/app/building-your-application/optimizing/bundle-analyzer)
      * [Lazy Loading](https://nextjs.org/docs/14/app/building-your-application/optimizing/lazy-loading)
      * [Analytics](https://nextjs.org/docs/14/app/building-your-application/optimizing/analytics)
      * [Instrumentation](https://nextjs.org/docs/14/app/building-your-application/optimizing/instrumentation)
      * [OpenTelemetry](https://nextjs.org/docs/14/app/building-your-application/optimizing/open-telemetry)
      * [Third Party Libraries](https://nextjs.org/docs/14/app/building-your-application/optimizing/third-party-libraries)
    * [Configuring](https://nextjs.org/docs/14/app/building-your-application/configuring)
      * [TypeScript](https://nextjs.org/docs/14/app/building-your-application/configuring/typescript)
      * [ESLint](https://nextjs.org/docs/14/app/building-your-application/configuring/eslint)
      * [Environment Variables](https://nextjs.org/docs/14/app/building-your-application/configuring/environment-variables)
      * [Absolute Imports and Module Path Aliases](https://nextjs.org/docs/14/app/building-your-application/configuring/absolute-imports-and-module-aliases)
      * [MDX](https://nextjs.org/docs/14/app/building-your-application/configuring/mdx)
      * [src Directory](https://nextjs.org/docs/14/app/building-your-application/configuring/src-directory)
      * [Draft Mode](https://nextjs.org/docs/14/app/building-your-application/configuring/draft-mode)
      * [Content Security Policy](https://nextjs.org/docs/14/app/building-your-application/configuring/content-security-policy)
    * [Testing](https://nextjs.org/docs/14/app/building-your-application/testing)
      * [Vitest](https://nextjs.org/docs/14/app/building-your-application/testing/vitest)
      * [Jest](https://nextjs.org/docs/14/app/building-your-application/testing/jest)
      * [Playwright](https://nextjs.org/docs/14/app/building-your-application/testing/playwright)
      * [Cypress](https://nextjs.org/docs/14/app/building-your-application/testing/cypress)
    * [Authentication](https://nextjs.org/docs/14/app/building-your-application/authentication)
    * [Deploying](https://nextjs.org/docs/14/app/building-your-application/deploying)
      * [Production Checklist](https://nextjs.org/docs/14/app/building-your-application/deploying/production-checklist)
      * [Static Exports](https://nextjs.org/docs/14/app/building-your-application/deploying/static-exports)
    * [Upgrading](https://nextjs.org/docs/14/app/building-your-application/upgrading)
      * [Codemods](https://nextjs.org/docs/14/app/building-your-application/upgrading/codemods)
      * [App Router Migration](https://nextjs.org/docs/14/app/building-your-application/upgrading/app-router-migration)
      * [Version 14](https://nextjs.org/docs/14/app/building-your-application/upgrading/version-14)
      * [Migrating from Vite](https://nextjs.org/docs/14/app/building-your-application/upgrading/from-vite)


  * [API Reference](https://nextjs.org/docs/14/app/api-reference)
    * [Components](https://nextjs.org/docs/14/app/api-reference/components)
      * [Font](https://nextjs.org/docs/14/app/api-reference/components/font)
      * [<Image>](https://nextjs.org/docs/14/app/api-reference/components/image)
      * [<Link>](https://nextjs.org/docs/14/app/api-reference/components/link)
      * [<Script>](https://nextjs.org/docs/14/app/api-reference/components/script)
    * [File Conventions](https://nextjs.org/docs/14/app/api-reference/file-conventions)
      * [default.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/default)
      * [error.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/error)
      * [layout.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/layout)
      * [loading.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/loading)
      * [not-found.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/not-found)
      * [page.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/page)
      * [route.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/route)
      * [Route Segment Config](https://nextjs.org/docs/14/app/api-reference/file-conventions/route-segment-config)
      * [template.js](https://nextjs.org/docs/14/app/api-reference/file-conventions/template)
      * [Metadata Files](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata)
        * [favicon, icon, and apple-icon](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/app-icons)
        * [manifest.json](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/manifest)
        * [opengraph-image and twitter-image](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/opengraph-image)
        * [robots.txt](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/robots)
        * [sitemap.xml](https://nextjs.org/docs/14/app/api-reference/file-conventions/metadata/sitemap)
    * [Functions](https://nextjs.org/docs/14/app/api-reference/functions)
      * [cookies](https://nextjs.org/docs/14/app/api-reference/functions/cookies)
      * [draftMode](https://nextjs.org/docs/14/app/api-reference/functions/draft-mode)
      * [fetch](https://nextjs.org/docs/14/app/api-reference/functions/fetch)
      * [generateImageMetadata](https://nextjs.org/docs/14/app/api-reference/functions/generate-image-metadata)
      * [generateMetadata](https://nextjs.org/docs/14/app/api-reference/functions/generate-metadata)
      * [generateSitemaps](https://nextjs.org/docs/14/app/api-reference/functions/generate-sitemaps)
      * [generateStaticParams](https://nextjs.org/docs/14/app/api-reference/functions/generate-static-params)
      * [generateViewport](https://nextjs.org/docs/14/app/api-reference/functions/generate-viewport)
      * [headers](https://nextjs.org/docs/14/app/api-reference/functions/headers)
      * [ImageResponse](https://nextjs.org/docs/14/app/api-reference/functions/image-response)
      * [NextRequest](https://nextjs.org/docs/14/app/api-reference/functions/next-request)
      * [NextResponse](https://nextjs.org/docs/14/app/api-reference/functions/next-response)
      * [notFound](https://nextjs.org/docs/14/app/api-reference/functions/not-found)
      * [permanentRedirect](https://nextjs.org/docs/14/app/api-reference/functions/permanentRedirect)
      * [redirect](https://nextjs.org/docs/14/app/api-reference/functions/redirect)
      * [revalidatePath](https://nextjs.org/docs/14/app/api-reference/functions/revalidatePath)
      * [revalidateTag](https://nextjs.org/docs/14/app/api-reference/functions/revalidateTag)
      * [unstable_cache](https://nextjs.org/docs/14/app/api-reference/functions/unstable_cache)
      * [unstable_noStore](https://nextjs.org/docs/14/app/api-reference/functions/unstable_noStore)
      * [useParams](https://nextjs.org/docs/14/app/api-reference/functions/use-params)
      * [usePathname](https://nextjs.org/docs/14/app/api-reference/functions/use-pathname)
      * [useReportWebVitals](https://nextjs.org/docs/14/app/api-reference/functions/use-report-web-vitals)
      * [useRouter](https://nextjs.org/docs/14/app/api-reference/functions/use-router)
      * [useSearchParams](https://nextjs.org/docs/14/app/api-reference/functions/use-search-params)
      * [useSelectedLayoutSegment](https://nextjs.org/docs/14/app/api-reference/functions/use-selected-layout-segment)
      * [useSelectedLayoutSegments](https://nextjs.org/docs/14/app/api-reference/functions/use-selected-layout-segments)
      * [userAgent](https://nextjs.org/docs/14/app/api-reference/functions/userAgent)
    * [next.config.js Options](https://nextjs.org/docs/14/app/api-reference/next-config-js)
      * [appDir](https://nextjs.org/docs/14/app/api-reference/next-config-js/appDir)
      * [assetPrefix](https://nextjs.org/docs/14/app/api-reference/next-config-js/assetPrefix)
      * [basePath](https://nextjs.org/docs/14/app/api-reference/next-config-js/basePath)
      * [compress](https://nextjs.org/docs/14/app/api-reference/next-config-js/compress)
      * [devIndicators](https://nextjs.org/docs/14/app/api-reference/next-config-js/devIndicators)
      * [distDir](https://nextjs.org/docs/14/app/api-reference/next-config-js/distDir)
      * [env](https://nextjs.org/docs/14/app/api-reference/next-config-js/env)
      * [eslint](https://nextjs.org/docs/14/app/api-reference/next-config-js/eslint)
      * [exportPathMap](https://nextjs.org/docs/14/app/api-reference/next-config-js/exportPathMap)
      * [generateBuildId](https://nextjs.org/docs/14/app/api-reference/next-config-js/generateBuildId)
      * [generateEtags](https://nextjs.org/docs/14/app/api-reference/next-config-js/generateEtags)
      * [headers](https://nextjs.org/docs/14/app/api-reference/next-config-js/headers)
      * [httpAgentOptions](https://nextjs.org/docs/14/app/api-reference/next-config-js/httpAgentOptions)
      * [images](https://nextjs.org/docs/14/app/api-reference/next-config-js/images)
      * [cacheHandler](https://nextjs.org/docs/14/app/api-reference/next-config-js/incrementalCacheHandlerPath)
      * [logging](https://nextjs.org/docs/14/app/api-reference/next-config-js/logging)
      * [mdxRs](https://nextjs.org/docs/14/app/api-reference/next-config-js/mdxRs)
      * [onDemandEntries](https://nextjs.org/docs/14/app/api-reference/next-config-js/onDemandEntries)
      * [optimizePackageImports](https://nextjs.org/docs/14/app/api-reference/next-config-js/optimizePackageImports)
      * [output](https://nextjs.org/docs/14/app/api-reference/next-config-js/output)
      * [pageExtensions](https://nextjs.org/docs/14/app/api-reference/next-config-js/pageExtensions)
      * [Partial Prerendering (experimental)](https://nextjs.org/docs/14/app/api-reference/next-config-js/partial-prerendering)
      * [poweredByHeader](https://nextjs.org/docs/14/app/api-reference/next-config-js/poweredByHeader)
      * [productionBrowserSourceMaps](https://nextjs.org/docs/14/app/api-reference/next-config-js/productionBrowserSourceMaps)
      * [reactStrictMode](https://nextjs.org/docs/14/app/api-reference/next-config-js/reactStrictMode)
      * [redirects](https://nextjs.org/docs/14/app/api-reference/next-config-js/redirects)
      * [rewrites](https://nextjs.org/docs/14/app/api-reference/next-config-js/rewrites)
      * [serverActions](https://nextjs.org/docs/14/app/api-reference/next-config-js/serverActions)
      * [serverComponentsExternalPackages](https://nextjs.org/docs/14/app/api-reference/next-config-js/serverComponentsExternalPackages)
      * [trailingSlash](https://nextjs.org/docs/14/app/api-reference/next-config-js/trailingSlash)
      * [transpilePackages](https://nextjs.org/docs/14/app/api-reference/next-config-js/transpilePackages)
      * [turbo](https://nextjs.org/docs/14/app/api-reference/next-config-js/turbo)
      * [typedRoutes](https://nextjs.org/docs/14/app/api-reference/next-config-js/typedRoutes)
      * [typescript](https://nextjs.org/docs/14/app/api-reference/next-config-js/typescript)
      * [urlImports](https://nextjs.org/docs/14/app/api-reference/next-config-js/urlImports)
      * [webpack](https://nextjs.org/docs/14/app/api-reference/next-config-js/webpack)
      * [webVitalsAttribution](https://nextjs.org/docs/14/app/api-reference/next-config-js/webVitalsAttribution)
    * [create-next-app](https://nextjs.org/docs/14/app/api-reference/create-next-app)
    * [Edge Runtime](https://nextjs.org/docs/14/app/api-reference/edge)
    * [Next.js CLI](https://nextjs.org/docs/14/app/api-reference/next-cli)


  * [Building Your Application](https://nextjs.org/docs/14/pages/building-your-application)
    * [Routing](https://nextjs.org/docs/14/pages/building-your-application/routing)
      * [Pages and Layouts](https://nextjs.org/docs/14/pages/building-your-application/routing/pages-and-layouts)
      * [Dynamic Routes](https://nextjs.org/docs/14/pages/building-your-application/routing/dynamic-routes)
      * [Linking and Navigating](https://nextjs.org/docs/14/pages/building-your-application/routing/linking-and-navigating)
      * [Custom App](https://nextjs.org/docs/14/pages/building-your-application/routing/custom-app)
      * [Custom Document](https://nextjs.org/docs/14/pages/building-your-application/routing/custom-document)
      * [Custom Errors](https://nextjs.org/docs/14/pages/building-your-application/routing/custom-error)
      * [API Routes](https://nextjs.org/docs/14/pages/building-your-application/routing/api-routes)
      * [Internationalization](https://nextjs.org/docs/14/pages/building-your-application/routing/internationalization)
      * [Authenticating](https://nextjs.org/docs/14/pages/building-your-application/routing/authenticating)
      * [Middleware](https://nextjs.org/docs/14/pages/building-your-application/routing/middleware)
    * [Rendering](https://nextjs.org/docs/14/pages/building-your-application/rendering)
      * [Server-side Rendering (SSR)](https://nextjs.org/docs/14/pages/building-your-application/rendering/server-side-rendering)
      * [Static Site Generation (SSG)](https://nextjs.org/docs/14/pages/building-your-application/rendering/static-site-generation)
      * [Automatic Static Optimization](https://nextjs.org/docs/14/pages/building-your-application/rendering/automatic-static-optimization)
      * [Client-side Rendering (CSR)](https://nextjs.org/docs/14/pages/building-your-application/rendering/client-side-rendering)
      * [Edge and Node.js Runtimes](https://nextjs.org/docs/14/pages/building-your-application/rendering/edge-and-nodejs-runtimes)
    * [Data Fetching](https://nextjs.org/docs/14/pages/building-your-application/data-fetching)
      * [getStaticProps](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/get-static-props)
      * [getStaticPaths](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/get-static-paths)
      * [Forms and Mutations](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/forms-and-mutations)
      * [getServerSideProps](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/get-server-side-props)
      * [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/incremental-static-regeneration)
      * [Client-side Fetching](https://nextjs.org/docs/14/pages/building-your-application/data-fetching/client-side)
    * [Styling](https://nextjs.org/docs/14/pages/building-your-application/styling)
      * [CSS Modules](https://nextjs.org/docs/14/pages/building-your-application/styling/css-modules)
      * [Tailwind CSS](https://nextjs.org/docs/14/pages/building-your-application/styling/tailwind-css)
      * [CSS-in-JS](https://nextjs.org/docs/14/pages/building-your-application/styling/css-in-js)
      * [Sass](https://nextjs.org/docs/14/pages/building-your-application/styling/sass)
    * [Optimizing](https://nextjs.org/docs/14/pages/building-your-application/optimizing)
      * [Images](https://nextjs.org/docs/14/pages/building-your-application/optimizing/images)
      * [Fonts](https://nextjs.org/docs/14/pages/building-your-application/optimizing/fonts)
      * [Scripts](https://nextjs.org/docs/14/pages/building-your-application/optimizing/scripts)
      * [Static Assets](https://nextjs.org/docs/14/pages/building-your-application/optimizing/static-assets)
      * [Bundle Analyzer](https://nextjs.org/docs/14/pages/building-your-application/optimizing/bundle-analyzer)
      * [Analytics](https://nextjs.org/docs/14/pages/building-your-application/optimizing/analytics)
      * [Lazy Loading](https://nextjs.org/docs/14/pages/building-your-application/optimizing/lazy-loading)
      * [Instrumentation](https://nextjs.org/docs/14/pages/building-your-application/optimizing/instrumentation)
      * [OpenTelemetry](https://nextjs.org/docs/14/pages/building-your-application/optimizing/open-telemetry)
      * [Third Party Libraries](https://nextjs.org/docs/14/pages/building-your-application/optimizing/third-party-libraries)
    * [Configuring](https://nextjs.org/docs/14/pages/building-your-application/configuring)
      * [TypeScript](https://nextjs.org/docs/14/pages/building-your-application/configuring/typescript)
      * [ESLint](https://nextjs.org/docs/14/pages/building-your-application/configuring/eslint)
      * [Environment Variables](https://nextjs.org/docs/14/pages/building-your-application/configuring/environment-variables)
      * [Absolute Imports and Module Path Aliases](https://nextjs.org/docs/14/pages/building-your-application/configuring/absolute-imports-and-module-aliases)
      * [src Directory](https://nextjs.org/docs/14/pages/building-your-application/configuring/src-directory)
      * [MDX](https://nextjs.org/docs/14/pages/building-your-application/configuring/mdx)
      * [AMP](https://nextjs.org/docs/14/pages/building-your-application/configuring/amp)
      * [Babel](https://nextjs.org/docs/14/pages/building-your-application/configuring/babel)
      * [PostCSS](https://nextjs.org/docs/14/pages/building-your-application/configuring/post-css)
      * [Custom Server](https://nextjs.org/docs/14/pages/building-your-application/configuring/custom-server)
      * [Draft Mode](https://nextjs.org/docs/14/pages/building-your-application/configuring/draft-mode)
      * [Error Handling](https://nextjs.org/docs/14/pages/building-your-application/configuring/error-handling)
      * [Debugging](https://nextjs.org/docs/14/pages/building-your-application/configuring/debugging)
      * [Preview Mode](https://nextjs.org/docs/14/pages/building-your-application/configuring/preview-mode)
      * [Content Security Policy](https://nextjs.org/docs/14/pages/building-your-application/configuring/content-security-policy)
    * [Testing](https://nextjs.org/docs/14/pages/building-your-application/testing)
      * [Vitest](https://nextjs.org/docs/14/pages/building-your-application/testing/vitest)
      * [Jest](https://nextjs.org/docs/14/pages/building-your-application/testing/jest)
      * [Playwright](https://nextjs.org/docs/14/pages/building-your-application/testing/playwright)
      * [Cypress](https://nextjs.org/docs/14/pages/building-your-application/testing/cypress)
    * [Deploying](https://nextjs.org/docs/14/pages/building-your-application/deploying)
      * [Production Checklist](https://nextjs.org/docs/14/pages/building-your-application/deploying/production-checklist)
      * [Static Exports](https://nextjs.org/docs/14/pages/building-your-application/deploying/static-exports)
      * [Multi Zones](https://nextjs.org/docs/14/pages/building-your-application/deploying/multi-zones)
      * [Continuous Integration (CI) Build Caching](https://nextjs.org/docs/14/pages/building-your-application/deploying/ci-build-caching)
    * [Upgrading](https://nextjs.org/docs/14/pages/building-your-application/upgrading)
      * [Codemods](https://nextjs.org/docs/14/pages/building-your-application/upgrading/codemods)
      * [From Pages to App](https://nextjs.org/docs/14/pages/building-your-application/upgrading/app-router-migration)
      * [Version 14](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-14)
      * [Version 13](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-13)
      * [Version 12](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-12)
      * [Version 11](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-11)
      * [Version 10](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-10)
      * [Version 9](https://nextjs.org/docs/14/pages/building-your-application/upgrading/version-9)


  * [API Reference](https://nextjs.org/docs/14/pages/api-reference)
    * [Components](https://nextjs.org/docs/14/pages/api-reference/components)
      * [Font](https://nextjs.org/docs/14/pages/api-reference/components/font)
      * [<Head>](https://nextjs.org/docs/14/pages/api-reference/components/head)
      * [<Image>](https://nextjs.org/docs/14/pages/api-reference/components/image)
      * [<Image> (Legacy)](https://nextjs.org/docs/14/pages/api-reference/components/image-legacy)
      * [<Link>](https://nextjs.org/docs/14/pages/api-reference/components/link)
      * [<Script>](https://nextjs.org/docs/14/pages/api-reference/components/script)
    * [Functions](https://nextjs.org/docs/14/pages/api-reference/functions)
      * [getInitialProps](https://nextjs.org/docs/14/pages/api-reference/functions/get-initial-props)
      * [getServerSideProps](https://nextjs.org/docs/14/pages/api-reference/functions/get-server-side-props)
      * [getStaticPaths](https://nextjs.org/docs/14/pages/api-reference/functions/get-static-paths)
      * [getStaticProps](https://nextjs.org/docs/14/pages/api-reference/functions/get-static-props)
      * [NextRequest](https://nextjs.org/docs/14/pages/api-reference/functions/next-request)
      * [NextResponse](https://nextjs.org/docs/14/pages/api-reference/functions/next-response)
      * [useAmp](https://nextjs.org/docs/14/pages/api-reference/functions/use-amp)
      * [useReportWebVitals](https://nextjs.org/docs/14/pages/api-reference/functions/use-report-web-vitals)
      * [useRouter](https://nextjs.org/docs/14/pages/api-reference/functions/use-router)
      * [userAgent](https://nextjs.org/docs/14/pages/api-reference/functions/userAgent)
    * [next.config.js Options](https://nextjs.org/docs/14/pages/api-reference/next-config-js)
      * [assetPrefix](https://nextjs.org/docs/14/pages/api-reference/next-config-js/assetPrefix)
      * [basePath](https://nextjs.org/docs/14/pages/api-reference/next-config-js/basePath)
      * [compress](https://nextjs.org/docs/14/pages/api-reference/next-config-js/compress)
      * [devIndicators](https://nextjs.org/docs/14/pages/api-reference/next-config-js/devIndicators)
      * [distDir](https://nextjs.org/docs/14/pages/api-reference/next-config-js/distDir)
      * [env](https://nextjs.org/docs/14/pages/api-reference/next-config-js/env)
      * [eslint](https://nextjs.org/docs/14/pages/api-reference/next-config-js/eslint)
      * [exportPathMap](https://nextjs.org/docs/14/pages/api-reference/next-config-js/exportPathMap)
      * [generateBuildId](https://nextjs.org/docs/14/pages/api-reference/next-config-js/generateBuildId)
      * [generateEtags](https://nextjs.org/docs/14/pages/api-reference/next-config-js/generateEtags)
      * [headers](https://nextjs.org/docs/14/pages/api-reference/next-config-js/headers)
      * [httpAgentOptions](https://nextjs.org/docs/14/pages/api-reference/next-config-js/httpAgentOptions)
      * [images](https://nextjs.org/docs/14/pages/api-reference/next-config-js/images)
      * [onDemandEntries](https://nextjs.org/docs/14/pages/api-reference/next-config-js/onDemandEntries)
      * [output](https://nextjs.org/docs/14/pages/api-reference/next-config-js/output)
      * [pageExtensions](https://nextjs.org/docs/14/pages/api-reference/next-config-js/pageExtensions)
      * [poweredByHeader](https://nextjs.org/docs/14/pages/api-reference/next-config-js/poweredByHeader)
      * [productionBrowserSourceMaps](https://nextjs.org/docs/14/pages/api-reference/next-config-js/productionBrowserSourceMaps)
      * [reactStrictMode](https://nextjs.org/docs/14/pages/api-reference/next-config-js/reactStrictMode)
      * [redirects](https://nextjs.org/docs/14/pages/api-reference/next-config-js/redirects)
      * [rewrites](https://nextjs.org/docs/14/pages/api-reference/next-config-js/rewrites)
      * [Runtime Config](https://nextjs.org/docs/14/pages/api-reference/next-config-js/runtime-configuration)
      * [trailingSlash](https://nextjs.org/docs/14/pages/api-reference/next-config-js/trailingSlash)
      * [transpilePackages](https://nextjs.org/docs/14/pages/api-reference/next-config-js/transpilePackages)
      * [turbo](https://nextjs.org/docs/14/pages/api-reference/next-config-js/turbo)
      * [typescript](https://nextjs.org/docs/14/pages/api-reference/next-config-js/typescript)
      * [urlImports](https://nextjs.org/docs/14/pages/api-reference/next-config-js/urlImports)
      * [webpack](https://nextjs.org/docs/14/pages/api-reference/next-config-js/webpack)
      * [webVitalsAttribution](https://nextjs.org/docs/14/pages/api-reference/next-config-js/webVitalsAttribution)
    * [create-next-app](https://nextjs.org/docs/14/pages/api-reference/create-next-app)
    * [Next.js CLI](https://nextjs.org/docs/14/pages/api-reference/next-cli)
    * [Edge Runtime](https://nextjs.org/docs/14/pages/api-reference/edge)


  * [Architecture](https://nextjs.org/docs/14/architecture)
    * [Accessibility](https://nextjs.org/docs/14/architecture/accessibility)
    * [Fast Refresh](https://nextjs.org/docs/14/architecture/fast-refresh)
    * [Next.js Compiler](https://nextjs.org/docs/14/architecture/nextjs-compiler)
    * [Supported Browsers](https://nextjs.org/docs/14/architecture/supported-browsers)
    * [Turbopack](https://nextjs.org/docs/14/architecture/turbopack)


  * [Community](https://nextjs.org/docs/14/community)
    * [Contribution Guide](https://nextjs.org/docs/14/community/contribution-guide)


On this page
  * [Fetching data on the server](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#fetching-data-on-the-server)
  * [Fetching data where it's needed](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#fetching-data-where-its-needed)
  * [Streaming](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#streaming)
  * [Parallel and sequential data fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-and-sequential-data-fetching)
  * [Sequential Data Fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#sequential-data-fetching)
  * [Parallel Data Fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-data-fetching)
  * [Preloading Data](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#preloading-data)
  * [Using React cache, server-only, and the Preload Pattern](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#using-react-cache-server-only-and-the-preload-pattern)
  * [Preventing sensitive data from being exposed to the client](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#preventing-sensitive-data-from-being-exposed-to-the-client)


Scroll to top 
This page is also available as Markdown at [/docs/14/app/building-your-application/data-fetching/patterns.md](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns.md). For an index of Next.js 14 documentation, see [/docs/14/llms.txt](https://nextjs.org/docs/14/llms.txt).
[Building Your Application](https://nextjs.org/docs/14/app/building-your-application)[Data Fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching)Data Fetching Patterns and Best Practices
You are currently viewing documentation for version 14 of Next.js.
# Patterns and Best Practices
Last updated March 7, 2024
There are a few recommended patterns and best practices for fetching data in React and Next.js. This page will go over some of the most common patterns and how to use them.
## Fetching data on the server[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#fetching-data-on-the-server)
Whenever possible, we recommend fetching data on the server with Server Components. This allows you to:
  * Have direct access to backend data resources (e.g. databases).
  * Keep your application more secure by preventing sensitive information, such as access tokens and API keys, from being exposed to the client.
  * Fetch data and render in the same environment. This reduces both the back-and-forth communication between client and server, as well as the [work on the main thread](https://vercel.com/blog/how-react-18-improves-application-performance) on the client.
  * Perform multiple data fetches with single round-trip instead of multiple individual requests on the client.
  * Reduce client-server [waterfalls](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-and-sequential-data-fetching).
  * Depending on your region, data fetching can also happen closer to your data source, reducing latency and improving performance.


Then, you can mutate or update data with [Server Actions](https://nextjs.org/docs/14/app/building-your-application/data-fetching/server-actions-and-mutations).
## Fetching data where it's needed[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#fetching-data-where-its-needed)
If you need to use the same data (e.g. current user) in multiple components in a tree, you do not have to fetch data globally, nor forward props between components. Instead, you can use `fetch` or React `cache` in the component that needs the data without worrying about the performance implications of making multiple requests for the same data.
This is possible because `fetch` requests are automatically memoized. Learn more about [request memoization](https://nextjs.org/docs/14/app/building-your-application/caching#request-memoization)
> **Good to know** : This also applies to layouts, since it's not possible to pass data between a parent layout and its children.
## Streaming[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#streaming)
Streaming and [Suspense](https://react.dev/reference/react/Suspense) are React features that allow you to progressively render and incrementally stream rendered units of the UI to the client.
With Server Components and [nested layouts](https://nextjs.org/docs/14/app/building-your-application/routing/pages-and-layouts), you're able to instantly render parts of the page that do not specifically require data, and show a [loading state](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming) for parts of the page that are fetching data. This means the user does not have to wait for the entire page to load before they can start interacting with it.
![Server Rendering with Streaming](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fserver-rendering-with-streaming.png&w=3840&q=75)![Server Rendering with Streaming](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fserver-rendering-with-streaming.png&w=3840&q=75)
To learn more about Streaming and Suspense, see the [Loading UI](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming) and [Streaming and Suspense](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming#streaming-with-suspense) pages.
## Parallel and sequential data fetching[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-and-sequential-data-fetching)
When fetching data inside React components, you need to be aware of two data fetching patterns: Parallel and Sequential.
![Sequential and Parallel Data Fetching](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fsequential-parallel-data-fetching.png&w=3840&q=75)![Sequential and Parallel Data Fetching](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fsequential-parallel-data-fetching.png&w=3840&q=75)
  * With **sequential data fetching** , requests in a route are dependent on each other and therefore create waterfalls. There may be cases where you want this pattern because one fetch depends on the result of the other, or you want a condition to be satisfied before the next fetch to save resources. However, this behavior can also be unintentional and lead to longer loading times.
  * With **parallel data fetching** , requests in a route are eagerly initiated and will load data at the same time. This reduces client-server waterfalls and the total time it takes to load data.


### Sequential Data Fetching[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#sequential-data-fetching)
If you have nested components, and each component fetches its own data, then data fetching will happen sequentially if those data requests are different (this doesn't apply to requests for the same data as they are automatically [memoized](https://nextjs.org/docs/14/app/building-your-application/caching#request-memoization)).
For example, the `Playlists` component will only start fetching data once the `Artist` component has finished fetching data because `Playlists` depends on the `artistID` prop:
app/artist/[username]/page.tsx
TypeScript
JavaScript TypeScript

```
// ...
 
async function Playlists({ artistID }: { artistID: string }) {
  // Wait for the playlists
  const playlists = await getArtistPlaylists(artistID)
 
  return (
    <ul>
      {playlists.map((playlist) => (
        <li key={playlist.id}>{playlist.name}</li>
      ))}
    </ul>
  )
}
 
export default async function Page({
  params: { username },
}: {
  params: { username: string }
}) {
  // Wait for the artist
  const artist = await getArtist(username)
 
  return (
    <>
      <h1>{artist.name}</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <Playlists artistID={artist.id} />
      </Suspense>
    </>
  )
}
```

In cases like this, you can use [`loading.js`](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming) (for route segments) or [React `<Suspense>`](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming#streaming-with-suspense) (for nested components) to show an instant loading state while React streams in the result.
This will prevent the whole route from being blocked by data fetching, and the user will be able to interact with the parts of the page that are not blocked.
> **Blocking Data Requests:**
> An alternative approach to prevent waterfalls is to fetch data globally, at the root of your application, but this will block rendering for all route segments beneath it until the data has finished loading. This can be described as "all or nothing" data fetching. Either you have the entire data for your page or application, or none.
> Any fetch requests with `await` will block rendering and data fetching for the entire tree beneath it, unless they are wrapped in a `<Suspense>` boundary or `loading.js` is used. Another alternative is to use [parallel data fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-data-fetching) or the [preload pattern](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#preloading-data).
### Parallel Data Fetching[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-data-fetching)
To fetch data in parallel, you can eagerly initiate requests by defining them outside the components that use the data, then calling them from inside the component. This saves time by initiating both requests in parallel, however, the user won't see the rendered result until both promises are resolved.
In the example below, the `getArtist` and `getArtistAlbums` functions are defined outside the `Page` component, then called inside the component, and we wait for both promises to resolve:
app/artist/[username]/page.tsx
TypeScript
JavaScript TypeScript

```
import Albums from './albums'
 
async function getArtist(username: string) {
  const res = await fetch(`https://api.example.com/artist/${username}`)
  return res.json()
}
 
async function getArtistAlbums(username: string) {
  const res = await fetch(`https://api.example.com/artist/${username}/albums`)
  return res.json()
}
 
export default async function Page({
  params: { username },
}: {
  params: { username: string }
}) {
  // Initiate both requests in parallel
  const artistData = getArtist(username)
  const albumsData = getArtistAlbums(username)
 
  // Wait for the promises to resolve
  const [artist, albums] = await Promise.all([artistData, albumsData])
 
  return (
    <>
      <h1>{artist.name}</h1>
      <Albums list={albums}></Albums>
    </>
  )
}
```

To improve the user experience, you can add a [Suspense Boundary](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming) to break up the rendering work and show part of the result as soon as possible.
## Preloading Data[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#preloading-data)
Another way to prevent waterfalls is to use the preload pattern. You can optionally create a `preload` function to further optimize parallel data fetching. With this approach, you don't have to pass promises down as props. The `preload` function can also have any name as it's a pattern, not an API.
components/Item.tsx
TypeScript
JavaScript TypeScript

```
import { getItem } from '@/utils/get-item'
 
export const preload = (id: string) => {
  // void evaluates the given expression and returns undefined
  // https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/void
  void getItem(id)
}
export default async function Item({ id }: { id: string }) {
  const result = await getItem(id)
  // ...
}
```

app/item/[id]/page.tsx
TypeScript
JavaScript TypeScript

```
import Item, { preload, checkIsAvailable } from '@/components/Item'
 
export default async function Page({
  params: { id },
}: {
  params: { id: string }
}) {
  // starting loading item data
  preload(id)
  // perform another asynchronous task
  const isAvailable = await checkIsAvailable()
 
  return isAvailable ? <Item id={id} /> : null
}
```

### Using React `cache`, `server-only`, and the Preload Pattern[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#using-react-cache-server-only-and-the-preload-pattern)
You can combine the `cache` function, the `preload` pattern, and the `server-only` package to create a data fetching utility that can be used throughout your app.
utils/get-item.ts
TypeScript
JavaScript TypeScript

```
import { cache } from 'react'
import 'server-only'
 
export const preload = (id: string) => {
  void getItem(id)
}
 
export const getItem = cache(async (id: string) => {
  // ...
})
```

With this approach, you can eagerly fetch data, cache responses, and guarantee that this data fetching [only happens on the server](https://nextjs.org/docs/14/app/building-your-application/rendering/composition-patterns#keeping-server-only-code-out-of-the-client-environment).
The `utils/get-item` exports can be used by Layouts, Pages, or other components to give them control over when an item's data is fetched.
> **Good to know:**
>   * We recommend using the [`server-only` package](https://nextjs.org/docs/14/app/building-your-application/rendering/composition-patterns#keeping-server-only-code-out-of-the-client-environment) to make sure server data fetching functions are never used on the client.
> 

## Preventing sensitive data from being exposed to the client[](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#preventing-sensitive-data-from-being-exposed-to-the-client)
We recommend using React's taint APIs, [`taintObjectReference`](https://react.dev/reference/react/experimental_taintObjectReference) and [`taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue), to prevent whole object instances or sensitive values from being passed to the client.
To enable tainting in your application, set the Next.js Config `experimental.taint` option to `true`:
next.config.js

```
module.exports = {
  experimental: {
    taint: true,
  },
}
```

Then pass the object or value you want to taint to the `experimental_taintObjectReference` or `experimental_taintUniqueValue` functions:
app/utils.ts
TypeScript
JavaScript TypeScript

```
import { queryDataFromDB } from './api'
import {
  experimental_taintObjectReference,
  experimental_taintUniqueValue,
} from 'react'
 
export async function getUserData() {
  const data = await queryDataFromDB()
  experimental_taintObjectReference(
    'Do not pass the whole user object to the client',
    data
  )
  experimental_taintUniqueValue(
    "Do not pass the user's phone number to the client",
    data,
    data.phoneNumber
  )
  return data
}
```

app/page.tsx
TypeScript
JavaScript TypeScript

```
import { getUserData } from './data'
 
export async function Page() {
  const userData = getUserData()
  return (
    <ClientComponent
      user={userData} // this will cause an error because of taintObjectReference
      phoneNumber={userData.phoneNumber} // this will cause an error because of taintUniqueValue
    />
  )
}
```

Learn more about [Security and Server Actions](https://nextjs.org/blog/security-nextjs-server-components-actions).
[PreviousServer Actions and Mutations](https://nextjs.org/docs/14/app/building-your-application/data-fetching/server-actions-and-mutations)[NextRendering](https://nextjs.org/docs/14/app/building-your-application/rendering)
Was this helpful?
Send
[](https://vercel.com/home?utm_source=next-site&utm_medium=footer&utm_campaign=next-website "Go to the Vercel website")
[![](https://nextjs.org/_next/static/immutable/media/logo-github-light.0j2vz9_zw2uex.svg)![](https://nextjs.org/_next/static/immutable/media/logo-github-dark.3cps0n_-l5sia.svg)](https://github.com/vercel/next.js)
* * *
[![](https://nextjs.org/_next/static/immutable/media/logo-twitter-x-light.3lfl0ys_vh_gz.svg)![](https://nextjs.org/_next/static/immutable/media/logo-twitter-x-dark.2ms8a02663zmn.svg)](https://x.com/nextjs)
* * *
[![](https://nextjs.org/_next/static/immutable/media/logo-bluesky-light.0oj6yf53-gzbh.svg)![](https://nextjs.org/_next/static/immutable/media/logo-bluesky-dark.1vnxp7olsp0zg.svg)](https://bsky.app/profile/nextjs.org)
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Analytics](https://vercel.com/analytics?utm_source=next-site&utm_medium=footer&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns)[Next.js Conf](https://nextjs.org/conf)[Previews](https://vercel.com/products/previews?utm_source=next-site&utm_medium=footer&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns)[Evals](https://nextjs.org/evals)
#### More
[Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce?utm_source=next-site&utm_medium=footer&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns)[Contact Sales](https://vercel.com/contact/sales?utm_source=next-site&utm_medium=footer&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns)[Community](https://community.vercel.com)[GitHub](https://github.com/vercel/next.js)[Releases](https://github.com/vercel/next.js/releases)[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)[Ecosystem Working Group](https://nextjs.org/ecosystem-working-group)
#### About Vercel
[Next.js + Vercel](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=footer&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns)[Open Source Software](https://vercel.com/oss?utm_source=next-site&utm_medium=footer&utm_campaign=docs_14_app_building-your-application_data-fetching_patterns)[GitHub](https://github.com/vercel)[Bluesky](https://bsky.app/profile/vercel.com)[X](https://x.com/vercel)
#### Legal
[Privacy Policy](https://vercel.com/legal/privacy-policy)Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
[![](https://nextjs.org/_next/static/immutable/media/logo-github-light.0j2vz9_zw2uex.svg)![](https://nextjs.org/_next/static/immutable/media/logo-github-dark.3cps0n_-l5sia.svg)](https://github.com/vercel/next.js)
* * *
[![](https://nextjs.org/_next/static/immutable/media/logo-twitter-x-light.3lfl0ys_vh_gz.svg)![](https://nextjs.org/_next/static/immutable/media/logo-twitter-x-dark.2ms8a02663zmn.svg)](https://x.com/nextjs)
* * *
[![](https://nextjs.org/_next/static/immutable/media/logo-bluesky-light.0oj6yf53-gzbh.svg)![](https://nextjs.org/_next/static/immutable/media/logo-bluesky-dark.1vnxp7olsp0zg.svg)](https://bsky.app/profile/nextjs.org)


## Source: https://ztabs.co/blog/nextjs-app-router-best-practices

[Skip to main content](https://ztabs.co/blog/nextjs-app-router-best-practices#main-content)
[ ztabssoftware studio ](https://ztabs.co/)
  * Services
  * Technologies
  * Products
  * Solutions
  * [Work](https://ztabs.co/work)
  * [Blog](https://ztabs.co/blog)


Toggle theme[Contact](https://ztabs.co/contact)[Start Your Project](https://ztabs.co/contact)Toggle Menu
Web Development
# Next.js App Router Best Practices for Production in 2026
Author
[ZTABS Team](https://ztabs.co/authors/ztabs-team)
Date Published
February 11, 2026
  1. [Home](https://ztabs.co/)
  2. [Blog](https://ztabs.co/blog)
  3. Next.js App Router Best Practices for Production in 2026


By **[ZTABS Team](https://ztabs.co/authors/ztabs-team)** Published February 11, 2026Updated March 14, 2026
**TL;DR:** A practical guide to building production Next.js applications with the App Router. Covers server and client components, streaming, parallel routes, server actions, the metadata API, and caching strategies with real code examples.
The [Next.js](https://ztabs.co/technologies/next-js) App Router has become the default architecture for React applications in production. Its server-first model, built-in streaming, and tight integration with React Server Components fundamentally change how you structure, render, and ship web applications.
This guide covers the patterns that matter in production — not toy examples, but the architectural decisions that determine whether your App Router project scales cleanly or collapses under its own complexity.
## Server Components vs Client Components
The most important mental model in the App Router is the server-client boundary. Every component is a Server Component by default. It runs only on the server, has zero JavaScript sent to the browser, and can directly access databases, file systems, and environment variables.

```
// app/dashboard/page.tsx — Server Component (default)
import { db } from "@/lib/database";

export default async function DashboardPage() {
  const metrics = await db.query("SELECT * FROM metrics WHERE date > NOW() - INTERVAL '30 days'");

  return (
    <section>
      <h1>Dashboard</h1>
      <MetricsGrid data={metrics} />
    </section>
  );
}

```

This component fetches data at render time with no `useEffect`, no loading spinners, and no client-side JavaScript. The HTML streams to the browser fully formed.
### When to Use Client Components
Add `"use client"` only when the component genuinely needs the browser. The three triggers are:
  1. **Event handlers** — `onClick`, `onChange`, `onSubmit`
  2. **Browser APIs** — `window`, `localStorage`, `IntersectionObserver`
  3. **React state and effects** — `useState`, `useEffect`, `useRef`


```
"use client";

import { useState } from "react";

interface FilterBarProps {
  categories: string[];
  onFilterChange: (selected: string[]) => void;
}

export function FilterBar({ categories, onFilterChange }: FilterBarProps) {
  const [selected, setSelected] = useState<string[]>([]);

  function toggleCategory(cat: string) {
    const next = selected.includes(cat)
      ? selected.filter((c) => c !== cat)
      : [...selected, cat];
    setSelected(next);
    onFilterChange(next);
  }

  return (
    <div className="flex gap-2 flex-wrap">
      {categories.map((cat) => (
        <button
          key={cat}
          onClick={() => toggleCategory(cat)}
          className={selected.includes(cat) ? "bg-primary text-white" : "bg-muted"}
        >
          {cat}
        </button>
      ))}
    </div>
  );
}

```

### The Composition Pattern
The key architectural insight is that Client Components can render Server Components passed as `children`. This lets you keep the client boundary as small as possible.

```
// app/products/page.tsx — Server Component
import { InteractiveLayout } from "@/components/interactive-layout";
import { ProductList } from "@/components/product-list";

export default async function ProductsPage() {
  return (
    <InteractiveLayout>
      {/* ProductList is a Server Component rendered inside a Client Component */}
      <ProductList />
    </InteractiveLayout>
  );
}

```

```
"use client";

import { useState, type ReactNode } from "react";

export function InteractiveLayout({ children }: { children: ReactNode }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex">
      <aside className={sidebarOpen ? "w-64" : "w-0"}>
        <button onClick={() => setSidebarOpen(!sidebarOpen)}>Toggle</button>
      </aside>
      <main className="flex-1">{children}</main>
    </div>
  );
}

```

## Streaming with Suspense
Streaming is the App Router feature that most dramatically improves perceived performance. Instead of waiting for all data before sending any HTML, the server streams the shell immediately and fills in data-dependent sections as they resolve.

```
// app/dashboard/page.tsx
import { Suspense } from "react";
import { RevenueChart } from "@/components/revenue-chart";
import { RecentOrders } from "@/components/recent-orders";
import { UserActivity } from "@/components/user-activity";
import { ChartSkeleton, TableSkeleton, ActivitySkeleton } from "@/components/skeletons";

export default function DashboardPage() {
  return (
    <div className="grid grid-cols-12 gap-6">
      <div className="col-span-8">
        <Suspense fallback={<ChartSkeleton />}>
          <RevenueChart />
        </Suspense>
      </div>
      <div className="col-span-4">
        <Suspense fallback={<ActivitySkeleton />}>
          <UserActivity />
        </Suspense>
      </div>
      <div className="col-span-12">
        <Suspense fallback={<TableSkeleton />}>
          <RecentOrders />
        </Suspense>
      </div>
    </div>
  );
}

```

Each `<Suspense>` boundary streams independently. If `RevenueChart` takes 2 seconds but `UserActivity` resolves in 200ms, the user sees activity data immediately while the chart skeleton remains visible. No waterfalls. No all-or-nothing loading states.
### Skeleton Design Rules
Good skeletons match the exact dimensions and layout of the content they replace. This prevents layout shift (CLS) and gives users an accurate mental model of what is loading.

```
export function ChartSkeleton() {
  return (
    <div className="h-[400px] w-full rounded-lg bg-muted animate-pulse">
      <div className="p-6">
        <div className="h-6 w-48 bg-muted-foreground/10 rounded" />
        <div className="mt-4 h-[300px] bg-muted-foreground/5 rounded" />
      </div>
    </div>
  );
}

```

## Parallel Routes
Parallel routes let you render multiple pages simultaneously in the same layout. They are defined with the `@` folder convention and are essential for dashboards, modals, and split-view interfaces.

```
app/
  dashboard/
    @analytics/
      page.tsx
      loading.tsx
    @notifications/
      page.tsx
      loading.tsx
    layout.tsx
    page.tsx

```

```
// app/dashboard/layout.tsx
interface DashboardLayoutProps {
  children: React.ReactNode;
  analytics: React.ReactNode;
  notifications: React.ReactNode;
}

export default function DashboardLayout({
  children,
  analytics,
  notifications,
}: DashboardLayoutProps) {
  return (
    <div className="grid grid-cols-12 gap-6">
      <div className="col-span-8">{children}</div>
      <div className="col-span-4 space-y-6">
        {analytics}
        {notifications}
      </div>
    </div>
  );
}

```

Each slot loads independently with its own `loading.tsx`, error boundary, and data dependencies. If the analytics slot fails, notifications still render. This is compositional resilience — each piece of the UI is isolated.
### Intercepting Routes for Modals
Parallel routes combine with intercepting routes to build modals that work with both client-side navigation and direct URL access.

```
app/
  photos/
    [id]/
      page.tsx          ← Full page view (direct URL or hard refresh)
    @modal/
      (.)[id]/
        page.tsx        ← Modal view (client-side navigation)
      default.tsx
    layout.tsx

```

```
// app/photos/@modal/(.)([id])/page.tsx
import { Modal } from "@/components/modal";
import { PhotoDetail } from "@/components/photo-detail";

export default function PhotoModal({ params }: { params: { id: string } }) {
  return (
    <Modal>
      <PhotoDetail id={params.id} />
    </Modal>
  );
}

```

Clicking a photo thumbnail opens a modal overlay. Sharing the URL or refreshing the page renders the full-page view. Same data, two presentation modes, zero code duplication for the data layer.
## Server Actions
Server Actions replace API routes for mutations. They are async functions that run on the server and can be called directly from Client Components or used as form actions.

```
// app/actions/contact.ts
"use server";

import { z } from "zod";
import { db } from "@/lib/database";
import { revalidatePath } from "next/cache";

const contactSchema = z.object({
  name: z.string().min(2).max(100),
  email: z.string().email(),
  message: z.string().min(10).max(5000),
});

export async function submitContactForm(formData: FormData) {
  const parsed = contactSchema.safeParse({
    name: formData.get("name"),
    email: formData.get("email"),
    message: formData.get("message"),
  });

  if (!parsed.success) {
    return { error: parsed.error.flatten().fieldErrors };
  }

  await db.insert("contacts", parsed.data);
  revalidatePath("/contact");

  return { success: true };
}

```

```
"use client";

import { useActionState } from "react";
import { submitContactForm } from "@/app/actions/contact";

export function ContactForm() {
  const [state, formAction, isPending] = useActionState(submitContactForm, null);

  return (
    <form action={formAction} className="space-y-4">
      <input name="name" placeholder="Your name" required className="input" />
      <input name="email" type="email" placeholder="Email" required className="input" />
      <textarea name="message" placeholder="Message" required className="textarea" />
      {state?.error && (
        <p className="text-destructive text-sm">Please fix the errors above.</p>
      )}
      <button type="submit" disabled={isPending} className="btn btn-primary">
        {isPending ? "Sending..." : "Send Message"}
      </button>
    </form>
  );
}

```

Server Actions are progressively enhanced. The form works without JavaScript — it submits as a standard HTML form and the server action processes it. When JavaScript is available, the submission is seamless with optimistic UI updates.
## The Metadata API
The App Router provides a typed, composable metadata API that replaces manual `<head>` management. Metadata can be static or dynamic, and it merges down the route hierarchy.

```
// app/layout.tsx — Global defaults
import type { Metadata } from "next";

export const metadata: Metadata = {
  metadataBase: new URL("https://example.com"),
  title: {
    template: "%s | Acme Corp",
    default: "Acme Corp — Build Better Software",
  },
  description: "Enterprise software development and consulting.",
  openGraph: {
    type: "website",
    locale: "en_US",
    siteName: "Acme Corp",
  },
};

```

```
// app/blog/[slug]/page.tsx — Dynamic metadata per page
import type { Metadata } from "next";
import { getPost } from "@/lib/blog";

interface BlogPostPageProps {
  params: { slug: string };
}

export async function generateMetadata({ params }: BlogPostPageProps): Promise<Metadata> {
  const post = await getPost(params.slug);

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      type: "article",
      publishedTime: post.publishedAt,
      authors: post.authors,
    },
    alternates: {
      canonical: `/blog/${params.slug}`,
    },
  };
}

export default async function BlogPostPage({ params }: BlogPostPageProps) {
  const post = await getPost(params.slug);
  return <article>{/* render post */}</article>;
}

```

The `generateMetadata` function runs on the server and is deduplicated with the page data fetch — Next.js ensures the `getPost` call is only made once even though both `generateMetadata` and the page component call it.
## Caching Strategies
Caching in the App Router operates at four layers, and understanding each is essential for production performance.
### 1. Request Memoization
React automatically deduplicates `fetch` calls with the same URL and options within a single render pass. This means you can call the same data function in `generateMetadata` and the page component without triggering duplicate requests.
### 2. Data Cache
By default, `fetch` responses are cached in the Data Cache indefinitely. You control revalidation with time-based or on-demand strategies.

```
// Time-based revalidation — refresh every 60 seconds
const data = await fetch("https://api.example.com/products", {
  next: { revalidate: 60 },
});

// On-demand revalidation — revalidate when data changes
import { revalidateTag } from "next/cache";

const data = await fetch("https://api.example.com/products", {
  next: { tags: ["products"] },
});

// In a Server Action after a mutation:
revalidateTag("products");

```

### 3. Full Route Cache
Static routes are rendered at build time and served from the edge. Dynamic routes (those using `cookies()`, `headers()`, or uncached data) are rendered on each request.

```
// Force a route to be dynamic
export const dynamic = "force-dynamic";

// Force a route to be static with ISR
export const revalidate = 3600; // Revalidate every hour

```

### 4. Router Cache
The client-side router caches visited routes in memory. Navigating back to a previously visited page is instant because the RSC payload is cached on the client.
## Error Handling at Scale
The App Router provides granular error handling through `error.tsx` files at every route segment.

```
"use client";

interface ErrorBoundaryProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function DashboardError({ error, reset }: ErrorBoundaryProps) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px] gap-4">
      <h2 className="text-xl font-semibold">Something went wrong</h2>
      <p className="text-muted-foreground">
        {error.digest
          ? "An unexpected error occurred. Our team has been notified."
          : error.message}
      </p>
      <button onClick={reset} className="btn btn-primary">
        Try Again
      </button>
    </div>
  );
}

```

Place `error.tsx` files at the most specific route segment possible. A dashboard with three parallel slots should have error boundaries in each slot, not a single boundary at the layout level. This ensures one failing section does not take down the entire page.
## Production Checklist
Before shipping an App Router application to production, verify these patterns are in place:
  * **Minimize client components.** Audit every `"use client"` directive. If a component only renders data without interactivity, it should be a Server Component.
  * **Suspense boundaries at data boundaries.** Every async data dependency should be wrapped in its own Suspense boundary with a dimensionally-accurate skeleton.
  * **Validate Server Actions.** Every Server Action must validate its inputs. Use Zod schemas and return typed error objects.
  * **Set revalidation strategies.** Every `fetch` call should have an explicit `revalidate` value or tag. Do not rely on defaults changing between Next.js versions.
  * **Use`generateStaticParams` for known routes.** Pre-render blog posts, product pages, and documentation at build time.
  * **Test with JavaScript disabled.** Server Actions with forms should work without client-side JavaScript.
  * **Monitor Core Web Vitals.** Use the Next.js Speed Insights package to track LCP, CLS, and INP in production.


## Build With Confidence
The App Router is not just a routing library — it is an architecture for building fast, resilient, and maintainable web applications. The patterns above represent thousands of hours of production experience distilled into actionable guidance.
If you are planning a new Next.js application, [comparing Next.js vs Nuxt](https://ztabs.co/compare/next-js-vs-nuxt) for your project, migrating from the Pages Router, or need help optimizing an existing App Router project for performance and scalability, [reach out to our team](https://ztabs.co/contact). We build Next.js applications that ship fast and stay fast — from initial architecture through to production monitoring and iteration.
Start with server components. Stream everything. Validate at every boundary.
## Frequently Asked Questions
### Should I migrate an existing Pages Router app to App Router?
Only migrate if you need streaming, React Server Components, or partial prerendering — not for the sake of being current. Pages Router is still fully supported and runs side-by-side with App Router in the same app. A typical migration on a 50-page app takes 3-6 weeks of engineering time.
### How much do Server Components actually reduce JavaScript bundle size?
In real audits, moving data-fetching components from client to server cuts client-side JS by 30-60% depending on how dependency-heavy your fetch layer is. A dashboard with charts, date pickers, and data grids often drops from 400KB to 150KB first-load JS. Interactive leaves still ship as client components.
### What's the gotcha with fetch caching in App Router?
Next.js aggressively caches fetch requests by default, which silently breaks dashboards that expect fresh data. You need to pass `cache: 'no-store'` or `next: { revalidate: 0 }` on any request that must be dynamic. This single issue causes the majority of "my data is stale" bug reports in App Router apps.
### When does App Router underperform Pages Router?
Small marketing sites with mostly static content see no benefit and occasionally slower builds because of the heavier RSC bundler work. Sites under 20 pages with no auth or personalization are often better served by static export or Pages Router until they grow.
### Explore Related Solutions
[ Web Development Modern web applications built with cutting-edge tech. ](https://ztabs.co/services/web-development)[ For Startups From MVP to scale — startup development. ](https://ztabs.co/startups)
### Need Help Building Your Project?
From web apps and mobile apps to AI solutions and SaaS platforms — we ship production software for 300+ clients.
[Get a Free Consultation](https://ztabs.co/contact)[View Our Services](https://ztabs.co/services)
### Related Articles
[10 min readWeb Performance Optimization in 2026: A Complete Guide to Core Web Vitals A hands-on guide to web performance optimization in 2026. Covers Core Web Vitals (LCP, CLS, INP), image optimization, code splitting, font loading, and measurable strategies to ship faster sites.](https://ztabs.co/blog/web-performance-optimization-2026)[16 min readTypeScript Design Patterns: A Practical Guide for 2026 A hands-on guide to implementing design patterns in TypeScript. Covers factory, observer, strategy, decorator, and builder patterns with real-world code examples and guidance on when each pattern solves a genuine problem.](https://ztabs.co/blog/typescript-design-patterns-guide)[14 min readTesting Strategies for Modern Web Apps: Vitest, Playwright, and Beyond A practical guide to testing modern web applications. Covers unit, integration, and E2E testing with Vitest, Playwright, and Testing Library. Includes the test pyramid, coverage strategies, and CI integration.](https://ztabs.co/blog/testing-strategies-for-modern-apps)
#### Newsletter
Get notified when we publish something new, and unsubscribe at any time.
We respect your privacy. No spam.
Subscribe
### Subscribe to our newsletter
Stay updated with our latest news and articles.
Subscribe
#### [Services](https://ztabs.co/services)
  * [AI Development](https://ztabs.co/services/ai-development)
  * [AI Agent Development](https://ztabs.co/services/ai-agent-development)
  * [AI Consulting](https://ztabs.co/services/ai-consulting)
  * [AI SaaS Development](https://ztabs.co/services/ai-saas-development)
  * [RAG & Knowledge Systems](https://ztabs.co/services/rag-development)
  * [Workflow Automation](https://ztabs.co/services/workflow-automation)
  * [View All →](https://ztabs.co/services)


#### [Technologies](https://ztabs.co/technologies)
  * [Shopify](https://ztabs.co/technologies/shopify)
  * [Next.js](https://ztabs.co/technologies/next-js)
  * [React Native](https://ztabs.co/technologies/react-native)
  * [Swift](https://ztabs.co/technologies/swift)
  * [Kotlin](https://ztabs.co/technologies/kotlin)


#### [Products](https://ztabs.co/products)
  * [Agiled](https://ztabs.co/products/agiled)
  * [Billed](https://ztabs.co/products/billed)
  * [SchedulingKit](https://ztabs.co/products/schedulingkit)
  * [AgencyPro](https://ztabs.co/products/agencypro)
  * [Chatsy](https://ztabs.co/products/chatsy)
  * [Morphed](https://ztabs.co/products/morphed)
  * [View All →](https://ztabs.co/products)


#### Hire Developers
  * [React Developers](https://ztabs.co/hire/react-developers)
  * [Node.js Developers](https://ztabs.co/hire/node-js-developers)
  * [Python Developers](https://ztabs.co/hire/python-developers)
  * [Full Stack Developers](https://ztabs.co/hire/full-stack-developers)
  * [AI/ML Engineers](https://ztabs.co/hire/ai-ml-engineers)
  * [DevOps Engineers](https://ztabs.co/hire/devops-engineers)


#### Solutions
  * [AI Development](https://ztabs.co/ai)
  * [SaaS Development](https://ztabs.co/saas)
  * [E-commerce](https://ztabs.co/ecommerce)
  * [Mobile Apps](https://ztabs.co/mobile)
  * [Cloud & DevOps](https://ztabs.co/cloud)
  * [For Startups](https://ztabs.co/startups)


#### Resources
  * [Compare Technologies](https://ztabs.co/compare)
  * [Cost Guides](https://ztabs.co/cost)
  * [Statistics & Data](https://ztabs.co/statistics)
  * [RSS Feed](https://ztabs.co/feed.xml)


#### Industries
  * [Healthcare](https://ztabs.co/industries/healthcare)
  * [Fintech](https://ztabs.co/industries/fintech)
  * [Real Estate](https://ztabs.co/industries/real-estate)
  * [SaaS Companies](https://ztabs.co/industries/saas-companies)
  * [E-commerce & DTC](https://ztabs.co/industries/ecommerce-dtc)
  * [Startups](https://ztabs.co/industries/startups-early-stage)
  * [Education](https://ztabs.co/industries/education)
  * [Restaurants](https://ztabs.co/industries/restaurants-hospitality)
  * [All Industries](https://ztabs.co/industries)


#### Company
  * [About](https://ztabs.co/about)
  * [Work](https://ztabs.co/work)
  * [Blog](https://ztabs.co/blog)
  * [Tools](https://ztabs.co/tools)
  * [Hire Developers](https://ztabs.co/hire)
  * [Contact](https://ztabs.co/contact)


#### Legal
  * [Privacy Policy](https://ztabs.co/privacy)
  * [Terms of Service](https://ztabs.co/terms)


[ ztabssoftware studio ](https://ztabs.co/)
© 2026 ZTABS. All rights reserved.
[twitter](https://x.com/ztabsofficial)[linkedin](https://linkedin.com/company/ztabs)[github](https://github.com/ztabs-official)[facebook](https://www.facebook.com/ztabsofficial/)


## Source: https://feature-sliced.design/vi/blog/nextjs-app-router-guide

[Chuyển đến nội dung chính](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#__docusaurus_skipToContent_fallback)
[ ![Logo](https://feature-sliced.design/vi/img/brand/logo-primary.png)![Logo](https://feature-sliced.design/vi/img/brand/logo-primary.png) **FSD**](https://feature-sliced.design/vi/)[📖 Tài liệu](https://feature-sliced.design/vi/docs/get-started/overview)[💫 Cộng đồng](https://feature-sliced.design/vi/community)[📝 Blog](https://feature-sliced.design/vi/blog)[🛠 Ví dụ](https://feature-sliced.design/vi/examples)
[v2.1](https://feature-sliced.design/vi/docs/get-started/overview)
  * [v2.1](https://feature-sliced.design/vi/docs/get-started/overview)
  * [v1.0](https://feature-sliced.design/featureslices.dev/v1.0.html)
  * [v0.1](https://feature-sliced.design/featureslices.dev/v0.1.html)
  * [feature-driven](https://github.com/feature-sliced/documentation/tree/rc/feature-driven)
  * [All versions](https://feature-sliced.design/vi/versions)


[](https://feature-sliced.design/vi/blog/nextjs-app-router-guide)
  * [Русский](https://feature-sliced.design/ru/blog/nextjs-app-router-guide)
  * [English](https://feature-sliced.design/blog/nextjs-app-router-guide)
  * [O'zbekcha](https://feature-sliced.design/uz/blog/nextjs-app-router-guide)
  * [한국어](https://feature-sliced.design/kr/blog/nextjs-app-router-guide)
  * [日本語](https://feature-sliced.design/ja/blog/nextjs-app-router-guide)
  * [Tiếng Việt](https://feature-sliced.design/vi/blog/nextjs-app-router-guide)
  * [中文](https://feature-sliced.design/zh/blog/nextjs-app-router-guide)
  * [Help Us Translate](https://github.com/feature-sliced/documentation/issues/244)


[](https://discord.gg/S8MzWTUsmp)[](https://github.com/feature-sliced/documentation)
Recent posts
### 2026
  * [The Next Frontier: Progressive Hydration](https://feature-sliced.design/vi/blog/progressive-hydration-explained)
  * [The Architect's Guide to Frontend Theming](https://feature-sliced.design/vi/blog/frontend-theming-patterns)
  * [Partial Hydration: The End of Slow Websites](https://feature-sliced.design/vi/blog/islands-architecture-hydration)
  * [Atomic CSS: The Most Performant Architecture?](https://feature-sliced.design/vi/blog/incremental-static-regeneration)
  * [BEM: A Timeless CSS Architecture for Components](https://feature-sliced.design/vi/blog/bem-css-architecture-guide)


# The Ultimate Next.js App Router Architecture
23 tháng 1, 2026 · 1 phút đọc 
![Evan Carter](https://feature-sliced.design/vi/img/brand/evan-carter.png)
Evan Carter
Senior frontend
TLDR:
![The Ultimate Next.js App Router Architecture](https://feature-sliced.design/vi/img/blog/nextjs-app-architecture.jpg)
This in-depth guide explores how to build a scalable and maintainable Next.js App Router architecture using React Server Components, modern data fetching, caching strategies, and Feature-Sliced Design, helping teams avoid technical debt and scale confidently in production.
Nextjs projects often start clean and end up as a tangled mix of Server Components, client-only islands, ad-hoc folders, and unpredictable caching. Feature-Sliced Design (FSD) on feature-sliced.design offers a modern, battle-tested way to keep the App Router, React Server Components, and data fetching cohesive as your codebase scales—without sacrificing performance, cohesion, or team autonomy.
## Why App Router Architecture Is the First Problem You Must Solve[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#why-app-router-architecture-is-the-first-problem-you-must-solve "Link trực tiếp đến heading")
![App Router Pattern](https://feature-sliced.design/vi/img/blog/app-router-pattern.webp)
A key principle in software engineering is that **structure is a performance feature** —not just for runtime, but for teams. Next.js App Router makes it easy to ship fast, but it also introduces new architectural pressure points:
  * **Two execution worlds:** Server Components and Client Components coexist, and the boundary matters for security, bundle size, and coupling.
  * **New routing primitives:** layouts, nested routes, loading/error boundaries, and route groups create powerful composition—and new ways to accidentally leak dependencies.
  * **Caching is now “part of the code”:** the default caching, revalidation, and invalidation APIs influence correctness as much as they influence speed. 
oaicite:0
  * **Deployment realities:** Vercel’s platform features and Next.js cache behavior shape how you design ISR, previews, and mutation flows in production. 
oaicite:1


If you do not plan for these constraints, you get the usual symptoms: spaghetti code, fat “utils”, global providers that quietly couple everything, slow onboarding, and refactors that break unrelated routes.
The goal of “The Ultimate Next.js App Router Architecture” is not to invent new patterns. It’s to combine proven architectural principles—**cohesion, low coupling, explicit public APIs, isolation, and unidirectional dependency flow** —with what App Router actually is: a server-first, streaming-by-default React architecture.
## The App Router Mental Model: Routing Is Composition, Not “Pages”[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-app-router-mental-model-routing-is-composition-not-pages "Link trực tiếp đến heading")
App Router is best understood as a **composition tree** :
  * **Segments** build a route hierarchy.
  * **Layouts** compose shared UI and shared server logic for a subtree.
  * **Pages** finalize a segment’s UI.
  * **loading.tsx / error.tsx** define boundaries.
  * **Route Handlers** define HTTP endpoints within the same routing model. 
oaicite:2


The architecture you want should align with that shape:
  1. **Keep route composition thin.** Routes should assemble features and widgets, not implement domain logic.
  2. **Keep business logic close to business concepts.** Put complexity where it belongs: in features and entities, not in layouts or route files.
  3. **Treat boundaries as contracts.** Server/Client boundaries, module boundaries, and public APIs should be explicit and stable.


This is exactly where Feature-Sliced Design fits: it gives you a **hierarchy of responsibility** (layers) and a **scale-friendly decomposition** (slices) that map cleanly onto App Router’s composition style.
## App Router vs Pages Router: What Actually Changes for Architecture[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#app-router-vs-pages-router-what-actually-changes-for-architecture "Link trực tiếp đến heading")
![Pages Router vs App Router Comparison](https://feature-sliced.design/vi/img/blog/page-vs-app-router.png)
Many teams treat “App Router vs Pages Router” as a routing upgrade. Architecturally, it’s a platform shift.
### Execution model and data fetching[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#execution-model-and-data-fetching "Link trực tiếp đến heading")
**Pages Router** encourages a request/response mindset with explicit data functions (like server-side props patterns) and client-driven interactivity. **App Router** shifts you toward:
  * **React Server Components** for server-first UI and data reads. 
oaicite:3
  * **Streaming** and partial rendering by default (especially with loading boundaries).
  * **Granular caching controls** across renders and fetches. 
oaicite:4


### API design[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#api-design "Link trực tiếp đến heading")
With Pages Router, many teams centralize server logic behind API routes and call them from the client. With App Router, you now have more options:
  * **Route Handlers** (HTTP endpoints) in `app/**/route.ts`. 
oaicite:5
  * **Server Actions** (server functions invoked from components/forms) for many mutation paths. 
oaicite:6


This is not merely convenience. It changes coupling:
  * Overusing Route Handlers can create a “mini-backend inside the frontend” with leaky DTOs.
  * Overusing Server Actions can lead to hidden side effects and accidental cross-feature dependencies if you don’t design boundaries.


### Caching and invalidation become architecture[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#caching-and-invalidation-become-architecture "Link trực tiếp đến heading")
In Pages Router, caching is often “HTTP headers + CDN + ISR”. In App Router, caching is deeper:
  * What you fetch, how you tag it, how you revalidate it, and where you cache it will shape correctness. 
oaicite:7
  * Next.js now offers “getting started” and “deep dive” guidance emphasizing caching layers and invalidation APIs as first-class tools. 
oaicite:8


If you want an architecture that scales, you must plan for cache boundaries the same way you plan for module boundaries.
## The Core Architectural Challenge: Keep Server-First Power Without Global Coupling[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-core-architectural-challenge-keep-server-first-power-without-global-coupling "Link trực tiếp đến heading")
A robust methodology for App Router must answer five questions:
  1. **Where does domain logic live?**
  2. **How do routes compose features without importing internals?**
  3. **Where do Server Components stop and Client Components start?**
  4. **How do we fetch data predictably and revalidate safely?**
  5. **How do we deploy and operate this on Vercel without surprises?**


Let’s compare common approaches and why they often fail in Next.js at scale.
## Common Frontend Architecture Approaches and Their Limits in Next.js[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#common-frontend-architecture-approaches-and-their-limits-in-nextjs "Link trực tiếp đến heading")
### Layered architecture (MVC, MVP, MVVM)[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#layered-architecture-mvc-mvp-mvvm "Link trực tiếp đến heading")
Layered patterns separate concerns by technical type. They are valuable, but in modern Next.js they often degrade into:
  * `components/`, `hooks/`, `services/`, `utils/` as global buckets.
  * UI concerns leaking into data code and vice versa.
  * “Shared service layer” becoming a dependency magnet (high fan-in, low cohesion).


This structure can be readable early, but it tends to create **implicit coupling** because nothing stops unrelated features from importing each other’s internals.
### Component-based architecture and Atomic Design[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#component-based-architecture-and-atomic-design "Link trực tiếp đến heading")
Atomic Design is excellent for design systems and consistent UI composition. But it does not answer:
  * Where do “user scenarios” live (e.g., add-to-cart, login, follow user)?
  * Where does domain model code live?
  * How do you prevent cross-feature imports?
  * How do you structure server vs client boundaries?


In App Router, you can build a beautiful component tree and still end up with fragile data flows and untestable business logic.
### Domain-Driven Design (DDD) on the frontend[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#domain-driven-design-ddd-on-the-frontend "Link trực tiếp đến heading")
DDD aligns structure to business concepts and bounded contexts. That’s a strong direction, but many frontend DDD attempts lack:
  * A clear dependency rule (what can depend on what).
  * A consistent layer system for shared UI, domain entities, and feature scenarios.
  * A pragmatic implementation style for UI-heavy codebases.


### Feature-Sliced Design (FSD) as the missing scaling layer[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#feature-sliced-design-fsd-as-the-missing-scaling-layer "Link trực tiếp đến heading")
Feature-Sliced Design is a modern blueprint for modularity:
  * Organize by **business relevance** (features and entities), not only by technical type.
  * Enforce **unidirectional dependency flow** via layers.
  * Make module boundaries explicit using a **public API**.


This fits Next.js App Router because routes are composition nodes and FSD specializes in composition by responsibility.
## Comparative Table: MVC vs Atomic Design vs FSD (Why FSD Fits App Router)[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#comparative-table-mvc-vs-atomic-design-vs-fsd-why-fsd-fits-app-router "Link trực tiếp đến heading")  
| Methodology  | What it optimizes  | What breaks first in App Router  |  
| --- | --- | --- |  
| MVC / MVVM  | Separation by technical role  | Global “service” gravity, coupling through shared layers  |  
| Atomic Design  | UI consistency and design systems  | No guidance for domain logic, data fetching, or feature boundaries  |  
| Feature-Sliced Design  | Modularity by business scope + strict dependency direction  | Requires discipline: public APIs, layer rules, and slice ownership  |  
The takeaway is pragmatic: keep what works (component decomposition, clear UI primitives), but add what you need to scale (feature boundaries and dependency rules).
## The Ultimate Next.js App Router Architecture with Feature-Sliced Design[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-ultimate-nextjs-app-router-architecture-with-feature-sliced-design "Link trực tiếp đến heading")
This section gives you a concrete structure you can apply today.
### The layers (FSD) mapped to Next.js App Router[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-layers-fsd-mapped-to-nextjs-app-router "Link trực tiếp đến heading")
FSD layers (from highest to lowest):
  * **app** : application initialization and global providers (composition root)
  * **pages** : route-level composition (per segment/page)
  * **widgets** : large UI blocks composed from features/entities
  * **features** : user interaction scenarios (business actions)
  * **entities** : domain models and domain UI (core business concepts)
  * **shared** : reusable, business-agnostic code (UI kit, utilities, config)


In App Router terms:
  * `app/` directory becomes the **routing runtime** , but your business code should live in `src/` FSD layers.
  * Your route files should import from **pages** and below, never from deep internals.


A common and effective setup is:
  * Use Next.js `app/` for routing only.
  * Use `src/` for the product architecture (FSD layers).


### A concrete directory structure[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#a-concrete-directory-structure "Link trực tiếp đến heading")
Below is a practical structure that keeps the App Router clean while allowing FSD to scale: app/ (public)/ layout.tsx page.tsx (auth)/ login/ page.tsx register/ page.tsx api/ webhooks/ route.ts _providers/ Providers.tsx layout.tsx error.tsx not-found.tsx loading.tsx
src/ app/ providers/ index.ts ui/ AppShell.tsx routing/ link.ts pages/ home/ ui/ HomePage.tsx index.ts login/ ui/ LoginPage.tsx index.ts widgets/ header/ ui/ Header.tsx index.ts product-grid/ ui/ ProductGrid.tsx index.ts features/ auth/ login/ ui/ LoginForm.tsx model/ login.schema.ts useLogin.ts api/ login.action.ts index.ts cart/ add-to-cart/ ui/ AddToCartButton.tsx model/ useAddToCart.ts api/ addToCart.action.ts index.ts entities/ user/ model/ types.ts session.ts ui/ UserAvatar.tsx index.ts product/ model/ types.ts api/ product.queries.ts ui/ ProductCard.tsx index.ts shared/ ui/ button/ Button.tsx input/ Input.tsx lib/ fetch/ fetcher.ts cache/ tags.ts config/ env.ts
This arrangement delivers three important benefits:
  * **Routes stay thin** and are easy to reason about.
  * **Features are cohesive** : UI + model + API live together.
  * **Refactors get safer** because you can move slices without chasing imports across the whole repo.


### Public API is non-negotiable[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#public-api-is-non-negotiable "Link trực tiếp đến heading")
To prevent spaghetti code, each slice exposes a stable surface:
  * `features/cart/add-to-cart/index.ts`
  * `entities/product/index.ts`
  * `widgets/header/index.ts`


Inside `index.ts`, export only what consumers should use. Everything else remains internal.
Example pattern (pseudo-code):
  * `features/cart/add-to-cart/index.ts`
    * exports: `AddToCartButton`, `addToCartAction`, maybe `useAddToCart`
    * does not export internal selectors, helper functions, or private types unless needed


This enforces encapsulation, reduces accidental coupling, and improves maintainability.
## Server Components vs Client Components: The Boundary Strategy That Prevents Chaos[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#server-components-vs-client-components-the-boundary-strategy-that-prevents-chaos "Link trực tiếp đến heading")
![Server Components vs Client Components](https://feature-sliced.design/vi/img/blog/client-server-component.jpg)
React Server Components (RSC) are a superpower, but they must be organized. A clean rule:
  * **Server Components own data reads and composition.**
  * **Client Components own interactivity and local UI state.**
  * **Keep client components “leaf-like”.** They should not become composition roots.


### Practical rules[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#practical-rules "Link trực tiếp đến heading")
  1. Default everything to Server Components (no `"use client"` unless needed).
  2. Put `"use client"` components inside **features** and **widgets** when interactivity is required.
  3. Avoid passing server-only objects to client components (e.g., database handles).
  4. Keep client boundaries narrow: pass minimal props, not service objects.


This produces high cohesion: server composition remains stable while interactive islands remain isolated.
### Example: A route composes a server-first page[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#example-a-route-composes-a-server-first-page "Link trực tiếp đến heading")
`app/(public)/page.tsx`:
  * imports `HomePage` from `src/pages/home`
  * does not implement domain logic directly


Pseudo-code:
  * `app/(public)/page.tsx`
    * `return <HomePage />`


`src/pages/home/ui/HomePage.tsx` (Server Component):
  * fetches products
  * composes `Header` and `ProductGrid`


`ProductGrid` might be server (render list) while `AddToCartButton` is client and lives in a feature slice.
## Data Fetching Patterns in App Router That Scale[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#data-fetching-patterns-in-app-router-that-scale "Link trực tiếp đến heading")
Search intent #1 and #3 demand a clear, comprehensive guide to data fetching across Server and Client Components.
### Server-side fetching: your default[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#server-side-fetching-your-default "Link trực tiếp đến heading")
Next.js explicitly supports fetching in Server Components via `fetch`, ORMs, and filesystem I/O. 
oaicite:9
A scalable approach is to keep data access in **entities/** (domain-specific reads) and expose them via a public API.
Example pattern:
  * `entities/product/api/product.queries.ts`
    * `getProductById(id)`
    * `listProducts(filters)`


The **page** imports these queries (or a feature-level “use case” function) and renders.
This avoids a “global services” bucket and keeps queries close to the domain model.
### Client-side fetching: when you truly need it[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#client-side-fetching-when-you-truly-need-it "Link trực tiếp đến heading")
Client fetching is appropriate when:
  * You need live updates independent of navigation.
  * You need user-driven polling or websockets.
  * You need client-only auth context to call an external API.


App Router guidance includes client fetching via Route Handlers as one of the standard paths. 
oaicite:10
In an FSD architecture:
  * Route Handlers live near routing (`app/api/**/route.ts`) or under a dedicated server boundary.
  * Client hooks live in **features/** (because they represent user scenarios).


Avoid building generic “api client” hooks that every slice imports without ownership. Prefer slice-owned hooks that wrap shared primitives.
### Streaming and loading states: turn latency into UX[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#streaming-and-loading-states-turn-latency-into-ux "Link trực tiếp đến heading")
One of the most practical benefits of App Router is streaming with `loading.tsx`. Use it intentionally:
  * Put fast, cacheable data in the server page.
  * Put slow, non-critical data in nested components wrapped by a loading boundary.


Architecturally, streaming works best when your UI is already decomposed into widgets and features—another reason FSD pairs well with App Router.
## Caching and Revalidation: Design It Like a System, Not a Trick[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#caching-and-revalidation-design-it-like-a-system-not-a-trick "Link trực tiếp đến heading")
Search intent #4 is where many “Next.js architectures” get vague. We will not.
Next.js provides multiple caching and revalidation APIs and emphasizes how they interact. 
oaicite:11
The key is to design a predictable strategy that fits your domain.
### The caching goals that matter[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-caching-goals-that-matter "Link trực tiếp đến heading")
  * **Correctness:** users should see accurate data within acceptable freshness bounds.
  * **Performance:** reduce repeated work and backend load.
  * **Operability:** you must be able to invalidate safely on mutations.
  * **Cost control:** caching reduces compute and database usage.


### A simple, robust strategy: tag everything you intend to invalidate[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#a-simple-robust-strategy-tag-everything-you-intend-to-invalidate "Link trực tiếp đến heading")
Next.js supports invalidation via functions like `revalidatePath` and `revalidateTag`. 
oaicite:12
Use this mental model:
  * If data changes because of a mutation, it must have a tag or a clear path invalidation strategy.
  * Prefer tags for domain entities (e.g., `product:123`, `cart:user:42`, `catalog`).
  * Use `revalidateTag` after successful mutations to refresh dependent pages.


A good “tag taxonomy” lives in `shared/lib/cache/tags.ts` and is imported by feature slices that mutate.
Example tag helpers (conceptual):
  * `tagProduct(id) => "product:" + id`
  * `tagCatalog() => "catalog"`
  * `tagUser(id) => "user:" + id`


This is an architectural win: tags become a stable contract between domain changes and UI freshness.
### Server Actions + revalidation: the mutation pipeline[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#server-actions--revalidation-the-mutation-pipeline "Link trực tiếp đến heading")
Many teams now use Server Actions for mutations, especially forms. Next.js documentation positions Server Actions as server-executed async functions usable from Server and Client Components. 
oaicite:13
A scalable pattern:
  1. Feature slice owns the mutation (e.g., `features/cart/add-to-cart/api/addToCart.action.ts`)
  2. Action performs mutation and then revalidates tags/paths relevant to that domain


This aligns responsibility: the slice that changes the data also owns freshness.
### Route Handlers vs Server Actions: when to use which[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#route-handlers-vs-server-actions-when-to-use-which "Link trực tiếp đến heading")
Use **Server Actions** when:
  * The mutation is tied to UI workflows (forms, buttons).
  * You want a direct, typed “call” from UI.
  * You want to keep the API surface internal to the app.


Use **Route Handlers** when:
  * You need a stable HTTP interface (webhooks, third-party callbacks, public API).
  * You need custom request/response handling with Web APIs. 
oaicite:14


A pragmatic rule: internal UI mutations → Server Actions; integration boundaries → Route Handlers.
### Cache Components: mixing static, cached, and dynamic content[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#cache-components-mixing-static-cached-and-dynamic-content "Link trực tiếp đến heading")
Next.js also introduced an opt-in “Cache Components” capability (enabled via a config flag) to mix static, cached, and dynamic content in one route. 
oaicite:15
Architecturally, treat this as a powerful tool—but still keep boundaries:
  * Use it to optimize rendering composition.
  * Keep business rules in features/entities so you don’t create route-level complexity.


## Concrete Example: Product Catalog + Cart in App Router with FSD[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#concrete-example-product-catalog--cart-in-app-router-with-fsd "Link trực tiếp đến heading")
Let’s make the architecture tangible with a common scenario: product list, product detail, add-to-cart, and cart badge in header.
### The slices[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-slices "Link trực tiếp đến heading")
  * `entities/product`: types, product queries, product UI
  * `entities/cart`: types, cart queries
  * `features/cart/add-to-cart`: button, server action, optimistic client state if needed
  * `widgets/header`: renders logo, nav, and cart badge
  * `pages/home`: composes product grid and header
  * `pages/product-details`: composes product view and add-to-cart


### The data flow[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-data-flow "Link trực tiếp đến heading")
  1. `pages/home` (Server Component) calls `entities/product/api/listProducts()`
  2. It renders `widgets/product-grid` which renders `entities/product/ui/ProductCard`
  3. `ProductCard` includes `features/cart/add-to-cart/ui/AddToCartButton` (Client Component)
  4. On click, `AddToCartButton` calls `addToCartAction()` (Server Action)
  5. The action mutates and then triggers `revalidateTag("cart:user:...")` and possibly `revalidateTag("catalog")` depending on business requirements. 
oaicite:16
  6. `widgets/header` (Server Component) reads cart summary and renders the badge


This yields a clean separation:
  * Server reads are colocated with domain entities.
  * Mutations are owned by feature slices.
  * UI composition is done by pages/widgets.
  * Cache invalidation is a first-class, slice-owned concern.


## Architecture Principles for Next.js That Prevent Technical Debt[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#architecture-principles-for-nextjs-that-prevent-technical-debt "Link trực tiếp đến heading")
These principles are stable and apply across Next.js versions.
### 1) High cohesion: keep things that change together together[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#1-high-cohesion-keep-things-that-change-together-together "Link trực tiếp đến heading")
If a feature changes, you should update one slice, not hunt across `components/`, `hooks/`, and `services/`.
FSD naturally encourages cohesion because each feature slice contains UI, model, and API related to that scenario.
### 2) Low coupling: prefer dependency direction over “shared helpers”[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#2-low-coupling-prefer-dependency-direction-over-shared-helpers "Link trực tiếp đến heading")
“Shared” code should be truly generic. If you place domain helpers in `shared/`, you create hidden coupling.
A healthier approach:
  * Domain logic lives in `entities/` and `features/`
  * `shared/` is for primitives (UI kit, small utilities, env config)


### 3) Explicit public API: stop accidental imports[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#3-explicit-public-api-stop-accidental-imports "Link trực tiếp đến heading")
Public APIs turn “anything can import anything” into “imports are contracts”.
This matters more in App Router because server/client boundaries and cache behavior amplify the cost of tangled dependencies.
### 4) Isolation: keep route-level files boring[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#4-isolation-keep-route-level-files-boring "Link trực tiếp đến heading")
Your `app/**/page.tsx` should read like orchestration:
  * import a page component
  * pass params
  * return UI


If routes contain business logic, they become brittle and hard to refactor.
### 5) Observability-friendly design: make cache and data boundaries visible[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#5-observability-friendly-design-make-cache-and-data-boundaries-visible "Link trực tiếp đến heading")
Caching problems are often invisible until production. Your architecture should make it easy to answer:
  * Which tags are invalidated by this mutation?
  * Which route segments depend on this entity?
  * Which components are client-only and why?


When tags, actions, and queries are owned by slices, these answers become obvious.
## Deployment to Vercel: App Router Best Practices That Survive Production[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#deployment-to-vercel-app-router-best-practices-that-survive-production "Link trực tiếp đến heading")
![Deploying a Next.js Project on Vercel](https://feature-sliced.design/vi/img/blog/nextjs-deploying-vercel.png)
Search intent #5 asks for best practices on Vercel. The strong approach is to treat deployment as part of architecture.
### Understand shared caching and ISR behavior[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#understand-shared-caching-and-isr-behavior "Link trực tiếp đến heading")
Next.js documentation explains that caching and revalidating pages (ISR and newer App Router functions) use a shared cache, and default storage differs by hosting model. 
oaicite:17
On Vercel, ISR and edge/CDN behavior also matter, and platform docs highlight how certain preview/draft flows interact with caching. 
oaicite:18
Practical advice:
  * Use ISR and tag invalidation for content that tolerates slight delay.
  * Keep mutation-driven freshness explicit (revalidate tags/paths from the feature that mutates).
  * Treat previews/draft modes as a separate concern with a clear security model.


### Use Route Handlers for integrations, not as your default backend[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#use-route-handlers-for-integrations-not-as-your-default-backend "Link trực tiếp đến heading")
Vercel makes it easy to ship endpoints, but a frontend repo that becomes a sprawling “API project” creates operational risk.
Guidance:
  * Webhooks, OAuth callbacks, and third-party integrations → Route Handlers.
  * UI-driven mutations → Server Actions, owned by feature slices.


This keeps your system understandable and reduces accidental public surface area.
### Production ergonomics: reduce cold-start and over-fetching via structure[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#production-ergonomics-reduce-cold-start-and-over-fetching-via-structure "Link trực tiếp đến heading")
Even if you optimize caching, poor architecture causes repeated work:
  * multiple components fetching the same data with different keys
  * duplicate requests within one render path
  * inconsistent cache tags


A slice-based design helps because queries live in one domain place and are reused intentionally, not accidentally.
## Step-by-Step: Migrating from Pages Router or “Flat Folders” to This Architecture[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#step-by-step-migrating-from-pages-router-or-flat-folders-to-this-architecture "Link trực tiếp đến heading")
This migration plan is designed to be safe and incremental.
  1. **Create`src/` and introduce FSD layers** without moving everything at once.
  2. **Add public APIs** (`index.ts`) for a few key slices.
  3. **Move one domain entity** (e.g., `entities/user`) and update imports.
  4. **Move one user scenario** into a feature slice (e.g., `features/auth/login`).
  5. **Refactor one route** : make `app/**/page.tsx` thin and delegate to `src/pages/**`.
  6. **Introduce cache tag taxonomy** in `shared/lib/cache/tags.ts`.
  7. **Move mutations to Server Actions** where appropriate, and attach revalidation.
  8. **Enforce rules** : add lint rules or tooling to prevent cross-layer imports.


Leading architects suggest that migrations succeed when the target structure is simple, repeatable, and enforced by conventions. FSD gives you that repeatability.
## Final Checklist: What “Ultimate App Router Architecture” Looks Like in Practice[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#final-checklist-what-ultimate-app-router-architecture-looks-like-in-practice "Link trực tiếp đến heading")
You know you’re on track when:
  * Routes are mostly composition and wiring.
  * Features own mutations, revalidation, and client interactivity.
  * Entities own domain reads and domain UI primitives.
  * Shared is small and boring.
  * Public APIs exist for every slice that others import.
  * Server/Client boundaries are narrow and intentional.
  * Cache tags are stable, named, and owned by the domain.


This approach helps to mitigate common challenges: it reduces coupling, increases cohesion, improves onboarding, and makes performance optimization less risky because structure mirrors responsibility.
## Conclusion[​](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#conclusion "Link trực tiếp đến heading")
A scalable Next.js App Router codebase is built on explicit boundaries: Server Components for composition and data reads, Client Components for focused interactivity, and predictable caching with clear invalidation rules. App Router gives you powerful primitives—layouts, streaming, Route Handlers, Server Actions, and revalidation APIs—but without structure, those same primitives can accelerate technical debt. Adopting Feature-Sliced Design is a long-term investment in maintainability and team productivity: it enforces unidirectional dependencies, promotes cohesive feature modules, and makes refactoring safer through public APIs. Ready to build scalable and maintainable frontend projects? Dive into the official **[Feature-Sliced Design Documentation](https://feature-sliced.design/docs/get-started/overview)** to get started. Have questions or want to share your experience? Join our active developer community on **[Website](https://feature-sliced.design/)**!
_Disclaimer: The architectural patterns discussed in this article are based on the Feature-Sliced Design methodology. For detailed implementation guides and the latest updates, please refer to the official documentation._
**Tags:**
  * [react server components](https://feature-sliced.design/vi/blog/tags/react-server-components)
  * [nextjs app router](https://feature-sliced.design/vi/blog/tags/nextjs-app-router)
  * [nextjs pages router](https://feature-sliced.design/vi/blog/tags/nextjs-pages-router)


[](https://github.com/feature-sliced/documentation/edit/master/blog/blog/2026-01-23-nextjs-app-router-guide.md)
[Bài mới hơn esbuild Architecture: How is it So Fast?](https://feature-sliced.design/vi/blog/esbuild-performance-explained)[Bài cũ hơn Rollup.js: The Architect's Choice for Libraries](https://feature-sliced.design/vi/blog/rollup-library-architecture)
  * [Why App Router Architecture Is the First Problem You Must Solve](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#why-app-router-architecture-is-the-first-problem-you-must-solve)
  * [The App Router Mental Model: Routing Is Composition, Not “Pages”](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-app-router-mental-model-routing-is-composition-not-pages)
  * [App Router vs Pages Router: What Actually Changes for Architecture](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#app-router-vs-pages-router-what-actually-changes-for-architecture)
    * [Execution model and data fetching](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#execution-model-and-data-fetching)
    * [API design](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#api-design)
    * [Caching and invalidation become architecture](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#caching-and-invalidation-become-architecture)
  * [The Core Architectural Challenge: Keep Server-First Power Without Global Coupling](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-core-architectural-challenge-keep-server-first-power-without-global-coupling)
  * [Common Frontend Architecture Approaches and Their Limits in Next.js](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#common-frontend-architecture-approaches-and-their-limits-in-nextjs)
    * [Layered architecture (MVC, MVP, MVVM)](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#layered-architecture-mvc-mvp-mvvm)
    * [Component-based architecture and Atomic Design](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#component-based-architecture-and-atomic-design)
    * [Domain-Driven Design (DDD) on the frontend](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#domain-driven-design-ddd-on-the-frontend)
    * [Feature-Sliced Design (FSD) as the missing scaling layer](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#feature-sliced-design-fsd-as-the-missing-scaling-layer)
  * [Comparative Table: MVC vs Atomic Design vs FSD (Why FSD Fits App Router)](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#comparative-table-mvc-vs-atomic-design-vs-fsd-why-fsd-fits-app-router)
  * [The Ultimate Next.js App Router Architecture with Feature-Sliced Design](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-ultimate-nextjs-app-router-architecture-with-feature-sliced-design)
    * [The layers (FSD) mapped to Next.js App Router](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-layers-fsd-mapped-to-nextjs-app-router)
    * [A concrete directory structure](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#a-concrete-directory-structure)
    * [Public API is non-negotiable](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#public-api-is-non-negotiable)
  * [Server Components vs Client Components: The Boundary Strategy That Prevents Chaos](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#server-components-vs-client-components-the-boundary-strategy-that-prevents-chaos)
    * [Practical rules](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#practical-rules)
    * [Example: A route composes a server-first page](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#example-a-route-composes-a-server-first-page)
  * [Data Fetching Patterns in App Router That Scale](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#data-fetching-patterns-in-app-router-that-scale)
    * [Server-side fetching: your default](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#server-side-fetching-your-default)
    * [Client-side fetching: when you truly need it](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#client-side-fetching-when-you-truly-need-it)
    * [Streaming and loading states: turn latency into UX](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#streaming-and-loading-states-turn-latency-into-ux)
  * [Caching and Revalidation: Design It Like a System, Not a Trick](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#caching-and-revalidation-design-it-like-a-system-not-a-trick)
    * [The caching goals that matter](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-caching-goals-that-matter)
    * [A simple, robust strategy: tag everything you intend to invalidate](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#a-simple-robust-strategy-tag-everything-you-intend-to-invalidate)
    * [Server Actions + revalidation: the mutation pipeline](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#server-actions--revalidation-the-mutation-pipeline)
    * [Route Handlers vs Server Actions: when to use which](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#route-handlers-vs-server-actions-when-to-use-which)
    * [Cache Components: mixing static, cached, and dynamic content](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#cache-components-mixing-static-cached-and-dynamic-content)
  * [Concrete Example: Product Catalog + Cart in App Router with FSD](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#concrete-example-product-catalog--cart-in-app-router-with-fsd)
    * [The slices](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-slices)
    * [The data flow](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#the-data-flow)
  * [Architecture Principles for Next.js That Prevent Technical Debt](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#architecture-principles-for-nextjs-that-prevent-technical-debt)
    * [1) High cohesion: keep things that change together together](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#1-high-cohesion-keep-things-that-change-together-together)
    * [2) Low coupling: prefer dependency direction over “shared helpers”](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#2-low-coupling-prefer-dependency-direction-over-shared-helpers)
    * [3) Explicit public API: stop accidental imports](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#3-explicit-public-api-stop-accidental-imports)
    * [4) Isolation: keep route-level files boring](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#4-isolation-keep-route-level-files-boring)
    * [5) Observability-friendly design: make cache and data boundaries visible](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#5-observability-friendly-design-make-cache-and-data-boundaries-visible)
  * [Deployment to Vercel: App Router Best Practices That Survive Production](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#deployment-to-vercel-app-router-best-practices-that-survive-production)
    * [Understand shared caching and ISR behavior](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#understand-shared-caching-and-isr-behavior)
    * [Use Route Handlers for integrations, not as your default backend](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#use-route-handlers-for-integrations-not-as-your-default-backend)
    * [Production ergonomics: reduce cold-start and over-fetching via structure](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#production-ergonomics-reduce-cold-start-and-over-fetching-via-structure)
  * [Step-by-Step: Migrating from Pages Router or “Flat Folders” to This Architecture](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#step-by-step-migrating-from-pages-router-or-flat-folders-to-this-architecture)
  * [Final Checklist: What “Ultimate App Router Architecture” Looks Like in Practice](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#final-checklist-what-ultimate-app-router-architecture-looks-like-in-practice)
  * [Conclusion](https://feature-sliced.design/vi/blog/nextjs-app-router-guide#conclusion)


Specs
  * [Tài liệu](https://feature-sliced.design/vi/docs/get-started/overview)
  * [Cộng đồng](https://feature-sliced.design/vi/community)
  * [Trợ giúp](https://feature-sliced.design/vi/nav)
  * [Thảo luận](https://github.com/feature-sliced/documentation/discussions)


Cộng đồng
  * [Discord](https://discord.gg/S8MzWTUsmp)
  * [Telegram (RU)](https://t.me/feature_sliced)
  * [Twitter](https://twitter.com/feature_sliced)
  * [Open Collective](https://opencollective.com/feature-sliced)
  * [YouTube](https://www.youtube.com/c/FeatureSlicedDesign)


Thêm
  * [GitHub](https://github.com/feature-sliced)
  * [Contribution Guide](https://github.com/feature-sliced/documentation/blob/master/CONTRIBUTING.md)
  * [License](https://github.com/feature-sliced/documentation/blob/master/LICENSE)
  * [Docs for LLMs](https://feature-sliced.design/vi/docs/llms)


[![Feature-Sliced Design - Architectural methodology for frontend projects](https://feature-sliced.design/vi/img/brand/logo-primary.png)![Feature-Sliced Design - Architectural methodology for frontend projects](https://feature-sliced.design/vi/img/brand/logo-primary.png)](https://github.com/feature-sliced)
[trực tiếp bóng đá xôi lạc](https://cultureandyouth.org/)[trực tiếp bóng đá xoilac](https://bachdangco.com/)[xoilac tv](https://sosmap.net/)[xoilac](https://phongkhamago.com/)[trực tiếp bóng đá hôm nay](https://colatv.io/)[truc tiep bong da](https://colatv.pro/)[trực tiếp bóng đá](https://colatv.website/)[cakhia](https://cakhia.org/)[cà khịa tv](https://www.nuukik.com/)[thapcam](https://thapcamtv.cab/)[gavang](https://gavangtv.fun/)[Xôi Lạc Tivi](https://mintconditionmusic.com/)[luongson](https://luongsontv.black/)[tài xỉu](https://taixiu.ae.org/)[b52club](https://b52club.army/)[m88](https://m88.haus/)[8kbet](https://8kbet.org.mx/)[u888](https://u888.org.mx/)[sunwin](https://sunwinn.earth/)[tỷ lệ kèo](https://tylekeo.host/)[tỷ lệ kèo](https://w88.properties/)[kèo bóng đá hôm nay](https://keowin.icu/)[go88](https://go88vie.com/)<https://i9bet.channel/><https://kqbd.in/>[tài xỉu online](https://placeh.io/)[w88 link](https://ipaca.uk.com/)[789club](https://789club.help/)<https://go88.archi/>[Xôi Lạc Link](https://northernlightsccs.com/)[xem trực tiếp Xoilac](https://mashrouleila.com/)[xem bóng đá xoilac](https://ecacolleges.com/)[cà khịa bóng đá](https://cronodon.com/)[Trực tiếp bóng đá 90phut](https://gnrd.net/)<https://www.basket31.tv/>[rikvip](https://rikvip.eu.com/)[Thập Cẩm Tivi](https://robbeewedow.com/)[88go](https://farma5.sa.com/)[VN88 com](https://flirt.ru.com/)
Bản quyền © 2018-2025 Feature-Sliced Design


## Source: https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj

[Skip to content](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#main-content)
Navigation menu [ ![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png) ](https://dev.to/)
Search [ Powered by Algolia Search ](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)
[ Log in ](https://dev.to/enter?signup_subforem=1) [ Create account ](https://dev.to/enter?signup_subforem=1&state=new-user)
## DEV Community
Close
![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg) 11 Add reaction 
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) 3 Like  ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) 2 Unicorn  ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) 2 Exploding Head  ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) 2 Raised Hands  ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg) 2 Fire 
0 Jump to Comments  0 Save  Boost 
More...
Copy link Copy link
Copied to Clipboard
[ Share to X ](https://twitter.com/intent/tweet?text=%22Architecting%20Large-Scale%20Next.js%20Applications%20%28Folder%20Structure%2C%20Patterns%2C%20Best%20Practices%29%22%20by%20Mayank%20Goyal%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Faddwebsolutionpvtltd%2Farchitecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj) [ Share to LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Faddwebsolutionpvtltd%2Farchitecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj&title=Architecting%20Large-Scale%20Next.js%20Applications%20%28Folder%20Structure%2C%20Patterns%2C%20Best%20Practices%29&summary=%E2%80%9CGood%20architecture%20makes%20the%20system%20easy%20to%20understand%3B%20great%20architecture%20makes%20it%20hard%20to...&source=DEV%20Community) [ Share to Facebook ](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Faddwebsolutionpvtltd%2Farchitecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj) [ Share to Mastodon ](https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2Faddwebsolutionpvtltd%2Farchitecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj)
[Share Post via...](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj) [Share Post via...](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj) [Report Abuse](https://dev.to/report-abuse)
[ ![Cover image for Architecting Large-Scale Next.js Applications \(Folder Structure, Patterns, Best Practices\)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy2er1masimbz13yyi980.gif) ](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy2er1masimbz13yyi980.gif)
[![AddWeb Solution Pvt Ltd profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F11063%2F0b7a4ce4-43ab-4718-abd0-1d314bc88f99.png)](https://dev.to/addwebsolutionpvtltd) [ ![Mayank Goyal](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3352520%2Fa4983e3d-2d7e-4e40-a2a5-e8699fa0f27f.jpg) ](https://dev.to/mayankgoyal)
[Mayank Goyal](https://dev.to/mayankgoyal) for [AddWeb Solution Pvt Ltd](https://dev.to/addwebsolutionpvtltd)
Posted on 13 Apr
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) 3 ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) 2 ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) 2 ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) 2 ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg) 2
#  Architecting Large-Scale Next.js Applications (Folder Structure, Patterns, Best Practices) 
[#frontend](https://dev.to/t/frontend) [#react](https://dev.to/t/react) [#nextjs](https://dev.to/t/nextjs) [#webdev](https://dev.to/t/webdev)
> “Good architecture makes the system easy to understand; great architecture makes it hard to break.”
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#key-takeaways) Key Takeaways 
  * Feature-based architecture is critical
  * Separate UI, logic, and data layers
  * Prefer server components for performance
  * Centralize API logic
  * Use scalable state management
  * Optimize early, not later


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#index) Index 
  1. Introduction
  2. Why Architecture Matters
  3. Core Principles of Scalable Architecture
  4. Advanced Folder Structure (Enterprise-Level)
  5. Architectural Patterns (Deep Dive)
  6. State Management at Scale
  7. Data Fetching & API Layer Design
  8. Authentication & Authorization Architecture
  9. Performance Optimization (Advanced)
  10. Error Handling & Logging
  11. Testing Strategy (Production-Ready)
  12. Dev Experience & Code Quality
  13. Deployment & Infrastructure Strategy
  14. Real-World Example (Enterprise Dashboard)
  15. Interesting Facts
  16. Stats
  17. FAQ’s
  18. Conclusion


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#introduction) Introduction 
Building small Next.js apps is easy. Scaling them to support millions of users, multiple developers, and complex business logic is not.  
Large-scale applications require:
  * Clean architecture
  * Predictable structure
  * Separation of concerns
  * Strong conventions Next.js (especially App Router) provides powerful primitives, but it does NOT enforce architecture, that’s your responsibility.


This guide gives you a production-grade blueprint.
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#why-architecture-matters) Why Architecture Matters 
At scale, poor architecture leads to:
  * Tight coupling between components
  * Duplicate logic across features
  * Slow builds & performance bottlenecks
  * Difficult onboarding for new developers


Good architecture enables:
  * Independent feature development
  * Faster debugging
  * Better scalability
  * Easier refactoring


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#core-principles-of-scalable-architecture) Core Principles of Scalable Architecture 
**1. Separation of Concerns**  
Divide responsibilities:
  * UI → components
  * Logic → hooks/services
  * Data → API layer


**2. Feature Isolation**  
Each feature should be self-contained.  
Think like mini-apps inside your app.
**3. Single Responsibility Principle**  
Each file/module should do one thing well.
**4. Dependency Direction**  
Components depend on hooks  
Hooks depend on services  
Services depend on APIs  
NOT the other way around.
**5. Scalability First Mindset**  
Design for scale even if you’re small today.
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#advanced-folder-structure-enterpriselevel) Advanced Folder Structure (Enterprise-Level) 

```
src/
│
├── app/                         # Next.js App Router
│   ├── (public)/
│   ├── (auth)/
│   ├── dashboard/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│
├── features/                    # Feature modules (CORE)
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── api/
│   │   ├── store/
│   │   └── types.ts
│   │
│   ├── products/
│   ├── orders/
│   └── users/
│
├── shared/                      # Cross-feature reusable code
│   ├── components/
│   ├── hooks/
│   ├── utils/
│   └── constants/
│
├── core/                        # App-level logic
│   ├── config/
│   ├── providers/
│   ├── middleware/
│   └── guards/
│
├── services/                    # Global services (rare)
├── lib/                         # Low-level utilities
├── types/                       # Global types
├── styles/
└── tests/

```

Enter fullscreen mode Exit fullscreen mode
> “Fetching data is easy. Fetching it efficiently is architecture.”
**Key Insight**  
Avoid “global chaos” folders like components/ for everything  
Prefer feature-based grouping
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#architectural-patterns-deep-dive) Architectural Patterns (Deep Dive) 
**1. Feature-Based Architecture (MOST IMPORTANT)**  
Each feature owns:  
UI  
logic  
API calls  
state  


```
features/products/
    components/
    hooks/
    services/
    store/

```

Enter fullscreen mode Exit fullscreen mode
**2. Layered Architecture**  


```
UI Layer (Components)
↓
Hooks Layer (Business Logic)
↓
Service Layer (API Calls)
↓
API Layer (External systems)

```

Enter fullscreen mode Exit fullscreen mode
**3. Server vs Client Component Strategy**
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx1ukizc2nbaa3674k6id.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx1ukizc2nbaa3674k6id.png)
Example:  


```
// Server Component
export default async function Page() {
  const data = await getProducts();
  return <ProductsClient data={data} />;
}

```

Enter fullscreen mode Exit fullscreen mode
**4. Smart vs Dumb Components**  
Smart → fetch + logic  
Dumb → UI only
**5. Composition Pattern**  
Avoid inheritance. Use composition:  


```
<Card>
  <ProductInfo />
</Card>

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#state-management-at-scale) State Management at Scale 
**When NOT to use global state**
  * Static data
  * Server-fetched data


**Recommended Strategy**
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fubva1g9kclr948nq6nhm.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fubva1g9kclr948nq6nhm.png)
**Example (Zustand Advanced)**  


```
import { create } from 'zustand';
export const useCartStore = create((set) => ({
  items: [],
  addItem: (item) =>
    set((state) => ({ items: [...state.items, item] })),
  clearCart: () => set({ items: [] })
}));

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#data-fetching-amp-api-layer-design) Data Fetching & API Layer Design 
**Bad Practice**  
Calling fetch directly in components everywhere.
**Good Practice**  


```
features/products/
  services/productService.ts

export const getProducts = async () => {
  const res = await fetch('/api/products');
  return res.json();
};

```

Enter fullscreen mode Exit fullscreen mode
> “Every unnecessary render is a tax on your use.”
**Caching Strategy**
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fky5ilifqh69r9fxw1xo7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fky5ilifqh69r9fxw1xo7.png)
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#authentication-amp-authorization-architecture) Authentication & Authorization Architecture 
**Recommended Setup**
  * Middleware for route protection
  * Server-side session validation
  * Role-based access Example: 



```
// middleware.ts
export function middleware(req) {
  const token = req.cookies.get('token');
  if (!token) return Response.redirect('/login');
}

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#performance-optimization-advanced) Performance Optimization (Advanced) 
**Techniques**
  * Code splitting (dynamic imports)
  * Partial hydration
  * Edge rendering
  * Image optimization
  * Memoization


**Example**  


```
const Chart = dynamic(() => import('./Chart'), {
  ssr: false
});

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#error-handling-amp-logging) Error Handling & Logging 
**Centralized Error Handling**  


```
export const handleError = (error) => {
  console.error(error);
};

```

Enter fullscreen mode Exit fullscreen mode
**Logging Tools**
  * Sentry
  * LogRocket


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#testing-strategy-productionready) Testing Strategy (Production-Ready) 
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F73xtlkanvzvmdagm2b77.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F73xtlkanvzvmdagm2b77.png)
**Example**  


```
test('adds item to cart', () => {
  const store = useCartStore.getState();
  store.addItem({ id: 1 });
  expect(store.items.length).toBe(1);
});

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#dev-experience-amp-code-quality) Dev Experience & Code Quality 
ESLint + Prettier  
Husky (pre-commit hooks)  
Strict TypeScript  
Absolute imports (@/features/...)
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#deployment-amp-infrastructure-strategy) Deployment & Infrastructure Strategy 
**Recommended Stack**
  * Hosting → Vercel
  * DB → PostgreSQL
  * CDN → Cloudflare
  * Monitoring → Sentry


**Scaling Tips**
  * Use Edge Functions
  * Optimize bundle size
  * Enable caching


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#realworld-example-enterprise-dashboard) Real-World Example (Enterprise Dashboard) 
**Structure**  


```
features/dashboard/
   components/
      StatsCard.tsx
   hooks/
      useStats.ts
   services/
      dashboardService.ts

```

Enter fullscreen mode Exit fullscreen mode
**Service**  


```
export const fetchStats = async () => {
  const res = await fetch('/api/stats');
  return res.json();
};

```

Enter fullscreen mode Exit fullscreen mode
**Hook**  


```
export const useStats = () => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchStats().then(setStats);
  }, []);

  return stats;
};

```

Enter fullscreen mode Exit fullscreen mode
**Component**  


```
export const StatsCard = ({ data }) => {
  return <div>{data.totalUsers}</div>;
};

```

Enter fullscreen mode Exit fullscreen mode
**Page**  


```
export default function DashboardPage() {
  const stats = useStats();

  if (!stats) return <p>Loading...</p>;

  return <StatsCard data={stats} />;
}

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#interesting-facts) Interesting Facts 
  * Next.js App Router defaults to Server Components.Source: <https://nextjs.org/docs/app/building-your-application/rendering/server-components>
  * Middleware runs at the Edge.Source: <https://nextjs.org/docs/pages/api-reference/file-conventions/middleware>
  * File-based routing reduces ~40% boilerplate.Source: <https://nextjs.org/docs/app/building-your-application/routing>
  * Built-in optimizations replace many libraries.Source: <https://nextjs.org/docs/architecture>
  * ISR allows hybrid static + dynamic pages.Source: <https://nextjs.org/docs/pages/building-your-application/rendering/incremental-static-regeneration>


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#stats) Stats 
  * Next.js is one of the fastest-growing React frameworks and is widely adopted for production-grade applications. Source: <https://nextjs.org/showcase>
  * Next.js has 120,000+ stars on GitHub, reflecting its strong developer adoption and community support. Source: <https://github.com/vercel/next.js>
  * According to the State of JS survey, Next.js consistently ranks among the top frameworks in developer satisfaction and usage. Source: <https://stateofjs.com/>
  * Vercel, the company behind Next.js, serves billions of requests per week across applications deployed on its platform. Source: <https://vercel.com/customers>
  * Next.js enables hybrid rendering (SSR, SSG, ISR), which improves performance and scalability for modern web applications. Source: <https://nextjs.org/docs/pages/building-your-application/rendering>
  * File-based routing in Next.js simplifies development by automatically mapping files to routes, reducing manual configuration. Source: <https://nextjs.org/docs/app/building-your-application/routing>


##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#faqs) FAQ’s 
**Q1. Is Redux necessary?**  
No. Use Zustand unless you need complex workflows.
**Q2. How to organize large teams?**
  * Feature ownership
  * Code reviews
  * Clear folder structure


**Q3. Should I use monorepo?**  
Yes, for multi-app systems (Nx / Turborepo).
**Q4. Where to keep reusable components?**  
`shared/components`
**Q5. What is the biggest mistake?**  
Mixing everything in global folders.
##  [ ](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj#conclusion) Conclusion 
Scaling a Next.js application is more about architecture than code. The difference between a messy app and a scalable system lies in:
  * Structure
  * Discipline
  * Consistency By following feature-based design, layered architecture, and modern Next.js patterns, you can build applications that scale effortlessly with both users and teams.


About the Author:_Mayank is a web developer at[AddWebSolution](https://www.addwebsolution.com/), building scalable apps with PHP, Node.js & React. Sharing ideas, code, and creativity._
##  Top comments (0)
Subscribe
![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)
Personal Trusted User [ Create template ](https://dev.to/settings/response-templates)
Templates let you quickly answer FAQs or store snippets for re-use.
Submit Preview [Dismiss](https://dev.to/404.html)
[Code of Conduct](https://dev.to/code-of-conduct) • [Report abuse](https://dev.to/report-abuse)
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](https://dev.to/addwebsolutionpvtltd/architecting-large-scale-nextjs-applications-folder-structure-patterns-best-practices-2dpj). 
Hide child comments as well
Confirm 
For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)
[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F11063%2F0b7a4ce4-43ab-4718-abd0-1d314bc88f99.png) AddWeb Solution Pvt Ltd  ](https://dev.to/addwebsolutionpvtltd)
Follow
Innovative Tech Partner for Your Digital Growth 
Trusted by global brands for web, mobile, and cloud solutions - innovate faster with AddWeb Solution.
[ Visit Website ](https://www.addwebsolution.com/)
###  More from [AddWeb Solution Pvt Ltd](https://dev.to/addwebsolutionpvtltd)
[ Building Reusable UI Components in React (Clean & Scalable Approach)  #react #frontend #webdev #javascript ](https://dev.to/addwebsolutionpvtltd/building-reusable-ui-components-in-react-clean-scalable-approach-gp1) [ Handling API Errors & Loading States in React (Clean UX Approach)  #react #javascript #frontend ](https://dev.to/addwebsolutionpvtltd/handling-api-errors-loading-states-in-react-clean-ux-approach-54o7) [ Data Fetching Strategies in Next.js - SSR, SSG, ISR, and RSC  #nextjs #react #webdev #frontend ](https://dev.to/addwebsolutionpvtltd/data-fetching-strategies-in-nextjs-ssr-ssg-isr-and-rsc-5a2p)
💎 DEV Diamond Sponsors 
Thank you to our Diamond Sponsors for supporting the DEV Community 
[ ![Google AI - Official AI Model and Platform Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxjlyhbdqehj3akhz166w.png) ](https://aistudio.google.com/?utm_source=partner&utm_medium=partner&utm_campaign=FY25-Global-DEVpartnership-sponsorship-AIS&utm_content=-&utm_term=-&bb=146443)
Google AI is the official AI Model and Platform Partner of DEV
[ ![Neon - Official Database Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbnl88cil6afxzmgwrgtt.png) ](https://neon.tech/?ref=devto&bb=146443)
Neon is the official database partner of DEV
[ ![Algolia - Official Search Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv30ephnolfvnlwgwm0yz.png) ](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral&bb=146443)
Algolia is the official search partner of DEV
[DEV Community](https://dev.to/) — A space to discuss and keep up software development and manage your software career 
  * [ Home ](https://dev.to/)
  * [ DEV++ ](https://dev.to/++)
  * [ Reading List ](https://dev.to/readinglist)
  * [ Videos ](https://dev.to/videos)
  * [ DEV Education Tracks ](https://dev.to/deved)
  * [ DEV Challenges ](https://dev.to/challenges)
  * [ DEV Help ](https://dev.to/help)
  * [ Advertise on DEV ](https://dev.to/advertise)
  * [ Organization Accounts ](https://dev.to/organizations)
  * [ DEV Showcase ](https://dev.to/showcase)
  * [ About ](https://dev.to/about)
  * [ Contact ](https://dev.to/contact)
  * [ Free Postgres Database ](https://dev.to/free-postgres-database-tier)
  * [ DEV Shop ](https://shop.forem.com/)
  * [ MLH ](https://mlh.io/)


  * [ Code of Conduct ](https://dev.to/code-of-conduct)
  * [ Privacy Policy ](https://dev.to/privacy)
  * [ Terms of Use ](https://dev.to/terms)


Built on [Forem](https://www.forem.com) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to) and other inclusive communities.
Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2026.
![DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)
We're a place where coders share, stay up-to-date and grow their careers. 
[ Log in ](https://dev.to/enter?signup_subforem=1) [ Create account ](https://dev.to/enter?signup_subforem=1&state=new-user)
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)


## Source: https://www.linkedin.com/posts/anooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx

## LinkedIn respects your privacy
LinkedIn and 3rd parties use essential and non-essential cookies to provide, secure, analyze and improve our Services, and to show you relevant ads (including **professional and job ads**) on and off LinkedIn. Learn more in our [Cookie Policy](https://www.linkedin.com/legal/cookie-policy).
Select Accept to consent or Reject to decline non-essential cookies for this use. You can update your choices at any time in your [settings](https://www.linkedin.com/mypreferences/g/guest-cookies).
Accept  Reject 
Agree & Join LinkedIn 
By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy). 
`` `` [ Skip to main content ](https://www.linkedin.com/posts/anooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx#main-content) [ LinkedIn ](https://www.linkedin.com/?trk=public_post_nav-header-logo)
  * [ Top Content  ](https://www.linkedin.com/top-content?trk=public_post_guest_nav_menu_topContent)
  * [ People  ](https://www.linkedin.com/pub/dir/+/+?trk=public_post_guest_nav_menu_people)
  * [ Learning  ](https://www.linkedin.com/learning/search?trk=public_post_guest_nav_menu_learning)
  * [ Jobs  ](https://www.linkedin.com/jobs/search?trk=public_post_guest_nav_menu_jobs)
  * [ Games  ](https://www.linkedin.com/games?trk=public_post_guest_nav_menu_games)


[ Sign in ](https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&fromSignIn=true&trk=public_post_nav-header-signin) [ Join now  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_nav-header-join) [ ](https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&fromSignIn=true&trk=public_post_nav-header-signin)
#  When to use Server Actions vs API Routes in Next.js
This title was summarized by AI from the post below.
[ ](https://in.linkedin.com/in/anooj-mathew-varghese?trk=public_post_feed-actor-image)
[ Anooj Mathew ](https://in.linkedin.com/in/anooj-mathew-varghese?trk=public_post_feed-actor-name)
6mo 
  * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)


💡 𝙒𝙝𝙚𝙣 𝙩𝙤 𝙪𝙨𝙚 𝙎𝙚𝙧𝙫𝙚𝙧 𝘼𝙘𝙩𝙞𝙤𝙣𝙨 𝙫𝙨 𝘼𝙋𝙄 𝙍𝙤𝙪𝙩𝙚𝙨 𝙞𝙣 𝙉𝙚𝙭𝙩.𝙟𝙨 If you’ve moved to [Next.js](http://Next.js?trk=public_post-text) 14+, you’ve probably wondered — “Should I use a Server Action or an API Route for this?” 🤔 Here’s the simple rule I follow 👇 ⚙️ 𝙎𝙚𝙧𝙫𝙚𝙧 𝘼𝙘𝙩𝙞𝙤𝙣𝙨 → 𝘾𝙐𝘿 (Create / Update / Delete) ✅ Ideal for server-side mutations directly from your components ✅ No need for manual fetch() — just call the async action ✅ Automatically runs securely on the server ✅ Handles form submissions, mutations, and cache revalidation seamlessly 💡 Example: Creating a user from a form Updating profile details Deleting a record 🌍 𝘼𝙋𝙄 𝙍𝙤𝙪𝙩𝙚𝙨 → 𝙍 (Read / Fetch) ✅ Perfect for data fetching — you can call them from clients, servers, or external systems ✅ Clean separation for GET endpoints ✅ Can be cached, paginated, and integrated across apps ✅ Works great for dashboards, mobile apps, and other consumers 💡 Example: Fetching data for charts or tables Public endpoints Mobile / external integrations 🚀 𝙎𝙪𝙢𝙢𝙖𝙧𝙮: 🧩 Use Server Actions for mutations (CUD) 🌐 Use API Routes for fetching data (R) Together, they create a clean and scalable pattern — mutations stay within Next, and reads stay reusable and sharable. 🧠 [Next.js](http://Next.js?trk=public_post-text) is slowly redefining the full-stack boundary — use Server Actions to simplify internal logic, and APIs to power everything beyond the UI. [#NextJS](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fnextjs&trk=public_post-text) [#React](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freact&trk=public_post-text) [#FullStack](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffullstack&trk=public_post-text) [#ServerActions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fserveractions&trk=public_post-text) [#API](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fapi&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#TypeScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ftypescript&trk=public_post-text)
  * 
`` ``
[ 2  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_comment-cta) `` ``
Share 
  * Copy
  * LinkedIn
  * Facebook
  * X


To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_feed-cta-banner-cta)
##  More Relevant Posts 
  * [](https://www.linkedin.com/posts/hitesh-lalwani-5435b5168_webdevelopment-javascript-frontend-activity-7395527260029718529-ZQc4)
[ ](https://in.linkedin.com/in/hitesh-lalwani-5435b5168?trk=public_post_feed-actor-image)
[ Hitesh Lalwani ](https://in.linkedin.com/in/hitesh-lalwani-5435b5168?trk=public_post_feed-actor-name)
5mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fhitesh-lalwani-5435b5168_webdevelopment-javascript-frontend-activity-7395527260029718529-ZQc4&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
🔥 LocalStorage vs LocalForage — Why Every Frontend Dev Should Understand the Difference Client-side storage isn’t just about saving data… It’s about choosing the right tool so your app stays fast, stable and scalable. 🔹 LocalStorage Stores data as strings only Synchronous → can block the main thread Great for small flags: theme, filters, UI preferences Not ideal for large or complex data structures 🔹 LocalForage (by Mozilla) Uses IndexedDB under the hood Stores objects, arrays, blobs, files & more Asynchronous → doesn’t freeze your UI Perfect for caching APIs, offline data, large lists, file-heavy apps 📌 Key Insight: LocalForage gives you the simplicity of LocalStorage with the power of IndexedDB — without writing complex database code. If your project is growing or performance is becoming critical, upgrading from LocalStorage to LocalForage can be a game-changer. Build smarter. Ship smoother. 🚀 [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#Frontend](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontend&trk=public_post-text) [#localStorage](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Flocalstorage&trk=public_post-text) [#localForage](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Flocalforage&trk=public_post-text) [#WebPerformance](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebperformance&trk=public_post-text) [#DevTips](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fdevtips&trk=public_post-text)
    * `` ``
[ 7  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fhitesh-lalwani-5435b5168_webdevelopment-javascript-frontend-activity-7395527260029718529-ZQc4&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fhitesh-lalwani-5435b5168_webdevelopment-javascript-frontend-activity-7395527260029718529-ZQc4&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fhitesh-lalwani-5435b5168_webdevelopment-javascript-frontend-activity-7395527260029718529-ZQc4&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fhitesh-lalwani-5435b5168_webdevelopment-javascript-frontend-activity-7395527260029718529-ZQc4&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/oleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7)
[ ](https://ua.linkedin.com/in/oleksandr-holovchak?trk=public_post_feed-actor-image)
[ Oleksandr Holovchak ](https://ua.linkedin.com/in/oleksandr-holovchak?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
REST API vs GraphQL — What’s the Real Difference? When it comes to building modern backends, the debate between REST API and GraphQL is still going strong. Both have their place — but understanding their core differences helps you pick the right tool for your system’s needs. 🔹 REST API Organized around multiple endpoints (/users, /posts, /comments) Each request returns a fixed structure of data Easy to cache and integrate But… often leads to over-fetching (getting more data than you need) or under-fetching (missing data, requiring multiple requests) 🔹 GraphQL Single endpoint (/graphql) Client defines exactly what fields it needs Reduces over-fetching Great for complex UIs and mobile apps But… can be harder to cache and requires more complex setup & security handling 💡 My take: If your data model is simple and performance is key — REST is perfectly fine. If your frontend needs flexibility and nested data from multiple sources — GraphQL is a game changer. [#NodeJS](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fnodejs&trk=public_post-text) [#GraphQL](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fgraphql&trk=public_post-text) [#RESTAPI](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Frestapi&trk=public_post-text) [#BackendDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fbackenddevelopment&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#TypeScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ftypescript&trk=public_post-text) [#APIDesign](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fapidesign&trk=public_post-text) [#SoftwareEngineering](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fsoftwareengineering&trk=public_post-text)
    * `` ``
[ 7  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [ 1 Comment ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7&trk=public_post_social-actions-comments)
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foleksandr-holovchak_nodejs-graphql-restapi-activity-7388852987433152512-5ZT7&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/amnasaleemofficial_mern-socketio-nodejs-activity-7387453385840517120-y5J1)
[ ](https://pk.linkedin.com/in/amnasaleemofficial?trk=public_post_feed-actor-image)
[ Amna Saleem ](https://pk.linkedin.com/in/amnasaleemofficial?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Famnasaleemofficial_mern-socketio-nodejs-activity-7387453385840517120-y5J1&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
🚀 Real-time Communication with [Socket.io](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2FSocket%2Eio&urlhash=En1d&trk=public_post-text) (9th Post of Our Series) In modern web applications, real-time communication has become essential — from chat systems and live notifications to collaborative tools. ⚡ That’s where [Socket.io](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2FSocket%2Eio&urlhash=En1d&trk=public_post-text) steps in! It allows bi-directional, event-based communication between the client and server — instantly updating all connected users without refreshing the page. 🔧 How It Works: The client connects to the server using WebSockets (or falls back to other protocols). Both sides can emit and listen to custom events. Perfect for real-time chat apps, live dashboards, notifications, and gaming platforms. 🧠 Example: // Server side ([Node.js](http://Node.js?trk=public_post-text) + Express) import { Server } from "[socket.io](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Fsocket%2Eio&urlhash=lrpT&trk=public_post-text)"; const io = new Server(5000, { cors: { origin: "*" } }); [io.on](http://io.on?trk=public_post-text)("connection", (socket) => { [console.log](http://console.log?trk=public_post-text)("User connected:", [socket.id](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Fsocket%2Eid&urlhash=eFMD&trk=public_post-text)); [socket.on](http://socket.on?trk=public_post-text)("message", (data) => [io.emit](http://io.emit?trk=public_post-text)("message", data)); }); // Client side (React) import { io } from "[socket.io](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Fsocket%2Eio&urlhash=lrpT&trk=public_post-text)-client"; const socket = io("http://localhost:5000"); [socket.on](http://socket.on?trk=public_post-text)("message", (data) => [console.log](http://console.log?trk=public_post-text)(data)); [socket.emit](http://socket.emit?trk=public_post-text)("message", "Hello from client!"); 💡 Why Use [Socket.io](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2FSocket%2Eio&urlhash=En1d&trk=public_post-text)? ✅ Real-time updates ✅ Low latency communication ✅ Simple integration with Express & React ✅ Built-in reconnection handling Next time you send a message or get an instant notification — there’s a good chance [Socket.io](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2FSocket%2Eio&urlhash=En1d&trk=public_post-text) is behind it 🔥 Stay tuned for the next post in our MERN Stack Series! 💻 [#MERN](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fmern&trk=public_post-text) [#SocketIO](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fsocketio&trk=public_post-text) [#NodeJS](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fnodejs&trk=public_post-text) [#React](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freact&trk=public_post-text) [#RealTime](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Frealtime&trk=public_post-text) [#WebSockets](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebsockets&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#Developers](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fdevelopers&trk=public_post-text) [#CodingJourney](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fcodingjourney&trk=public_post-text)
    * View C2PA information
`` ``
[ 7  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Famnasaleemofficial_mern-socketio-nodejs-activity-7387453385840517120-y5J1&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Famnasaleemofficial_mern-socketio-nodejs-activity-7387453385840517120-y5J1&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Famnasaleemofficial_mern-socketio-nodejs-activity-7387453385840517120-y5J1&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Famnasaleemofficial_mern-socketio-nodejs-activity-7387453385840517120-y5J1&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/venkateshkumark_javascript-asyncawait-errorhandling-activity-7389948718831288321-mW2a)
[ ](https://in.linkedin.com/in/venkateshkumark?trk=public_post_feed-actor-image)
[ Venkatesh Kumar ](https://in.linkedin.com/in/venkateshkumark?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvenkateshkumark_javascript-asyncawait-errorhandling-activity-7389948718831288321-mW2a&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
Error Handling in Async/Await (try...catch in JavaScript) When using Async/Await, handling errors properly is just as important as handling data. That’s where the try...catch block shines It helps you catch and manage errors without crashing your app. Definition: try — contains the code that may throw an error. catch — handles the error gracefully when something goes wrong. Example: function fetchData(success) { return new Promise((resolve, reject) => { setTimeout(() => { if (success) resolve("✅ Data fetched successfully"); else reject("❌ Failed to fetch data"); }, 1000); }); } async function getData() { try { [console.log](http://console.log?trk=public_post-text)("Fetching data..."); const result = await fetchData(false); // change to true to test success [console.log](http://console.log?trk=public_post-text)(result); } catch (error) { [console.error](http://console.error?trk=public_post-text)("Error caught:", error); } finally { [console.log](http://console.log?trk=public_post-text)("Operation completed ✅"); } } getData(); Output (if failed): Fetching data... Error caught: ❌ Failed to fetch data Operation completed ✅ ⚙️ Why it’s useful: ✅ Prevents app crashes ✅ Keeps async code clean ✅ Helps in debugging network/API issues ✅ Works beautifully with multiple awaits 🔖 [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#AsyncAwait](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fasyncawait&trk=public_post-text) [#ErrorHandling](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ferrorhandling&trk=public_post-text) [#TryCatch](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ftrycatch&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#Frontend](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontend&trk=public_post-text) [#CodingTips](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fcodingtips&trk=public_post-text) [#AsyncProgramming](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fasyncprogramming&trk=public_post-text) [#JSConcepts](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjsconcepts&trk=public_post-text) [#100DaysOfCode](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2F100daysofcode&trk=public_post-text) [#LearnsJS](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Flearnsjs&trk=public_post-text) [#DeveloperJourney](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fdeveloperjourney&trk=public_post-text) [#WebDevCommunity](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevcommunity&trk=public_post-text)
`` ``
[ 2  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvenkateshkumark_javascript-asyncawait-errorhandling-activity-7389948718831288321-mW2a&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvenkateshkumark_javascript-asyncawait-errorhandling-activity-7389948718831288321-mW2a&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvenkateshkumark_javascript-asyncawait-errorhandling-activity-7389948718831288321-mW2a&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvenkateshkumark_javascript-asyncawait-errorhandling-activity-7389948718831288321-mW2a&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/jyotika-sethi-06805213a_react-reactjs-nextjs-activity-7391508588147466241-l9mv)
[ ](https://in.linkedin.com/in/jyotika-sethi-06805213a?trk=public_post_feed-actor-image)
[ Jyotika Sethi ](https://in.linkedin.com/in/jyotika-sethi-06805213a?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjyotika-sethi-06805213a_react-reactjs-nextjs-activity-7391508588147466241-l9mv&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
⚛️ React 19 – New & Updated Hooks use() → Lets you directly use async data or promises inside components without useEffect, simplifying data fetching. 🧠 Example: const user = use(fetchUser()); useOptimistic() → Makes optimistic UI updates easy by letting you show temporary data before the server confirms changes. 🧠 Example: Instantly add a todo to the list before it’s saved. useActionState() → Manages form state, submission, and errors in one place, making form handling cleaner. 🧠 Example: Handle loading and validation directly with one hook. useFormStatus() → Gives real-time status of a form (like pending or submitted) during server actions. 🧠 Example: Disable the submit button while the form is sending data. useDeferredValue() (from React 18) → Defers rendering of slow components to keep the UI responsive. 🧠 Example: Smooth typing experience during heavy data filtering. useTransition() (from React 18) → Allows marking state updates as non-urgent, improving perceived performance. 🧠 Example: Show loading spinner while background updates happen. React 18 improved performance with concurrent rendering and transitions, React 19 makes async data and forms simpler and more intuitive with use(), useOptimistic(), and useActionState(). [#react](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freact&trk=public_post-text) [#reactjs](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freactjs&trk=public_post-text) [#nextjs](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fnextjs&trk=public_post-text) [#javascript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#frontend](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontend&trk=public_post-text)
`` ``
[ 21  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjyotika-sethi-06805213a_react-reactjs-nextjs-activity-7391508588147466241-l9mv&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjyotika-sethi-06805213a_react-reactjs-nextjs-activity-7391508588147466241-l9mv&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjyotika-sethi-06805213a_react-reactjs-nextjs-activity-7391508588147466241-l9mv&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjyotika-sethi-06805213a_react-reactjs-nextjs-activity-7391508588147466241-l9mv&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/a4pratapsingh_usemastering-useeffect-in-react-the-complete-activity-7389221365016580096-kDDM)
[ ](https://in.linkedin.com/in/a4pratapsingh?trk=public_post_feed-actor-image)
[ Ankit Singh ](https://in.linkedin.com/in/a4pratapsingh?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fa4pratapsingh_usemastering-useeffect-in-react-the-complete-activity-7389221365016580096-kDDM&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
Still confused about useEffect in React? Let’s clear it up once and for all! When I first started learning React, useEffect was one of those hooks that always felt tricky. When does it run? Why does it re-run? What’s the deal with the dependency array? After some deep practice and a lot of mistakes, I finally cracked how useEffect truly works, and I wrote a detailed, beginner-friendly tutorial to help others understand it too. In this post, I’ve explained: 1. What useEffect actually does 2. When and how it runs 3. How to use the cleanup function 4. Real examples for API fetching, timers, and more If you’re learning React or want to master hooks, this one’s for you. [https://lnkd.in/d66KSm7V](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2Fd66KSm7V&urlhash=ohgy&trk=public_post-text) [#React](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freact&trk=public_post-text) [#ReactHooks](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freacthooks&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#Frontend](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontend&trk=public_post-text) [#CodingJourney](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fcodingjourney&trk=public_post-text)
[ UseMastering useEffect in React - The Complete Beginner’s Guide to Side Effects  medium.com  ](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fmedium%2Ecom%2F%40a4ankit%2Fusemastering-useeffect-in-react-the-complete-beginners-guide-to-side-effects-6c947b6745de&urlhash=ipOp&trk=public_post_feed-article-content)
`` ``
[ 2  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fa4pratapsingh_usemastering-useeffect-in-react-the-complete-activity-7389221365016580096-kDDM&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fa4pratapsingh_usemastering-useeffect-in-react-the-complete-activity-7389221365016580096-kDDM&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fa4pratapsingh_usemastering-useeffect-in-react-the-complete-activity-7389221365016580096-kDDM&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fa4pratapsingh_usemastering-useeffect-in-react-the-complete-activity-7389221365016580096-kDDM&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/akanimomichael_nextjs-reactjs-webdevelopment-activity-7393744080599609344-d5kv)
[ ](https://ng.linkedin.com/in/akanimomichael?trk=public_post_feed-actor-image)
[ Akanimo Michael ](https://ng.linkedin.com/in/akanimomichael?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fakanimomichael_nextjs-reactjs-webdevelopment-activity-7393744080599609344-d5kv&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
Static vs Dynamic Data Fetching in [Next.js](http://Next.js?trk=public_post-text) One of the things I love about [Next.js](http://Next.js?trk=public_post-text) is how flexible it is when it comes to data fetching. The framework gives you full control over when and how data is fetched whether at build time or on every request. Let’s break it down Static Data Fetching (getStaticProps) Data is fetched at build time, and the generated HTML is served to every user. It’s super fast and perfect for: Blogs Marketing pages Product listings that don’t change often Think of it like preloading everything before users arrive. Dynamic Data Fetching (getServerSideProps / API Routes / Client Fetching) Data is fetched on each request (or in real time from the client). Best for: Dashboards User profiles Real-time feeds Admin panels Think of it as loading content just-in-time for each visitor. With [Next.js](http://Next.js?trk=public_post-text), you can even mix both approaches use static fetching for stable data and dynamic fetching for live updates. That’s what makes it one of the most powerful frameworks for building modern web apps. [#Nextjs](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fnextjs&trk=public_post-text) [#ReactJS](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freactjs&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#FrontendDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontenddevelopment&trk=public_post-text) [#APIs](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fapis&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#Coding](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fcoding&trk=public_post-text) [#WebPerformance](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebperformance&trk=public_post-text)
    * `` ``
[ 1  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fakanimomichael_nextjs-reactjs-webdevelopment-activity-7393744080599609344-d5kv&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fakanimomichael_nextjs-reactjs-webdevelopment-activity-7393744080599609344-d5kv&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fakanimomichael_nextjs-reactjs-webdevelopment-activity-7393744080599609344-d5kv&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fakanimomichael_nextjs-reactjs-webdevelopment-activity-7393744080599609344-d5kv&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/roman-fedytskyi_react-introduces-new-use-hook-in-latest-activity-7388596360406532096-9Mrw)
[ ](https://www.linkedin.com/in/roman-fedytskyi?trk=public_post_feed-actor-image)
[ Roman Fedytskyi ](https://www.linkedin.com/in/roman-fedytskyi?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Froman-fedytskyi_react-introduces-new-use-hook-in-latest-activity-7388596360406532096-9Mrw&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
React’s New use() Hook Simplifies Async Data Handling. React just introduced a game-changing API, the use() hook, designed to make asynchronous data fetching and server component integration seamless. What it does: - Lets you “unwrap” promises directly inside components - Removes the need for useEffect, loading states, or extra state hooks - Works hand-in-hand with Suspense and Server Components - Simplifies async rendering with cleaner, synchronous-style code No extra effects, no manual state management. React now handles suspension, hydration, and error recovery natively. The use() hook signals a philosophical shift in React’s architecture: async rendering is no longer an afterthought, it’s built into the core model. What do you think? Is this the end of useEffect for data fetching? [#React](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freact&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#Frontend](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontend&trk=public_post-text) [#Async](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fasync&trk=public_post-text) [#Suspense](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fsuspense&trk=public_post-text) [#ReactServerComponents](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freactservercomponents&trk=public_post-text) [#RomanFedytskyi](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fromanfedytskyi&trk=public_post-text)
[ React Introduces New use() Hook in Latest Version  medium.com  ](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fmedium%2Ecom%2F%40roman_fedyskyi%2Freact-introduces-new-use-hook-in-latest-version-ed83ef4c3c50&urlhash=qzck&trk=public_post_feed-article-content)
`` ``
[ 23  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Froman-fedytskyi_react-introduces-new-use-hook-in-latest-activity-7388596360406532096-9Mrw&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Froman-fedytskyi_react-introduces-new-use-hook-in-latest-activity-7388596360406532096-9Mrw&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Froman-fedytskyi_react-introduces-new-use-hook-in-latest-activity-7388596360406532096-9Mrw&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Froman-fedytskyi_react-introduces-new-use-hook-in-latest-activity-7388596360406532096-9Mrw&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/jawad26_reactjs-suspense-datafetching-activity-7388076994313240577-c57D)
[ ](https://pk.linkedin.com/in/jawad26?trk=public_post_feed-actor-image)
[ Muhammad Jawad Hassan ](https://pk.linkedin.com/in/jawad26?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjawad26_reactjs-suspense-datafetching-activity-7388076994313240577-c57D&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
𝗪𝗮𝗻𝘁 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝗱𝗮𝘁𝗮 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗯𝗹𝗼𝗰𝗸𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗨𝗜? 𝗧𝗿𝘆 𝗥𝗲𝗮𝗰𝘁 𝗦𝘂𝘀𝗽𝗲𝗻𝘀𝗲! Suspense lets you "wait" for async operations (like data fetching) without blocking the entire UI. No more loading spinners that freeze your app! How it works: → Wrap your async component with 𝗥𝗲𝗮𝗰𝘁.𝗦𝘂𝘀𝗽𝗲𝗻𝘀𝗲 → Use a "fallback" component (e.g., a spinner or skeleton screen) while data is loading → Once data is ready, React automatically swaps in the fully loaded component Benefits: • Improved user experience—only the relevant part of the UI waits for data • Cleaner code—no more manual loading states or conditional rendering • Seamless integration with React Query, SWR, or other data-fetching libraries Example: ``` <Suspense fallback={<Spinner />}> <AsyncComponent /> </Suspense> ``` Tip: Combine Suspense with 𝗥𝗲𝗮𝗰𝘁.𝗹𝗮𝘇𝘆 for even better performance. Load components only when they’re needed! 𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲𝘀: • 𝗥𝗲𝗮𝗰𝘁 𝗱𝗼𝗰𝘀: [https://lnkd.in/dUpifpQG](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FdUpifpQG&urlhash=1FR7&trk=public_post-text) • 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗮𝗹 𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹𝘀 𝗼𝗻 𝗦𝘂𝘀𝗽𝗲𝗻𝘀𝗲 + 𝗱𝗮𝘁𝗮 𝗳𝗲𝘁𝗰𝗵𝗶𝗻𝗴 [#ReactJS](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freactjs&trk=public_post-text) [#Suspense](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fsuspense&trk=public_post-text) [#DataFetching](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fdatafetching&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text) [#Frontend](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Ffrontend&trk=public_post-text) [#ReactDev](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freactdev&trk=public_post-text)
`` ``
[ 1  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjawad26_reactjs-suspense-datafetching-activity-7388076994313240577-c57D&trk=public_post_social-actions-reactions) `` `` `` `` `` `` ``
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjawad26_reactjs-suspense-datafetching-activity-7388076994313240577-c57D&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjawad26_reactjs-suspense-datafetching-activity-7388076994313240577-c57D&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fjawad26_reactjs-suspense-datafetching-activity-7388076994313240577-c57D&trk=public_post_feed-cta-banner-cta)
  * [](https://www.linkedin.com/posts/pedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ)
[ ](https://br.linkedin.com/in/pedro-teixeira-106a20170?trk=public_post_feed-actor-image)
[ Pedro Teixeira ](https://br.linkedin.com/in/pedro-teixeira-106a20170?trk=public_post_feed-actor-name)
6mo 
    * [ ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fpedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)
Stop writing boilerplate code for data caching! 🤯 If you’re building with [Next.js](http://Next.js?trk=public_post-text), you’re sitting on a performance goldmine you might not even know about: the enhanced `fetch` API. [Next.js](http://Next.js?trk=public_post-text) has quietly turned the standard Web `fetch` function into a powerful, built-in data caching layer. This isn’t just a minor feature; it’s a fundamental shift that drastically improves your application’s performance and reduces server load. The Magic Behind the Scenes: In the App Router, every `fetch` request is automatically cached on the server (Data Cache). This means that instead of hitting your database or external API on every request, [Next.js](http://Next.js?trk=public_post-text) serves the data instantly from its cache. The result? Pages load faster, and your infrastructure costs drop. How to Master It (The Engagement Hook): The real power comes from control. You can easily manage the cache lifetime using the `revalidate` option: `revalidate: 60` This simple line gives you the power of Incremental Static Regeneration (ISR) on a per-fetch basis. For dynamic content, you can opt out with `cache: 'no-store'`. What’s the biggest headache your team currently faces with data fetching and caching in your [Next.js](http://Next.js?trk=public_post-text) applications? Share your challenges below! 👇 [#Nextjs](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fnextjs&trk=public_post-text) [#React](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Freact&trk=public_post-text) [#WebDevelopment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdevelopment&trk=public_post-text) [#Performance](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fperformance&trk=public_post-text) [#Caching](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fcaching&trk=public_post-text) [#WebDev](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fwebdev&trk=public_post-text) [#JavaScript](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjavascript&trk=public_post-text)
    * `` ``
[ 9  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fpedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [ 1 Comment ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fpedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ&trk=public_post_social-actions-comments)
[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fpedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fpedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ&trk=public_post_comment-cta) `` ``
Share 
    * Copy
    * LinkedIn
    * Facebook
    * X
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fpedro-teixeira-106a20170_nextjs-react-webdevelopment-activity-7389074836280578048-xWVJ&trk=public_post_feed-cta-banner-cta)


![](https://media.licdn.com/dms/image/v2/C5616AQGXYvEB1fFmFQ/profile-displaybackgroundimage-shrink_200_800/profile-displaybackgroundimage-shrink_200_800/0/1612028191317?e=2147483647&v=beta&t=gayCkfg93b5Y7EnSTkCHveu_URh55uYccezEYAim1Wo)
652 followers 
  * [ 50 Posts ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fin%2Fanooj-mathew-varghese%2Frecent-activity%2F&trk=public_post_follow-posts)


[ View Profile ](https://in.linkedin.com/in/anooj-mathew-varghese?trk=public_post_follow-view-profile) [ Connect ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2Fupdate%2Furn%3Ali%3Aactivity%3A7389139610506989568&trk=public_post_follow)
##  Explore content categories 
  * [Career](https://www.linkedin.com/top-content/career/)
  * [Productivity](https://www.linkedin.com/top-content/productivity/)
  * [Finance](https://www.linkedin.com/top-content/finance/)
  * [Soft Skills & Emotional Intelligence](https://www.linkedin.com/top-content/soft-skills-emotional-intelligence/)
  * [Project Management](https://www.linkedin.com/top-content/project-management/)
  * [Education](https://www.linkedin.com/top-content/education/)
  * [Technology](https://www.linkedin.com/top-content/technology/)
  * [Leadership](https://www.linkedin.com/top-content/leadership/)
  * [Ecommerce](https://www.linkedin.com/top-content/ecommerce/)
  * [User Experience](https://www.linkedin.com/top-content/user-experience/)

Show more  Show less 
  * LinkedIn © 2026
  * [ About ](https://about.linkedin.com?trk=d_public_post_footer-about)
  * [ Accessibility ](https://www.linkedin.com/accessibility?trk=d_public_post_footer-accessibility)
  * [ User Agreement ](https://www.linkedin.com/legal/user-agreement?trk=d_public_post_footer-user-agreement)
  * [ Privacy Policy ](https://www.linkedin.com/legal/privacy-policy?trk=d_public_post_footer-privacy-policy)
  * [ Cookie Policy ](https://www.linkedin.com/legal/cookie-policy?trk=d_public_post_footer-cookie-policy)
  * [ Copyright Policy ](https://www.linkedin.com/legal/copyright-policy?trk=d_public_post_footer-copyright-policy)
  * [ Brand Policy ](https://brand.linkedin.com/policies?trk=d_public_post_footer-brand-policy)
  * [ Guest Controls ](https://www.linkedin.com/psettings/guest-controls?trk=d_public_post_footer-guest-controls)
  * [ Community Guidelines ](https://www.linkedin.com/legal/professional-community-policies?trk=d_public_post_footer-community-guide)
  *     * العربية (Arabic) 
    * বাংলা (Bangla) 
    * Čeština (Czech) 
    * Dansk (Danish) 
    * Deutsch (German) 
    * Ελληνικά (Greek) 
    * **English (English)**
    * Español (Spanish) 
    * فارسی (Persian) 
    * Suomi (Finnish) 
    * Français (French) 
    * हिंदी (Hindi) 
    * Magyar (Hungarian) 
    * Bahasa Indonesia (Indonesian) 
    * Italiano (Italian) 
    * עברית (Hebrew) 
    * 日本語 (Japanese) 
    * 한국어 (Korean) 
    * मराठी (Marathi) 
    * Bahasa Malaysia (Malay) 
    * Nederlands (Dutch) 
    * Norsk (Norwegian) 
    * ਪੰਜਾਬੀ (Punjabi) 
    * Polski (Polish) 
    * Português (Portuguese) 
    * Română (Romanian) 
    * Русский (Russian) 
    * Svenska (Swedish) 
    * తెలుగు (Telugu) 
    * ภาษาไทย (Thai) 
    * Tagalog (Tagalog) 
    * Türkçe (Turkish) 
    * Українська (Ukrainian) 
    * Tiếng Việt (Vietnamese) 
    * 简体中文 (Chinese (Simplified)) 
    * 正體中文 (Chinese (Traditional)) 
Language 


``
##  Sign in to view more content 
Create your free account or sign in to continue your search
`` `` `` `` `` ``
Email or phone 
Password 
Show
[Forgot password?](https://www.linkedin.com/uas/request-password-reset?trk=csm-v2_forgot_password) Sign in 
Sign in with Email
or 
New to LinkedIn? [Join now](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fanooj-mathew-varghese_nextjs-react-fullstack-activity-7389139610506989568-I4Wx&trk=public_post_contextual-sign-in-modal_join-link)
By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy). 


## Source: https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo

# 
![site logo](https://stackoverflow.com/Content/Sites/stackoverflow/Img/icon-48.png?v=6452e6a98212)
By clicking “Sign up”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our [privacy policy](https://stackoverflow.com/legal/privacy-policy).
Sign up with Google
Sign up with GitHub
# OR
Email
Password
Sign up
Already have an account? [Log in](https://stackoverflow.com/users/login)
[Skip to main content](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo#content)
[](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo) [ ](https://stackoverflow.com "Stack Overflow")
  1. [ About ](https://stackoverflow.co/)
  2. Products
  3. [ For Teams ](https://stackoverflow.co/internal/)


  1. [ Stack Internal Implement a knowledge platform layer to power your enterprise and AI tools. ](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=stack-overflow-for-teams)
  2. [ Stack Data Licensing Get access to top-class technical expertise with trusted & attributed content. ](https://stackoverflow.co/data-licensing/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=overflow-api)
  3. [ Stack Ads Connect your brand to the world’s most trusted technologist communities. ](https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=stack-overflow-advertising)
  4. [ Releases Keep up-to-date on features we add to Stack Overflow and Stack Internal. ](https://stackoverflow.blog/releases/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=releases)
  5. [About the company](https://stackoverflow.co/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=about-the-company) [Visit the blog](https://stackoverflow.blog/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=blog)


Loading…
  1. [](https://stackoverflow.com/help "Help Center and other resources")
     * [ Tour  Start here for a quick overview of the site  ](https://stackoverflow.com/tour)
     * [ Help Center  Detailed answers to any questions you might have  ](https://stackoverflow.com/help)
     * [ Meta  Discuss the workings and policies of this site  ](https://meta.stackoverflow.com)
     * [ About Us  Learn more about Stack Overflow the company, and our products  ](https://stackoverflow.co/)
  2. [ ](https://stackexchange.com "A list of all 183 Stack Exchange sites")
  3. ###  [current community](https://stackoverflow.com)
     * [ Stack Overflow  ](https://stackoverflow.com)
[help](https://stackoverflow.com/help) [chat](https://chat.stackoverflow.com/?tab=explore)
     * [ Meta Stack Overflow  ](https://meta.stackoverflow.com)
###  your communities 
[Sign up](https://stackoverflow.com/users/signup?ssrc=site_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f76415591%2fhow-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo) or [log in](https://stackoverflow.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f76415591%2fhow-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo) to customize your list. 
###  [more stack exchange communities](https://stackexchange.com/sites)
[company blog](https://stackoverflow.blog)
  4. [Log in](https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f76415591%2fhow-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo)
  5. [Sign up](https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f76415591%2fhow-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo)


# 
Let's set up your homepage Select a few topics you're interested in:
pythonjavascriptc#reactjsjavaandroidhtmlflutterc++node.jstypescriptcssrphpangularnext.jsspring-bootmachine-learningsqlexceliosazuredocker
Or search from our full list:
  * javascript
  * python
  * java
  * c#
  * php
  * android
  * html
  * jquery
  * c++
  * css
  * ios
  * sql
  * mysql
  * r
  * reactjs
  * node.js
  * arrays
  * c
  * asp.net
  * json
  * python-3.x
  * .net
  * ruby-on-rails
  * swift
  * sql-server
  * django
  * angular
  * objective-c
  * excel
  * pandas
  * angularjs
  * regex
  * typescript
  * ruby
  * linux
  * ajax
  * iphone
  * vba
  * xml
  * laravel
  * spring
  * asp.net-mvc
  * database
  * wordpress
  * string
  * flutter
  * postgresql
  * mongodb
  * wpf
  * windows
  * xcode
  * amazon-web-services
  * bash
  * git
  * oracle-database
  * spring-boot
  * dataframe
  * azure
  * firebase
  * list
  * multithreading
  * docker
  * vb.net
  * react-native
  * eclipse
  * algorithm
  * powershell
  * macos
  * visual-studio
  * numpy
  * image
  * forms
  * scala
  * function
  * vue.js
  * performance
  * twitter-bootstrap
  * selenium
  * winforms
  * kotlin
  * loops
  * dart
  * express
  * sqlite
  * hibernate
  * matlab
  * python-2.7
  * shell
  * rest
  * apache
  * entity-framework
  * android-studio
  * csv
  * maven
  * linq
  * qt
  * dictionary
  * unit-testing
  * asp.net-core
  * facebook
  * apache-spark
  * tensorflow
  * file
  * swing
  * class
  * unity-game-engine
  * sorting
  * date
  * authentication
  * go
  * symfony
  * t-sql
  * opencv
  * matplotlib
  * .htaccess
  * google-chrome
  * for-loop
  * datetime
  * codeigniter
  * perl
  * http
  * validation
  * sockets
  * google-maps
  * object
  * uitableview
  * xaml
  * oop
  * visual-studio-code
  * if-statement
  * cordova
  * ubuntu
  * web-services
  * email
  * android-layout
  * github
  * spring-mvc
  * elasticsearch
  * kubernetes
  * selenium-webdriver
  * ms-access
  * ggplot2
  * parsing
  * user-interface
  * pointers
  * google-sheets
  * c++11
  * security
  * machine-learning
  * google-apps-script
  * ruby-on-rails-3
  * templates
  * flask
  * nginx
  * variables
  * exception
  * sql-server-2008
  * gradle
  * debugging
  * tkinter
  * delphi
  * listview
  * jpa
  * asynchronous
  * haskell
  * web-scraping
  * jsp
  * pdf
  * ssl
  * amazon-s3
  * google-cloud-platform
  * xamarin
  * testing
  * jenkins
  * wcf
  * batch-file
  * generics
  * npm
  * ionic-framework
  * network-programming
  * unix
  * recursion
  * google-app-engine
  * mongoose
  * visual-studio-2010
  * .net-core
  * android-fragments
  * assembly
  * animation
  * math
  * rust
  * svg
  * session
  * intellij-idea
  * hadoop
  * join
  * winapi
  * curl
  * django-models
  * laravel-5
  * url
  * heroku
  * next.js
  * http-redirect
  * tomcat
  * inheritance
  * google-cloud-firestore
  * webpack
  * gcc
  * swiftui
  * image-processing
  * keras
  * asp.net-mvc-4
  * logging
  * dom
  * matrix
  * pyspark
  * actionscript-3
  * button
  * post
  * optimization
  * firebase-realtime-database
  * cocoa
  * xpath
  * jquery-ui
  * iis
  * d3.js
  * javafx
  * web
  * firefox
  * xslt
  * internet-explorer
  * caching
  * select
  * asp.net-mvc-3
  * opengl
  * events
  * asp.net-web-api
  * plot
  * dplyr
  * encryption
  * magento
  * search
  * stored-procedures
  * amazon-ec2
  * ruby-on-rails-4
  * memory
  * multidimensional-array
  * canvas
  * audio
  * random
  * jsf
  * vector
  * redux
  * cookies
  * input
  * facebook-graph-api
  * flash
  * indexing
  * xamarin.forms
  * arraylist
  * ipad
  * cocoa-touch
  * data-structures
  * video
  * model-view-controller
  * azure-devops
  * serialization
  * apache-kafka
  * jdbc
  * razor
  * awk
  * woocommerce
  * routes
  * mod-rewrite
  * servlets
  * excel-formula
  * beautifulsoup
  * filter
  * iframe
  * docker-compose
  * design-patterns
  * aws-lambda
  * text
  * visual-c++
  * django-rest-framework
  * cakephp
  * mobile
  * android-intent
  * struct
  * react-hooks
  * methods
  * groovy
  * mvvm
  * lambda
  * ssh
  * time
  * checkbox
  * ecmascript-6
  * grails
  * installation
  * google-chrome-extension
  * cmake
  * sharepoint
  * shiny
  * spring-security
  * jakarta-ee
  * plsql
  * android-recyclerview
  * core-data
  * types
  * sed
  * meteor
  * android-activity
  * bootstrap-4
  * activerecord
  * replace
  * graph
  * websocket
  * group-by
  * scikit-learn
  * vim
  * file-upload
  * boost
  * junit
  * memory-management
  * sass
  * async-await
  * import
  * deep-learning
  * error-handling
  * eloquent
  * dynamic
  * dependency-injection
  * silverlight
  * soap
  * layout
  * apache-spark-sql
  * charts
  * deployment
  * browser
  * gridview
  * svn
  * while-loop
  * google-bigquery
  * vuejs2
  * highcharts
  * dll
  * ffmpeg
  * view
  * foreach
  * makefile
  * redis
  * plugins
  * c#-4.0
  * reporting-services
  * jupyter-notebook
  * unicode
  * merge
  * reflection
  * https
  * server
  * google-maps-api-3
  * twitter
  * extjs
  * oauth-2.0
  * terminal
  * pip
  * axios
  * split
  * cmd
  * encoding
  * pytorch
  * django-views
  * collections
  * database-design
  * hash
  * automation
  * netbeans
  * ember.js
  * data-binding
  * build
  * tcp
  * apache-flex
  * sqlalchemy
  * pdo
  * entity-framework-core
  * concurrency
  * command-line
  * spring-data-jpa
  * printing
  * react-redux
  * java-8
  * lua
  * html-table
  * neo4j
  * ansible
  * service
  * jestjs
  * enums
  * flexbox
  * parameters
  * promise
  * material-ui
  * module
  * visual-studio-2012
  * outlook
  * mysqli
  * web-applications
  * uwp
  * webview
  * firebase-authentication
  * jquery-mobile
  * utf-8
  * datatable
  * python-requests
  * parallel-processing
  * colors
  * drop-down-menu
  * scipy
  * tfs
  * scroll
  * hive
  * count
  * syntax
  * ms-word
  * twitter-bootstrap-3
  * ssis
  * rxjs
  * fonts
  * constructor
  * file-io
  * google-analytics
  * paypal
  * three.js
  * powerbi
  * cassandra
  * graphql
  * discord
  * graphics
  * compiler-errors
  * gwt
  * react-router
  * socket.io
  * backbone.js
  * memory-leaks
  * solr
  * url-rewriting
  * datatables
  * nlp
  * terraform
  * oauth
  * datagridview
  * drupal
  * zend-framework
  * oracle11g
  * knockout.js
  * triggers
  * interface
  * neural-network
  * django-forms
  * casting
  * angular-material
  * jmeter
  * linked-list
  * google-api
  * path
  * timer
  * arduino
  * django-templates
  * orm
  * windows-phone-7
  * directory
  * proxy
  * parse-platform
  * visual-studio-2015
  * cron
  * conditional-statements
  * push-notification
  * functional-programming
  * primefaces
  * pagination
  * model
  * jar
  * xamarin.android
  * hyperlink
  * uiview
  * visual-studio-2013
  * vbscript
  * google-cloud-functions
  * azure-active-directory
  * gitlab
  * jwt
  * download
  * swift3
  * sql-server-2005
  * rspec
  * process
  * pygame
  * configuration
  * properties
  * callback
  * combobox
  * windows-phone-8
  * linux-kernel
  * safari
  * scrapy
  * emacs
  * permissions
  * x86
  * clojure
  * scripting
  * raspberry-pi
  * io
  * scope
  * azure-functions
  * compilation
  * mongodb-query
  * responsive-design
  * nhibernate
  * angularjs-directive
  * expo
  * reference
  * architecture
  * binding
  * request
  * bluetooth
  * dns
  * playframework
  * 3d
  * version-control
  * pyqt
  * discord.js
  * doctrine-orm
  * package
  * f#
  * rubygems
  * get
  * sql-server-2012
  * tree
  * autocomplete
  * datepicker
  * kendo-ui
  * openssl
  * jackson
  * yii
  * controller
  * grep
  * xamarin.ios
  * nested
  * static
  * null
  * statistics
  * transactions
  * datagrid
  * active-directory
  * uiviewcontroller
  * dockerfile
  * webforms
  * sas
  * computer-vision
  * discord.py
  * phpmyadmin
  * notifications
  * duplicates
  * pycharm
  * youtube
  * mocking
  * nullpointerexception
  * yaml
  * menu
  * sum
  * blazor
  * plotly
  * bitmap
  * visual-studio-2008
  * floating-point
  * asp.net-mvc-5
  * yii2
  * css-selectors
  * stl
  * android-listview
  * jsf-2
  * electron
  * time-series
  * cryptography
  * ant
  * hashmap
  * character-encoding
  * msbuild
  * asp.net-core-mvc
  * stream
  * sdk
  * google-drive-api
  * jboss
  * selenium-chromedriver
  * joomla
  * devise
  * cuda
  * navigation
  * cors
  * frontend
  * anaconda
  * background
  * multiprocessing
  * binary
  * pyqt5
  * camera
  * iterator
  * linq-to-sql
  * mariadb
  * onclick
  * ios7
  * android-jetpack-compose
  * microsoft-graph-api
  * android-asynctask
  * rabbitmq
  * tabs
  * amazon-dynamodb
  * environment-variables
  * laravel-4
  * uicollectionview
  * linker
  * insert
  * coldfusion
  * xsd
  * console
  * continuous-integration
  * upload
  * textview
  * ftp
  * opengl-es
  * macros
  * operating-system
  * mockito
  * localization
  * formatting
  * json.net
  * xml-parsing
  * type-conversion
  * data.table
  * vuejs3
  * kivy
  * timestamp
  * integer
  * calendar
  * segmentation-fault
  * android-ndk
  * prolog
  * char
  * drag-and-drop
  * crash
  * jasmine
  * azure-pipelines
  * dependencies
  * automated-tests
  * geometry
  * fortran
  * android-gradle-plugin
  * itext
  * sprite-kit
  * mfc
  * header
  * attributes
  * nosql
  * firebase-cloud-messaging
  * format
  * nuxt.js
  * db2
  * odoo
  * jquery-plugins
  * event-handling
  * julia
  * jenkins-pipeline
  * leaflet
  * annotations
  * flutter-layout
  * keyboard
  * nestjs
  * postman
  * arm
  * textbox
  * stripe-payments
  * visual-studio-2017
  * gulp
  * libgdx
  * uikit
  * timezone
  * synchronization
  * azure-web-app-service
  * google-sheets-formula
  * dom-events
  * wso2
  * xampp
  * aggregation-framework
  * namespaces
  * crystal-reports
  * uiscrollview
  * android-emulator
  * swagger
  * jvm
  * sequelize.js
  * com
  * chart.js
  * snowflake-cloud-data-platform
  * subprocess
  * html5-canvas
  * webdriver
  * garbage-collection
  * geolocation
  * sql-update
  * dialog
  * centos
  * concatenation
  * numbers
  * qml
  * widget
  * tuples
  * set
  * java-stream
  * mapreduce
  * ionic2
  * smtp
  * android-edittext
  * windows-10
  * rotation
  * nuget
  * modal-dialog
  * spring-data
  * radio-button
  * doctrine
  * http-headers
  * grid
  * lucene
  * sonarqube
  * xmlhttprequest
  * listbox
  * initialization
  * switch-statement
  * internationalization
  * boolean
  * components
  * apache-camel
  * gdb
  * google-play
  * ios5
  * serial-port
  * return
  * youtube-api
  * ldap
  * pivot
  * eclipse-plugin
  * latex
  * frameworks
  * tags
  * c++17
  * containers
  * subquery
  * github-actions
  * embedded
  * dataset
  * foreign-keys
  * asp-classic
  * label
  * uinavigationcontroller
  * delegates
  * copy
  * google-cloud-storage
  * struts2
  * protractor
  * migration
  * base64
  * uibutton
  * queue
  * find
  * sql-server-2008-r2
  * arguments
  * composer-php
  * append
  * jaxb
  * stack
  * zip
  * tailwind-css
  * cucumber
  * autolayout
  * ide
  * entity-framework-6
  * iteration
  * popup
  * r-markdown
  * windows-7
  * vb6
  * clang
  * g++
  * airflow
  * hover
  * ssl-certificate
  * jqgrid
  * range
  * gmail


Next You’ll be prompted to create an account to view your personalized homepage.
  1.     1. [ Home ](https://stackoverflow.com/)
    2. [ Questions ](https://stackoverflow.com/questions)
    3. [ AI Assist ](https://stackoverflow.com/ai-assist)
    4. [ Tags ](https://stackoverflow.com/tags)
    5. [ Challenges ](https://stackoverflow.com/beta/challenges)
    6. [ Chat ](https://chat.stackoverflow.com/?tab=explore)
    7. [ Articles ](https://stackoverflow.blog/contributed?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=so-blog&utm_content=experiment-articles)
    8. [ Users ](https://stackoverflow.com/users)
    9. [ Companies ](https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&so_source=SiteNav)
    10. [ Collectives ](javascript:void\(0\))
    11. Communities for your favorite technologies. [Explore all Collectives](https://stackoverflow.com/collectives-all)
  2. Stack Internal
Stack Overflow for Teams is now called **Stack Internal**. Bring the best of human thought and AI automation together at your work. 
[Try for free](https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams) [Learn more](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams)
  3. [ Stack Internal ](javascript:void\(0\))
  4. Bring the best of human thought and AI automation together at your work. [Learn more](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams-compact)


##### Collectives™ on Stack Overflow
Find centralized, trusted content and collaborate around the technologies you use most.
[ Learn more about Collectives ](https://stackoverflow.com/collectives)
**Stack Internal**
Knowledge at work
Bring the best of human thought and AI automation together at your work.
[ Explore Stack Internal ](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams-compact-popover)
# [How to best manage migrations with Drizzle ORM in a Monorepo?](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo)
[ Ask Question ](https://stackoverflow.com/questions/ask)
Asked 2 years, 11 months ago
Modified [2 years, 11 months ago](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo?lastactivity "2023-06-06 14:13:17Z")
Viewed 4k times 
This question shows research effort; it is useful and clear
3 
This question does not show any research effort; it is unclear or not useful
Save this question.
[](https://stackoverflow.com/posts/76415591/timeline)
Show activity on this post.
How do you best manage/execute database migrations if the same database is being used within multiple projects?
**Some background:**
I have a project with a monorepo structure build with Turborepo on top of npm workspaces. In the repo I have an internal library that exports a client to perform operations on a postgres database. I then have two apps that use this library to perform operations on the database.
The shared library uses Drizzle ORM to manage the database schema and migrations. It basically exports a client that

```

Copy
export class SomeClient {

  private db: PostgresJsDatabase;
  
  constructor(connection: string) {
    const queryClient = postgres(connection);
    this.db = drizzle(queryClient);
  }

  // business logic functions...

}

```

I create and keep all migrations in a folder within the library directory using Drizzles CLI, Drizzle Kit. But now I am wondering how to execute the migrations. My initial idea was to implement a `migrate()` function on the client:

```

Copy
migrate() {
  return migrate(this.db, { migrationsFolder: 'migrations' });
}

```

However, I can't execute this function within the apps that use the client, because the folder with the migrations is in the library.
One idea to workaround this, was to simply copy all migrations into the apps after creating them or to create a symlink to the migrations folder of the library. My goal is to execute the migrations automatically in the apps on startup. Do you have any ideas or alternative approaches?
  * [postgresql](https://stackoverflow.com/questions/tagged/postgresql "show questions tagged 'postgresql'")
  * [orm](https://stackoverflow.com/questions/tagged/orm "show questions tagged 'orm'")
  * [database-migration](https://stackoverflow.com/questions/tagged/database-migration "show questions tagged 'database-migration'")
  * [monorepo](https://stackoverflow.com/questions/tagged/monorepo "show questions tagged 'monorepo'")
  * [drizzle](https://stackoverflow.com/questions/tagged/drizzle "show questions tagged 'drizzle'")


[Share](https://stackoverflow.com/q/76415591)
Share a link to this question
Copy link[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/ "The current license for this post: CC BY-SA 4.0")
Short permalink to this question
[Improve this question](https://stackoverflow.com/posts/76415591/edit)
Follow 
Follow this question to receive notifications
asked Jun 6, 2023 at 14:13
[![benjiman's user avatar](https://www.gravatar.com/avatar/5f9e0ded7129d58e2baf1d10e3c56f82?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/1372783/benjiman)
[benjiman](https://stackoverflow.com/users/1372783/benjiman)
4,08844 gold badges3535 silver badges4646 bronze badges
2
  * Hiya, did you come up with a solution to this? I'm facing the same issue. Thanks
CallumVass
– [CallumVass](https://stackoverflow.com/users/1005030/callumvass "11,466 reputation")
2023-09-05 14:55:05 +00:00
[ Commented Sep 5, 2023 at 14:55 ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo#comment135822169_76415591)
  * @CallumVass Kind of. I ended up maintaining the migrations and the migrations folder within the library and then run the migrations using `migrate()` as part of the startup routine in one of the backend services that uses the library. It's not ideal but it works as long as everything stays a monorepo. As we are not planning to release the library outside of the monorepo, I'm okay with it for now. BTW, I came up with this after discussing it with one of the Drizzle maintainers in their Discord, so have look there if you have questions.
benjiman
– [benjiman](https://stackoverflow.com/users/1372783/benjiman "4,088 reputation")
2023-09-08 06:24:22 +00:00
[ Commented Sep 8, 2023 at 6:24 ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo#comment135856518_76415591)


[ Add a comment ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.") |  [ ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo "Expand to show all comments on this post")
Related questions
[ 4  PostgreSQL migration issue in AWS RDS with Drizzle ORM: 'no pg_hba.conf entry for host' error ](https://stackoverflow.com/questions/76818549/postgresql-migration-issue-in-aws-rds-with-drizzle-orm-no-pg-hba-conf-entry-fo?rq=2)
[ 13  How to use Turborepo for an existing react app created with Create React App in order to make it a monorepo? ](https://stackoverflow.com/questions/70498521/how-to-use-turborepo-for-an-existing-react-app-created-with-create-react-app-in?rq=2)
[ 0  How to perform migrations in golang migrate when the sql files are located in a github folder? ](https://stackoverflow.com/questions/76730030/how-to-perform-migrations-in-golang-migrate-when-the-sql-files-are-located-in-a?rq=2)
Related questions
[ 4  PostgreSQL migration issue in AWS RDS with Drizzle ORM: 'no pg_hba.conf entry for host' error ](https://stackoverflow.com/questions/76818549/postgresql-migration-issue-in-aws-rds-with-drizzle-orm-no-pg-hba-conf-entry-fo?rq=2)
[ 13  How to use Turborepo for an existing react app created with Create React App in order to make it a monorepo? ](https://stackoverflow.com/questions/70498521/how-to-use-turborepo-for-an-existing-react-app-created-with-create-react-app-in?rq=2)
[ 0  How to perform migrations in golang migrate when the sql files are located in a github folder? ](https://stackoverflow.com/questions/76730030/how-to-perform-migrations-in-golang-migrate-when-the-sql-files-are-located-in-a?rq=2)
[ 7  How to create data migrations with Drizzle ORM? ](https://stackoverflow.com/questions/77263506/how-to-create-data-migrations-with-drizzle-orm?rq=2)
[ 2  How to Manage EF Migrations Between Development and Production Databases? ](https://stackoverflow.com/questions/22019307/how-to-manage-ef-migrations-between-development-and-production-databases?rq=2)
[ 0  Config file for shared component library in a Turborepo ](https://stackoverflow.com/questions/72410096/config-file-for-shared-component-library-in-a-turborepo?rq=2)
##  0
Sorted by:  [ Reset to default ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo?answertab=scoredesc#tab-top)
Highest score (default)  Trending (recent votes count more)  Date modified (newest first)  Date created (oldest first) 
##  Know someone who can answer? Share a link to this [question](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo) via email, [Twitter](https://twitter.com/share?url=https%3a%2f%2fstackoverflow.com%2fq%2f76415591%3fstw%3d2), or [Facebook](https://www.facebook.com/sharer.php?u=https%3a%2f%2fstackoverflow.com%2fq%2f76415591%3fsfb%3d2). 
##  Your Answer 
[ ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo)
Thanks for contributing an answer to Stack Overflow!
  * Please be sure to _answer the question_. Provide details and share your research!


But _avoid_ …
  * Asking for help, clarification, or responding to other answers.
  * Making statements based on opinion; back them up with references or personal experience.


To learn more, see our [tips on writing great answers](https://stackoverflow.com/help/how-to-answer).
Draft saved
Draft discarded
### Sign up or [log in](https://stackoverflow.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f76415591%2fhow-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo%23new-answer)
Submit
### Post as a guest
Name
Email
Required, but never shown
Post Your Answer  Discard 
By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our [privacy policy](https://stackoverflow.com/legal/privacy-policy).
Start asking to get answers
Find the answer to your question by asking.
[Ask question](https://stackoverflow.com/questions/ask)
Explore related questions
  * [postgresql](https://stackoverflow.com/questions/tagged/postgresql "show questions tagged 'postgresql'")
  * [orm](https://stackoverflow.com/questions/tagged/orm "show questions tagged 'orm'")
  * [database-migration](https://stackoverflow.com/questions/tagged/database-migration "show questions tagged 'database-migration'")
  * [monorepo](https://stackoverflow.com/questions/tagged/monorepo "show questions tagged 'monorepo'")
  * [drizzle](https://stackoverflow.com/questions/tagged/drizzle "show questions tagged 'drizzle'")


See similar questions with these tags.
  * The Overflow Blog 
  * [How we replaced Ingress-NGINX at Stack Overflow](https://stackoverflow.blog/2026/05/06/how-we-replaced-nginx-ingress-at-stack-overflow/?cb=1)
  * [AI giveth and AI taketh CPU](https://stackoverflow.blog/2026/05/08/ai-giveth-and-ai-taketh-cpu/?cb=1)
  * Featured on Meta 
  * [(Almost) One year of Challenges](https://meta.stackexchange.com/questions/418261/almost-one-year-of-challenges?cb=1)
  * [Policy: Generative AI (e.g., ChatGPT) is banned](https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned?cb=1)


Community activity
Last 1 hr
Loading…
####  [ Hot Network Questions ](https://stackexchange.com/questions?tab=hot)
  * [ Is Yuyushiki OVA character art style difference intentional? ](https://anime.stackexchange.com/questions/69815/is-yuyushiki-ova-character-art-style-difference-intentional)
  * [ How did Michelson achieve interference fringes with an unpolarized and incoherent light ](https://physics.stackexchange.com/questions/872154/how-did-michelson-achieve-interference-fringes-with-an-unpolarized-and-incoheren)
  * [ Hartree-Fock Ground State definition in Szabo's Modern Quantum Chemistry ](https://chemistry.stackexchange.com/questions/195470/hartree-fock-ground-state-definition-in-szabos-modern-quantum-chemistry)
  * [ Adding mic together to make a composite mic ](https://electronics.stackexchange.com/questions/768856/adding-mic-together-to-make-a-composite-mic)
  * [ Who is the narrator of Uttar Ramayana? ](https://hinduism.stackexchange.com/questions/69921/who-is-the-narrator-of-uttar-ramayana)
  * [ Do you have to reroll all 1 and 2 dice when using GWF? ](https://rpg.stackexchange.com/questions/219284/do-you-have-to-reroll-all-1-and-2-dice-when-using-gwf)
  * [ Implementing the magic gate using these 4-anyon braiding processes ](https://puzzling.stackexchange.com/questions/137970/implementing-the-magic-gate-using-these-4-anyon-braiding-processes)
  * [ Do people with intellectual disabilities, children and the indoctrinated have less moral agency? ](https://philosophy.stackexchange.com/questions/138278/do-people-with-intellectual-disabilities-children-and-the-indoctrinated-have-le)
  * [ Was there food and fuel remaining in the wrecks of Erebus and Terror on the Franklin expedition? ](https://history.stackexchange.com/questions/80063/was-there-food-and-fuel-remaining-in-the-wrecks-of-erebus-and-terror-on-the-fran)
  * [ Can anyone become a data analyst? or who can become a data scientist? ](https://datascience.stackexchange.com/questions/137934/can-anyone-become-a-data-analyst-or-who-can-become-a-data-scientist)
  * [ How do I fix a gutter that was cut open diagonally? ](https://diy.stackexchange.com/questions/330462/how-do-i-fix-a-gutter-that-was-cut-open-diagonally)
  * [ EDG vs GCC/Clang in constexpr rvalue reference behavior in constant expressions ](https://stackoverflow.com/questions/79937637/edg-vs-gcc-clang-in-constexpr-rvalue-reference-behavior-in-constant-expressions)
  * [ A simple but groan-worthy puzzle ](https://puzzling.stackexchange.com/questions/137982/a-simple-but-groan-worthy-puzzle)
  * [ Why didn't the Hail Mary automatically jettison empty fuel tanks? ](https://scifi.stackexchange.com/questions/304375/why-didnt-the-hail-mary-automatically-jettison-empty-fuel-tanks)
  * [ Is this Ramanujan-style multiplicative magic square concept known? ](https://math.stackexchange.com/questions/5136013/is-this-ramanujan-style-multiplicative-magic-square-concept-known)
  * [ How to deal with pseudoreplication when there is near-complete separation due to sampling design? ](https://stats.stackexchange.com/questions/675903/how-to-deal-with-pseudoreplication-when-there-is-near-complete-separation-due-to)
  * [ Why does Caesar refer to himself in the third person? ](https://literature.stackexchange.com/questions/31970/why-does-caesar-refer-to-himself-in-the-third-person)
  * [ How can one identify an authentic Buddhist lineage or disciplic succession? ](https://buddhism.stackexchange.com/questions/55683/how-can-one-identify-an-authentic-buddhist-lineage-or-disciplic-succession)
  * [ 50s-60s SS. Spacers move an ice asteroid to Earth orbit as an "Up Yours" to the politician who was complaining about spacers using Earth's water ](https://scifi.stackexchange.com/questions/304379/50s-60s-ss-spacers-move-an-ice-asteroid-to-earth-orbit-as-an-up-yours-to-the)
  * [ Is time reversal in physics equal to a film playing backwards? ](https://physics.stackexchange.com/questions/872172/is-time-reversal-in-physics-equal-to-a-film-playing-backwards)
  * [ Can South Korea extradite a US-Korean dual citizen who deserted the Korean military and fled to the US? ](https://law.stackexchange.com/questions/114735/can-south-korea-extradite-a-us-korean-dual-citizen-who-deserted-the-korean-milit)
  * [ Has Philosophy investigated non-verbal reasoning? ](https://philosophy.stackexchange.com/questions/138303/has-philosophy-investigated-non-verbal-reasoning)
  * [ What is a number whose Lagrange number is Freiman's constant? ](https://mathoverflow.net/questions/511134/what-is-a-number-whose-lagrange-number-is-freimans-constant)
  * [ Is there any justification for the "10% thrust" test, beyond a gag? ](https://scifi.stackexchange.com/questions/304391/is-there-any-justification-for-the-10-thrust-test-beyond-a-gag)


[ ](https://stackoverflow.com/feeds/question/76415591 "Feed of this question and its answers")
#  Subscribe to RSS 
Question feed 
To subscribe to this RSS feed, copy and paste this URL into your RSS reader.
[ ](https://stackoverflow.com/questions/76415591/how-to-best-manage-migrations-with-drizzle-orm-in-a-monorepo)
lang-sql
#  Why are you flagging this comment?
Probable spam. 
This comment promotes a product, service or website while [failing to disclose the author's affiliation](https://stackoverflow.com/help/promotion).
Unfriendly or contains harassment/bigotry/abuse. 
This comment is unkind, insulting or attacks another person or group. Learn more in our [Abusive behavior policy](https://stackoverflow.com/conduct/abusive-behavior).
Not needed. 
This comment is not relevant to the post.

```
  

```

Enter at least 6 characters
Something else. 
A problem not listed above. Try to be as specific as possible.

```
  

```

Enter at least 6 characters
Flag comment Cancel
You have 0 flags left today
# 
![Illustration of upvote icon after it is clicked](https://stackoverflow.com/Content/Img/modal/img-upvote.png?v=fce73bd9724d)
# Hang on, you can't upvote just yet.
You'll need to complete a few actions and gain 15 reputation points before being able to upvote. **Upvoting** indicates when questions and answers are useful. [What's reputation and how do I get it?](https://stackoverflow.com/help/whats-reputation)
Instead, you can save this post to reference later.
Save this post for later Not now
[](https://stackoverflow.com)
##### [Stack Overflow](https://stackoverflow.com)
  * [Questions](https://stackoverflow.com/questions)
  * [Help](https://stackoverflow.com/help)
  * [Chat](https://chat.stackoverflow.com/?tab=explore)


##### [Business](https://stackoverflow.co/)
  * [Stack Internal](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=teams)
  * [Stack Data Licensing](https://stackoverflow.co/data-licensing/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=data-licensing)
  * [Stack Ads](https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=advertising)


##### [Company](https://stackoverflow.co/)
  * [About](https://stackoverflow.co/)
  * [Press](https://stackoverflow.co/company/press/)
  * [Work Here](https://stackoverflow.co/company/work-here/)
  * [Legal](https://stackoverflow.com/legal)
  * [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
  * [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)
  * [Contact Us](https://stackoverflow.com/contact)
  * Cookie Settings 
  * [Cookie Policy](https://policies.stackoverflow.co/stack-overflow/cookie-policy)


##### [Stack Exchange Network](https://stackexchange.com)
  * [ Technology ](https://stackexchange.com/sites#technology)
  * [ Culture & recreation ](https://stackexchange.com/sites#culturerecreation)
  * [ Life & arts ](https://stackexchange.com/sites#lifearts)
  * [ Science ](https://stackexchange.com/sites#science)
  * [ Professional ](https://stackexchange.com/sites#professional)
  * [ Business ](https://stackexchange.com/sites#business)
  * [ API ](https://api.stackexchange.com/)
  * [ Data ](https://data.stackexchange.com/)


  * [Blog](https://stackoverflow.blog?blb=1)
  * [Facebook](https://www.facebook.com/officialstackoverflow/)
  * [Twitter](https://twitter.com/stackoverflow)
  * [LinkedIn](https://linkedin.com/company/stack-overflow)
  * [Instagram](https://www.instagram.com/thestackoverflow)


Site design / logo © 2026 Stack Exchange Inc;  user contributions licensed under  [CC BY-SA](https://stackoverflow.com/help/licensing) .  rev 2026.5.8.42955


## Source: https://medium.com/@the.sikandar.dev/postgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3

[Sitemap](https://medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)
# PostgreSQL + Next.js + Drizzle ORM(A Step-by-Step Guide)
[![Sikandar Dev](https://miro.medium.com/v2/resize:fill:32:32/1*sNNiHdylwXTlhUUv68ee6Q.png)](https://medium.com/@the.sikandar.dev?source=post_page---byline--cb487b1a3ca3---------------------------------------)
[Sikandar Dev](https://medium.com/@the.sikandar.dev?source=post_page---byline--cb487b1a3ca3---------------------------------------)
Follow
2 min read
·
Feb 19, 2026
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb487b1a3ca3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&user=Sikandar+Dev&userId=486497bac988&source=---header_actions--cb487b1a3ca3---------------------clap_footer------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb487b1a3ca3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&source=---header_actions--cb487b1a3ca3---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dcb487b1a3ca3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&source=---header_actions--cb487b1a3ca3---------------------post_audio_button------------------)
Share
YouTube Video URL
Managing databases in a Next.js application can feel tricky, but **Drizzle ORM** makes it straightforward. It’s type-safe, lightweight, and modern — a refreshing alternative to bulky ORMs.
## Get Sikandar Dev’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
In this guide, we’ll integrate **PostgreSQL with Next.js using Drizzle ORM** for a smooth and efficient database workflow.
## Why Drizzle ORM?
Drizzle ORM is built with **performance and developer experience** in mind. Some highlights:
  * ✅ **Type Safety** — Full TypeScript support.
  * ⚡ **Lightweight & Fast** — Minimal dependencies.
  * 🔄 **Easy Migrations** — Schema-based, CLI-driven.
  * 📝 **SQL-like Syntax** — Intuitive and flexible queries.
  * 📊 **Drizzle Studio** — Built-in visual database management.


## Installation
Install the required packages:

```
npm install drizzle-orm @vercel/postgres pg  
npm install -D drizzle-kit
```

## Configure Database Connection
Create a `.env.local` file in your project root:

```
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
```

## Create Drizzle Config File
Add a `drizzle.config.ts` at the root of your project:

```
import { defineConfig } from 'drizzle-kit'  
  
export default defineConfig({  
  strict: true,  
  verbose: true,  
  out: "./drizzle",  
  dialect: "postgresql",  
  schema: "./src/db/schema.ts",  
  dbCredentials: {  
    url: process.env.DATABASE_URL!,  
  }  
})
```

## Create a DB Instance
Set up the database connection in `src/db/index.ts`:

```
import { Pool } from "pg"  
import { drizzle } from "drizzle-orm/node-postgres"  
  
const pool = new Pool({  
  connectionString: process.env.DATABASE_URL!,  
})  
  
export const db = drizzle(pool)
```

## Define Your Schema
Create `src/db/schema.ts` to define your tables:

```
import { pgTable, serial, text } from 'drizzle-orm/pg-core'  
  
export const users = pgTable('users', {  
  id: serial('id').primaryKey(),  
  name: text('name').notNull(),  
  email: text('email').unique().notNull(),  
})
```

## Run Migrations
Generate and apply migrations with Drizzle Kit:

```
npx drizzle-kit generate  
npx drizzle-kit push
```

You can also explore your database visually using:

```
npx drizzle-kit studio
```

## Query the Database
Use Drizzle ORM to run queries in your app:

```
import { db } from '@/db'  
import { users } from '@/db/schema'  
  
async function getUsers() {  
  return await db.select().from(users)  
}
```

## Conclusion
With Drizzle ORM, integrating **PostgreSQL into a Next.js app** is:
  * Type-safe
  * Easy to migrate
  * Simple to query
  * Developer-friendly


It’s a fantastic choice for building **modern, scalable web applications** without the headaches of traditional ORMs.
[Postgresql](https://medium.com/tag/postgresql?source=post_page-----cb487b1a3ca3---------------------------------------)
[Nextjs](https://medium.com/tag/nextjs?source=post_page-----cb487b1a3ca3---------------------------------------)
[Drizzle](https://medium.com/tag/drizzle?source=post_page-----cb487b1a3ca3---------------------------------------)
[Database](https://medium.com/tag/database?source=post_page-----cb487b1a3ca3---------------------------------------)
[Drizzleorm](https://medium.com/tag/drizzleorm?source=post_page-----cb487b1a3ca3---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb487b1a3ca3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&user=Sikandar+Dev&userId=486497bac988&source=---footer_actions--cb487b1a3ca3---------------------clap_footer------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb487b1a3ca3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&user=Sikandar+Dev&userId=486497bac988&source=---footer_actions--cb487b1a3ca3---------------------clap_footer------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb487b1a3ca3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40the.sikandar.dev%2Fpostgresql-next-js-drizzle-orm-a-step-by-step-guide-cb487b1a3ca3&source=---footer_actions--cb487b1a3ca3---------------------bookmark_footer------------------)
[![Sikandar Dev](https://miro.medium.com/v2/resize:fill:48:48/1*sNNiHdylwXTlhUUv68ee6Q.png)](https://medium.com/@the.sikandar.dev?source=post_page---post_author_info--cb487b1a3ca3---------------------------------------)
[![Sikandar Dev](https://miro.medium.com/v2/resize:fill:64:64/1*sNNiHdylwXTlhUUv68ee6Q.png)](https://medium.com/@the.sikandar.dev?source=post_page---post_author_info--cb487b1a3ca3---------------------------------------)
Follow
## [Written by Sikandar Dev](https://medium.com/@the.sikandar.dev?source=post_page---post_author_info--cb487b1a3ca3---------------------------------------)
[1 follower](https://medium.com/@the.sikandar.dev/followers?source=post_page---post_author_info--cb487b1a3ca3---------------------------------------)
·[1 following](https://medium.com/@the.sikandar.dev/following?source=post_page---post_author_info--cb487b1a3ca3---------------------------------------)
Sharing programming tips, coding experiments, and lessons learned from building real projects.
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----cb487b1a3ca3---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----cb487b1a3ca3---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----cb487b1a3ca3---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cb487b1a3ca3---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----cb487b1a3ca3---------------------------------------)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cb487b1a3ca3---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cb487b1a3ca3---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cb487b1a3ca3---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----cb487b1a3ca3---------------------------------------)
To make Medium work, we log user data. By using Medium, you agree to our [Privacy Policy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9), including cookie policy.


## Source: https://neon.com/docs/guides/drizzle-migrations

[Team accounts with unlimited members now available to everyone! Invite your teammates and ship faster together, even on the Free Plan. ![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fleft-pattern.0ggh6pmfsjnge.png&w=2048&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fright-pattern.0om3izpcvesnf.png&w=2048&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fleft-pattern-xl.0btjnvn399m8c.png&w=1920&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fright-pattern-xl.06ipzujqzypwp.png&w=1080&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fleft-pattern-lg.12jbotg9.30te.png&w=828&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fright-pattern-lg.0km-ihtg_aba4.png&w=640&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fleft-pattern-sm.0cgdd6kib75s0.png&w=1080&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fright-pattern-sm.01~ruf.6y8.1b.png&w=640&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)![](https://neon.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fleft-pattern-xs.09.p8gofv73xu.png&w=640&q=100&dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu)](https://neon.com/docs/changelog/2026-03-13)
[Neon](https://neon.com/)
[Docs](https://neon.com/docs)
Search...⌘K
Ask AI
[](https://discord.gg/92vNTzKDGp)[](https://github.com/neondatabase/neon)
[Log in](https://console.neon.tech/login)[Sign up](https://console.neon.tech/signup)
  * [Get started](https://neon.com/docs/introduction)
  * [About](https://neon.com/docs/introduction/architecture-overview)
  * Connect
    * [](https://neon.com/docs/connect/connect-intro)
    * [](https://neon.com/docs/connect/query-with-psql-editor)
    * [](https://neon.com/docs/connect/connection-errors)
  * Develop
    * Frontend & Frameworks
      * [](https://neon.com/docs/get-started/frameworks)
      * [](https://neon.com/docs/get-started/languages)
      * [](https://neon.com/docs/get-started/orms)
    * Backend
      * [](https://neon.com/docs/data-api/overview)
      * [](https://neon.com/docs/auth/overview)
      * [](https://neon.com/docs/guides/row-level-security)
    * AI
      * [](https://neon.com/docs/ai/ai-agents-tools)
      * [](https://neon.com/docs/ai/ai-intro)
    * Tools & Workflows
      * [](https://neon.com/docs/reference/api-reference)
      * [](https://neon.com/docs/local/neon-local)
      * [](https://neon.com/docs/guides/integrations)
      * [](https://neon.com/docs/reference/claimable-postgres)
      * [](https://neon.com/templates)
      * [](https://github.com/neondatabase/examples)
  * Manage
    * [](https://neon.com/docs/manage/platform)
    * [](https://neon.com/docs/introduction/about-billing)
    * [](https://neon.com/docs/security/security-overview)
  * Postgres
    * [](https://neon.com/docs/extensions/pg-extensions)
    * [](https://neon.com/docs/postgresql/introduction)
    * [](https://neon.com/docs/reference/compatibility)
    * [](https://neon.com/docs/postgresql/postgres-version-policy)
    * [](https://neon.com/docs/postgresql/postgres-upgrade)
    * [](https://neon.com/postgresql/tutorial)
  * Resources
    * [](https://neon.com/docs/introduction/status)
    * [](https://neon.com/docs/introduction/support)
    * [](https://neon.com/docs/changelog)
    * [](https://neon.com/docs/introduction/roadmap)
    * [](https://neon.com/docs/introduction/early-access)
    * [](https://neon.com/docs/community/community-intro)
    * [](https://neon.com/docs/reference/glossary)
    * [](https://neon.com/docs/reference/feeds)
  * [Platform integration](https://neon.com/docs/guides/platform-integration-overview)


Search...⌘K
Ask AI
Full Neon documentation index: <https://neon.com/docs/llms.txt>
[](https://neon.com/docs/guides/integrations)
  * Authentication
    * [Auth0 ](https://neon.com/docs/guides/auth-auth0)
    * [Auth.js ](https://neon.com/docs/guides/auth-authjs)
    * [Clerk ](https://neon.com/docs/guides/auth-clerk)
    * [Okta ](https://neon.com/docs/guides/auth-okta)
  * Deploy
    * [Cloudflare ](https://neon.com/docs/guides/cloudflare-pages)
      * [Cloudflare Pages ](https://neon.com/docs/guides/cloudflare-pages)
      * [Cloudflare Workers ](https://neon.com/docs/guides/cloudflare-workers)
    * [Deno ](https://neon.com/docs/guides/deno)
    * [Heroku ](https://neon.com/docs/guides/heroku)
    * [Koyeb ](https://neon.com/docs/guides/koyeb)
    * [Netlify Functions ](https://neon.com/docs/guides/netlify-functions)
    * [Railway ](https://neon.com/docs/guides/railway)
    * [Render ](https://neon.com/docs/guides/render)
    * [Vercel ](https://neon.com/docs/guides/vercel-overview)
      * [Integration Overview ](https://neon.com/docs/guides/vercel-overview)
      * [Vercel-Managed (Native Integration) ](https://neon.com/docs/guides/vercel-managed-integration)
      * [Neon-Managed (Connectable Account) ](https://neon.com/docs/guides/neon-managed-vercel-integration)
      * [Managing preview branch cleanup ](https://neon.com/docs/guides/vercel-branch-cleanup)
      * [Manual Setup ](https://neon.com/docs/guides/vercel-manual)
      * [Connecting to Neon from Vercel ](https://neon.com/docs/guides/vercel-connection-methods)
      * [Migrating from Vercel Postgres ](https://neon.com/docs/guides/vercel-postgres-transition-guide)
  * Develop
    * [Convex ](https://neon.com/guides/convex-neon)
    * [GitHub integration ](https://neon.com/docs/guides/neon-github-integration)
    * [Knex ](https://neon.com/docs/guides/knex)
    * [Prisma ](https://neon.com/docs/guides/prisma)
    * [TypeORM ](https://neon.com/docs/guides/typeorm)
  * File & media storage
    * [File storage ](https://neon.com/docs/guides/file-storage)
    * [AWS S3 ](https://neon.com/docs/guides/aws-s3)
    * [Azure Blob Storage ](https://neon.com/docs/guides/azure-blob-storage)
    * [Backblaze B2 ](https://neon.com/docs/guides/backblaze-b2)
    * [Cloudflare R2 ](https://neon.com/docs/guides/cloudflare-r2)
    * [Cloudinary ](https://neon.com/docs/guides/cloudinary)
    * [ImageKit ](https://neon.com/docs/guides/imagekit)
    * [Uploadcare ](https://neon.com/docs/guides/uploadcare)
  * Query
    * [AskYourDatabase ](https://neon.com/docs/guides/askyourdatabase)
    * [Cloudflare Hyperdrive ](https://neon.com/docs/guides/cloudflare-hyperdrive)
    * [Draxlr ](https://neon.com/docs/guides/draxlr)
    * [Exograph ](https://neon.com/docs/guides/exograph)
    * [Grafbase ](https://neon.com/docs/guides/grafbase)
    * [Hasura ](https://neon.com/docs/guides/hasura)
    * [PostgREST ](https://neon.com/docs/guides/postgrest)
    * [WunderGraph ](https://neon.com/docs/guides/wundergraph)
  * Replicate from Neon
    * [Airbyte ](https://neon.com/docs/guides/logical-replication-airbyte)
    * [Bemi ](https://neon.com/docs/guides/bemi)
    * [ClickHouse ](https://neon.com/docs/guides/logical-replication-clickhouse)
    * [Confluent ](https://neon.com/docs/guides/logical-replication-kafka-confluent)
    * [Databricks ](https://neon.com/docs/guides/logical-replication-databricks)
    * [Decodable ](https://neon.com/docs/guides/logical-replication-decodable)
    * [Estuary Flow ](https://neon.com/docs/guides/logical-replication-estuary-flow)
    * [Fivetran ](https://neon.com/docs/guides/logical-replication-fivetran)
    * [Inngest ](https://neon.com/docs/guides/logical-replication-inngest)
    * [Materialize ](https://neon.com/docs/guides/logical-replication-materialize)
    * [Neon to Neon ](https://neon.com/docs/guides/logical-replication-neon-to-neon)
    * [Postgres ](https://neon.com/docs/guides/logical-replication-postgres)
    * [Prisma Pulse ](https://neon.com/docs/guides/logical-replication-prisma-pulse)
    * [Sequin ](https://neon.com/docs/guides/sequin)
    * [Snowflake ](https://neon.com/docs/guides/logical-replication-airbyte-snowflake)
  * Replicate to Neon
    * [AlloyDB ](https://neon.com/docs/guides/logical-replication-alloydb)
    * [AWS RDS ](https://neon.com/docs/guides/logical-replication-rds-to-neon)
    * [Cloud SQL ](https://neon.com/docs/guides/logical-replication-cloud-sql)
    * [Neon to Neon ](https://neon.com/docs/guides/logical-replication-neon-to-neon)
    * [Postgres ](https://neon.com/docs/guides/logical-replication-postgres-to-neon)
    * [Replicate from Azure ](https://neon.com/docs/import/migrate-from-azure-postgres)
    * [Replicate from Supabase ](https://neon.com/docs/guides/logical-replication-supabase-to-neon)
  * Schema Migration
    * [Django ](https://neon.com/docs/guides/django-migrations)
    * [Drizzle ](https://neon.com/docs/guides/drizzle-migrations)
    * [Entity Framework ](https://neon.com/docs/guides/entity-migrations)
    * [Flyway ](https://neon.com/docs/guides/flyway)
      * [Get started ](https://neon.com/docs/guides/flyway)
      * [Manage multiple environments ](https://neon.com/docs/guides/flyway-multiple-environments)
    * [Laravel ](https://neon.com/docs/guides/laravel-migrations)
    * [Liquibase ](https://neon.com/docs/guides/liquibase)
      * [Get started ](https://neon.com/docs/guides/liquibase)
      * [Developer workflow ](https://neon.com/docs/guides/liquibase-workflow)
    * [Prisma ](https://neon.com/docs/guides/prisma-migrations)
    * [Rails ](https://neon.com/docs/guides/rails-migrations)
    * [Sequelize ](https://neon.com/docs/guides/sequelize)
    * [SQLAlchemy ](https://neon.com/docs/guides/sqlalchemy-migrations)
  * Serverless
    * [AWS Lambda ](https://neon.com/docs/guides/aws-lambda)
    * [Azure Functions ](https://neon.com/guides/query-postgres-azure-functions)
    * [Neon serverless driver ](https://neon.com/docs/serverless/serverless-driver)
    * [Trigger serverless functions with Inngest ](https://neon.com/docs/guides/trigger-serverless-functions)


[](https://neon.com/docs)/[Integrations (3rd party)](https://neon.com/docs/guides/integrations)/Schema Migration/Drizzle
# Schema migration with Neon Postgres and Drizzle ORM
Set up Neon Postgres and run migrations for your TypeScript project using Drizzle ORM
Copy page
[Drizzle](https://orm.drizzle.team/) is a TypeScript-first ORM that connects to all major databases and works across most Javascript runtimes. It provides a simple way to define database schemas and queries in an SQL-like dialect and tools to generate and run migrations.
This guide shows how to use `Drizzle` with the `Neon` Postgres database in a Typescript project. We'll create a simple Node.js application with `Hono.js` and demonstrate the full workflow of setting up and working with your database using `Drizzle`.
##  Prerequisites[](https://neon.com/docs/guides/drizzle-migrations#prerequisites)
To follow along with this guide, you will need:
  * A Neon account. If you do not have one, sign up at [Neon](https://neon.tech). Your Neon project comes with a ready-to-use Postgres database named `neondb`. We'll use this database in the following examples.
  * [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed on your local machine. We'll use Node.js to build and test the application locally.


##  Setting up your Neon database[](https://neon.com/docs/guides/drizzle-migrations#setting-up-your-neon-database)
###  Initialize a new project[](https://neon.com/docs/guides/drizzle-migrations#initialize-a-new-project)
  1. Log in to the Neon Console and navigate to the [Projects](https://console.neon.tech/app/projects) section.
  2. Select a project or click the `New Project` button to create a new one.


###  Retrieve your Neon database connection string[](https://neon.com/docs/guides/drizzle-migrations#retrieve-your-neon-database-connection-string)
Find your database connection string by clicking the **Connect** button on your **Project Dashboard** to open the **Connect to your database** modal. It should look similar to this:

```
postgresql://alex:AbC123dEf@ep-cool-darkness-123456.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require
```

Keep your connection string handy for later use.
#### note
Neon supports both direct and pooled database connection strings, which you can find by clicking the **Connect** button on your **Project Dashboard** to open the **Connect to your database** modal. A pooled connection string connects your application to the database via a PgBouncer connection pool, allowing for a higher number of concurrent connections. However, using a pooled connection string for migrations can lead to errors. For this reason, we recommend using a direct (non-pooled) connection when performing migrations. For more information about direct and pooled connections, see [Connection pooling](https://neon.com/docs/connect/connection-pooling).
##  Setting up the TypeScript application[](https://neon.com/docs/guides/drizzle-migrations#setting-up-the-typescript-application)
###  Create a new Hono.js project[](https://neon.com/docs/guides/drizzle-migrations#create-a-new-honojs-project)
We'll create a simple catalog, with API endpoints that query the database for authors and a list of their books. Run the following command in your terminal to set up a new project using `Hono.js`:

```
npm create hono@latest neon-drizzle-guide
```

This initiates an interactive CLI prompt to set up a new project. To follow along with this guide, you can use the following settings:

```
Need to install the following packages:
create-hono@0.9.0
Ok to proceed? (y) y

create-hono version 0.9.0
✔ Using target directory … neon-drizzle-guide
✔ Which template do you want to use? › nodejs
cloned honojs/starter#main to ./repos/javascript/neon-drizzle-guide
✔ Do you want to install project dependencies? … yes
✔ Which package manager do you want to use? › npm
```

To use Drizzle and connect to the Neon database, we also add the `drizzle-orm` and `drizzle-kit` packages to our project, along with the `Neon serverless` driver library.

```
cd neon-drizzle-guide && touch .env
npm install drizzle-orm @neondatabase/serverless
npm install -D drizzle-kit dotenv
```

Add the `DATABASE_URL` environment variable to your `.env` file, which you'll use to connect to our Neon database. Use the connection string that you obtained from the Neon Console earlier:

```
# .env
DATABASE_URL=NEON_DATABASE_CONNECTION_STRING
```

Test that the starter `Hono.js` application works by running `npm run dev` in the terminal. You should see the `Hello, Hono!` message when you navigate to `http://localhost:3000` in your browser.
###  Set up the database schema[](https://neon.com/docs/guides/drizzle-migrations#set-up-the-database-schema)
Now, we will define the schema for the application using the `Drizzle` ORM. Create a new `schema.ts` file in your `src` directory and add the following code:

```
// src/schema.ts

import { pgTable, integer, serial, text, timestamp } from 'drizzle-orm/pg-core';

export const authors = pgTable('authors', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  bio: text('bio'),
  createdAt: timestamp('created_at').notNull().defaultNow(),
});

export const books = pgTable('books', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  authorId: integer('author_id').references(() => authors.id),
  createdAt: timestamp('created_at').notNull().defaultNow(),
});
```

The code defines two tables: `authors`, which will contain the list of all the authors, and `books`, which will contain the list of books written by the authors. Each book is associated with an author using the `authorId` field.
To generate a migration to create these tables in the database, we'll use the `drizzle-kit` command. Add the following script to the `package.json` file at the root of your project:

```
{
  "scripts": {
    "db:generate": "drizzle-kit generate --dialect=postgresql --schema=src/schema.ts --out=./drizzle"
  }
}
```

Then, run the following command in your terminal to generate the migration files:

```
npm run db:generate
```

This command generates a new folder named `drizzle` containing the migration files for the `authors` and `books` tables.
###  Run the migration[](https://neon.com/docs/guides/drizzle-migrations#run-the-migration)
The generated migration file is written in SQL and contains the necessary commands to create the tables in the database. To apply these migrations, we'll use the [Neon serverless driver](https://neon.com/docs/serverless/serverless-driver) and helper functions provided by the `drizzle-orm` library.
Create a new `migrate.ts` in your `src` directory and add the following code:

```
// src/migrate.ts

import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
import { migrate } from 'drizzle-orm/neon-http/migrator';
import { config } from 'dotenv';

config({ path: '.env' });

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle(sql);

const main = async () => {
  try {
    await migrate(db, { migrationsFolder: 'drizzle' });
    console.log('Migration completed');
  } catch (error) {
    console.error('Error during migration:', error);
    process.exit(1);
  }
};

main();
```

The `drizzle-orm` package comes with an integration for `Neon`, which allows us to run the migrations using the `migrate` function. Add a new script to the `package.json` file that executes the migration.

```
{
  "scripts": {
    "db:migrate": "tsx ./src/migrate.ts"
  }
}
```

You can now run the migration script using the following command:

```
npm run db:migrate
```

You should see the `Migration completed` message in the terminal, indicating that the migration was successful.
###  Seed the database[](https://neon.com/docs/guides/drizzle-migrations#seed-the-database)
To test the application works, we need to add some example data to our tables. Create a new file at `src/seed.ts` and add the following code to it:

```
// src/seed.ts

import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
import { authors, books } from './schema';
import { config } from 'dotenv';

config({ path: '.env' });

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle(sql);

async function seed() {
  await db.insert(authors).values([
    {
      name: 'J.R.R. Tolkien',
      bio: 'The creator of Middle-earth and author of The Lord of the Rings.',
    },
    {
      name: 'George R.R. Martin',
      bio: 'The author of the epic fantasy series A Song of Ice and Fire.',
    },
    {
      name: 'J.K. Rowling',
      bio: 'The creator of the Harry Potter series.',
    },
  ]);

  const authorRows = await db.select().from(authors);
  const authorIds = authorRows.map((row) => row.id);

  await db.insert(books).values([
    {
      title: 'The Fellowship of the Ring',
      authorId: authorIds[0],
    },
    {
      title: 'The Two Towers',
      authorId: authorIds[0],
    },
    {
      title: 'The Return of the King',
      authorId: authorIds[0],
    },
    {
      title: 'A Game of Thrones',
      authorId: authorIds[1],
    },
    {
      title: 'A Clash of Kings',
      authorId: authorIds[1],
    },
    {
      title: "Harry Potter and the Philosopher's Stone",
      authorId: authorIds[2],
    },
    {
      title: 'Harry Potter and the Chamber of Secrets',
      authorId: authorIds[2],
    },
  ]);
}

async function main() {
  try {
    await seed();
    console.log('Seeding completed');
  } catch (error) {
    console.error('Error during seeding:', error);
    process.exit(1);
  }
}

main();
```

This script inserts some seed data into the `authors` and `books` tables. Add a new script to the `package.json` file that runs the seeding program.

```
{
  "scripts": {
    "db:seed": "tsx ./src/seed.ts"
  }
}
```

Run the seed script using the following command:

```
npm run db:seed
```

You should see the `Seeding completed` message in the terminal, indicating that the seed data was inserted into the database.
###  Implement the API endpoints[](https://neon.com/docs/guides/drizzle-migrations#implement-the-api-endpoints)
Now that the database is set up and populated with data, we can implement the API to query the authors and their books. Replace the existing `src/index.ts` file with the following code:

```
// src/index.ts

import { serve } from '@hono/node-server';
import { Hono } from 'hono';
import { env } from 'hono/adapter';
import { config } from 'dotenv';

import { eq } from 'drizzle-orm';
import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
import { authors, books } from './schema';

config({ path: '.env' });
const app = new Hono();

app.get('/', (c) => {
  return c.text('Hello, this is a catalog of books!');
});

app.get('/authors', async (c) => {
  const { DATABASE_URL } = env<{ DATABASE_URL: string }>(c);
  const sql = neon(DATABASE_URL);
  const db = drizzle(sql);

  const output = await db.select().from(authors);
  return c.json(output);
});

app.get('/books/:authorId', async (c) => {
  const { DATABASE_URL } = env<{ DATABASE_URL: string }>(c);
  const sql = neon(DATABASE_URL);
  const db = drizzle(sql);

  const authorId = c.req.param('authorId');
  const output = await db
    .select()
    .from(books)
    .where(eq(books.authorId, Number(authorId)));
  return c.json(output);
});

const port = 3000;
console.log(`Server is running on port ${port}`);

serve({
  fetch: app.fetch,
  port,
});
```

This code sets up a simple API with two endpoints: `/authors` and `/books/:authorId`. The `/authors` endpoint returns a list of all the authors, and the `/books/:authorId` endpoint returns a list of books written by the specific author with the given `authorId`.
Run the application using the following command:

```
npm run dev
```

This will start a `Hono.js` server at `http://localhost:3000`. Navigate to `http://localhost:3000/authors` and `http://localhost:3000/books/1` in your browser to check that the API works as expected.
##  Migration after a schema change[](https://neon.com/docs/guides/drizzle-migrations#migration-after-a-schema-change)
To demonstrate how to execute a schema change, we'll add a new column to the `authors` table, listing the country of origin for each author.
###  Generate the new migration[](https://neon.com/docs/guides/drizzle-migrations#generate-the-new-migration)
Modify the code in the `src/schema.ts` file to add the new column to the `authors` table:

```
// src/schema.ts

import { pgTable, integer, serial, text, timestamp } from 'drizzle-orm/pg-core';

export const authors = pgTable('authors', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  bio: text('bio'),
  country: text('country'),
  createdAt: timestamp('created_at').notNull().defaultNow(),
});

export const books = pgTable('books', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  authorId: integer('author_id').references(() => authors.id),
  createdAt: timestamp('created_at').notNull().defaultNow(),
});
```

Now, we can run the following command to generate a new migration file:

```
npm run db:generate
```

This command generates a new migration file in the `drizzle` folder, with the SQL command to add the new column to the `authors` table.
###  Run the migration[](https://neon.com/docs/guides/drizzle-migrations#run-the-migration)
Run the migration script using the following command:

```
npm run db:migrate
```

You should see the `Migration completed` message in the terminal, indicating it was successful.
###  Verify the schema change[](https://neon.com/docs/guides/drizzle-migrations#verify-the-schema-change)
To verify that the schema change was successful, run the application using the following command:

```
npm run dev
```

You can navigate to `http://localhost:3000/authors` in your browser to check that each author entry has a `country` field, currently set to `null`.
##  Conclusion[](https://neon.com/docs/guides/drizzle-migrations#conclusion)
In this guide, we set up a new TypeScript project using `Hono.js` and `Drizzle` ORM and connected it to a `Neon` Postgres database. We created a schema for the database, generated and ran migrations, and implemented API endpoints to query the database.
##  Source code[](https://neon.com/docs/guides/drizzle-migrations#source-code)
You can find the source code for the application described in this guide on GitHub.
  * [![](https://neon.com/_next/static/media/pattern.0bu1f.rwl1ln~.svg?dpl=dpl_Hr2V9VztBAN28TdN8UasVZGP6sdu) Migrations with Neon and Drizzle Run Neon database migrations using Drizzle ](https://github.com/neondatabase/guide-neon-drizzle)


##  Resources[](https://neon.com/docs/guides/drizzle-migrations#resources)
For more information on the tools used in this guide, refer to the following resources:
  * [Drizzle ORM](https://orm.drizzle.team/)
  * [Hono.js](https://hono.dev/)


##  Need help?[](https://neon.com/docs/guides/drizzle-migrations#need-help)
Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](https://neon.com/docs/introduction/support).
Was this page helpful?
YesNo
Thank you for your feedback!
[Edit on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/guides/drizzle-migrations.md)
[Previous Django](https://neon.com/docs/guides/django-migrations)[Next Entity Framework](https://neon.com/docs/guides/entity-migrations)
  * [Prerequisites](https://neon.com/docs/guides/drizzle-migrations#prerequisites)
  * [Setting up your Neon database](https://neon.com/docs/guides/drizzle-migrations#setting-up-your-neon-database)
  * [Setting up the TypeScript application](https://neon.com/docs/guides/drizzle-migrations#setting-up-the-typescript-application)
  * [Migration after a schema change](https://neon.com/docs/guides/drizzle-migrations#migration-after-a-schema-change)
  * [Conclusion](https://neon.com/docs/guides/drizzle-migrations#conclusion)
  * [Source code](https://neon.com/docs/guides/drizzle-migrations#source-code)
  * [Resources](https://neon.com/docs/guides/drizzle-migrations#resources)
  * [Need help?](https://neon.com/docs/guides/drizzle-migrations#need-help)


Set up Neon with AI
Copy neon init command
Neon Docs
[Neon](https://neon.com/)
A Databricks Company
[Neon status loading...](https://neonstatus.com/)
© Neon 2026. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the [Apache Software Foundation](https://www.apache.org).
[Privacy Notice](https://www.databricks.com/legal/privacynotice)[Terms of Use](https://www.databricks.com/legal/terms-of-use)[Neon Platform Terms](https://neon.com/platform-terms)[Modern Slavery Statement](https://www.databricks.com/legal/modern-slavery-policy-statement)[California Privacy](https://www.databricks.com/legal/supplemental-privacy-notice-california-residents)
Company
  * [About](https://neon.com/about-us)
  * [Blog](https://neon.com/blog)
  * [Careers](https://www.databricks.com/company/careers/open-positions?department=engineering&location=all&itm_source=www&itm_category=company&itm_page=engineering-at-databricks&itm_location=body&itm_component=hero&itm_offer=open-positions)
  * [Contact Sales](https://neon.com/contact-sales)
  * [Security](https://neon.com/security)


Resources
  * [Docs](https://neon.com/docs)
  * [Changelog](https://neon.com/docs/changelog)
  * [Support](https://neon.com/docs/introduction/support)
  * [Community Guides](https://neon.com/guides)
  * [FAQs](https://neon.com/faqs)
  * [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial)
  * [Startups](https://neon.com/startups)


Community
  * [](https://discord.gg/92vNTzKDGp)
  * [](https://github.com/neondatabase/neon)
  * [](https://twitter.com/neondatabase/)
  * [](https://www.linkedin.com/company/neon-inc/)
  * [](https://www.youtube.com/channel/UCoMzQTJSIr7-RU1QbomQI2w)


Compliance
  * [CCPACompliant](https://trust.neon.com/?itemUid=4064ac33-7b48-407b-aed7-ce02971d1ec1)
  * [GDPRCompliant](https://trust.neon.com/?itemUid=45220873-6e51-4dbb-b1b1-37d66ee9ef95)
  * [ISO 27001Certified](https://trust.neon.com/?itemUid=1fed9faa-4a87-427c-9a95-96b4d6bf66b7)
  * [ISO 27701Certified](https://trust.neon.com/?itemUid=dc79cbc7-c99d-4eb9-891e-f5dc44b943d7)
  * [SOC 2Certified](https://trust.neon.com/?itemUid=7bfa66da-33ab-49de-8391-e329738a1ae9)
  * [HIPAACompliant](https://neon.com/docs/security/hipaa)
    * [Compliance Guide](https://neon.com/docs/security/hipaa)
    * [Neon’s Sub Contractors](https://neon.com/hipaa-contractors)
  * [Trust Center](https://trust.neon.com)


We use cookies to improve our services. Learn more in our [Cookie Policy](https://neon.com/cookie-policy).
Opt outAccept


## Source: https://medium.com/@tomas.gabrs/setting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c

[Sitemap](https://medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)
# Setting Up Drizzle ORM with Fastify in an NX Monorepo
[![Tomas Gabrs @ Tomio](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@tomas.gabrs?source=post_page---byline--fdd34229254c---------------------------------------)
[Tomas Gabrs @ Tomio](https://medium.com/@tomas.gabrs?source=post_page---byline--fdd34229254c---------------------------------------)
Follow
10 min read
·
Sep 24, 2024
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ffdd34229254c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&user=Tomas+Gabrs+%40+Tomio&userId=63a16f4f6d26&source=---header_actions--fdd34229254c---------------------clap_footer------------------)
50
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffdd34229254c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&source=---header_actions--fdd34229254c---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dfdd34229254c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&source=---header_actions--fdd34229254c---------------------post_audio_button------------------)
Share
## Story
As Tomio, I want to connect my Fastify API to a local file-based database,  
so that I can store and retrieve data dynamically from a single table, using Drizzle ORM.
Press enter or click to view image in full size
![Drizzle logo](https://miro.medium.com/v2/resize:fit:700/1*O99TAn77put-xOUF4U0c_Q.jpeg)
## Previous Steps
Previously, we established an NX monorepo as the foundation for our microservices, starting with a minimal Fastify application paired with Zod for schema validation. Alongside, we implemented ESLint rules to maintain consistent import sorting across the codebase. Now, we’re moving forward by introducing database support with Drizzle ORM.
  * [Creating NX Monorepo for Scalable Microservices Architecture](https://medium.com/@tomas.gabrs/creating-an-nx-monorepo-for-scalable-microservices-architecture-78b25dc7b7dd)
  * [Building a Fastify Application with Zod Validation in an NX Monorepo](https://medium.com/@tomas.gabrs/building-a-fastify-application-with-zod-validation-in-an-nx-monorepo-7c49ed6d77be)
  * [Establishing Consistent Import Sorting in an NX Monorepo](https://medium.com/@tomas.gabrs/establishing-consistent-import-sorting-in-an-nx-monorepo-64515b05968f)


## Why Drizzle ORM with libSQL?
Our Fastify API is currently serving hardcoded responses. To move beyond this, we opted for [Drizzle ORM](https://orm.drizzle.team/) to manage our database interactions. Drizzle stands out due to its type-safe approach and smooth integration with [libSQL](https://github.com/tursodatabase/libsql), a SQLite fork optimized for cloud use by [Turso](https://turso.tech/). Given that most of our microservices will handle simple data models, libSQL serves as a suitable lightweight solution. Should our needs evolve, we can easily scale to a more complex database.
### Installing Dependencies
Before diving into implementation, we need to install the required packages for Drizzle ORM and libSQL, based on [Drizzle documentation](https://orm.drizzle.team/docs/get-started-sqlite).

```
npm install drizzle-orm  
npm install -D drizzle-kit  
npm install @libsql/client
```

## Creating the CMS Service Database Library
In an NX monorepo, it’s best practice to encapsulate all database logic in a dedicated library. Using the `@nx/node` plugin, we generate the `cms-service-database` library.

```
nx generate @nx/node:library --name=cms-service-database --buildable=true --directory=libs/cms-service/database --importPath=@tomio-open/cms-service-database --projectNameAndRootFormat=as-provided --testEnvironment=node --unitTestRunner=none --no-interactive
```

### Database Schema
The schema is the core of our database. In Drizzle ORM, we [define the schema](https://orm.drizzle.team/docs/sql-schema-declaration) in a TypeScript file, which serves as the single source of truth for migrations and queries. For now, we keep things simple with a schema containing an `id`, `cmsKey`, and `value`.

```
// libs/cms-service/database/src/schema.ts  
import { randomUUID } from 'crypto';  
import { sqliteTable, text } from 'drizzle-orm/sqlite-core';  
  
export const texts = sqliteTable('texts', {  
  id: text('id', { length: 36 })  
    .primaryKey()  
    .$defaultFn(() => randomUUID()),  
  cmsKey: text('cms_key').notNull(),  
  value: text('value').notNull(),  
});
```

### Types
Before implementing additional logic in our library, we will first define the foundational types that will be used throughout.

```
// libs/cms-service/database/src/types.ts  
import { Config as DrizzleConfig } from 'drizzle-kit';  
import { InferSelectModel } from 'drizzle-orm';  
import { LibSQLDatabase } from 'drizzle-orm/libsql';  
  
import * as schema from './schema';  
  
export type Text = InferSelectModel<typeof schema.texts>;  
  
export type Config = DrizzleConfig;  
  
export type Database = LibSQLDatabase<typeof schema>;  
  
export type Repository = {  
  getTexts: () => Promise<Text[]>;  
};
```

We maintain strict typing throughout the database library:
  * `Text` — Inferred directly from the schema, ensuring changes in the schema are reflected in this type.
  * `Config`—A type for Drizzle ORM’s configuration.
  * `Database` — Typed as `LibSQLDatabase` with the defined schema.
  * `Repository` — A type for the repository, which will initially support only the `getTexts` method.


### Creating the Database
Next, we implement a `createDatabase` factory function. This function accepts a `databaseUrl` as a parameter, making the database configuration flexible for different environments (e.g., `local`, `dev`, `prod`).

```
// libs/cms-service/database/src/database.ts  
import { createClient } from '@libsql/client';  
import { drizzle } from 'drizzle-orm/libsql';  
  
import * as schema from './schema';  
import { Database } from './types';  
  
export const createDatabase = (url: string): Database => {  
  const client = createClient({  
    url,  
  });  
  
  const database = drizzle(client, {  
    schema,  
  });  
  
  return database;  
};
```

### Repository Implementation
The repository pattern decouples the database logic from the rest of the application. The `createRepository` function accepts the database instance and provides methods for interacting with the data, such as fetching all texts.

```
// libs/cms-service/database/src/repository.ts  
import { texts } from './schema';  
import { Database, Repository } from './types';  
  
export const createRepository = (database: Database): Repository => {  
  const getTexts = async () => {  
    return database.select().from(texts);  
  };  
  
  return {  
    getTexts,  
  };  
};
```

### Database Configuration
The final component we need to implement in our `cms-service-database` library is the configuration, which will be used by `drizzle-kit` for generating migration files, running database migrations, or using Drizzle Studio. While `drizzle-kit` scripts can accept command-line arguments or load a configuration file, we chose to use a configuration file to centralize and manage all settings in one place.

```
// libs/cms-service/database/src/config.ts  
import { defineConfig } from 'drizzle-kit';  
import { resolve } from 'path';  
  
import { Config } from './types';  
  
const baseConfig: Pick<Config, 'migrations'> & {  
  dialect: 'sqlite';  
  driver: 'turso';  
} = {  
  dialect: 'sqlite',  
  driver: 'turso',  
  migrations: {  
    prefix: 'timestamp',  
  },  
};  
  
// To be used in applications, it needs absolute paths to schema and migrations.  
export const createDatabaseConfig = (url: string): Config => {  
  return defineConfig({  
    ...baseConfig,  
    schema: resolve(__dirname, './schema.ts'),  
    out: resolve(__dirname, '../migrations'),  
    dbCredentials: {  
      url,  
    },  
  });  
};  
  
// To be used in this library, it needs relative paths from project.json to schema and migrations.  
export default defineConfig({  
  ...baseConfig,  
  schema: './src/schema.ts',  
  out: './migrations',  
});
```

We create two exports in our config.ts:
  * `baseConfig`: Used internally within the `cms-service-database` library for generating independent migration scripts.
  * `createDatabaseConfig`: A factory method used in the` cms-service-api` application, allowing us to configure the database for different environments.


For more details on configuring `drizzle-kit` and its specific properties, refer to the [documentation page](https://orm.drizzle.team/kit-docs/config-reference).
### Library Exports
Once the `cms-service-database` library is fully implemented, we can export the key components to be used in other applications or libraries:

```
// libs/cms-service/database/src/index.ts  
export { createDatabaseConfig } from './config';  
export { createDatabase } from './database';  
export { createRepository } from './repository';  
export { Config, Database, Repository, Text } from './types';
```

This exports all the necessary factories and types for reuse across the projects.
### Generating Database Migrations
With the schema defined, we’re ready to generate migrations using `drizzle-kit`. We add a target to `project.json` to simplify this process:

```
// libs/cms-service/database/project.json  
"db:generate": {  
  "executor": "nx:run-commands",  
  "options": {  
    "command": "drizzle-kit generate --config=./src/config.ts",  
    "cwd": "libs/cms-service/database"  
  }  
}
```

Running this target generates migration files based on the schema, ensuring the database structure stays in sync with the code:

```
nx run cms-service-database:db:generate
```

When executed, `drizzle-kit` will:
  1. Load the `config.ts` file.
  2. Use the `schema` property to locate the defined schema.
  3. Generate database migrations that match the schema, formatted according to the specified `dialect` and `driver`.
  4. Save the migration files to the location specified by the `out` property, with a timestamp prefix based on the `migrations.prefix` property.


Additionally, it will generate some meta files for internal usage. Once this step is complete, the database setup is ready to be integrated into our Fastify application.
## Integrating the Database with Fastify
### Setting Up the Environment and Cleaning Up `project.json`
Now that we’re prepared to connect our Fastify application to the database, we need to consider the various environments in which our application may run. Common environments include `local`, `development`, `testing`, `UAT`, and `production`. For now, we’ll focus on setting up only the `local` environment, with plans to iterate on additional environments later.
## Get Tomas Gabrs @ Tomio’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
In an NX monorepo, environment configurations are defined in the `project.json` file. In our `cms-service-api`, there are currently two configurations for the `build` and `serve` targets: `development` and `production`. We will remove the `production` configuration and rename the `development` configuration to `local`.
The best practice for configuring environments is to use `.env` files. According to [NX documentation](https://nx.dev/recipes/tips-n-tricks/define-environment-variables), we will create a `.env.local` file for our local environment. When any target runs with the `local` configuration, it will load the environment variables from this file. We will define the database URL within this file:

```
# apps/cms-service-api/.env.local  
DATABASE_URL=file:/path-to-project/tomio-open/apps/cms-service-api/local.db
```

When using libSQL locally, we can specify the database URL as an absolute file path that points to our database file. Additionally, we will create a `.env.example` file for each application:

```
# apps/cms-service-api/.env.example  
DATABASE_URL=
```

It’s important to avoid pushing environment files to GitHub, as they may contain sensitive information. To prevent this, we will add new rules to our `.gitignore` file, ensuring that all environment files except `.env.example` are ignored by Git:

```
# .gitignore  
# environments  
.env*  
!.env.example
```

With this setup, our local environment is ready, and we can now use the `DATABASE_URL` in our application.
### Database Configuration
To utilize Drizzle Kit and execute database migrations in our local environment, we need to create a configuration for the database.

```
// apps/cms-service-api/src/config/database.ts  
import { createDatabaseConfig } from '@tomio-open/cms-service-database';  
  
const databaseConfig = createDatabaseConfig(process.env.DATABASE_URL);  
  
export default databaseConfig;
```

In this code, we use the `createDatabaseConfig` factory exported from the `cms-service-database` library, supplying it with the URL to our local database as defined in our `.env.local` file. By exporting this configuration, we ensure that Drizzle Kit scripts can easily load and utilize it.
### Creating Migration Target
With our database configuration in place, we can now set up a migration target for our application.

```
"db:migrate": {  
  "executor": "nx:run-commands",  
  "defaultConfiguration": "local",  
  "options": {  
    "command": "drizzle-kit migrate --config=./src/config/database.ts",  
    "cwd": "apps/cms-service-api"  
  },  
  "configurations": {  
    "local": {}  
  }  
}
```

In this setup, we’ve defined the `db:migrate` target. When executed, it will load the database configuration and run migrations from our `cms-service-database` library against the database specified in our `.env.local` file:

```
nx run cms-service-api:db:migrate
```

Upon running this command, the database file located at `apps/cms-service-api/local.db` should be created, indicating that our database is ready for use. To prevent pushing this local database file to GitHub, we will update our `.gitignore` as follows:

```
# .gitignore  
# local databases  
*.db*
```

With these configurations, we are now fully prepared to utilize our database within the API.
### Fastify Plugin
While it’s possible to use our database and repository directly within each route, a more efficient approach is to create a Fastify plugin. This allows us to instantiate the database and repository once and make them available across all routes.
Here’s how to implement the plugin:

```
// apps/cms-service-api/src/app/plugins/repository.ts  
import fp from 'fastify-plugin';  
  
import {  
  createDatabase,  
  createRepository,  
} from '@tomio-open/cms-service-database';  
import { ZodFastifyInstance } from '@tomio-open/zod-fastify';  
  
type RepositoryOptions = {  
  databaseUrl: string;  
};  
  
export const repositoryPlugin = fp(  
  async (fastify: ZodFastifyInstance, options: RepositoryOptions) => {  
    const database = createDatabase(options.databaseUrl);  
    const repository = createRepository(database);  
  
    fastify.decorate('repository', repository);  
  }  
);  
  
// apps/cms-service-api/src/app/plugins/index.ts  
export { repositoryPlugin } from './repository';  
export { sensiblePlugin } from './sensible';
```

The `repositoryPlugin` initializes the database and passes it to the repository factory. Once the repository is created, we decorate the Fastify instance with it. After registering this plugin in our application, we can seamlessly access the repository in all our routes.
### Using the Repository in Route Handlers
To utilize the repository in our routes, we first need to register the plugin in our Fastify application.
Here’s how to do that:

```
// apps/cms-service-api/src/app/app.ts  
import { ZodFastifyInstance } from '@tomio-open/zod-fastify';  
  
import { repositoryPlugin, sensiblePlugin } from './plugins';  
import { routes } from './routes';  
  
type AppOptions = {  
  databaseUrl: string;  
};  
  
export const app = async (fastify: ZodFastifyInstance, options: AppOptions) => {  
  fastify.register(sensiblePlugin);  
  fastify.register(repositoryPlugin, {  
    databaseUrl: options.databaseUrl,  
  });  
  
  fastify.register(routes, { prefix: '/api' });  
};
```

Next, when we register our application with Fastify, we must pass the `databaseUrl`:

```
// apps/cms-service-api/src/main.ts  
server.register(app, {  
  databaseUrl: process.env.DATABASE_URL,  
});
```

After registering the plugin, the Fastify instance will have a new `repository` property, which we can use in our route handlers.
Here’s how to define a route that uses the repository:

```
// apps/cms-service-api/src/app/routes/root.ts  
import { z } from 'zod';  
  
import { ZodFastifyInstance } from '@tomio-open/zod-fastify';  
  
export const routes = async (fastify: ZodFastifyInstance) => {  
  fastify.get(  
    '/',  
    {  
      schema: {  
        response: {  
          200: z.object({  
            data: z.array(  
              z.object({  
                id: z.string(),  
                cmsKey: z.string(),  
                value: z.string(),  
              })  
            ),  
          }),  
        },  
      },  
    },  
    async () => {  
      const data = await fastify.repository.getTexts();  
  
      return { data };  
    }  
  );  
};
```

However, we encounter an error indicating that the property `repository` does not exist on type `ZodFastifyInstance`. This is because TypeScript is not aware that we decorated the instance inside our plugin.
To resolve this, we need to augment the `FastifyInstance` in our `repositoryPlugin`:

```
// apps/cms-service-api/src/app/plugins/repository.ts  
import {  
  createDatabase,  
  createRepository,  
  Repository,  
} from '@tomio-open/cms-service-database';  
  
declare module 'fastify' {  
  interface FastifyInstance {  
    repository: Repository;  
  }  
}
```

With this change, TypeScript now recognizes the `repository` property on `FastifyInstance`, providing autocomplete support in our IDE with the correct types.
## Test setup
We’re now ready to verify our implementation. Run the following command to `lint`, `build`, and `serve` the `cms-service-api`:

```
nx run-many -t lint build serve
```

This command will lint all projects, build them, and start the `cms-service-api`. We shouldn't encounter any errors. When we navigate to `localhost:3000/api/root`, we should see the response `{"data":[]}`. This is expected since our database is currently empty. We will add some data in the next step.
## Conclusion
We successfully integrated a local file-based database with our Fastify application using Drizzle ORM. We explored the essential steps, including setting up environment configurations, creating a robust database configuration, and developing a Fastify plugin to manage our repository efficiently. With a clean and organized approach, we ensured that our application can easily interact with the database while maintaining scalability and flexibility.
## Next Steps
Currently, our API is returning empty data. While we won’t be creating an endpoint for data creation just yet, we’ll be adding Drizzle Studio to our application. This will enable us to inspect our database and create new records through a user-friendly interface. After that, we will connect our application to a remote libSQL database hosted on Turso.
## Resources
  * [Drizzle ORM](https://orm.drizzle.team/)
  * [libSQL](https://github.com/tursodatabase/libsql)
  * [Turso](https://turso.tech/)
  * [Drizzle with Turso](https://orm.drizzle.team/docs/get-started-sqlite)
  * [Drizzle SQL Schema Declaration](https://orm.drizzle.team/docs/sql-schema-declaration)
  * [Drizzle Kit](https://orm.drizzle.team/kit-docs/overview)
  * [Configuring Drizzle Kit](https://orm.drizzle.team/kit-docs/config-reference)
  * [NX Environment Variables](https://nx.dev/recipes/tips-n-tricks/define-environment-variables)


## Tomio Open
_At_** _Tomio Open_** _, we are dedicated to building software solutions for non-profit organizations, focusing entirely on giving back to the community. We take no profit from our work for these organizations and believe in the power of collaboration and open education. Through our articles, we share our journey and insights, helping fellow developers learn from our experiences. Stay connected with us as we continue to create impactful solutions and spread knowledge for the greater good._
[Nx](https://medium.com/tag/nx?source=post_page-----fdd34229254c---------------------------------------)
[Drizzle](https://medium.com/tag/drizzle?source=post_page-----fdd34229254c---------------------------------------)
[Typescript](https://medium.com/tag/typescript?source=post_page-----fdd34229254c---------------------------------------)
[JavaScript](https://medium.com/tag/javascript?source=post_page-----fdd34229254c---------------------------------------)
[Fastify](https://medium.com/tag/fastify?source=post_page-----fdd34229254c---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ffdd34229254c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&user=Tomas+Gabrs+%40+Tomio&userId=63a16f4f6d26&source=---footer_actions--fdd34229254c---------------------clap_footer------------------)
50
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ffdd34229254c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&user=Tomas+Gabrs+%40+Tomio&userId=63a16f4f6d26&source=---footer_actions--fdd34229254c---------------------clap_footer------------------)
50
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffdd34229254c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tomas.gabrs%2Fsetting-up-drizzle-orm-with-fastify-in-an-nx-monorepo-fdd34229254c&source=---footer_actions--fdd34229254c---------------------bookmark_footer------------------)
[![Tomas Gabrs @ Tomio](https://miro.medium.com/v2/resize:fill:48:48/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@tomas.gabrs?source=post_page---post_author_info--fdd34229254c---------------------------------------)
[![Tomas Gabrs @ Tomio](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@tomas.gabrs?source=post_page---post_author_info--fdd34229254c---------------------------------------)
Follow
## [Written by Tomas Gabrs @ Tomio](https://medium.com/@tomas.gabrs?source=post_page---post_author_info--fdd34229254c---------------------------------------)
[7 followers](https://medium.com/@tomas.gabrs/followers?source=post_page---post_author_info--fdd34229254c---------------------------------------)
·[0 following](https://medium.com/@tomas.gabrs/following?source=post_page---post_author_info--fdd34229254c---------------------------------------)
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----fdd34229254c---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----fdd34229254c---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----fdd34229254c---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----fdd34229254c---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----fdd34229254c---------------------------------------)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----fdd34229254c---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----fdd34229254c---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----fdd34229254c---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----fdd34229254c---------------------------------------)
To make Medium work, we log user data. By using Medium, you agree to our [Privacy Policy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9), including cookie policy.


## Source: https://orm.drizzle.team/docs/migrations

[We've merged alternation-engine into Beta release. Try it out!](https://github.com/drizzle-team/drizzle-orm/releases/tag/v1.0.0-beta.2)
[ ](https://orm.drizzle.team/) [ Documentation ](https://orm.drizzle.team/docs/overview)
Search`K`
[ 33k+ ](https://github.com/drizzle-team/drizzle-orm) [ ](https://orm.drizzle.team/announcements)
meet drizzle
[ Get started ](https://orm.drizzle.team/docs/get-started)[ Sustainability ](https://orm.drizzle.team/docs/sustainability)[ Why Drizzle? ](https://orm.drizzle.team/docs/overview)[ Guides ](https://orm.drizzle.team/docs/guides)[ Tutorials ](https://orm.drizzle.team/docs/tutorials)[ Latest releases ](https://orm.drizzle.team/docs/latest-releases)[ Gotchas ](https://orm.drizzle.team/docs/gotchas)
Upgrade to v1.0 RC
[ How to upgrade? ](https://orm.drizzle.team/docs/upgrade-v1)[ Relational Queries v1 to v2 ](https://orm.drizzle.team/docs/relations-v1-v2)
Fundamentals
[ Schema ](https://orm.drizzle.team/docs/sql-schema-declaration)[ Relations ](https://orm.drizzle.team/docs/relations-schema-declaration)[ Database connection ](https://orm.drizzle.team/docs/connect-overview)[ Query Data ](https://orm.drizzle.team/docs/data-querying)[ Migrations ](https://orm.drizzle.team/docs/migrations)
Connect 
[ PostgreSQL ](https://orm.drizzle.team/docs/get-started-postgresql)[ Gel ](https://orm.drizzle.team/docs/get-started-gel)[ MySQL ](https://orm.drizzle.team/docs/get-started-mysql)[ SQLite ](https://orm.drizzle.team/docs/get-started-sqlite)[ MSSQL ](https://orm.drizzle.team/docs/get-started-mssql)[ CockroachDB ](https://orm.drizzle.team/docs/get-started-cockroach)[ SingleStore ](https://orm.drizzle.team/docs/get-started-singlestore)[ PlanetScale Postgres ](https://orm.drizzle.team/docs/connect-planetscale-postgres)[ Neon ](https://orm.drizzle.team/docs/connect-neon)[ Vercel Postgres ](https://orm.drizzle.team/docs/connect-vercel-postgres)[ Prisma Postgres ](https://orm.drizzle.team/docs/connect-prisma-postgres)[ Supabase ](https://orm.drizzle.team/docs/connect-supabase)[ Xata ](https://orm.drizzle.team/docs/connect-xata)[ PGLite ](https://orm.drizzle.team/docs/connect-pglite)[ Nile ](https://orm.drizzle.team/docs/connect-nile)[ Bun SQL ](https://orm.drizzle.team/docs/connect-bun-sql)[ Effect Postgres ](https://orm.drizzle.team/docs/connect-effect-postgres)[ Netlify Database ](https://orm.drizzle.team/docs/connect-netlify-db)[ PlanetScale MySQL ](https://orm.drizzle.team/docs/connect-planetscale)[ TiDB ](https://orm.drizzle.team/docs/connect-tidb)[ Turso Cloud ](https://orm.drizzle.team/docs/connect-turso)[ Turso Database ](https://orm.drizzle.team/docs/connect-turso-database)[ SQLite Cloud ](https://orm.drizzle.team/docs/connect-sqlite-cloud)[ Cloudflare D1 ](https://orm.drizzle.team/docs/connect-cloudflare-d1)[ Bun SQLite ](https://orm.drizzle.team/docs/connect-bun-sqlite)[ Node SQLite ](https://orm.drizzle.team/docs/connect-node-sqlite)[ Cloudflare Durable Objects ](https://orm.drizzle.team/docs/connect-cloudflare-do)[ Expo SQLite ](https://orm.drizzle.team/docs/connect-expo-sqlite)[ OP SQLite ](https://orm.drizzle.team/docs/connect-op-sqlite)[ React Native SQLite ](https://orm.drizzle.team/docs/connect-react-native-sqlite)[ AWS Data API Postgres ](https://orm.drizzle.team/docs/connect-aws-data-api-pg)[ AWS Data API MySQL ](https://orm.drizzle.team/docs/connect-aws-data-api-mysql)[ Drizzle Proxy ](https://orm.drizzle.team/docs/connect-drizzle-proxy)
Expand
Manage schema
[ Data types ](https://orm.drizzle.team/docs/column-types/pg)[ Indexes & Constraints ](https://orm.drizzle.team/docs/indexes-constraints)[ Sequences ](https://orm.drizzle.team/docs/sequences)[ Views ](https://orm.drizzle.team/docs/views)[ Schemas ](https://orm.drizzle.team/docs/schemas)[ Drizzle Relations ](https://orm.drizzle.team/docs/relations-v2)[ Row-Level Security (RLS) ](https://orm.drizzle.team/docs/rls)[ Extensions ](https://orm.drizzle.team/docs/extensions/pg)[ [OLD] Drizzle Relations ](https://orm.drizzle.team/docs/relations)
Migrations
[ Overview ](https://orm.drizzle.team/docs/kit-overview)[ `generate` ](https://orm.drizzle.team/docs/drizzle-kit-generate)[ `migrate` ](https://orm.drizzle.team/docs/drizzle-kit-migrate)[ `push` ](https://orm.drizzle.team/docs/drizzle-kit-push)[ `pull` ](https://orm.drizzle.team/docs/drizzle-kit-pull)[ `export` ](https://orm.drizzle.team/docs/drizzle-kit-export)[ `check` ](https://orm.drizzle.team/docs/drizzle-kit-check)[ `up` ](https://orm.drizzle.team/docs/drizzle-kit-up)[ `studio` ](https://orm.drizzle.team/docs/drizzle-kit-studio)[ Custom migrations ](https://orm.drizzle.team/docs/kit-custom-migrations)[ Migrations for teams ](https://orm.drizzle.team/docs/kit-migrations-for-teams)[ Web and mobile ](https://orm.drizzle.team/docs/kit-web-mobile)[ drizzle.config.ts ](https://orm.drizzle.team/docs/drizzle-config-file)
Seeding
[ Overview ](https://orm.drizzle.team/docs/seed-overview)[ Generators ](https://orm.drizzle.team/docs/seed-functions)[ Versioning ](https://orm.drizzle.team/docs/seed-versioning)
Access your data
[ Query ](https://orm.drizzle.team/docs/rqb-v2)[ Select ](https://orm.drizzle.team/docs/select)[ Insert ](https://orm.drizzle.team/docs/insert)[ Update ](https://orm.drizzle.team/docs/update)[ Delete ](https://orm.drizzle.team/docs/delete)[ Filters ](https://orm.drizzle.team/docs/operators)[ Utils ](https://orm.drizzle.team/docs/query-utils)[ Joins ](https://orm.drizzle.team/docs/joins)[ Magic sql`` operator ](https://orm.drizzle.team/docs/sql)[ [OLD] Query V1 ](https://orm.drizzle.team/docs/rqb)
Performance
[ Queries ](https://orm.drizzle.team/docs/perf-queries)[ Serverless ](https://orm.drizzle.team/docs/perf-serverless)
Advanced
[ Set Operations ](https://orm.drizzle.team/docs/set-operations)[ Generated Columns ](https://orm.drizzle.team/docs/generated-columns)[ Transactions ](https://orm.drizzle.team/docs/transactions)[ Batch ](https://orm.drizzle.team/docs/batch-api)[ Cache ](https://orm.drizzle.team/docs/cache)[ Dynamic query building ](https://orm.drizzle.team/docs/dynamic-query-building)[ Read Replicas ](https://orm.drizzle.team/docs/read-replicas)[ Custom types ](https://orm.drizzle.team/docs/custom-types)[ Goodies ](https://orm.drizzle.team/docs/goodies)
Validations
[ zod ](https://orm.drizzle.team/docs/zod)[ valibot ](https://orm.drizzle.team/docs/valibot)[ typebox ](https://orm.drizzle.team/docs/typebox)[ arktype ](https://orm.drizzle.team/docs/arktype)[ typebox-legacy ](https://orm.drizzle.team/docs/typebox-legacy)[ effect-schema ](https://orm.drizzle.team/docs/effect-schema)
Extensions
[ Prisma ](https://orm.drizzle.team/docs/prisma)[ ESLint Plugin ](https://orm.drizzle.team/docs/eslint-plugin)[ drizzle-graphql ](https://orm.drizzle.team/docs/graphql)
System Light Dark
[ Become a Sponsor ](https://driz.link/sponsor) [ Twitter ](https://mobile.twitter.com/DrizzleORM) [ Discord ](https://discord.gg/yfjTbVXMW4)
[ v1.0 98% ](https://orm.drizzle.team/roadmap)
[ Benchmarks ](https://orm.drizzle.team/benchmarks) [ Extension ](https://driz.link/extension) [ Studio ](https://orm.drizzle.team/drizzle-studio/overview) [ Studio Package ](https://github.com/drizzle-team/drizzle-studio-npm) [ Gateway ](https://gateway.drizzle.team) [ Drizzle Run ](https://drizzle.run)
Our goodies!
[ Our Primary backer ![](https://orm.drizzle.team/docs/migrations) ![PlanetScale](https://orm.drizzle.team/docs/migrations) ](https://driz.link/planetscale) [ Our Cloud Partner ![](https://orm.drizzle.team/docs/migrations) ![Railway](https://orm.drizzle.team/docs/migrations) ](https://driz.link/railway)
[ ![](https://orm.drizzle.team/docs/migrations) ![Neon](https://orm.drizzle.team/docs/migrations) ](https://driz.link/neon)[ ![](https://orm.drizzle.team/docs/migrations) ![SQLite Cloud](https://orm.drizzle.team/docs/migrations) ](https://driz.link/sqlitecloud)[ ![](https://orm.drizzle.team/docs/migrations) ![Upstash](https://orm.drizzle.team/docs/migrations) ](https://driz.link/upstash)[ ![](https://orm.drizzle.team/docs/migrations) ![Lokalise](https://orm.drizzle.team/docs/migrations) ](https://driz.link/lokalise)[ ![](https://orm.drizzle.team/docs/migrations) ![Replit](https://orm.drizzle.team/docs/migrations) ](https://driz.link/replit)[ ![](https://orm.drizzle.team/docs/migrations) ![Sentry](https://orm.drizzle.team/docs/migrations) ](https://driz.link/sentry)[ ![](https://orm.drizzle.team/docs/migrations) ![Sevalla](https://orm.drizzle.team/docs/migrations) ](https://driz.link/sevalla)[ ![](https://orm.drizzle.team/docs/migrations) ![Clerk](https://orm.drizzle.team/docs/migrations) ](https://clerk.com)[ ![](https://orm.drizzle.team/docs/migrations) ![Warp](https://orm.drizzle.team/docs/migrations) ](https://driz.link/warp)[ ![](https://orm.drizzle.team/docs/migrations) ![Turso](https://orm.drizzle.team/docs/migrations) 🚀 Drizzle is giving you 10% off Turso Scaler and Pro for 1 Year 🚀 ](https://driz.link/turso)[ ![](https://orm.drizzle.team/docs/migrations) ![Payload](https://orm.drizzle.team/docs/migrations) ](https://driz.link/payload)[ ![](https://orm.drizzle.team/docs/migrations) ![Xata](https://orm.drizzle.team/docs/migrations) ](https://driz.link/xataio)[ ![](https://orm.drizzle.team/docs/migrations) ![Sponsor](https://orm.drizzle.team/docs/migrations) ](https://driz.link/sponsor)
Product by Drizzle Team 
[ One Dollar Stats $1 per mo web analytics christmas   
deal  ](https://driz.link/onedollarstats)
# Drizzle migrations fundamentals
SQL databases require you to specify a **strict schema** of entities you’re going to store upfront and if (when) you need to change the shape of those entities - you will need to do it via **schema migrations**.
There’re multiple production grade ways of managing database migrations. Drizzle is designed to perfectly suits all of them, regardless of you going **database first** or **codebase first**.
**Database first** is when your database schema is a source of truth. You manage your database schema either directly on the database or via database migration tools and then you pull your database schema to your codebase application level entities.
**Codebase first** is when database schema in your codebase is a source of truth and is under version control. You declare and manage your database schema in JavaScript/TypeScript and then you apply that schema to the database itself either with Drizzle, directly or via external migration tools.
#### How can Drizzle help?[](https://orm.drizzle.team/docs/migrations#how-can-drizzle-help)
We’ve built [**drizzle-kit**](https://orm.drizzle.team/docs/kit-overview) - CLI app for managing migrations with Drizzle.

```
drizzle-kit migrate
drizzle-kit generate
drizzle-kit push
drizzle-kit pull
```

It is designed to let you choose how to approach migrations based on your current business demands.
It fits in both database and codebase first approaches, it lets you **push your schema** or **generate SQL migration** files or **pull the schema** from database. It is perfect wether you work alone or in a team.
  

* * *
**Now let’s pick the best option for your project:**
**Option 1**
> I manage database schema myself using external migration tools or by running SQL migrations directly on my database. From Drizzle I just need to get current state of the schema from my database and save it as TypeScript schema file.
Expand details
That’s a **database first** approach. You have your database schema as a **source of truth** and Drizzle lets you pull database schema to TypeScript using [`drizzle-kit pull`](https://orm.drizzle.team/docs/drizzle-kit-pull) command.

```
                                  ┌────────────────────────┐      ┌─────────────────────────┐ 
                                  │                        │ <---  CREATE TABLE "users" (
┌──────────────────────────┐      │                        │        "id" SERIAL PRIMARY KEY,
│ ~ drizzle-kit pull       │      │                        │        "name" TEXT,
└─┬────────────────────────┘      │        DATABASE        │        "email" TEXT UNIQUE
  │                               │                        │       );
  └ Pull datatabase schema -----> │                        │
  ┌ Generate Drizzle       <----- │                        │
  │ schema TypeScript file        └────────────────────────┘
  │
  v
```

```
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(),
});
```

**Option 2**
> I want to have database schema in my TypeScript codebase, I don’t wanna deal with SQL migration files.  
>  I want Drizzle to “push” my schema directly to the database
Expand details
That’s a **codebase first** approach. You have your TypeScript Drizzle schema as a **source of truth** and Drizzle lets you push schema changes to the database using [`drizzle-kit push`](https://orm.drizzle.team/docs/drizzle-kit-push) command.
That’s the best approach for rapid prototyping and we’ve seen dozens of teams and solo developers successfully using it as a primary migrations flow in their production applications.
src/schema.ts
```
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(), // <--- added column
});
```

```
Add column to `users` table                                                                          
┌──────────────────────────┐                  
│ + email: text().unique() │                  
└─┬────────────────────────┘                  
  │                                           
  v                                           
┌──────────────────────────┐                  
│ ~ drizzle-kit push       │                  
└─┬────────────────────────┘                  
  │                                           ┌──────────────────────────┐
  └ Pull current datatabase schema ---------> │                          │
                                              │                          │
  ┌ Generate alternations based on diff <---- │         DATABASE         │
  │                                           │                          │
  └ Apply migrations to the database -------> │                          │
                                       │      └──────────────────────────┘
                                       │
  ┌────────────────────────────────────┴──────────────┐
   ALTER TABLE `users` ADD COLUMN `email` TEXT UNIQUE; 
```

**Option 3**
> I want to have database schema in my TypeScript codebase, I want Drizzle to generate SQL migration files for me and apply them to my database
Expand details
That’s a **codebase first** approach. You have your TypeScript Drizzle schema as a source of truth and Drizzle lets you generate SQL migration files based on your schema changes with [`drizzle-kit generate`](https://orm.drizzle.team/docs/drizzle-kit-generate) and then apply them to the database with [`drizzle-kit migrate`](https://orm.drizzle.team/docs/drizzle-kit-migrate) commands.
src/schema.ts
```
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(),
});
```

```
┌────────────────────────┐                  
│ $ drizzle-kit generate │                  
└─┬──────────────────────┘                  
  │                                           
  └ 1. read previous migration folders
    2. find diff between current and previous schema
    3. prompt developer for renames if necessary
  ┌ 4. generate SQL migration and persist to file
  │    ┌─┴───────────────────────────────────────┐  
  │      📂 drizzle       
  │      └ 📂 20242409125510_premium_mister_fear
  │        ├ 📜 snapshot.json
  │        └ 📜 migration.sql
  v
```

```
-- drizzle/20242409125510_premium_mister_fear/migration.sql

CREATE TABLE "users" (
 "id" SERIAL PRIMARY KEY,
 "name" TEXT,
 "email" TEXT UNIQUE
);
```

```
┌───────────────────────┐                  
│ $ drizzle-kit migrate │                  
└─┬─────────────────────┘                  
  │                                                         ┌──────────────────────────┐                                         
  └ 1. read migration.sql files in migrations folder        │                          │
    2. fetch migration history from database -------------> │                          │
  ┌ 3. pick previously unapplied migrations <-------------- │         DATABASE         │
  └ 4. apply new migration to the database ---------------> │                          │
                                                            │                          │
                                                            └──────────────────────────┘
[✓] done!                                                 
```

**Option 4**
> I want to have database schema in my TypeScript codebase, I want Drizzle to generate SQL migration files for me and I want Drizzle to apply them during runtime
Expand details
That’s a **codebase first** approach. You have your TypeScript Drizzle schema as a source of truth and Drizzle lets you generate SQL migration files based on your schema changes with [`drizzle-kit generate`](https://orm.drizzle.team/docs/drizzle-kit-generate) and then you can apply them to the database during runtime of your application.
This approach is widely used for **monolithic** applications when you apply database migrations during zero downtime deployment and rollback DDL changes if something fails. This is also used in **serverless** deployments with migrations running in **custom resource** once during deployment process.
src/schema.ts
```
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(),
});
```

```
┌────────────────────────┐                  
│ $ drizzle-kit generate │                  
└─┬──────────────────────┘                  
  │                                           
  └ 1. read previous migration folders
    2. find diff between current and previous schema
    3. prompt developer for renames if necessary
  ┌ 4. generate SQL migration and persist to file
  │    ┌─┴───────────────────────────────────────┐  
  │      📂 drizzle       
  │      └ 📂 20242409125510_premium_mister_fear
  │        ├ 📜 snapshot.json
  │        └ 📜 migration.sql
  v
```

```
-- drizzle/20242409125510_premium_mister_fear/migration.sql

CREATE TABLE "users" (
 "id" SERIAL PRIMARY KEY,
 "name" TEXT,
 "email" TEXT UNIQUE
);
```

```
// index.ts
import { drizzle } from "drizzle-orm/node-postgres"
import { migrate } from 'drizzle-orm/node-postgres/migrator';

const db = drizzle(process.env.DATABASE_URL);

await migrate(db);
```

```
┌───────────────────────┐                  
│ npx tsx src/index.ts  │                  
└─┬─────────────────────┘                  
  │                                                      
  ├ 1. init database connection                             ┌──────────────────────────┐                                         
  └ 2. read migration.sql files in migrations folder        │                          │
    3. fetch migration history from database -------------> │                          │
  ┌ 4. pick previously unapplied migrations <-------------- │         DATABASE         │
  └ 5. apply new migration to the database ---------------> │                          │
                                                            │                          │
                                                            └──────────────────────────┘
[✓] done!                                                 
```

**Option 5**
> I want to have database schema in my TypeScript codebase, I want Drizzle to generate SQL migration files for me, but I will apply them to my database myself or via external migration tools
Expand details
That’s a **codebase first** approach. You have your TypeScript Drizzle schema as a source of truth and Drizzle lets you generate SQL migration files based on your schema changes with [`drizzle-kit generate`](https://orm.drizzle.team/docs/drizzle-kit-generate) and then you can apply them to the database either directly or via external migration tools.
src/schema.ts
```
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(),
});
```

```
┌────────────────────────┐                  
│ $ drizzle-kit generate │                  
└─┬──────────────────────┘                  
  │                                           
  └ 1. read previous migration folders
    2. find diff between current and previous scheama
    3. prompt developer for renames if necessary
  ┌ 4. generate SQL migration and persist to file
  │    ┌─┴───────────────────────────────────────┐  
  │      📂 drizzle       
  │      └ 📂 20242409125510_premium_mister_fear
  │        ├ 📜 snapshot.json
  │        └ 📜 migration.sql
  v
```

```
-- drizzle/20242409125510_premium_mister_fear/migration.sql

CREATE TABLE "users" (
 "id" SERIAL PRIMARY KEY,
 "name" TEXT,
 "email" TEXT UNIQUE
);
```

```
┌───────────────────────────────────┐                  
│ (._.) now you run your migrations │           
└─┬─────────────────────────────────┘  
  │
 directly to the database
  │                                         ┌────────────────────┐
  ├────────────────────────────────────┬───>│                    │  
  │                                    │    │      Database      │           
 or via external tools                 │    │                    │   
  │                                    │    └────────────────────┘
  │  ┌────────────────────┐            │      
  └──│ Bytebase           ├────────────┘         
     ├────────────────────┤  
     │ Liquibase          │
     ├────────────────────┤ 
     │ Atlas              │
     ├────────────────────┤ 
     │ etc…               │
     └────────────────────┘

[✓] done!                                                 
```

**Option 6**
> I want to have database schema in my TypeScript codebase, I want Drizzle to output the SQL representation of my Drizzle schema to the console, and I will apply them to my database via [Atlas](https://atlasgo.io/guides/orms/drizzle)
Expand details
That’s a **codebase first** approach. You have your TypeScript Drizzle schema as a source of truth and Drizzle lets you export SQL statements based on your schema changes with [`drizzle-kit export`](https://orm.drizzle.team/docs/drizzle-kit-generate) and then you can apply them to the database via [Atlas](https://atlasgo.io/guides/orms/drizzle) or other external SQL migration tools.
src/schema.ts
```
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(),
});
```

```
┌────────────────────────┐                  
│ $ drizzle-kit export   │                  
└─┬──────────────────────┘                  
  │                                           
  └ 1. read your drizzle schema
    2. generated SQL representation of your schema
  ┌ 3. outputs to console
  │    
  │        
  v
```

```
CREATE TABLE "users" (
 "id" SERIAL PRIMARY KEY,
 "name" TEXT,
 "email" TEXT UNIQUE
);
```

```
┌───────────────────────────────────┐                  
│ (._.) now you run your migrations │           
└─┬─────────────────────────────────┘  
  │
 via Atlas
  │                                    ┌──────────────┐
  │  ┌────────────────────┐            │              │
  └──│ Atlas              ├───────────>│  Database    │      
     └────────────────────┘            │              │       
                                       └──────────────┘

[✓] done!                                                 
```



## Source: https://medium.com/@ndmangrule/comprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9

[Sitemap](https://medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)
# Comprehensive Guide to Test-Driven Development (TDD) with React
[![Nitin Mangrule](https://miro.medium.com/v2/resize:fill:32:32/1*cfacQvlE-Muk_2hrqWwKBw@2x.jpeg)](https://medium.com/@ndmangrule?source=post_page---byline--ed7e0cdea9d9---------------------------------------)
[Nitin Mangrule](https://medium.com/@ndmangrule?source=post_page---byline--ed7e0cdea9d9---------------------------------------)
Follow
23 min read
·
Feb 10, 2025
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fed7e0cdea9d9&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&user=Nitin+Mangrule&userId=76d05ddc4a2b&source=---header_actions--ed7e0cdea9d9---------------------clap_footer------------------)
21
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed7e0cdea9d9&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&source=---header_actions--ed7e0cdea9d9---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Ded7e0cdea9d9&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&source=---header_actions--ed7e0cdea9d9---------------------post_audio_button------------------)
Share
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*j6OQ75GsoqrBLu1DYi2zYw.png)
## Introduction
### Why TDD is Crucial for Scalable React Applications
As React applications grow in complexity, ensuring reliability and maintainability becomes a challenge. Test-Driven Development (TDD) addresses these challenges by enforcing a structured approach to writing code.
TDD ensures that every piece of logic is verified before implementation, reducing the risk of regressions as the application scales. In a large codebase, small changes can have unintended side effects. With TDD, developers receive immediate feedback through failing tests, making it easier to track down issues before they reach production.
Moreover, TDD encourages writing modular, loosely coupled code. Since tests are written first, developers naturally structure their components and functions in a way that makes them testable and reusable, improving overall software design.
### Benefits of TDD for Maintainability, Scalability, and Team Collaboration
  1. **Maintainability**


  * Since TDD enforces test coverage from the start, the codebase remains robust and resistant to regressions.
  * Refactoring becomes safer because developers have an existing suite of tests to validate changes.
  * Debugging becomes faster as issues are caught early in the development cycle.


**2. Scalability**
  * As applications grow, well-tested components and modules can be confidently reused in different parts of the project.
  * When onboarding new developers, a strong test suite serves as living documentation, helping them understand expected behaviors without deep-diving into the entire codebase.
  * A well-tested codebase allows teams to confidently introduce new features without fear of breaking existing functionality.


**3. Team Collaboration**
  * TDD fosters better communication among developers, designers, and product managers by ensuring features are well-defined before implementation.
  * Since TDD enforces a “test-first” mindset, it encourages modularity and clean separation of concerns, making it easier for teams to work on different parts of the codebase simultaneously.
  * Teams using TDD tend to follow coding best practices, resulting in more consistent and readable code.


### Addressing Common Myths About TDD
  1. **“TDD Slows Down Development”**


Initially, TDD may feel slower due to the discipline required to write tests first. However, in the long run, it significantly reduces debugging time and regressions, leading to **faster overall development**.
**2. “100% Test Coverage Means 100% Bug-Free Code”**
While high test coverage is beneficial, it doesn’t guarantee the absence of bugs. Effective TDD requires **writing meaningful tests** , not just achieving coverage metrics.
**3. “TDD is Only for Backend Development”**
Many frontend developers assume TDD is unnecessary in UI-heavy applications. However, in React, **component logic, state management, hooks, and API interactions all benefit from TDD** just as much as backend systems.
## Core Principles of TDD
### Red-Green-Refactor Cycle
The **Red-Green-Refactor** cycle is the fundamental workflow of TDD. This iterative process ensures code is built incrementally, with a focus on correctness and maintainability.
  1. **Red (Write a Failing Test)**


  * Define the expected behavior before implementing the actual functionality.
  * The test should fail initially since the feature does not yet exist. This step ensures the test is valid and properly written.


**2. Green (Implement the Minimum Code to Pass the Test)**
  * Write just enough code to make the test pass.
  * Avoid over-engineering at this stage — focus on making the test pass with minimal effort.


**3. Refactor (Optimize Code While Keeping Tests Green)**
  * Clean up the code, improve efficiency, and ensure readability without altering functionality.
  * All tests should continue to pass after refactoring.


This cycle is repeated for every new piece of functionality, ensuring continuous improvement of the codebase.
### Writing Minimal Failing Tests
One of the key principles of TDD is **writing the simplest possible test** that fails before implementation.
  * **Tests should be focused and precise.** Each test should cover a single aspect of functionality, making it easier to pinpoint issues.
  * **Avoid testing unnecessary details.** Tests should validate the behavior rather than implementation specifics, ensuring flexibility in refactoring.
  * **Write tests that reflect real-world usage.** This makes it easier to maintain tests as the application evolves.


For example, when building a simple counter component in React, the first test might be:

```
test('renders Counter with initial value 0', () => {  
  render(<Counter />);  
  expect(screen.getByText('Count: 0')).toBeInTheDocument();  
});
```

This test fails because the `Counter` component does not yet exist. This failure drives the implementation forward.
### Incremental Improvements with Refactoring
TDD enforces **small, iterative changes** rather than large, risky refactors. Once a test passes, developers refine the implementation while ensuring tests remain green.
  * **Remove duplication:** If multiple tests require the same setup, move it to a `beforeEach` function or utility.
  * **Optimize logic:** Replace brute-force solutions with more elegant implementations without altering behavior.
  * **Improve readability:** Refactor both production code and test code to maintain clarity.


For example, if a component initially manages state using local variables, after passing tests, it may be refactored to use the `useState` hook while ensuring all tests remain green.
### Testing Types: Unit, Integration, and End-to-End (E2E)
A robust test strategy in React applications involves three main types of tests:
  1. **Unit Tests**


  * Focus on testing individual components or functions in isolation.
  * Ensure that a component renders correctly and behaves as expected.
  * Example: Testing a button click updates state.


```
test('increments counter on button click', () => {  
   render(<Counter />);  
   fireEvent.click(screen.getByRole('button', { name: /increment/i }));  
   expect(screen.getByText('Count: 1')).toBeInTheDocument();   
});
```

**2. Integration Tests**
  * Test how multiple components work together.
  * Ensure data flows correctly between components and external dependencies (e.g., APIs, context providers).
  * Example: Testing a form component that interacts with an API.


```
test('submits form and displays success message', async () => {  
   render(<LoginForm />);  
   fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'user@example.com' } });  
   fireEvent.click(screen.getByRole('button', { name: /submit/i }));  
   expect(await screen.findByText('Login Successful')).toBeInTheDocument();   
});
```

**3. End-to-End (E2E) Tests**
  * Simulate real user interactions across the entire application.
  * Run tests in a browser environment using tools like Cypress or Playwright.
  * Example: Testing a login flow from entering credentials to navigating the dashboard.


```
it('allows a user to log in', () => {  
   cy.visit('/login');  
   cy.get('input[name=email]').type('user@example.com');  
   cy.get('input[name=password]').type('password123');  
   cy.get('button[type=submit]').click();  
   cy.url().should('include', '/dashboard');   
});
```

  * Each type of test serves a unique purpose, and **a well-balanced test suite includes all three levels** to ensure confidence in the application’s stability.


## Setting Up a TDD-Friendly React Environment
Before implementing TDD in a React project, it’s crucial to set up the right testing tools and configurations. A well-configured environment ensures smooth test execution, better debugging, and an overall improved development experience.
### Choosing the Right Testing Libraries: Jest, React Testing Library, Cypress, etc.
A successful TDD workflow in React requires selecting appropriate testing libraries based on different testing needs.
  * **Jest** : Jest is the de facto testing framework for React applications. It provides fast test execution, built-in mocking, and code coverage analysis. Jest is primarily used for unit and integration testing.
  * **React Testing Library (RTL)** : RTL is the recommended library for testing React components. It encourages testing from a user’s perspective rather than relying on implementation details. It works seamlessly with Jest.
  * **Cypress** : Cypress is a popular end-to-end testing framework that runs tests directly in the browser. It is ideal for testing complete user flows, such as form submissions and navigation.
  * **Playwright** : Similar to Cypress, Playwright provides reliable E2E testing across different browsers, including headless execution. It is useful for cross-browser testing.
  * **MSW (Mock Service Worker)** : MSW is useful for mocking API responses during integration and E2E tests. It intercepts network requests, enabling controlled testing of different API scenarios.


For most React applications, Jest and React Testing Library handle unit and integration tests, while Cypress or Playwright covers E2E tests.
### Configuring Jest for Efficient Testing
Jest is included by default in Create React App (CRA) projects. However, in a custom setup or Next.js application, Jest needs to be manually installed and configured.
To install Jest and React Testing Library, run:

```
npm install --save-dev jest @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

Next, configure Jest by creating a `jest.config.js` file:

```
module.exports = {  
  testEnvironment: "jsdom",  
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],  
  collectCoverage: true,  
  coverageReporters: ["json", "lcov", "text", "clover"],  
};
```

Inside `jest.setup.js`, configure React Testing Library:

```
import "@testing-library/jest-dom/extend-expect";
```

For improved test performance:
  * Use **test-specific mocks** instead of real API calls to speed up execution.
  * Run tests in **watch mode** (`jest --watch`) to automatically re-run tests when files change.
  * Use **coverage reports** (`jest --coverage`) to identify untested parts of the codebase.


### Using TypeScript with TDD for Better Type Safety
TypeScript enhances TDD by ensuring strict type safety and reducing runtime errors.
To set up Jest with TypeScript, install the necessary dependencies:

```
npm install --save-dev ts-jest @types/jest
```

Then, configure Jest to work with TypeScript in `jest.config.js`:

```
module.exports = {  
  preset: "ts-jest",  
  testEnvironment: "jsdom",  
};
```

With TypeScript, tests benefit from:
  * **Early error detection** by catching type mismatches before runtime.
  * **Better autocompletion** and **self-documenting tests** for improved developer experience.
  * **Easier refactoring** since TypeScript enforces type correctness across tests and production code.


By combining Jest, React Testing Library, and TypeScript, we ensure a strong foundation for writing test-driven React applications.
## Writing Your First TDD Test in React
TDD follows a simple philosophy: write a failing test first, implement the minimum required code to pass the test, and then refactor while keeping tests green.
### Breaking Down a Feature into Testable Units
When applying TDD, it’s essential to **break down the feature into small, testable units**.
For example, if the requirement is to build a simple **Counter** component, we can break it down into:
  1. The component should render with an initial count of `0`.
  2. The counter should increment when the “Increment” button is clicked.
  3. The counter should decrement when the “Decrement” button is clicked.


Each of these requirements translates into an individual test case.
### Writing a Failing Test for a Simple React Component
Start by creating a test file named `Counter.test.tsx`.

```
import { render, screen, fireEvent } from "@testing-library/react";  
import Counter from "./Counter";  
  
test("renders Counter with initial value 0", () => {  
  render(<Counter />);  
  expect(screen.getByText("Count: 0")).toBeInTheDocument();  
});
```

At this point, the test fails because the `Counter` component does not exist yet. This failure **drives the implementation forward**.
### Implementing the Component to Pass the Test
Next, create a `Counter.tsx` file with minimal implementation to pass the test.

```
import { useState } from "react";  
  
export default function Counter() {  
  const [count, setCount] = useState(0);  
  return (  
    <div>  
      <p>Count: {count}</p>  
      <button onClick={() => setCount(count + 1)}>Increment</button>  
      <button onClick={() => setCount(count - 1)}>Decrement</button>  
    </div>  
  );  
}
```

Run the test suite using:

```
npm test
```

The test should now pass, confirming that the component renders correctly with an initial count of `0`.
### Refactoring While Ensuring Tests Stay Green
Now that the test passes, we can safely refactor the code.
  * Extract repetitive logic into helper functions.
  * Improve accessibility by adding semantic HTML elements.
  * Ensure tests are resilient to minor UI changes by querying elements by their role instead of text content.


Updating the test file to use `getByRole` for better maintainability:

```
test("renders Counter with initial value 0", () => {  
  render(<Counter />);  
  expect(screen.getByRole("status")).toHaveTextContent("Count: 0");  
});
```

Updating the component to reflect this change:

```
export default function Counter() {  
  const [count, setCount] = useState(0);  
  return (  
      <div>  
        <p role="status">Count: {count}</p>  
        <button onClick={() => setCount(count + 1)}>Increment</button>  
        <button onClick={() => setCount(count - 1)}>Decrement</button>  
      </div>  
    );  
  }
```

Now, if we rerun our tests, they should still pass, ensuring our refactoring did not break any functionality.
This structured approach ensures that our component is built incrementally and tested at every stage, leading to a **more reliable and maintainable React application**.  
5. TDD for Component Development
When applying TDD to React components, it’s essential to understand different testing strategies for functional and class components, the role of snapshot tests, and how to simulate user interactions effectively.
### Testing Functional Components vs. Class Components
React has shifted towards functional components with hooks as the recommended approach for new applications. However, legacy codebases may still use class components, so understanding how to test both is beneficial.
**Testing Functional Components**
Functional components rely on hooks like `useState` and `useEffect` for state and side effects. Since these components are often stateless or have minimal internal logic, testing focuses on:
  * Rendering the correct UI based on props
  * Interacting with event handlers
  * Verifying state changes using `useState`
  * Mocking effects triggered by `useEffect`


Example test for a functional **Counter** component:

```
import { render, screen, fireEvent } from "@testing-library/react";  
import Counter from "./Counter";  
test("increments count when button is clicked", () => {  
  render(<Counter />);  
    
  const button = screen.getByText("Increment");  
  fireEvent.click(button);  
    
  expect(screen.getByText("Count: 1")).toBeInTheDocument();  
});
```

Since functional components rely on hooks, testing state changes ensures behavior remains predictable.
**Testing Class Components**
Class components manage state using `this.state` and handle updates with `setState`. Testing class components involves:
  * Verifying `state` updates correctly
  * Mocking lifecycle methods like `componentDidMount`
  * Testing instance methods


Example test for a **class-based Counter** component:

```
import { render, screen, fireEvent } from "@testing-library/react";  
import Counter from "./Counter";  
test("increments count when button is clicked", () => {  
  render(<Counter />);  
    
  const button = screen.getByText("Increment");  
  fireEvent.click(button);  
    
  expect(screen.getByText("Count: 1")).toBeInTheDocument();  
});
```

Though the testing process is similar, functional components have simpler, more predictable behavior. If working in a legacy codebase, converting class components to functional components can simplify testing.
### Writing Snapshot Tests and When to Use Them
Snapshot testing ensures that the UI does not change unexpectedly. It captures the rendered output of a component and compares it to a previously saved snapshot. If the output changes, the test fails, alerting developers to unintended modifications.
To install Jest’s snapshot testing utility, ensure `jest` is properly configured in your project.
Example of a snapshot test for a simple **Button** component:

```
import { render } from "@testing-library/react";  
import Button from "./Button";  
test("renders Button correctly", () => {  
  const { asFragment } = render(<Button label="Click Me" />);  
  expect(asFragment()).toMatchSnapshot();  
});
```

When the test runs, Jest generates a snapshot file storing the component’s rendered output. If the UI changes, developers must review and approve the update by running:

```
npm test -- -u
```

**When to Use Snapshot Tests**
  * Ideal for **static UI components** (buttons, icons, modals) that rarely change.
  * Useful for **visual regression testing** , ensuring CSS or layout changes do not break components.
  * Not recommended for dynamic components with frequently changing data, as snapshots can become fragile and lead to false positives.


### Simulating User Interactions with React Testing Library
User interaction is a crucial aspect of React applications. React Testing Library (RTL) provides utilities to simulate events and verify UI updates accordingly.
Example of testing a form submission:

```
import { render, screen, fireEvent } from "@testing-library/react";  
import LoginForm from "./LoginForm";  
test("submits form when user enters valid input", () => {  
  render(<LoginForm />);  
  fireEvent.change(screen.getByLabelText(/email/i), { target: { value: "user@example.com" } });  
  fireEvent.change(screen.getByLabelText(/password/i), { target: { value: "securePassword" } });  
  fireEvent.click(screen.getByRole("button", { name: /submit/i }));  
  expect(screen.getByText("Login successful")).toBeInTheDocument();  
});
```

RTL simulates real user interactions, such as filling out forms, clicking buttons, and triggering events. This ensures that components behave correctly when used in real-world scenarios.
## TDD with Hooks
Hooks introduced a new paradigm in React development. Since they encapsulate state and behavior, testing hooks ensures composability and reusability in complex applications.
### Testing Custom Hooks with `renderHook`
React Testing Library provides `@testing-library/react-hooks`, which simplifies testing custom hooks in isolation.
Example: Testing a **useCounter** hook

```
import { renderHook, act } from "@testing-library/react";  
import { useCounter } from "./useCounter";  
test("increments and decrements count", () => {  
  const { result } = renderHook(() => useCounter());  
  act(() => {  
    result.current.increment();  
  });  
  expect(result.current.count).toBe(1);  
  act(() => {  
    result.current.decrement();  
  });  
  expect(result.current.count).toBe(0);  
});
```

The `renderHook` utility allows testing hooks without mounting an actual component. `act()` ensures state updates are properly simulated within React’s event loop.
### Mocking API Calls Inside Hooks
Hooks that fetch data or interact with APIs require mocking network requests to ensure deterministic test results.
Example: Testing a **useFetchData** hook

```
import { renderHook, act } from "@testing-library/react";  
import { useFetchData } from "./useFetchData";  
import { rest } from "msw";  
import { setupServer } from "msw/node";  
  
const server = setupServer(  
  rest.get("/api/data", (req, res, ctx) => {  
    return res(ctx.json({ message: "Hello World" }));  
  })  
);  
beforeAll(() => server.listen());  
afterEach(() => server.resetHandlers());  
afterAll(() => server.close());  
test("fetches and returns data", async () => {  
  const { result, waitForNextUpdate } = renderHook(() => useFetchData());  
  await waitForNextUpdate();  
  expect(result.current.data).toEqual({ message: "Hello World" });  
  expect(result.current.loading).toBe(false);  
});
```

This approach ensures:
  * API requests are **mocked** using `msw`, preventing real network calls.
  * Hooks are tested in isolation without external dependencies.
  * Edge cases, such as network failures, can be simulated by modifying the mock response.


### Ensuring Hooks Remain Composable and Reusable
When designing hooks, consider:
  * Keeping hooks **pure** by avoiding direct DOM manipulations.
  * Making hooks **configurable** by accepting parameters instead of hardcoding logic.
  * Ensuring hooks work well with different state management solutions (e.g., React Context, Redux).


For example, a **useTheme** hook should allow dynamic configuration:tsx

```
import { useState, useEffect } from "react";  
export function useTheme(defaultTheme = "light") {  
  const [theme, setTheme] = useState(defaultTheme);  
  useEffect(() => {  
    document.body.className = theme;  
  }, [theme]);  
  return { theme, setTheme };  
}
```

By following these best practices, hooks remain reusable across multiple components and projects.
## TDD in Complex React Applications
As React applications grow in complexity, testing becomes more challenging due to global state management, server-side rendering, and asynchronous operations. TDD ensures that these complexities are handled in a structured and reliable manner.
### Testing Context Providers and Global State (Redux, Zustand, Recoil)
When an application relies on global state, components are often wrapped inside a **Context Provider** (React Context) or a state management library like **Redux** , **Zustand** , or **Recoil**. Testing these components requires simulating global state and ensuring interactions update state correctly.
**Testing React Context Providers**
For a **ThemeContext** that provides a light/dark mode toggle:

```
import { render, screen } from "@testing-library/react";  
import { ThemeProvider, useTheme } from "./ThemeContext";  
const ThemeComponent = () => {  
  const { theme } = useTheme();  
  return <p>Current theme: {theme}</p>;  
};  
test("provides the default theme", () => {  
  render(  
    <ThemeProvider>  
      <ThemeComponent />  
    </ThemeProvider>  
  );  
  expect(screen.getByText("Current theme: light")).toBeInTheDocument();  
});
```

Here, `ThemeProvider` is wrapped around a test component to ensure the correct theme is provided.
**Testing Redux with TDD**
For a Redux store with a counter:

```
import { render, screen } from "@testing-library/react";  
import { Provider } from "react-redux";  
import { store } from "./store";  
import Counter from "./Counter";  
test("renders with initial state", () => {  
  render(  
    <Provider store={store}>  
      <Counter />  
    </Provider>  
  );  
  expect(screen.getByText("Count: 0")).toBeInTheDocument();  
});
```

To test actions, dispatch an action and verify the UI updates correctly:

```
import { fireEvent } from "@testing-library/react";  
test("increments the counter", () => {  
  render(  
    <Provider store={store}>  
      <Counter />  
    </Provider>  
  );  
    
  fireEvent.click(screen.getByText("Increment"));  
  expect(screen.getByText("Count: 1")).toBeInTheDocument();  
});
```

**Testing Zustand and Recoil**
For Zustand, use `act()` to trigger state changes:

```
import { renderHook, act } from "@testing-library/react";  
import { useCounterStore } from "./store";  
test("increments state", () => {  
  const { result } = renderHook(() => useCounterStore());  
  act(() => result.current.increment());  
  expect(result.current.count).toBe(1);  
});
```

Recoil’s testing requires using `<RecoilRoot>` to provide state context:

```
import { RecoilRoot } from "recoil";  
import { counterState } from "./atoms";  
import { useRecoilState } from "recoil";  
test("reads and updates recoil state", () => {  
  render(  
    <RecoilRoot>  
      <CounterComponent />  
    </RecoilRoot>  
  );  
  fireEvent.click(screen.getByText("Increment"));  
  expect(screen.getByText("Count: 1")).toBeInTheDocument();  
});
```

### TDD for React Server Components (If Applicable)
React Server Components (RSC) introduce a different testing paradigm since they execute on the server rather than the client. To test RSC:
  * Use **integration tests** rather than unit tests, as RSC does not rely on React state or hooks.
  * Mock **server-side data fetching** when testing the behavior.
  * Utilize **end-to-end (E2E) tests** to validate UI updates.


Example of testing an RSC component using Jest:

```
import { render } from "@testing-library/react";  
import ServerComponent from "./ServerComponent";  
test("renders server data", async () => {  
  const { findByText } = render(<ServerComponent />);  
  expect(await findByText("Server Data: Success")).toBeInTheDocument();  
});
```

### Handling Asynchronous Operations and API Calls in Tests
Modern applications rely on API calls, making testing asynchronous behavior crucial.
## Get Nitin Mangrule’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
**Mocking API Calls Using MSW (Mock Service Worker)**
MSW intercepts network requests, allowing tests to simulate API responses.

```
import { rest } from "msw";  
import { setupServer } from "msw/node";  
const server = setupServer(  
  rest.get("/api/user", (req, res, ctx) => {  
    return res(ctx.json({ name: "John Doe" }));  
  })  
);  
beforeAll(() => server.listen());  
afterEach(() => server.resetHandlers());  
afterAll(() => server.close());
```

Inside the test:

```
import { render, screen } from "@testing-library/react";  
import UserComponent from "./UserComponent";  
test("fetches and displays user data", async () => {  
  render(<UserComponent />);  
  expect(await screen.findByText("User: John Doe")).toBeInTheDocument();  
});
```

This ensures API-dependent components remain reliable even when backend services are unavailable.
## Test-Driven Development for Performance Optimization
Performance optimization in React involves improving rendering efficiency, reducing re-renders, and optimizing data fetching. TDD can be extended to performance by writing performance tests first, identifying bottlenecks, and optimizing accordingly.
### Writing Performance Tests Before Optimization
Performance testing in React focuses on:
  * Measuring **render times** of components.
  * Identifying **unnecessary re-renders**.
  * Detecting **slow API responses**.


Example of testing a slow-rendering component:

```
import { render } from "@testing-library/react";  
import PerformanceComponent from "./PerformanceComponent";  
test("renders within acceptable time", () => {  
  const start = performance.now();  
  render(<PerformanceComponent />);  
  const end = performance.now();  
  expect(end - start).toBeLessThan(100); // Ensure render time is <100ms  
});
```

If the test fails, optimizations such as **React.memo** , **useCallback** , and **lazy loading** can be applied.
### Profiling Components with React Profiler
React Profiler helps measure component rendering performance. To use it in tests:

```
import { Profiler } from "react";  
import { render } from "@testing-library/react";  
const callback = (id, phase, actualTime) => {  
  console.log(`Component ${id} rendered in ${actualTime}ms during ${phase}`);  
};  
test("profiles component render time", () => {  
  render(  
    <Profiler id="TestComponent" onRender={callback}>  
      <PerformanceComponent />  
    </Profiler>  
  );  
});
```

By analyzing the console logs, developers can identify inefficient renders and apply optimizations.
### Ensuring Tests Capture Performance Regressions
Performance regressions occur when optimizations degrade over time. To prevent them:
  * Use **benchmark tests** that fail if rendering exceeds a predefined time limit.
  * Ensure **memoized components (React.memo)** are not re-rendering unnecessarily.
  * Optimize **useEffect dependencies** to prevent excessive API calls.


Example of testing excessive renders:

```
import { render } from "@testing-library/react";  
import PerformanceComponent from "./PerformanceComponent";  
test("does not re-render unnecessarily", () => {  
  const { rerender } = render(<PerformanceComponent count={0} />);  
  rerender(<PerformanceComponent count={0} />);  
  expect(console.log).not.toHaveBeenCalledWith("Component re-rendered");  
});
```

Using `console.log` to track renders ensures optimizations are effective.
## Integrating TDD with CI/CD
Integrating TDD with Continuous Integration and Continuous Deployment (CI/CD) ensures that tests run automatically whenever code is pushed or merged. This prevents regressions and enforces code quality in a collaborative development environment.
### Automating Test Execution in CI Pipelines (GitHub Actions, GitLab CI/CD)
Most CI/CD platforms support automated test execution. Here’s how you can integrate Jest and Cypress tests in a GitHub Actions pipeline.
**Example: GitHub Actions Workflow for Running Jest and Cypress Tests**
Create a `.github/workflows/test.yml` file:

```
name: Run Tests  
on:  
  push:  
    branches:  
      - main  
      - develop  
  pull_request:  
jobs:  
  test:  
    runs-on: ubuntu-latest  
    steps:  
      - name: Checkout repository  
        uses: actions/checkout@v3  
      - name: Setup Node.js  
        uses: actions/setup-node@v3  
        with:  
          node-version: 18  
      - name: Install dependencies  
        run: npm install  
      - name: Run Jest tests  
        run: npm test  
      - name: Run Cypress tests  
        uses: cypress-io/github-action@v4  
        with:  
          build: npm run build  
          start: npm start  
          wait-on: http://localhost:3000
```

This pipeline ensures that every commit triggers unit and E2E tests, preventing untested code from being merged.
### Parallelizing Tests for Faster Execution
In large-scale applications, test suites can be slow. Parallelizing them speeds up execution.
  * **Jest** supports parallel test execution out of the box. Run tests in parallel using:


```
jest --maxWorkers=4
```

  * This distributes tests across four CPU cores.
  * **Cypress** can split tests across multiple machines:


```
cypress run --record --parallel
```

  * This is useful when running large E2E test suites.


### Code Coverage and Enforcing Test Quality Gates
Maintaining a minimum test coverage ensures code quality. Configure Jest to enforce a minimum coverage threshold in `package.json`:

```
"jest": {  
  "collectCoverage": true,  
  "coverageThreshold": {  
    "global": {  
      "branches": 80,  
      "functions": 80,  
      "lines": 80,  
      "statements": 80  
    }  
  }  
}
```

In a CI pipeline, fail builds if coverage is too low:

```
jest --coverage && npm run check-coverage
```

For Cypress, generate coverage using `cypress/code-coverage` plugin.
## Common Pitfalls and How to Overcome Them
Even though TDD improves code quality, developers often face challenges like slow development speed, over-testing, and test fragility.
### When TDD Slows Down Development and How to Mitigate It
TDD can initially feel slow because it requires writing tests before code. However, productivity improves over time as debugging and refactoring efforts decrease.
**How to mitigate:**
  * Focus on **high-value tests** (critical business logic, API interactions).
  * Use **Test Spikes** — write exploratory code first, then apply TDD when necessary.
  * Leverage **auto-mocking** and **fixtures** to reduce setup time.


### Avoiding Over-Testing and Fragile Tests
Over-testing occurs when too many unnecessary tests are written, leading to maintainability issues. Fragile tests break frequently due to minor UI or implementation changes.
**How to avoid:**
  * **Test behavior, not implementation.** Instead of checking how a function works internally, test its input and output.
  * **Minimize snapshot tests.** Avoid large snapshots that fail due to minor UI changes.
  * **Use integration tests wisely.** They should validate end-to-end functionality rather than replace unit tests.


Example of a **fragile test** (bad practice):

```
test("renders a button with class name btn-primary", () => {  
  render(<Button label="Click me" />);  
  expect(screen.getByRole("button")).toHaveClass("btn-primary");  
});
```

Better approach (testing behavior, not implementation details):

```
test("button triggers action on click", () => {  
  const onClick = jest.fn();  
  render(<Button label="Click me" onClick={onClick} />);  
  fireEvent.click(screen.getByRole("button"));  
  expect(onClick).toHaveBeenCalled();  
});
```

### Best Practices for Maintaining a Robust Test Suite
  * **Keep tests independent.** Avoid sharing state between tests.
  * **Run tests in isolation.** Each test should work regardless of execution order.
  * **Refactor tests as the code evolves.** Clean up obsolete tests when refactoring components.
  * **Use meaningful test names.** Instead of `it("works")`, write `it("displays an error message when form submission fails")`.


## TDD for Component Composition and Reusability
When developing reusable components, TDD helps ensure they are flexible and adaptable across different parts of an application.
### Writing Tests to Ensure Reusability of Components
A reusable `Button` component should work with different styles and behaviors.

```
import { render, screen } from "@testing-library/react";  
import Button from "./Button";  
test("renders with default props", () => {  
  render(<Button label="Submit" />);  
  expect(screen.getByText("Submit")).toBeInTheDocument();  
});  
test("applies custom class", () => {  
  render(<Button label="Click" className="custom-class" />);  
  expect(screen.getByText("Click")).toHaveClass("custom-class");  
});
```

By writing tests before implementing features, we ensure components remain flexible.
### Testing Higher-Order Components (HOCs) and Render Props
**Testing a Higher-Order Component (HOC)**
A simple HOC that provides authentication state:

```
const withAuth = (Component) => (props) => {  
  const isAuthenticated = true;  
  return <Component {...props} isAuthenticated={isAuthenticated} />;  
};
```

Test that it correctly passes authentication status:

```
test("HOC passes authentication status", () => {  
  const MockComponent = ({ isAuthenticated }) => (  
    <p>{isAuthenticated ? "Authenticated" : "Not Authenticated"}</p>  
  );  
    
  const WrappedComponent = withAuth(MockComponent);  
  render(<WrappedComponent />);  
    
  expect(screen.getByText("Authenticated")).toBeInTheDocument();  
});
```

### Ensuring Prop Validation and TypeScript Integration
TypeScript enhances test reliability by enforcing type safety.
For a component using TypeScript:

```
type ButtonProps = {  
  label: string;  
  onClick?: () => void;  
};  
  
const Button: React.FC<ButtonProps> = ({ label, onClick }) => (  
  <button onClick={onClick}>{label}</button>  
);
```

Test invalid prop types using TypeScript’s `@ts-expect-error`:

```
test("throws error for missing required prop", () => {  
  // @ts-expect-error - Intentionally passing incorrect type  
  expect(() => render(<Button />)).toThrow();  
});
```

This ensures that components enforce proper prop types at runtime.
## TDD for Microfrontends and Modular Architectures
Microfrontends allow different teams to develop and deploy independent frontend modules, but ensuring reliability across these modules requires a solid testing strategy. TDD helps enforce clear contracts, prevent regressions, and maintain isolation while enabling seamless integration.
### How TDD Applies in a Microfrontend Architecture
In a microfrontend setup, multiple frontend modules operate independently but must work together seamlessly. TDD helps:
  * Ensure that each module behaves as expected before integration.
  * Prevent regressions when making updates to individual microfrontends.
  * Validate shared dependencies, such as APIs and UI components.


A typical TDD approach for microfrontends involves:
  1. **Unit Testing** — Writing tests for isolated components within each microfrontend.
  2. **Integration Testing** — Validating how microfrontends interact with shared services.
  3. **Contract Testing** — Ensuring consistency in APIs and shared data models.


### Writing Tests for Isolated Frontend Modules
Each microfrontend should be tested independently to ensure that it functions correctly in isolation.
For example, if a **User Dashboard** microfrontend fetches and displays user data, we can write a failing test first:

```
test("renders user data correctly", async () => {  
  render(<UserDashboard />);  
    
  expect(screen.getByText(/loading/i)).toBeInTheDocument();  
    
  const userData = await screen.findByText("John Doe");  
  expect(userData).toBeInTheDocument();  
});
```

Then implement the component and ensure it passes the test:

```
const UserDashboard = () => {  
  const [user, setUser] = useState(null);  
  useEffect(() => {  
      fetch("/api/user")  
        .then((res) => res.json())  
        .then((data) => setUser(data));  
    }, []);  
    if (!user) return <p>Loading...</p>;  
    return <h1>{user.name}</h1>;  
};
```

Finally, refactor and verify that tests remain green.
### Contract Testing Between Microfrontends
Microfrontends communicate via APIs or shared data structures. Contract testing ensures that changes in one microfrontend don’t break others.
**Example:** Using Pact.js to validate API contracts between a `User Profile` and `Notification` microfrontend.

```
import { Pact } from "@pact-foundation/pact";  
const provider = new Pact({  
  consumer: "UserProfileFrontend",  
  provider: "NotificationService",  
});  
describe("Contract Test for Notifications API", () => {  
  beforeAll(() => provider.setup());  
  afterAll(() => provider.finalize());  
  test("should receive expected notification data", async () => {  
    await provider.addInteraction({  
      state: "User has notifications",  
      uponReceiving: "a request for user notifications",  
      withRequest: { method: "GET", path: "/notifications" },  
      willRespondWith: { status: 200, body: [{ id: 1, message: "New alert" }] },  
    });  
    const response = await fetch("/notifications").then((res) => res.json());  
    expect(response).toEqual([{ id: 1, message: "New alert" }]);  
  });  
});
```

This test ensures that the Notifications API remains consistent even if it evolves over time.
## TDD for Server-Side Rendering (SSR) and Static Site Generation (SSG) in Next.js
Next.js applications can render content on the server (SSR) or generate static pages (SSG). Testing these components ensures that data-fetching functions and hydration work correctly.
### Testing SSR Components Effectively
SSR components render on the server before being sent to the client. They often depend on server-side data, so tests should validate both rendering and API interactions.
**Example: Testing an SSR component that fetches user data**
Failing test:

```
import { render, screen } from "@testing-library/react";  
import UserProfile from "../pages/profile";  
test("renders user profile data", async () => {  
  render(<UserProfile user={{ name: "John Doe" }} />);  
    
  expect(await screen.findByText("John Doe")).toBeInTheDocument();  
});
```

Implementation:

```
const UserProfile = ({ user }) => {  
  return <h1>{user.name}</h1>;  
};  
export default UserProfile;
```

### Writing Tests for `getServerSideProps` and `getStaticProps`
Next.js provides two key functions for fetching data:
  * `getServerSideProps` – Fetches data at request time.
  * `getStaticProps` – Pre-fetches data at build time.


**Testing**`**getServerSideProps**`
Failing test:

```
import { getServerSideProps } from "../pages/profile";  
test("fetches user data on server-side", async () => {  
  const context = { params: { id: "123" } };  
  const response = await getServerSideProps(context);  
  expect(response).toEqual({  
    props: { user: { name: "John Doe" } },  
  });  
});
```

Implementation:

```
export async function getServerSideProps() {  
  const res = await fetch("https://api.example.com/user");  
  const user = await res.json();  
  return { props: { user } };  
}
```

**Testing**`**getStaticProps**`
Failing test:

```
import { getStaticProps } from "../pages/blog";  
test("fetches blog posts at build time", async () => {  
  const response = await getStaticProps();  
  expect(response).toEqual({  
    props: { posts: [{ id: 1, title: "Next.js TDD" }] },  
  });  
});
```

Implementation:

```
export async function getStaticProps() {  
  const res = await fetch("https://api.example.com/posts");  
  const posts = await res.json();  
  return { props: { posts } };  
}
```

### Ensuring Hydration Issues Are Caught Early
Hydration mismatches happen when the server-rendered HTML doesn’t match the client-rendered output. Next.js warns about these mismatches, but tests can catch them early.
**Example: Avoiding Hydration Mismatches in a Date Component**
**Incorrect Approach (Causes Hydration Mismatch)**

```
const TimeComponent = () => {  
  return <p>{new Date().toLocaleTimeString()}</p>;  
};
```

Each render generates a new timestamp, leading to inconsistencies.
**Correct Approach (Fixes Hydration Issue)**

```
const TimeComponent = () => {  
  const [time, setTime] = useState(null);  
  useEffect(() => {  
      setTime(new Date().toLocaleTimeString());  
    }, []);  
    return <p>{time || "Loading..."}</p>;  
  };
```

**Testing Hydration Behavior**

```
test("avoids hydration mismatch in time display", () => {  
  render(<TimeComponent />);  
  expect(screen.getByText(/Loading/i)).toBeInTheDocument();  
});
```

## Property-Based Testing and Fuzz Testing in React
Property-based testing and fuzz testing go beyond traditional unit tests by dynamically generating test cases based on predefined properties, ensuring that components can handle a wide range of inputs. This is particularly useful for validating forms, user-generated content, and logic-heavy components.
### When and Why to Use Property-Based Testing
Unlike example-based testing (where you test specific values), property-based testing:
  * Generates **random test cases** within defined constraints.
  * Helps uncover **edge cases** that developers might not anticipate.
  * Reduces the need for writing multiple test scenarios manually.


For example, instead of testing a form with fixed names like `"John Doe"`, property-based tests might generate random strings of various lengths, special characters, or even empty values to ensure robustness.
Use property-based testing when:
  * **Validating form input handling** (e.g., names, emails, passwords).
  * **Testing sorting, filtering, or transformations** where multiple inputs should behave predictably.
  * **Ensuring component resilience** against unexpected or extreme inputs.


### Introducing Tools Like `fast-check` for Generating Test Cases
`fast-check[](https://github.com/dubzzz/fast-check)` is a popular property-based testing library for JavaScript. It helps generate diverse test cases automatically.
**Example: Testing a function that capitalizes names**
Failing test:

```
import * as fc from "fast-check";  
import { capitalizeName } from "../utils";  
test("capitalizeName should handle various inputs", () => {  
  fc.assert(  
    fc.property(fc.string(), (name) => {  
      const result = capitalizeName(name);  
      expect(result[0]).toEqual(result[0]?.toUpperCase());  
    })  
  );  
});
```

Implementation:

```
export function capitalizeName(name) {  
  if (!name) return "";  
  return name.charAt(0).toUpperCase() + name.slice(1);  
}
```

This test will run with randomly generated strings, uncovering issues with empty values, special characters, or long inputs.
### Ensuring Components Handle a Wide Range of Inputs
Property-based testing helps verify UI behavior under unpredictable user inputs.
**Example: Testing a**`**<TextInput>**`**component’s behavior**

```
import * as fc from "fast-check";  
import { render, screen } from "@testing-library/react";  
import TextInput from "../components/TextInput";  
test("TextInput should accept diverse input values", () => {  
  fc.assert(  
    fc.property(fc.string(), async (randomInput) => {  
      render(<TextInput />);  
      const input = screen.getByRole("textbox");  
      await userEvent.type(input, randomInput);  
      expect(input).toHaveValue(randomInput);  
    })  
  );  
});
```

This ensures that the `<TextInput>` component can handle text of any length, special characters, or even empty values without breaking.
## Real-World Case Study: Implementing TDD in a React Project
Let’s walk through how a real-world React project applied TDD to implement a new feature, step by step.
### Step-by-Step Walkthrough: Building a Search Component Using TDD
**1️⃣ Feature Breakdown and Writing the First Failing Test**
We need a `<SearchBox>` component that:
  * Renders an input field.
  * Filters a list of items as the user types.


The first failing test:

```
import { render, screen } from "@testing-library/react";  
import SearchBox from "../components/SearchBox";  
test("renders search input", () => {  
  render(<SearchBox />);  
  expect(screen.getByPlaceholderText("Search...")).toBeInTheDocument();  
});
```

**2️⃣ Implementing the Component to Pass the Test**

```
const SearchBox = () => {  
  return <input type="text" placeholder="Search..." />;  
};  
export default SearchBox;
```

Now the test passes ✅.
**3️⃣ Adding Filtering Logic**
New failing test:

```
import userEvent from "@testing-library/user-event";  
test("filters items based on input", async () => {  
  const items = ["Apple", "Banana", "Orange"];  
  render(<SearchBox items={items} />);  
  const input = screen.getByPlaceholderText("Search...");  
  await userEvent.type(input, "Ban");  
  expect(screen.getByText("Banana")).toBeInTheDocument();  
  expect(screen.queryByText("Apple")).not.toBeInTheDocument();  
});
```

Updating implementation:

```
const SearchBox = ({ items }) => {  
  const [query, setQuery] = useState("");  
  const filteredItems = items.filter((item) =>  
      item.toLowerCase().includes(query.toLowerCase())  
    );  
    return (  
      <div>  
        <input  
          type="text"  
          placeholder="Search..."  
          onChange={(e) => setQuery(e.target.value)}  
        />  
        <ul>  
          {filteredItems.map((item) => (  
            <li key={item}>{item}</li>  
          ))}  
        </ul>  
      </div>  
    );  
};
```

All tests pass ✅.
**4️⃣ Refactoring While Keeping Tests Green**
Refactor into smaller components while ensuring tests remain green.

```
const SearchInput = ({ onSearch }) => (  
  <input type="text" placeholder="Search..." onChange={(e) => onSearch(e.target.value)} />  
);  
const SearchList = ({ items }) => (  
  <ul>{items.map((item) => <li key={item}>{item}</li>)}</ul>  
);  
const SearchBox = ({ items }) => {  
  const [query, setQuery] = useState("");  
  const filteredItems = items.filter((item) => item.toLowerCase().includes(query.toLowerCase()));  
  return (  
    <div>  
      <SearchInput onSearch={setQuery} />  
      <SearchList items={filteredItems} />  
    </div>  
  );  
};
```

All tests still pass ✅.
## Conclusion
### Final Thoughts on Adopting TDD in React Projects
  * TDD helps create scalable, maintainable, and reliable React applications.
  * A test-first mindset improves developer confidence and reduces regressions.
  * Proper tooling and best practices make TDD practical even for large teams.


### Encouraging a Test-Driven Mindset in Engineering Teams
To successfully integrate TDD:
  * Educate the team on the **benefits and best practices**.
  * Start **small** , applying TDD to new components or isolated features.
  * Use **automation and CI/CD** to enforce testing discipline.
  * Treat failing tests as opportunities to **improve design and maintainability**.


### Additional Resources for Mastering TDD in React
  * **Books** : “Test-Driven Development by Example” — Kent Beck
  * **Courses** : Frontend Masters — “Testing React Apps”
  * **Tools** : Jest, React Testing Library, Cypress, fast-check


[Testing](https://medium.com/tag/testing?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Tdd](https://medium.com/tag/tdd?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Micro Frontends](https://medium.com/tag/micro-frontends?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Jest](https://medium.com/tag/jest?source=post_page-----ed7e0cdea9d9---------------------------------------)
[React](https://medium.com/tag/react?source=post_page-----ed7e0cdea9d9---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fed7e0cdea9d9&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&user=Nitin+Mangrule&userId=76d05ddc4a2b&source=---footer_actions--ed7e0cdea9d9---------------------clap_footer------------------)
21
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fed7e0cdea9d9&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&user=Nitin+Mangrule&userId=76d05ddc4a2b&source=---footer_actions--ed7e0cdea9d9---------------------clap_footer------------------)
21
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed7e0cdea9d9&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ndmangrule%2Fcomprehensive-guide-to-test-driven-development-tdd-with-react-ed7e0cdea9d9&source=---footer_actions--ed7e0cdea9d9---------------------bookmark_footer------------------)
[![Nitin Mangrule](https://miro.medium.com/v2/resize:fill:48:48/1*cfacQvlE-Muk_2hrqWwKBw@2x.jpeg)](https://medium.com/@ndmangrule?source=post_page---post_author_info--ed7e0cdea9d9---------------------------------------)
[![Nitin Mangrule](https://miro.medium.com/v2/resize:fill:64:64/1*cfacQvlE-Muk_2hrqWwKBw@2x.jpeg)](https://medium.com/@ndmangrule?source=post_page---post_author_info--ed7e0cdea9d9---------------------------------------)
Follow
## [Written by Nitin Mangrule](https://medium.com/@ndmangrule?source=post_page---post_author_info--ed7e0cdea9d9---------------------------------------)
[42 followers](https://medium.com/@ndmangrule/followers?source=post_page---post_author_info--ed7e0cdea9d9---------------------------------------)
·[11 following](https://medium.com/@ndmangrule/following?source=post_page---post_author_info--ed7e0cdea9d9---------------------------------------)
Frontend Lead at BlackRock. Crafting seamless user experiences. Passionate about frontend innovation. Follow for insights and tips.
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----ed7e0cdea9d9---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----ed7e0cdea9d9---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ed7e0cdea9d9---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ed7e0cdea9d9---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----ed7e0cdea9d9---------------------------------------)
To make Medium work, we log user data. By using Medium, you agree to our [Privacy Policy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9), including cookie policy.


## Source: https://gitnation.com/react-testing-library

[GitNation](https://gitnation.com/)
  * [FAQ](https://gitnation.com/faq)
  * Support/Feedback
  * [Nation`s stats](https://gitnation.com/javascript-developers-statistics/index)


[Log in](https://gitnation.com/login?return-to=%2Freact-testing-library)
0
  * [Discover](https://gitnation.com/)
  * [Events](https://gitnation.com/events)
  * [Talks](https://gitnation.com/talks)
  * [Workshops](https://gitnation.com/workshops)
  * [People](https://gitnation.com/people)
  * [Articles](https://gitnation.com/articles)
  * [Multipass](https://gitnation.com/multipass)
  * [All tags](https://gitnation.com/tags)
  * [RSS feeds](https://gitnation.com/rss-feeds)


  * [Login](https://gitnation.com/login?return-to=/react-testing-library)
  * [About us](https://gitnation.org/foundation/)
  * [FAQ](https://gitnation.com/faq)
  * Support/Feedback


Follow us
[](https://www.linkedin.com/company/gitnation/)[](https://twitter.com/GitNationOrg/)[](https://www.instagram.com/gitnation/)[](https://www.tiktok.com/@gitnationorg/)[](https://bsky.app/profile/gitnation.bsky.social)
# React Testing Library: A Complete Guide to Modern Testing Frameworks
## ![](https://res.cloudinary.com/stichting-frontend-amsterdam/image/upload/v1738862321/Screenshot_2025-02-06_at_17.18.29_r5pzih.png)
## Introduction
React testing has evolved significantly in recent years, with React Testing Library emerging as a leading solution for creating reliable, maintainable test suites. As organizations increasingly prioritize robust testing strategies, understanding the landscape of React testing libraries and frameworks has become crucial for modern web development.
GitNation brings together leading experts in React testing, including Josh Justice, a veteran developer who specializes in React testing optimization, Bonnie Schulkin, who brings 18 years of software industry experience with a focus on test-driven development, and Murat K Ozcan, a Staff Engineer & Test Architect with extensive experience in testing frameworks. Their collective insights provide a comprehensive view of current best practices and emerging trends in React testing.
This guide explores the complete ecosystem of React testing libraries, focusing on practical implementation strategies and real-world solutions. Whether you're transitioning from Enzyme, evaluating Cypress Component Testing, or looking to optimize your existing React Testing Library implementation, you'll find actionable insights drawn from our experts' deep experience and successful implementations.
  

## Core Testing Libraries and Frameworks  
  

### React Testing Library: The Modern Standard
React Testing Library has revolutionized how developers approach component testing, emphasizing user behavior over implementation details. As Josh Justice explains in his comprehensive workshop on React Testing Library, this approach leads to more maintainable and reliable tests:
"React Testing Library answers many crucial testing questions, allowing developers to focus on what matters: testing behavior that users care about rather than implementation details that may change."
The library's focus on accessibility and user interaction patterns has made it the preferred choice for teams building production-grade React applications.
Reference: [Designing Effective Tests with React Testing Library](https://gitnation.com/contents/designing-effective-tests-with-react-testing-library) - talk by Josh Justice from React Day Berlin 2022. 
  

### Transitioning from Enzyme
While many teams still maintain Enzyme-based test suites, there's a clear industry trend toward React Testing Library. Bonnie Schulkin's journey from Enzyme to React Testing Library offers valuable insights into this transition:
"Testing Library's opinionated framework enforces best testing practices, encourages accessibility, and leads to simpler, more readable tests. The shift has fundamentally improved how we approach component testing."
Her experience highlights the key advantages of modern testing approaches, including improved test stability and reduced maintenance overhead.
Reference: [Testing React: A Convert’s Journey from Enzyme to Testing Library](https://gitnation.com/contents/testing-react-a-converts-journey-from-enzyme-to-testing-library) - talk by Bonnie Schulkin from TestJS summit January 2021   
  

### Cypress Component Testing: A Powerful Alternative
Cypress Component Testing offers unique advantages for teams seeking real browser-based testing solutions. Murat K Ozcan's detailed comparison between Cypress and React Testing Library reveals important considerations:
"Cypress Component Testing provides superior developer experience and observability, offering unique advantages for complex components and stable testing in CI environments."
His analysis helps teams make informed decisions about their testing infrastructure, particularly for projects requiring sophisticated interaction testing.
Reference: [Cypress vs Jest: Testing Insights](https://gitnation.com/contents/cypress-component-testing-vs-react-testing-library) - talk by Murat K Ozcan from TestJS Summit 2023 
  

## Best Practices and Implementation Strategies
  

### Test-Driven Development with React
Josh Justice emphasizes the importance of test-driven development in React applications:
"TDD helps you see how to test each bit of logic, whether to mock dependencies and improves the overall design of your components."
Key TDD principles for React applications include:
  * Writing tests before implementation
  * Focusing on component behavior
  * Maintaining test isolation
  * Using realistic user interactions


Reference: [Designing Effective Tests with React Testing Library](https://gitnation.com/contents/designing-effective-tests-with-react-testing-library) - talk by Josh Justice from React Day Berlin 2022. 
  

### Component Testing Strategies
Drawing from multiple expert perspectives, successful component testing requires:
  1. Behavior-Focused Testing
     * Test user interactions rather than implementation
     * Focus on accessibility and screen reader compatibility
     * Verify expected outcomes from a user's perspective
  2. Effective Test Organization
     * Group related tests logically
     * Maintain clear test descriptions
     * Follow consistent naming conventions
  3. Mocking and Integration
     * Use appropriate mocking strategies
     * Test external integrations effectively
     * Handle asynchronous operations properly


  

### Handling Asynchronous Operations
Testing asynchronous operations requires special consideration. Murat K Ozcan provides valuable insights into handling async testing challenges:
"The key to stable async tests is understanding the different approaches available in each testing framework and choosing the right tool for your specific needs."
Reference: [Cypress vs Jest: Testing Insights](https://gitnation.com/contents/cypress-component-testing-vs-react-testing-library) - talk by Murat K Ozcan from TestJS Summit 2023 
  

## Advanced Testing Considerations
  

### Accessibility Testing
React Testing Library's emphasis on accessibility has transformed how teams approach component testing. Bonnie Schulkin notes:
"The focus on accessibility queries has not only improved our tests but has made our components more accessible by default."
Key accessibility testing principles include:
  * Using semantic HTML elements
  * Testing with screen reader considerations
  * Verifying ARIA attributes and roles


Reference: Testing React:[ A Convert’s Journey from Enzyme to Testing Library](https://gitnation.com/contents/testing-react-a-converts-journey-from-enzyme-to-testing-library) - talk by Bonnie Schulkin at TestJS Summit 2021   
  

### Performance Testing and Optimization
Performance testing considerations include:
  * Component render optimization
  * State management efficiency
  * Network request handling
  * Animation performance


## Conclusion
The landscape of React testing continues to evolve, with React Testing Library, Cypress Component Testing, and other frameworks providing robust solutions for different testing needs. Through the insights shared by our expert speakers at GitNation conferences, we've explored comprehensive strategies for implementing effective testing practices.
For deeper insights into specific testing approaches and advanced implementations, we encourage you to explore the full talks referenced throughout this guide. Each presentation offers detailed examples, practical demonstrations, and expert guidance to help you build more reliable and maintainable React applications.
Continue your React testing journey by watching our expert talks:
  * [Josh Justice's comprehensive guide to React Testing Library](https://gitnation.com/contents/introduction-to-react-native-testing-library) - workshop at React Advanced 2022
  * [Bonnie Schulkin's insights on transitioning from Enzyme](https://gitnation.com/contents/testing-react-a-converts-journey-from-enzyme-to-testing-library) - talk at TestJS Summit 2021
  * [Murat K Ozcan's detailed comparison of testing frameworks](https://gitnation.com/contents/cypress-component-testing-vs-react-testing-library) - talk at TestJS Summit 2023


These resources provide the detailed knowledge and practical examples you need to implement effective testing strategies in your React applications.
[react](https://gitnation.com/tags/react)[vue](https://gitnation.com/tags/vue)[web development](https://gitnation.com/tags/web-development)[typescript](https://gitnation.com/tags/typescript)[best practices](https://gitnation.com/tags/best-practices)[node.js](https://gitnation.com/tags/nodejs)[performance](https://gitnation.com/tags/performance)[testing](https://gitnation.com/tags/testing)[devtools](https://gitnation.com/tags/devtools)[react native](https://gitnation.com/tags/react-native)[user interfaces](https://gitnation.com/tags/user-interfaces)[unit testing](https://gitnation.com/tags/unit-testing)[api development](https://gitnation.com/tags/api-development)[automation](https://gitnation.com/tags/automation)[accessibility](https://gitnation.com/tags/accessibility)[vue 3](https://gitnation.com/tags/vue-3)[ci cd](https://gitnation.com/tags/ci-cd)[cypress](https://gitnation.com/tags/cypress)[js runtimes](https://gitnation.com/tags/js-runtimes)[deep dive](https://gitnation.com/tags/deep-dive)[panel discussions](https://gitnation.com/tags/panel-discussions)[test driven development react](https://gitnation.com/tags/test-driven-development-react)[cypress react native](https://gitnation.com/tags/cypress-react-native)[react testing](https://gitnation.com/tags/react-testing)[react native detox](https://gitnation.com/tags/react-native-detox)[react testing library](https://gitnation.com/tags/react-testing-library)[react native testing](https://gitnation.com/tags/react-native-testing)[react native test automation](https://gitnation.com/tags/react-native-test-automation)[cypress react](https://gitnation.com/tags/cypress-react)[msw react](https://gitnation.com/tags/msw-react)[enzyme vs react testing library](https://gitnation.com/tags/enzyme-vs-react-testing-library)[react enzyme](https://gitnation.com/tags/react-enzyme)[react native testing library](https://gitnation.com/tags/react-native-testing-library)[react reassure](https://gitnation.com/tags/react-reassure)[react testing library typescript](https://gitnation.com/tags/react-testing-library-typescript)
18 Dec, 2024
Share
[](http://twitter.com/share?text=Found%20a%20nice%20one%20at%20GitNation&url=https://gitnation.com/contents/react-testing-library)[](https://www.facebook.com/sharer/sharer.php?u=https://gitnation.com/contents/react-testing-library&t=Found%20a%20nice%20one%20at%20GitNation)[](https://linkedin.com/shareArticle?url=https://gitnation.com/contents/react-testing-library)
## Table of contents
Article
[1. Introduction](https://gitnation.com/react-testing-library#introduction)[2. Best Practices and Implementation Strategies](https://gitnation.com/react-testing-library#best-practices-and-implementation-strategies)[3. Advanced Testing Considerations](https://gitnation.com/react-testing-library#advanced-testing-considerations)[4. Conclusion](https://gitnation.com/react-testing-library#conclusion)
### [FAQ](https://gitnation.com/react-testing-library#faq-link)
## FAQ
What is React Testing Library?
React Testing Library is a popular testing utility that encourages testing components from a user's perspective, focusing on accessibility and user interactions rather than implementation details.
How do I choose the right testing approach for my React application?
Consider your application's complexity, focus on user behavior, use semantic queries, mock dependencies strategically, and choose tools that align with your testing goals.
What are the key principles of modern React testing?
Key principles include testing user interactions, using accessible queries, focusing on component behavior, handling asynchronous rendering, and considering performance implications.
Are there tools beyond React Testing Library for testing?
Yes, tools like Vitest, Reassure, and custom solutions offer additional testing capabilities, each with unique strengths for different testing scenarios.
How can I improve my React testing skills?
Watch conference talks, practice writing user-centric tests, explore different testing libraries, and continuously learn about new testing strategies and tools.
## Learn more about the topic from these talks
[Fire-Side Chat with Kent C. Dodds](https://gitnation.com/contents/fire-side-chat-with-kent-c-dodds)
![React Summit Remote Edition 2021](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376965/gu6c5rsayr3qtz6zvshf.jpg?auto=format,compress&fit=scale&w=60)React Summit Remote Edition 2021
min
Fire-Side Chat with Kent C. Dodds
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Kent C. Dodds](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1663241015/dev/Kent_C._Dodds_cekgpk.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Kent C. Dodds Creator of EpicWeb.dev, EpicReact.Dev, TestingJavaScript.com ](https://gitnation.com/person/kent_c_dodds)
Kent C. Dodds discusses various topics including migrating projects to TypeScript, Next.js and Remix, testing libraries, RTL testing with React Testing Library, integration testing for component libraries, testing design systems, writing tests, communication resources, and the popularity of Hooks in React development.
[panel discussions](https://gitnation.com/tags/panel-discussions)
[Shipping High Quality JS Apps with Confidence](https://gitnation.com/contents/shipping-high-quality-js-apps-with-confidence)
![TestJS Summit - January, 2021](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376949/rlwmbgekjgai9xefiety.png?auto=format,compress&fit=scale&w=60)TestJS Summit - January, 2021
min
Shipping High Quality JS Apps with Confidence
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Tomasz Łakomy](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1623768335/r5vk9zj73hkvjmtnbxl2.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Tomasz Łakomy Stedi ](https://gitnation.com/person/tomasz_lakomy)
Today's Talk highlights the importance of software quality and its impact on businesses. It emphasizes the use of different tools and practices to improve software quality. The Talk covers topics such as testing with TypeScript and React Testing Library, accessibility, Cypress for end-to-end testing, writing better queries, monitoring performance, using feature flags with LaunchDarkly, and the value of Prettier. The key takeaway is that developing high-quality software with fast feedback loops and simplicity is crucial for success.
[testing](https://gitnation.com/tags/testing)[automation](https://gitnation.com/tags/automation)
[Testing React: A Convert’s Journey from Enzyme to Testing Library](https://gitnation.com/contents/testing-react-a-converts-journey-from-enzyme-to-testing-library)
![TestJS Summit - January, 2021](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376949/rlwmbgekjgai9xefiety.png?auto=format,compress&fit=scale&w=60)TestJS Summit - January, 2021
min
Testing React: A Convert’s Journey from Enzyme to Testing Library
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Bonnie Schulkin](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1623768399/kzc1tie95ycrd82aywcw.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Bonnie Schulkin Teacher, Coder & Testing Enthusiast ](https://gitnation.com/person/bonnie_schulkin)
The speaker switched from Enzyme to the REACT Testing Library due to its encouragement of best practices, easier refactoring, and promotion of accessible code. The shift from class-based components to functional components in React is also highlighted. The benefits of the Testing Library include improved readability and user interaction simulation through DOM assertions, as well as its opinionated nature and focus on accessible code.
[react](https://gitnation.com/tags/react)[testing](https://gitnation.com/tags/testing)[enzyme vs react testing library](https://gitnation.com/tags/enzyme-vs-react-testing-library)[react enzyme](https://gitnation.com/tags/react-enzyme)[react testing library](https://gitnation.com/tags/react-testing-library)
[To Mock or Not to Mock - That's the Question](https://gitnation.com/contents/to-mock-or-not-to-mock-thats-the-question)
![React Advanced 2021](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1751972628/React_Advanced_kaftzq.png?auto=format,compress&fit=scale&w=60)React Advanced 2021
min
To Mock or Not to Mock - That's the Question
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Rita Castro](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1700670009/lVIYbYStXG5FnOOG9bqISqQhmgx2O8KF2p7bmwMYD5M%403D.png?auto=format,compress&fit=crop&w=300&h=300)
[ Rita CastroMentorship available Volkswagen Group Digital Solutions [Portugal] ](https://gitnation.com/person/rita_castro)
This Talk discusses the SDC's approach to software development using agile methodologies and extreme programming. It highlights the benefits of pair programming and the use of atomic design in React components. The importance of test-driven development and the React testing library is emphasized, along with the implementation of code, navigation, and form validation using Formik and Yup. The talk also touches on the abstraction layers in software development and the testing of user journeys and accessibility in the BookKeeper app.
[testing](https://gitnation.com/tags/testing)[best practices](https://gitnation.com/tags/best-practices)
[React, TypeScript, and TDD](https://gitnation.com/contents/react-typescript-and-tdd)
![React Advanced 2021](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1751972628/React_Advanced_kaftzq.png?auto=format,compress&fit=scale&w=60)React Advanced 2021
min
React, TypeScript, and TDD
Featured Workshop
[![Paul Everitt](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1635339335/y3kgisevb9twtqayglw4.jpg?auto=format,compress&fit=crop&w=300&h=300) Paul Everitt](https://gitnation.com/person/paul_everitt)
ReactJS is wildly popular and thus wildly supported. TypeScript is increasingly popular, and thus increasingly supported.  
  
The two together? Not as much. Given that they both change quickly, it's hard to find accurate learning materials.  
  
React+TypeScript, with JetBrains IDEs? That three-part combination is the topic of this series. We'll show a little about a lot. Meaning, the key steps to getting productive, in the IDE, for React projects using TypeScript. Along the way we'll show test-driven development and emphasize tips-and-tricks in the IDE. 
[react](https://gitnation.com/tags/react)[best practices](https://gitnation.com/tags/best-practices)[typescript](https://gitnation.com/tags/typescript)[devtools](https://gitnation.com/tags/devtools)[web development](https://gitnation.com/tags/web-development)[test driven development react](https://gitnation.com/tags/test-driven-development-react)
[Test your UI in the REAL Browser](https://gitnation.com/contents/test-your-ui-in-the-real-browser)
![TestJS Summit 2021](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376949/rlwmbgekjgai9xefiety.png?auto=format,compress&fit=scale&w=60)TestJS Summit 2021
min
Test your UI in the REAL Browser
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Gert Hengeveld](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1636463878/xouyr1rzfk8v7xcrslj1.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Gert Hengeveld Chromatic ](https://gitnation.com/person/gert_hengeveld)
Storybook is a powerful tool for building UI components and testing them. It allows for easy reuse and compatibility with other tools. Storybook 6.4 introduces interactive stories and live coding, making it easier to create and debug complex components. It also integrates with popular testing libraries like Jest and Testing Library. Storybook aims to bridge the gap between end-to-end testing and unit testing, providing automated testing options for UI components.
[testing](https://gitnation.com/tags/testing)[user interfaces](https://gitnation.com/tags/user-interfaces)
[Introduction to React Native Testing Library](https://gitnation.com/contents/introduction-to-react-native-testing-library)
![React Advanced 2022](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1751972628/React_Advanced_kaftzq.png?auto=format,compress&fit=scale&w=60)React Advanced 2022
min
Introduction to React Native Testing Library
Workshop
[![Josh Justice](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1663333494/dev/Josh_Justice_mtodzc.jpg?auto=format,compress&fit=crop&w=300&h=300) Josh Justice](https://gitnation.com/person/josh_justice)
Are you satisfied with your test suites? If you said no, you’re not alone—most developers aren’t. And testing in React Native is harder than on most platforms. How can you write JavaScript tests when the JS and native code are so intertwined? And what in the world are you supposed to do about that persistent act() warning? Faced with these challenges, some teams are never able to make any progress testing their React Native app, and others end up with tests that don’t seem to help and only take extra time to maintain.  
But it doesn’t have to be this way. React Native Testing Library (RNTL) is a great library for component testing, and with the right mental model you can use it to implement tests that are low-cost and high-value. In this three-hour workshop you’ll learn the tools, techniques, and principles you need to implement tests that will help you ship your React Native app with confidence. You’ll walk away with a clear vision for the goal of your component tests and with techniques that will help you address any obstacle that gets in the way of that goal.you will know:- The different kinds React Native tests, and where component tests fit in- A mental model for thinking about the inputs and outputs of the components you test- Options for selecting text, image, and native code elements to verify and interact with them- The value of mocks and why they shouldn’t be avoided- The challenges with asynchrony in RNTL tests and how to handle them- Options for handling native functions and components in your JavaScript tests  
Prerequisites:- Familiarity with building applications with React Native- Basic experience writing automated tests with Jest or another unit testing framework- You do not need any experience with React Native Testing Library- Machine setup: Node 16.x or 18.x, Yarn, be able to successfully create and run a new Expo app following the instructions on https://docs.expo.dev/get-started/create-a-new-app/
[testing](https://gitnation.com/tags/testing)[react native](https://gitnation.com/tags/react-native)[unit testing](https://gitnation.com/tags/unit-testing)[cypress react native](https://gitnation.com/tags/cypress-react-native)[react native detox](https://gitnation.com/tags/react-native-detox)[react native test automation](https://gitnation.com/tags/react-native-test-automation)[react native testing](https://gitnation.com/tags/react-native-testing)[react native testing library](https://gitnation.com/tags/react-native-testing-library)
[Designing Effective Tests with React Testing Library](https://gitnation.com/contents/designing-effective-tests-with-react-testing-library)
![React Day Berlin 2022](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1657225787/udbtwudbhkfg8fl0ljey.png?auto=format,compress&fit=scale&w=60)React Day Berlin 2022
min
Designing Effective Tests with React Testing Library
Workshop
[![Josh Justice](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1663333494/dev/Josh_Justice_mtodzc.jpg?auto=format,compress&fit=crop&w=300&h=300) Josh Justice](https://gitnation.com/person/josh_justice)
React Testing Library is a great framework for React component tests because there are a lot of questions it answers for you, so you don’t need to worry about those questions. But that doesn’t mean testing is easy. There are still a lot of questions you have to figure out for yourself: How many component tests should you write vs end-to-end tests or lower-level unit tests? How can you test a certain line of code that is tricky to test? And what in the world are you supposed to do about that persistent act() warning?  
In this three-hour workshop we’ll introduce React Testing Library along with a mental model for how to think about designing your component tests. This mental model will help you see how to test each bit of logic, whether or not to mock dependencies, and will help improve the design of your components. You’ll walk away with the tools, techniques, and principles you need to implement low-cost, high-value component tests.  
Prerequisites:- Familiarity with building applications with React- Basic experience writing automated tests with Jest or another unit testing framework- You do not need any experience with React Testing Library- Machine setup: Node LTS, Yarn
[react](https://gitnation.com/tags/react)[react testing library typescript](https://gitnation.com/tags/react-testing-library-typescript)[test driven development react](https://gitnation.com/tags/test-driven-development-react)
[Automated Performance Regression Testing with Reassure](https://gitnation.com/contents/automated-performance-regression-testing-with-reassure)
![React Advanced 2022](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1751972628/React_Advanced_kaftzq.png?auto=format,compress&fit=scale&w=60)React Advanced 2022
min
Automated Performance Regression Testing with Reassure
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Michał Pierzchała](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1661784404/dev/Micha%C5%82_Pierzcha%C5%82a_uphsuv.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Michał Pierzchała Callstack ](https://gitnation.com/person/michal_pierzchala)
Today's Talk introduces Reacher, a performance monitoring tool for React and React Native codebases. It highlights the need for catching performance regressions early in the development process and identifies JavaScript misusage as a common source of performance issues. ReaSure, developed by Covstack, is presented as a promising library that integrates with existing ecosystems and provides reliable render time measurements and helpful insights for code review. Considerations for operating in a JavaScript VM are discussed, including JIT, garbage collection, and module resolution caching. Statistical analysis using the z-score is mentioned as a method for determining the significance of measurement results.
[performance](https://gitnation.com/tags/performance)[testing](https://gitnation.com/tags/testing)[react native](https://gitnation.com/tags/react-native)[ci cd](https://gitnation.com/tags/ci-cd)[react reassure](https://gitnation.com/tags/react-reassure)
[Designing Effective Tests With React Testing Library](https://gitnation.com/contents/designing-effective-tests-with-react-testing-library-1153)
![React Summit 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376923/fszvxiu9y2alolt9eymk.jpg?auto=format,compress&fit=scale&w=60)React Summit 2023
min
Designing Effective Tests With React Testing Library
Featured Workshop
[![Josh Justice](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1663333494/dev/Josh_Justice_mtodzc.jpg?auto=format,compress&fit=crop&w=300&h=300) Josh Justice](https://gitnation.com/person/josh_justice)
React Testing Library is a great framework for React component tests because there are a lot of questions it answers for you, so you don’t need to worry about those questions. But that doesn’t mean testing is easy. There are still a lot of questions you have to figure out for yourself: How many component tests should you write vs end-to-end tests or lower-level unit tests? How can you test a certain line of code that is tricky to test? And what in the world are you supposed to do about that persistent act() warning?  
In this three-hour workshop we’ll introduce React Testing Library along with a mental model for how to think about designing your component tests. This mental model will help you see how to test each bit of logic, whether or not to mock dependencies, and will help improve the design of your components. You’ll walk away with the tools, techniques, and principles you need to implement low-cost, high-value component tests.  
Table of contents- The different kinds of React application tests, and where component tests fit in- A mental model for thinking about the inputs and outputs of the components you test- Options for selecting DOM elements to verify and interact with them- The value of mocks and why they shouldn’t be avoided- The challenges with asynchrony in RTL tests and how to handle them  
Prerequisites- Familiarity with building applications with React- Basic experience writing automated tests with Jest or another unit testing framework- You do not need any experience with React Testing Library- Machine setup: Node LTS, Yarn
[react](https://gitnation.com/tags/react)[testing](https://gitnation.com/tags/testing)[best practices](https://gitnation.com/tags/best-practices)[deep dive](https://gitnation.com/tags/deep-dive)[react testing](https://gitnation.com/tags/react-testing)[react testing library](https://gitnation.com/tags/react-testing-library)[test driven development react](https://gitnation.com/tags/test-driven-development-react)
[Testing Vue 3 Applications with Mock Service Worker](https://gitnation.com/contents/testing-vue-3-applications-with-mock-service-worker)
![Vue.js London 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1621500214/fcizntw4zinyl8pzu058.png?auto=format,compress&fit=scale&w=60)Vue.js London 2023
min
Testing Vue 3 Applications with Mock Service Worker
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Lisi Linhart](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1676922625/dev/Lisi_Linhart_imeiij.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Lisi Linhart Storyblok ](https://gitnation.com/person/lisi_linhart)
This Talk discusses testing V3 applications with Mock Service Worker, which is a library that allows simulating server responses in tests. It covers setting up Mock Service Worker by creating mock API responses and connecting it with the application. The Talk also explains how to write unit tests for asynchronous components using Vue's suspense component. It demonstrates how to test components that interact with APIs and handle error responses. Additionally, it mentions the testing library for components without API calls and emphasizes the importance of testing component interactions and API integration.
[testing](https://gitnation.com/tags/testing)[vue 3](https://gitnation.com/tags/vue-3)[msw react](https://gitnation.com/tags/msw-react)
[Creating My First Open Source Vue 3 Library](https://gitnation.com/contents/creating-my-first-open-source-vue-3-library)
![Vue.js London 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1621500214/fcizntw4zinyl8pzu058.png?auto=format,compress&fit=scale&w=60)Vue.js London 2023
min
Creating My First Open Source Vue 3 Library
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Erik Hanchett](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1761898990/Screenshot_2025-10-31_at_11.22.50_ryyaaw.png?auto=format,compress&fit=crop&w=300&h=300)
[ Erik Hanchett AWS ](https://gitnation.com/person/erik_hanchett)
Let's talk about Vue 3 and creating your first open source library. We'll discuss design choices, a personal example of creating a Vue 3 open source library, community and open source, lessons learned, and key takeaways for creating an open source project. We'll also cover building a Vue 3 library, the Authenticator project and its requirements, code sharing and best practices, using Xstate for state management, Vue 3 best practices, testing strategies, open sourcing and community feedback, documentation driven development, challenges and improvements, and the roadmap for the future.
[vue](https://gitnation.com/tags/vue)[vue 3](https://gitnation.com/tags/vue-3)[api development](https://gitnation.com/tags/api-development)
[A11y Beyond the Theory: Integrating Accessibility Testing Into Your Workflow](https://gitnation.com/contents/a11y-beyond-the-theory-integrating-accessibility-testing-into-your-workflow-1632)
![React Summit US 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1691484715/RSUS_Portal_400x400_gwyiwq.png?auto=format,compress&fit=scale&w=60)React Summit US 2023
min
A11y Beyond the Theory: Integrating Accessibility Testing Into Your Workflow
[Watch video: A11y Beyond the Theory: Integrating Accessibility Testing Into Your Workflow](https://gitnation.com/contents/a11y-beyond-the-theory-integrating-accessibility-testing-into-your-workflow-1632/video)
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Lucky Nkosi](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1688409849/Lucky_Nkosi_a2bips.png?auto=format,compress&fit=crop&w=300&h=300)
[ Lucky Nkosi Lucky is a Software Engineer at BBD ](https://gitnation.com/person/lucky_nkosi)
Ntandala Kengose, a software developer, emphasizes the importance of accessibility in software development and the responsibility it carries. The Web Content Accessibility Guidelines (WCAG) provide technical guidelines for making web content more accessible. Ntandala shares various accessibility testing tools and highlights the need for automation in testing. Tools like Pelly CI and GitHub Actions can be used for automated accessibility testing and CI integration. The X-Accessibility Ginter and Husky are tools that provide insights and ensure accessibility in development.
[accessibility](https://gitnation.com/tags/accessibility)[automation](https://gitnation.com/tags/automation)
[Exploring Node.js Test Runner](https://gitnation.com/contents/exploring-nodejs-test-runner)
![TestJS Summit 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376949/rlwmbgekjgai9xefiety.png?auto=format,compress&fit=scale&w=60)TestJS Summit 2023
min
Exploring Node.js Test Runner
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Marco Ippolito](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1718355712/g54Mqm1QulhWOsBd6vsnI%402FixTi1w8mhKVgrLc8%402FEMh0%403D.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Marco Ippolito Member of Node.js Technical Steering Committee ](https://gitnation.com/person/marco_ippolito)
Today's Talk introduces the new Node.js test runner and its features, including filtering, sub-testing, and reporting. It also discusses executing and writing tests in Node.js, as well as the features of the Node.js testing library. The advantages of the Node.js test runner include the ability to create custom test reporters and use TypeScript. However, there are limitations such as a small ecosystem and limited libraries. Upcoming features include test planning, faster test running, and continuous evolution. The Q&A session covers topics like test runner speed, reporters, sharding, and parallelization.
[node.js](https://gitnation.com/tags/nodejs)
[Component Testing With Vitest](https://gitnation.com/contents/component-testing-with-vitest)
![TestJS Summit 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376949/rlwmbgekjgai9xefiety.png?auto=format,compress&fit=scale&w=60)TestJS Summit 2023
min
Component Testing With Vitest
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Maya Shavin](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1634671847/qfjwe07603nrr9dmqall.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Maya Shavin Published author, international speaker and an open-source library maintainer of frontend and web projects ](https://gitnation.com/person/maya_shavin)
This Talk explores the challenges of choosing and learning testing frameworks, emphasizing the importance of planning, automation, and prioritizing unit testing. The VTEST framework is introduced as a fast and stable option for unit testing JavaScript and TypeScript code, with a focus on logic and mocking external dependencies. The Talk also covers testing React hooks, integration testing with TestingLibraryReact, component testing, and achieving code coverage. Best practices include performing accessibility tests, planning tests before coding, and using data test IDs for stability.
[unit testing](https://gitnation.com/tags/unit-testing)
[Testing Library: Everybody Uses It, But Nobody Understands It](https://gitnation.com/contents/testing-library-everybody-uses-it-but-nobody-understands-it)
![TestJS Summit 2023](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376949/rlwmbgekjgai9xefiety.png?auto=format,compress&fit=scale&w=60)TestJS Summit 2023
min
Testing Library: Everybody Uses It, But Nobody Understands It
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Matan Borenkraout](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1696438646/Matan_b9takp.jpg?auto=format,compress&fit=crop&w=300&h=300)
[ Matan Borenkraout Microsoft ](https://gitnation.com/person/matan_borenkraout)
This Talk is about a developer's first open source contribution to the Testing Library, exploring how it works and its importance in testing. It discusses the challenges of testing in a Node environment and the use of getByRole query to find elements. The Talk also highlights the complexities of implicit roles and the need for specific attributes to filter elements. It emphasizes the importance of verifying visibility and accessibility when querying elements and the process of test clean up.
[testing](https://gitnation.com/tags/testing)[unit testing](https://gitnation.com/tags/unit-testing)
[Mastering Node.js Test Runner](https://gitnation.com/contents/mastering-nodejs-test-runner-2112)
![Node Congress 2024](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376938/eav9rff77rtiyz7qse5v.jpg?auto=format,compress&fit=scale&w=60)Node Congress 2024
min
Mastering Node.js Test Runner
Workshop
[![Marco Ippolito](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1718355712/g54Mqm1QulhWOsBd6vsnI%402FixTi1w8mhKVgrLc8%402FEMh0%403D.jpg?auto=format,compress&fit=crop&w=300&h=300) Marco Ippolito](https://gitnation.com/person/marco_ippolito)
Node.js test runner is modern, fast, and doesn't require additional libraries, but understanding and using it well can be tricky.You will learn how to use Node.js test runner to its full potential.We'll show you how it compares to other tools, how to set it up, and how to run your tests effectively. During the workshop, we'll do exercises to help you get comfortable with filtering, using native assertions, running tests in parallel, using CLI, and more. We'll also talk about working with TypeScript, making custom reports, and code coverage.
[testing](https://gitnation.com/tags/testing)[typescript](https://gitnation.com/tags/typescript)[node.js](https://gitnation.com/tags/nodejs)
[What's New on Node.js Test Runner and Why it's Game-changing](https://gitnation.com/contents/whats-new-on-nodejs-test-runner-and-why-its-game-changing)
![Node Congress 2024](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1619376938/eav9rff77rtiyz7qse5v.jpg?auto=format,compress&fit=scale&w=60)Node Congress 2024
min
What's New on Node.js Test Runner and Why it's Game-changing
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Lucas Santos](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1690393812/Lucas_Santos_bi5tja.png?auto=format,compress&fit=crop&w=300&h=300)
[ Lucas Santos Brazilian programmer, content creator, and professional trainer ](https://gitnation.com/person/lucas_santos)
The Node.js Test Runner is presented as a better alternative to Jest, offering more flexibility and improved performance. It supports TypeScript out of the box and provides comprehensive test suite visualization. The test runner has native support for code coverage and upcoming features include module mocking and improved filtering. Shifting to the test runner is simple and helps the community grow.
[js runtimes](https://gitnation.com/tags/js-runtimes)
[Beyond React Testing Library: Testing React Libraries (and library-like code)](https://gitnation.com/contents/beyond-react-testing-library-testing-react-libraries-and-library-like-code)
![React Advanced 2024](https://gitnation.imgix.net/stichting-frontend-amsterdam/image/upload/v1751972628/React_Advanced_kaftzq.png?auto=format,compress&fit=scale&w=60)React Advanced 2024
min
Beyond React Testing Library: Testing React Libraries (and library-like code)
![](https://gitnation.com/_next/static/media/article-head-bg-not-mask-optimized.42d4b7d2.avif)
![Lenz Weber-Tronic](https://avatars.githubusercontent.com/u/4282439?v=4)
[ Lenz Weber-Tronic Apollo GraphQL ](https://gitnation.com/person/lenz_webertronic)
Today's talk is called Beyond Testing Library, Testing React Libraries and Library-like Code. The speaker, Lenz Liebertronik, discusses the special requirements for testing libraries, including minimizing re-renders, avoiding tearing, and rendering components granularly. They highlight scenarios where React Testing Library falls short and introduce the Testing Library React render stream as a solution. The speaker demonstrates how to test hooks, multiple hooks, and assert re-renders using different techniques. They caution about potential issues with React upgrades, test-only components, ACT batching, and Suspense boundaries. The speaker shares real-world usage of the render stream library and discusses the limitations of correlating renders with DOM commits. They emphasize the importance of testing libraries and gradually optimizing code. They also mention the benefits of using the testing library and conclude with gratitude and a Dutch lesson.
[testing](https://gitnation.com/tags/testing)
Main menu
  * [Discover](https://gitnation.com/)
  * [Events](https://gitnation.com/events)
  * [Talks](https://gitnation.com/talks)
  * [Workshops](https://gitnation.com/workshops)
  * [People](https://gitnation.com/people)
  * [Mentors](https://gitnation.com/mentors)
  * [Articles](https://gitnation.com/articles)
  * [Multipass](https://gitnation.com/multipass)
  * [All tags](https://gitnation.com/tags)


Newsletter
Do not miss a deal from us. Get new talks, workshops, and free or discounted conference tickets
Subscribe
[GitNation](https://gitnation.com/)
Company
  * [About us](https://gitnation.org/foundation/)
  * [Careers](https://gitnation.org/careers/)
  * Contact us
  * [Promote your product at tech conferences](https://gitnation.com/sponsors)


Assistance
  * [FAQ](https://gitnation.com/faq)
  * Support/Feedback
  * [RSS Feeds](https://gitnation.com/rss-feeds)


Legal
  * [Terms & Conditions](https://gitnation.org/terms)
  * [Privacy Policy](https://gitnation.org/data-promise)
  * [Code Of Conduct](https://gitnation.com/coc)


Community
[](https://www.linkedin.com/company/gitnation/)[](https://twitter.com/GitNationOrg/)[](https://www.instagram.com/gitnation/)[](https://www.tiktok.com/@gitnationorg/)[](https://bsky.app/profile/gitnation.bsky.social)
© 2026 GitNation. All rights reserved.
  * [](https://gitnation.com/javascript-developers-statistics)




## Source: https://infinum.com/handbook/frontend/react/testing/best-practices

[Frontend Handbook](https://infinum.com/handbook/frontend)
  1. [Styleguide](https://infinum.com/handbook/frontend/styleguide)
  2. [How to CSS](https://infinum.com/handbook/frontend/how-to-css)
  3. [Assets](https://infinum.com/handbook/frontend/assets)
  4. [Naming Cheat Sheet](https://infinum.com/handbook/frontend/naming-cheat-sheet)
  5. [Changesets](https://infinum.com/handbook/frontend/changesets)
  6. [Logging](https://infinum.com/handbook/frontend/logging)
  7. Code Quality
    1. [Creating a pull request](https://infinum.com/handbook/frontend/code-quality/creating-a-pull-request)
    2. [Reviewing a pull request](https://infinum.com/handbook/frontend/code-quality/reviewing-a-pull-request)
    3. [Tools](https://infinum.com/handbook/frontend/code-quality/tools)
  8. [Accessibility](https://infinum.com/handbook/frontend/accessibility)
  9. [Email templates](https://infinum.com/handbook/frontend/email-templates)
  10. [Auth](https://infinum.com/handbook/frontend/auth)
  11. [Testing](https://infinum.com/handbook/frontend/testing)
  12. Angular
    1. [Introduction](https://infinum.com/handbook/frontend/angular/introduction)
    2. Getting started with Angular
      1. [Official documentation](https://infinum.com/handbook/frontend/angular/getting-started-with-angular/official-documentation)
      2. [Infinum Angular guidelines and best practices Handbook](https://infinum.com/handbook/frontend/angular/getting-started-with-angular/infinum-angular-guidelines-and-best-practices-handbook)
      3. [Various online resources](https://infinum.com/handbook/frontend/angular/getting-started-with-angular/various-online-resources)
      4. [Get to know RxJS](https://infinum.com/handbook/frontend/angular/getting-started-with-angular/get-to-know-rxjs)
    3. Angular guidelines and best practices
      1. [Core libraries, configuration and tools](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/core-libraries-configuration-and-tools)
      2. [File and module organization and naming](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/file-and-module-organization-and-naming)
      3. [Presentational and smart or container components](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/presentational-and-smart-or-container-components)
      4. [Environments](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/environments)
      5. [Formatting, naming and best practices](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/formatting-naming-and-best-practices)
      6. [Dependency injection](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/dependency-injection)
      7. [Angular Universal (server-side rendering)](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/angular-universal-server-side-rendering)
      8. [Two-way binding](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/two-way-binding)
      9. [Working with forms](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/working-with-forms)
      10. [DatX data store](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/datx-data-store)
      11. [Assets & caching](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/assets-and-caching)
      12. [Localization](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/localization)
      13. [Testing](https://infinum.com/handbook/frontend/angular/angular-guidelines-and-best-practices/testing)
    4. Server-side rendering (SSR)
      1. [Introduction](https://infinum.com/handbook/frontend/angular/server-side-rendering-ssr/introduction)
      2. [Transfer state](https://infinum.com/handbook/frontend/angular/server-side-rendering-ssr/transfer-state)
      3. [Environment variables](https://infinum.com/handbook/frontend/angular/server-side-rendering-ssr/environment-variables)
      4. [SEO and social media sharing](https://infinum.com/handbook/frontend/angular/server-side-rendering-ssr/seo-and-social-media-sharing)
      5. [Robots and sitemap](https://infinum.com/handbook/frontend/angular/server-side-rendering-ssr/robots-and-sitemap)
      6. [Platform specific globals and providers](https://infinum.com/handbook/frontend/angular/server-side-rendering-ssr/platform-specific-globals-and-providers)
  13. React
    1. [Intro](https://infinum.com/handbook/frontend/react/intro)
    2. Getting started
      1. [Ecosystem](https://infinum.com/handbook/frontend/react/getting-started/ecosystem)
      2. [Official documentation](https://infinum.com/handbook/frontend/react/getting-started/official-documentation)
      3. [NextJS](https://infinum.com/handbook/frontend/react/getting-started/nextjs)
      4. [Other useful resources](https://infinum.com/handbook/frontend/react/getting-started/other-useful-resources)
    3. [Project structure](https://infinum.com/handbook/frontend/react/project-structure)
    4. [React hooks](https://infinum.com/handbook/frontend/react/react-hooks)
    5. [Chakra UI](https://infinum.com/handbook/frontend/react/chakra-ui)
    6. Tailwind
      1. [Intro](https://infinum.com/handbook/frontend/react/tailwind/intro)
      2. [Shadcn](https://infinum.com/handbook/frontend/react/tailwind/shadcn)
      3. [Best practices](https://infinum.com/handbook/frontend/react/tailwind/best-practices)
    7. [React Guidelines and Best Practices](https://infinum.com/handbook/frontend/react/react-guidelines-and-best-practices)
    8. [Common SSR errors](https://infinum.com/handbook/frontend/react/common-ssr-errors)
    9. [Libraries](https://infinum.com/handbook/frontend/react/libraries)
    10. Testing
      1. [Best practices](https://infinum.com/handbook/frontend/react/testing/best-practices)
      2. [User actions](https://infinum.com/handbook/frontend/react/testing/user-actions)
      3. [SSR performance](https://infinum.com/handbook/frontend/react/testing/ssr-performance)
      4. [Timers](https://infinum.com/handbook/frontend/react/testing/timers)
    11. Recipes
      1. [Intro](https://infinum.com/handbook/frontend/react/recipes/intro)
      2. [Development proxy](https://infinum.com/handbook/frontend/react/recipes/development-proxy)
      3. [Error Handling](https://infinum.com/handbook/frontend/react/recipes/error-handling)
      4. [Unsupported browser redirection](https://infinum.com/handbook/frontend/react/recipes/unsupported-browser-redirection)
      5. [Characters encoding issue in static pages in NextJS](https://infinum.com/handbook/frontend/react/recipes/characters-encoding-issue-in-static-pages-in-nextjs)
      6. [NextJS font optimization](https://infinum.com/handbook/frontend/react/recipes/nextjs-font-optimization)
      7. [Caching and revalidation](https://infinum.com/handbook/frontend/react/recipes/caching-and-revalidation)
      8. [React Concurrency](https://infinum.com/handbook/frontend/react/recipes/react-concurrency)
      9. [Component Default Props](https://infinum.com/handbook/frontend/react/recipes/component-default-props)
      10. [Datx Store Provider](https://infinum.com/handbook/frontend/react/recipes/datx-store-provider)
      11. [Session Handling](https://infinum.com/handbook/frontend/react/recipes/session-handling)
      12. [Next Auth](https://infinum.com/handbook/frontend/react/recipes/next-auth)
      13. [Imperative update](https://infinum.com/handbook/frontend/react/recipes/imperative-update)
      14. [Keeping consistent values trough rerenders](https://infinum.com/handbook/frontend/react/recipes/keeping-consistent-values-trough-rerenders)
      15. [How to build core component](https://infinum.com/handbook/frontend/react/recipes/how-to-build-core-component)
  14. React Native
    1. [Project setup](https://infinum.com/handbook/frontend/react-native/project-setup)
    2. [Application icon](https://infinum.com/handbook/frontend/react-native/application-icon)
    3. [Custom fonts](https://infinum.com/handbook/frontend/react-native/custom-fonts)
    4. [Styling](https://infinum.com/handbook/frontend/react-native/styling)
    5. [Navigation](https://infinum.com/handbook/frontend/react-native/navigation)
    6. [Data persistence](https://infinum.com/handbook/frontend/react-native/data-persistence)
    7. [Debugging network + Flipper](https://infinum.com/handbook/frontend/react-native/debugging-network-flipper)
    8. [Testing](https://infinum.com/handbook/frontend/react-native/testing)
    9. [Code signing and deployment](https://infinum.com/handbook/frontend/react-native/code-signing-and-deployment)
  15. [Vue](https://infinum.com/handbook/frontend/vue)
  16. Node
    1. [Package managers guidelines](https://infinum.com/handbook/frontend/node/package-managers-guidelines)
    2. [Managing Node-NPM versions](https://infinum.com/handbook/frontend/node/managing-node-npm-versions)
  17. SASS Styleguide
    1. [File organization](https://infinum.com/handbook/frontend/sass-styleguide/file-organization)
    2. [Code quality](https://infinum.com/handbook/frontend/sass-styleguide/code-quality)
  18. [Useful links](https://infinum.com/handbook/frontend/useful-links)


[](https://infinum.com/)
Frontend Handbook
[Homepage](https://infinum.com/handbook/)
Best practices
Last modified on Fri 27 Feb 2026
Tools we use for testing are [React-Testing-Library](https://testing-library.com/docs/) and [Jest](https://jestjs.io/docs/en/getting-started)
##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#video-guide)Video guide
If you want to see more practical usage, [here](https://www.youtube.com/watch?v=KfaFyB0uedk) is the recording form JS Standup about next.js testing presented by 🦌. The project tested in the video is LearnReact project.
##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#setup)Setup
First of all, install Jest:

```
pnpm install -D -E jest @types/jest

```

Add a test script to `package.json`:

```
  "scripts": {
    "test": "jest",

    // optional?
    "test:ci": "jest --ci --coverage",
    "test:update": "pnpm test -- --u",
    "test:watch": "pnpm test -- --watch",
    // ...other scripts
  }

```

Create the `jest.config.js` file in the project root and follow the instructions for the [Rust compiler setup](https://nextjs.org/docs/testing#setting-up-jest-with-the-rust-compiler).
Next, install `react-test-library`:

```
pnpm i -D -E @testing-library/react

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#user-events)User events
Use [testing-library/user-event](https://github.com/testing-library/user-event) for mocking events:

```
pnpm install -D -E @testing-library/user-event

```

##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#utils)Utils
###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#mock-providers-and-store)Mock providers and store
While testing, we need to mock various providers like [`<ChakraProvider>`](https://chakra-ui.com/docs/getting-started#setup-provider/). To mock all providers, we can create a `./__tests__/test-utils.tsx` file where we will export the [custom render](https://testing-library.com/docs/react-testing-library/setup/#custom-render) method with all providers:

```
const AllProviders = ({ children }) => (
  <ChakraProvider theme={theme}>{children}</ChakraProvider>
);

```

Beside providers, we need to mock the [datx](https://datx.dev/) store:

```
export const StoreMockContext = React.createContext<AppCollection | null>(null);

const withMockStore = (PageComponent: NextPage) => {
  const WithMockStore: FC = (props) => {
    const store: AppCollection = new AppCollection();

    return (
      <StoreMockContext.Provider value={store}>
        <PageComponent {...props} />
      </StoreMockContext.Provider>
    );
  };

  return WithMockStore;
};

```

While testing we can wrap the component in `<StoreMockContext.Consumer>` to get access to the store. The store is needed for mocking the datx model with relationships.
After mocking all providers and the store, we export everything:

```
const customRender = (ui: React.ReactElement, options?: any) =>
  render(ui, { wrapper: withMockStore(AllProviders), ...options });

// re-export everything
export * from "@testing-library/react";

// override render method
export { customRender as render };

```

Now, when testing components we'll import `render` from `__tests__/test-utils.tsx` instead of `@testing-library/react`, like this:

```
import { render } from "__tests__/test-utils";

```

Or if we add `path` to `tsconfig`:

```
{
  "compilerOptions": {
    ...
    "paths": {
      ...
      "@test-utils": ["__tests__/test-utils.tsx"]
    }
  },
}

```

Then we can import render like this:

```
import { render } from "@test-utils";

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#folder-structure)Folder structure
All tests should be defined in the same directory where the file being tested is. There is one exception, and that is the `pages` folder because Next.js doesn't allow tests in the `pages` folder. That's why we have the `__tests__` folder in the root of our application.
Example:

```
src
.
├── __mocks__
│   └── react-i18next.tsx
├── __tests__
│   ├── pages
│   │   └── user.test.ts
│   └── test-utils.tsx
├── pages
│   └── user.ts
├── fetchers
│   └── users
│       ├── users.ts
│       └── users.test.ts
└── components
    └── shared
        └── Button
            ├── Button.test.tsx
            └── Button.tsx

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#code__mocks__code)`__mocks__`
Manual mocks are used to stub out functionality with mock data. For example, instead of accessing a resource from `node_modules` you might want to create a mock module that allows you to use fake data. Manual mocks are defined by writing a module in the `__mocks__/` subdirectory immediately adjacent to the module. ([docs](https://jestjs.io/docs/en/manual-mocks))
For example, if we want to mock [react-i18next](https://react.i18next.com/), we will create `./__mocks__/react-i18next.tsx`

```
import {
  I18nextProvider,
  initReactI18next,
  setDefaults,
  getDefaults,
  setI18n,
  getI18n,
} from "react-i18next";

const useMock = [(k) => k, {}];
useMock.t = (k) => k;
useMock.i18n = {
  language: "en-GB",
};

module.exports = {
  // this mock makes sure any components using the translate HoC receive the t function as a prop
  withTranslation: () => (Component) => (props) =>
    <Component t={(k) => k} {...props} />,
  useTranslation: jest.fn(() => useMock),

  // mock if needed
  I18nextProvider,
  initReactI18next,
  setDefaults,
  getDefaults,
  setI18n,
  getI18n,
};

```

##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#introduction)Introduction
Based on [the Guiding Principles](https://testing-library.com/docs/guiding-principles/), your tests should resemble how users interact with your code (component, page, etc.) as much as possible. In this context, the user is not the end application user, but some parent component that would use the component that is being tested.
**Query priorities** ([more info](https://testing-library.com/docs/guide-which-query/)):
  1. Queries Accessible to Everyone queries that reflect the experience of visual/mouse users as well as those that use assistive technology


  * `getByRole` - this can be used to query every element that is exposed in the accessibility tree. With the `name` option you can filter the returned elements by their accessible name. This should be your top preference for just about everything. There's not much you can't get with this (if you can't, it's possible your UI is inaccessible). Most often, this will be used with the name option like so: `getByRole('button', {name: /submit/i})`. Check the [list of roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques#roles).
  * `getByLabelText` - only really good for form fields, but this is the number one method a user finds those elements, so it should be your top preference.
  * `getByPlaceholderText` - a placeholder is not a substitute for a label. But if that's all you have, then it's better than alternatives.
  * `getByText` - not useful for forms, but this is the number 1 method a user finds most non-interactive elements (like divs and spans).
  * `getByDisplayValue` - the current value of a form element can be useful when navigating a page with filled-in values.


  1. Semantic Queries HTML5 and ARIA compliant selectors. Note that the user experience of interacting with these attributes varies greatly across browsers and assistive technology.


  * `getByAltText` - if your element is one which supports `alt` text (`img`, `area`, and `input`), then you can use this to find that element
  * `getByTitle` - the title attribute is not consistently read by screenreaders, and is not visible by default for sighted users


  1. Test IDs


  * `getByTestId` - The user cannot see (or hear) these, so this is only recommended for cases where you can't match by role or text or it doesn't make sense (e.g. the text is dynamic).


**Avoid unnecessary "is rendering" test**
Since we have no value in testing whether our component will correctly render, avoid writing these type of tests and focus on more valuable tests instead.
**Avoid destructuring`render` result for querying/finding elements**
It is recommended that you avoid destructuring the `render(...)` result and use `screen` object instead. To see more info about [why you should use screen](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library#not-using-screen), and other common mistakes in RTL usage, please refer to the [Kents](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library) blog post.
###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#naming-convention)Naming Convention
Tests should have meaningful names and should be nested properly by following the next pattern:
  1. Root `describe` must be the same as the component/page/hook/util we're testing
  2. Nested `describe`s must have the `when` prefix (to indicate specific scenarios)
  3. Description of `it` must be a use case sentence


An example:

```
describe("useAuth", () => {
  it("should throw context error", () => {
    // ...
  });
  it("should toggle loading state", () => {
    // ..
  });

  describe("when user exists", () => {
    it("should return the user object", () => {
      // ...
    });
    it("should log out user", () => {
      // ...
    });
  });

  describe("when user does not exist", () => {
    it("should return guest user", () => {
      // ...
    });
    it("should destroy session on window close", () => {
      // ...
    });
  });
});

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#basic-test-example)Basic test example
Base Component:

```
const Button: FC<ButtonProps> = (props) => <button {...props} />;

```

Test:

```
describe("Button", () => {
  // or something more meaningful
  it("should handle click", () => {
    const buttonText = "click here";
    const testOnClick = jest.fn();

    render(<Button onClick={testOnClick}>{buttonText}</Button>);

    user.click(screen.getByText(buttonText));

    expect(testOnClick).toBeCalledTimes(1);
  });
});

```

**Components that use a base component test example**
Component:

```
import { Button } from "components/Button";

const UserCard: FC<UserCardProps> = ({ title }) => (
  <Card>
    <h3>{title}</h3>
    <Button>click</Button>
  </Card>
);

```

Test:
Here, the `Button` component is mocked since we only care about the specifics of the `UserCard` component. This is especially useful when you don't want to generate a large tree inside your tests for components that don't have any impact on the actual test.

```
import { screen } from '@testing-library/react';
import { Button } from "components/Button";

jest.mock("components/Button");
(Button as jest.Mock).mockReturnValue(<button />);

describe("UserCard", () => {
  it("should display the correct title", () => {
    const username = "Test User";

    render(<UserCard title={username} />);

    expect(screen.getByText(username)).toBeDefined();
  });
});

```

##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#repeated-component-rendering)Repeated component rendering
Describe your rendering inside `beforeEach` so you could use `screen.{getBySomething}` in your tests later, to reduce number of unnecessary renders.
An example:

```
describe("AlertButton", () => {
  let title: string;
  let confirmButtonText: string;
  let onConfirm: () => void;

  beforeEach(() => {
    title = "Bonjour";
    confirmButtonText = "Like, share, subscribe";
    onConfirm = jest.fn();

    render(
      <AlertButton
        title={title}
        confirmButtonText={confirmButtonText}
        onConfirm={onConfirm}
      />
    );
  });

  describe("when clicked", () => {
    beforeEach(async () => {
      await waitFor(() => {
        user.click(screen.getByText(buttonText));
      });
    });

    it("should open alert dialog", () => {
      expect(screen.queryByRole("alertdialog")).toBeNull();
    });
    it("should display correct title", () => {
      expect(screen.queryByText(title)).not.toBeNull();
    });
  });

  describe("when confirm is clicked", () => {
    beforeEach(async () => {
      await waitFor(() => {
        user.click(screen.getByText(buttonText));
      });
    });

    it("should close the dialog", () => {
      expect(screen.queryByRole("alertdialog")).toBeNull();
    });

    // ... more test cases
  });
});

```

> **Note:** This is a shortened example of this concept, you can refer to the standup video section for more info: [Next.js testing - Testing shared components](https://youtu.be/KfaFyB0uedk?t=1005)
##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#testing-user-events)Testing user events
User actions are the bread and butter of interactive web applications. Testing user actions means ensuring that when a user clicks, drags, types, or interacts with your application in any way, the app behaves correctly.
**Why is it important?** \ React components often encapsulate user interactions. Imagine a form where a user submits data or a button that toggles a specific state. If these don't work as expected, users can lose trust in our application. Or worse, our brand.
**Testing Flow:** \ To test user actions, you'll usually:
  1. Render the component under test.
  2. Simulate a user action (like a button click).
  3. Check the outcome – this could be a changed state, a rendered element, or an API call.


**Further Exploration:** We have added a more comprehensive chapter on **Testing User Actions** , providing real-world examples and a guide that will help you ensure your React applications respond correctly to user interactions. You can find it here: [Testing - User actions](https://infinum.com/handbook/frontend/react/testing/user-actions)
##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#page-component-testing)Page component testing
Pages tests should be located in `src/__tests__/pages` folder because Next.js is not allowing tests in `/pages` folder. Test name should be the same as the page file with `test.tsx` extension.
Page example:

```
const UserPage: NextPage = () => {
  const { data, error } = useSWR<Array<User>, IResponseError>(
    USER_KEY,
    fetchUsers
  );

  if (error) {
    return <ErrorPage />;
  }

  if (!data) {
    return <LoadingPage />;
  }

  return <UserTemplate userList={data} />;
};

export default UserPage;

```

In this page example we should test all three states of the page component. To do that we should mock `<ErrorPage>`, `<LoadingPage>` and `<UserTemplate>` and check if it's rendered based on the fetcher response.
Test example:

```
jest.mock("components/error-page");
jest.mock("components/loading-page");
jest.mock("components/user-template");
jest.mock("fetchers/users");

(ErrorPage as jest.Mock).mockReturnValue(
  <div data-testid="error-page-testid" />
);
(LoadingPage as jest.Mock).mockReturnValue(
  <div data-testid="loading-page-testid" />
);
(UserTemplate as jest.Mock).mockReturnValue(
  <div data-testid="user-template-page-testid" />
);

describe("User Page", () => {
  it("should render error page", async () => {
    (fetchUsers as jest.Mock).mockResolvedValue(new Error("Error occurred!"));

    render(<UserPage />);

    expect(await screen.findByTestId("error-page-testid")).toBeDefined();
  });
  it("should render loading page", async () => {
    (fetchUsers as jest.Mock).mockResolvedValue(null);

    render(<UserPage />);

    expect(await screen.findByTestId("loading-page-testid")).toBeDefined();
  });
  it("should render user page", async () => {
    (fetchUsers as jest.Mock).mockResolvedValue([{ username: "test user" }]);

    render(<UserPage />);

    expect(
      await screen.findByTestId("user-template-page-testid")
    ).toBeDefined();
  });
});

```

Because of testing `useSWR` behavior (which will re-render DOM after fetcher promise is resolved), we need to use `findByTestId` method that returns a promise that will resolve when the element is added to DOM.
###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#swr-testing)SWR testing
To use SWR in your tests, add `SWRConfig` to your `AllProviders` mock with the following setup (note: your cases could require more customization):

```
const AllProviders = ({ children }) => (
  <SWRConfig value={{ dedupingInterval: 0, provider: () => new Map() }}>
    <ChakraProvider theme={theme}>{children}</ChakraProvider>
  </SWRConfig>
);

```

With this setup, we are sure that each component we're testing will have its own cache, so we don't have to manually clear the cache before each test.
Check out [this issue](https://github.com/vercel/swr/issues/781) and [this answer](https://github.com/vercel/swr/issues/781#issuecomment-952738214) that explains fixing the known problem.
###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#server-side-rendering)Server side rendering
For testing pages that are rendered on server we use [next-page-tester](https://github.com/toomuchdesign/next-page-tester). It is used for testing pages that fetch data in `getServerSideProps` or `getStaticProps`.
User page example:

```
const UserPage: NextPage<any> = ({ data }) => {
  return <UserTemplate users={data} />;
};

export async function getServerSideProps() {
  const store = new AppCollection();

  const data = await fetchUsers(store);

  return { props: { data } };
}

export default UserPage;

```

Test example:

```
describe("User Page", () => {
  it("displays user data", async () => {
    (fetchUsers as jest.Mock).mockResolvedValue([
      new User({
        id: "1",
        name: "Test user",
        role: new Role({ name: RoleTypes.User }),
      }),
    ]);

    const { render } = await getPage({
      route: "/user",
    });

    render();

    expect(screen.queryByText("Test user")).not.toBeNull();
  });
});

```

##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#testing-passed-props)Testing passed props
A quick how to on using Jest to check if correct props are passed to a child component.
This example is purely to show how to verify that a React components props are passed in a Jest unit test. There are two components, a `MyModal` and a `Modal` from Chakra UI library. The `MyModal` renders `Modal` and `Button`, and the 'open' state is handled with `useDisclosure` hook. The goal is to check if `Modal` component gets the `isOpen={true}` prop when the user clicks the button.

```
// MyModal.tsx
export const MyModal: FC<ButtonProps> = (props) => {
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <>
      <Button {...props} onClick={onOpen}>
        Open my modal
      </Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        {/* Modal stuff */}
      </Modal>
    </>
  );
};

// MyModal.test.tsx
import { Modal } from "@chakra-ui/react";

jest.mock("@chakra-ui/react", () => {
  const originalImplementation = jest.requireActual("@chakra-ui/react");

  return {
    ...originalImplementation,
    Modal: jest.fn((props) => {
      const { Modal: OriginalModal } = jest.requireActual("@chakra-ui/react");

      return <OriginalModal {...props} />;
    }),
  };
});

describe("MyModal", () => {
  it("should open on click", () => {
    render(<MyModal />);

    expect(Modal).toBeCalledWith(
      expect.objectContaining({ isOpen: false }),
      expect.anything()
    );

    const button = screen.queryByRole("button");
    expect(button).toBeDefined();

    userEvent.click(button);
    expect(Modal).toBeCalledWith(
      expect.objectContaining({ isOpen: true }),
      expect.anything()
    );
  });
});

```

##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#fetchers)Fetchers
Fetcher tests should be located in `/fetchers/{{ fetcher name }}` folder next to the fetcher that is tested.

```
...
└── fetchers
    └── users
        ├── user.ts
        └── user.test.ts

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#using-datx)Using datx:
When testing fetchers that use Datx, we create mocked store Datx store and instead of making API calls with `request` we need to mock `request` and test the functionality of the fetcher.
In the example below our fetcher fetches one User model and if the user doesn't have a relationship to Role model we add a default one.

```
export async function fetchUser(
  store: AppCollection,
  id: string
): Promise<User> {
  try {
    const response = await store.request(`users/${id}`, "GET", undefined, {
      include: ["role"],
    });
    const user = response.data as User;

    if (user.role === null) {
      const newRole = store.add({ name: RoleTypes.User }, Role);
      user.role = newRole;
    }

    return user;
  } catch (resError) {
    throw resError.error;
  }
}

```

Test example:

```
describe("fetchUser", () => {
  it("should return success with only user", async () => {
    const mockStore = new AppCollection();
    const mockUser = mockStore.add({}, User);

    mockStore.request = jest.fn().mockResolvedValue({ data: mockUser });

    const fetchResponse = await fetchUsers(mockStore, "1");

    expect(fetchResponse).toBeInstanceOf(User);
    expect(fetchResponse.role).toBeDefined();
    expect(fetchResponse.role.name).toBe(RoleTypes.User);
  });

  it("should return success with user and role", async () => {
    const mockStore = new AppCollection();
    const mockRole = mockStore.add({ name: RoleTypes.Superadmin }, Role);
    const mockUser = mockStore.add({ role: mockRole }, User);

    mockStore.request = jest.fn().mockResolvedValue({ data: mockUser });

    const fetchResponse = await fetchUsers(mockStore, "1");

    expect(fetchResponse).toBeInstanceOf(User);
    expect(fetchResponse.role).toBeDefined();
    expect(fetchResponse.role.name).toBe(RoleTypes.Superadmin);
  });

  it("should return an error", async () => {
    const mockError = { description: "Error occurred!" };
    const mockStore = new AppCollection();
    mockStore.request = jest.fn().mockRejectedValue({ error: [mockError] });

    try {
      await fetchUsers(mockStore, "1");
    } catch (fetchError) {
      expect(fetchError.length).toBe(1);
      expect(fetchError[0]).toBe(mockError);
    }
  });
});

```

For more info about testing asynchronous code read [docs](https://jestjs.io/docs/en/asynchronous).
##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#mocking-api-routes)Mocking API routes
[Mock Service Worker](https://mswjs.io/docs/) is an API mocking library that uses Service Worker API to intercept actual requests.
Example:

```
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";

const apiEndpoint = "http://localhost:3000";

const mockTodoData = [{ title: "Todo #1", todos: [] }];

const server = setupServer(
  // Describe the requests to mock.
  http.post(`${apiEndpoint}/api/todo-lists`, () => {
    return HttpResponse.json(mockTodoData);
  })
);

beforeAll(() => {
  // Establish requests interception layer before all tests.
  server.listen();
});

afterAll(() => {
  // Clean up after all tests are done
  server.close();
});

test("TodoComponent renders correct number of rows", async () => {
  render(<TodoList />);

  const Rows = screen.getAllByRole("row");
  expect(Rows.length).toBe(1);
});

```

##  [](https://infinum.com/handbook/frontend/react/testing/best-practices#hooks)Hooks
`@testing-library/react` provides `renderHook` and `act` for testing custom hooks. These utilities create a simple test harness that handles running hooks within the body of a function component, as well as providing various useful utility functions for updating the inputs and retrieving the outputs of your custom hook. This approach provides a testing experience as close as possible to how your hook is used in a real component.
###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#example-hook)Example hook:

```
function useModal(initialOpen = false) {
  const [isOpen, setOpen] = useState(initialOpen);

  const toggle = useCallback(() => {
    setIsOpen(!isOpen);
  }, [isOpen]);

  const close = useCallback(() => {
    setIsOpen(false);
  }, []);

  return { isOpen, close, toggle };
}

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#example-test)Example test:

```
describe("useModal", () => {
  it("should toggle isOpen on toggle call", async () => {
    const { result } = renderHook(() => useModal());

    await waitFor(() => {
      result.current.toggle();
    });

    expect(result.current.isOpen).toBe(true);
  });

  it("should change isOpen to false on close call", async () => {
    const { result } = renderHook(() => useModal(true));

    await waitFor(() => {
      result.current.close();
    });

    expect(result.current.isOpen).toBe(false);
  });
});

```

###  [](https://infinum.com/handbook/frontend/react/testing/best-practices#mock-hooks)Mock hooks
Sometimes we want our custom hook to return a mock response while we test component consuming it.
Example hook:

```
// @/hooks/useTodos.ts
export const useTodos = (config?: SWRConfiguration) => {
  return useSWR(() => {
    return "api/todo-lists";
  }, config);
};

```

Example mock and test:

```
import * as hooks from "@/hooks/useTodos";

const mockTodoData = [{ title: "Todo #1", todos: [] }];

jest.spyOn(hooks, "useTodos").mockImplementation(() => {
  return {
    data: mockTodoData,
  } as SWRResponse;
});

test("TodoComponent renders correct number of rows", async () => {
  render(<TodoList />); // uses useTodos

  const Rows = screen.getAllByRole("row");
  expect(Rows.length).toBe(1);
});

```

Spy will now redirect any hook calls to mock implementation.
[Libraries](https://infinum.com/handbook/frontend/react/libraries)[User actions](https://infinum.com/handbook/frontend/react/testing/user-actions)
[© 2026 Infinum Inc.](https://infinum.com/)
[Subscribe to Infinum Frontend Newsletter](https://frontendcookies.ongoodbits.com/)[Visit infinum.com](https://infinum.com)
Login


## Source: https://testing-library.com/docs/react-testing-library/intro/

[Skip to main content](https://testing-library.com/docs/react-testing-library/intro/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/react-testing-library/intro/)
  * [Core API](https://testing-library.com/docs/react-testing-library/intro/)
  * [Frameworks](https://testing-library.com/docs/react-testing-library/intro/)
    * [DOM Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/react-testing-library/intro)
      * [Example](https://testing-library.com/docs/react-testing-library/example-intro)
      * [Setup](https://testing-library.com/docs/react-testing-library/setup)
      * [API](https://testing-library.com/docs/react-testing-library/api)
      * [Migrate from Enzyme](https://testing-library.com/docs/react-testing-library/migrate-from-enzyme)
      * [FAQ](https://testing-library.com/docs/react-testing-library/faq)
      * [Cheatsheet](https://testing-library.com/docs/react-testing-library/cheatsheet)
    * [Vue Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Angular Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Svelte Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Marko Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Preact Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Reason Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Native Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Solid Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Qwik Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/react-testing-library/intro/)
  * [Ecosystem](https://testing-library.com/docs/react-testing-library/intro/)


  * [](https://testing-library.com/)
  * Frameworks
  * React Testing Library
  * Introduction


On this page
# React Testing Library
[`React Testing Library`](https://github.com/testing-library/react-testing-library) builds on top of `DOM Testing Library` by adding APIs for working with React components.
## Installation[​](https://testing-library.com/docs/react-testing-library/intro/#installation "Direct link to heading")
To get started with `React Testing Library`, you'll need to install it together with its peerDependency `@testing-library/dom`:
  * npm
  * Yarn



```
npm install --save-dev @testing-library/react @testing-library/dom  

```


```
yarn add --dev @testing-library/react @testing-library/dom  

```

### With TypeScript[​](https://testing-library.com/docs/react-testing-library/intro/#with-typescript "Direct link to heading")
To get full type coverage, you need to install the types for `react` and `react-dom` as well:
  * npm
  * Yarn



```
npm install --save-dev @testing-library/react @testing-library/dom @types/react @types/react-dom  

```


```
yarn add --dev @testing-library/react @testing-library/dom @types/react @types/react-dom  

```

## The problem[​](https://testing-library.com/docs/react-testing-library/intro/#the-problem "Direct link to heading")
You want to write maintainable tests for your React components. As a part of this goal, you want your tests to avoid including implementation details of your components and rather focus on making your tests give you the confidence for which they are intended. As part of this, you want your testbase to be maintainable in the long run so refactors of your components (changes to implementation but not functionality) don't break your tests and slow you and your team down.
## This solution[​](https://testing-library.com/docs/react-testing-library/intro/#this-solution "Direct link to heading")
The `React Testing Library` is a very light-weight solution for testing React components. It provides light utility functions on top of `react-dom` and `react-dom/test-utils`, in a way that encourages better testing practices. Its primary guiding principle is:
> [The more your tests resemble the way your software is used, the more confidence they can give you.](https://testing-library.com/docs/guiding-principles)
So rather than dealing with instances of rendered React components, your tests will work with actual DOM nodes. The utilities this library provides facilitate querying the DOM in the same way the user would. Finding form elements by their label text (just like a user would), finding links and buttons from their text (like a user would). It also exposes a recommended way to find elements by a `data-testid` as an "escape hatch" for elements where the text content and label do not make sense or is not practical.
This library encourages your applications to be more accessible and allows you to get your tests closer to using your components the way a user will, which allows your tests to give you more confidence that your application will work when a real user uses it.
This library is a replacement for [Enzyme](http://airbnb.io/enzyme/). While you _can_ follow these guidelines using Enzyme itself, enforcing this is harder because of all the extra utilities that Enzyme provides (utilities which facilitate testing implementation details). Read more about this in [the FAQ](https://testing-library.com/docs/react-testing-library/faq).
**What this library is not** :
  1. A test runner or framework
  2. Specific to a testing framework (though we recommend Jest as our preference, the library works with any framework. See [Using Without Jest](https://testing-library.com/docs/react-testing-library/setup#using-without-jest))


> NOTE: This library is built on top of [`DOM Testing Library`](https://testing-library.com/docs/dom-testing-library/intro) which is where most of the logic behind the queries is.
## Tutorials[​](https://testing-library.com/docs/react-testing-library/intro/#tutorials "Direct link to heading")
Have a look at the "What is React Testing library?" video below for an introduction to the library.
[![what is react testing library](https://img.youtube.com/vi/JKOwJUM4_RM/0.jpg)](https://youtu.be/JKOwJUM4_RM)
Also, don't miss this [tutorial for React Testing Library](https://www.robinwieruch.de/react-testing-library).
[](https://github.com/testing-library/testing-library-docs/edit/main/docs/react-testing-library/intro.mdx)
Last updated on **Jun 3, 2024** by **Matan Borenkraout**
[Previous Cheatsheet](https://testing-library.com/docs/dom-testing-library/cheatsheet)[Next Example](https://testing-library.com/docs/react-testing-library/example-intro)
  * [Installation](https://testing-library.com/docs/react-testing-library/intro/#installation)
    * [With TypeScript](https://testing-library.com/docs/react-testing-library/intro/#with-typescript)
  * [The problem](https://testing-library.com/docs/react-testing-library/intro/#the-problem)
  * [This solution](https://testing-library.com/docs/react-testing-library/intro/#this-solution)
  * [Tutorials](https://testing-library.com/docs/react-testing-library/intro/#tutorials)


Docs
  * [Getting Started](https://testing-library.com/docs)
  * [Examples](https://testing-library.com/docs/example-codesandbox)
  * [API](https://testing-library.com/docs/dom-testing-library/api)
  * [Help](https://testing-library.com/docs/dom-testing-library/faq)


Community
  * [Blog](https://testing-library.com/blog)
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/react-testing-library)
  * [Discord](https://discord.gg/testing-library)


More
  * [Star](https://github.com/testing-library/react-testing-library)
  * [GitHub](https://github.com/testing-library)
  * [Edit Docs on GitHub](https://github.com/testing-library/testing-library-docs)
  * [Hosted by Netlify](https://netlify.com)


![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-128x128.png)
Copyright © 2018-2026 Kent C. Dodds and contributors


## Source: https://legacy.reactjs.org/docs/testing.html

[](https://surveys.savanta.com/survey/selfserve/21e3/210643?list=2)We want to hear from you![Take our 2021 Community Survey!](https://surveys.savanta.com/survey/selfserve/21e3/210643?list=2)
This site is no longer updated.[Go to react.dev](https://react.dev/blog/2023/03/16/introducing-react-dev)
[![](https://legacy.reactjs.org/docs/testing.html)React](https://legacy.reactjs.org/)[Docs](https://legacy.reactjs.org/docs/getting-started.html)[Tutorial](https://legacy.reactjs.org/tutorial/tutorial.html)[Blog](https://legacy.reactjs.org/blog/)[Community](https://legacy.reactjs.org/community/support.html)
[v18.2.0](https://legacy.reactjs.org/versions)[Languages](https://legacy.reactjs.org/languages)[GitHub](https://github.com/facebook/react/)
# Testing Overview
You can test React components similar to testing other JavaScript code.
There are a few ways to test React components. Broadly, they divide into two categories:
  * **Rendering component trees** in a simplified test environment and asserting on their output.
  * **Running a complete app** in a realistic browser environment (also known as “end-to-end” tests).


This documentation section focuses on testing strategies for the first case. While full end-to-end tests can be very useful to prevent regressions to important workflows, such tests are not concerned with React components in particular, and are out of the scope of this section.
###  [](https://legacy.reactjs.org/docs/testing.html#tradeoffs)Tradeoffs 
When choosing testing tools, it is worth considering a few tradeoffs:
  * **Iteration speed vs Realistic environment:** Some tools offer a very quick feedback loop between making a change and seeing the result, but don’t model the browser behavior precisely. Other tools might use a real browser environment, but reduce the iteration speed and are flakier on a continuous integration server.
  * **How much to mock:** With components, the distinction between a “unit” and “integration” test can be blurry. If you’re testing a form, should its test also test the buttons inside of it? Or should a button component have its own test suite? Should refactoring a button ever break the form test?


Different answers may work for different teams and products.
###  [](https://legacy.reactjs.org/docs/testing.html#tools)Recommended Tools 
**[Jest](https://facebook.github.io/jest/)** is a JavaScript test runner that lets you access the DOM via [`jsdom`](https://legacy.reactjs.org/docs/testing-environments.html#mocking-a-rendering-surface). While jsdom is only an approximation of how the browser works, it is often good enough for testing React components. Jest provides a great iteration speed combined with powerful features like mocking [modules](https://legacy.reactjs.org/docs/testing-environments.html#mocking-modules) and [timers](https://legacy.reactjs.org/docs/testing-environments.html#mocking-timers) so you can have more control over how the code executes.
**[React Testing Library](https://testing-library.com/react)** is a set of helpers that let you test React components without relying on their implementation details. This approach makes refactoring a breeze and also nudges you towards best practices for accessibility. Although it doesn’t provide a way to “shallowly” render a component without its children, a test runner like Jest lets you do this by [mocking](https://legacy.reactjs.org/docs/testing-recipes.html#mocking-modules).
###  [](https://legacy.reactjs.org/docs/testing.html#learn-more)Learn More 
This section is divided in two pages:
  * [Recipes](https://legacy.reactjs.org/docs/testing-recipes.html): Common patterns when writing tests for React components.
  * [Environments](https://legacy.reactjs.org/docs/testing-environments.html): What to consider when setting up a testing environment for React components.


Is this page useful?[Edit this page](https://github.com/reactjs/reactjs.org/tree/main/content/docs/testing.md)
Installation
  * [Getting Started](https://legacy.reactjs.org/docs/getting-started.html)
  * [Add React to a Website](https://legacy.reactjs.org/docs/add-react-to-a-website.html)
  * [Create a New React App](https://legacy.reactjs.org/docs/create-a-new-react-app.html)
  * [CDN Links](https://legacy.reactjs.org/docs/cdn-links.html)
  * [Release Channels](https://legacy.reactjs.org/docs/release-channels.html)


Main Concepts
  * [1. Hello World](https://legacy.reactjs.org/docs/hello-world.html)
  * [2. Introducing JSX](https://legacy.reactjs.org/docs/introducing-jsx.html)
  * [3. Rendering Elements](https://legacy.reactjs.org/docs/rendering-elements.html)
  * [4. Components and Props](https://legacy.reactjs.org/docs/components-and-props.html)
  * [5. State and Lifecycle](https://legacy.reactjs.org/docs/state-and-lifecycle.html)
  * [6. Handling Events](https://legacy.reactjs.org/docs/handling-events.html)
  * [7. Conditional Rendering](https://legacy.reactjs.org/docs/conditional-rendering.html)
  * [8. Lists and Keys](https://legacy.reactjs.org/docs/lists-and-keys.html)
  * [9. Forms](https://legacy.reactjs.org/docs/forms.html)
  * [10. Lifting State Up](https://legacy.reactjs.org/docs/lifting-state-up.html)
  * [11. Composition vs Inheritance](https://legacy.reactjs.org/docs/composition-vs-inheritance.html)
  * [12. Thinking In React](https://legacy.reactjs.org/docs/thinking-in-react.html)


Advanced Guides
  * [Accessibility](https://legacy.reactjs.org/docs/accessibility.html)
  * [Code-Splitting](https://legacy.reactjs.org/docs/code-splitting.html)
  * [Context](https://legacy.reactjs.org/docs/context.html)
  * [Error Boundaries](https://legacy.reactjs.org/docs/error-boundaries.html)
  * [Forwarding Refs](https://legacy.reactjs.org/docs/forwarding-refs.html)
  * [Fragments](https://legacy.reactjs.org/docs/fragments.html)
  * [Higher-Order Components](https://legacy.reactjs.org/docs/higher-order-components.html)
  * [Integrating with Other Libraries](https://legacy.reactjs.org/docs/integrating-with-other-libraries.html)
  * [JSX In Depth](https://legacy.reactjs.org/docs/jsx-in-depth.html)
  * [Optimizing Performance](https://legacy.reactjs.org/docs/optimizing-performance.html)
  * [Portals](https://legacy.reactjs.org/docs/portals.html)
  * [Profiler](https://legacy.reactjs.org/docs/profiler.html)
  * [React Without ES6](https://legacy.reactjs.org/docs/react-without-es6.html)
  * [React Without JSX](https://legacy.reactjs.org/docs/react-without-jsx.html)
  * [Reconciliation](https://legacy.reactjs.org/docs/reconciliation.html)
  * [Refs and the DOM](https://legacy.reactjs.org/docs/refs-and-the-dom.html)
  * [Render Props](https://legacy.reactjs.org/docs/render-props.html)
  * [Static Type Checking](https://legacy.reactjs.org/docs/static-type-checking.html)
  * [Strict Mode](https://legacy.reactjs.org/docs/strict-mode.html)
  * [Typechecking With PropTypes](https://legacy.reactjs.org/docs/typechecking-with-proptypes.html)
  * [Uncontrolled Components](https://legacy.reactjs.org/docs/uncontrolled-components.html)
  * [Web Components](https://legacy.reactjs.org/docs/web-components.html)


API Reference
  * [React](https://legacy.reactjs.org/docs/react-api.html)
    * [React.Component](https://legacy.reactjs.org/docs/react-component.html)
  * [ReactDOM](https://legacy.reactjs.org/docs/react-dom.html)
  * [ReactDOMClient](https://legacy.reactjs.org/docs/react-dom-client.html)
  * [ReactDOMServer](https://legacy.reactjs.org/docs/react-dom-server.html)
  * [DOM Elements](https://legacy.reactjs.org/docs/dom-elements.html)
  * [SyntheticEvent](https://legacy.reactjs.org/docs/events.html)
  * [Test Utilities](https://legacy.reactjs.org/docs/test-utils.html)
  * [Test Renderer](https://legacy.reactjs.org/docs/test-renderer.html)
  * [JS Environment Requirements](https://legacy.reactjs.org/docs/javascript-environment-requirements.html)
  * [Glossary](https://legacy.reactjs.org/docs/glossary.html)


Hooks
  * [1. Introducing Hooks](https://legacy.reactjs.org/docs/hooks-intro.html)
  * [2. Hooks at a Glance](https://legacy.reactjs.org/docs/hooks-overview.html)
  * [3. Using the State Hook](https://legacy.reactjs.org/docs/hooks-state.html)
  * [4. Using the Effect Hook](https://legacy.reactjs.org/docs/hooks-effect.html)
  * [5. Rules of Hooks](https://legacy.reactjs.org/docs/hooks-rules.html)
  * [6. Building Your Own Hooks](https://legacy.reactjs.org/docs/hooks-custom.html)
  * [7. Hooks API Reference](https://legacy.reactjs.org/docs/hooks-reference.html)
  * [8. Hooks FAQ](https://legacy.reactjs.org/docs/hooks-faq.html)


Testing
  * [](https://legacy.reactjs.org/docs/testing.html)
  * [Testing Recipes](https://legacy.reactjs.org/docs/testing-recipes.html)
  * [Testing Environments](https://legacy.reactjs.org/docs/testing-environments.html)


Contributing
  * [How to Contribute](https://legacy.reactjs.org/docs/how-to-contribute.html)
  * [Codebase Overview](https://legacy.reactjs.org/docs/codebase-overview.html)
  * [Implementation Notes](https://legacy.reactjs.org/docs/implementation-notes.html)
  * [Design Principles](https://legacy.reactjs.org/docs/design-principles.html)


FAQ
  * [AJAX and APIs](https://legacy.reactjs.org/docs/faq-ajax.html)
  * [Babel, JSX, and Build Steps](https://legacy.reactjs.org/docs/faq-build.html)
  * [Passing Functions to Components](https://legacy.reactjs.org/docs/faq-functions.html)
  * [Component State](https://legacy.reactjs.org/docs/faq-state.html)
  * [Styling and CSS](https://legacy.reactjs.org/docs/faq-styling.html)
  * [File Structure](https://legacy.reactjs.org/docs/faq-structure.html)
  * [Versioning Policy](https://legacy.reactjs.org/docs/faq-versioning.html)
  * [Virtual DOM and Internals](https://legacy.reactjs.org/docs/faq-internals.html)


  * Next article
[Testing Recipes](https://legacy.reactjs.org/docs/testing-recipes.html)


Docs
[Installation](https://legacy.reactjs.org/docs/getting-started.html)[Main Concepts](https://legacy.reactjs.org/docs/hello-world.html)[Advanced Guides](https://legacy.reactjs.org/docs/accessibility.html)[API Reference](https://legacy.reactjs.org/docs/react-api.html)[Hooks](https://legacy.reactjs.org/docs/hooks-intro.html)[Testing](https://legacy.reactjs.org/docs/testing.html)[Contributing](https://legacy.reactjs.org/docs/how-to-contribute.html)[FAQ](https://legacy.reactjs.org/docs/faq-ajax.html)
Channels
[GitHub](https://github.com/facebook/react)[Stack Overflow](https://stackoverflow.com/questions/tagged/reactjs)[Discussion Forums](https://reactjs.org/community/support.html#popular-discussion-forums)[Reactiflux Chat](https://discord.gg/reactiflux)[DEV Community](https://dev.to/t/react)[Facebook](https://www.facebook.com/react)[Twitter](https://twitter.com/reactjs)
Community
[Code of Conduct](https://github.com/facebook/react/blob/main/CODE_OF_CONDUCT.md)[Community Resources](https://legacy.reactjs.org/community/support.html)
More
[Tutorial](https://legacy.reactjs.org/tutorial/tutorial.html)[Blog](https://legacy.reactjs.org/blog)[Acknowledgements](https://legacy.reactjs.org/acknowledgements.html)[React Native](https://reactnative.dev/)[Privacy](https://opensource.facebook.com/legal/privacy)[Terms](https://opensource.facebook.com/legal/terms)
[![Facebook Open Source](https://legacy.reactjs.org/docs/testing.html)](https://opensource.facebook.com/projects/)
Copyright © 2026 Meta Platforms, Inc.


## Source: https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/

[Skip to main content](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/#main-content)
[](https://www.satellytes.com/)
[Services](https://www.satellytes.com/services/) [About Us](https://www.satellytes.com/about-us/) [Career](https://www.satellytes.com/career/) [Blog](https://www.satellytes.com/blog/) [Contact](https://www.satellytes.com/contact/)
  * [English](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/)
  * [Deutsch](https://www.satellytes.com/de/)


[Services](https://www.satellytes.com/services/) [About Us](https://www.satellytes.com/about-us/) [Career](https://www.satellytes.com/career/) [Blog](https://www.satellytes.com/blog/) [Contact](https://www.satellytes.com/contact/)
Language
[English](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/)[Deutsch](https://www.satellytes.com/de/)
![Hands-On: Writing good commit messages and enforcing valid Pull Request titles on GitHub](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/images/hero_hu_6abe4512efdb5a62.webp)
[Satellytes](https://www.satellytes.com/) › [Blog](https://www.satellytes.com/blog) › Hands-On: Writing good commit messages and enforcing valid Pull Request titles on GitHub
# Hands-On: Writing good commit messages and enforcing valid Pull Request titles on GitHub
21. December 2023 · 10min read · Markus Edenhauser
We all have seen it. Whether you look at older commits in your projects or come to a new repository, you are likely to come across commits which are named like _fix issue_ , _refactor styling, fix wrong query_ and have no clue what these were about, or which component or part of the application those commits have affected.
This is something you want to avoid facing when looking at a repository.
By following our guidelines and implementing the suggested setup, you can ensure consistency and clarity in your PR titles and commit messages, making it easier for reviewers and collaborators to understand the changes.
# TLDR; What you can expect from reading on
  * a guide to write better commit messages (and Pull Request titles)
  * an example of how to implement automated linting based on commitlint
  * a GitHub action that helps you to run commitlint against pull request titles to enforce proper PR titles. This is required only if you squash PRs, where the feature branch commit history gets squashed into the main branch with one single commit.
  * a ready-to-go repository with commitlint and the GitHub action


You’ll find all the scripts from below in our related blog repository: [github.com/satellytes/blog-jenkins-github-pr-comments](https://github.com/satellytes/blog-jenkins-github-pr-comments)
## Writing good commit messages
A good commit message and PR title style are essential if you plan to maintain a project in the longer term, especially if more than one person is working on it. While it may not be crucial to have the commit messages in your branch written in the conventional style since they will be squashed anyway, it is extremely important to have the same conventional style in the pull request title.
### Commit Message Styling
We are a fan of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/#summary), the de facto standard for writing sensible commit messages. Examples of proper commit messages are:

```
feat(api): add slack notifications to processing cron jobs
fix(dashboard): remove duplicate list api calls
refactor(metrics): support multiple query ids for stats
docs(dashboard): explain how metrics are calculated
chore(workspace): add generated files to .gitignore

```

output similar to command: git log –oneline | head -n 5
The most used types are `feat`, `fix`, `refactor`, `docs`, `test`, `chore` representing the intention of the commit. In the brackets, we put the scope (e.g. component or area of effect). After the colon follows the description of the change.
If you want to know more, check out the [conventional commits summary](https://www.conventionalcommits.org/en/v1.0.0/#summary). There are also options for marking breaking changes and adding additional info to a commit.
To show the last commits in the terminal, similar to the output above, type `git log --oneline | head -n 10` where 10 is the amount of commits to show.
### Commit Message Best Practices
Next to proper _type_ and _scope_ , it is all about the description (the part after the colon (`:`). Our recommendations:
  * **Clarity is Key:** Craft concise, explicit commit messages. Avoid vagueness like “Fixed a bug” Offer specific details highlighting the change’s purpose or impact.
  * **Context Matters:** Embed relevant details - issue numbers, discussions - in your commit messages. It clarifies the intent behind the changes, fostering collaboration.
  * **Bug Fixes & References:** Addressing a Bug? Reference it in your message, briefly outlining the problem and your solution. You might also want to link the issue in the Pull Request like _Fixes #123_ or _Resolves #123_
  * **Logical Commits:** For larger tasks or multiple fixes, break them into logical commits. Each should stand alone, simplifying review, reversion, or cherry-picking.
  * **Use Imperatives:** Frame messages in the imperative mood - “Add,” “Fix,” “Update.” This guides the commit’s purpose, enhancing actionability.
  * **Summarize Succinctly:** Open with a 50-90-character summary to encapsulate the commit’s core. It’s what surfaces in commit logs - make it meaningful.
  * **Message Updates:** When revising a commit message, use Git’s `--amend` option. Avoid cluttering history with multiple messages; keep commits self-contained.


All these patterns also apply to Pull Request titles, since they will show up as merge commits if you merge your PRs using the [_squash merge_](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests) option, which is the preferred way to not clutter the main commit history.
## Enforcing correct commit style
Since we know now how to write proper commit messages, let’s implement automation mechanisms to check them on the user and repository side.
> You find the full example in our GitHub repository [satellytes/blog-conventional-commits-github-action](https://github.com/satellytes/blog-conventional-commits-github-action) so there is no need to copy and paste everything you’ll find below for trying. Feel free to clone or fork the repository, run `npm install` and follow the rest of the article to understand our code better.
### Install and configure the checker
We are using [commitlint](https://commitlint.js.org/#/) to validate our commit messages. It checks a string, which is handed over from a pre-commit hook, against a configured pattern defined by the file `commitlint.config.js` in the root of our project.
You can install the required packages with `npm install --save-dev commitlint @commitlint/config-angular`
We are using the `config-angular` style here, which is a proposal by Google. Despite its name, you do not necessarily need to work with angular, it is just the name of the team at Google which created that commitlint plugin.
An example of a valid `commitlint.config.js`:

```
module.exports = {
  extends: ['@commitlint/config-angular'],
  rules: {
    /* disable the header rule to exclude type & scope from the total length calculations
     we focus on the subject length instead */
    'header-max-length': [0, 'always'],
    /* keep the rule of max 72 for the actual commit message (without type & scope) */
    'subject-max-length': [2, 'always', 72],
    'type-enum': [
      2,
      'always',
      ['chore', 'ci', 'docs', 'feat', 'fix', 'refactor', 'revert', 'test']
    ],
    'scope-enum': [2, 'always', ['workspace', 'common', 'app', 'api', 'library']]
  }
};

```

commitlint.config.js
As you can see, we disable the `header-max-length` as well as `subject-max-length` since we usually [automatically generate](https://github.com/satellytes/blog-conventional-commits-github-action/blob/main/commitlint.config.js#L13) the `scope-enum` from component or library names and thus the max length would easily be reached. If you are curious where the limit 72 comes from, it’s a kind of a random number coming from an older age, but it also makes sense in terms of readability:
> The limit of the line length in 70–80 characters may well have originated from various technical limitations of various equipment. The American teletypewriters could type only 72 CPL, while the British ones even less, 70 CPL. [Source: Wikipedia](https://en.wikipedia.org/wiki/Characters_per_line)
Like mentioned before, we tend to generate the scopes programmatically, e.g. from folder names. Take a look at the `[commitlint.config.js` in our example repository](<https://github.com/satellytes/blog-conventional-commits-github-action/blob/main/commitlint.config.js#L13>) to see how we did it.
Once we have installed the packages and created our configuration, we can give it a try by manually running commitlint against a given string:
❌ Testing a wrong commit message: `echo "some feature" | npx commitlint`
![commitlint error: invalid type and subject](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/images/Bildschirmfoto_2023-12-12_um_15.24.31.png)
❌ A wrong type: `echo "feat(unknown): some feature" | npx commitlint`
![commitlint error: invalid type](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/images/Bildschirmfoto_2023-12-12_um_15.26.56.png)
✅ And a proper commit message: `echo "feat(common): some feature" | npx commitlint`
![commitlint: success](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/images/Bildschirmfoto_2023-12-12_um_15.25.30.png)
Upon success, the lint command remains silent.
### Automatically running the check upon committing
We use [husky](https://typicode.github.io/husky/) to manage our commit-msg (and other) git hooks. It can be automatically set up in your workspace by running `npx husky-init && npm install` (see [husky getting-started docs](https://typicode.github.io/husky/getting-started.html#automatic-recommended) if you use other node package manager flavors like yarn, pnpm, bun).
Let’s add now our commitlint as a commit-msg hook: `npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"’`
You’re all set now. Upon committing, husky will run commitlint, which stops the commit from being saved if an invalid commit message is defined.
As long as no one is committing with `git commit --no-verify` and skips the checks, our git commit history should be in a consistent shape.
## Pull Request/Merge Request title check by using a GitHub Action
> This section is only relevant for repositories where [“squash merge”](https://docs.github.com/de/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github#squashing-your-merge-commits) for Pull Requests is enabled. Squashing keeps the commit history shorter, since each developed branch results in a single commit in the main branch. While a merge commit of PR results in merging all commits of a given branch to be applied on the main branch. Using squash is very common in open source and corporate projects.
Since we have now nice commits on the user side, we still can get bad commit messages into our main branch coming from Pull/Merge Requests.
My colleague Felix Hamann created a [pr-title-linter GitHub action](https://github.com/satellytes/blog-conventional-commits-github-action/tree/main/.github/actions/pr-title-linter) a while ago for this very reason, which can be used either directly from the codebase, or being deployed as an action in your environment.
### The GitHub Action code
`main.ts` ([source](https://github.com/satellytes/blog-conventional-commits-github-action/blob/main/.github/actions/pr-title-linter/src/main.ts)) - the entry point for our action.
It makes use of the `[@actions` toolkit by GitHub](<https://github.com/actions/toolkit>) to implement the action with NodeJS. We get the PR title from the `github.context.payload`, parse options with `core.getIntput`, run the linter with `await lint(title, ..`, then print out the result `core.info` and throw an error with `core.setFailed` when an invalid PR title was present during the action run. Upon success, the lint shows “All good” info and the run succeeds.

```
import * as core from "@actions/core";
import * as github from "@actions/github";
import { lint, formatResult } from "./lint";

(async function run() {
  const title = github.context.payload.pull_request?.title;
  const configFile = core.getInput("commitlintConfigFile");

  core.info(
    `🔎 Checking if the title of this PR "${title}" meets the requirements ...`
  );

  try {
    const lintResult = await lint(title, configFile);
    if (!lintResult.valid) {
      core.setFailed(`\\n ${formatResult(lintResult)}`);
    } else {
      core.info(`✔️ All good`);
    }
  } catch (error) {
    core.setFailed(error as Error);
  }
})();

```

main.ts
`lint.ts` ([source](https://github.com/satellytes/blog-conventional-commits-github-action/blob/main/.github/actions/pr-title-linter/src/lint.ts)) - the `lint` and `formatResult` methods that use commitlint programmatically.

```
import { info, getInput } from "@actions/core";
import commitlintLoad from "@commitlint/load";
import commitlintLint from "@commitlint/lint";
import commitlintFormat from "@commitlint/format";

/**
 * @param {string} message PR title or commit message
 * @param {string} configFile path to commitlint config file
 * @returns raw results from `@commitlint/lint()`
 */
export async function lint(message: string, configFile: string): Promise<any> {
  // eslint-disable-next-line i18n-text/no-en
  info(`Loading commitlint config from "${configFile}"...`);
  const config = await commitlintLoad({}, { file: configFile });

  return commitlintLint(
    message,
    config.rules,
    config.parserPreset
      ? { parserOpts: config.parserPreset.parserOpts as any }
      : {},
  );
}

/**
 *
 * @param {Object} lintResult raw results from `@commitlint/lint()`
 * @returns string with human-readable error message
 */
export function formatResult(lintResult: any): string {
  const options: { helpUrl?: string } = {};
  const helpUrl = getInput("helpUrl", { required: false });
  if (helpUrl) {
    options.helpUrl = helpUrl;
  }

  return commitlintFormat(
    {
      results: [
        {
          warnings: lintResult.warnings,
          errors: lintResult.errors,
          input: lintResult.input,
        },
      ],
    },
    options,
  );
}

```

lint.ts
`.github/workflows/pr-checks.yml` ([source](https://github.com/satellytes/blog-conventional-commits-github-action/blob/main/.github/workflows/pr-checks.yml)) - the GitHub workflow to run the action.
This workflow is tested on [github.com](http://github.com), so you can directly use it in your custom repository. Action runs get triggered on any PR change, including the title update.
We’re using the default `ubuntu-latest` runner and the public `actions/setup-node@v3` to require NodeJS version 18 and install our dependencies.
We then run the main.ts script directly with `ts-node` to skip an extra compilation step, which you can also do locally to verify that the paths to the scripts are correct. Run `npx ts-node .github/actions/pr-title-linter/src/main.ts` to verify.

```
name: PR checks

on:
  pull_request:
    types: [opened, reopened, edited, synchronize]
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.event.number }}
  cancel-in-progress: true

jobs:
  pr-title-lint:
    name: Ensure proper PR title
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install --frozen-lockfile
      - run: npx ts-node .github/actions/pr-title-linter/src/main.ts

```

Once you have applied these code parts, or copied them over from our [blog example repository](https://github.com/satellytes/blog-conventional-commits-github-action/tree/main/.github), you should see that workflow being triggered when creating a Pull Request.
![github action: successful pr title linter run](https://www.satellytes.com/blog/post/writing-and-enforcing-conventional-commit-messages-and-pull-request-titles/images/Bildschirmfoto_2023-12-12_um_15.30.08.png)
## Summary
By following the guidelines and implementing the suggested setup, we have achieved the ability to write better commit messages and enforce valid Pull Request titles. This improves the clarity and consistency of our project’s history, making it easier for reviewers and collaborators to understand the changes.
Having a well-maintained commit history also allows us to leverage tools like the `[release-it` npm package](<https://github.com/release-it/release-it>) to automatically generate changelogs based on our commit messages. This streamlines the release process and ensures that our customers see relevant changes more easily.
Overall, creating a homogenous workspace with clear commit messages and PR titles is crucial for maintaining readability and simplifying the understanding of what has changed on the project in the past.
[](https://www.satellytes.com/blog)
### SATELLYTES
Jahnstraße 21  
83093 Bad Endorf  
Germany
### SERVICES
  * [AI Engineering](https://www.satellytes.com/services#ai-engineering)
  * [Platform Engineering](https://www.satellytes.com/services#platform-engineering)
  * [Technical Leadership](https://www.satellytes.com/services#technical-leadership)


### COMPANY
  * [About Us](https://www.satellytes.com/about-us)
  * [Blog](https://www.satellytes.com/blog)
  * [Contact](https://www.satellytes.com/contact)


[Imprint](https://www.satellytes.com/imprint/) • [Privacy Policy](https://www.satellytes.com/data-privacy/)
© 2026 Satellytes Digital Consulting GmbH. All rights reserved.
## Your Privacy Choices
We use cookies and similar technologies to operate the website error-free and for the purposes described below. By clicking 'Accept all cookies', you consent to the use of all cookies. If you click 'Reject all', you reject all cookies that require consent. Details on individual Cookies can be found in the 'Manage cookie preferences' modal. You also have the option of selecting Cookie categories individually in that modal. You can change or revoke your cookie settings at any time on the data privacy page.
Accept all cookies  Reject all  Manage cookie preferences
[Data Privacy](https://www.satellytes.com/data-privacy/) [Imprint](https://www.satellytes.com/imprint/)
## Manage Your Cookie Preferences
### Cookie Usage
We use cookies and similar technologies to ensure the website functions properly, to store your preferences, and to analyze how visitors interact with the website. By clicking 'Accept all cookies', you consent to the use of all cookies. If you click 'Reject all', you reject all cookies that require consent. By clicking on 'Save Preferences' you only accept the selected Cookies. You can change or revoke your cookie settings at any time on the data privacy page.
#### Necessary Cookies
These cookies are necessary for the website to function properly and cannot be switched off in our systems. They are only used to store your privacy preferences.  
| Name  | Service  | Description  | Expiration  |  
| --- | --- | --- | --- |  
| cc_cookie  | satellytes.com  | Stores the user's cookie consent state for the current domain  | 1 year  |  
#### Social Embeds
YouTube Embeds
YouTube embeds are video content from YouTube that we integrate into our website, allowing you to view the content directly on our site without needing to navigate to YouTube. This process is known as "embedding." You can enable YouTube embeds through this cookie consent solution now or later when you decide to view a YouTube embed on our website.  
  
Google is responsible for the YouTube platform under data protection law. Google uses cookies and similar technologies so that you can view YouTube content on this website. These technologies can only be used by Google after you have activated social embeds. Until then, you will remain invisible to Google.  
  
This service is used on this website.  
  
**Company which processes the data**  
Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, D04E5W5, Ireland. However, personal data may also be processed by Google LLC, 1600 Amphitheater Parkway, Mountain View, CA 94043, USA (data transfer mechanism: EU-US Data Protection Framework certification; EU standard contract).  
  
**Collected data**  
This list represents all (personal) data that is collected by or through the use of this service. To our knowledge, Google processes your IP address and information about which social embed you have activated on our site. Further information on the processing of your personal data by Google can be found in the Google privacy policy at: <https://policies.google.com/privacy?hl=en>.  
  
Read the privacy policy of the data processor: <https://policies.google.com/privacy?hl=en>
### More information
For any queries in relation to our policy on cookies and your choices, please [contact us](https://www.satellytes.com/contact/).
Accept all cookies  Reject all  Save Preferences


## Source: https://graphite.com/blog/pull-request-guidelines

[Skip to content](https://graphite.com/blog/pull-request-guidelines#main-content)[Cursor Cloud Agents are now in Graphite. Create, review, and ship without leaving your PR. Read more](https://graphite.com/blog/cursor-cloud-agents)
[](https://graphite.com/)
  * Features
  * Resources
  * [Customers](https://graphite.com/customers)
  * [Docs](https://graphite.com/docs)
  * [Pricing](https://graphite.com/pricing)
  * [Contact](https://cursor.com/contact-sales?product=graphite)


[Log inG](https://app.graphite.com)
[Sign up](https://app.graphite.com/signup)
Menu
[Blog](https://graphite.com/blog)
[Engineering](https://graphite.com/blog?category=engineering)
# Improving team velocity through better pull request practices
![author](https://graphite.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F85246%2F1701820663-prof-pic-ninad.jpeg&w=3840&q=75)
Ninad Pathak
Feb 21, 2024
  * Setting the stage—DevApp Inc.'s pull request woes
  * Step 1: Write useful pull request descriptions
  * Step 2: Keep pull requests small
  * Step 3: Make code reviews more collaborative
  * Step 4: Break down reviews into checklists
  * Step 5: Adopt a dedicated code review tool
  * Step 6: Define SLAs for pull request turnaround
  * Step 7: Automate testing pre-merge
  * Streamline adoption of PR best practices with Graphite


Open
  1. [Setting the stage—DevApp Inc.'s pull request woes](https://graphite.com/blog/pull-request-guidelines#setting-the-stagedevapp-incs-pull-request-woes)
  2. [Step 1: Write useful pull request descriptions](https://graphite.com/blog/pull-request-guidelines#step-1-write-useful-pull-request-descriptions)
  3. [Step 2: Keep pull requests small](https://graphite.com/blog/pull-request-guidelines#step-2-keep-pull-requests-small)
  4. [Step 3: Make code reviews more collaborative](https://graphite.com/blog/pull-request-guidelines#step-3-make-code-reviews-more-collaborative)
  5. [Step 4: Break down reviews into checklists](https://graphite.com/blog/pull-request-guidelines#step-4-break-down-reviews-into-checklists)
  6. [Step 5: Adopt a dedicated code review tool](https://graphite.com/blog/pull-request-guidelines#step-5-adopt-a-dedicated-code-review-tool)
  7. [Step 6: Define SLAs for pull request turnaround](https://graphite.com/blog/pull-request-guidelines#step-6-define-slas-for-pull-request-turnaround)
  8. [Step 7: Automate testing pre-merge](https://graphite.com/blog/pull-request-guidelines#step-7-automate-testing-pre-merge)
  9. [Streamline adoption of PR best practices with Graphite](https://graphite.com/blog/pull-request-guidelines#streamline-adoption-of-pr-best-practices-with-graphite)


ShareCopy to clipboard
Failed
As software teams strive to deliver value faster, pull requests are a focal point for accelerating development cycles. 
However, managing pull requests effectively is easier said than done. 
Between keeping branches up-to-date, reviewing code, fixing merge conflicts, and testing across environments, it’s no wonder pull requests often lead to bottlenecks.
In this guide, we’ll walk through best practices for creating, reviewing, and merging pull requests to help your team collaborate better and ship code faster. 
We’ll follow an example story of a fictional team at DevApp Inc. to see how implementing pull request guidelines step-by-step can have a meaningful impact on velocity.
## Setting the stage—DevApp Inc.'s pull request woes
Let’s consider a hypothetical company—DevApp Inc.
DevApp is a startup building a platform for selling widgets online. Their engineering team follows agile principles and practices continuous delivery with an Ops culture.
However, as the codebase and team grew over time, their pull request process became inefficient:
  * **Pull requests sat open for days** or weeks before being reviewed.
  * **Reviews were superficial** and missed critical flaws.
  * **Merge conflicts happened** **frequently** , slowing things down.
  * **There was little testing** before merging to master.


As a result, new features and bug fixes took way too long to ship. The constant patching of regressions also ate into precious development time between releases. DevApp’s velocity declined sharply.
The CTO decided enough was enough. They took seven specific steps to help improve the efficiency of their internal workflows. 
_Let’s look at what steps they took and understand how you, too, can improve your team velocity through better pull request practices._
### Step 1: Write useful pull request descriptions
DevApp Inc struggled with vague pull request titles like "Fix issue #12345." This made it difficult for reviewers to prioritize or understand changes.
To fix this, DevApp Inc. decided to standardize the [_Conventional Commits_](https://www.conventionalcommits.org/en/v1.0.0/) specification for all pull requests and commits. They now require all commit messages to follow the structured format:
Terminal
Copy to clipboard
Failed

```

<type>[optional scope]: <description>    
[optional body]  
[optional footer(s)]

```

For example:
Terminal
Copy to clipboard
Failed

```

fix(auth): resolve encoding issue causing sign in failures


Fix UTF-8 encoding of auth token to address sign in issues on iOS.
Users were unable to sign in on iOS causing decreased engagement.
Updated LoginViewController to encode token before sending.


Reviewed-by: Jane  
Refs: #123, #456

```

The commit type (**fix** , **feat** , **docs,** etc.) communicates the intent. This helps teammates understand what was fixed or added from the commit message alone.
DevApp Inc. also required PR descriptions to follow a template with sections as below:
Terminal
Copy to clipboard
Failed

```

## What changed
- Fixed encoding issue in LoginViewController causing auth token to be invalid
- Updated to use UTF-8 encoding before sending token


## Why
- Users were unable to sign in on iOS causing decreased engagement 
- Encoding fixes the issue based on analysis 


## Risks 
- Low risk of regression


## Testing
- Manually tested sign in flow on iOS 13/14


## Checklist
[ ] Code builds clean  
[ ] Added tests 
[ ] CI passes
[ ] Peer reviewed

```

This information helps reviewers understand the context of the code changes at a glance.
> _Keep it simple. You are communicating with a person, not writing code all over again. And writing a long, complex description is just creating more work for the person on the other side. Short, concise and descriptive PRs get reviewer juices flowing, and ultimately move the process more smoothly along. —_[ __Gonzalo Bañuelos, Cloud Engineer and Entrepeneur__](https://www.linkedin.com/in/gbanuel/)
The descriptive summaries helped reviewers better organize and prioritize pull requests. PRs got picked up faster for review as reviewers now knew what was within their domain. 
However, it’s a challenge to ask developers to write large PR descriptions. At Graphite, we faced similar problems during development. We are currently [_experimenting with Graphite AI_](https://graphite.dev/blog/ai-code-review-experiments) to automatically understand what files changed and how those changes impact the project, enabling the auto-generation of descriptions for developers to modify and enrich with nuances.
### Step 2: Keep pull requests small
![](https://graphite.com/blog/pull-request-guidelines)![](https://graphite.com/blog/pull-request-guidelines)
**Next, work towards a “1 PR = 1 feature/fix” rule**. 
No more cramming multiple unrelated changes into one massive PR! Developers should split up changes across multiple small, focused PRs.
**For example, instead of:**
Terminal
Copy to clipboard
Failed

```

Big PR: Apple Pay Integration + Guest checkout fix + Product reviews

```

**They would now open**[ _**stacks of small, atomic PRs**_](https://stacking.dev/)**:**
Terminal
Copy to clipboard
Failed

```

PR 1: Apple Pay integration
PR 2: Allow guest checkout with invalid postal code 
PR 3: Add review summary to product page

```

Small PRs make code reviews drastically easier. Reviewers can thoroughly inspect the changes without getting overwhelmed. Approvals then start happening much faster as a result.
Additionally, since each PR contained isolated changes, there were fewer instances of code conflicts or things breaking unexpectedly in staging.
However, stacking with GitHub is unnecessarily complex, which can deter developers from implementing that workflow. You need a tool that’s built to improve PR velocity. 
**That’s where a tool like a**[ _**Graphite**_](https://graphite.dev/)**comes in.**
![](https://graphite.com/blog/pull-request-guidelines)![](https://graphite.com/blog/pull-request-guidelines)
While GitHub works well as a version control system, it can be challenging to manage when teams scale and need to ship code faster. This is where tools like Graphite come in handy.
Graphite seamlessly integrates with GitHub to help developers [_**create smaller, focused pull requests**_](https://graphite.dev/blog/stacked-prs) more easily:
  * [_**Stacking workflow**_](https://graphite.dev/guides/stacked-diffs): Easily split up tasks across branches with automatic stacking. Group-related branches to ship collectively.
  * [_**PR inbox**_](https://graphite.dev/features/inbox): Like an email inbox for PRs. The advanced custom filters allow developers to organize pull requests in customizable sections based on author, labels, review status, and commits. You can use this to keep context when handling multiple PRs.
  * [_**CLI**_](https://graphite.dev/features/cli): Create, checkout, and view PRs without context switching from the command line.
  * [_**VS Code extension**_](https://graphite.dev/features/vscode): Git GUI tightly coupled with stacking workflow allowing you to stack directly from your IDE.


With Graphite, DevApp Inc.'s developers could break down tasks into independent units of work and ship incrementally. The integrated dev environment also enables context switching between branches and PRs with minimal overhead.
Graphite's smart features enhance GitHub workflows to facilitate the creation of smaller PRs. Developers stayed unblocked with less context switching, helping DevApp Inc. ship code changes faster.
### Step 3: Make code reviews more collaborative
The previous changes accelerated the individual phases of the PR process. But DevApp Inc. also wanted to improve the code review experience itself.
Instead of back and forth between the author and reviewer, code reviews were made more collaborative. This was done by encouraging devs to review each other’s code frequently. 
The fresh perspectives help reveal gaps, prevent blind spots, and produce better solutions—before they even reach the code review stage.
> _It’s easy to fall into a place of being overly harsh with feedback, but a code review is a great place to show some empathy and build rapport. Talk about what was good, what could be better, and don’t be a logic bully as Adam Grant would put it. —_[ __Robert Wood, Operating Partner, Sidekick Security__](https://www.linkedin.com/advice/0/how-do-you-collaborate-coordinate-other-reviewers-developers?trk=cah1&utm_source=share&utm_campaign=copy_contribution_link&utm_medium=member_desktop&contributionUrn=urn%3Ali%3Acomment%3A%28articleSegment%3A%28urn%3Ali%3AlinkedInArticle%3A7042511778617995266%2C7042511781474279424%29%2C7045389842922242048%29&articleSegmentUrn=urn%3Ali%3AarticleSegment%3A%28urn%3Ali%3AlinkedInArticle%3A7042511778617995266%2C7042511781474279424%29&dashContributionUrn=urn%3Ali%3Afsd_comment%3A%287045389842922242048%2CarticleSegment%3A%28urn%3Ali%3AlinkedInArticle%3A7042511778617995266%2C7042511781474279424%29%29)
Reviewers also need a more inquisitive, less judgmental tone when asking questions or seeking clarifications. The motive of a comment must go from critiquing code to suggesting solutions. **For example:**
![](https://graphite.com/blog/pull-request-guidelines)![](https://graphite.com/blog/pull-request-guidelines)
To further improve collaboration, code review tools like [_Graphite_](https://graphite.dev/) offer centralized PR inbox that gives focused visibility into all pending tasks. 
### Step 4: Break down reviews into checklists
Studies show that checklist-driven code reviews increase defect detection rates by [_over 66.7%_](https://link.springer.com/chapter/10.1007/978-3-540-45143-3_9) compared to non-checklist-based methods.
DevApp Inc.’s team analyzed the types of defects that frequently slipped through reviews. These ranged from security flaws and performance issues to not following coding conventions.
**They decided to create review checklists around five key areas:**
  1. **Security** : Validate inputs, prevent injections, enforce HTTPS, etc.
  2. **Correctness** : Handles edge cases properly, no obvious logic bugs.
  3. **Architecture** : Aligns with existing patterns, maintainable code.
  4. **Performance** : No n+1 queries, inefficient loops, repetitive IO ops.
  5. **Style** : Follows naming conventions and code styles.


Reviewers now methodically inspect PRs against each checklist item before approving. This kept reviews consistent regardless of who was reviewing and ensured nothing major slipped through the cracks.
If you need inspiration, here’s a [_code review checklist_](https://gist.github.com/katyhuff/845e06656f18784210190e4f46a4aa95) a reviewer shared on GitHub.
![](https://graphite.com/blog/pull-request-guidelines)![](https://graphite.com/blog/pull-request-guidelines)
The upfront effort in building these checklists can pay off greatly over the long run as your reviews become more intentional and focused, speeding up the time it takes to review PRs and giving authors more actionable feedback. Also, treat the checklist as a living document that should be updated and adjusted to suit your team’s growing needs.
### Step 5: Adopt a dedicated code review tool
While GitHub provides built-in code review features, they remain fairly basic and restrictive for optimizing workflows at scale. GitHub's interface also makes it tedious and challenging to [_filter requests_](https://graphite.dev/docs/customize-pr-inbox) for effective prioritization.
A fast-moving team like the hypothetical DevApp Inc. would start to bottleneck as more developers are added and the number of PRs starts growing exponentially. 
You need something to help you properly organize code review tasks without overwhelming the users. That's why high-performance teams often adopt dedicated code review tools for simplifying pull request management. 
For example, [_Graphite_](https://graphite.dev/) aggregates all pull requests across repositories into unified, customizable views—filterable by the developer, reviewer, status, age, priority attributes, and more, for effective prioritization.
![](https://graphite.com/blog/pull-request-guidelines)![](https://graphite.com/blog/pull-request-guidelines)
At a glance, developers could easily spot workload distribution imbalances—helping them keep the tasks moving while they proactively balance reviews teamwide. Graphite offers visibility not just into volume, but [_key PR metrics_](https://graphite.dev/blog/github-pr-metrics) like first response times and completion rates too.
The built-in routing algorithms recommended reviewers based on expertise fit, availability, and past pull request cycle times. @mention notifications integrated seamlessly with [_Slack_](https://graphite.dev/docs/slack-notifications) and the powerful [_VS Code extension_](https://graphite.dev/features/vscode) enabled quick task switching.
### Step 6: Define SLAs for pull request turnaround
After implementing the above changes, things started moving faster for the DevApp team. But without actual metrics, tracking pull request SLAs, velocity gains depended too much on individual effort levels.
DevApp Inc. decided to track cycle time performance at each stage and define time-bound SLAs:
  * **Time to first review** : Initial feedback given in ≤24 hrs.
  * **Publish to merge time** : PR is merged or closed in ≤5 days.


These were integrated with custom analytics using [_Graphite_](https://graphite.dev/). Their automated monitoring gave real-time visibility into throughput and bottlenecks.
When SLA breaches happened, the team investigated why, for example, a PR waiting days to be picked up? Who dropped the ball? How can we improve here?
Just having the structure for accountability drove more discipline. Moreover, the data gave them confidence they were shipping value reliably and faster.
### Step 7: Automate testing pre-merge
![](https://graphite.com/blog/pull-request-guidelines)![](https://graphite.com/blog/pull-request-guidelines)
Like many development teams scaling quickly, DevApp Inc. struggled with maintaining code quality. With engineers shipping features rapidly, bugs still slipped into production—despite diligent QA and code reviews.
Manual testing had become a bottleneck to DevApp Inc.'s rapid development velocity. To address this common scaling challenge, they started including pre-merge automated testing.
  * Set up CI/CD pipelines to auto-execute tests on every pull request.
  * Included end-to-end integration and performance validation instead of simple unit tests.
  * Security scans automatically checked and verified dependencies.


Now, when engineers open PRs, these pipelines run rigorous quality checks on the changes. If any test failed, reviewers were immediately notified to request adjustments from developers which greatly improved dev velocity.
## Streamline adoption of PR best practices with Graphite
**None of these practices are revolutionary individually.**
But by improving each phase—creating, reviewing, merging PRs—you can compound small gains into an exponentially faster development cycle.
The key insight is recognizing the synergies between process steps—you must work on the bottlenecks while strengthening safeguards simultaneously. This balanced approach allows teams to ship faster without quality compromises.
So, start by analyzing your current PR workflow end-to-end. Look for high-leverage areas to drive efficiency through tools, automation, and better collaboration.
If team adoption is the challenge, try [_Graphite_](https://graphite.dev/). It is purpose-built to help improve workflows by subtly enforcing PR best practices:
  * **Graphite integrates seamlessly with GitHub** so you can start seeing benefits in minutes without disrupting your team's existing workflow.
  * **The smart productivity features help implement** many of the guidelines covered here, like creating smaller PRs, tracking SLAs, automating testing, and more—all with minimal configuration.
  * **Graphite was built by scaling engineering teams** to help them collaborate better. The UI and workflows are designed specifically to streamline PR processes end-to-end.


> _"Graphite makes it much faster for me to develop because I’m spending less time wrangling git" —_[ __Rodda John, Engineer at Ramp__](https://graphite.dev/customer/ramp)
Take the first steps towards significant dev productivity gains. [_Sign up for a free Graphite account_](https://app.graphite.dev/signup) and experience the productivity boost for your team. The effort is well worth the results!
### Related articles
### [Why AI will never replace human code review Mar 17, 2025 Engineering ](https://graphite.com/blog/ai-wont-replace-human-code-review)### [AI code generation will remain fragmented Nov 25, 2024 Engineering ](https://graphite.com/blog/ai-code-generation-will-remain-fragmented)### [Introducing frozen branches: A safer way to build on your teammates’ work Sep 17, 2025 Engineering ](https://graphite.com/blog/introducing-frozen-branches)
## Built for the world’s fastest engineering teams, now available for everyone.
[Request a demo](https://cursor.com/contact-sales?product=graphite)
[Start free trial](https://app.graphite.com/signup)
### Features
  * [CLI](https://graphite.com/features#cli)
  * [Merge queue](https://graphite.com/features#merge-queue)
  * [Insights](https://graphite.com/features#insights)
  * [PR inbox](https://graphite.com/features#inbox)
  * [AI Reviews](https://graphite.com/features/ai-reviews)
  * [AgentsNew](https://graphite.com/features/agents)
  * [Graphite Chat](https://graphite.com/features/chat)


### Company
  * [Blog](https://graphite.com/blog)
  * [Customers](https://graphite.com/customers)
  * [Careers0](https://graphite.com/careers)
  * [Privacy policy](https://graphite.com/privacy)
  * [Terms of service](https://graphite.com/terms-of-service)


### Resources
  * [Docs](https://graphite.com/docs)
  * [Pricing](https://graphite.com/pricing)
  * [Status](https://status.graphite.com)
  * [Guides](https://graphite.com/guides)
  * [Stacking workflow](https://graphite.com/stacking)


### Connect
  * [](https://cursor.com/contact-sales?product=graphite)
  * [Community Slack](https://community.graphite.com)
  * [](https://github.com/withgraphite/)
  * [(Twitter)](https://x.com/graphite/)
  * [](https://www.linkedin.com/company/withgraphite/)
  * [](https://www.youtube.com/@withgraphite)


[Loading](https://status.graphite.com)
© Graphite 2026
![An image of the Graphite logo as a neon sign](https://graphite.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgraphite_logo_neon_sign.fd632602.webp&w=2048&q=75&dpl=dpl_6wDxRcctuQa1HZEM2KcZxwZJFUYd)![Graphite wordmark](https://graphite.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwhite%402x.6327aed5.webp&w=3840&q=75&dpl=dpl_6wDxRcctuQa1HZEM2KcZxwZJFUYd)


## Source: https://www.conventionalcommits.org/en/v1.0.0/

[ ](https://www.conventionalcommits.org/)
  * Versions
    * [v1.0.0](https://www.conventionalcommits.org/en/v1.0.0)
    * [v1.0.0-beta.4](https://www.conventionalcommits.org/en/v1.0.0-beta.4)
    * [v1.0.0-beta.3](https://www.conventionalcommits.org/en/v1.0.0-beta.3)
    * [v1.0.0-beta.2](https://www.conventionalcommits.org/en/v1.0.0-beta.2)
    * [v1.0.0-beta.1](https://www.conventionalcommits.org/en/v1.0.0-beta.1)
    * [v1.0.0-beta](https://www.conventionalcommits.org/en/v1.0.0-beta)
  * Languages
    * [English](https://www.conventionalcommits.org/en/)
    * [Italian](https://www.conventionalcommits.org/it/)
    * [Polish](https://www.conventionalcommits.org/pl/)
    * [简体中文](https://www.conventionalcommits.org/zh-hans/)
    * [繁體中文](https://www.conventionalcommits.org/zh-hant/)
    * [Spanish](https://www.conventionalcommits.org/es/)
    * [Русский](https://www.conventionalcommits.org/ru/)
    * [日本語](https://www.conventionalcommits.org/ja/)
    * [Français](https://www.conventionalcommits.org/fr/)
    * [한국어](https://www.conventionalcommits.org/ko/)
    * [हिन्दी](https://www.conventionalcommits.org/hi/)
    * [Português Brasileiro](https://www.conventionalcommits.org/pt-br/)
    * [Indonesia](https://www.conventionalcommits.org/id/)
    * [Հայերեն](https://www.conventionalcommits.org/hy/)
    * [Deutsch](https://www.conventionalcommits.org/de/)
    * [ไทย](https://www.conventionalcommits.org/th/)
    * [Ukrainian - Українська](https://www.conventionalcommits.org/uk/)
    * [Belarusian - Беларуская](https://www.conventionalcommits.org/be/)
    * [Türkçe](https://www.conventionalcommits.org/tr/)
    * [Nederlands](https://www.conventionalcommits.org/nl/)
    * [Tamil - தமிழ்](https://www.conventionalcommits.org/ta/)
    * [Malayalam - മലയാളം](https://www.conventionalcommits.org/ml/)
    * [Romanian](https://www.conventionalcommits.org/ro/)
    * [বাংলা (Bengali)](https://www.conventionalcommits.org/bn/)
    * [Uzbek (O'zbekcha)](https://www.conventionalcommits.org/uz/)
    * [العربية](https://www.conventionalcommits.org/ar/)
    * [فارسی](https://www.conventionalcommits.org/pr/)
    * [Ελληνικά](https://www.conventionalcommits.org/gr/)
    * [Serbian - Srpski](https://www.conventionalcommits.org/sr/)
    * [Sinhala](https://www.conventionalcommits.org/si/)
  * [About](https://www.conventionalcommits.org/en/about)


# Conventional Commits
A specification for adding human and machine readable meaning to commit messages
[Quick Summary](https://www.conventionalcommits.org/en/v1.0.0/#summary) [Full Specification](https://www.conventionalcommits.org/en/v1.0.0/#specification) [Contribute](https://github.com/conventional-commits/conventionalcommits.org)
![](https://www.conventionalcommits.org/img/git-flow--welcome.png)
# Conventional Commits 1.0.0
##  [](https://www.conventionalcommits.org/en/v1.0.0/#summary)Summary
The Conventional Commits specification is a lightweight convention on top of commit messages. It provides an easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. This convention dovetails with [SemVer](http://semver.org), by describing the features, fixes, and breaking changes made in commit messages.
The commit message should be structured as follows:
* * *

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

```

* * *
The commit contains the following structural elements, to communicate intent to the consumers of your library:
  1. **fix:** a commit of the _type_ `fix` patches a bug in your codebase (this correlates with [`PATCH`](http://semver.org/#summary) in Semantic Versioning).
  2. **feat:** a commit of the _type_ `feat` introduces a new feature to the codebase (this correlates with [`MINOR`](http://semver.org/#summary) in Semantic Versioning).
  3. **BREAKING CHANGE:** a commit that has a footer `BREAKING CHANGE:`, or appends a `!` after the type/scope, introduces a breaking API change (correlating with [`MAJOR`](http://semver.org/#summary) in Semantic Versioning). A BREAKING CHANGE can be part of commits of any _type_.
  4. _types_ other than `fix:` and `feat:` are allowed, for example [@commitlint/config-conventional](https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional) (based on the [Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)) recommends `build:`, `chore:`, `ci:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:`, and others.
  5. _footers_ other than `BREAKING CHANGE: <description>` may be provided and follow a convention similar to [git trailer format](https://git-scm.com/docs/git-interpret-trailers).


Additional types are not mandated by the Conventional Commits specification, and have no implicit effect in Semantic Versioning (unless they include a BREAKING CHANGE).  A scope may be provided to a commit’s type, to provide additional contextual information and is contained within parenthesis, e.g., `feat(parser): add ability to parse arrays`.
##  [](https://www.conventionalcommits.org/en/v1.0.0/#examples)Examples
###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with-description-and-breaking-change-footer)Commit message with description and breaking change footer

```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files

```

###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with--to-draw-attention-to-breaking-change)Commit message with `!` to draw attention to breaking change

```
feat!: send an email to the customer when a product is shipped

```

###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with-scope-and--to-draw-attention-to-breaking-change)Commit message with scope and `!` to draw attention to breaking change

```
feat(api)!: send an email to the customer when a product is shipped

```

###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with-both--and-breaking-change-footer)Commit message with both `!` and BREAKING CHANGE footer

```
feat!: drop support for Node 6

BREAKING CHANGE: use JavaScript features not available in Node 6.

```

###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with-no-body)Commit message with no body

```
docs: correct spelling of CHANGELOG

```

###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with-scope)Commit message with scope

```
feat(lang): add Polish language

```

###  [](https://www.conventionalcommits.org/en/v1.0.0/#commit-message-with-multi-paragraph-body-and-multiple-footers)Commit message with multi-paragraph body and multiple footers

```
fix: prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z
Refs: #123

```

##  [](https://www.conventionalcommits.org/en/v1.0.0/#specification)Specification
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).
  1. Commits MUST be prefixed with a type, which consists of a noun, `feat`, `fix`, etc., followed by the OPTIONAL scope, OPTIONAL `!`, and REQUIRED terminal colon and space.
  2. The type `feat` MUST be used when a commit adds a new feature to your application or library.
  3. The type `fix` MUST be used when a commit represents a bug fix for your application.
  4. A scope MAY be provided after a type. A scope MUST consist of a noun describing a section of the codebase surrounded by parenthesis, e.g., `fix(parser):`
  5. A description MUST immediately follow the colon and space after the type/scope prefix. The description is a short summary of the code changes, e.g., _fix: array parsing issue when multiple spaces were contained in string_.
  6. A longer commit body MAY be provided after the short description, providing additional contextual information about the code changes. The body MUST begin one blank line after the description.
  7. A commit body is free-form and MAY consist of any number of newline separated paragraphs.
  8. One or more footers MAY be provided one blank line after the body. Each footer MUST consist of a word token, followed by either a `:<space>` or `<space>#` separator, followed by a string value (this is inspired by the [git trailer convention](https://git-scm.com/docs/git-interpret-trailers)).
  9. A footer’s token MUST use `-` in place of whitespace characters, e.g., `Acked-by` (this helps differentiate the footer section from a multi-paragraph body). An exception is made for `BREAKING CHANGE`, which MAY also be used as a token.
  10. A footer’s value MAY contain spaces and newlines, and parsing MUST terminate when the next valid footer token/separator pair is observed.
  11. Breaking changes MUST be indicated in the type/scope prefix of a commit, or as an entry in the footer.
  12. If included as a footer, a breaking change MUST consist of the uppercase text BREAKING CHANGE, followed by a colon, space, and description, e.g., _BREAKING CHANGE: environment variables now take precedence over config files_.
  13. If included in the type/scope prefix, breaking changes MUST be indicated by a `!` immediately before the `:`. If `!` is used, `BREAKING CHANGE:` MAY be omitted from the footer section, and the commit description SHALL be used to describe the breaking change.
  14. Types other than `feat` and `fix` MAY be used in your commit messages, e.g., _docs: update ref docs._
  15. The units of information that make up Conventional Commits MUST NOT be treated as case-sensitive by implementors, with the exception of BREAKING CHANGE which MUST be uppercase.
  16. BREAKING-CHANGE MUST be synonymous with BREAKING CHANGE, when used as a token in a footer.


##  [](https://www.conventionalcommits.org/en/v1.0.0/#why-use-conventional-commits)Why Use Conventional Commits
  * Automatically generating CHANGELOGs.
  * Automatically determining a semantic version bump (based on the types of commits landed).
  * Communicating the nature of changes to teammates, the public, and other stakeholders.
  * Triggering build and publish processes.
  * Making it easier for people to contribute to your projects, by allowing them to explore a more structured commit history.


##  [](https://www.conventionalcommits.org/en/v1.0.0/#faq)FAQ
###  [](https://www.conventionalcommits.org/en/v1.0.0/#how-should-i-deal-with-commit-messages-in-the-initial-development-phase)How should I deal with commit messages in the initial development phase?
We recommend that you proceed as if you’ve already released the product. Typically _somebody_ , even if it’s your fellow software developers, is using your software. They’ll want to know what’s fixed, what breaks etc.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#are-the-types-in-the-commit-title-uppercase-or-lowercase)Are the types in the commit title uppercase or lowercase?
Any casing may be used, but it’s best to be consistent.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#what-do-i-do-if-the-commit-conforms-to-more-than-one-of-the-commit-types)What do I do if the commit conforms to more than one of the commit types?
Go back and make multiple commits whenever possible. Part of the benefit of Conventional Commits is its ability to drive us to make more organized commits and PRs.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#doesnt-this-discourage-rapid-development-and-fast-iteration)Doesn’t this discourage rapid development and fast iteration?
It discourages moving fast in a disorganized way. It helps you be able to move fast long term across multiple projects with varied contributors.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#might-conventional-commits-lead-developers-to-limit-the-type-of-commits-they-make-because-theyll-be-thinking-in-the-types-provided)Might Conventional Commits lead developers to limit the type of commits they make because they’ll be thinking in the types provided?
Conventional Commits encourages us to make more of certain types of commits such as fixes. Other than that, the flexibility of Conventional Commits allows your team to come up with their own types and change those types over time.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#how-does-this-relate-to-semver)How does this relate to SemVer?
`fix` type commits should be translated to `PATCH` releases. `feat` type commits should be translated to `MINOR` releases. Commits with `BREAKING CHANGE` in the commits, regardless of type, should be translated to `MAJOR` releases.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#how-should-i-version-my-extensions-to-the-conventional-commits-specification-eg-jameswomackconventional-commit-spec)How should I version my extensions to the Conventional Commits Specification, e.g. `@jameswomack/conventional-commit-spec`?
We recommend using SemVer to release your own extensions to this specification (and encourage you to make these extensions!)
###  [](https://www.conventionalcommits.org/en/v1.0.0/#what-do-i-do-if-i-accidentally-use-the-wrong-commit-type)What do I do if I accidentally use the wrong commit type?
####  [](https://www.conventionalcommits.org/en/v1.0.0/#when-you-used-a-type-thats-of-the-spec-but-not-the-correct-type-eg-fix-instead-of-feat)When you used a type that’s of the spec but not the correct type, e.g. `fix` instead of `feat`
Prior to merging or releasing the mistake, we recommend using `git rebase -i` to edit the commit history. After release, the cleanup will be different according to what tools and processes you use.
####  [](https://www.conventionalcommits.org/en/v1.0.0/#when-you-used-a-type-not-of-the-spec-eg-feet-instead-of-feat)When you used a type _not_ of the spec, e.g. `feet` instead of `feat`
In a worst case scenario, it’s not the end of the world if a commit lands that does not meet the Conventional Commits specification. It simply means that commit will be missed by tools that are based on the spec.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#do-all-my-contributors-need-to-use-the-conventional-commits-specification)Do all my contributors need to use the Conventional Commits specification?
No! If you use a squash based workflow on Git lead maintainers can clean up the commit messages as they’re merged—adding no workload to casual committers. A common workflow for this is to have your git system automatically squash commits from a pull request and present a form for the lead maintainer to enter the proper git commit message for the merge.
###  [](https://www.conventionalcommits.org/en/v1.0.0/#how-does-conventional-commits-handle-revert-commits)How does Conventional Commits handle revert commits?
Reverting code can be complicated: are you reverting multiple commits? if you revert a feature, should the next release instead be a patch?
Conventional Commits does not make an explicit effort to define revert behavior. Instead we leave it to tooling authors to use the flexibility of _types_ and _footers_ to develop their logic for handling reverts.
One recommendation is to use the `revert` type, and a footer that references the commit SHAs that are being reverted:

```
revert: let us never again speak of the noodle incident

Refs: 676104e, a215868

```

License
[Creative Commons - CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
[ ![](https://www.netlify.com/img/global/badges/netlify-light.svg) ](https://www.netlify.com)
[](https://github.com/conventional-commits/conventionalcommits.org)


## Source: https://www.deployhq.com/blog/the-perfect-pull-request-best-practices-for-collaborative-development

[Skip to main content](https://www.deployhq.com/blog/the-perfect-pull-request-best-practices-for-collaborative-development#main-content) [Skip to navigation](https://www.deployhq.com/blog/the-perfect-pull-request-best-practices-for-collaborative-development#main-navigation)
Ready to streamline your deployments? **Start deploying with confidence today.**
[Get Started](https://www.deployhq.com/signup?cta=Blog+Sticky+Banner)
### Header
Primary Navigation [![DeployHQ](https://www.deployhq.com/assets/logos/deployhq-logo-dark-5d651de1840ee1ca1ebd14015d57f72b07185615e919747b65852154aeec77d8.svg) ![DeployHQ](https://www.deployhq.com/assets/logos/deployhq-logo-9586cdf9994a2286049465b3f9fa9df456051a862066c61031f2a1ed72518f4f.svg) ](https://www.deployhq.com/)
  * [Features](https://www.deployhq.com/features)
DEPLOYMENTS
    * [ Zero Downtime Deployments Deploy without interruption ](https://www.deployhq.com/features/zero-downtime-deployments)
    * [ Turbo Deployments Lightning fast deploys ](https://www.deployhq.com/features/turbo-deployments)
    * [ Docker Builds Container-based builds ](https://www.deployhq.com/features/docker-builds)
    * [ Automatic Deployment Deploy on every push ](https://www.deployhq.com/features/automatic-deployments)
    * [ Deploy Behind Firewalls Secure private deployments ](https://www.deployhq.com/features/deploy-behind-firewalls)
FEATURES
    * [ One-Click Rollback Instant rollback capability ](https://www.deployhq.com/features/one-click-rollback)
    * [ Build Pipelines Custom build workflows ](https://www.deployhq.com/features/build-pipelines)
    * [ Deployment Targets Multi-environment deploys ](https://www.deployhq.com/features/deployment-targets)
    * [ Deployment Templates Reusable configurations ](https://www.deployhq.com/features/deployment-templates)
    * [ Deployment Zones Geographic distribution ](https://www.deployhq.com/features/deployment-zones)
INTEGRATIONS
    * [ Deploy from GitHub GitHub integration ](https://www.deployhq.com/deploy-from-github)
    * [ Deploy from GitLab GitLab integration ](https://www.deployhq.com/deploy-from-gitlab)
    * [ Deploy from Bitbucket Bitbucket integration ](https://www.deployhq.com/deploy-from-bitbucket)
    * [ Deploy to VPS Any virtual private server ](https://www.deployhq.com/vps)
    * [ Deploy WordPress WordPress deployments ](https://www.deployhq.com/wordpress)
    * [ Deploy to Shopify Shopify deployments ](https://www.deployhq.com/shopify)
    * [ Static Sites & S3 Deploy to cloud storage ](https://www.deployhq.com/features/static-hosting)
    * [ Game Servers Deploy to game servers ](https://www.deployhq.com/deploy-to-game-servers)
DEVELOPER TOOLS
    * [ REST API Full API access ](https://www.deployhq.com/features/api)
    * [ DeployHQ AI AI-powered assistance ](https://www.deployhq.com/features/ai)
    * [ MCP Server Model Context Protocol ](https://www.deployhq.com/features/deployhq-mcp)
    * [ PR Radar Pull request dashboard ](https://www.deployhq.com/features/pr-radar)
    * [ CLI & Agents Deploy from the terminal ](https://www.deployhq.com/agents)
    * [ AI PageSpeed Performance insights ](https://pagespeed.deployhq.com/)
    * [ Powerful Integrations Connect your tools ](https://www.deployhq.com/features/integrations)
  * [Pricing](https://www.deployhq.com/pricing)
  * [Testimonials](https://www.deployhq.com/customers)
  * [Blog](https://www.deployhq.com/blog)
  * [Help](https://www.deployhq.com/support)
    * [ Ask AI Instant AI-powered answers ](https://www.deployhq.com/support#ask-ai)
    * [ Support Centre Browse help articles ](https://www.deployhq.com/support)
    * [ Learn Git Git tutorials & guides ](https://www.deployhq.com/git)
    * [ Deployment Guides Step-by-step instructions ](https://www.deployhq.com/guides)
    * [ Cheatsheets Quick-reference docs ](https://www.deployhq.com/cheatsheets)
    * [ Changelog & Updates Latest product updates ](https://changelog.deployhq.com/changelog)
    * [ Service Status System health & uptime ](https://status.deployhq.com/)
    * [ Contact Us Get in touch with us ](https://www.deployhq.com/contact)
  * ![Light mode](https://www.deployhq.com/assets/icons/sun-f944214d7a8b0785968beca13813c987e13e2b1dfd8232797600382587d3fb0c.svg) ![Dark mode](https://www.deployhq.com/assets/icons/moon-88e44224484d4887c8cbb27f7fd645227467e038a23f93721b84ff98168ea53e.svg)
  * [Login](https://identity.deployhq.com/login/deploy)
  * [Start deploying free →](https://www.deployhq.com/signup?cta=Start+deploying+free+%E2%86%92)

Toggle Menu Close Menu
# Pull Request Best Practices: A Complete Guide (2026)
By Facundo F · Updated on 12th April 2026
[Git](https://www.deployhq.com/blog/category/git), [Tips & Tricks](https://www.deployhq.com/blog/category/tips), [Tutorials](https://www.deployhq.com/blog/category/tutorials), and [What Is](https://www.deployhq.com/blog/category/what-is)
![Pull Request Best Practices: A Complete Guide \(2026\)](https://blog.deployhq.com/attachment/592e1af7-3a59-42fb-ad43-f85aa974f903/thumb1400.jpg)
Pull requests sit at the intersection of code quality, team communication, and deployment safety. A well-crafted PR does more than move code from one branch to another — it creates a reviewable record of intent, provides a checkpoint for automated testing, and (when connected to a deployment pipeline like [DeployHQ](https://www.deployhq.com/signup)) triggers the exact sequence of steps that puts your changes into production. Yet most teams treat PRs as a formality rather than a craft.
**Updated for 2026:** This guide now covers AI-assisted code review tools (GitHub Copilot, CodeRabbit), modern merge queue strategies, and the stacked PR workflows that high-velocity teams use to ship without sacrificing review quality.
This guide covers what separates effective pull requests from the ones that sit open for days, accumulate dozens of comments, and still ship bugs.
## Pull Request vs Merge Request: What's the Difference?
If you use GitLab instead of GitHub, you know these as **merge requests** (MRs) rather than pull requests. The concept is identical — a proposal to merge one branch into another, with a diff, a description, and a review workflow. The naming difference is purely historical:
  * **GitHub** calls them **pull requests** because the original Git operation was `git request-pull`, asking a maintainer to _pull_ your changes into their repository. 
  * **GitLab** calls them **merge requests** because the end result is a _merge_ into the target branch, which arguably describes the intent more clearly. 
  * **Bitbucket** uses **pull requests** , same as GitHub. 

  
| Feature  | GitHub (PR)  | GitLab (MR)  |  
| --- | --- | --- |  
| Draft/WIP support  | Draft PRs  | Draft MRs (formerly WIP prefix)  |  
| Approvals  | Required reviewers  | Approval rules with optional code owners  |  
| Merge strategies  | Merge, squash, rebase  | Merge, squash, fast-forward, semi-linear  |  
| CI integration  | GitHub Actions, status checks  | GitLab CI/CD, pipelines  |  
| Auto-merge  | Merge queue  | Auto-merge when pipeline succeeds  |  
Everything in this guide applies equally to both. Where platform-specific features differ (like merge strategies or CI configuration), the underlying principles — small diffs, clear descriptions, thorough reviews — remain the same. [DeployHQ](https://www.deployhq.com) supports [deploying from GitHub](https://www.deployhq.com/deploy-from-github), [GitLab](https://www.deployhq.com/deploy-from-gitlab), and Bitbucket, so the deploy-on-merge pattern works regardless of which platform your team uses.
## Anatomy of a Great Pull Request
Every pull request has four components that determine how quickly and thoroughly it gets reviewed:
  * **Title** — a single line that tells the reviewer what changed and why 
  * **Description** — context, motivation, testing notes, and deployment considerations 
  * **Diff** — the actual code changes, ideally small and focused 
  * **Metadata** — labels, reviewers, linked issues, and CI status 


The title and description are where most PRs fail. A title like "Fix bug" or "Update code" forces the reviewer to read every line of the diff before they understand what they're looking at. Compare that with "Fix race condition in session cleanup that caused 502s under load" — the reviewer immediately knows the problem, the component, and the impact.
## PR Size: The Single Biggest Factor in Review Quality
Research from SmartBear's study of Cisco's code review practices found that review effectiveness drops sharply after 200-400 lines of change. Reviewers examining more than 400 lines found significantly fewer defects per line — not because the code was better, but because cognitive fatigue sets in and reviewers start skimming.
Google's internal engineering data tells a similar story. Their research shows that the median time-to-review doubles for every additional 100 lines changed, and PRs over 500 lines have a much higher rate of post-merge defects.
**Practical guidelines for PR size:**  
| Lines Changed  | Review Quality  | Typical Review Time  |  
| --- | --- | --- |  
| 1–100  | High — reviewers catch most issues  | 15–30 minutes  |  
| 100–300  | Good — focused attention still possible  | 30–60 minutes  |  
| 300–500  | Declining — fatigue reduces thoroughness  | 1–3 hours  |  
| 500+  | Poor — reviewers skim, bugs slip through  | Days (often delayed)  |  
If your PR crosses the 400-line mark, ask yourself whether it can be split. A database migration, a new service layer, and the API endpoint that ties them together are three separate PRs — not one.
### Stacked PRs for Large Features
When a feature genuinely requires thousands of lines, use stacked PRs (also called chained PRs or PR chains). Each PR builds on the previous one:
  1. **PR 1** : Database schema changes and migrations 
  2. **PR 2** : Service layer and business logic (targets PR 1's branch) 
  3. **PR 3** : API endpoints (targets PR 2's branch) 
  4. **PR 4** : Frontend integration (targets PR 3's branch) 


Each PR stays reviewable. Each can be tested and deployed independently through a staging pipeline.
#### How to Structure a Stacked PR Workflow
The key to stacked PRs is that each branch targets the _previous_ branch, not `main`. When PR 1 merges into `main`, PR 2 automatically retargets to `main` (GitHub does this natively). Here is a concrete workflow:

```
# Create the first branch off main
git checkout -b feat/user-auth-schema main
# ... make schema changes, push, open PR 1 targeting main

# Create the second branch off the first
git checkout -b feat/user-auth-service feat/user-auth-schema
# ... implement service layer, push, open PR 2 targeting feat/user-auth-schema

# Create the third branch off the second
git checkout -b feat/user-auth-api feat/user-auth-service
# ... add API endpoints, push, open PR 3 targeting feat/user-auth-service

```

When the base PR receives changes during review, rebase the dependent branches:

```
git checkout feat/user-auth-service
git rebase feat/user-auth-schema
git push --force-with-lease

```

#### Tools for Managing Stacked PRs
Manually rebasing stacked branches gets tedious fast. These tools automate the rebasing and retargeting:
  * **[Graphite](https://graphite.dev)** — purpose-built for stacked PRs on GitHub. Automatically rebases the entire stack when any PR is updated, provides a CLI (`gt`) for creating and navigating stacks, and adds a dashboard showing stack status. 
  * **[ghstack](https://github.com/ezyang/ghstack)** — Meta's open-source tool for creating stacked diffs on GitHub. Each commit becomes a separate PR, similar to the Phabricator workflow. 
  * **GitHub merge queue** — while not a stacking tool per se, merge queues ensure that stacked PRs merge in order and that CI passes against the actual merge result, preventing integration failures. 
  * **`git-branchless`**— provides a`git restack` command that automatically rebases all dependent branches when a base branch changes. 


For teams shipping 10+ PRs per day, stacked PRs are not a nice-to-have — they are how you maintain review quality at high velocity without blocking developers on sequential reviews.
## PR Description Best Practices
A PR description should answer three questions the reviewer will have before they look at a single line of code:
  1. **What changed?** — a summary of the modification 
  2. **Why?** — the business reason, bug report, or technical motivation 
  3. **How should I review this?** — where to start, what to focus on, what's intentionally left out 


The description is not a commit log. Do not just paste your commit messages — synthesize them into a narrative. A reviewer reading the description should understand the change well enough to predict what the diff will look like before they open it.
**Good descriptions include:**
  * A link to the issue or ticket that motivated the change 
  * The root cause (for bug fixes), not just the symptom 
  * Screenshots or recordings for UI changes 
  * A "How to Review" section that guides the reviewer through the diff in a logical order 
  * Deployment notes — environment variables, migrations, feature flags 


**Bad descriptions include:**
  * "See ticket" (forces the reviewer to context-switch to another tool) 
  * A copy-paste of the commit log 
  * Nothing at all 


Here is a practical template:

```
## What

Brief summary of the changes (2-3 sentences max).

## Why

Link to the issue, bug report, or product requirement.
Explain the root cause if this is a fix.

## How to Review

- Start with `src/auth/session.ts` — this is the core change
- The test file mirrors the production scenarios from the incident
- Ignore whitespace changes in `config/` — automated formatter ran

## Testing

- [ ] Unit tests pass locally
- [ ] Tested manually against staging
- [ ] Verified rollback path works

## Deployment Notes

- Requires ENV var `SESSION_TIMEOUT_MS` to be set
- Database migration runs automatically
- Safe to deploy during business hours — no downtime expected

```

The "Deployment Notes" section matters more than most teams realise. When your PRs feed directly into a deployment tool — for instance, [DeployHQ's automatic deployments](https://www.deployhq.com/features/automatic-deployments) that trigger on merge — the reviewer needs to know whether the change requires environment variables, database migrations, or a specific deployment order.
## Commit Message Conventions
Individual commits within a PR tell the story of how you built the change. The [Conventional Commits](https://www.conventionalcommits.org/) specification provides a structured format that tools can parse — and it pairs well with a [standardized approach to commit messages](https://deployhq.com/blog/conventional-commits-a-standardized-approach-to-commit-messages) that keeps your Git history clean:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]

```

Common types:  
| Type  | When to Use  |  
| --- | --- |  
| `feat`  | New feature or capability  |  
| `fix`  | Bug fix  |  
| `refactor`  | Code restructuring with no behaviour change  |  
| `docs`  | Documentation only  |  
| `test`  | Adding or updating tests  |  
| `chore`  | Build config, dependencies, tooling  |  
| `perf`  | Performance improvement  |  
**Real example from a deployment pipeline change:**

```
feat(deploy): add zero-downtime deployment support for Node.js apps

Implements atomic symlink switching for Node.js applications
deployed via DeployHQ. The new deployment strategy creates a
release directory, installs dependencies, then atomically swaps
the symlink only after health checks pass.

Closes #247

```

This commit message tells future developers exactly what changed, why, and which issue it resolved — without reading the diff. If you use AI-assisted development tools like Claude Code, the [Co-Authored-By attribution](https://deployhq.com/blog/how-to-use-git-with-claude-code-understanding-the-co-authored-by-attribution) in commit footers helps track which changes involved AI collaboration.
## AI-Assisted Code Review
AI code review tools have matured rapidly through 2025-2026 and are now a practical layer in the PR workflow — not a replacement for human reviewers, but a first pass that catches mechanical issues before a human spends time on them.
### Tools Worth Evaluating
**GitHub Copilot Code Review** — integrated directly into GitHub PRs. When you request a review from "Copilot", it posts inline comments on the diff identifying bugs, security issues, and performance concerns. It works best for catching null pointer risks, missing error handling, and obvious logic errors. It does not understand your business domain or architectural intent — that is still the human reviewer's job.
**CodeRabbit** — an AI review bot that posts a structured summary on every PR: a walkthrough of changes, a sequence diagram of affected call paths, and inline suggestions. It integrates with GitHub and GitLab and can be configured to enforce team-specific conventions via a `.coderabbit.yaml` file.
**Amazon CodeGuru Reviewer** — focuses on Java and Python, with particular strength in identifying concurrency bugs, resource leaks, and AWS SDK misuse. Less useful for frontend or polyglot codebases.
### How AI Review Fits into the Workflow
The most effective pattern is to run AI review _before_ human review:

```
flowchart LR
    A[Push to PR] --> B[CI Checks]
    B --> C[AI Review]
    C --> D[Author Fixes AI Findings]
    D --> E[Human Review]
    E --> F{Approved?}
    F -- Yes --> G[Merge]
    F -- No --> D

```

This means the human reviewer spends their time on architecture, business logic, and design — not pointing out that a function doesn't handle the null case. Teams that adopted this pattern at Stripe and Shopify report 30-40% reduction in human review round-trips.
**Practical tips:**
  * Configure AI reviewers to comment only on high-confidence findings. Low-confidence noise trains your team to ignore AI comments entirely. 
  * Use AI review for the [code review step before deployment](https://deployhq.com/blog/ai-code-review-before-deployment) — it catches issues that would otherwise reach production. 
  * Do not let AI review replace your second human reviewer on security-sensitive code (auth, payments, PII handling). AI tools miss context-dependent vulnerabilities. 
  * Review AI suggestions critically — they can be wrong, especially about performance trade-offs and architectural fit. 


## Code Review Best Practices: The Reviewer's Perspective
Most PR guides focus on the author. But review quality depends just as much on the reviewer's approach.
### Before You Start Reviewing
  1. **Read the description first.** If it doesn't make sense, ask for clarification before reading code. Reviewing code without understanding intent is guesswork. 
  2. **Check the PR size.** If it's over 400 lines, consider asking the author to split it. You'll both save time. 
  3. **Look at the CI results.** If tests are failing, don't start a manual review. Let the author fix CI first. 


### During Review
**Focus on what matters, in order:**
  1. **Correctness** — Does this code do what it claims? Are there edge cases? 
  2. **Security** — SQL injection, XSS, auth bypasses, secrets in code 
  3. **Architecture** — Does this fit the existing patterns? Will it cause problems at scale? 
  4. **Maintainability** — Can someone else understand this in six months? 
  5. **Style** — Leave this to linters. Don't nitpick formatting in reviews. 


**Comment with intent.** Prefix your comments so the author knows what's required:
  * `blocking:` — must be fixed before merge 
  * `nit:` — minor suggestion, optional 
  * `question:` — seeking understanding, not requesting a change 
  * `suggestion:` — take it or leave it 


**Example:**

```
blocking: This query interpolates user input directly into SQL.
Use parameterised queries instead.

---

nit: This variable name `d` could be more descriptive.
Maybe `deployment_config`?

---

question: Is there a reason we're not using the existing
`retry_with_backoff` utility here?

```

### After Review
Approve with confidence or request changes with specifics. "Looks good" is not a review — it's a rubber stamp. If you approved, say what you checked: "Reviewed the auth logic and migration. LGTM."
## PR Review Checklist
Use this checklist as a reference when reviewing pull requests. Copy it into your team's wiki or PR template and adapt it to your codebase.
### Correctness
  * [ ] The code does what the PR description claims 
  * [ ] Edge cases are handled (empty inputs, null values, boundary conditions) 
  * [ ] Error paths return meaningful messages, not silent failures 
  * [ ] Database queries use parameterised inputs (no string interpolation) 


### Security
  * [ ] No secrets, API keys, or credentials in the diff 
  * [ ] User input is validated and sanitised before use 
  * [ ] Authentication and authorisation checks are present where needed 
  * [ ] Dependencies added are from trusted sources with no known CVEs 


### Testing
  * [ ] New code has corresponding tests 
  * [ ] Tests cover both happy path and failure scenarios 
  * [ ] Existing tests still pass (CI green) 
  * [ ] Manual testing notes are included for UI or workflow changes 


### Architecture & Maintainability
  * [ ] Changes follow existing patterns in the codebase 
  * [ ] No unnecessary dependencies introduced 
  * [ ] Functions and classes have clear, single responsibilities 
  * [ ] Complex logic includes comments explaining _why_ , not just _what_


### Deployment Readiness
  * [ ] Database migrations are backward-compatible (can roll back safely) 
  * [ ] New environment variables are documented 
  * [ ] Feature flags are in place for risky changes 
  * [ ] The change is safe for [zero-downtime deployment](https://www.deployhq.com/features/zero-downtime-deployments)
  * [ ] [Rollback path](https://www.deployhq.com/features/one-click-rollback) has been considered 


## Branch Protection and Automated Checks
Branch protection rules prevent merging code that hasn't been reviewed or tested. Both GitHub and GitLab support these natively.
**Recommended branch protection for`main` :**
  * Require at least 1 approving review (2 for critical services) 
  * Require status checks to pass (CI, linting, type checking) 
  * Require branches to be up to date before merging 
  * Dismiss stale reviews when new commits are pushed 
  * Restrict who can push directly to `main`


### CI Pipeline for PRs
A minimal CI pipeline that runs on every PR should include:

```
# .github/workflows/pr-checks.yml
name: PR Checks

on:
  pull_request:
    branches: [main, staging]

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install dependencies
        run: npm ci

      - name: Type check
        run: npm run typecheck

      - name: Lint
        run: npm run lint

      - name: Unit tests
        run: npm test -- --coverage

      - name: Check PR size
        run: |
          LINES_CHANGED=$(git diff --stat origin/main...HEAD | tail -1 | awk '{print $4}')
          if [ "$LINES_CHANGED" -gt 500 ]; then
            echo "::warning::This PR changes $LINES_CHANGED lines. Consider splitting it."
          fi

```

The point is not to block every large PR — it's to make size visible so teams can make conscious decisions.
## Pull Requests and Deployment Workflows
The gap between "PR merged" and "code running in production" is where many teams lose confidence. If merging a PR requires someone to manually SSH into a server, run a build, and copy files — the process is fragile and error-prone.
This is where connecting your Git workflow to a deployment tool changes the dynamic. When you deploy through [DeployHQ](https://www.deployhq.com), merging a PR can automatically trigger the full deployment sequence: install dependencies, run [build pipeline commands](https://www.deployhq.com/features/build-pipelines), upload changed files, and execute post-deployment scripts.

```
flowchart LR
    A[Feature Branch] --> B[Open PR]
    B --> C[CI Checks Pass]
    C --> D[Code Review]
    D --> E{Approved?}
    E -- No --> F[Request Changes]
    F --> B
    E -- Yes --> G[Merge to main]
    G --> H[DeployHQ Triggered]
    H --> I[Build & Test]
    I --> J[Deploy to Staging]
    J --> K[Deploy to Production]
    K --> L[Zero-Downtime Swap]

```

### Deploy-on-Merge Pattern
The deploy-on-merge pattern works well for teams practising trunk-based development or short-lived feature branches:
  1. Developer opens PR against `main`
  2. CI runs automated checks 
  3. Reviewer approves 
  4. Developer merges 
  5. [DeployHQ](https://www.deployhq.com) detects the push to `main` and triggers deployment 
  6. [Zero-downtime deployment](https://www.deployhq.com/features/zero-downtime-deployments) swaps the new release in without dropping connections 


This pattern only works safely when you trust your test suite and review process. The PR is your last manual checkpoint before code reaches production — which is why everything in this guide matters.
### Staging Environments and Preview Deploys
For teams that want an extra verification step, configure [DeployHQ](https://www.deployhq.com) to deploy `main` merges to staging first. A separate manual trigger (or a promotion workflow) moves the build to production after someone verifies staging.
You can also set up branch-based deployments where PRs targeting specific branches deploy to preview environments — giving reviewers a live URL to test against before approving.
## PR Templates
Rather than relying on authors to remember the right format, add a template to your repository. GitHub looks for `.github/PULL_REQUEST_TEMPLATE.md` automatically.

```
## What does this PR do?

<!-- Summarise the change in 2-3 sentences -->

## Why is this change needed?

<!-- Link to issue, explain the problem, or describe the requirement -->

## How to review

<!-- Guide the reviewer: where to start, what to focus on -->

## Testing

- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] Works on staging environment

## Deployment considerations

- [ ] No new environment variables required
- [ ] Database migration included (if applicable)
- [ ] Safe for automatic deployment on merge
- [ ] Rollback plan documented (for high-risk changes)

## Screenshots / recordings

<!-- If UI changes, add before/after screenshots -->

```

Save this file in your repository root and every new PR will start with this structure pre-filled.
## Common PR Anti-Patterns
These patterns slow teams down and degrade code quality. If you recognise any of them, address the root cause — not just the symptom.
### The Mega-PR
**Symptom:** 2,000+ lines, touching 30 files, combining three unrelated features.
**Why it happens:** The author "got on a roll" and didn't stop to commit separately, or the feature was planned as a monolith.
**Fix:** Require stacked PRs for anything over 400 lines. Make splitting a norm, not an exception.
### The Drive-By Approval
**Symptom:** "LGTM" comment within 2 minutes of a 500-line PR being opened.
**Why it happens:** Social pressure to unblock teammates, combined with no clear review expectations.
**Fix:** Branch protection rules requiring status checks. Team agreements on minimum review time relative to PR size.
### The Nitpick Review
**Symptom:** 40 comments, all about variable naming and blank lines. Zero comments about logic or correctness.
**Why it happens:** Style issues are easy to spot. Logical issues require understanding context.
**Fix:** Automate style enforcement with linters and formatters. Reserve human review for what humans are good at: logic, architecture, and intent.
### The Ghost PR
**Symptom:** PR opened three weeks ago. 47 comments. Author has rebased six times. Still not merged.
**Why it happens:** The PR was too large, the scope kept creeping, or there's no team agreement on review turnaround time.
**Fix:** Set a team SLA for reviews (e.g., first review within 24 hours). If a PR isn't merged within a week, something is wrong with the process.
### Refactoring Mixed with Features
**Symptom:** "While I was in there, I also refactored the entire auth module."
**Why it happens:** Good intentions — the developer saw messy code and wanted to clean it up.
**Fix:** Separate PRs. One for the refactoring (with its own tests), one for the feature. Mixing them makes both harder to review and riskier to deploy.
## Measuring PR Health
Track these metrics to understand whether your PR process is helping or hurting:  
| Metric  | Healthy Range  | Warning Sign  |  
| --- | --- | --- |  
| Median time to first review  | < 4 hours  | > 24 hours  |  
| Median time to merge  | < 2 days  | > 5 days  |  
| Average PR size  | < 300 lines  | > 500 lines  |  
| Review comments per PR  | 2–8  | 0 (rubber stamp) or 20+ (scope issue)  |  
| Post-merge defect rate  | < 5%  | > 15%  |  
These numbers vary by team size and domain, but the trends matter more than the absolutes. If your time-to-merge is climbing, investigate whether PRs are getting larger or reviews are getting slower.
## Bringing It All Together
The pull request is not just a code review tool — it's the connective tissue between writing code and deploying it. When your PRs are small, well-described, and reviewed thoroughly, they become reliable checkpoints. When those checkpoints feed directly into automated deployment through a tool like [DeployHQ](https://www.deployhq.com), you get a workflow where merging a PR means the change is tested, reviewed, and live — without manual steps in between.
Start with one improvement. If your PRs lack descriptions, add a template. If reviews take too long, set a size limit. If deployment is manual, connect your repository to [DeployHQ](https://www.deployhq.com/signup) and let merges trigger deploys. Each change compounds.
* * *
**Ready to connect your pull request workflow to automated deployments?** [Sign up for DeployHQ](https://www.deployhq.com/signup) and start deploying from GitHub, GitLab, or Bitbucket in minutes.
If you have questions about configuring deployment triggers, branch-based environments, or zero-downtime deployments, reach out to us at support@deployhq.com or find us on [Twitter/X @deployhq](https://x.com/deployhq).
## Tell us how you feel about this post?
  * 0
  * 0
  * 0
  * 0
  * 0


##  Enjoy this? Share it!
  * [Share on LinkedIn ](https://www.linkedin.com/shareArticle?title=Pull+Request+Best+Practices%3A+A+Complete+Guide+%282026%29&url=https%3A%2F%2Fwww.deployhq.com%2Fblog%2Fthe-perfect-pull-request-best-practices-for-collaborative-development&summary=Learn+pull+request+best+practices+that+actually+improve+code+review+quality.+Covers+PR+sizing+%28why+400+lines+is+the+limit%29%2C+effective+descriptions%2C+reviewer+techniques%2C+stacked+PRs%2C+and+deploy-on-merge+workflows+with+CI%2FCD+integration.&mini=true&source=The+DeployHQ+Blog)
  * [Share on X ](https://twitter.com/share?text=Pull+Request+Best+Practices%3A+A+Complete+Guide+%282026%29&url=https%3A%2F%2Fwww.deployhq.com%2Fblog%2Fthe-perfect-pull-request-best-practices-for-collaborative-development)
  * [Share on Bluesky ](https://bsky.app/intent/compose?text=Pull%20Request%20Best%20Practices%3A%20A%20Complete%20Guide%20%282026%29%20https%3A%2F%2Fwww.deployhq.com%2Fblog%2Fthe-perfect-pull-request-best-practices-for-collaborative-development)
  * [Share on Mastodon ](https://mastodonshare.com/?text=Pull%20Request%20Best%20Practices%3A%20A%20Complete%20Guide%20%282026%29%20https%3A%2F%2Fwww.deployhq.com%2Fblog%2Fthe-perfect-pull-request-best-practices-for-collaborative-development)


Written by
### Facundo F
Facundo | CTO | DeployHQ | Continuous Delivery & Software Engineering Leadership - As CTO at DeployHQ, Facundo leads the software engineering team, driving innovation in continuous delivery. Outside of work, he enjoys cycling and nature, accompanied by Bono 🐶.
[More posts → ](https://www.deployhq.com/blog)
About DeployHQ
![DeployHQ](https://www.deployhq.com/assets/logos/deployhq-logo-dark-5d651de1840ee1ca1ebd14015d57f72b07185615e919747b65852154aeec77d8.svg) ![DeployHQ](https://www.deployhq.com/assets/logos/deployhq-logo-light-10d13fa98b70b094292123bc103f983614de57f31605b9e8361df4d0b87f210f.svg)
DeployHQ automates your deployment workflow — push code to your repository and let DeployHQ build, test, and deploy to any server. Supports Git, SSH/SFTP, cloud providers, and integrations with the tools you already use.
[Start deploying for free](https://www.deployhq.com/signup)
[Back to top ](https://www.deployhq.com/blog/the-perfect-pull-request-best-practices-for-collaborative-development)
[![DeployHQ](https://www.deployhq.com/assets/logos/deployhq-logo-dark-5d651de1840ee1ca1ebd14015d57f72b07185615e919747b65852154aeec77d8.svg) ![DeployHQ](https://www.deployhq.com/assets/logos/deployhq-logo-9586cdf9994a2286049465b3f9fa9df456051a862066c61031f2a1ed72518f4f.svg) ](https://www.deployhq.com/)
[All systems operational ](https://status.deployhq.com/)
[![GitHub](https://www.deployhq.com/assets/qlog/social/github-0f5bf5f3802343116d1758b6b70d2cec4f288c6f0feb30a1f65682d8b5f43686.svg) ![GitHub](https://www.deployhq.com/assets/qlog/social-dark/github-eedd97c55b52b5ba4f3795227052b78cffa89c26c799a736b7e792a51b703f82.svg) ](https://github.com/deployhq)[![X](https://www.deployhq.com/assets/qlog/social/x-f604e995965973cac098ae651469f376dbe477b7ab5dff4b4d67f9fd368f2c29.svg) ![X](https://www.deployhq.com/assets/qlog/social-dark/x-95e68199a75e0e936c11c486f8c5d69f5992534fea1c9eaa77cf2044296311c8.svg) ](https://x.com/deployhq)[![LinkedIn](https://www.deployhq.com/assets/qlog/social/linkedin-0edfc613235061d2978926b0934d654022890ce797c369030a2c44ec7e3cc296.svg) ![LinkedIn](https://www.deployhq.com/assets/qlog/social-dark/linkedin-ff5c0fbd22d4cb5c643c9c58e1a60a151fb5d5db51bca5ac7510b3281ca7f49b.svg) ![LinkedIn](https://www.deployhq.com/assets/qlog/social/linkedin-color-62f4f4b58767e1c2b10b30efeae4c46b902dc412635877716a1a822618f7c67d.svg) ](https://linkedin.com/company/deployhq/)[![Bluesky](https://www.deployhq.com/assets/qlog/social/bluesky-967ef5ac0ccfe6ca1d05ce665ca0a9ca530f9ce92deccb8f9bb5d73b76cbbcfa.svg) ![Bluesky](https://www.deployhq.com/assets/qlog/social-dark/bluesky-527a11f627215fcbf32386a396012a076f6134b12d75de9a0e8b54a167ddcd68.svg) ![Bluesky](https://www.deployhq.com/assets/qlog/social/bluesky-color-ec88bfbdcb899f18cc807c7bf46089ec006cde2109ad39fde9b49caa2926cbb1.svg) ](https://bsky.app/profile/deployhq.com)
Deploy faster with confidence.
From idea to production in minutes.
### Product
[Features](https://www.deployhq.com/features) [Pricing](https://www.deployhq.com/pricing) [Testimonials](https://www.deployhq.com/customers) [Documentation](https://www.deployhq.com/support) [API Reference](https://api.deployhq.com/docs) [Integrations](https://www.deployhq.com/features/integrations) [For Developers](https://www.deployhq.com/for-developers) [For Agencies](https://www.deployhq.com/for-agencies) [For Engineering Teams](https://www.deployhq.com/for-engineering-teams)
### Resources
[Blog](https://www.deployhq.com/blog) [Support Center](https://www.deployhq.com/support) [Guides and tutorials](https://www.deployhq.com/guides) [Status Page](https://status.deployhq.com/) [Changelog](https://changelog.deployhq.com/) [Learn Git](https://www.deployhq.com/git) [AI PageSpeed](https://pagespeed.deployhq.com/) [DeployHQ AI](https://www.deployhq.com/features/ai) [DeployHQ MCP Server](https://www.deployhq.com/features/deployhq-mcp) [CLI & Agents](https://www.deployhq.com/agents) [PR Radar](https://www.deployhq.com/features/pr-radar) [Ask AI](https://www.deployhq.com/support#ask-ai)
### Solutions
[Deploy from GitHub](https://www.deployhq.com/deploy-from-github) [Deploy from GitLab](https://www.deployhq.com/deploy-from-gitlab) [Deploy from Bitbucket](https://www.deployhq.com/deploy-from-bitbucket) [Deploy from Slack](https://www.deployhq.com/features/integrations/slack) [Shared Hosting Deployments](https://www.deployhq.com/shared-hosting) [VPS Deployments](https://www.deployhq.com/vps) [WordPress Deployments](https://www.deployhq.com/wordpress) [Zero Downtime](https://www.deployhq.com/features/zero-downtime-deployments) [Turbo Deployments](https://www.deployhq.com/features/turbo-deployments) [Static Site Deployments](https://www.deployhq.com/features/static-hosting) [Game Server Deployments](https://www.deployhq.com/deploy-to-game-servers)
### Company
[About](https://www.deployhq.com/about) [Careers](https://saas.group/careers/) [Contact](https://www.deployhq.com/contact) [Terms of Service](https://www.deployhq.com/terms) [Privacy Policy](https://www.deployhq.com/privacy) [Security](https://www.deployhq.com/security) [Cookie Policy](https://www.deployhq.com/blog/the-perfect-pull-request-best-practices-for-collaborative-development)
### Compare
[DeployHQ vs Buddy](https://www.deployhq.com/compare/deployhq-vs-buddy) [DeployHQ vs Jenkins](https://www.deployhq.com/compare/deployhq-vs-jenkins) [DeployHQ vs GitHub Actions](https://www.deployhq.com/compare/deployhq-vs-github-actions) [DeployHQ vs CircleCI](https://www.deployhq.com/compare/deployhq-vs-circleci) [DeployHQ vs Laravel Forge](https://www.deployhq.com/compare/deployhq-vs-laravel-forge) [All comparisons](https://www.deployhq.com/compare)
2026 DeployHQ (saas.group LLC). All rights reserved. [Running on 100% renewable energy](https://www.deployhq.com/green)


## Source: https://levelup.gitconnected.com/better-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2

[Sitemap](https://levelup.gitconnected.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)
## [Level Up Coding](https://levelup.gitconnected.com/?source=post_page---publication_nav-5517fd7b58a6-cd17b56962f2---------------------------------------)
·
Follow publication
[![Level Up Coding](https://miro.medium.com/v2/resize:fill:76:76/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_sidebar-5517fd7b58a6-cd17b56962f2---------------------------------------)
Coding tutorials and news. The developer homepage [gitconnected.com](http://gitconnected.com) && [skilled.dev](http://skilled.dev) && [levelup.dev](http://levelup.dev)
Follow publication
1
1
Top highlight
1
# Better Git branching strategy — Multi-apps, monorepos and multiple teams in focus — SimGit Flow
[![Andrew Winnicki](https://miro.medium.com/v2/resize:fill:64:64/1*rFLRs0U4Iwa4Z8zVmI-zPw.png)](https://andrewwinnicki.medium.com/?source=post_page---byline--cd17b56962f2---------------------------------------)
[Andrew Winnicki](https://andrewwinnicki.medium.com/?source=post_page---byline--cd17b56962f2---------------------------------------)
Follow
9 min read
·
May 16, 2022
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2Fcd17b56962f2&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&user=Andrew+Winnicki&userId=bbca98adbb88&source=---header_actions--cd17b56962f2---------------------clap_footer------------------)
534
10
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcd17b56962f2&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&source=---header_actions--cd17b56962f2---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dcd17b56962f2&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&source=---header_actions--cd17b56962f2---------------------post_audio_button------------------)
Share
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*6HrnBPxlzNxdGHzzJYsuUg.jpeg)
## A bit of history…
Back in 2016, we introduced a new frontend architecture and had to move towards a better, more organised, and more robust branching strategy (honestly, before that, it was just wild west, and we usually just pushed stuff to master release them). Our starting point wasn’t Git Flow or other commonly known or accepted branching strategy. Instead, we decided to try something that felt like it made sense and evolved over time, learning from our mistakes and addressing all issues and concerns. Our aim was to develop something that works well for our organisation without bias or compromises on important bits.
We ended up with a branching strategy that proved very efficient and worked perfectly with our eight frontend applications shared across nine agile teams and over fifteen frontend developers in total. All apps were run and deployed from a single mono-repo. We solved all our previous problems and did not introduce any new serious challenges. As with every solution, we ended up with compromises and a few trade-offs, but all were worth accepting.
## [Leadership Mentoring 1:1 leadership mentoring for CTOs, VPs & tech founders. Build clarity, confidence & resilience to lead teams, scale… www.andrewwinnicki.com ](https://www.andrewwinnicki.com/mentoring/leadership-mentoring/?source=post_page-----cd17b56962f2---------------------------------------)
> “A branching strategy that allows multiple teams to work on the same repository and push LIVE with minimal effort and high confidence in code others wrote.”
## The result... SimGit Flow
The branching strategy developed and perfected throughout the years proved to work across various companies, teams and technology stacks. What started as a flow for frontend apps was adapted later by iOS, Android, and backend teams. Every time a new team(s) tried the approach, it became a standard across the company after a few minor tweaks. What I found interesting is that almost everyone raised similar concerns, but in the end, none of them actually materialised in the real world scenarios.
Is this solution perfect? Hell No.  
Is it good? Well, pretty good.  
Can it be better? Always!
There is no silver bullet that solves all the problems, but maybe this approach will be one that will help your team. At least you can be assured it’s not a theory but a real-life approach that evolved over a long time and was proven multiple times on the battlefield.
## The core principles
  * **Master****is the source of truth.**  
That’s where every development starts, and the **master** branch is the ultimate source of truth. Your new code begins here, and you can be sure about anything you find there already as it has been 100% tested and is already live. There are no surprises as the branch is protected, and humans are not allowed to merge anything in manually or through PR.
  * **Prefixes for branches.**  
It helps to find branches easier and understand their purpose from the prefix. It is also easier to clean up the GIT when you don’t have to review it one by one.
  * **Descriptive branch names.**  
The prefix is one thing. A descriptive name is essential to help understand what we are looking at. Avoid names that are only IDs of tickets from your board. Make it human friendly and readable.
  * **Proper versioning.**  
Versioning affects release branch names, so it’s easier to find and push them out without affecting other teams’ workflows.
  * **Automate as much as possible.**  
Branch creation, versioning, merging. It will require some work, but it’s nothing unusual or more complicated to do than in any other release automation flow.


Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*-kllk8xGZkZYwlLL_KCZQg.jpeg)
## A bit more about prefixes.
  * **master/main** — our “golden copy” which always represents what is currently live, fully working, with no surprises.
  * **wip/*name*** —these will be used mostly for experimental work, POCs and other non-ticket based tasks. “WIP” means it cannot go live on its own, and probably it is a part of a significant feature or stream of work. It also might be a temporary integration branch. You can push these branches to dev servers for testing.  
**Example:** wip/newBuildProcess
  * **feature/#####-*name*** — these branches will be required to develop and test new features/tasks/bug fixes. You can push them to servers for testing before committing to a release. Use ##### for ticket number if it helps you connect the code with a task.  
**Example:** feature _/W_ EB1234-headerUpdate
  * **release**** _/_****X.XX**  
**Example:** release _/_ 3.12
  * **integration/*name*** — occasionally we will end up with tickets that are a part of a bigger feature and they all have to be tested and go live together. These are often considered as long-lived branches and allow for continous development and PRs to create the final feature/project.  
**Example:** integration/newUserRegistrationFlow
  * **hotfix/#####-*name*** — branch created from a specific release that we want to apply a hotfix to.  
**Example:** hotfix _/_ D _W_ C3342-datadogConsoleErrors


_Note: We decided to never delete release branches, and it was a smart move. Whenever we needed to go through history, check code at a specific time, or review updates, branches were all available and easy to find._
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*HKPBDSXnx-G8jgkyRLeHQw.jpeg)
## Pros:
  * It is something **between GitFlow and GitHub Flow** in many aspects but clarifies and simplifies a few unexplained areas.
  * It is a great **fit where the full CD is impossible** to implement due to extra manual steps, approval process or timing issues.
  * **Perfect for monorepos** with multiple apps built on shared core and worked on by various teams with different delivery schedules and priorities.
  * You will be able to easily create a**release in isolation** , test it, deploy it and only once it is 100% fine, merge it back to Master. This means nobody will be annoyed if your code fails because it wasn’t tested yet.
  * **Multiple teams** can create releases for different apps from the same repo and deploy them without blocking each other.
  * Easy to **manage multiple releases** simultaneously and sync them just before pushing the code live.
  * No need for **develop** branch. Just forget about it.
  * **There are no collisions in release branch naming** since versioning is controlled by the build process & pipelines.
  * **The master/main** branch is always safe to use for a new release. You can trust there is no untested code or nasty surprises.
  * **No need to rely on hashes or tags** , making everything human-readable, but it is still a good idea to leave tags whenever the release has been pushed live and merged back to master.
  * Features (on release branches) can **go live whenever they are ready** & tested.
  * Since each release is a separate branch, it’s straightforward**to roll back** or do updates on this particular branch and release any app.
  * **No release cycle locking** due to unfinished code or waiting on dependencies or other teams.
  * Encourages **testing** before merging.
  * Creates **less cognitive overhead** for developers as branches are maintained by the release pipelines (assuming you have proper automation in place).
  * Embraces **work-in-progress PR** s, rather than monster PRs at the end.
  * **Easy to abandon a release** if it’s not needed anymore for any reason.
  * There is a lot of potential to**extend this flow for CI** and automatic deployment to the dev environment, but it will require some adjustments.


## Cons:
  * **Release branch name will** **change** per release, so it might require writing more intelligent pipelines as you won’t be releasing from one branch (usually master).
  * **Harder to automate** for continuous delivery, but not impossible.
  * Developers need to **keep track** of what releases are in progress.
  * **Before merging to the release branch** , you need to ensure you are working on the latest code from the master (merge it in).
  * If your team is working on a significant feature and need to test it, you might (don’t have to) end up with**the integration branch** before pushing it all to a release.
  * Since things might change in the master during development, you will have to merge it in later, and it **might create some extra conflicts to resolve**.
  * When all team members work in some kind of isolation, **you will get conflicts when they all meet** in the release branch (this was our biggest concern, which wasn’t really that bad).
  * It might all **make no sense** if you don’t consider proper versioning and pipeline automation.


## App versioning is important!
Since it is a bit bigger topic, I will cover that in one of my future posts, including how to automate it during the build process and what are the good and bad practices based on our learning.
## Get Andrew Winnicki’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
In short, we always used with classic SemVer 2.0 (<https://semver.org/>) — major, minor, update. Although, some teams decided to just adopt flat versioning and use major versions only. Whatever works for your team, but there are good reasons why SimVer works well, especially for the web frontend.
I wrote a blogpost on that topic too….
## [Better versioning for frontend applications (and not only) is like traffic lights for engineers. It’s crucial to understand what we can expect from the code without digging through the repo like a pig on a beach… andrewwinnicki.medium.com ](https://andrewwinnicki.medium.com/better-versioning-for-frontend-applications-and-not-only-is-like-traffic-lights-for-engineers-380e9beb6a42?source=post_page-----cd17b56962f2---------------------------------------)
## Release proces is important!
Pipelines control how branches for each release are created, versioned and correctly updated with relevant changes to avoid mistakes. Most importantly, they are responsible for safely pushing your code live and merging everything back to master. It is impossible to be serious about software engineering and not have release automation in place.
Since it’s another important topic that I won’t be able to cover here, you can expect another blog post in the future, which will neatly connect the branching and versioning together with the release process.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*R6P4Pm-d62oPt22bS1S7oA.jpeg)
## Examples, examples, examples…
A few examples from the real-life explaining how code will flow between teams and developers to deliver safely to a live environment.
### 1. Simple
Two devs are preparing two features and releasing them together.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*sHApexlApm_0sYvWqSYn4w.png)
### 2. Typical
A few features, a release branch, and a late merge.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*Qm5VDht5461fgoZHWaovsg.png)
### 3. Regular features and one very long one. Two releases.
A flow where one feature takes quite long. Basically, before merging to release, it is always wise to merge in the master again to be 100% up to date.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*4ZSvLrUbTn0QCjA5QWS-2g.png)
### 4. Abandoned release.
When one release started, another was created afterwards but went live before the first one (quick fix, probably). This could be prevented by making some extra safeguards in your pipelines which will avoid creating more than one release “in progress” at a time. Also, hotfix could be used instead for the small update.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*OzZxsArOizjkUd2gIYMh5w.png)
### 5. Hotfix after a release.
If you have a simple bugfix to existing live code, you can use a hotfix. That will help you not end up in a situation like the one above. A hotfix is used to update the existing version with a small but important patch.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*Yi7bHKlMd9qejrEwl04SKg.png)
### 6. A bit more is going on.
Please note that different people and teams are likely to be handled such an example. It might look complicated, but it will go smooth if you follow two simple rules.
  * Always make sure you merged in master to your release branch and the versions are correct.
  * Communicate to the team release plans and ongoing branches (often, teams work together to create one release and push it out).


Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*3HR-Wuj52S4uIiMtPDt2Bw.png)
## Quick Summary
It is impossible to cover and explain all edge scenarios in one blogpost, but there is also a good reason why I didn’t want to do that. It’s easy to get obsessed with challenges, see them as blockers and not even try something different that might solve the majority of our problems. The above branching strategy delivers on 99,9% of typical use cases . As I said earlier, it worked efficiently across multiple teams sharing code in one repo and pushing through the same release pipelines into 8 different apps. As long as you communicate and cooperate (not compete) with other teams, it should all go smooth.
**Give it a go and let me know how you made it better!**
_ps. Thanks to Alfredo Pinto for a suggestion about the name for this flow. We had a little exchange in the comments on Medium ;)_
[Git](https://medium.com/tag/git?source=post_page-----cd17b56962f2---------------------------------------)
[Software Development](https://medium.com/tag/software-development?source=post_page-----cd17b56962f2---------------------------------------)
[Software](https://medium.com/tag/software?source=post_page-----cd17b56962f2---------------------------------------)
[Front End Development](https://medium.com/tag/front-end-development?source=post_page-----cd17b56962f2---------------------------------------)
[DevOps](https://medium.com/tag/devops?source=post_page-----cd17b56962f2---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2Fcd17b56962f2&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&user=Andrew+Winnicki&userId=bbca98adbb88&source=---footer_actions--cd17b56962f2---------------------clap_footer------------------)
534
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2Fcd17b56962f2&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&user=Andrew+Winnicki&userId=bbca98adbb88&source=---footer_actions--cd17b56962f2---------------------clap_footer------------------)
534
10
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcd17b56962f2&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fbetter-git-branching-strategy-multi-apps-monorepos-and-multiple-teams-in-focus-cd17b56962f2&source=---footer_actions--cd17b56962f2---------------------bookmark_footer------------------)
[![Level Up Coding](https://miro.medium.com/v2/resize:fill:96:96/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--cd17b56962f2---------------------------------------)
[![Level Up Coding](https://miro.medium.com/v2/resize:fill:128:128/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--cd17b56962f2---------------------------------------)
Follow
## [Published in Level Up Coding](https://levelup.gitconnected.com/?source=post_page---post_publication_info--cd17b56962f2---------------------------------------)
[327K followers](https://levelup.gitconnected.com/followers?source=post_page---post_publication_info--cd17b56962f2---------------------------------------)
·[Last published 7 hours ago](https://levelup.gitconnected.com/from-notepad-to-no-pad-is-the-ide-dead-8757589f0d6a?source=post_page---post_publication_info--cd17b56962f2---------------------------------------)
Coding tutorials and news. The developer homepage [gitconnected.com](http://gitconnected.com) && [skilled.dev](http://skilled.dev) && [levelup.dev](http://levelup.dev)
Follow
[![Andrew Winnicki](https://miro.medium.com/v2/resize:fill:96:96/1*rFLRs0U4Iwa4Z8zVmI-zPw.png)](https://andrewwinnicki.medium.com/?source=post_page---post_author_info--cd17b56962f2---------------------------------------)
[![Andrew Winnicki](https://miro.medium.com/v2/resize:fill:128:128/1*rFLRs0U4Iwa4Z8zVmI-zPw.png)](https://andrewwinnicki.medium.com/?source=post_page---post_author_info--cd17b56962f2---------------------------------------)
Follow
## [Written by Andrew Winnicki](https://andrewwinnicki.medium.com/?source=post_page---post_author_info--cd17b56962f2---------------------------------------)
[558 followers](https://andrewwinnicki.medium.com/followers?source=post_page---post_author_info--cd17b56962f2---------------------------------------)
·[28 following](https://medium.com/@andrewwinnicki/following?source=post_page---post_author_info--cd17b56962f2---------------------------------------)
London-based mentor, guide, coach, facilitator, tech leader, software engineer, creative spirit, and above all, a human being committed to helping men thrive.
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----cd17b56962f2---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----cd17b56962f2---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----cd17b56962f2---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cd17b56962f2---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----cd17b56962f2---------------------------------------)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cd17b56962f2---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cd17b56962f2---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cd17b56962f2---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----cd17b56962f2---------------------------------------)
To make Medium work, we log user data. By using Medium, you agree to our [Privacy Policy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9), including cookie policy.


## Source: https://konabos.com/blog/building-a-full-stack-app-with-next-js-trpc-drizzle-orm-neon-database

# [![Konabos](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/050f2be3-aa82-4198-b001-6073a0a64489/konabos-Vertical-Logo-high-res.png?w=160&h=160&fm=webp&)](https://konabos.com/)
[![Konabos](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/050f2be3-aa82-4198-b001-6073a0a64489/konabos-Vertical-Logo-high-res.png?w=224&h=224&fm=webp&)](https://konabos.com/)
  * [Who We Are](https://konabos.com/who-we-are)
  * Services
  * Partners
  * [Case Studies](https://konabos.com/case-studies)
  * [Blog](https://konabos.com/blog)
  * [Videos](https://konabos.com/videos)
  * [Contact Us](https://konabos.com/contact)


![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/2ea5cf60-1d36-4564-92dd-135a311e13e3/Intro-to-tRPC.jpg)
# Building a Full-Stack App with Next.js, tRPC, Drizzle ORM & Neon Database
Jose Raimondi - Front-End Developer
3 Mar 2025
Share on social media
In this blog post, we’ll walk through setting up a modern full-stack application using tRPC, Next.js, Drizzle ORM, Neon Database, and Zod. Our project will be a simple recipes app, where users can add and retrieve recipes with structured validation.  
  
Why These Technologies?
  * **Next.js** : A powerful React framework with built-in API routes.
  * **tRPC** : Type-safe APIs without needing REST or GraphQL.
  * **Drizzle ORM** : A TypeScript-first ORM with a great developer experience.
  * **Neon Database** : A serverless Postgres database that will work for our example.


## Setting Up the Project
  1. Initialize Next.js with typescript:  
  
`npx create-next-app@latest recipes-app --typescript  
 cd recipes-app  
 `
  2. Install dependencies  
  
`npm install @trpc/server @trpc/client @trpc/react-query @trpc/next superjson   
 npm install drizzle-orm pg neon zod @hookform/resolvers  
 npm install -D @types/node @types/react`


## Creating a Neon Database
### 1. Sign Up for Neon
Go to [Neon.tech](https://neon.tech/) and sign up for an account. Once logged in, create a new project and select PostgreSQL as your database.
### 2. Retrieve Your Database Connection String
Once your database is created, go to the **Connection** tab and copy the PostgreSQL connection string. It should look like this:  
  
`postgres://user:password@your-neon-db.neon.tech/dbname`
### 3. Set Up Environment Variables
Create a `.env` file in the root of your project and add your database URL:
`DATABASE_URL=postgres://user:password@your-neon-db.neon.tech/dbname`
## Setting up tRPC`
## 1. Create the tRPC Router
Create a new folder `server/trpc` and inside, add `trpc.ts`:  

![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/9a592e39-39e7-48f0-a5d8-bd34f4d15566/trpc-snap-18.png)
  
Here, `initTRPC.create()` initializes the tRPC instance with SuperJSON for automatic serialization and deserialization of complex data structures. We can also format errors to the structure that we want
### 2. Create the Recipes Router
Inside `server/index`, create `index.ts` file where we can add our router:  

![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/9d425411-917f-44bb-9f84-c156ce26272b/trpc-snap-2.png)
  
A router in tRPC acts as a central hub for defining API endpoints. Each router groups related procedures (functions) that handle different operations, such as retrieving or modifying data. It allows us to define queries (data fetching) and mutations (data modifications) in a type-safe manner.
### 3. Create TRPC handler:
you can add this inside inside `api/trpc/[trpc]/route.ts` file
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/8bf32758-1b0e-493a-8d4e-2b060d5869a3/trpc-snap-3.png)
  
This will ensure each tRPC route is handled correctly.
## Configuring Drizzle ORM with Neon Database
### 1. Setup Database Connection
Create `db/drizzle.ts`:
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/8e3551c7-005c-47ac-961a-7b9d69baf5c1/trpc-snap-4.png)
  
Drizzle ORM allows us to interact with our Neon database using a clean, type-safe API.
### 2. Define Recipe Model
Create `db/schema.ts`:
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/aafad132-81ea-4db0-8bfd-bb427cdbc67d/trpc-snap-5.png)
  
This schema defines a `recipes` table with an unique id, a `title`, a JSON array of `ingredients`, and a `text`field for `instructions`.
### 3. Create drizzle config
Create drizzle.config.ts on the root of your project:
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/776e7347-c597-4770-9887-4693abccc537/trpc-snap-6.png)
  
Ensure that schema path is pointing to the correct file 
### 4. Run Database Migrations
To ensure our database is in sync with our schema, we generate and apply migrations. After you do this you should be able to see the tables in your neon DB  
  
`drz --config drizzle.config.ts generate`
`drz --config drizzle.config.ts push  
 `
## Using tRPC in the Frontend
### 1. Setup tRPC Provider
Create `_trpc` folder and define` clients.ts` file:
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/9add9e4e-aa9d-4a74-bafd-fcfd3bd91c53/trpc-snap-7.png)
  
This initializes a tRPC client that can be used throughout the app.
  
Then we can create `Provider.tsx  
 `
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/a18daa68-e34c-4294-a649-667eb3bc68ab/trpc-snap-17.png)
  
(Notice how trpc takes advantage of tanstack react-query as well)
And add the Provider to your root layout:
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/73edf7b2-0c8e-40df-abc9-4a4d304a2dcf/trpc-snap-9.png)
  
This setup ensures that our entire application has access to the tRPC client and React Query for caching and state management.
### 2. Fetch Recipes in a Component
Create `components/Recipes.tsx`:  

![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/8ee3303a-8dcb-4afb-bfb4-f51063ef2d9d/trpc-snap-11.png)
  
and `Recipes.hooks.ts` for handling logic
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/02f4c029-113a-4040-abb1-d2407f4473ff/trpc-snap-12.png)
  
If you have every used tanstack react-query, you will find this code very familiar as it works on a similar way. Also you will be able to see how every request method is strongly typed!
You should as well add an individual Recipe card component
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/fe91e87a-7e2c-4f1c-bb37-01521a3a5e15/trpc-snap-13.png)
### 3. Create form to edit and create recipes
Add `CreateOrEditRecipe.tsx`
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/c6d14509-cd90-4111-8581-f94b7219ce3e/trpc-snap-14.png)
As well as `CreateOrEditREcipe.hooks.ts` to handle the logic (here you can define the behaviour for successful mutations as well as errored ones):  

![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/e082c96e-d302-4d6a-be77-898c801a2735/trpc-snap-16.png)
And there you have it! by combining Next.js, tRPC, Drizzle ORM, Neon Database, and Zod, we built a fully type-safe, modern recipes app with great developer experience. This stack provides scalability and maintainability while avoiding unnecessary complexity. 
![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/7034ad92-cc72-4f3c-8421-e5f20108d265/reicpe-app.png)
If you have any questions or improvements, don't be shy to reach out! and please feel free to play with the structure and the logic as you like, since this is just an example.
* * *
Tags:
[TypeScript](https://konabos.com/tag/typescript)[React](https://konabos.com/tag/react)
* * *
Share on social media
![Jose Raimondi](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/4e52232c-6396-404a-8e40-f6af794e79cd/Jose-Raimondi_240x240.png)
#### Jose Raimondi
Jose is a Front-End Developer with a love for building new things. He finds the idea of working with the latest technologies such as React.js, Next.js, Kentico Kontent, Tailwind CSS, etc, very  
thrilling. Coming from a musical background, he sees that software engineering shares something with music, which is creativity. Embracing the challenge of learning more every day, as technology evolves there will always be excitement for him in the field.
[](https://www.linkedin.com/in/jose-raimondi98/)[](https://www.twitter.com/eljose)
## Related content
[![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/61b61c94-8ece-4bfd-b82e-e4d5cd679451/hero-blog.jpeg?w=730&h=448&fm=webp&) 20 May 2025 [Tailwind Css](https://konabos.com/tag/tailwind-css) [TypeScript](https://konabos.com/tag/typescript) [Testing](https://konabos.com/tag/testing) [Test Case Management](https://konabos.com/tag/test-case-management) [Next.js](https://konabos.com/tag/next-js) [React](https://konabos.com/tag/react) [Playwright](https://konabos.com/tag/playwright) BDD Testing with Next.js and Playwright: Scalable, Readable, Reliable | Konabos Learn how to set up BDD testing in Next.js using Playwright, Cucumber, and Gherkin. Build scalable, readable tests that align devs, QA, and stakeholders. ](https://konabos.com/blog/bdd-testing-with-next-js-and-playwright-scalable-readable-reliable)
[![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/9f0fc7e3-11bc-40eb-adf2-efd0d11c6c8b/draft.jpg?w=730&h=448&fm=webp&) 23 Apr 2025 [TypeScript](https://konabos.com/tag/typescript) [React](https://konabos.com/tag/react) [Next.js](https://konabos.com/tag/next-js) Add Preview Mode to Pages with Payload CMS and Next.js | Konabos Learn how to add preview functionality to your Payload CMS pages using Next.js 14s draft mode. Enable real-time content previews with a simple setup. ](https://konabos.com/blog/add-preview-functionality-to-your-pages-using-payload-cms-and-next-js)
[![](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/54421f82-ad6f-43a6-b0c2-7e5d7ef1e0b9/react%20blog%203.png?w=730&h=448&fm=webp&) 12 Feb 2025 [React](https://konabos.com/tag/react) [Next.js](https://konabos.com/tag/next-js) Managing Global State in React with Context and useReducer | Konabos Learn how to manage global state in React using Context and useReducer with TypeScript ](https://konabos.com/blog/managing-global-state-in-react-with-context-and-usereducer)
view more
* * *
## Subscribe to newsletter
Enter email address
I accept the Terms and conditions and the Privacy policy
Submit
![Konabos](https://assets-us-01.kc-usercontent.com:443/1bfb8498-0a69-0062-41f9-7be1ab72379a/050f2be3-aa82-4198-b001-6073a0a64489/konabos-Vertical-Logo-high-res.png?w=416&h=416&fm=webp&)
[](https://www.linkedin.com/company/konabos "LinkedIn")[](https://www.youtube.com/konabosinc "YouTube")
### Quick Links
[Home](https://konabos.com/)[Services](https://konabos.com/services)[Blog](https://konabos.com/blog)[Videos](https://konabos.com/videos)[News](https://konabos.com/news)[Podcast](https://konaverse.konabos.com/)[Careers](https://konabos.com/careers)[Partners](https://konabos.com/partners)[Contact Us](https://konabos.com/contact)
### Our Services
[Customer Experience Strategy](https://konabos.com/services/digital-strategy)[Architecture](https://konabos.com/services/architecture)[UX & Creative](https://konabos.com/services/user-experience-and-user-interface-design)[Development](https://konabos.com/services/development)[Training & Coaching](https://konabos.com/services/training-and-coaching)[Sitecore Personalization Enablement](https://konabos.com/services/sitecore-personalization-enablement)[WAaaS: Web Accessibility as a Service](https://konabos.com/services/accessibility-compliance-audit-services)[Support](https://konabos.com/services/support)
### Contact Us
LocationsCalifornia, USAOttawa, CanadaToronto, Canada
[+1-866-577-6310](tel:+1-866-577-6310)
info@konabos.com
2026 Konabos Inc. All Rights Reserved.
[Privacy policy](https://konabos.com/privacy-policy)|[Terms and Conditions](https://konabos.com/terms-and-conditions)


## Source: https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/

![Revisit consent button](https://cdn-cookieyes.com/assets/images/revisit.svg)
We use cookies. [Cookies Policy](https://softwaremill.com/cookies-policy)
Customize Reject All Accept All
Customize Consent Preferences ![](https://cdn-cookieyes.com/assets/images/close.svg)
We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.
The cookies that are categorized as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site. ... Show more
NecessaryAlways Active
Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.
  * Cookie
cookieyes-consent
  * Duration
1 year
  * Description
CookieYes sets this cookie to remember users' consent preferences so that their preferences are respected on subsequent visits to this site. It does not collect or store any personal information about the site visitors.


  * Cookie
sessionId
  * Duration
Never Expires
  * Description
This cookie, set by Microsoft, is used by the website to store the user's session ID and is sent with each request to the ASP.NET application.


  * Cookie
_cfuvid
  * Duration
session
  * Description
Calendly sets this cookie to track users across sessions to optimize user experience by maintaining session consistency and providing personalized services


  * Cookie
dd_cookie_test_*
  * Duration
1 minute
  * Description
Datadog Real User Monitoring (RUM) Browser SDK sets this cookie as a temporary cookie used to test for cookie support. 


  * Cookie
JSESSIONID
  * Duration
session
  * Description
New Relic uses this cookie to store a session identifier so that New Relic can monitor session counts for an application.


  * Cookie
rc::a
  * Duration
Never Expires
  * Description
This cookie is set by the Google recaptcha service to identify bots to protect the website against malicious spam attacks.


  * Cookie
rc::c
  * Duration
session
  * Description
This cookie is set by the Google recaptcha service to identify bots to protect the website against malicious spam attacks.


  * Cookie
m
  * Duration
1 year 1 month 4 days 1 minute
  * Description
Stripe sets this cookie for fraud prevention purposes. It identifies the device used to access the website, allowing the website to be formatted accordingly.


Functional
Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.
  * Cookie
lidc
  * Duration
1 day
  * Description
LinkedIn sets the lidc cookie to facilitate data center selection.


  * Cookie
li_gc
  * Duration
6 months
  * Description
Linkedin set this cookie for storing visitor's consent regarding using cookies for non-essential purposes.


  * Cookie
__cf_bm
  * Duration
1 hour
  * Description
Cloudflare set the cookie to support Cloudflare Bot Management. 


  * Cookie
ytidb::LAST_RESULT_ENTRY_KEY
  * Duration
Never Expires
  * Description
The cookie ytidb::LAST_RESULT_ENTRY_KEY is used by YouTube to store the last search result entry that was clicked by the user. This information is used to improve the user experience by providing more relevant search results in the future.


  * Cookie
yt-remote-session-app
  * Duration
session
  * Description
The yt-remote-session-app cookie is used by YouTube to store user preferences and information about the interface of the embedded YouTube video player.


  * Cookie
yt-remote-cast-installed
  * Duration
session
  * Description
The yt-remote-cast-installed cookie is used to store the user's video player preferences using embedded YouTube video.


  * Cookie
yt-remote-session-name
  * Duration
session
  * Description
The yt-remote-session-name cookie is used by YouTube to store the user's video player preferences using embedded YouTube video.


  * Cookie
yt-remote-fast-check-period
  * Duration
session
  * Description
The yt-remote-fast-check-period cookie is used by YouTube to store the user's video player preferences for embedded YouTube videos.


  * Cookie
S
  * Duration
1 hour 1 minute
  * Description
Used by Yahoo to provide ads, content or analytics.


  * Cookie
lang
  * Duration
session
  * Description
LinkedIn sets this cookie to remember a user's language setting.


  * Cookie
yt-remote-cast-available
  * Duration
session
  * Description
The yt-remote-cast-available cookie is used to store the user's preferences regarding whether casting is available on their YouTube video player.


  * Cookie
sp_t
  * Duration
1 year
  * Description
The sp_t cookie is set by Spotify to implement audio content from Spotify on the website and also registers information on user interaction related to the audio content.


  * Cookie
sp_landing
  * Duration
1 day
  * Description
The sp_landing is set by Spotify to implement audio content from Spotify on the website and also registers information on user interaction related to the audio content.


Analytics
Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.
  * Cookie
_ga
  * Duration
1 year 1 month 4 days
  * Description
Google Analytics sets this cookie to calculate visitor, session and campaign data and track site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognise unique visitors.


  * Cookie
_gid
  * Duration
1 day
  * Description
Google Analytics sets this cookie to store information on how visitors use a website while also creating an analytics report of the website's performance. Some of the collected data includes the number of visitors, their source, and the pages they visit anonymously.


  * Cookie
_gat_UA-*
  * Duration
1 minute
  * Description
Google Analytics sets this cookie for user behaviour tracking. 


  * Cookie
_ga_*
  * Duration
1 year 1 month 4 days
  * Description
Google Analytics sets this cookie to store and count page views.


  * Cookie
_fbp
  * Duration
3 months
  * Description
Facebook sets this cookie to display advertisements when either on Facebook or on a digital platform powered by Facebook advertising after visiting the website.


  * Cookie
uid
  * Duration
1 year 1 month 4 days
  * Description
This is a Google UserID cookie that tracks users across various website segments.


  * Cookie
sid
  * Duration
1 year 1 month 4 days
  * Description
The sid cookie contains digitally signed and encrypted records of a user’s Google account ID and most recent sign-in time.


  * Cookie
_s
  * Duration
1 year
  * Description
This cookie is associated with Shopify's analytics suite.


  * Cookie
_gat_gtag_UA_*
  * Duration
1 minute
  * Description
Google Analytics sets this cookie to store a unique user ID.


  * Cookie
_gh_sess
  * Duration
session
  * Description
GitHub sets this cookie for temporary application and framework state between pages like what step the user is on in a multiple step form.


  * Cookie
browser_id
  * Duration
5 years
  * Description
This cookie is used for identifying the visitor browser on re-visit to the website.


  * Cookie
ahoy_visitor
  * Duration
2 years
  * Description
This cookie is set by Powr for analytics measurement.


  * Cookie
ahoy_visit
  * Duration
4 hours
  * Description
This cookie is set by Powr for analytics measurement.


  * Cookie
ajs_user_id
  * Duration
Never Expires
  * Description
This cookie is set by Segment to help track visitor usage, events, target marketing, and also measure application performance and stability.


  * Cookie
ajs_anonymous_id
  * Duration
Never Expires
  * Description
This cookie is set by Segment to count the number of people who visit a certain site by tracking if they have visited before.


  * Cookie
attribution_user_id
  * Duration
1 year
  * Description
This cookie is set by Typeform for usage statistics and is used in context with the website's pop-up questionnaires and messengering.


  * Cookie
_tccl_visitor
  * Duration
1 year
  * Description
Godaddy sets this cookie to collect aggregated, anonymized data to improve the site’s performance.


  * Cookie
_tccl_visit
  * Duration
1 hour
  * Description
Godaddy sets this cookie to collect aggregated, anonymized data to improve the site’s performance.


  * Cookie
_lfa
  * Duration
1 year
  * Description
The lfa cookie is a third-party tracking cookie used by the Leadfeeder service to identify business visitors by their IP addresses. It collects data such as visited pages and time spent on the site to facilitate lead generation, website analytics, and retargeting for B2B marketing. This information helps companies recognize which businesses are visiting their websites, enabling them to identify potential leads and tailor their marketing efforts.


  * Cookie
_lfa_consent
  * Duration
1 year
  * Description
The _lfa_consent stores consent status (expires after 2 years).


  * Cookie
_lfa_test_cookie_stored
  * Duration
Less than a minute
  * Description
A cookie that is only temporarily used to check if the browser supports cookies or not. This cookie might show up in a cookie scanner for your consent management platform.


  * Cookie
vuid
  * Duration
1 year 1 month 4 days
  * Description
Vimeo installs this cookie to collect tracking information by setting a unique ID to embed videos on the website. 


  * Cookie
_pk_id
  * Duration
1 year
  * Description
Used by the Piwik PRO analytical tool to recognize visitors and record their various actions during their visits.


  * Cookie
_pk_ses
  * Duration
30 min
  * Description
Used by the Piwik PRO analytical tool to group all user actions within one session.


Performance
Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors.
No cookies to display.
Advertisement
Advertisement cookies are used to provide visitors with customized advertisements based on the pages you visited previously and to analyze the effectiveness of the ad campaigns.
  * Cookie
YSC
  * Duration
session
  * Description
Youtube sets this cookie to track the views of embedded videos on Youtube pages.


  * Cookie
VISITOR_INFO1_LIVE
  * Duration
6 months
  * Description
YouTube sets this cookie to measure bandwidth, determining whether the user gets the new or old player interface.


  * Cookie
_rdt_uuid
  * Duration
3 months
  * Description
Reddit sets this cookie to build a profile of your interests and show you relevant ads.


  * Cookie
muc_ads
  * Duration
1 year 1 month 4 days
  * Description
Twitter sets this cookie to collect user behaviour and interaction data to optimize the website.


  * Cookie
personalization_id
  * Duration
1 year 1 month 4 days
  * Description
Twitter sets this cookie to integrate and share features for social media and also store information about how the user uses the website, for tracking and targeting.


  * Cookie
bcookie
  * Duration
1 year
  * Description
LinkedIn sets this cookie from LinkedIn share buttons and ad tags to recognize browser IDs.


  * Cookie
bscookie
  * Duration
1 year
  * Description
LinkedIn sets this cookie to store performed actions on the website.


  * Cookie
yt-remote-device-id
  * Duration
Never Expires
  * Description
YouTube sets this cookie to store the user's video preferences using embedded YouTube videos.


  * Cookie
yt-remote-connected-devices
  * Duration
Never Expires
  * Description
YouTube sets this cookie to store the user's video preferences using embedded YouTube videos.


  * Cookie
yt.innertube::requests
  * Duration
Never Expires
  * Description
YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen.


  * Cookie
yt.innertube::nextId
  * Duration
Never Expires
  * Description
YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen.


  * Cookie
scribd_ubtc
  * Duration
10 years
  * Description
Scribd sets this cookie to gather data on user behaviour across several websites and maximise the relevancy of the advertisements on the website.


  * Cookie
NID
  * Duration
6 months 1 minute
  * Description
Google sets the cookie for advertising purposes; to limit the number of times the user sees an ad, to unwanted mute ads, and to measure the effectiveness of ads.


  * Cookie
VISITOR_PRIVACY_METADATA
  * Duration
6 months
  * Description
YouTube sets this cookie to store the user's cookie consent state for the current domain. 


  * Cookie
guest_id
  * Duration
20 years
  * Description
Twitter sets this cookie to identify and track the website visitor. It registers if a user is signed in to the Twitter platform and collects information about ad preferences.


  * Cookie
COMPASS
  * Duration
1 hour 1 minute
  * Description
The COMPASS cookie is used by Yahoo to deliver targeted advertising based on user's online behavior.


Uncategorized
Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.
  * Cookie
_octo
  * Duration
1 year
  * Description
No description available.


  * Cookie
logged_in
  * Duration
1 year
  * Description
No description available.


  * Cookie
__Secure-ROLLOUT_TOKEN
  * Duration
6 months
  * Description
YouTube sets this cookie to manage feature rollout and experimentation. It helps Google control which new features or interface changes are shown to users as part of testing and staged rollouts, ensuring consistent experience for a given user during an experiment.


  * Cookie
CSRF-TOKEN
  * Duration
session
  * Description
Description is currently not available.


  * Cookie
li_alerts
  * Duration
1 year
  * Description
LinkedIn sets this cookie to track impressions of LinkedIn alerts, such as the Cookie Banner and to implement cool-off periods for display of alerts.


  * Cookie
AWSALBTGCORS
  * Duration
7 days
  * Description
No description available.


  * Cookie
tf_respondent_cc
  * Duration
6 months
  * Description
Description is currently not available.


  * Cookie
AWSALBTG
  * Duration
7 days
  * Description
No description available.


  * Cookie
_scc_session
  * Duration
20 minutes
  * Description
Description is currently not available.


  * Cookie
_secure_speakerd_session
  * Duration
14 days
  * Description
Description is currently not available.


  * Cookie
__Secure-YEC
  * Duration
past
  * Description
Description is currently not available.


  * Cookie
_stackblitz_session
  * Duration
session
  * Description
Description is currently not available.


Reject All Save My Preferences Accept All
[](https://softwaremill.com/)[](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
  * [Services](https://softwaremill.com/) [Services](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
    * ## Services overview
Partner with us to experience how the right technology choices can strengthen the core of your business, driving growth and excellence.
[Explore](https://softwaremill.com/services/)
      * Expertise
        * [End-to-End Partnership](https://softwaremill.com/services/end-to-end-technology-partnership/)
        * [High-Performance Modern Backends](https://softwaremill.com/services/backend-development/)
        * [Next-Gen Systems Integration](https://softwaremill.com/services/next-gen-systems-integration/)
        * [LLM-enhanced Solutions](https://softwaremill.com/services/llm-enhanced-solutions/)
        * [Fractional CTO and Consulting](https://softwaremill.com/services/fractional-cto/)
        * [Cybersecurity](https://softwaremill.com/services/software-security-built-into-delivery/)
      * Operations
        * [Cloud Cost Reduction](https://softwaremill.com/services/cloud-cost-reduction-for-your-business/)
        * [DevOps as a Service](https://softwaremill.com/services/devops-as-a-service/)
        * [Platform Engineering](https://softwaremill.com/services/platform-engineering/)
        * [Software Audit & Consulting](https://softwaremill.com/services/software-development-audit-and-consulting/)
        * [Observability Services](https://softwaremill.com/services/observability-services/)
        * [Legacy Systems Migration](https://softwaremill.com/services/jvm-legacy-systems-migration/)
      * Technology Partnerships 
        * [Confluent](https://softwaremill.com/services/confluent-plus-partner/)
        * [Grafana](https://softwaremill.com/observability-with-grafana/)
        * [Redis](https://softwaremill.com/redis-for-speed-and-scale/)
        * [Aikido](https://softwaremill.com/services/software-security-with-aikido/)
        * [ScyllaDB](https://softwaremill.com/services/partner-with-scylladb-experts/)
      * [VirtusLab Group](https://virtuslab.com/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
        * [AI Implementation](https://virtuslab.com/expertise/gen-ai-software-development/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
        * [DevEx](https://virtuslab.com/expertise/developer-experience/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
### Why Choose Us
Looking for a technology partner? Here’s why leading companies trust us to deliver.
[Find out](https://softwaremill.com/why-choose-us/)
  * [Industries](https://softwaremill.com/) [Industries](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
    * ## How we work
Our method combines engineering excellence with open communication and trust. It’s a proven approach that keeps projects on track and innovation flowing.
[Discover](https://softwaremill.com/how-we-work/)
      * [FinTech](https://softwaremill.com/services/fintech-software-development/)
      * [MedTech](https://softwaremill.com/portfolio-clients/?industry=medtech)
      * [Entertainment](https://softwaremill.com/portfolio-clients/?industry=entertainment)
      * [Telco](https://softwaremill.com/portfolio-clients/?industry=telco)
      * [InsurTech](https://virtuslab.com/sectors/insurance/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
      * [Retail](https://virtuslab.com/sectors/retail-industry/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
### Portfolio
Read our success stories and find out how well-designed technology keeps our clients ahead of the curve.
[ Explore](https://softwaremill.com/portfolio-clients/)
  * [Technologies](https://softwaremill.com/) [Technologies](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
    * ## Technologies
Experience the difference that true engineering can make.
[Discover](https://softwaremill.com/technologies/)
      * [Backend](https://softwaremill.com/services/backend-development/)
        * [Java](https://softwaremill.com/services/java-development/)
        * [Scala](https://softwaremill.com/top-scala-experts/)
        * [Rust](https://softwaremill.com/services/rust-expertise/)
        * [Kotlin](https://softwaremill.com/services/kotlin-software-development/)
        * [TypeScript](https://softwaremill.com/services/reliable-development-with-typescript/)
        * [Node.js](https://softwaremill.com/services/modern-development-node-js/)
      * [Frontend](https://softwaremill.com/services/frontend-development-team/)
        * [React](https://softwaremill.com/services/professionally-crafted-applications-with-react)
        * [Angular](https://softwaremill.com/services/secure-scalable-applications-with-angular/)
        * [Vue](https://softwaremill.com/services/refined-app-development-with-vue)
      * Cloud
        * [Kubernetes](https://softwaremill.com/services/secure-and-reliable-kubernetes-solutions)
        * [Grafana](https://softwaremill.com/observability-with-grafana/)
        * [OpenTelemetry](https://softwaremill.com/services/opentelemetry/)
        * [AWS](https://softwaremill.com/services/top-notch-aws-services/)
        * [GCP](https://softwaremill.com/services/end-to-end-google-cloud-services/)
        * [Azure](https://softwaremill.com/services/azure-expertise/)
      * Data
        * [Apache Kafka](https://softwaremill.com/services/apache-kafka-services/)
        * [ScyllaDB](https://softwaremill.com/services/partner-with-scylladb-experts/)
        * [Apache Flink](https://softwaremill.com/services/apache-flink-services/)
        * [Apache Cassandra](https://softwaremill.com/services/apache-cassandra-services/)
  * [Company](https://softwaremill.com/) [Company](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
    * ## About us
Our motto: "Engineering. Excellence. Trust."
[Learn](https://softwaremill.com/about-us/)
      * [How we work](https://softwaremill.com/how-we-work/)
      * [Why choose us](https://softwaremill.com/why-choose-us/)
      * [Great place to work](https://softwaremill.com/great-place-to-work/)
      * [Meet the team](https://softwaremill.com/team/)
      * [FAQ](https://softwaremill.com/how-we-work#faq/)
      * Technology Partnerships
        * [Confluent ](https://softwaremill.com/services/confluent-plus-partner/)
        * [Grafana](https://softwaremill.com/observability-with-grafana/)
        * [Redis](https://softwaremill.com/redis-for-speed-and-scale/)
        * [Aikido](https://softwaremill.com/services/software-security-with-aikido/)
        * [ScyllaDB](https://softwaremill.com/services/partner-with-scylladb-experts/)
### Join Us
Join the best remote tech company awarded by Great Place to Work.
[Read more](https://softwaremill.com/join-us/)
  * [Technology Blog](https://softwaremill.com/blog/)[Technology Blog](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
  * [Resources](https://softwaremill.com/) [Resources](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)
    * ## Open Source
We create dev tools that a wide audience, including us, uses on a daily basis. Explore them!
[See our tools](https://softwaremill.com/open-source/)
      * Knowledge Base
        * [Technology Blog](https://softwaremill.com/blog/)
        * [Business Insights](https://softwaremill.com/business-insights/)
        * [Ebooks](https://softwaremill.com/resources/whitepapers/)
        * [Success Stories](https://softwaremill.com/portfolio-clients/)
        * [Youtube Channel](https://www.youtube.com/c/SoftwareMillCom)
        * [Tech Trends of the Decade](https://softwaremill.com/technology-trends/)
      * Our Tools
        * [Kafka Visualisation Tool](https://softwaremill.com/kafka-visualisation/)
        * [RX Playground](https://softwaremill.com/learn-reactive-programming-with-rx-playground/)
        * [LLM Tool](https://llm-demo.softwaremill.com/)
        * [Open Source](https://softwaremill.com/open-source/)
      * Newsletters
        * [Tapir Tech Update](https://softwaremill.com/tapir-tech-update/)
        * [Scala Times](https://scalatimes.com/)
        * [SoftwareMill News](http://eepurl.com/glzeA9)
      * Conferences
        * [Scalar Conference](https://www.scalar-conf.com/)
        * [Rustikon Conference](https://www.rustikon.dev/)
### Scalar Conference
Join the biggest Scala event in Central Europe. Est. 2014.
[Visit](https://www.scalar-conf.com/)
  * [Talk to us](https://softwaremill.com/contact/)[Talk to us](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)


  * Services 
  * Industries 
  * Technologies 
  * Company 
  * [Technology Blog](https://softwaremill.com/blog/)
  * Resources 
  * [Talk to us](https://softwaremill.com/contact/)


  * Expertise 
  * Operations 


  * Technology Partnerships 
  * VirtusLab Group ![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)


  * [Why Choose Us](https://softwaremill.com/why-choose-us/)


## Services overview
Partner with us to experience how the right technology choices can strengthen the core of your business, driving growth and excellence.
[Explore](https://softwaremill.com/services/)
  * [FinTech](https://softwaremill.com/services/fintech-software-development/)
  * [MedTech](https://softwaremill.com/portfolio-clients/?industry=medtech)
  * [Entertainment](https://softwaremill.com/portfolio-clients/?industry=entertainment)
  * [Telco](https://softwaremill.com/portfolio-clients/?industry=telco)


  * [InsurTech](https://virtuslab.com/sectors/insurance/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
  * [Retail](https://virtuslab.com/sectors/retail-industry/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)


  * [Portfolio](https://softwaremill.com/portfolio-clients/)


## How we work
Our method combines engineering excellence with open communication and trust. It’s a proven approach that keeps projects on track and innovation flowing.
[Discover](https://softwaremill.com/how-we-work/)
  * Backend 
  * Frontend 


  * Cloud 
  * Data 


  * [](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/)


## Technologies
Experience the difference that true engineering can make.
[Discover](https://softwaremill.com/technologies/)
  * [How we work](https://softwaremill.com/how-we-work/)
  * [Why choose us](https://softwaremill.com/why-choose-us/)
  * [Great place to work](https://softwaremill.com/great-place-to-work/)
  * [Meet the team](https://softwaremill.com/team/)
  * [FAQ](https://softwaremill.com/how-we-work#faq/)


  * Technology Partnerships 


  * [Join Us](https://softwaremill.com/join-us/)


## About us
Our motto: "Engineering. Excellence. Trust."
[Learn](https://softwaremill.com/about-us/)
  * Knowledge Base 
  * Our Tools 


  * Newsletters 
  * Conferences 


  * [Scalar Conference](https://www.scalar-conf.com/)


## Open Source
We create dev tools that a wide audience, including us, uses on a daily basis. Explore them!
[See our tools](https://softwaremill.com/open-source/)
  * [End-to-End Partnership](https://softwaremill.com/services/end-to-end-technology-partnership/)
  * [High-Performance Modern Backends](https://softwaremill.com/services/backend-development/)
  * [Next-Gen Systems Integration](https://softwaremill.com/services/next-gen-systems-integration/)
  * [LLM-enhanced Solutions](https://softwaremill.com/services/llm-enhanced-solutions/)
  * [Fractional CTO and Consulting](https://softwaremill.com/services/fractional-cto/)
  * [Cybersecurity](https://softwaremill.com/services/software-security-built-into-delivery/)


## Why Choose Us
Looking for a technology partner? Here’s why leading companies trust us to deliver.
[Find out](https://softwaremill.com/why-choose-us/)
  * [Cloud Cost Reduction](https://softwaremill.com/services/cloud-cost-reduction-for-your-business/)
  * [DevOps as a Service](https://softwaremill.com/services/devops-as-a-service/)
  * [Platform Engineering](https://softwaremill.com/services/platform-engineering/)
  * [Software Audit & Consulting](https://softwaremill.com/services/software-development-audit-and-consulting/)
  * [Observability Services](https://softwaremill.com/services/observability-services/)
  * [Legacy Systems Migration](https://softwaremill.com/services/jvm-legacy-systems-migration/)


## Why Choose Us
Looking for a technology partner? Here’s why leading companies trust us to deliver.
[Find out](https://softwaremill.com/why-choose-us/)
  * [Confluent](https://softwaremill.com/services/confluent-plus-partner/)
  * [Grafana](https://softwaremill.com/observability-with-grafana/)
  * [Redis](https://softwaremill.com/redis-for-speed-and-scale/)
  * [Aikido](https://softwaremill.com/services/software-security-with-aikido/)
  * [ScyllaDB](https://softwaremill.com/services/partner-with-scylladb-experts/)


## Why Choose Us
Looking for a technology partner? Here’s why leading companies trust us to deliver.
[Find out](https://softwaremill.com/why-choose-us/)
  * [VirtusLab Group](https://virtuslab.com/)
  * [AI Implementation](https://virtuslab.com/expertise/gen-ai-software-development/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)
  * [DevEx](https://virtuslab.com/expertise/developer-experience/)![Badge](https://softwaremill.com/user/themes/softwaremill/assets/uploads/virtuslab-logo.png?g-a7fe5a19)


## Why Choose Us
Looking for a technology partner? Here’s why leading companies trust us to deliver.
[Find out](https://softwaremill.com/why-choose-us/)
  * [Backend](https://softwaremill.com/services/backend-development/)
  * [Java](https://softwaremill.com/services/java-development/)
  * [Scala](https://softwaremill.com/top-scala-experts/)
  * [Rust](https://softwaremill.com/services/rust-expertise/)
  * [Kotlin](https://softwaremill.com/services/kotlin-software-development/)
  * [TypeScript](https://softwaremill.com/services/reliable-development-with-typescript/)
  * [Node.js](https://softwaremill.com/services/modern-development-node-js/)


  * [Frontend](https://softwaremill.com/services/frontend-development-team/)
  * [React](https://softwaremill.com/services/professionally-crafted-applications-with-react)
  * [Angular](https://softwaremill.com/services/secure-scalable-applications-with-angular/)
  * [Vue](https://softwaremill.com/services/refined-app-development-with-vue)


  * [Kubernetes](https://softwaremill.com/services/secure-and-reliable-kubernetes-solutions)
  * [Grafana](https://softwaremill.com/observability-with-grafana/)
  * [OpenTelemetry](https://softwaremill.com/services/opentelemetry/)
  * [AWS](https://softwaremill.com/services/top-notch-aws-services/)
  * [GCP](https://softwaremill.com/services/end-to-end-google-cloud-services/)
  * [Azure](https://softwaremill.com/services/azure-expertise/)


  * [Apache Kafka](https://softwaremill.com/services/apache-kafka-services/)
  * [ScyllaDB](https://softwaremill.com/services/partner-with-scylladb-experts/)
  * [Apache Flink](https://softwaremill.com/services/apache-flink-services/)
  * [Apache Cassandra](https://softwaremill.com/services/apache-cassandra-services/)


  * [Confluent ](https://softwaremill.com/services/confluent-plus-partner/)
  * [Grafana](https://softwaremill.com/observability-with-grafana/)
  * [Redis](https://softwaremill.com/redis-for-speed-and-scale/)
  * [Aikido](https://softwaremill.com/services/software-security-with-aikido/)
  * [ScyllaDB](https://softwaremill.com/services/partner-with-scylladb-experts/)


## Join Us
Join the best remote tech company awarded by Great Place to Work.
[Read more](https://softwaremill.com/join-us/)
  * [Technology Blog](https://softwaremill.com/blog/)
  * [Business Insights](https://softwaremill.com/business-insights/)
  * [Ebooks](https://softwaremill.com/resources/whitepapers/)
  * [Success Stories](https://softwaremill.com/portfolio-clients/)
  * [Youtube Channel](https://www.youtube.com/c/SoftwareMillCom)
  * [Tech Trends of the Decade](https://softwaremill.com/technology-trends/)


## Scalar Conference
Join the biggest Scala event in Central Europe. Est. 2014.
[Visit](https://www.scalar-conf.com/)
  * [Kafka Visualisation Tool](https://softwaremill.com/kafka-visualisation/)
  * [RX Playground](https://softwaremill.com/learn-reactive-programming-with-rx-playground/)
  * [LLM Tool](https://llm-demo.softwaremill.com/)
  * [Open Source](https://softwaremill.com/open-source/)


## Scalar Conference
Join the biggest Scala event in Central Europe. Est. 2014.
[Visit](https://www.scalar-conf.com/)
  * [Tapir Tech Update](https://softwaremill.com/tapir-tech-update/)
  * [Scala Times](https://scalatimes.com/)
  * [SoftwareMill News](http://eepurl.com/glzeA9)


## Scalar Conference
Join the biggest Scala event in Central Europe. Est. 2014.
[Visit](https://www.scalar-conf.com/)
  * [Scalar Conference](https://www.scalar-conf.com/)
  * [Rustikon Conference](https://www.rustikon.dev/)


## Scalar Conference
Join the biggest Scala event in Central Europe. Est. 2014.
[Visit](https://www.scalar-conf.com/)
#### Contents 
  * [Modern Full Stack Application Architecture Using Next.js 15+](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-modern-full-stack-application-architecture-using-nextjs-15)
  * [Introduction](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-introduction)
  * [Key features of Next.js](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-key-features-of-nextjs)
  * [Starting the project](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-starting-the-project)
  * [Project’s structure](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-projects-structure)
  * [Server Actions](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-server-actions)
  * [Server and Client Components](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-server-and-client-components)
  * [When to use Client Components:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-when-to-use-client-components)
  * [When to use Server Components:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-when-to-use-server-components)
  * [Package manager](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-package-manager)
  * [Linter and code formatter](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-linter-and-code-formatter)
  * [Styling](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-styling)
  * [Other noteworthy libraries include:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-other-noteworthy-libraries-include)
  * [Working with environment variables](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-working-with-environment-variables)
  * [Handling forms and validations](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-handling-forms-and-validations)
  * [Testing](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-testing)
  * [Authentication](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-authentication)
  * [Key features of Auth.js include:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-key-features-of-authjs-include)
  * [Database integration](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-database-integration)
  * [Docker containerization](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-docker-containerization)
  * [Deployment](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-deployment)
  * [Next.js can, therefore, be deployed:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-nextjs-can-therefore-be-deployed)
  * [Summary](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-summary)


#### Contents 
  * [Modern Full Stack Application Architecture Using Next.js 15+](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-modern-full-stack-application-architecture-using-nextjs-15)
  * [Introduction](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-introduction)
  * [Key features of Next.js](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-key-features-of-nextjs)
  * [Starting the project](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-starting-the-project)
  * [Project’s structure](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-projects-structure)
  * [Server Actions](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-server-actions)
  * [Server and Client Components](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-server-and-client-components)
  * [When to use Client Components:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-when-to-use-client-components)
  * [When to use Server Components:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-when-to-use-server-components)
  * [Package manager](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-package-manager)
  * [Linter and code formatter](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-linter-and-code-formatter)
  * [Styling](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-styling)
  * [Other noteworthy libraries include:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-other-noteworthy-libraries-include)
  * [Working with environment variables](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-working-with-environment-variables)
  * [Handling forms and validations](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-handling-forms-and-validations)
  * [Testing](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-testing)
  * [Authentication](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-authentication)
  * [Key features of Auth.js include:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-key-features-of-authjs-include)
  * [Database integration](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-database-integration)
  * [Docker containerization](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-docker-containerization)
  * [Deployment](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-deployment)
  * [Next.js can, therefore, be deployed:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-nextjs-can-therefore-be-deployed)
  * [Summary](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-summary)


# Modern Full Stack Application Architecture Using Next.js 15+
  * [Architecture](https://softwaremill.com/blog/?tag=architecture)
  * [Full stack](https://softwaremill.com/blog/?tag=full%20stack)
  * [React](https://softwaremill.com/blog/?tag=react)
  * [frameworks](https://softwaremill.com/blog/?tag=frameworks)
  * [Next.Js](https://softwaremill.com/blog/?tag=next.js)


[](https://softwaremill.com/blog/?author=Bartosz%20Butrym)
[Bartosz Butrym](https://softwaremill.com/blog/?author=Bartosz%20Butrym)
  * [](https://pl.linkedin.com/in/bartosz-butrym-web-development)
  * [](https://github.com/BartekButrym)


25 Jun 2025. 21 minutes read 
![Modern Full Stack Application Architecture Using Next.js 15+ featured image](https://softwaremill.com/user/pages/blog/303.modern-full-stack-application-architecture-using-next-js-15/zxvgloz5c6bgokv.jpg?g-a7fe5a19)
The React library has been popular in the frontend world for many years. It allows developers to build interactive user interfaces with reusable components that can be composed together. This modular approach makes the application scalable and easy to maintain.
As a library, React allows developers to select additional tools, such as routing, state management, data fetching, caching, or page rendering strategies. This flexible approach gives a lot of freedom. Yet, in practice, it boils down to making architectural decisions, such as how to structure folders and files, what naming conventions to adopt, how to secure the application at the SSR level, what approach to take for SEO, or, finally, how to take care of the developer experience. Developers must, therefore, spend time configuring tools and reinventing solutions for typical application requirements.
## Introduction
Among frameworks that offer such configuration and tools “out of the box”, Next.js is dominant. Currently, it is the most mature framework and, therefore, a fairly obvious choice, especially for [React developers](https://softwaremill.com/services/professionally-crafted-applications-with-react/) or ones who want to build their applications in the React ecosystem.
Next.js prioritizes server-side rendering (SSR) as its primary rendering technique. It also enables the use of static-site generation (SSG), incremental static regeneration (ISR), and client-side rendering (CSR). In addition, it provides React Server Components (RSC) and React Server Functions (RSF) as basic architectural elements. Moreover, Next.js allows to mix and match these rendering techniques; for example, a landing page can use SSG, while an application with authentication (dashboard) can use SSR.
React itself allows the creation of applications that run only on the client side. So, if the backend is needed for it (for example, for handling database queries, or authentication), it needs to be built separately and integrated with the React application. Next.js, on the other hand, enables the development of full-stack applications. It allows the developer to focus on both the frontend and the backend in one framework.
## Key features of Next.js
  1. **SSR** - built-in support for rendering pages on the server, improving performance and SEO
  2. **SSG** - support for static site generation, where pages are generated at compile time and served as static HTML files for faster loading and reduced server load
  3. **Automatic code splitting** - Next.js splits code into smaller and more manageable chunks, optimizing performance and loading time
  4. **CSS support** - support for various CSS solutions including CSS modules, CSS-in-JS libraries, global CSS styles, providing flexibility in application styling
  5. **Data fetching** - support for various methods of fetching data at compile time or at request time
  6. **Routing** - is greatly simplified due to automatic route generation based on file structure and page directories
  7. **Image optimization** - automatic optimization to ensure optimal loading performance by resizing and compressing images
  8. **Built-in CSS and JavaScript bundling** - automatically optimizes and bundles CSS and JS for more efficient loading
  9. **API proxying** - allows to create API routes that can serve as proxies for third-party APIs, supporting fetching data and security
  10. **Internationalization support** - Next.js provides tools and libraries for multi-language support


Considering the indicated features and advantages of Next.js, it is worth considering in which cases it is justified to use this framework instead of pure React. Next.js will, therefore, be useful for content-rich websites, i.e., blogs, or e-commerce, where at the same time SEO plays an important role. Next.js can significantly improve the performance of applications, resulting in the user not needing to fetch and run a lot of JS on the device, which is important, especially on slower devices or slower networks.
Thus, staying with pure React will be more suitable in situations where we are dealing with:
  * Microservices architecture, or there is logic heavily based on the backend
  * An application that relies heavily on real-time updates
  * Highly customized user interface such as animations, interactions, and complex layouts


We are past the introduction, so it is time to get to specifics. I will present the remaining concepts a developer should consider when building an application in Next.js by scaffolding and configuring the application to make CRUD operations on articles, including authentication.
## Starting the project
In the terminal:

```
npx create-next-app@latest

```

After running this command, we answer several prompts, and soon after all requirements will be automatically configured.
![starting%20the%20project%20prompts%20to%20answer](https://softwaremill.com/user/pages/blog/303.modern-full-stack-application-architecture-using-next-js-15/starting%20the%20project%20prompts%20to%20answer.png?g-a7fe5a19)
## Project’s structure
One of the questions concerns the choice of router. Next.js has two types of them:
  1. **App Router** - a newer router that supports new React features like Server Components and Server Actions,
  2. **Pages Router** - uses a file-system router to map each file to a route. Before version 13, it was the main way to create routes. It is still supported in newer versions.


Before Next.js introduced App Router, building in-app routing was based on Pages Router. In essence, it used React Router built into Next.js to handle navigation between pages automatically.
The Pages Router technique boils down to creating .js or .ts files in the pages directory, and Next.js will automatically create sub-pages of the application from them. For example, creating such a structure: pages/users.ts will generate a page at /users.
When a request is needed to be sent to the server in Pages Router, there are getServerSideProps or getStaticProps methods which can be used in the pages files.
The newer (from version 13) and recommended approach, App Router, gives developers more control and flexibility. App Router uses directories to define routes, allowing more advanced features like nested layouts.
Having an app/users/page.ts structure, this page is by default a server component (executed on the server), and the /users path becomes the route. In addition, it is possible to create layouts that will be shared on multiple routes, making it easier to maintain a consistent design and structure throughout the application.
In Next.js, reserved folders and file names have special meanings for the application. For example, for folders those will be: src, public, app, [folder], […folder]. For files, those will be for example, (with extensions .ts, .js, .tsx, .jsx, respectively): middleware, layout, page, loading, error. Their location in the project structure determines how pages and components are rendered and how the entire application behaves. 
For more detailed information, see: [project structure and organization](https://nextjs.org/docs/app/getting-started/project-structure)
## Server Actions
With the newer approach, server-side operations such as data fetching, form submission, and database interactions are done via **Server Actions**. In the App Router, all requests are server-side by default, which simplifies the process of communicating with the server before the page is rendered. Server Actions can be called in both **Server** and **Client Components**.
Server Actions are defined using the 'use server' directive. Next.js needs information that a function or all the exports in the file are to be treated as a Server Action. Without this directive, Next.js will not recognize whether a function is local (used only by server components) or whether it should be exported as Server Actions and called by the client. This is expected because Next.js allows hybrid mixing of Client and Server Components. And only functions that are marked with the 'use server' directive can be called by the client.
For example:

```
'use server';

import { eq } from 'drizzle-orm';
import db from '@/db';
import { articles } from '@/db/schema';

export async function getArticleBySlug(slug: string) {
  return await db.query.articles.findFirst({
    where: eq(articles.slug, slug),
  });
}

```

With the 'use server' directive, the getArticleBySlug function can be called in both:
**Server Component:**

```
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const data = await getArticleBySlug(slug);
  // ...
}

```

and **Client Component** (like passing this function as a callback to an event handler or in useEffect):
or:

```
'use client';

import { createArticle } from '@/lib/actions/article.actions';
// ...

export const ArticleForm = () => {
  return (
    <form action={createArticle}>
    {/* ... */}
    <button type='submit'>Create</button>
    </form>
  );
};

```

or:

```
'use client';

import { createArticle } from '@/lib/actions/article.actions';
// ...

export const ArticleForm = () => {
  return (
    <>
    {/* ... */}
    <button
        onClick={async () => {
        const formData = new FormData();
        formData.append('title', 'Article title');
        await createArticle(formData);
        }}
    >
        Create
    </button>
    </>
  );
};

```

If the 'use server' directive were omitted, Next.js could treat such a function as an ordinary helper function. Consequently the function would not be registered as a Server Action and could not be dynamically called from the Client Component.
The 'use server' directive could be placed at the top of an asynchronous function to mark that function as Server Action or at the top of a separate file to mark all exports of that file as Server Actions:

```
// Directive at the top of a separate file
'use server';

export async function createArticle(article: Article): Promise<ReturnType> {
  const parsedArticle = articleFormSchema.parse(article);

  if (!parsedArticle.success) return { message: 'Something went wrong' };

  return { message: 'Article created' };
}

// Directive at the top of an async function
export function Page() {
  const createArticle = async () => {
    'use server';
    // ...
  };

  return <form action={createArticle}>...</form>;
}

```

## Server and Client Components
Now let’s answer the question of when to use **Client** and **Server Components**.
By default, layouts and pages are Server Components. It allows sending server requests and rendering parts of the user interface on the server, optionally caching and passing the results to the client. In contrast, you can use Client Components when interaction or access to the browser API is needed. Creating a Client Component involves adding a 'use client' directive at the top of the file, above the imports. Once a file is marked with the 'use client' directive, all its imports and subcomponents are considered part of the client bundle. It also means there is no need to add a 'use client' directive to every component intended for the client.
### When to use Client Components:
  * Component state management and event handling (e.g. onClick, onChange)
  * Component lifecycle usage (e.g. useEffect)
  * Browser API access (localStorage, window, geolocation)
  * Custom hooks


### When to use Server Components:
  * Communicating with the database
  * Using API keys, tokens, other sensitive data that should not be accessible to the client
  * Limiting the amount of JavaScript sent to the browser
  * Improving [First Contentful Paint](https://web.dev/articles/fcp?hl=pl) and sending content progressively to the client


## Package manager
When initializing the project, we used npx command, which enables running Node.js packages from the npm registry on the fly, without installing them globally. As for the package manager, npm is the most commonly used one, mainly because it comes with every Node.js installation. However yarn, pnpm and bun are good alternatives, especially pnpm because of its better performance.
Should a need arise to create several applications that depend on each other or share a common set of components, the concept of monorepo is worth considering. For that, tools such as [Nx](https://nx.dev/) or [Turborepo](https://turborepo.com/) might work well.
## Linter and code formatter
Once the project has been initialized, it is worth taking care of a unified code style in the next step. The ESLint linter will help with this, as it enforces a certain code style and will point out an error in our IDE if specified rules are not followed.
A code formatter such as **Prettier** should be an addition to this. It can be configured so that the code will be formatted - according to specific rules - every time the file is saved. Prettier is not a replacement for ESLint, but it integrates well with it.
Install the package with:

```
npm install --save-dev eslint-config-prettier
```

Additionally, add information about the package to the ESLint configuration file (eslint.config.mjs).
By the way, remember to install a package for sorting import declarations according to a certain order. For example, third-party libraries will be at the top, followed by alias imports and finally relative imports, plus there are spaces between these groups, making this part of the file clean and readable:

```
npm install --save-dev @trivago/prettier-plugin-sort-imports
```

Then, add this package to the list of plugins in the .prettierrc.json file and specify the sorting rules:

```
{
  "importOrder": [
    "^(react|next?/?([a-zA-Z/]*))$",
    "<THIRD_PARTY_MODULES>",
    "^@/(.*)$",
    "^[./]"
  ],
  "importOrderSeparation": true,
  "importOrderSortSpecifiers": true,
  "plugins": ["@trivago/prettier-plugin-sort-imports"]
}
```

## Styling
The application is ready to use **Tailwind CSS**. Obviously, it is a matter of need and taste how the application will be styled. However, it is worth giving this framework a chance because of its approach to _utility classes_ , which are easily composable to build any project. What sets Tailwind CSS apart is that it does not give us ready-made components, but tools to build our own components.
The traditional approach used classes like: container, section-wrapper, accordion, heading-1, notification and so on. In Tailwind CSS, there are no such classes, but instead a set of simple tools, such as flex (which gives display: flex), w-screen (width: 100vw), text-lg (gives both font-size of a certain size and line-height of a certain size), and so on. I encourage you to read the [documentation](https://tailwindcss.com/docs/styling-with-utility-classes).
In various projects, one might come across various user interface styling requirements. These range from a defined system design, where custom components are required, to a more flexible approach, where one can rely on off-the-shelf solutions. One of the popular component libraries these days is [shadcn/ui](https://ui.shadcn.com/), which uses Tailwind primitive classes and creates ready-made components from them. Moreover, there is no need to install this library as a dependency in the project, but the code is dropped into the components directory, so we have access to the source code. The shadcn/ui components come with basic styling, making them easily configurable for application design.
### Other noteworthy libraries include:
  * [HeadlessUI](https://headlessui.com/)
  * [Chakra UI](https://chakra-ui.com/)
  * [Material UI](https://mui.com/material-ui/)
  * [HeroUI](https://www.heroui.com/)


## Working with environment variables
In the next step, we’ll take a look at configuring the work with environment variables. Next.js will detect the .env file in the project by default and load the environment variables set there, which are then available through process.env. However, it may happen that some variable is not set, or is not of a particular type, such as for the port number we would like it to be numbers and not strings. So, to work with environment variables in a type-safe way, along with automatic validation, it’s worth reaching for the [Zod library](https://zod.dev/), which allows us to define a schema for the required variables and validate them at application startup.
However, we can go a step further and use the [T3 Env library](https://env.t3.gg/docs/nextjs), which is built on top of Zod and is dedicated to managing environment variables in TypeScript/Next.js projects. In addition, it allows for the separation of client-side and server-side variables.
Installation:

```
npm install @t3-oss/env-nextjs zod

```

In the src/env/server.ts file, we create a scheme for server-specific environment variables:

```
import { createEnv } from "@t3-oss/env-nextjs";
import "dotenv/config";
import { z } from "zod";

export const env = createEnv({
  server: {
    NODE_ENV: z.enum(["development", "production"]),
    AUTH_GOOGLE_ID: z.string(),
    AUTH_GOOGLE_SECRET: z.string(),
    SESSION_SECRET: z.string(),
    DATABASE_URL: z.string().url(),
    CLOUDINARY_NAME: z.string(),
    CLOUDINARY_KEY: z.string(),
    CLOUDINARY_SECRET: z.string(),
  },
  onValidationError: (issues) => {
    console.error("❌ Invalid environment variables:", issues);
    process.exit(1);
  },
  emptyStringAsUndefined: true,
  experimental__runtimeEnv: process.env,
});

```

When needed, for the client I will want to have a separate src/env/client.ts file because to make the environment variable available in the browser, we need to add the NEXT _PUBLIC_ prefix to it.
It is recommended to import this file into next.config.ts file. This will ensure that the environment variables are checked at compile time. If any variable is missing, the application will not start at all.
To protect our application from using process.env directly in any place and to force the use of the created schema, we can install the [eslint-plugin-n plugin](https://github.com/eslint-community/eslint-plugin-n):

```
npm install –save-dev eslint-plugin-n
```

and use it in the eslint.config.mjs file:

```
const eslintConfig = [
  ...compat.config({
    plugins: ['n'],
    rules: {
    "n/no-process-env": ["error"]
    }
  })
];

```

With this, to refer to an environment variable, we must import the env constant defined before:

```
import { env } from “@/env/server”;
```

and use it:

```
env.DATABASE_URL
```

## Handling forms and validations
Forms are an indispensable part of the application. Working with them presents several challenges. We must consider client-side validation to provide users with immediate feedback, and server-side validation to ensure data integrity and form state management. It can quickly become complicated, particularly for multi-step forms or those with dynamic fields. Both the developer and user experience can be significantly improved when using specialized libraries that provide a structured approach to validation, reduce boilerplate, and help maintain a consistent user interface for error states and feedback.
[React Hook Form](https://react-hook-form.com/get-started) stands out as a performance-oriented form library. It is designed to minimize re-rendering and ensure flexibility. React Hook Form uses a hooks-first approach that reduces the complexity of the component tree and prevents unnecessary re-rendering.
Installation:

```
npm install react-hook-form
```

And the example:

```
import { zodResolver } from "@hookform/resolvers/zod";
import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";

// ...

const {
  register,
  handleSubmit,
  formState: { errors },
} = useForm({
  resolver: zodResolver(articleFormSchema),
  defaultValues: { ... },
});

  const onSubmit: SubmitHandler<z.infer<typeof articleFormSchema>> = async (
    values
  ) => { ... };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
        <div>
        <Input {...register("title", { required: true })} />
        <p>{errors.title?.message}</p>
        </div>
        {/* ... */}
    </form>
  );
};

```

React Hook Form works great with libraries for schema validation (in the above example, we used zodResolver). While discussing the topic of environment variables, I mentioned the Zod library. It will work perfectly in this case as well. It is a TypeScript-first library. It allows us to define validation schemes via a chain API interface that uses the TypeScript type inference system. One of the key advantages of Zod is its ability to be the single source of truth for both client-side and server-side validation logic. It means we can define a validation schema once and use it throughout the application.
Example:

```
import { z } from "zod";

export const signUpFormSchema = z
  .object({
    name: z.string().min(3, "Name must be at least 3 characters"),
    email: z.string().email("Invalid email address"),
    password: z.string().min(6, "Password must be at least 6 characters"),
    confirmPassword: z
    .string()
    .min(6, "Confirm password must be at least 6 characters"),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords don't match",
    path: ["confirmPassword"],
  });
```

On the other hand, for server-side validation, Zod provides a clean and simple way to validate request’s payload:

```
import { signUpFormSchema } from "@/validations/sign-up.validator";

export async function signup(_state: FormState, formData: FormData) {
  try {
    const user = signUpFormSchema.parse({
    name: formData.get("name"),
    email: formData.get("email"),
    password: formData.get("password"),
    confirmPassword: formData.get("confirmPassword"),
    });
    // ...
  } catch (error) {
    // ...
  }
}
```

## Testing
The foundation of testing is a framework such as [Vitest](https://vitest.dev) or [Jest](https://jestjs.io). It provides tools for running tests, an assertion library, spying, and mocking functions. A complementary tool will also be the [React Testing Library](https://testing-library.com/docs/react-testing-library/intro). It allows us to render React components and simulate events on HTML elements.
When it comes to choosing a test tool for E2E testing, [Playwright](https://playwright.dev) is recommended, while [Cypress](https://docs.cypress.io) is an alternative. These tools enable automating and simulating user interactions in the browser, ensuring that the application behaves as expected.
## Authentication
In the next step, let’s discuss authentication configuration. In general terms, authentication consists of the following concepts:
  * **Authentication:** is the process of verifying a user’s identity, thus verifying that the person trying to access an application is who they claim to be
  * **Session management:** tracking the authentication status of a user when requesting resources
  * **Authorization:** determining what resources and operations a user has access to once they have authenticated with an application


There are many ways to set up authentication in a project. There is an entire article on the [Next.js documentation page](https://nextjs.org/docs/app/guides/authentication) about how to do this from scratch, along with session management. However, it will not always be necessary to do it from scratch. So, ready-made solutions are recommended, if only for greater security and simplicity. Such libraries offer built-in authentication, session management, and authorization solutions, as well as additional features such as social login, multi-factor authentication, or role-based access control (RBAC). Here Next.js lists [compatible authentication and session management libraries](https://nextjs.org/docs/app/guides/authentication#auth-libraries).
For our application example, I will focus on [Auth.js](https://authjs.dev/getting-started/installation?framework=Next.js). It is a complete authentication solution built not only for Next.js but also compatible with other backend frameworks (before version 5, it was NextAuth, and it was only compatible with Next.js). It significantly reduces the time needed to implement secure authentication in a project.
### Key features of Auth.js include:
  * Built-in support for popular authentication providers (e.g. Google, GitHub, FaceBook)
  * Email/password authentication option
  * Comprehensive session management
  * Role-based access control
  * Security features like CSRF protection and http-only cookies


I will use two ways to authenticate:
  1. [Credentials provider](https://authjs.dev/getting-started/authentication/credentials) - support login using any credentials, such as email and password
  2. [Google provider](https://authjs.dev/getting-started/providers/google) - login using Google account


For session management, there are two types of sessions:
  1. Stateless - session data is stored in browser cookies. A cookie is sent with each request allowing verification on the server. This is a simpler method, but may be less secure (I will use this method - [JWT token](https://jwt.io/introduction)
  2. Database - session data is stored in the database, and the user’s browser receives only encrypted session ID. This method is more secure, but can be more complicated and use more server resources


Installation:

```
npm install next-auth@beta
```

Configuration in @/auth.ts file:

```
import NextAuth, { type User } from "next-auth";
import Credentials from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";

export const { handlers, signIn, signOut, auth } = NextAuth({
  session: {
    strategy: "jwt",
  },
  providers: [
    GoogleProvider,
    Credentials({
    credentials: {
        email: {},
        password: {},
    },
    authorize: async (credentials) => {
        // ...
    },
    }),
  ],
});
```

Then, to secure the route we can use:

```
import { auth } from '@/auth';

// ...

const session = await auth();

if (!session?.user) {
  return redirect('/sign-in');
}
```

Here you can find more details about [installing Auth.js](https://authjs.dev/getting-started/installation?framework=Next.js).
## Database integration
When developing any Next.js application, we often have to deal with a database ORM. Among several, there are two very popular ones: [Prisma](https://www.prisma.io) and [Drizzle ORM](https://orm.drizzle.team/docs/get-started).
I will opt for Drizzle ORM. Drizzle is distinguished by the fact that there is no need for code generation, which is characteristic of Prisma. In Prisma, a schema needs to be defined first and then run the npx prisma generate command (after any change in the schema file). This step generates the Prisma client (@prisma/client) and the model's type definition.
In Drizzle, the definition of a table in TypeScript is at the same time the definition of types ready for use, without the need to run separate commands to generate code. Thus, any schema change in Drizzle does not require an additional step to update the types and ORM client.
In addition, Drizzle has built-in helper functions that take the same table definitions and turn them into Zod validators (again, no additional code generation). 
Moreover, Drizzle has different adapters depending on what type of database is used in the project. PostgreSQL, MySQL, SQLite, Neon, Supabase, among others, are supported (you can [read more here](https://orm.drizzle.team/docs/overview)). For each of these types, there are many different ways to connect databases.
I want to connect to PostgreSQL, which runs inside a Docker container.
Installation:

```
npm i drizzle-orm postgres
npm i -D drizzle-kit
```

Driver initialization:

```
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import { env } from "@/env/server";
import * as schema from "./schema/index";

const queryClient = postgres(env.DATABASE_URL);
const db = drizzle({ client: queryClient, schema });

export default db;
```

Drizzle configuration (drizzle.config.ts):

```
import { defineConfig } from "drizzle-kit";
import { env } from "@/env/server";

export default defineConfig({
  out: "./src/db/migrations",
  schema: "./src/db/schema/index.ts",
  dialect: "postgresql",
  dbCredentials: {
    url: env.DATABASE_URL!,
  },
});
```

Sample schema (src/db/articles.ts):

```
import { relations } from "drizzle-orm";
import {
  boolean,
  index,
  pgTable,
  text,
  timestamp,
  uniqueIndex,
  uuid,
  varchar,
} from "drizzle-orm/pg-core";
import users from "./users";

const articles = pgTable(
  "article",
  {
    id: uuid().primaryKey().defaultRandom(),
    title: varchar("title", { length: 255 }),
    slug: varchar("slug", { length: 255 }).notNull(),
    content: text("content").notNull(),
    image: varchar("image", { length: 2048 }),
    isPublic: boolean("is_public").default(false),
    authorId: uuid("author_id")
    .notNull()
    .references(() => users.id, { onDelete: "cascade" }),
    createdAt: timestamp("created_at", { mode: "string" })
    .notNull()
    .defaultNow(),
    updatedAt: timestamp("updated_at", { mode: "string" })
    .notNull()
    .defaultNow(),
  },
  (table) => [
    uniqueIndex("slug_idx").on(table.slug),
    index("title_idx").on(table.title),
  ]
);

export const articlesRelations = relations(articles, ({ one }) => ({
  author: one(users, {
    fields: [articles.authorId],
    references: [users.id],
  }),
}));
```

This schema is imported in src/db/schema/index.ts file and plugged in drizzle.config.ts configuration. To query the database, let’s create a helper function in the src/lib/actions/article.actions.ts file:

```
"use server";

import db from "@/db";

// ...

export async function getArticleBySlug(slug: string) {
  const article = await db.query.articles.findFirst({
    where: eq(articles.slug, slug),
  });

  return article;
}
```

Now, this method can be called in the page file:

```
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = await getArticleBySlug(slug);
  // ...
}
```

## Docker containerization
To run a database in a Docker container, make sure to have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed, enabling easy container management. There are many ways to run a Docker container - for example, directly from the command line or pre-made images - but let’s follow a more structured way. Create a docker-compose.yml file and put all the necessary information (like PostgreSQL image, ports, and environment variables) in it:

```
services:
  database:
    image: postgres
    container_name: readium_postgres
    environment:
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres
    POSTGRES_DB: readium
    ports:
    - 5432:5432
    volumes:
    - dockerreadiumdata:/var/lib/postgresql/data
    healthcheck:
    test: ["CMD-SHELL", "pg_isready -U postgres -d readium"]
    interval: 10s
    timeout: 5s
    retries: 5
    restart: unless-stopped

volumes:
  dockerreadiumdata:
```

Thus, starting the database will come down to calling a command in the terminal:

```
docker compose up
```

## Deployment
Deploying and hosting a Next.js application is similar to deploying any other application, and much of it depends on the needs and decisions of developers and business decisions.
### Next.js can, therefore, be deployed:
  * As a Node.js server with any vendor supporting this environment
  * With any vendor supporting Docker containers, including container orchestration such as Kubernetes or a cloud provider
  * As a static export (for static pages or SPAs)
  * Or, last but not least, customized to run on different platforms supporting infrastructure


[Here you will find more information](https://nextjs.org/docs/app/getting-started/deploying).
## Summary
In this article, I took a step-by-step look at modern [full stack application architecture](https://softwaremill.com/services/frontend-development-team/) using Next.js 15 and such technologies as TypeScript, Server Actions, Server and Client Components, Auth.js, Tailwind CSS, Drizzle ORM, PostgreSQL, and Docker. I have shown not only how to connect these tools but also how to build a clear project structure, manage state and types, and ensure a clear division of logic between the frontend and backend.
I hope this knowledge will help you create robust and scalable applications. If you want to see the complete code of the application discussed in the article, you can find it in the [public repository on GitHub](https://github.com/BartoszButrymSoftwareMill/next-js-full-stack-modern-architecture).
[Blog Comments powered by Disqus.](http://disqus.com)
#### Contents
  * [Modern Full Stack Application Architecture Using Next.js 15+](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-modern-full-stack-application-architecture-using-nextjs-15)
  * [Introduction](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-introduction)
  * [Key features of Next.js](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-key-features-of-nextjs)
  * [Starting the project](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-starting-the-project)
  * [Project’s structure](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-projects-structure)
  * [Server Actions](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-server-actions)
  * [Server and Client Components](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-server-and-client-components)
  * [When to use Client Components:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-when-to-use-client-components)
  * [When to use Server Components:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-when-to-use-server-components)
  * [Package manager](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-package-manager)
  * [Linter and code formatter](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-linter-and-code-formatter)
  * [Styling](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-styling)
  * [Other noteworthy libraries include:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-other-noteworthy-libraries-include)
  * [Working with environment variables](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-working-with-environment-variables)
  * [Handling forms and validations](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-handling-forms-and-validations)
  * [Testing](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-testing)
  * [Authentication](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-authentication)
  * [Key features of Auth.js include:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-key-features-of-authjs-include)
  * [Database integration](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-database-integration)
  * [Docker containerization](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-docker-containerization)
  * [Deployment](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-deployment)
  * [Next.js can, therefore, be deployed:](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-nextjs-can-therefore-be-deployed)
  * [Summary](https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/#section-summary)


###  Latest from our Tech Blog 
[Read more](https://softwaremill.com/blog/)
[Adapter Pattern in Rust: Overcoming the Orphan Rule with Newtype and Extension Traits](https://softwaremill.com/adapter-pattern-in-rust-overcoming-the-orphan-rule-with-newtype-and-extension-traits/) Bartłomiej Kuras, 06 May 2026 
### SoftwareMill Sp. z o.o.
ul. Na Uboczu 8/87  
02-791 Warszawa  
Poland
Services 
  * [All services](https://softwaremill.com/services/)
  * [Backend ](https://softwaremill.com/services/backend-development/)
  * [Frontend](https://softwaremill.com/services/frontend-development-team/)
  * [Cybersecurity](https://softwaremill.com/services/software-security-built-into-delivery/)
  * [LLM Solutions](https://softwaremill.com/services/llm-enhanced-solutions/)
  * [Cloud](https://softwaremill.com/services/cloud-cost-reduction-for-your-business/)
  * [DevOps](https://softwaremill.com/services/devops-as-a-service/)


Technologies 
  * [All technologies](https://softwaremill.com/technologies/)
  * [Scala](https://softwaremill.com/top-scala-experts/)
  * [Java](https://softwaremill.com/services/java-development/)
  * [Rust](https://softwaremill.com/services/rust-expertise/)
  * [Apache Kafka](https://softwaremill.com/services/apache-kafka-services/)
  * [Kotlin](https://softwaremill.com/services/kotlin-software-development)
  * [Node.js](https://softwaremill.com/services/modern-development-node-js/)


Company 
  * [About us](https://softwaremill.com/about-us/)
  * [How we work](https://softwaremill.com/how-we-work/)
  * [Why choose us](https://softwaremill.com/why-choose-us/)
  * [Careers](https://softwaremill.com/join-us/)
  * [Great Place To Work](https://softwaremill.com/great-place-to-work/)
  * [Remote](https://softwaremill.com/company-remote/)
  * [VirtusLab Group](https://virtuslab.com/#virtuslab-group)


  * [ Contact us ](https://softwaremill.com/contact/)
  * [ Success stories ](https://softwaremill.com/portfolio-clients/)
  * [ Technology blog ](https://softwaremill.com/blog/)
  * [ Ebooks ](https://softwaremill.com/resources/whitepapers/)
  * [ Open source ](https://softwaremill.com/open-source/)
  * [ Newsletter ](https://softwaremill.us2.list-manage.com/subscribe?u=ba834c562d82d9aba5eaf90ba&id=49adef524d)
  * [ Privacy Policy ](https://softwaremill.com/privacy-policy/)


© 2026 SoftwareMill. All rights reserved.
  * [](https://x.com/softwaremill "X")
  * [](https://www.facebook.com/softwaremill "Facebook")
  * [](https://www.linkedin.com/company/808422 "LinkedIn")
  * [](https://github.com/softwaremill "Github")
  * [](https://www.youtube.com/c/SoftwareMillCom "YouTube")
  * [](https://instagram.com/softwaremill_vibes "Instagram")
  * [](http://www.slideshare.net/softwaremill "Slideshare")
  * [](https://clutch.co/profile/softwaremill "Clutch")
  * [](https://blog.softwaremill.com/?gi=854e7326b87a "Medium")
  * [](https://softwaremill.social/@softwaremill "Mastodon")
  * [](https://softwaremill.com/blog.rss "RSS")
  * [](https://bsky.app/profile/softwaremill.com "Bluesky")




## Source: https://windsurf.run/optimized-nextjs-typescript-best-practices-modern-ui-ux

[windsurf.run](https://windsurf.run/)
[Rules](https://windsurf.run/rules)[MCPs](https://windsurf.run/mcp)[Learn](https://windsurf.run/learn)[About](https://windsurf.run/about)Search
[Sign In](https://windsurf.run/login?next=/optimized-nextjs-typescript-best-practices-modern-ui-ux)
TypeScript23Python16Next.js12React12PHP8JavaScript6TailwindCSS5Laravel5C#4Web Development4Game Development4Expo4React Native4Flutter4Tailwind4Testing4Vite4Supabase4Rust3API3Meta-Prompt3Node.js3SvelteKit3SwiftUI3Swift3WordPress3Angular2Blockchain2html2Backend Development2Unity2Django2FastAPI2Microservices2Clean Architecture2GraphQL2Alpine.js2Go2Golang2Best Practices2CSS2Accessibility2ionic2cordova2angular2Java2Vue.js2Zod2Zustand2NestJs2Node2NuxtJS2Vue2Function2Ruby2Rails2Svelte2Terraform2UX2Vivado2FPGA2AL1Business Central1android1kotlin1Astro1Arduino-Framework1AutoHotkey1Blazor1ASP.NET Core1Cosmos1CosmWasm1IBC1bootstrap1Chrome Extension1Browser API1Convex1cpp1c++1Data Analyst1Jupyter1Deep Learning1PyTorch1Transformer1LLM1Diffusion1devops1kubernetes1azure1python1bash1ansible1REST API1.NET1Drupal1CMS1Elixir1Phoenix1elixir1phoenix1ex1Serverless1Fastify1typescript1Flask1Feature-first1Bloc1Gatsby1Ghost1Global1net/http1Observability1Security1HTML1Responsive Design1htmx1firebase1firestore1Spring1Spring-Boot1Quarkus1Jakarta EE1MicroProfile1GraalVM1Vert.x1JAX1Machine Learning1Julia1DataScience1Franework1Livewire1DaisyUI1Lua1Scripting1Manifest1Backend development1Critique1Reflection1Trajectory Analysis1WebShop1Acting1Tamagui1Monorepo1Solito1i18n1Stripe1@app/common1Redux1Viem v21Wagmi v21Standard.js1Radix UI1Shadcn UI1Payload CMS1MongoDB1Odoo1Enterprise1OnchainKit1Typescript1User Story1Open API1OAS1Pixi.js1Web1Mobile1Playwright1Prisma1ORM1Package Management1uv1Cybersecurity1Tooling1Tailwind CSS1three.js1React three fiber1Remix1RoboCorp1RSpec1async1channel1mpsc1Salesforce1SFDX1Force.com1sanity1cms1headless1Solana1Anchor1Web3.js1Metaplex1Solidity1Smart Contracts1Ethereum1Paraglide.js1COT1Tauri1Cross-Platform Desktop App1Technical Writing1Developer Content1Tutorials1Cloud1Infrastructure as Code1UI1Design1SystemVerilog1Timing Optimization1Synthesis1AXI1High-Performance1DMA1Web Scraping1Jina AI1WooCommerce1Shopify1Theme Development1Liquid1Performance1
[Submit ](https://github.com/pontusab/cursor.directory)
[`     You are an expert full-stack developer proficient in TypeScript, React, Next.js, and modern UI/UX frameworks (e.g., Tailwind CSS, Shadcn UI, Radix UI). Your task is to produce the most optimized and maintainable Next.js code, following best practices and adhering to the principles of clean code and robust architecture.      ### Objective     - Create a Next.js solution that is not only functional but also adheres to the best practices in performance, security, and maintainability.      ### Code Style and Structure     - Write concise, technical TypeScript code with accurate examples.     - Use functional and declarative programming patterns; avoid classes.     - Favor iteration and modularization over code duplication.     - Use descriptive variable names with auxiliary verbs (e.g., `isLoading`, `hasError`).     - Structure files with exported components, subcomponents, helpers, static content, and types.     - Use lowercase with dashes for directory names (e.g., `components/auth-wizard`).      ### Optimization and Best Practices     - Minimize the use of `'use client'`, `useEffect`, and `setState`; favor React Server Components (RSC) and Next.js SSR features.     - Implement dynamic imports for code splitting and optimization.     - Use responsive design with a mobile-first approach.     - Optimize images: use WebP format, include size data, implement lazy loading.      ### Error Handling and Validation     - Prioritize error handling and edge cases:       - Use early returns for error conditions.       - Implement guard clauses to handle preconditions and invalid states early.       - Use custom error types for consistent error handling.      ### UI and Styling     - Use modern UI frameworks (e.g., Tailwind CSS, Shadcn UI, Radix UI) for styling.     - Implement consistent design and responsive patterns across platforms.      ### State Management and Data Fetching     - Use modern state management solutions (e.g., Zustand, TanStack React Query) to handle global state and data fetching.     - Implement validation using Zod for schema validation.      ### Security and Performance     - Implement proper error handling, user input validation, and secure coding practices.     - Follow performance optimization techniques, such as reducing load times and improving rendering efficiency.      ### Testing and Documentation     - Write unit tests for components using Jest and React Testing Library.     - Provide clear and concise comments for complex logic.     - Use JSDoc comments for functions and components to improve IDE intellisense.      ### Methodology     1. **System 2 Thinking**: Approach the problem with analytical rigor. Break down the requirements into smaller, manageable parts and thoroughly consider each step before implementation.     2. **Tree of Thoughts**: Evaluate multiple possible solutions and their consequences. Use a structured approach to explore different paths and select the optimal one.     3. **Iterative Refinement**: Before finalizing the code, consider improvements, edge cases, and optimizations. Iterate through potential enhancements to ensure the final solution is robust.      **Process**:     1. **Deep Dive Analysis**: Begin by conducting a thorough analysis of the task at hand, considering the technical requirements and constraints.     2. **Planning**: Develop a clear plan that outlines the architectural structure and flow of the solution, using <PLANNING> tags if necessary.     3. **Implementation**: Implement the solution step-by-step, ensuring that each part adheres to the specified best practices.     4. **Review and Optimize**: Perform a review of the code, looking for areas of potential optimization and improvement.     5. **Finalization**: Finalize the code by ensuring it meets all requirements, is secure, and is performant.     `](https://windsurf.run/optimized-nextjs-typescript-best-practices-modern-ui-ux)
### MTZN
[![MTZN](https://e7.pngegg.com/pngimages/613/636/png-clipart-computer-icons-user-profile-male-avatar-avatar-heroes-logo.png)](https://mtzn.pl)
Next.jsTypeScript+6 more
[](https://github.com/pontusab/cursor.directory)


## Source: https://www.robinwieruch.de/react-tech-stack/

[The Road to Next — your interactive course for Next.js with React ](https://www.road-to-next.com/)
[](https://www.robinwieruch.de/)
  * [Hire Me](https://www.robinwieruch.de/work-with-me/)
  * [Blog](https://www.robinwieruch.de/blog/)
  * [About](https://www.robinwieruch.de/about/)
  * Courses 
[The Road to Next ](https://www.road-to-next.com/)[The Road to React ](https://www.roadtoreact.com/)


  * [Hire Me](https://www.robinwieruch.de/work-with-me/)
  * [Blog](https://www.robinwieruch.de/blog/)
  * [About](https://www.robinwieruch.de/about/)
  * Courses 
    * [The Road to Next ](https://www.road-to-next.com/)
    * [The Road to React ](https://www.roadtoreact.com/)


[React](https://www.robinwieruch.de/categories/react/)
# React Tech Stack [2025]
Robin Wieruch • December 9, 2024
There are always new technologies coming out in the React ecosystem. In this article, we will explore one (!) popular React tech stack for full-stack applications in 2025 which will allow you to create your own product (i.e. SaaS) or at least the MVP of it.
_Why would I write this guide in the first place?_ I have been working on many projects for several years as a freelance web developer and as a solo founder. Every year I re-evaluate the tech stack I use and try to keep up with the latest trends while still having an eye on the stability and maintainability of the project for the next years.
_To give some more context:_ I have been working on a SaaS as a founder for almost an entire year and the SaaS became profitable. I like the tech stack that I have chosen back then, but I would choose a different tech stack if I would start a new project today.
This article is a result of my research, experience and my work on a full-stack web development course that I worked on for the entire year of 2024 which reflects my choice of the tech stack.
[ Read More The Road to Next ](https://www.road-to-next.com/)
Let’s dive into the short but comprehensive list.
# React Tech Stack
**Next.js** is a framework on top of React. It is one of the most popular choices when building full-stack applications with React, because it comes with lots of features out of the box (e.g. routing, caching), several rendering strategies within the same application to optimize for different goals and all the recent features from React (e.g. Server Components and Server Functions) to connect your React application to the backend.
**Astro** would be my _optional_ choice to create a landing page for the product if you don’t leverage the Next.js project as one monolithic application which would also be able to serve static and dynamic pages. While Astro would lead you to using a subdomain for your application (e.g. app.example.com), it would allow you to create a fast landing page with a great developer experience where you can choose from a wide range of landing pages which would free your time to work more on your SaaS.
[ Read More How to start a React Project ](https://www.robinwieruch.de/react-starter/)
**Server Components** are not available in all React frameworks, but they are in Next. So I wanted to give them an extra mention, because they change how full-stack React applications are built. In there most basic form, they allow you to write components that execute on the server and therefore allow you to access the server (e.g. database).
**Server Functions** are another React feature enabled in Next.js that I would like to mention, because they give you the ability to execute server-side code from your React components by just calling a function. It behaves like a typed remote procedure call (RPC), but under the hood there is an API endpoint that is created for you.
**Server Actions** are a subset of Server Functions (mentioned earlier). There are a few libraries available that add a layer of abstraction to make them more user-friendly. Personally, I haven’t felt the need to use them (yet), as you can easily implement your own abstraction with just a few lines of code. However, if you’re looking for a ready-made solution, check out next-safe-actions or zsa.
[ Read More React as a full-stack framework ](https://www.robinwieruch.de/react-full-stack-framework/)
**Tailwind CSS** : Although it continues to divide opinions within the developer community, I believe Tailwind is the best choice today for rapid product development and maintaining CSS in the long term. From my own experience, and that of many of my students, once you get the hang of Tailwind after a week, it’s hard to imagine going back to traditional CSS approaches.
**Shadcn UI** : UI libraries come and go, but Shadcn UI has been trending for over a year now. It’s a popular choice that works seamlessly with Tailwind CSS and offers a refreshing approach to UI management with its versionless system. I’d say it’s a great choice for now, until the next big thing comes along or if everything starts to look too similar again.
**Lucide React** : Since this icon library already comes with Shadcn UI, I wouldn’t see a need to replace it with something else. Once there is another popular kid on the block, I would consider switching for the next project. There is no big buy-in with Lucide React.
[ Read More CSS Styling in React ](https://www.robinwieruch.de/react-css-styling/)
**TypeScript** : I think there is not much say about this choice. TypeScript became the industry standard for JavaScript projects and it is a great choice to have a better developer experience, less bugs and more maintainable code.
**Zod** : Is the industry standard for validation in React projects, because it aligns nicely with TypeScript. These days I am only using it for server-side validation (e.g. Server Actions) and keep the client-side forms lightweight with native HTML validation. This way there is no complexity in form components with any third-party form libraries.
[ Read More State in React ](https://www.robinwieruch.de/react-state/)
**nuqs** is my go-to solution for typed URL state (e.g. search, sort, pagination) in Next.js. If you are using another framework, this feature may be built-in or you may have to use another library. In any case, I think it’s important to have a solution for URL state.
**Zustand** is my _optional_ choice for client-side state management. However, I _rarely_ use client-side state these days because URL state, client-side data caching (e.g. React Query), and server-driven React applications (e.g. Server Components) have reduced the need for it in many cases.
**React Query** is my _optional_ solution for client-side data fetching whenever it is needed for more complex cases (e.g. infinite scrolling). However, when the project complexity is low, I would stick exclusively to Server Components.
[ Read More Data Fetching in React ](https://www.robinwieruch.de/react-fetching-data/)
**Prisma (ORM)** is always used as my ORM of choice. However, since there is always a hype for the latest trends, you could also replace it with Drizzle. I would stick with Prisma for now, because it is a stable choice and it is already used in many projects.
**Supabase (Database)** would be my choice for a database as a service. It gives you a Postgres database and many more features. Personally I only use their database, because I avoid the buy-in of their other features where I want to can keep my tech choice more flexible. For the database, I would only connect to it with Prisma and not use many of their features which would allow you to replace it any time with another database (e.g. Neon).
**Lucia (Authentication)** : These days I go with Lucia even though it is deprecated as a library. However, it is still used as a [learning resource](https://lucia-auth.com/) where it teaches the underlying concepts of authentication with libraries like Oslo, Argon2, and optionally Arctic. So you will end up with a hand rolled authentication system that is tailored to your needs instead of having a buy-in into third-party solutions like Clerk or Kinde.
**S3 (File Upload)** : Building your own file upload system with Amazon’s AWS S3, presigned URLs, and AWS IAM isn’t difficult, and it offers the flexibility to store files at the lowest cost. I wouldn’t recommend using any other third-party solution, as it’s a “implement once and forget” scenario. Most third-party services use the same API, so you can switch providers later if needed.
**Inngest (Queue)** : For my recent projects that required scaling the backend with more sophisticated task orchestration, I used [Inngest](https://www.inngest.com/). Personally, I rely on it for tasks that aren’t time-critical and can run in the background. It’s an excellent choice for a queue system that’s easy to set up and maintain.
**React Email + Resend** : While the former allows you to create email templates with React components, the latter is a great solution for sending emails. Previously I have used [Postmark](https://postmarkapp.com/) where you can use React Email as well, but I am quite happy with my switch to Resend.
**Vercel (Hosting)** : I have been using Vercel for several years. Back then it was called Zeit and their service was called Now. They offer a great solution for hosting full-stack applications, however, I can also see why people are hesitant to use it. If you are looking for self-hosted alternative, I would recommend using [Hetzner](https://www.hetzner.com/)/[DigitalOcean](https://m.do.co/c/fb27c90322f3) with [Coolify](https://coolify.io/).
[ Read More Libraries for React projects ](https://www.robinwieruch.de/react-libraries/)
**CloudFlare (Domain)** : I used different providers over the years, but I am pretty happy with CloudFlare to manage all of my domains these days. They offer a great UI and you can attach extra information to your DNS records which makes it easier to track your services.
**Stripe (Payment Gateway)** : I don’t have a hard recommendation for a payment gateway. I have used Stripe for several years and I am happy with it. However, I can see why people are hesitant to use it, because even though they have a great documentation and a great API, they also increase their API and feature surface which can be overwhelming.
[ Read More Form Validation in React ](https://www.robinwieruch.de/react-form-validation/)
**Testing & Tooling**: I don’t have any hard recommendations for testing and tooling. I’d say these days a mix of React Testing Library and Cypress/Playwright is a good choice for testing. For tooling, I would recommend using ESLint (perhaps Biome in the future) and Prettier. Even though I’d hope for a good Storybook alternative, it is still my go-to solution for UI documentation. In addition I am using [tsx](https://www.npmjs.com/package/tsx) for executing TypeScript (e.g. database seeding) from the terminal.
* * *
Essentially this is the tech stack that I would choose today for a new project and which I teach for a comprehensive full-stack application in [The Road to Next](https://www.road-to-next.com/). I hope this article helps you to make a decision for your next project.
## Never Miss an Article
Join 50,000+ developers getting weekly insights on full-stack engineering and AI.
AI Agentic UI Architecture React Next.js TypeScript Node.js Full-Stack Monorepos Product Engineering
[Subscribe on Substack ](https://rwieruch.substack.com/)
High signal, low noise. Unsubscribe at any time.
[Robin Wieruch](https://www.robinwieruch.de/)
Freelance Full-Stack Software Engineer for AI and Product. Based in Berlin, Germany.
  * [Blog](https://www.robinwieruch.de/blog/)
  * [About](https://www.robinwieruch.de/about/)
  * [Hire Me](https://www.robinwieruch.de/work-with-me/)
  * [Legal](https://www.robinwieruch.de/legal/)
  * [RSS](https://www.robinwieruch.de/index.xml)


[](https://twitter.com/rwieruch)[](https://github.com/rwieruch)[](https://www.linkedin.com/in/robin-wieruch-971933a6/)
© 2026 Robin Wieruch. All rights reserved.
Featured Course
## The Road to Next
Full-stack Next.js + React course. Learn to build production-ready applications from scratch.
[Check it out ](https://www.road-to-next.com/)No thanks


## Source: https://medium.com/@gvsakhil143/best-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5

[Sitemap](https://medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)
# Best Practices to follow while reviewing a Frontend PR (Pull Request) — Javascript, Typescript
[![Gvs Akhil](https://miro.medium.com/v2/resize:fill:32:32/2*U0t2G1yrrczhufaZLBO9ug.jpeg)](https://medium.com/@gvsakhil143?source=post_page---byline--64e297993fa5---------------------------------------)
[Gvs Akhil](https://medium.com/@gvsakhil143?source=post_page---byline--64e297993fa5---------------------------------------)
Follow
3 min read
·
Jul 31, 2023
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F64e297993fa5&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&user=Gvs+Akhil&userId=e7bd17272de1&source=---header_actions--64e297993fa5---------------------clap_footer------------------)
2
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F64e297993fa5&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&source=---header_actions--64e297993fa5---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D64e297993fa5&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&source=---header_actions--64e297993fa5---------------------post_audio_button------------------)
Share
Press enter or click to view image in full size
![Pull Request Review](https://miro.medium.com/v2/resize:fit:1000/1*UMox-gqLtbhR3edgXFxorA.png)
Code collaboration lies at the heart of modern software development, and Pull Requests (PR’s) have become an indispensable part of the process. When a developer or a team completes a new feature or fixes a bug, they submit a PR for others to review before merging it into the main codebase. However, the effectiveness of a PR review largely depends on the approach taken by the reviewers. In this article, we will explore a set of best practices that can help reviewers provide valuable feedback, foster a constructive review environment, and ultimately enhance the overall development process. Let’s dive into the essential best practices to follow while reviewing a PR.
We are using Azure Boards and Azure Pull Requests. I follow these points to make sure the best code runs on the server:
  1. _Never compare reusable values with strings, try using an enum_


**Wrong:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*vcO066ZAc25JZdEK9yGKUg.png)
**Correct:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*FPgI_TrNbcEarPYj-zowhA.png)
**Reason:** If you are not using an enum, devs use Active, active or activ which leads to many errors during runtime.
_Note: If you are using Javascript you can still use Object.freeze or export some const object instead of using an enum as enum is not supported in javascript_
2. _Never encourage inline styling_ — The inline styling concept might not help you to build the best React components in your app. If you’re planning to build a very performant, scalable, and rich application inline styling is not the right option for you.
## Get Gvs Akhil’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
**Wrong:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*5hN8mw5vjX_AXSXt8pukCQ.png)
**Correct:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*QkEs_2kwgBrtnBcYeaz_Aw.png)
3. _Make use of scss when we use some reusable colours —_ This will help us to change the colors all over the application at once if designs got updated or if we are dealing with dark and light themes.
**Wrong:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*-Y1EshDcp1msBkzKO4APUQ.png)
**Correct:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*xmPUqtrhoceSUPDx9Laq7Q.png)
**variables.scss file:**
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*PMFVVDGd2DNHsKQupF_ePA.png)
4. _Peer Reviews:_ Peer reviews are best for double confirmation on whats good or bad and also helps teammates to understand others code or new ways of writing it.
  * We ask teammates to do a peer review in between themselves and if anything needs to be corrected they add comments and make sure all comments are fixed by developer.
  * Once all looks good we send it to the Team Lead where he checks the code for second time and approves the PR if all looks good or else same process of adding comments and resolving it goes on.


These are only a few that we follow while reviewing PR’s for frontend. We have a very big checklist to check which I will be adding as part of my another post. Thanks for your time, hope you have learnt something new.
**_Happy Coding :)_**
[Angular](https://medium.com/tag/angular?source=post_page-----64e297993fa5---------------------------------------)
[React](https://medium.com/tag/react?source=post_page-----64e297993fa5---------------------------------------)
[Pull Request](https://medium.com/tag/pull-request?source=post_page-----64e297993fa5---------------------------------------)
[Pull Request Reviews](https://medium.com/tag/pull-request-reviews?source=post_page-----64e297993fa5---------------------------------------)
[Vue](https://medium.com/tag/vue?source=post_page-----64e297993fa5---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F64e297993fa5&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&user=Gvs+Akhil&userId=e7bd17272de1&source=---footer_actions--64e297993fa5---------------------clap_footer------------------)
2
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F64e297993fa5&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&user=Gvs+Akhil&userId=e7bd17272de1&source=---footer_actions--64e297993fa5---------------------clap_footer------------------)
2
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F64e297993fa5&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gvsakhil143%2Fbest-practices-to-follow-while-reviewing-a-frontend-pr-pull-request-javascript-typescript-64e297993fa5&source=---footer_actions--64e297993fa5---------------------bookmark_footer------------------)
[![Gvs Akhil](https://miro.medium.com/v2/resize:fill:48:48/2*U0t2G1yrrczhufaZLBO9ug.jpeg)](https://medium.com/@gvsakhil143?source=post_page---post_author_info--64e297993fa5---------------------------------------)
[![Gvs Akhil](https://miro.medium.com/v2/resize:fill:64:64/2*U0t2G1yrrczhufaZLBO9ug.jpeg)](https://medium.com/@gvsakhil143?source=post_page---post_author_info--64e297993fa5---------------------------------------)
Follow
## [Written by Gvs Akhil](https://medium.com/@gvsakhil143?source=post_page---post_author_info--64e297993fa5---------------------------------------)
[18 followers](https://medium.com/@gvsakhil143/followers?source=post_page---post_author_info--64e297993fa5---------------------------------------)
·[21 following](https://medium.com/@gvsakhil143/following?source=post_page---post_author_info--64e297993fa5---------------------------------------)
Full Stack developer working as a Tech Lead in Godomo. I have expertise around Angular, NextJS, Flutter, NodeJS, .Net, Python, Mongodb, MySQL, Azure, AWS
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----64e297993fa5---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----64e297993fa5---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----64e297993fa5---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----64e297993fa5---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----64e297993fa5---------------------------------------)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----64e297993fa5---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----64e297993fa5---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----64e297993fa5---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----64e297993fa5---------------------------------------)
To make Medium work, we log user data. By using Medium, you agree to our [Privacy Policy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9), including cookie policy.


## Primary Source: TS Style Guide



## Primary Source: TS Dev Style Guide



## Primary Source: TS Handbook



## Primary Source: AWS Guidelines



