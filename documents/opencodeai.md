# opencode.ai

## Table of Contents

- [Intro](#intro)
  - [Install](#install)
  - [Configure](#configure)
  - [Usage](#usage)
  - [Customize](#customize)
- [Config](#config)
  - [Format](#format)
  - [OpenCode Zen](#opencode-zen)
  - [Custom provider](#custom-provider)
  - [Pricing](#pricing)
  - [Deployment](#deployment)
  - [FAQ](#faq)
- [Troubleshooting](#troubleshooting)
  - [Getting help](#getting-help)
  - [Common issues](#common-issues)
- [Migrating to 1.0](#migrating-to-10)
  - [Upgrading](#upgrading)
  - [UX changes](#ux-changes)
  - [Breaking changes](#breaking-changes)
- [TUI](#tui)
  - [Bash commands](#bash-commands)
  - [Configure](#configure-1)
  - [Commands](#commands)
  - [Global Flags](#global-flags)
- [IDE](#ide)
  - [Usage](#usage-1)
  - [Installation](#installation)
- [Zen](#zen)
  - [Background](#background)
  - [How it works](#how-it-works)
  - [Endpoints](#endpoints)
  - [Privacy](#privacy)
  - [For enterprises](#for-enterprises)
- [GitHub](#github)
  - [Features](#features)
  - [Installation](#installation-1)
  - [Configuration](#configuration)
  - [Examples](#examples)
  - [Custom tools](#custom-tools)
  - [MCP servers](#mcp-servers-1)
  - [Internals](#internals)
  - [Types](#types)
  - [Precedence](#precedence)
  - [Custom Instructions](#custom-instructions)
- [External File Loading](#external-file-loading)
- [Development Guidelines](#development-guidelines)
- [General Guidelines](#general-guidelines)
  - [Configure](#configure-2)
  - [Options](#options)
  - [Create agents](#create-agents)
  - [Recommended models](#recommended-models)
  - [Set a default](#set-a-default)
- [Themes](#themes-2)
  - [Terminal requirements](#terminal-requirements)
  - [Built-in themes](#built-in-themes)
  - [System theme](#system-theme)
  - [Using a theme](#using-a-theme)
- [Keybinds](#keybinds-1)
- [Commands](#commands-1)
  - [Options](#options-1)
  - [Tools](#tools-2)
  - [Agents](#agents)
- [LSP Servers](#lsp-servers)
  - [Built-in](#built-in)
  - [How It Works](#how-it-works-1)
  - [Configure](#configure-3)
  - [Additional Information](#additional-information)
- [MCP servers](#mcp-servers-2)
  - [Caveats](#caveats)
  - [Configure](#configure-4)
  - [Examples](#examples-1)
  - [Examples](#examples-2)
- [SDK](#sdk)
  - [Install](#install-2)
  - [Config](#config-1)
  - [Types](#types-1)
  - [APIs](#apis)
  - [Spec](#spec)

<a name="intro"></a>

## Intro

Get started with OpenCode.

[**OpenCode**](/) is an AI coding agent built for the terminal.

![OpenCode TUI with the opencode theme](/docs/_astro/screenshot.Bs5D4atL_ZvsvFu.webp)

Let’s get started.

---

<a name="prerequisites"></a>

##### [Prerequisites](#prerequisites)

To use OpenCode, you’ll need:

1. A modern terminal emulator like:

   - [WezTerm](https://wezterm.org), cross-platform
   - [Alacritty](https://alacritty.org), cross-platform
   - [Ghostty](https://ghostty.org), Linux and macOS
   - [Kitty](https://sw.kovidgoyal.net/kitty/), Linux and macOS
2. API keys for the LLM providers you want to use.

---

<a name="install"></a>

### [Install](#install)

The easiest way to install OpenCode is through the install script.

Terminal window

```auto
curl -fsSL https://opencode.ai/install | bash
```

You can also install it with the following commands:

- **Using Node.js**

  - [npm](#tab-panel-0)
  - [Bun](#tab-panel-1)
  - [pnpm](#tab-panel-2)
  - [Yarn](#tab-panel-3)

  Terminal window

  ```auto
  npm install -g opencode-ai
  ```

  Terminal window

  ```auto
  bun install -g opencode-ai
  ```

  Terminal window

  ```auto
  pnpm install -g opencode-ai
  ```

  Terminal window

  ```auto
  yarn global add opencode-ai
  ```

- **Using Homebrew on macOS and Linux**

  Terminal window

  ```auto
  brew install opencode
  ```

- **Using Paru on Arch Linux**

  Terminal window

  ```auto
  paru -S opencode-bin
  ```

##### [Windows](#windows)

- **Using Chocolatey**

  Terminal window

  ```auto
  choco install opencode
  ```

- **Using Scoop**

  Terminal window

  ```auto
  scoop bucket add extras



  scoop install extras/opencode
  ```

- **Using NPM**

  Terminal window

  ```auto
  npm install -g opencode-ai
  ```

- **Using Mise**

  Terminal window

  ```auto
  mise use --pin -g ubi:sst/opencode
  ```

- **Using Docker**

  Terminal window

  ```auto
  docker run -it --rm ghcr.io/sst/opencode
  ```

Support for installing OpenCode on Windows using Bun is currently in progress.

You can also grab the binary from the [Releases](https://github.com/sst/opencode/releases).

---

<a name="configure"></a>

### [Configure](#configure)

With OpenCode you can use any LLM provider by configuring their API keys.

If you are new to using LLM providers, we recommend using [OpenCode Zen](/docs/zen).
It’s a curated list of models that have been tested and verified by the OpenCode
team.

1. Run `opencode auth login`, select opencode, and head to [opencode.ai/auth](https://opencode.ai/auth).
2. Sign in, add your billing details, and copy your API key.
3. Paste your API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  opencode



   │



   ●  Create an api key at https://opencode.ai/auth



   │



   ◆  Enter your API key



   │  _



   └
   ```

Alternatively, you can select one of the other providers. [Learn more](/docs/providers#directory).

---

### [Initialize](#initialize)

Now that you’ve configured a provider, you can navigate to a project that
you want to work on.

Terminal window

```auto
cd /path/to/project
```

And run OpenCode.

Terminal window

```auto
opencode
```

Next, initialize OpenCode for the project by running the following command.

```auto
/init
```

This will get OpenCode to analyze your project and create an `AGENTS.md` file in
the project root.

Tip

You should commit your project’s `AGENTS.md` file to Git.

This helps OpenCode understand the project structure and the coding patterns
used.

---

<a name="usage"></a>

### [Usage](#usage)

You are now ready to use OpenCode to work on your project. Feel free to ask it
anything!

If you are new to using an AI coding agent, here are some examples that might
help.

---

<a name="ask-questions"></a>

#### [Ask questions](#ask-questions)

You can ask OpenCode to explain the codebase to you.

Tip

Use the `@` key to fuzzy search for files in the project.

```auto
How is authentication handled in @packages/functions/src/api/index.ts
```

This is helpful if there’s a part of the codebase that you didn’t work on.

---

#### [Add features](#add-features)

You can ask OpenCode to add new features to your project. Though we first recommend asking it to create a plan.

1. **Create a plan**

   OpenCode has a *Plan mode* that disables its ability to make changes and
   instead suggest *how* it’ll implement the feature.

   Switch to it using the **Tab** key. You’ll see an indicator for this in the lower right corner.

   ```auto
   <TAB>
   ```

   Now let’s describe what we want it to do.

   ```auto
   When a user deletes a note, we'd like to flag it as deleted in the database.



   Then create a screen that shows all the recently deleted notes.



   From this screen, the user can undelete a note or permanently delete it.
   ```

   You want to give OpenCode enough details to understand what you want. It helps
   to talk to it like you are talking to a junior developer on your team.

   Tip

   Give OpenCode plenty of context and examples to help it understand what you
   want.
2. **Iterate on the plan**

   Once it gives you a plan, you can give it feedback or add more details.

   ```auto
   We'd like to design this new screen using a design I've used before.



   [Image #1] Take a look at this image and use it as a reference.
   ```

   Tip

   Drag and drop images into the terminal to add them to the prompt.

   OpenCode can scan any images you give it and add them to the prompt. You can
   do this by dragging and dropping an image into the terminal.
3. **Build the feature**

   Once you feel comfortable with the plan, switch back to *Build mode* by
   hitting the **Tab** key again.

   ```auto
   <TAB>
   ```

   And asking it to make the changes.

   ```auto
   Sounds good! Go ahead and make the changes.
   ```

---

<a name="make-changes"></a>

#### [Make changes](#make-changes)

For more straightforward changes, you can ask OpenCode to directly build it
without having to review the plan first.

```auto
We need to add authentication to the /settings route. Take a look at how this is



handled in the /notes route in @packages/functions/src/notes.ts and implement



the same logic in @packages/functions/src/settings.ts
```

You want to make sure you provide a good amount of detail so OpenCode makes the right
changes.

---

#### [Undo changes](#undo-changes)

Let’s say you ask OpenCode to make some changes.

```auto
Can you refactor the function in @packages/functions/src/api/index.ts?
```

But you realize that it is not what you wanted. You **can undo** the changes
using the `/undo` command.

```auto
/undo
```

OpenCode will now revert the changes you made and show your original message
again.

```auto
Can you refactor the function in @packages/functions/src/api/index.ts?
```

From here you can tweak the prompt and ask OpenCode to try again.

Tip

You can run `/undo` multiple times to undo multiple changes.

Or you **can redo** the changes using the `/redo` command.

```auto
/redo
```

---

### [Share](#share)

The conversations that you have with OpenCode can be [shared with your
team](/docs/share).

```auto
/share
```

This will create a link to the current conversation and copy it to your clipboard.

Note

Conversations are not shared by default.

Here’s an [example conversation](https://opencode.ai/s/4XP1fce5) with OpenCode.

---

<a name="customize"></a>

### [Customize](#customize)

And that’s it! You are now a pro at using OpenCode.

To make it your own, we recommend [picking a theme](/docs/themes), [customizing the keybinds](/docs/keybinds), [configuring code formatters](/docs/formatters), [creating custom commands](/docs/commands), or playing around with the [OpenCode config](/docs/config).

---

<a name="config"></a>

## Config

Using the OpenCode JSON config.

You can configure OpenCode using a JSON config file.

---

<a name="format"></a>

### [Format](#format)

OpenCode supports both **JSON** and **JSONC** (JSON with Comments) formats.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



// Theme configuration



"theme": "opencode",



"model": "anthropic/claude-sonnet-4-5",



"autoupdate": true,



}
```

---

### [Locations](#locations)

You can place your config in a couple of different locations and they have a
different order of precedence.

Config Merging

Configuration files are **merged together**, not replaced. Settings from all config locations are combined using a deep merge strategy, where later configs override earlier ones only for conflicting keys. Non-conflicting settings from all configs are preserved.

For example, if your global config sets `theme: "opencode"` and `autoupdate: true`, and your project config sets `model: "anthropic/claude-sonnet-4-5"`, the final configuration will include all three settings.

---

#### [Global](#global)

Place your global OpenCode config in `~/.config/opencode/opencode.json`. You’ll want to use the global config for things like themes, providers, or keybinds.

---

#### [Per project](#per-project)

You can also add a `opencode.json` in your project. Settings from this config are merged with and can override the global config. This is useful for configuring providers or modes specific to your project.

Tip

Place project specific config in the root of your project.

When OpenCode starts up, it looks for a config file in the current directory or traverse up to the nearest Git directory.

This is also safe to be checked into Git and uses the same schema as the global one.

---

#### [Custom path](#custom-path)

You can also specify a custom config file path using the `OPENCODE_CONFIG` environment variable. Settings from this config are merged with and can override the global and project configs.

Terminal window

```auto
export OPENCODE_CONFIG=/path/to/my/custom-config.json



opencode run "Hello world"
```

---

<a name="custom-directory"></a>

#### [Custom directory](#custom-directory)

You can specify a custom config directory using the `OPENCODE_CONFIG_DIR`
environment variable. This directory will be searched for agents, commands,
modes, and plugins just like the standard `.opencode` directory, and should
follow the same structure.

Terminal window

```auto
export OPENCODE_CONFIG_DIR=/path/to/my/config-directory



opencode run "Hello world"
```

Note: The custom directory is loaded after the global config and `.opencode` directories, so it can override their settings.

---

### [Schema](#schema)

The config file has a schema that’s defined in [**`opencode.ai/config.json`**](https://opencode.ai/config.json).

Your editor should be able to validate and autocomplete based on the schema.

---

#### [TUI](#tui)

You can configure TUI-specific settings through the `tui` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tui": {



"scroll_speed": 3,



"scroll_acceleration": {



"enabled": true



}



}



}
```

Available options:

- `scroll_acceleration.enabled` - Enable macOS-style scroll acceleration. **Takes precedence over `scroll_speed`.**
- `scroll_speed` - Custom scroll speed multiplier (default: `1`, minimum: `1`). Ignored if `scroll_acceleration.enabled` is `true`.

[Learn more about using the TUI here](/docs/tui).

---

<a name="tools"></a>

#### [Tools](#tools)

You can manage the tools an LLM can use through the `tools` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"write": false,



"bash": false



}



}
```

[Learn more about tools here](/docs/tools).

---

#### [Models](#models)

You can configure the providers and models you want to use in your OpenCode config through the `provider`, `model` and `small_model` options.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {},



"model": "anthropic/claude-sonnet-4-5",



"small_model": "anthropic/claude-haiku-4-5"



}
```

The `small_model` option configures a separate model for lightweight tasks like title generation. By default, OpenCode tries to use a cheaper model if one is available from your provider, otherwise it falls back to your main model.

You can also configure [local models](/docs/models#local). [Learn more](/docs/models).

---

<a name="themes"></a>

#### [Themes](#themes)

You can configure the theme you want to use in your OpenCode config through the `theme` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"theme": ""



}
```

[Learn more here](/docs/themes).

---

#### [Agents](#agents)

You can configure specialized agents for specific tasks through the `agent` option.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"agent": {



"code-reviewer": {



"description": "Reviews code for best practices and potential issues",



"model": "anthropic/claude-sonnet-4-5",



"prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",



"tools": {



// Disable file modification tools for review-only agent



"write": false,



"edit": false,



},



},



},



}
```

You can also define agents using markdown files in `~/.config/opencode/agent/` or `.opencode/agent/`. [Learn more here](/docs/agents).

---

<a name="sharing"></a>

#### [Sharing](#sharing)

You can configure the [share](/docs/share) feature through the `share` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"share": "manual"



}
```

This takes:

- `"manual"` - Allow manual sharing via commands (default)
- `"auto"` - Automatically share new conversations
- `"disabled"` - Disable sharing entirely

By default, sharing is set to manual mode where you need to explicitly share conversations using the `/share` command.

---

#### [Commands](#commands)

You can configure custom commands for repetitive tasks through the `command` option.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"command": {



"test": {



"template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",



"description": "Run tests with coverage",



"agent": "build",



"model": "anthropic/claude-haiku-4-5",



},



"component": {



"template": "Create a new React component named $ARGUMENTS with TypeScript support.\nInclude proper typing and basic structure.",



"description": "Create a new component",



},



},



}
```

You can also define commands using markdown files in `~/.config/opencode/command/` or `.opencode/command/`. [Learn more here](/docs/commands).

---

<a name="keybinds"></a>

#### [Keybinds](#keybinds)

You can customize your keybinds through the `keybinds` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"keybinds": {}



}
```

[Learn more here](/docs/keybinds).

---

#### [Autoupdate](#autoupdate)

OpenCode will automatically download any new updates when it starts up. You can disable this with the `autoupdate` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"autoupdate": false



}
```

If you don’t want updates but want to be notified when a new version is available, set `autoupdate` to `"notify"`.

---

<a name="formatters"></a>

#### [Formatters](#formatters)

You can configure code formatters through the `formatter` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"formatter": {



"prettier": {



"disabled": true



},



"custom-prettier": {



"command": ["npx", "prettier", "--write", "$FILE"],



"environment": {



"NODE_ENV": "development"



},



"extensions": [".js", ".ts", ".jsx", ".tsx"]



}



}



}
```

[Learn more about formatters here](/docs/formatters).

---

#### [Permissions](#permissions)

By default, opencode **allows all operations** without requiring explicit approval. You can change this using the `permission` option.

For example, to ensure that the `edit` and `bash` tools require user approval:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"edit": "ask",



"bash": "ask"



}



}
```

[Learn more about permissions here](/docs/permissions).

---

<a name="mcp-servers"></a>

#### [MCP servers](#mcp-servers)

You can configure MCP servers you want to use through the `mcp` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {}



}
```

[Learn more here](/docs/mcp-servers).

---

#### [Instructions](#instructions)

You can configure the instructions for the model you’re using through the `instructions` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]



}
```

This takes an array of paths and glob patterns to instruction files. [Learn more
about rules here](/docs/rules).

---

<a name="disabled-providers"></a>

#### [Disabled providers](#disabled-providers)

You can disable providers that are loaded automatically through the `disabled_providers` option. This is useful when you want to prevent certain providers from being loaded even if their credentials are available.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"disabled_providers": ["openai", "gemini"]



}
```

The `disabled_providers` option accepts an array of provider IDs. When a provider is disabled:

- It won’t be loaded even if environment variables are set.
- It won’t be loaded even if API keys are configured through `opencode auth login`.
- The provider’s models won’t appear in the model selection list.

---

### [Variables](#variables)

You can use variable substitution in your config files to reference environment variables and file contents.

---

#### [Env vars](#env-vars)

Use `{env:VARIABLE_NAME}` to substitute environment variables:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"model": "{env:OPENCODE_MODEL}",



"provider": {



"anthropic": {



"models": {},



"options": {



"apiKey": "{env:ANTHROPIC_API_KEY}"



}



}



}



}
```

If the environment variable is not set, it will be replaced with an empty string.

---

<a name="files"></a>

#### [Files](#files)

Use `{file:path/to/file}` to substitute the contents of a file:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"instructions": ["./custom-instructions.md"],



"provider": {



"openai": {



"options": {



"apiKey": "{file:~/.secrets/openai-key}"



}



}



}



}
```

File paths can be:

- Relative to the config file directory
- Or absolute paths starting with `/` or `~`

These are useful for:

- Keeping sensitive data like API keys in separate files.
- Including large instruction files without cluttering your config.
- Sharing common configuration snippets across multiple config files.

---

## Providers

Using any LLM provider in OpenCode.

OpenCode uses the [AI SDK](https://ai-sdk.dev/) and [Models.dev](https://models.dev) to support for **75+ LLM providers** and it supports running local models.

To add a provider you need to:

1. Add the API keys for the provider using `opencode auth login`.
2. Configure the provider in your OpenCode config.

---

#### [Credentials](#credentials)

When you add a provider’s API keys with `opencode auth login`, they are stored
in `~/.local/share/opencode/auth.json`.

---

#### [Config](#config)

You can customize the providers through the `provider` section in your OpenCode
config.

---

##### [Base URL](#base-url)

You can customize the base URL for any provider by setting the `baseURL` option. This is useful when using proxy services or custom endpoints.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"anthropic": {



"options": {



"baseURL": "https://api.anthropic.com/v1"



}



}



}



}
```

---

<a name="opencode-zen"></a>

### [OpenCode Zen](#opencode-zen)

OpenCode Zen is a list of models provided by the OpenCode team that have been
tested and verified to work well with OpenCode. [Learn more](/docs/zen).

Tip

If you are new, we recommend starting with OpenCode Zen.

1. Run `opencode auth login`, select opencode, and head to [opencode.ai/auth](https://opencode.ai/auth).
2. Sign in, add your billing details, and copy your API key.
3. Paste your API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  opencode



   │



   ●  Create an api key at https://opencode.ai/auth



   │



   ◆  Enter your API key



   │  _



   └
   ```

4. Run `/models` in the TUI to see the list of models we recommend.

It works like any other provider in OpenCode. And is completely optional to use
it.

---

### [Directory](#directory)

Let’s look at some of the providers in detail. If you’d like to add a provider to the
list, feel free to open a PR.

Note

Don’t see a provider here? Submit a PR.

---

#### [Amazon Bedrock](#amazon-bedrock)

To use Amazon Bedrock with OpenCode:

1. Head over to the **Model catalog** in the Amazon Bedrock console and request
   access to the models you want.

   Tip

   You need to have access to the model you want in Amazon Bedrock.
2. You’ll need either to set one of the following environment variables:

   - `AWS_ACCESS_KEY_ID`: You can get this by creating an IAM user and generating
     an access key for it.
   - `AWS_PROFILE`: First login through AWS IAM Identity Center (or AWS SSO) using
     `aws sso login`. Then get the name of the profile you want to use.
   - `AWS_BEARER_TOKEN_BEDROCK`: You can generate a long-term API key from the
     Amazon Bedrock console.

   Once you have one of the above, set it while running opencode.

   Terminal window

   ```auto
   AWS_ACCESS_KEY_ID=XXX opencode
   ```

   Or add it to your bash profile.

   ~/.bash\_profile

   ```auto
   export AWS_ACCESS_KEY_ID=XXX
   ```

3. Run the `/models` command to select the model you want.

---

#### [Anthropic](#anthropic)

We recommend signing up for [Claude Pro](https://www.anthropic.com/news/claude-pro) or [Max](https://www.anthropic.com/max), it’s the most cost-effective way to use opencode.

Once you’ve signed up, run `opencode auth login` and select Anthropic.

Terminal window

```auto
$ opencode auth login



┌  Add credential



│



◆  Select provider



│  ● Anthropic



│  ...



└
```

Here you can select the **Claude Pro/Max** option and it’ll open your browser
and ask you to authenticate.

Terminal window

```auto
$ opencode auth login



┌  Add credential



│



◇  Select provider



│  Anthropic



│



◆  Login method



│  ● Claude Pro/Max



│  ○ Create API Key



│  ○ Manually enter API Key



└
```

Now all the the Anthropic models should be available when you use the `/models` command.

###### [Using API keys](#using-api-keys)

You can also select **Create API Key** if you don’t have a Pro/Max subscription. It’ll also open your browser and ask you to login to Anthropic and give you a code you can paste in your terminal.

Or if you already have an API key, you can select **Manually enter API Key** and paste it in your terminal.

---

#### [Azure OpenAI](#azure-openai)

1. Head over to the [Azure portal](https://portal.azure.com/) and create an **Azure OpenAI** resource. You’ll need:

   - **Resource name**: This becomes part of your API endpoint (`https://RESOURCE_NAME.openai.azure.com/`)
   - **API key**: Either `KEY 1` or `KEY 2` from your resource
2. Go to [Azure AI Foundry](https://ai.azure.com/) and deploy a model.

   Note

   The deployment name must match the model name for opencode to work properly.
3. Run `opencode auth login` and select **Azure**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Azure



   │  ...



   └
   ```

4. Enter your API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Azure



   │



   ◇  Enter your API key



   │  _



   └
   ```

5. Set your resource name as an environment variable:

   Terminal window

   ```auto
   AZURE_RESOURCE_NAME=XXX opencode
   ```

   Or add it to your bash profile:

   ~/.bash\_profile

   ```auto
   export AZURE_RESOURCE_NAME=XXX
   ```

6. Run the `/models` command to select your deployed model.

---

#### [Azure Cognitive Services](#azure-cognitive-services)

1. Head over to the [Azure portal](https://portal.azure.com/) and create an **Azure OpenAI** resource. You’ll need:

   - **Resource name**: This becomes part of your API endpoint (`https://AZURE_COGNITIVE_SERVICES_RESOURCE_NAME.cognitiveservices.azure.com/`)
   - **API key**: Either `KEY 1` or `KEY 2` from your resource
2. Go to [Azure AI Foundry](https://ai.azure.com/) and deploy a model.

   Note

   The deployment name must match the model name for opencode to work properly.
3. Run `opencode auth login` and select **Azure**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Azure Cognitive Services



   │  ...



   └
   ```

4. Enter your API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Azure Cognitive Services



   │



   ◇  Enter your API key



   │  _



   └
   ```

5. Set your resource name as an environment variable:

   Terminal window

   ```auto
   AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX opencode
   ```

   Or add it to your bash profile:

   ~/.bash\_profile

   ```auto
   export AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX
   ```

6. Run the `/models` command to select your deployed model.

---

#### [Baseten](#baseten)

1. Head over to the [Baseten](https://app.baseten.co/), create an account, and generate an API key.
2. Run `opencode auth login` and select **Baseten**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Baseten



   │  ...



   └
   ```

3. Enter your Baseten API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Baseten



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model.

---

#### [Cerebras](#cerebras)

1. Head over to the [Cerebras console](https://inference.cerebras.ai/), create an account, and generate an API key.
2. Run `opencode auth login` and select **Cerebras**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Cerebras



   │  ...



   └
   ```

3. Enter your Cerebras API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Cerebras



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Qwen 3 Coder 480B*.

---

#### [Cortecs](#cortecs)

1. Head over to the [Cortecs console](https://cortecs.ai/), create an account, and generate an API key.
2. Run `opencode auth login` and select **Cortecs**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Cortecs



   │  ...



   └
   ```

3. Enter your Cortecs API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Cortecs



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Kimi K2 Instruct*.

---

#### [DeepSeek](#deepseek)

1. Head over to the [DeepSeek console](https://platform.deepseek.com/), create an account, and click **Create new API key**.
2. Run `opencode auth login` and select **DeepSeek**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● DeepSeek



   │  ...



   └
   ```

3. Enter your DeepSeek API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  DeepSeek



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a DeepSeek model like *DeepSeek Reasoner*.

---

#### [Deep Infra](#deep-infra)

1. Head over to the [Deep Infra dashboard](https://deepinfra.com/dash), create an account, and generate an API key.
2. Run `opencode auth login` and select **Deep Infra**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Deep Infra



   │  ...



   └
   ```

3. Enter your Deep Infra API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Deep Infra



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model.

---

#### [Fireworks AI](#fireworks-ai)

1. Head over to the [Fireworks AI console](https://app.fireworks.ai/), create an account, and click **Create API Key**.
2. Run `opencode auth login` and select **Fireworks AI**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Fireworks AI



   │  ...



   └
   ```

3. Enter your Fireworks AI API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Fireworks AI



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Kimi K2 Instruct*.

---

#### [GitHub Copilot](#github-copilot)

To use your GitHub Copilot subscription with opencode:

Note

Some models might need a [Pro+
subscription](https://github.com/features/copilot/plans) to use.

Some models need to be manually enabled in your [GitHub Copilot settings](https://docs.github.com/en/copilot/how-tos/use-ai-models/configure-access-to-ai-models#setup-for-individual-use).

1. Run `opencode auth login` and select GitHub Copilot.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  GitHub Copilot



   │



   ◇   ──────────────────────────────────────────────╮



   │                                                 │



   │  Please visit: https://github.com/login/device  │



   │  Enter code: 8F43-6FCF                          │



   │                                                 │



   ├─────────────────────────────────────────────────╯



   │



   ◓  Waiting for authorization...
   ```

2. Navigate to [github.com/login/device](https://github.com/login/device) and enter the code.
3. Now run the `/models` command to select the model you want.

---

<a name="google-vertex-ai"></a>

#### [Google Vertex AI](#google-vertex-ai)

To use Google Vertex AI with OpenCode:

1. Head over to the **Model Garden** in the Google Cloud Console and check the
   models available in your region.

   Note

   You need to have a Google Cloud project with Vertex AI API enabled.
2. Set the required environment variables:

   - `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID
   - `VERTEX_LOCATION` (optional): The region for Vertex AI (defaults to `global`)
   - Authentication (choose one):
     - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your service account JSON key file
     - Authenticate using gcloud CLI: `gcloud auth application-default login`

   Set them while running opencode.

   Terminal window

   ```auto
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json GOOGLE_CLOUD_PROJECT=your-project-id opencode
   ```

   Or add them to your bash profile.

   ~/.bash\_profile

   ```auto
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json



   export GOOGLE_CLOUD_PROJECT=your-project-id



   export VERTEX_LOCATION=global
   ```

Tip

The `global` region improves availability and reduces errors at no extra cost. Use regional endpoints (e.g., `us-central1`) for data residency requirements. [Learn more](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#regional_and_global_endpoints)

1. Run the `/models` command to select the model you want.

---

<a name="groq"></a>

#### [Groq](#groq)

1. Head over to the [Groq console](https://console.groq.com/), click **Create API Key**, and copy the key.
2. Run `opencode auth login` and select Groq.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Groq



   │  ...



   └
   ```

3. Enter the API key for the provider.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Groq



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select the one you want.

---

<a name="hugging-face"></a>

#### [Hugging Face](#hugging-face)

[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) provides access to open models supported by 17+ providers.

1. Head over to [Hugging Face settings](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained) to create a token with permission to make calls to Inference Providers.
2. Run `opencode auth login` and select **Hugging Face**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Hugging Face



   │  ...



   └
   ```

3. Enter your Hugging Face token.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Hugging Face



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Kimi-K2-Instruct* or *GLM-4.6*.

---

<a name="llamacpp"></a>

#### [llama.cpp](#llamacpp)

You can configure opencode to use local models through [llama.cpp’s](https://github.com/ggml-org/llama.cpp) llama-server utility

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"llama.cpp": {



"npm": "@ai-sdk/openai-compatible",



"name": "llama-server (local)",



"options": {



"baseURL": "http://127.0.0.1:8080/v1"



},



"models": {



"qwen3-coder:a3b": {



"name": "Qwen3-Coder: a3b-30b (local)"



}



},



"limit": {



"context": 128000,



"output": 65536



}



}



}



}
```

In this example:

- `llama.cpp` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server.
- `models` is a map of model IDs to their configurations. The model name will be displayed in the model selection list.

---

#### [IO.NET](#ionet)

IO.NET offers 17 models optimized for various use cases:

1. Head over to the [IO.NET console](https://ai.io.net/), create an account, and generate an API key.
2. Run `opencode auth login` and select **IO.NET**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● IO.NET



   │  ...



   └
   ```

3. Enter your IO.NET API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  IO.NET



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model.

---

#### [LM Studio](#lm-studio)

You can configure opencode to use local models through LM Studio.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"lmstudio": {



"npm": "@ai-sdk/openai-compatible",



"name": "LM Studio (local)",



"options": {



"baseURL": "http://127.0.0.1:1234/v1"



},



"models": {



"google/gemma-3n-e4b": {



"name": "Gemma 3n-e4b (local)"



}



}



}



}



}
```

In this example:

- `lmstudio` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server.
- `models` is a map of model IDs to their configurations. The model name will be displayed in the model selection list.

---

<a name="moonshot-ai"></a>

#### [Moonshot AI](#moonshot-ai)

To use Kimi K2 from Moonshot AI:

1. Head over to the [Moonshot AI console](https://platform.moonshot.ai/console), create an account, and click **Create API key**.
2. Run `opencode auth login` and select **Moonshot AI**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ...



   │  ● Moonshot AI



   └
   ```

3. Enter your Moonshot API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Moonshot AI



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select *Kimi K2*.

---

<a name="ollama"></a>

#### [Ollama](#ollama)

You can configure opencode to use local models through Ollama.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"ollama": {



"npm": "@ai-sdk/openai-compatible",



"name": "Ollama (local)",



"options": {



"baseURL": "http://localhost:11434/v1"



},



"models": {



"llama2": {



"name": "Llama 2"



}



}



}



}



}
```

In this example:

- `ollama` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server.
- `models` is a map of model IDs to their configurations. The model name will be displayed in the model selection list.

Tip

If tool calls aren’t working, try increasing `num_ctx` in Ollama. Start around 16k - 32k.

---

#### [Ollama Cloud](#ollama-cloud)

To use Ollama Cloud with OpenCode:

1. Head over to <https://ollama.com/> and sign in or create an account.
2. Navigate to **Settings** > **Keys** and click **Add API Key** to generate a new API key.
3. Copy the API key for use in OpenCode.
4. Run `opencode auth login` and select **Ollama Cloud**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Ollama Cloud



   │  ...



   └
   ```

5. Enter your Ollama Cloud API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Ollama Cloud



   │



   ◇  Enter your API key



   │  _



   └
   ```

6. **Important**: Before using cloud models in OpenCode, you must pull the model information locally:

   Terminal window

   ```auto
   ollama pull gpt-oss:20b-cloud
   ```

7. Run the `/models` command to select your Ollama Cloud model.

---

<a name="openai"></a>

#### [OpenAI](#openai)

1. Head over to the [OpenAI Platform console](https://platform.openai.com/api-keys), click **Create new secret key**, and copy the key.
2. Run `opencode auth login` and select OpenAI.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● OpenAI



   │  ...



   └
   ```

3. Enter the API key for the provider.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  OpenAI



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select the one you want.

---

<a name="opencode-zen-1"></a>

#### [OpenCode Zen](#opencode-zen-1)

OpenCode Zen is a list of tested and verified models provided by the OpenCode team. [Learn more](/docs/zen).

1. Sign in to **[OpenCode Zen](https://opencode.ai/auth)** and click **Create API Key**.
2. Run `opencode auth login` and select **OpenCode Zen**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● OpenCode Zen



   │  ...



   └
   ```

3. Enter your OpenCode API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  OpenCode Zen



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Qwen 3 Coder 480B*.

---

<a name="openrouter"></a>

#### [OpenRouter](#openrouter)

1. Head over to the [OpenRouter dashboard](https://openrouter.ai/settings/keys), click **Create API Key**, and copy the key.
2. Run `opencode auth login` and select OpenRouter.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● OpenRouter



   │  ○ Anthropic



   │  ○ Google



   │  ...



   └
   ```

3. Enter the API key for the provider.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  OpenRouter



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Many OpenRouter models are preloaded by default, run the `/models` command to select the one you want.

   You can also add additional models through your opencode config.

   opencode.json

   ```auto
   {



   "$schema": "https://opencode.ai/config.json",



   "provider": {



   "openrouter": {



   "models": {



   "somecoolnewmodel": {}



   }



   }



   }



   }
   ```

5. You can also customize them through your opencode config. Here’s an example of specifying a provider

   opencode.json

   ```auto
   {



   "$schema": "https://opencode.ai/config.json",



   "provider": {



   "openrouter": {



   "models": {



   "moonshotai/kimi-k2": {



   "options": {



   "provider": {



   "order": ["baseten"],



   "allow_fallbacks": false



   }



   }



   }



   }



   }



   }



   }
   ```

---

<a name="ovhcloud-ai-endpoints"></a>

#### [OVHcloud AI Endpoints](#ovhcloud-ai-endpoints)

1. Head over to the [OVHcloud panel](https://ovh.com/manager). Navigate to the `Public Cloud` section, `AI & Machine Learning` > `AI Endpoints` and in `API Keys` tab, click **Create a new API key**.
2. Run `opencode auth login` and select **OVHcloud AI Endpoints**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● OVHcloud AI Endpoints



   │  ...



   └
   ```

3. Enter your OVHcloud AI Endpoints API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  OVHcloud AI Endpoints



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *gpt-oss-120b*.

---

<a name="together-ai"></a>

#### [Together AI](#together-ai)

1. Head over to the [Together AI console](https://api.together.ai), create an account, and click **Add Key**.
2. Run `opencode auth login` and select **Together AI**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Together AI



   │  ...



   └
   ```

3. Enter your Together AI API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Together AI



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Kimi K2 Instruct*.

---

<a name="xai"></a>

#### [xAI](#xai)

For a limited time, you can use xAI’s Grok Code for free with opencode.

Tip

Grok Code is available for free for a limited time on opencode.

1. Make sure you are on the latest version of opencode.
2. Run the `/models` command and select **Grok Code Free**.

As a part of the trial period, the xAI team will be using the request logs to
monitor and improve Grok Code.

---

<a name="zai"></a>

#### [Z.AI](#zai)

1. Head over to the [Z.AI API console](https://z.ai/manage-apikey/apikey-list), create an account, and click **Create a new API key**.
2. Run `opencode auth login` and select **Z.AI**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Z.AI



   │  ...



   └
   ```

   If you are subscribed to the **GLM Coding Plan**, select **Z.AI Coding Plan**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Z.AI Coding Plan



   │  ...



   └
   ```

3. Enter your Z.AI API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Z.AI



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *GLM-4.5*.

---

#### [ZenMux](#zenmux)

1. Head over to the [ZenMux dashboard](https://zenmux.ai/settings/keys), click **Create API Key**, and copy the key.
2. Run `opencode auth login` and select ZenMux.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● ZenMux



   │  ○ Zhipu AI



   │  ○ Zhipu AI Coding Plan



   │  ...



   └
   ```

3. Enter the API key for the provider.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  ZenMux



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Many ZenMux models are preloaded by default, run the `/models` command to select the one you want.

   You can also add additional models through your opencode config.

   opencode.json

   ```auto
   {



   "$schema": "https://opencode.ai/config.json",



   "provider": {



   "zenmux": {



   "models": {



   "somecoolnewmodel": {}



   }



   }



   }



   }
   ```

---

<a name="custom-provider"></a>

### [Custom provider](#custom-provider)

To add any **OpenAI-compatible** provider that’s not listed in `opencode auth login`:

Tip

You can use any OpenAI-compatible provider with opencode. Most modern AI providers offer OpenAI-compatible APIs.

1. Run `opencode auth login` and scroll down to **Other**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ...



   │  ● Other



   └
   ```

2. Enter a unique ID for the provider.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Enter provider id



   │  myprovider



   └
   ```

   Note

   Choose a memorable ID, you’ll use this in your config file.
3. Enter your API key for the provider.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ▲  This only stores a credential for myprovider - you will need configure it in opencode.json, check the docs for examples.



   │



   ◇  Enter your API key



   │  sk-...



   └
   ```

4. Create or update your `opencode.json` file in your project directory:

   opencode.json

   ```auto
   {



   "$schema": "https://opencode.ai/config.json",



   "provider": {



   "myprovider": {



   "npm": "@ai-sdk/openai-compatible",



   "name": "My AI ProviderDisplay Name",



   "options": {



   "baseURL": "https://api.myprovider.com/v1"



   },



   "models": {



   "my-model-name": {



   "name": "My Model Display Name"



   }



   }



   }



   }



   }
   ```

   Here are the configuration options:

   - **npm**: AI SDK package to use, `@ai-sdk/openai-compatible` for OpenAI-compatible providers
   - **name**: Display name in UI.
   - **models**: Available models.
   - **options.baseURL**: API endpoint URL.
   - **options.apiKey**: Optionally set the API key, if not using auth.
   - **options.headers**: Optionally set custom headers.

   More on the advanced options in the example below.
5. Run the `/models` command and your custom provider and models will appear in the selection list.

---

<a name="example"></a>

###### [Example](#example)

Here’s an example setting the `apiKey`, `headers`, and model `limit` options.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"myprovider": {



"npm": "@ai-sdk/openai-compatible",



"name": "My AI ProviderDisplay Name",



"options": {



"baseURL": "https://api.myprovider.com/v1",



"apiKey": "{env:ANTHROPIC_API_KEY}",



"headers": {



"Authorization": "Bearer custom-token"



}



},



"models": {



"my-model-name": {



"name": "My Model Display Name",



"limit": {



"context": 200000,



"output": 65536



}



}



}



}



}



}
```

Configuration details:

- **apiKey**: Set using `env` variable syntax, [learn more](/docs/config#env-vars).
- **headers**: Custom headers sent with each request.
- **limit.context**: Maximum input tokens the model accepts.
- **limit.output**: Maximum tokens the model can generate.

The `limit` fields allow OpenCode to understand how much context you have left. Standard providers pull these from models.dev automatically.

---

### [Troubleshooting](#troubleshooting)

If you are having trouble with configuring a provider, check the following:

1. **Check the auth setup**: Run `opencode auth list` to see if the credentials
   for the provider are added to your config.

   This doesn’t apply to providers like Amazon Bedrock, that rely on environment variables for their auth.
2. For custom providers, check the opencode config and:

   - Make sure the provider ID used in `opencode auth login` matches the ID in your opencode config.
   - The right npm package is used for the provider. For example, use `@ai-sdk/cerebras` for Cerebras. And for all other OpenAI-compatible providers, use `@ai-sdk/openai-compatible`.
   - Check correct API endpoint is used in the `options.baseURL` field.

---

#### [Venice AI](#venice-ai)

1. Head over to the [Venice AI console](https://venice.ai), create an account, and generate an API key.
2. Run `opencode auth login` and select **Venice AI**.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◆  Select provider



   │  ● Venice AI



   │  ...



   └
   ```

3. Enter your Venice AI API key.

   Terminal window

   ```auto
   $ opencode auth login



   ┌  Add credential



   │



   ◇  Select provider



   │  Venice AI



   │



   ◇  Enter your API key



   │  _



   └
   ```

4. Run the `/models` command to select a model like *Llama 3.3 70B*.

---

## Enterprise

Using OpenCode securely in your organization.

OpenCode Enterprise is for organizations that want to ensure that their code and data never leaves their infrastructure. It can do this by using a centralized config that integrates with your SSO and internal AI gateway.

Note

OpenCode does not store any of your code or context data.

To get started with OpenCode Enterprise:

1. Do a trial internally with your team.
2. **[Contact us](mailto:contact@anoma.ly)** to discuss pricing and implementation options.

---

### [Trial](#trial)

OpenCode is open source and does not store any of your code or context data, so your developers can simply [get started](/docs/) and carry out a trial.

---

#### [Data handling](#data-handling)

**OpenCode does not store your code or context data.** All processing happens locally or through direct API calls to your AI provider.

This means that as long as you are using a provider you trust, or an internal
AI gateway, you can use OpenCode securely.

The only caveat here is the optional `/share` feature.

---

##### [Sharing conversations](#sharing-conversations)

If a user enables the `/share` feature, the conversation and the data associated with it are sent to the service we use to host these share pages at opencode.ai.

The data is currently served through our CDN’s edge network, and is cached on the edge near your users.

We recommend you disable this for your trial.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"share": "disabled"



}
```

[Learn more about sharing](/docs/share).

---

<a name="code-ownership"></a>

#### [Code ownership](#code-ownership)

**You own all code produced by OpenCode.** There are no licensing restrictions or ownership claims.

---

<a name="pricing"></a>

### [Pricing](#pricing)

We use a per-seat model for OpenCode Enterprise. If you have your own LLM gateway, we do not charge for tokens used. For further details about pricing and implementation options, **[contact us](mailto:contact@anoma.ly)**.

---

<a name="deployment"></a>

### [Deployment](#deployment)

Once you have completed your trial and you are ready to use OpenCode at
your organization, you can **[contact us](mailto:contact@anoma.ly)** to discuss
pricing and implementation options.

---

<a name="central-config"></a>

#### [Central Config](#central-config)

We can set up OpenCode to use a single central config for your entire organization.

This centralized config can integrate with your SSO provider and ensures all users access only your internal AI gateway.

---

<a name="sso-integration"></a>

#### [SSO integration](#sso-integration)

Through the central config, OpenCode can integrate with your organization’s SSO provider for authentication.

This allows OpenCode to obtain credentials for your internal AI gateway through your existing identity management system.

---

<a name="internal-ai-gateway"></a>

#### [Internal AI gateway](#internal-ai-gateway)

With the central config, OpenCode can also be configured to use only your internal AI gateway.

You can also disable all other AI providers, ensuring all requests go through your organization’s approved infrastructure.

---

<a name="self-hosting"></a>

#### [Self-hosting](#self-hosting)

While we recommend disabling the share pages to ensure your data never leaves
your organization, we can also help you self-host them on your infrastructure.

This is currently on our roadmap. If you’re interested, **[let us know](mailto:contact@anoma.ly)**.

---

<a name="faq"></a>

### [FAQ](#faq)

What is OpenCode Enterprise?

OpenCode Enterprise is for organizations that want to ensure that their code and data never leaves their infrastructure. It can do this by using a centralized config that integrates with your SSO and internal AI gateway.

How do I get started with OpenCode Enterprise?

Simply start with an internal trial with your team. OpenCode by default does not store your code or context data, making it easy to get started.

Then **[contact us](mailto:contact@anoma.ly)** to discuss pricing and implementation options.

How does enterprise pricing work?

We offer per-seat enterprise pricing. If you have your own LLM gateway, we do not charge for tokens used. For further details, **[contact us](mailto:contact@anoma.ly)** for a custom quote based on your organization’s needs.

Is my data secure with OpenCode Enterprise?

Yes. OpenCode does not store your code or context data. All processing happens locally or through direct API calls to your AI provider. With central config and SSO integration, your data remains secure within your organization’s infrastructure.

Can we use our own private NPM registry?

OpenCode supports private npm registries through Bun’s native `.npmrc` file support. If your organization uses a private registry, such as JFrog Artifactory, Nexus, or similar, ensure developers are authenticated before running OpenCode.

To set up authentication with your private registry:

Terminal window

```auto
npm login --registry=https://your-company.jfrog.io/api/npm/npm-virtual/
```

This creates `~/.npmrc` with authentication details. OpenCode will automatically
pick this up.

Caution

You must be logged into the private registry before running OpenCode.

Alternatively, you can manually configure a `.npmrc` file:

~/.npmrc

```auto
registry=https://your-company.jfrog.io/api/npm/npm-virtual/



//your-company.jfrog.io/api/npm/npm-virtual/:_authToken=${NPM_AUTH_TOKEN}
```

Developers must be logged into the private registry before running OpenCode to ensure packages can be installed from your enterprise registry.

---

<a name="troubleshooting"></a>

## Troubleshooting

Common issues and how to resolve them.

To debug any issues with OpenCode, you can check the logs or the session data
that it stores locally.

---

<a name="logs"></a>

#### [Logs](#logs)

Log files are written to:

- **macOS/Linux**: `~/.local/share/opencode/log/`
- **Windows**: `%USERPROFILE%\.local\share\opencode\log\`

Log files are named with timestamps (e.g., `2025-01-09T123456.log`) and the most recent 10 log files are kept.

You can set the log level with the `--log-level` command-line option to get more detailed debug information. For example, `opencode --log-level DEBUG`.

---

<a name="storage"></a>

#### [Storage](#storage)

opencode stores session data and other application data on disk at:

- **macOS/Linux**: `~/.local/share/opencode/`
- **Windows**: `%USERPROFILE%\.local\share\opencode`

This directory contains:

- `auth.json` - Authentication data like API keys, OAuth tokens
- `log/` - Application logs
- `project/` - Project-specific data like session and message data
  - If the project is within a Git repo, it is stored in `./<project-slug>/storage/`
  - If it is not a Git repo, it is stored in `./global/storage/`

---

<a name="getting-help"></a>

### [Getting help](#getting-help)

If you’re experiencing issues with OpenCode:

1. **Report issues on GitHub**

   The best way to report bugs or request features is through our GitHub repository:

   [**github.com/sst/opencode/issues**](https://github.com/sst/opencode/issues)

   Before creating a new issue, search existing issues to see if your problem has already been reported.
2. **Join our Discord**

   For real-time help and community discussion, join our Discord server:

   [**opencode.ai/discord**](https://opencode.ai/discord)

---

<a name="common-issues"></a>

### [Common issues](#common-issues)

Here are some common issues and how to resolve them.

---

<a name="opencode-wont-start"></a>

#### [opencode won’t start](#opencode-wont-start)

1. Check the logs for error messages
2. Try running with `--print-logs` to see output in the terminal
3. Ensure you have the latest version with `opencode upgrade`

---

<a name="authentication-issues"></a>

#### [Authentication issues](#authentication-issues)

1. Try re-authenticating with `opencode auth login <provider>`
2. Check that your API keys are valid
3. Ensure your network allows connections to the provider’s API

---

<a name="model-not-available"></a>

#### [Model not available](#model-not-available)

1. Check that you’ve authenticated with the provider
2. Verify the model name in your config is correct
3. Some models may require specific access or subscriptions

If you encounter `ProviderModelNotFoundError` you are most likely incorrectly
referencing a model somewhere.
Models should be referenced like so: `<providerId>/<modelId>`

Examples:

- `openai/gpt-4.1`
- `openrouter/google/gemini-2.5-flash`
- `opencode/kimi-k2`

To figure out what models you have access to, run `opencode models`

---

<a name="provideriniterror"></a>

#### [ProviderInitError](#provideriniterror)

If you encounter a ProviderInitError, you likely have an invalid or corrupted configuration.

To resolve this:

1. First, verify your provider is set up correctly by following the [providers guide](/docs/providers)
2. If the issue persists, try clearing your stored configuration:

   Terminal window

   ```auto
   rm -rf ~/.local/share/opencode
   ```

3. Re-authenticate with your provider:

   Terminal window

   ```auto
   opencode auth login <provider>
   ```

---

<a name="ai_apicallerror-and-provider-package-issues"></a>

#### [AI\_APICallError and provider package issues](#ai_apicallerror-and-provider-package-issues)

If you encounter API call errors, this may be due to outdated provider packages. opencode dynamically installs provider packages (OpenAI, Anthropic, Google, etc.) as needed and caches them locally.

To resolve provider package issues:

1. Clear the provider package cache:

   Terminal window

   ```auto
   rm -rf ~/.cache/opencode
   ```

2. Restart opencode to reinstall the latest provider packages

This will force opencode to download the most recent versions of provider packages, which often resolves compatibility issues with model parameters and API changes.

---

#### [Copy/paste not working on Linux](#copypaste-not-working-on-linux)

Linux users need to have one of the following clipboard utilities installed for copy/paste functionality to work:

**For X11 systems:**

Terminal window

```auto
apt install -y xclip



# or



apt install -y xsel
```

**For Wayland systems:**

Terminal window

```auto
apt install -y wl-clipboard
```

**For headless environments:**

Terminal window

```auto
apt install -y xvfb



# and run:



Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &



export DISPLAY=:99.0
```

opencode will detect if you’re using Wayland and prefer `wl-clipboard`, otherwise it will try to find clipboard tools in order of: `xclip` and `xsel`.

---

<a name="migrating-to-10"></a>

## Migrating to 1.0

What's new in OpenCode 1.0.

OpenCode 1.0 is a complete rewrite of the TUI.

We moved from the go+bubbletea based TUI which had performance and capability issues to an in-house framework (OpenTUI) written in zig+solidjs.

The new TUI works like the old one since it connects to the same opencode server.

---

<a name="upgrading"></a>

### [Upgrading](#upgrading)

You should not be autoupgraded to 1.0 if you are currently using a previous
version. However some older versions of OpenCode always grab latest.

To upgrade manually, run

Terminal window

```auto
opencode upgrade 1.0.0
```

To downgrade back to 0.x, run

Terminal window

```auto
opencode upgrade 0.15.31
```

---

<a name="ux-changes"></a>

### [UX changes](#ux-changes)

The session history is more compressed, only showing full details of the edit and bash tool.

We added a command bar which almost everything flows through. Press ctrl+p to bring it up in any context and see everything you can do.

Added a session sidebar (can be toggled) with useful information.

We removed some functionality that we weren’t sure anyone actually used. If something important is missing please open an issue and we’ll add it back quickly.

---

<a name="breaking-changes"></a>

### [Breaking changes](#breaking-changes)

<a name="theme"></a>

#### [Theme](#theme)

The `system` theme has not yet been ported and custom themes aren’t loaded yet but both of these will be fixed this week.

<a name="keybinds-renamed"></a>

#### [Keybinds renamed](#keybinds-renamed)

- messages\_revert -> messages\_undo
- switch\_agent -> agent\_cycle
- switch\_agent\_reverse -> agent\_cycle\_reverse
- switch\_mode -> agent\_cycle
- switch\_mode\_reverse -> agent\_cycle\_reverse

<a name="keybinds-removed"></a>

#### [Keybinds removed](#keybinds-removed)

- messages\_layout\_toggle
- messages\_next
- messages\_previous
- file\_diff\_toggle
- file\_search
- file\_close
- file\_list
- app\_help
- project\_init
- tool\_details
- thinking\_blocks

---

<a name="tui"></a>

## TUI

Using the OpenCode terminal user interface.

OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

Running OpenCode starts the TUI for the current directory.

Terminal window

```auto
opencode
```

Or you can start it for a specific working directory.

Terminal window

```auto
opencode /path/to/project
```

Once you’re in the TUI, you can prompt it with a message.

```auto
Give me a quick summary of the codebase.
```

---

### [File references](#file-references)

You can reference files in your messages using `@`. This does a fuzzy file search in the current working directory.

Tip

You can also use `@` to reference files in your messages.

```auto
How is auth handled in @packages/functions/src/api/index.ts?
```

The content of the file is added to the conversation automatically.

---

<a name="bash-commands"></a>

### [Bash commands](#bash-commands)

Start a message with `!` to run a shell command.

```auto
!ls -la
```

The output of the command is added to the conversation as a tool result.

---

### [Commands](#commands)

When using the OpenCode TUI, you can type `/` followed by a command name to quickly execute actions. For example:

```auto
/help
```

Most commands also have keybind using `ctrl+x` as the leader key, where `ctrl+x` is the default leader key. [Learn more](/docs/keybinds).

Here are all available slash commands:

---

<a name="compact"></a>

#### [compact](#compact)

Compact the current session. *Alias*: `/summarize`

```auto
/compact
```

**Keybind:** `ctrl+x c`

---

#### [details](#details)

Toggle tool execution details.

```auto
/details
```

**Keybind:** `ctrl+x d`

---

<a name="editor"></a>

#### [editor](#editor)

Open external editor for composing messages. Uses the editor set in your `EDITOR` environment variable. [Learn more](#editor-setup).

```auto
/editor
```

**Keybind:** `ctrl+x e`

---

#### [exit](#exit)

Exit OpenCode. *Aliases*: `/quit`, `/q`

```auto
/exit
```

**Keybind:** `ctrl+x q`

---

<a name="export"></a>

#### [export](#export)

Export current conversation to Markdown and open in your default editor. Uses the editor set in your `EDITOR` environment variable. [Learn more](#editor-setup).

```auto
/export
```

**Keybind:** `ctrl+x x`

---

#### [help](#help)

Show the help dialog.

```auto
/help
```

**Keybind:** `ctrl+x h`

---

<a name="init"></a>

#### [init](#init)

Create or update `AGENTS.md` file. [Learn more](/docs/rules).

```auto
/init
```

**Keybind:** `ctrl+x i`

---

#### [models](#models)

List available models.

```auto
/models
```

**Keybind:** `ctrl+x m`

---

<a name="new"></a>

#### [new](#new)

Start a new session. *Alias*: `/clear`

```auto
/new
```

**Keybind:** `ctrl+x n`

---

#### [redo](#redo)

Redo a previously undone message. Only available after using `/undo`.

Tip

Any file changes will also be restored.

Internally, this uses Git to manage the file changes. So your project **needs to
be a Git repository**.

```auto
/redo
```

**Keybind:** `ctrl+x r`

---

<a name="sessions"></a>

#### [sessions](#sessions)

List and switch between sessions. *Aliases*: `/resume`, `/continue`

```auto
/sessions
```

**Keybind:** `ctrl+x l`

---

#### [share](#share)

Share current session. [Learn more](/docs/share).

```auto
/share
```

**Keybind:** `ctrl+x s`

---

<a name="themes-1"></a>

#### [themes](#themes)

List available themes.

```auto
/themes
```

**Keybind:** `ctrl+x t`

---

#### [undo](#undo)

Undo last message in the conversation. Removes the most recent user message, all subsequent responses, and any file changes.

Tip

Any file changes made will also be reverted.

Internally, this uses Git to manage the file changes. So your project **needs to
be a Git repository**.

```auto
/undo
```

**Keybind:** `ctrl+x u`

---

<a name="unshare"></a>

#### [unshare](#unshare)

Unshare current session. [Learn more](/docs/share#un-sharing).

```auto
/unshare
```

---

### [Editor setup](#editor-setup)

Both the `/editor` and `/export` commands use the editor specified in your `EDITOR` environment variable.

- [Linux/macOS](#tab-panel-4)
- [Windows (CMD)](#tab-panel-5)
- [Windows (PowerShell)](#tab-panel-6)

Terminal window

```auto
# Example for nano or vim



export EDITOR=nano



export EDITOR=vim



# For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.



# include --wait



export EDITOR="code --wait"
```

To make it permanent, add this to your shell profile;
`~/.bashrc`, `~/.zshrc`, etc.

Terminal window

```auto
set EDITOR=notepad



<a name="for-gui-editors-vs-code-cursor-vscodium-windsurf-zed-etc"></a>
# For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.



<a name="include-wait"></a>
# include --wait



set EDITOR=code --wait
```

To make it permanent, use **System Properties** > **Environment
Variables**.

Terminal window

```auto
$env:EDITOR = "notepad"



# For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.



# include --wait



$env:EDITOR = "code --wait"
```

To make it permanent, add this to your PowerShell profile.

Popular editor options include:

- `code` - Visual Studio Code
- `cursor` - Cursor
- `windsurf` - Windsurf
- `vim` - Vim editor
- `nano` - Nano editor
- `notepad` - Windows Notepad
- `subl` - Sublime Text

Note

Some editors like VS Code need to be started with the `--wait` flag.

Some editors need command-line arguments to run in blocking mode. The `--wait` flag makes the editor process block until closed.

---

<a name="configure-1"></a>

### [Configure](#configure)

You can customize TUI behavior through your OpenCode config file.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tui": {



"scroll_speed": 3,



"scroll_acceleration": {



"enabled": true



}



}



}
```

#### [Options](#options)

- `scroll_acceleration` - Enable macOS-style scroll acceleration for smooth, natural scrolling. When enabled, scroll speed increases with rapid scrolling gestures and stays precise for slower movements. **This setting takes precedence over `scroll_speed` and overrides it when enabled.**
- `scroll_speed` - Controls how fast the TUI scrolls when using scroll commands (minimum: `1`). Defaults to `1` on Unix and `3` on Windows. **Note: This is ignored if `scroll_acceleration.enabled` is set to `true`.**

---

## CLI

OpenCode CLI options and commands.

The OpenCode CLI by default starts the [TUI](/docs/tui) when run without any arguments.

Terminal window

```auto
opencode
```

But it also accepts commands as documented on this page. This allows you to interact with OpenCode programmatically.

Terminal window

```auto
opencode run "Explain how closures work in JavaScript"
```

---

#### [tui](#tui)

Start the OpenCode terminal user interface.

Terminal window

```auto
opencode [project]
```

<a name="flags"></a>

##### [Flags](#flags)

| Flag | Short | Description |
| --- | --- | --- |
| `--continue` | `-c` | Continue the last session |
| `--session` | `-s` | Session ID to continue |
| `--prompt` | `-p` | Prompt to use |
| `--model` | `-m` | Model to use in the form of provider/model |
| `--agent` |  | Agent to use |
| `--port` |  | Port to listen on |
| `--hostname` |  | Hostname to listen on |

---

<a name="commands"></a>

### [Commands](#commands)

The OpenCode CLI also has the following commands.

---

<a name="agent"></a>

#### [agent](#agent)

Manage agents for OpenCode.

Terminal window

```auto
opencode agent [command]
```

---

##### [create](#create)

Create a new agent with custom configuration.

Terminal window

```auto
opencode agent create
```

This command will guide you through creating a new agent with a custom system prompt and tool configuration.

---

<a name="auth"></a>

#### [auth](#auth)

Command to manage credentials and login for providers.

Terminal window

```auto
opencode auth [command]
```

---

##### [login](#login)

OpenCode is powered by the provider list at [Models.dev](https://models.dev), so you can use `opencode auth login` to configure API keys for any provider you’d like to use. This is stored in `~/.local/share/opencode/auth.json`.

Terminal window

```auto
opencode auth login
```

When OpenCode starts up it loads the providers from the credentials file. And if there are any keys defined in your environments or a `.env` file in your project.

---

<a name="list"></a>

##### [list](#list)

Lists all the authenticated providers as stored in the credentials file.

Terminal window

```auto
opencode auth list
```

Or the short version.

Terminal window

```auto
opencode auth ls
```

---

<a name="logout"></a>

##### [logout](#logout)

Logs you out of a provider by clearing it from the credentials file.

Terminal window

```auto
opencode auth logout
```

---

#### [github](#github)

Manage the GitHub agent for repository automation.

Terminal window

```auto
opencode github [command]
```

---

<a name="install-1"></a>

##### [install](#install)

Install the GitHub agent in your repository.

Terminal window

```auto
opencode github install
```

This sets up the necessary GitHub Actions workflow and guides you through the configuration process. [Learn more](/docs/github).

---

##### [run](#run)

Run the GitHub agent. This is typically used in GitHub Actions.

Terminal window

```auto
opencode github run
```

<a name="flags-1"></a>

###### [Flags](#flags-1)

| Flag | Description |
| --- | --- |
| `--event` | GitHub mock event to run the agent for |
| `--token` | GitHub personal access token |

---

<a name="models"></a>

#### [models](#models)

List all available models from configured providers.

Terminal window

```auto
opencode models
```

This command displays all models available across your configured providers in the format `provider/model`.

This is useful for figuring out the exact model name to use in [your config](/docs/config/).

---

#### [run](#run-1)

Run opencode in non-interactive mode by passing a prompt directly.

Terminal window

```auto
opencode run [message..]
```

This is useful for scripting, automation, or when you want a quick answer without launching the full TUI. For example.

Terminal window

```auto
opencode run Explain the use of context in Go
```

You can also attach to a running `opencode serve` instance to avoid MCP server cold boot times on every run:

Terminal window

```auto
# Start a headless server in one terminal



opencode serve



# In another terminal, run commands that attach to it



opencode run --attach http://localhost:4096 "Explain async/await in JavaScript"
```

<a name="flags-2"></a>

##### [Flags](#flags-2)

| Flag | Short | Description |
| --- | --- | --- |
| `--command` |  | The command to run, use message for args |
| `--continue` | `-c` | Continue the last session |
| `--session` | `-s` | Session ID to continue |
| `--share` |  | Share the session |
| `--model` | `-m` | Model to use in the form of provider/model |
| `--agent` |  | Agent to use |
| `--file` | `-f` | File(s) to attach to message |
| `--format` |  | Format: default (formatted) or json (raw JSON events) |
| `--title` |  | Title for the session (uses truncated prompt if no value provided) |
| `--attach` |  | Attach to a running opencode server (e.g., <http://localhost:4096>) |
| `--port` |  | Port for the local server (defaults to random port) |

---

<a name="serve"></a>

#### [serve](#serve)

Start a headless opencode server for API access. Check out the [server docs](/docs/server) for the full HTTP interface.

Terminal window

```auto
opencode serve
```

This starts an HTTP server that provides API access to opencode functionality without the TUI interface.

##### [Flags](#flags-3)

| Flag | Short | Description |
| --- | --- | --- |
| `--port` | `-p` | Port to listen on |
| `--hostname` |  | Hostname to listen on |

---

#### [upgrade](#upgrade)

Updates opencode to the latest version or a specific version.

Terminal window

```auto
opencode upgrade [target]
```

To upgrade to the latest version.

Terminal window

```auto
opencode upgrade
```

To upgrade to a specific version.

Terminal window

```auto
opencode upgrade v0.1.48
```

<a name="flags-3"></a>

##### [Flags](#flags-4)

| Flag | Short | Description |
| --- | --- | --- |
| `--method` | `-m` | The installation method that was used; curl, npm, pnpm, bun, brew |

---

<a name="global-flags"></a>

### [Global Flags](#global-flags)

The opencode CLI takes the following global flags.

| Flag | Short | Description |
| --- | --- | --- |
| `--help` | `-h` | Display help |
| `--version` | `-v` | Print version number |
| `--print-logs` |  | Print logs to stderr |
| `--log-level` |  | Log level (DEBUG, INFO, WARN, ERROR) |

---

<a name="ide"></a>

## IDE

The OpenCode extension for VS Code, Cursor, and other IDEs

OpenCode integrates with VS Code, Cursor, or any IDE that supports a terminal. Just run `opencode` in the terminal to get started.

---

<a name="usage-1"></a>

### [Usage](#usage)

- **Quick Launch**: Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open OpenCode in a split terminal view, or focus an existing terminal session if one is already running.
- **New Session**: Use `Cmd+Shift+Esc` (Mac) or `Ctrl+Shift+Esc` (Windows/Linux) to start a new OpenCode terminal session, even if one is already open. You can also click the OpenCode button in the UI.
- **Context Awareness**: Automatically share your current selection or tab with OpenCode.
- **File Reference Shortcuts**: Use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Linux/Windows) to insert file references. For example, `@File#L37-42`.

---

<a name="installation"></a>

### [Installation](#installation)

To install OpenCode on VS Code and popular forks like Cursor, Windsurf, VSCodium:

1. Open VS Code
2. Open the integrated terminal
3. Run `opencode` - the extension installs automatically

If on the other hand you want to use your own IDE when you run `/editor` or `/export` from the TUI, you’ll need to set `export EDITOR="code --wait"`. [Learn more](/docs/tui/#editor-setup).

---

<a name="manual-install"></a>

#### [Manual Install](#manual-install)

Search for **OpenCode** in the Extension Marketplace and click **Install**.

---

<a name="troubleshooting-1"></a>

#### [Troubleshooting](#troubleshooting)

If the extension fails to install automatically:

- Ensure you’re running `opencode` in the integrated terminal.
- Confirm the CLI for your IDE is installed:
  - For VS Code: `code` command
  - For Cursor: `cursor` command
  - For Windsurf: `windsurf` command
  - For VSCodium: `codium` command
  - If not, run `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for “Shell Command: Install ‘code’ command in PATH” (or the equivalent for your IDE)
- Ensure VS Code has permission to install extensions

---

<a name="zen"></a>

## Zen

Curated list of models provided by OpenCode.

OpenCode Zen is a list of tested and verified models provided by the OpenCode team.

Note

OpenCode Zen is currently in beta.

Zen works like any other provider in OpenCode. You login to OpenCode Zen and get
your API key. It’s **completely optional** and you don’t need to use it to use
OpenCode.

---

<a name="background"></a>

### [Background](#background)

There are a large number of models out there but only a few of
these models work well as coding agents. Additionally, most providers are
configured very differently; so you get very different performance and quality.

Tip

We tested a select group of models and providers that work well with OpenCode.

So if you are using a model through something like OpenRouter, you can never be
sure if you are getting the best version of the model you want.

To fix this, we did a couple of things:

1. We tested a select group of models and talked to their teams about how to
   best run them.
2. We then worked with a few providers to make sure these were being served
   correctly.
3. Finally, we benchmarked the combination of the model/provider and came up
   with a list that we feel good recommending.

OpenCode Zen is an AI gateway that gives you access to these models.

---

<a name="how-it-works"></a>

### [How it works](#how-it-works)

OpenCode Zen works like any other provider in OpenCode.

1. You sign in to **[OpenCode Zen](https://opencode.ai/auth)**, add your billing
   details, and copy your API key.
2. You run `opencode auth login`, select opencode, and paste your API key.
3. Run `/models` in the TUI to see the list of models we recommend.

You are charged per request and you can add credits to your account.

---

<a name="endpoints"></a>

### [Endpoints](#endpoints)

You can also access our models through the following API endpoints.

| Model | Model ID | Endpoint | AI SDK Package |
| --- | --- | --- | --- |
| GPT 5.1 | gpt-5.1 | `https://opencode.ai/zen/v1/responses` | `@ai-sdk/openai` |
| GPT 5.1 Codex | gpt-5.1-codex | `https://opencode.ai/zen/v1/responses` | `@ai-sdk/openai` |
| GPT 5 | gpt-5 | `https://opencode.ai/zen/v1/responses` | `@ai-sdk/openai` |
| GPT 5 Codex | gpt-5-codex | `https://opencode.ai/zen/v1/responses` | `@ai-sdk/openai` |
| GPT 5 Nano | gpt-5-nano | `https://opencode.ai/zen/v1/responses` | `@ai-sdk/openai` |
| Claude Sonnet 4.5 | claude-sonnet-4-5 | `https://opencode.ai/zen/v1/messages` | `@ai-sdk/anthropic` |
| Claude Sonnet 4 | claude-sonnet-4 | `https://opencode.ai/zen/v1/messages` | `@ai-sdk/anthropic` |
| Claude Haiku 4.5 | claude-haiku-4-5 | `https://opencode.ai/zen/v1/messages` | `@ai-sdk/anthropic` |
| Claude Haiku 3.5 | claude-3-5-haiku | `https://opencode.ai/zen/v1/messages` | `@ai-sdk/anthropic` |
| Claude Opus 4.5 | claude-opus-4-5 | `https://opencode.ai/zen/v1/messages` | `@ai-sdk/anthropic` |
| Claude Opus 4.1 | claude-opus-4-1 | `https://opencode.ai/zen/v1/messages` | `@ai-sdk/anthropic` |
| Gemini 3 Pro | gemini-3-pro | `https://opencode.ai/zen/v1/models/gemini-3-pro` | `@ai-sdk/google` |
| GLM 4.6 | glm-4.6 | `https://opencode.ai/zen/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Kimi K2 | kimi-k2 | `https://opencode.ai/zen/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Kimi K2 Thinking | kimi-k2-thinking | `https://opencode.ai/zen/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Qwen3 Coder 480B | qwen3-coder | `https://opencode.ai/zen/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Grok Code Fast 1 | grok-code | `https://opencode.ai/zen/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Big Pickle | big-pickle | `https://opencode.ai/zen/v1/chat/completions` | `@ai-sdk/openai-compatible` |

The [model id](/docs/config/#models) in your OpenCode config
uses the format `opencode/<model-id>`. For example, for GPT 5.1 Codex, you would
use `opencode/gpt-5.1-codex` in your config.

---

<a name="models-1"></a>

#### [Models](#models)

You can fetch the full list of available models and their metadata from:

```auto
https://opencode.ai/zen/v1/models
```

---

### [Pricing](#pricing)

We support a pay-as-you-go model. Below are the prices **per 1M tokens**.

| Model | Input | Output | Cached Read | Cached Write |
| --- | --- | --- | --- | --- |
| Big Pickle | Free | Free | Free | - |
| Grok Code Fast 1 | Free | Free | Free | - |
| GLM 4.6 | $0.60 | $2.20 | $0.10 | - |
| Kimi K2 | $0.40 | $2.50 | - | - |
| Kimi K2 Thinking | $0.40 | $2.50 | - | - |
| Qwen3 Coder 480B | $0.45 | $1.50 | - | - |
| Claude Sonnet 4.5 (≤ 200K tokens) | $3.00 | $15.00 | $0.30 | $3.75 |
| Claude Sonnet 4.5 (> 200K tokens) | $6.00 | $22.50 | $0.60 | $7.50 |
| Claude Sonnet 4 (≤ 200K tokens) | $3.00 | $15.00 | $0.30 | $3.75 |
| Claude Sonnet 4 (> 200K tokens) | $6.00 | $22.50 | $0.60 | $7.50 |
| Claude Haiku 4.5 | $1.00 | $5.00 | $0.10 | $1.25 |
| Claude Haiku 3.5 | $0.80 | $4.00 | $0.08 | $1.00 |
| Claude Opus 4.5 | $5.00 | $25.00 | $0.50 | $6.25 |
| Claude Opus 4.1 | $15.00 | $75.00 | $1.50 | $18.75 |
| Gemini 3 Pro (≤ 200K tokens) | $2.00 | $12.00 | $0.20 | - |
| Gemini 3 Pro (> 200K tokens) | $4.00 | $18.00 | $0.40 | - |
| GPT 5.1 | $1.07 | $8.50 | $0.107 | - |
| GPT 5.1 Codex | $1.07 | $8.50 | $0.107 | - |
| GPT 5 | $1.07 | $8.50 | $0.107 | - |
| GPT 5 Codex | $1.07 | $8.50 | $0.107 | - |
| GPT 5 Nano | Free | Free | Free | - |

You might notice *Claude Haiku 3.5* in your usage history. This is a [low cost model](/docs/config/#models) that’s used to generate the titles of your sessions.

Note

Credit card fees are passed along at cost; we don’t charge anything beyond that.

The free models:

- Grok Code Fast 1 is currently free on OpenCode for a limited time. The xAI team is using this time to collect feedback and improve Grok Code.
- Big Pickle is a stealth model that’s free on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.

[Contact us](mailto:contact@anoma.ly) if you have any questions.

---

### [Privacy](#privacy)

All our models are hosted in the US. Our providers follow a zero-retention policy and do not use your data for model training, with the following exceptions:

- Grok Code Fast 1: During its free period, collected data may be used to improve Grok Code.
- Big Pickle: During its free period, collected data may be used to improve the model.
- OpenAI APIs: Requests are retained for 30 days in accordance with [OpenAI’s Data Policies](https://platform.openai.com/docs/guides/your-data).
- Anthropic APIs: Requests are retained for 30 days in accordance with [Anthropic’s Data Policies](https://docs.anthropic.com/en/docs/claude-code/data-usage).

---

### [For Teams](#for-teams)

Zen also works great for teams. You can invite teammates, assign roles, curate
the models your team uses, and more.

Note

Workspaces are currently free for teams as a part of the beta.

Managing your workspace is currently free for teams as a part of the beta. We’ll be
sharing more details on the pricing soon.

---

#### [Roles](#roles)

You can invite teammates to your workspace and assign roles:

- **Admin**: Manage models, members, API keys, and billing
- **Member**: Manage only their own API keys

Admins can also set monthly spending limits for each member to keep costs under control.

---

#### [Model access](#model-access)

Admins can enable or disable specific models for the workspace. Requests made to a disabled model will return an error.

This is useful for cases where you want to disable the use of a model that
collects data.

---

#### [Bring your own key](#bring-your-own-key)

You can use your own OpenAI or Anthropic API keys while still accessing other models in Zen.

When you use your own keys, tokens are billed directly by the provider, not by Zen.

For example, your organization might already have a key for OpenAI or Anthropic
and you want to use that instead of the one that Zen provides.

---

### [Goals](#goals)

We created OpenCode Zen to:

1. **Benchmark** the best models/providers for coding agents.
2. Have access to the **highest quality** options and not downgrade performance or route to cheaper providers.
3. Pass along any **price drops** by selling at cost; so the only markup is to cover our processing fees.
4. Have **no lock-in** by allowing you to use it with any other coding agent. And always let you use any other provider with OpenCode as well.

---

## Share

Share your OpenCode conversations.

OpenCode’s share feature allows you to create public links to your OpenCode conversations, so you can collaborate with teammates or get help from others.

Note

Shared conversations are publicly accessible to anyone with the link.

---

### [How it works](#how-it-works)

When you share a conversation, OpenCode:

1. Creates a unique public URL for your session
2. Syncs your conversation history to our servers
3. Makes the conversation accessible via the shareable link — `opencode.ai/s/<share-id>`

---

### [Sharing](#sharing)

OpenCode supports three sharing modes that control how conversations are shared:

---

#### [Manual (default)](#manual-default)

By default, OpenCode uses manual sharing mode. Sessions are not shared automatically, but you can manually share them using the `/share` command:

```auto
/share
```

This will generate a unique URL that’ll be copied to your clipboard.

To explicitly set manual mode in your [config file](/docs/config):

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"share": "manual"



}
```

---

#### [Auto-share](#auto-share)

You can enable automatic sharing for all new conversations by setting the `share` option to `"auto"` in your [config file](/docs/config):

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"share": "auto"



}
```

With auto-share enabled, every new conversation will automatically be shared and a link will be generated.

---

<a name="disabled"></a>

#### [Disabled](#disabled)

You can disable sharing entirely by setting the `share` option to `"disabled"` in your [config file](/docs/config):

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"share": "disabled"



}
```

To enforce this across your team for a given project, add it to the `opencode.json` in your project and check into Git.

---

### [Un-sharing](#un-sharing)

To stop sharing a conversation and remove it from public access:

```auto
/unshare
```

This will remove the share link and delete the data related to the conversation.

---

<a name="privacy"></a>

### [Privacy](#privacy)

There are a few things to keep in mind when sharing a conversation.

---

<a name="data-retention"></a>

#### [Data retention](#data-retention)

Shared conversations remain accessible until you explicitly unshare them. This
includes:

- Full conversation history
- All messages and responses
- Session metadata

---

<a name="recommendations"></a>

#### [Recommendations](#recommendations)

- Only share conversations that don’t contain sensitive information.
- Review conversation content before sharing.
- Unshare conversations when collaboration is complete.
- Avoid sharing conversations with proprietary code or confidential data.
- For sensitive projects, disable sharing entirely.

---

<a name="for-enterprises"></a>

### [For enterprises](#for-enterprises)

For enterprise deployments, the share feature can be:

- **Disabled** entirely for security compliance
- **Restricted** to users authenticated through SSO only
- **Self-hosted** on your own infrastructure

[Learn more](/docs/enterprise) about using opencode in your organization.

---

<a name="github"></a>

## GitHub

Use opencode in GitHub issues and pull-requests.

opencode integrates with your GitHub workflow. Mention `/opencode` or `/oc` in your comment, and opencode will execute tasks within your GitHub Actions runner.

---

<a name="features"></a>

### [Features](#features)

- **Triage issues**: Ask opencode to look into an issue and explain it to you.
- **Fix and implement**: Ask opencode to fix an issue or implement a feature. And it will work in a new branch and submits a PR with all the changes.
- **Secure**: opencode runs inside your GitHub’s runners.

---

<a name="installation-1"></a>

### [Installation](#installation)

Run the following command in a project that is in a GitHub repo:

Terminal window

```auto
opencode github install
```

This will walk you through installing the GitHub app, creating the workflow, and setting up secrets.

---

#### [Manual Setup](#manual-setup)

Or you can set it up manually.

1. **Install the GitHub app**

   Head over to [**github.com/apps/opencode-agent**](https://github.com/apps/opencode-agent). Make sure it’s installed on the target repository.
2. **Add the workflow**

   Add the following workflow file to `.github/workflows/opencode.yml` in your repo. Make sure to set the appropriate `model` and required API keys in `env`.

   .github/workflows/opencode.yml

   ```auto
   name: opencode



   on:



   issue_comment:



   types: [created]



   pull_request_review_comment:



   types: [created]



   jobs:



   opencode:



   if: |



   contains(github.event.comment.body, '/oc') ||



   contains(github.event.comment.body, '/opencode')



   runs-on: ubuntu-latest



   permissions:



   id-token: write



   steps:



   - name: Checkout repository



   uses: actions/checkout@v4



   with:



   fetch-depth: 1



   - name: Run opencode



   uses: sst/opencode/github@latest



   env:



   ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}



   with:



   model: anthropic/claude-sonnet-4-20250514



   # share: true



   # github_token: xxxx
   ```

3. **Store the API keys in secrets**

   In your organization or project **settings**, expand **Secrets and variables** on the left and select **Actions**. And add the required API keys.

---

<a name="configuration"></a>

### [Configuration](#configuration)

- `model`: The model to use with opencode. Takes the format of `provider/model`. This is **required**.
- `share`: Whether to share the opencode session. Defaults to **true** for public repositories.
- `token`: Optional GitHub access token for performing operations such as creating comments, committing changes, and opening pull requests. By default, opencode uses the installation access token from the opencode GitHub App, so commits, comments, and pull requests appear as coming from the app.

  Alternatively, you can use the GitHub Action runner’s [built-in `GITHUB_TOKEN`](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) without installing the opencode GitHub App. Just make sure to grant the required permissions in your workflow:

  ```auto
  permissions:



  id-token: write



  contents: write



  pull-requests: write



  issues: write
  ```

  You can also use a [personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)(PAT) if preferred.

---

### [Examples](#examples)

Here are some examples of how you can use opencode in GitHub.

- **Explain an issue**

  Add this comment in a GitHub issue.

  ```auto
  /opencode explain this issue
  ```

  opencode will read the entire thread, including all comments, and reply with a clear explanation.
- **Fix an issue**

  In a GitHub issue, say:

  ```auto
  /opencode fix this
  ```

  And opencode will create a new branch, implement the changes, and open a PR with the changes.
- **Review PRs and make changes**

  Leave the following comment on a GitHub PR.

  ```auto
  Delete the attachment from S3 when the note is removed /oc
  ```

  opencode will implement the requested change and commit it to the same PR.
- **Review specific code lines**

  Leave a comment directly on code lines in the PR’s “Files” tab. opencode automatically detects the file, line numbers, and diff context to provide precise responses.

  ```auto
  [Comment on specific lines in Files tab]



  /oc add error handling here
  ```

  When commenting on specific lines, opencode receives:

  - The exact file being reviewed
  - The specific lines of code
  - The surrounding diff context
  - Line number information

  This allows for more targeted requests without needing to specify file paths or line numbers manually.

---

## GitLab

Use opencode in GitLab issues and merge requests.

opencode integrates with your GitLab workflow.
Mention `@opencode` in a comment, and opencode will execute tasks within your GitLab CI pipeline.

---

### [Features](#features)

- **Triage issues**: Ask opencode to look into an issue and explain it to you.
- **Fix and implement**: Ask opencode to fix an issue or implement a feature.
  It will work create a new branch and raised a merge request with the changes.
- **Secure**: opencode runs on your GitLab runners.

---

### [Setup](#setup)

opencode runs in your GitLab CI/CD pipeline, here’s what you’ll need to set it up:

Tip

Check out the [**GitLab docs**](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/) for up to date instructions.

1. Configure your GitLab environment
2. Set up CI/CD
3. Get an AI model provider API key
4. Create a service account
5. Configure CI/CD variables
6. Create a flow config file, here’s an example:

   Flow configuration

   ```auto
   image: node:22-slim



   commands:



   - echo "Installing opencode"



   - npm install --global opencode-ai



   - echo "Installing glab"



   - export GITLAB_TOKEN=$GITLAB_TOKEN_OPENCODE



   - apt-get update --quiet && apt-get install --yes curl wget gpg git && rm --recursive --force /var/lib/apt/lists/*



   - curl --silent --show-error --location "https://raw.githubusercontent.com/upciti/wakemeops/main/assets/install_repository" | bash



   - apt-get install --yes glab



   - echo "Configuring glab"



   - echo $GITLAB_HOST



   - echo "Creating opencode auth configuration"



   - mkdir --parents ~/.local/share/opencode



   - |



   cat > ~/.local/share/opencode/auth.json << EOF



   {



   "anthropic": {



   "type": "api",



   "key": "$ANTHROPIC_API_KEY"



   }



   }



   EOF



   - echo "Configuring git"



   - git config --global user.email "opencode@gitlab.com"



   - git config --global user.name "Opencode"



   - echo "Testing glab"



   - glab issue list



   - echo "Running Opencode"



   - |



   opencode run "



   You are an AI assistant helping with GitLab operations.



   Context: $AI_FLOW_CONTEXT



   Task: $AI_FLOW_INPUT



   Event: $AI_FLOW_EVENT



   Please execute the requested task using the available GitLab tools.



   Be thorough in your analysis and provide clear explanations.



   <important>



   Please use the glab CLI to access data from GitLab. The glab CLI has already been authenticated. You can run the corresponding commands.



   If you are asked to summarize an MR or issue or asked to provide more information then please post back a note to the MR/Issue so that the user can see it.



   You don't need to commit or push up changes, those will be done automatically based on the file changes you make.



   </important>



   "



   - git checkout --branch $CI_WORKLOAD_REF origin/$CI_WORKLOAD_REF



   - echo "Checking for git changes and pushing if any exist"



   - |



   if ! git diff --quiet || ! git diff --cached --quiet || [ --not --zero "$(git ls-files --others --exclude-standard)" ]; then



   echo "Git changes detected, adding and pushing..."



   git add .



   if git diff --cached --quiet; then



   echo "No staged changes to commit"



   else



   echo "Committing changes to branch: $CI_WORKLOAD_REF"



   git commit --message "Codex changes"



   echo "Pushing changes up to $CI_WORKLOAD_REF"



   git push https://gitlab-ci-token:$GITLAB_TOKEN@$GITLAB_HOST/gl-demo-ultimate-dev-ai-epic-17570/test-java-project.git $CI_WORKLOAD_REF



   echo "Changes successfully pushed"



   fi



   else



   echo "No git changes detected, skipping push"



   fi



   variables:



   - ANTHROPIC_API_KEY



   - GITLAB_TOKEN_OPENCODE



   - GITLAB_HOST
   ```

You can refer to the [GitLab CLI agents docs](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/) for detailed instructions.

---

<a name="examples"></a>

### [Examples](#examples)

Here are some examples of how you can use opencode in GitLab.

Tip

You can configure to use a different trigger phrase than `@opencode`.

- **Explain an issue**

  Add this comment in a GitLab issue.

  ```auto
  @opencode explain this issue
  ```

  opencode will read the issue and reply with a clear explanation.
- **Fix an issue**

  In a GitLab issue, say:

  ```auto
  @opencode fix this
  ```

  opencode will create a new branch, implement the changes, and open a merge request with the changes.
- **Review merge requests**

  Leave the following comment on a GitLab merge request.

  ```auto
  @opencode review this merge request
  ```

  opencode will review the merge request and provide feedback.

---

## Tools

Manage the tools an LLM can use.

Tools allow the LLM to perform actions in your codebase. OpenCode comes with a set of built-in tools, but you can extend it with [custom tools](/docs/custom-tools) or [MCP servers](/docs/mcp-servers).

By default, all tools are **enabled** and don’t need permission to run. But you can configure this and control the [permissions](/docs/permissions) through your config.

---

### [Configure](#configure)

You can configure tools globally or per agent. Agent-specific configs override global settings.

By default, all tools are set to `true`. To disable a tool, set it to `false`.

---

#### [Global](#global)

Disable or enable tools globally using the `tools` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"write": false,



"bash": false,



"webfetch": true



}



}
```

You can also use wildcards to control multiple tools at once. For example, to disable all tools from an MCP server:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"mymcp_*": false



}



}
```

---

#### [Per agent](#per-agent)

Override global tool settings for specific agents using the `tools` config in the agent definition.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"write": true,



"bash": true



},



"agent": {



"plan": {



"tools": {



"write": false,



"bash": false



}



}



}



}
```

For example, here the `plan` agent overrides the global config to disable `write` and `bash` tools.

You can also configure tools for agents in Markdown.

~/.config/opencode/agent/readonly.md

```auto
---



description: Read-only analysis agent



mode: subagent



tools:



write: false



edit: false



bash: false



---



Analyze code without making any modifications.
```

[Learn more](/docs/agents#tools) about configuring tools per agent.

---

### [Built-in](#built-in)

Here are all the built-in tools available in OpenCode.

---

#### [bash](#bash)

Execute shell commands in your project environment.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"bash": true



}



}
```

This tool allows the LLM to run terminal commands like `npm install`, `git status`, or any other shell command.

---

<a name="edit"></a>

#### [edit](#edit)

Modify existing files using exact string replacements.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"edit": true



}



}
```

This tool performs precise edits to files by replacing exact text matches. It’s the primary way the LLM modifies code.

---

#### [write](#write)

Create new files or overwrite existing ones.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"write": true



}



}
```

Use this to allow the LLM to create new files. It will overwrite existing files if they already exist.

---

<a name="read"></a>

#### [read](#read)

Read file contents from your codebase.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"read": true



}



}
```

This tool reads files and returns their contents. It supports reading specific line ranges for large files.

---

#### [grep](#grep)

Search file contents using regular expressions.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"grep": true



}



}
```

Fast content search across your codebase. Supports full regex syntax and file pattern filtering.

---

<a name="glob"></a>

#### [glob](#glob)

Find files by pattern matching.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"glob": true



}



}
```

Search for files using glob patterns like `**/*.js` or `src/**/*.ts`. Returns matching file paths sorted by modification time.

---

#### [list](#list)

List files and directories in a given path.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"list": true



}



}
```

This tool lists directory contents. It accepts glob patterns to filter results.

---

<a name="patch"></a>

#### [patch](#patch)

Apply patches to files.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"patch": true



}



}
```

This tool applies patch files to your codebase. Useful for applying diffs and patches from various sources.

Tip

This tool is disabled for subagents by default, but you can enable it manually. [Learn more](/docs/agents/#tools)

---

#### [todowrite](#todowrite)

Manage todo lists during coding sessions.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"todowrite": true



}



}
```

Creates and updates task lists to track progress during complex operations. The LLM uses this to organize multi-step tasks.

Tip

This tool is disabled for subagents by default, but you can enable it manually. [Learn more](/docs/agents/#tools)

---

<a name="todoread"></a>

#### [todoread](#todoread)

Read existing todo lists.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"todoread": true



}



}
```

Reads the current todo list state. Used by the LLM to track what tasks are pending or completed.

---

#### [webfetch](#webfetch)

Fetch web content.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"webfetch": true



}



}
```

Allows the LLM to fetch and read web pages. Useful for looking up documentation or researching online resources.

---

<a name="custom-tools"></a>

### [Custom tools](#custom-tools)

Custom tools let you define your own functions that the LLM can call. These are defined in your config file and can execute arbitrary code.

[Learn more](/docs/custom-tools) about creating custom tools.

---

<a name="mcp-servers-1"></a>

### [MCP servers](#mcp-servers)

MCP (Model Context Protocol) servers allow you to integrate external tools and services. This includes database access, API integrations, and third-party services.

[Learn more](/docs/mcp-servers) about configuring MCP servers.

---

<a name="internals"></a>

### [Internals](#internals)

Internally, tools like `grep`, `glob`, and `list` use [ripgrep](https://github.com/BurntSushi/ripgrep) under the hood. By default, ripgrep respects `.gitignore` patterns, which means files and directories listed in your `.gitignore` will be excluded from searches and listings.

---

<a name="ignore-patterns"></a>

#### [Ignore patterns](#ignore-patterns)

To include files that would normally be ignored, create a `.ignore` file in your project root. This file can explicitly allow certain paths.

.ignore

```auto
!node_modules/



!dist/



!build/
```

For example, this `.ignore` file allows ripgrep to search within `node_modules/`, `dist/`, and `build/` directories even if they’re listed in `.gitignore`.

---

## Rules

Set custom instructions for opencode.

You can provide custom instructions to opencode by creating an `AGENTS.md` file. This is similar to `CLAUDE.md` or Cursor’s rules. It contains instructions that will be included in the LLM’s context to customize its behavior for your specific project.

---

### [Initialize](#initialize)

To create a new `AGENTS.md` file, you can run the `/init` command in opencode.

Tip

You should commit your project’s `AGENTS.md` file to Git.

This will scan your project and all its contents to understand what the project is about and generate an `AGENTS.md` file with it. This helps opencode to navigate the project better.

If you have an existing `AGENTS.md` file, this will try to add to it.

---

### [Example](#example)

You can also just create this file manually. Here’s an example of some things you can put into an `AGENTS.md` file.

AGENTS.md

```auto
# SST v3 Monorepo Project



This is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.



## Project Structure



- `packages/` - Contains all workspace packages (functions, core, web, etc.)



- `infra/` - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)



- `sst.config.ts` - Main SST configuration with dynamic imports



## Code Standards



- Use TypeScript with strict mode enabled



- Shared code goes in `packages/core/` with proper exports configuration



- Functions go in `packages/functions/`



- Infrastructure should be split into logical files in `infra/`



## Monorepo Conventions



- Import shared modules using workspace names: `@my-app/core/example`
```

We are adding project-specific instructions here and this will be shared across your team.

---

<a name="types"></a>

### [Types](#types)

opencode also supports reading the `AGENTS.md` file from multiple locations. And this serves different purposes.

<a name="project"></a>

#### [Project](#project)

The ones we have seen above, where the `AGENTS.md` is placed in the project root, are project-specific rules. These only apply when you are working in this directory or its sub-directories.

<a name="global"></a>

#### [Global](#global)

You can also have global rules in a `~/.config/opencode/AGENTS.md` file. This gets applied across all opencode sessions.

Since this isn’t committed to Git or shared with your team, we recommend using this to specify any personal rules that the LLM should follow.

---

<a name="precedence"></a>

### [Precedence](#precedence)

So when opencode starts, it looks for:

1. **Local files** by traversing up from the current directory
2. **Global file** by checking `~/.config/opencode/AGENTS.md`

If you have both global and project-specific rules, opencode will combine them together.

---

<a name="custom-instructions"></a>

### [Custom Instructions](#custom-instructions)

You can specify custom instruction files in your `opencode.json` or the global `~/.config/opencode/opencode.json`. This allows you and your team to reuse existing rules rather than having to duplicate them to AGENTS.md.

Example:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]



}
```

All instruction files are combined with your `AGENTS.md` files.

---

### [Referencing External Files](#referencing-external-files)

While opencode doesn’t automatically parse file references in `AGENTS.md`, you can achieve similar functionality in two ways:

#### [Using opencode.json](#using-opencodejson)

The recommended approach is to use the `instructions` field in `opencode.json`:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"instructions": ["docs/development-standards.md", "test/testing-guidelines.md", "packages/*/AGENTS.md"]



}
```

<a name="manual-instructions-in-agentsmd"></a>

#### [Manual Instructions in AGENTS.md](#manual-instructions-in-agentsmd)

You can teach opencode to read external files by providing explicit instructions in your `AGENTS.md`. Here’s a practical example:

AGENTS.md

```auto
<a name="typescript-project-rules"></a>
# TypeScript Project Rules



<a name="external-file-loading"></a>
## External File Loading



CRITICAL: When you encounter a file reference (e.g., @rules/general.md), use your Read tool to load it on a need-to-know basis. They're relevant to the SPECIFIC task at hand.



Instructions:



- Do NOT preemptively load all references - use lazy loading based on actual need



- When loaded, treat content as mandatory instructions that override defaults



- Follow references recursively when needed



<a name="development-guidelines"></a>
## Development Guidelines



For TypeScript code style and best practices: @docs/typescript-guidelines.md



For React component architecture and hooks patterns: @docs/react-patterns.md



For REST API design and error handling: @docs/api-standards.md



For testing strategies and coverage requirements: @test/testing-guidelines.md



<a name="general-guidelines"></a>
## General Guidelines



Read the following file immediately as it's relevant to all workflows: @rules/general-guidelines.md.
```

This approach allows you to:

- Create modular, reusable rule files
- Share rules across projects via symlinks or git submodules
- Keep AGENTS.md concise while referencing detailed guidelines
- Ensure opencode loads files only when needed for the specific task

Tip

For monorepos or projects with shared standards, using `opencode.json` with glob patterns (like `packages/*/AGENTS.md`) is more maintainable than manual instructions.

---

## Agents

Configure and use specialized agents.

Agents are specialized AI assistants that can be configured for specific tasks and workflows. They allow you to create focused tools with custom prompts, models, and tool access.

Tip

Use the plan agent to analyze code and review suggestions without making any code changes.

You can switch between agents during a session or invoke them with the `@` mention.

---

### [Types](#types)

There are two types of agents in OpenCode; primary agents and subagents.

---

#### [Primary agents](#primary-agents)

Primary agents are the main assistants you interact with directly. You can cycle through them using the **Tab** key, or your configured `switch_agent` keybind. These agents handle your main conversation and can access all configured tools.

Tip

You can use the **Tab** key to switch between primary agents during a session.

OpenCode comes with two built-in primary agents, **Build** and **Plan**. We’ll
look at these below.

---

#### [Subagents](#subagents)

Subagents are specialized assistants that primary agents can invoke for specific tasks. You can also manually invoke them by **@ mentioning** them in your messages.

OpenCode comes with one built-in subagent, **General**. We’ll look at this below.

---

### [Built-in](#built-in)

OpenCode comes with two built-in primary agents and one built-in subagent.

---

#### [Build](#build)

*Mode*: `primary`

Build is the **default** primary agent with all tools enabled. This is the standard agent for development work where you need full access to file operations and system commands.

---

#### [Plan](#plan)

*Mode*: `primary`

A restricted agent designed for planning and analysis. We use a permission system to give you more control and prevent unintended changes.
By default, all of the following are set to `ask`:

- `file edits`: All writes, patches, and edits
- `bash`: All bash commands

This agent is useful when you want the LLM to analyze code, suggest changes, or create plans without making any actual modifications to your codebase.

---

#### [General](#general)

*Mode*: `subagent`

A general-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. Use when searching for keywords or files and you’re not confident you’ll find the right match in the first few tries.

---

### [Usage](#usage)

1. For primary agents, use the **Tab** key to cycle through them during a session. You can also use your configured `switch_agent` keybind.
2. Subagents can be invoked:

   - **Automatically** by primary agents for specialized tasks based on their descriptions.
   - Manually by **@ mentioning** a subagent in your message. For example.

     ```auto
     @general help me search for this function
     ```

3. **Navigation between sessions**: When subagents create their own child sessions, you can navigate between the parent session and all child sessions using:

   - **<Leader>+Right** (or your configured `session_child_cycle` keybind) to cycle forward through parent → child1 → child2 → … → parent
   - **<Leader>+Left** (or your configured `session_child_cycle_reverse` keybind) to cycle backward through parent ← child1 ← child2 ← … ← parent

   This allows you to seamlessly switch between the main conversation and specialized subagent work.

---

<a name="configure-2"></a>

### [Configure](#configure)

You can customize the built-in agents or create your own through configuration. Agents can be configured in two ways:

---

<a name="json"></a>

#### [JSON](#json)

Configure agents in your `opencode.json` config file:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"agent": {



"build": {



"mode": "primary",



"model": "anthropic/claude-sonnet-4-20250514",



"prompt": "{file:./prompts/build.txt}",



"tools": {



"write": true,



"edit": true,



"bash": true



}



},



"plan": {



"mode": "primary",



"model": "anthropic/claude-haiku-4-20250514",



"tools": {



"write": false,



"edit": false,



"bash": false



}



},



"code-reviewer": {



"description": "Reviews code for best practices and potential issues",



"mode": "subagent",



"model": "anthropic/claude-sonnet-4-20250514",



"prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",



"tools": {



"write": false,



"edit": false



}



}



}



}
```

---

#### [Markdown](#markdown)

You can also define agents using markdown files. Place them in:

- Global: `~/.config/opencode/agent/`
- Per-project: `.opencode/agent/`

~/.config/opencode/agent/review.md

```auto
---



description: Reviews code for quality and best practices



mode: subagent



model: anthropic/claude-sonnet-4-20250514



temperature: 0.1



tools:



write: false



edit: false



bash: false



---



You are in code review mode. Focus on:



- Code quality and best practices



- Potential bugs and edge cases



- Performance implications



- Security considerations



Provide constructive feedback without making direct changes.
```

The markdown file name becomes the agent name. For example, `review.md` creates a `review` agent.

---

<a name="options"></a>

### [Options](#options)

Let’s look at these configuration options in detail.

---

<a name="description"></a>

#### [Description](#description)

Use the `description` option to provide a brief description of what the agent does and when to use it.

opencode.json

```auto
{



"agent": {



"review": {



"description": "Reviews code for best practices and potential issues"



}



}



}
```

This is a **required** config option.

---

#### [Temperature](#temperature)

Control the randomness and creativity of the LLM’s responses with the `temperature` config.

Lower values make responses more focused and deterministic, while higher values increase creativity and variability.

opencode.json

```auto
{



"agent": {



"plan": {



"temperature": 0.1



},



"creative": {



"temperature": 0.8



}



}



}
```

Temperature values typically range from 0.0 to 1.0:

- **0.0-0.2**: Very focused and deterministic responses, ideal for code analysis and planning
- **0.3-0.5**: Balanced responses with some creativity, good for general development tasks
- **0.6-1.0**: More creative and varied responses, useful for brainstorming and exploration

opencode.json

```auto
{



"agent": {



"analyze": {



"temperature": 0.1,



"prompt": "{file:./prompts/analysis.txt}"



},



"build": {



"temperature": 0.3



},



"brainstorm": {



"temperature": 0.7,



"prompt": "{file:./prompts/creative.txt}"



}



}



}
```

If no temperature is specified, OpenCode uses model-specific defaults; typically 0 for most models, 0.55 for Qwen models.

---

#### [Disable](#disable)

Set to `true` to disable the agent.

opencode.json

```auto
{



"agent": {



"review": {



"disable": true



}



}



}
```

---

<a name="prompt"></a>

#### [Prompt](#prompt)

Specify a custom system prompt file for this agent with the `prompt` config. The prompt file should contain instructions specific to the agent’s purpose.

opencode.json

```auto
{



"agent": {



"review": {



"prompt": "{file:./prompts/code-review.txt}"



}



}



}
```

This path is relative to where the config file is located. So this works for both the global OpenCode config and the project specific config.

---

#### [Model](#model)

Use the `model` config to override the default model for this agent. Useful for using different models optimized for different tasks. For example, a faster model for planning, a more capable model for implementation.

opencode.json

```auto
{



"agent": {



"plan": {



"model": "anthropic/claude-haiku-4-20250514"



}



}



}
```

---

<a name="tools-1"></a>

#### [Tools](#tools)

Control which tools are available in this agent with the `tools` config. You can enable or disable specific tools by setting them to `true` or `false`.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"tools": {



"write": true,



"bash": true



},



"agent": {



"plan": {



"tools": {



"write": false,



"bash": false



}



}



}



}
```

Note

The agent-specific config overrides the global config.

You can also use wildcards to control multiple tools at once. For example, to disable all tools from an MCP server:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"agent": {



"readonly": {



"tools": {



"mymcp_*": false,



"write": false,



"edit": false



}



}



}



}
```

[Learn more about tools](/docs/tools).

---

<a name="permissions"></a>

#### [Permissions](#permissions)

You can configure permissions to manage what actions an agent can take. Currently, the permissions for the `edit`, `bash`, and `webfetch` tools can be configured to:

- `"ask"` — Prompt for approval before running the tool
- `"allow"` — Allow all operations without approval
- `"deny"` — Disable the tool

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"edit": "deny"



}



}
```

You can override these permissions per agent.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"edit": "deny"



},



"agent": {



"build": {



"permission": {



"edit": "ask"



}



}



}



}
```

You can also set permissions in Markdown agents.

~/.config/opencode/agent/review.md

```auto
---



description: Code review without edits



mode: subagent



permission:



edit: deny



bash:



"git diff": allow



"git log*": allow



"*": ask



webfetch: deny



---



Only analyze code and suggest changes.
```

You can set permissions for specific bash commands.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"agent": {



"build": {



"permission": {



"bash": {



"git push": "ask"



}



}



}



}



}
```

This can take a glob pattern.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"agent": {



"build": {



"permission": {



"bash": {



"git *": "ask"



}



}



}



}



}
```

And you can also use the `*` wildcard to manage permissions for all commands.
Where the specific rule can override the `*` wildcard.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"agent": {



"build": {



"permission": {



"bash": {



"git status": "allow",



"*": "ask"



}



}



}



}



}
```

[Learn more about permissions](/docs/permissions).

---

<a name="mode"></a>

#### [Mode](#mode)

Control the agent’s mode with the `mode` config. The `mode` option is used to determine how the agent can be used.

opencode.json

```auto
{



"agent": {



"review": {



"mode": "subagent"



}



}



}
```

The `mode` option can be set to `primary`, `subagent`, or `all`. If no `mode` is specified, it defaults to `all`.

---

#### [Additional](#additional)

Any other options you specify in your agent configuration will be **passed through directly** to the provider as model options. This allows you to use provider-specific features and parameters.

For example, with OpenAI’s reasoning models, you can control the reasoning effort:

opencode.json

```auto
{



"agent": {



"deep-thinker": {



"description": "Agent that uses high reasoning effort for complex problems",



"model": "openai/gpt-5",



"reasoningEffort": "high",



"textVerbosity": "low"



}



}



}
```

These additional options are model and provider-specific. Check your provider’s documentation for available parameters.

Tip

Run `opencode models` to see a list of the available models.

---

<a name="create-agents"></a>

### [Create agents](#create-agents)

You can create new agents using the following command:

Terminal window

```auto
opencode agent create
```

This interactive command will:

1. Ask where to save the agent; global or project-specific.
2. Description of what the agent should do.
3. Generate an appropriate system prompt and identifier.
4. Let you select which tools the agent can access.
5. Finally, create a markdown file with the agent configuration.

---

### [Use cases](#use-cases)

Here are some common use cases for different agents.

- **Build agent**: Full development work with all tools enabled
- **Plan agent**: Analysis and planning without making changes
- **Review agent**: Code review with read-only access plus documentation tools
- **Debug agent**: Focused on investigation with bash and read tools enabled
- **Docs agent**: Documentation writing with file operations but no system commands

---

### [Examples](#examples)

Here are some examples agents you might find useful.

Tip

Do you have an agent you’d like to share? [Submit a PR](https://github.com/sst/opencode).

---

#### [Documentation agent](#documentation-agent)

~/.config/opencode/agent/docs-writer.md

```auto
---



description: Writes and maintains project documentation



mode: subagent



tools:



bash: false



---



You are a technical writer. Create clear, comprehensive documentation.



Focus on:



- Clear explanations



- Proper structure



- Code examples



- User-friendly language
```

---

<a name="security-auditor"></a>

#### [Security auditor](#security-auditor)

~/.config/opencode/agent/security-auditor.md

```auto
---



description: Performs security audits and identifies vulnerabilities



mode: subagent



tools:



write: false



edit: false



---



You are a security expert. Focus on identifying potential security issues.



Look for:



- Input validation vulnerabilities



- Authentication and authorization flaws



- Data exposure risks



- Dependency vulnerabilities



- Configuration security issues
```

---

## Models

Configuring an LLM provider and model.

OpenCode uses the [AI SDK](https://ai-sdk.dev/) and [Models.dev](https://models.dev) to support for **75+ LLM providers** and it supports running local models.

---

### [Providers](#providers)

Most popular providers are preloaded by default. If you’ve added the credentials for a provider through `opencode auth login`, they’ll be available when you start OpenCode.

Learn more about [providers](/docs/providers).

---

### [Select a model](#select-a-model)

Once you’ve configured your provider you can select the model you want by typing in:

```auto
/models
```

---

<a name="recommended-models"></a>

### [Recommended models](#recommended-models)

There are a lot of models out there, with new models coming out every week.

Tip

Consider using one of the models we recommend.

However, there are only a few of them that are good at both generating code and tool calling.

Here are several models that work well with OpenCode, in no particular order. (This is not an exhaustive list):

- GPT 5.1
- GPT 5.1 Codex
- Claude Sonnet 4.5
- Claude Haiku 4.5
- Kimi K2
- GLM 4.6
- Qwen3 Coder
- Gemini 3 Pro

---

<a name="set-a-default"></a>

### [Set a default](#set-a-default)

To set one of these as the default model, you can set the `model` key in your
OpenCode config.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"model": "lmstudio/google/gemma-3n-e4b"



}
```

Here the full ID is `provider_id/model_id`.

If you’ve configured a [custom provider](/docs/providers#custom), the `provider_id` is key from the `provider` part of your config, and the `model_id` is the key from `provider.models`.

---

### [Configure models](#configure-models)

You can globally configure a model’s options through the config.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"openai": {



"models": {



"gpt-5": {



"options": {



"reasoningEffort": "high",



"textVerbosity": "low",



"reasoningSummary": "auto",



"include": ["reasoning.encrypted_content"],



},



},



},



},



"anthropic": {



"models": {



"claude-sonnet-4-5-20250929": {



"options": {



"thinking": {



"type": "enabled",



"budgetTokens": 16000,



},



},



},



},



},



},



}
```

Here we’re configuring global settings for two built-in models: `gpt-5` when accessed via the `openai` provider, and `claude-sonnet-4-20250514` when accessed via the `anthropic` provider.
The built-in provider and model names can be found on [Models.dev](https://models.dev).

You can also configure these options for any agents that you are using. The agent config overrides any global options here. [Learn more](/docs/agents/#additional).

You can also define custom models that extend built-in ones and can optionally use specific options by referring to their id:

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"provider": {



"opencode": {



"models": {



"gpt-5-high": {



"id": "gpt-5",



"options": {



"reasoningEffort": "high",



"textVerbosity": "low",



"reasoningSummary": "auto",



},



},



"gpt-5-low": {



"id": "gpt-5",



"options": {



"reasoningEffort": "low",



"textVerbosity": "low",



"reasoningSummary": "auto",



},



},



},



},



},



}
```

---

### [Loading models](#loading-models)

When OpenCode starts up, it checks for models in the following priority order:

1. The `--model` or `-m` command line flag. The format is the same as in the config file: `provider_id/model_id`.
2. The model list in the OpenCode config.

   opencode.json

   ```auto
   {



   "$schema": "https://opencode.ai/config.json",



   "model": "anthropic/claude-sonnet-4-20250514"



   }
   ```

   The format here is `provider/model`.
3. The last used model.
4. The first model using an internal priority.

---

<a name="themes-2"></a>

## Themes

Select a built-in theme or define your own.

With OpenCode you can select from one of several built-in themes, use a theme that adapts to your terminal theme, or define your own custom theme.

By default, OpenCode uses our own `opencode` theme.

---

<a name="terminal-requirements"></a>

### [Terminal requirements](#terminal-requirements)

For themes to display correctly with their full color palette, your terminal must support **truecolor** (24-bit color). Most modern terminals support this by default, but you may need to enable it:

- **Check support**: Run `echo $COLORTERM` - it should output `truecolor` or `24bit`
- **Enable truecolor**: Set the environment variable `COLORTERM=truecolor` in your shell profile
- **Terminal compatibility**: Ensure your terminal emulator supports 24-bit color (most modern terminals like iTerm2, Alacritty, Kitty, Windows Terminal, and recent versions of GNOME Terminal do)

Without truecolor support, themes may appear with reduced color accuracy or fall back to the nearest 256-color approximation.

---

<a name="built-in-themes"></a>

### [Built-in themes](#built-in-themes)

OpenCode comes with several built-in themes.

| Name | Description |
| --- | --- |
| `system` | Adapts to your terminal’s background color |
| `tokyonight` | Based on the [Tokyonight](https://github.com/folke/tokyonight.nvim) theme |
| `everforest` | Based on the [Everforest](https://github.com/sainnhe/everforest) theme |
| `ayu` | Based on the [Ayu](https://github.com/ayu-theme) dark theme |
| `catppuccin` | Based on the [Catppuccin](https://github.com/catppuccin) theme |
| `gruvbox` | Based on the [Gruvbox](https://github.com/morhetz/gruvbox) theme |
| `kanagawa` | Based on the [Kanagawa](https://github.com/rebelot/kanagawa.nvim) theme |
| `nord` | Based on the [Nord](https://github.com/nordtheme/nord) theme |
| `matrix` | Hacker-style green on black theme |
| `one-dark` | Based on the [Atom One](https://github.com/Th3Whit3Wolf/one-nvim) Dark theme |

And more, we are constantly adding new themes.

---

<a name="system-theme"></a>

### [System theme](#system-theme)

The `system` theme is designed to automatically adapt to your terminal’s color scheme. Unlike traditional themes that use fixed colors, the *system* theme:

- **Generates gray scale**: Creates a custom gray scale based on your terminal’s background color, ensuring optimal contrast.
- **Uses ANSI colors**: Leverages standard ANSI colors (0-15) for syntax highlighting and UI elements, which respect your terminal’s color palette.
- **Preserves terminal defaults**: Uses `none` for text and background colors to maintain your terminal’s native appearance.

The system theme is for users who:

- Want OpenCode to match their terminal’s appearance
- Use custom terminal color schemes
- Prefer a consistent look across all terminal applications

---

<a name="using-a-theme"></a>

### [Using a theme](#using-a-theme)

You can select a theme by bringing up the theme select with the `/theme` command. Or you can specify it in your [config](/docs/config).

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"theme": "tokyonight"



}
```

---

### [Custom themes](#custom-themes)

OpenCode supports a flexible JSON-based theme system that allows users to create and customize themes easily.

---

#### [Hierarchy](#hierarchy)

Themes are loaded from multiple directories in the following order where later directories override earlier ones:

1. **Built-in themes** - These are embedded in the binary
2. **User config directory** - Defined in `~/.config/opencode/themes/*.json` or `$XDG_CONFIG_HOME/opencode/themes/*.json`
3. **Project root directory** - Defined in the `<project-root>/.opencode/themes/*.json`
4. **Current working directory** - Defined in `./.opencode/themes/*.json`

If multiple directories contain a theme with the same name, the theme from the directory with higher priority will be used.

---

#### [Creating a theme](#creating-a-theme)

To create a custom theme, create a JSON file in one of the theme directories.

For user-wide themes:

Terminal window

```auto
mkdir -p ~/.config/opencode/themes



vim ~/.config/opencode/themes/my-theme.json
```

And for project-specific themes.

Terminal window

```auto
mkdir -p .opencode/themes



vim .opencode/themes/my-theme.json
```

---

#### [JSON format](#json-format)

Themes use a flexible JSON format with support for:

- **Hex colors**: `"#ffffff"`
- **ANSI colors**: `3` (0-255)
- **Color references**: `"primary"` or custom definitions
- **Dark/light variants**: `{"dark": "#000", "light": "#fff"}`
- **No color**: `"none"` - Uses the terminal’s default color or transparent

---

#### [Color definitions](#color-definitions)

The `defs` section is optional and it allows you to define reusable colors that can be referenced in the theme.

---

#### [Terminal defaults](#terminal-defaults)

The special value `"none"` can be used for any color to inherit the terminal’s default color. This is particularly useful for creating themes that blend seamlessly with your terminal’s color scheme:

- `"text": "none"` - Uses terminal’s default foreground color
- `"background": "none"` - Uses terminal’s default background color

---

#### [Example](#example)

Here’s an example of a custom theme:

my-theme.json

```auto
{



"$schema": "https://opencode.ai/theme.json",



"defs": {



"nord0": "#2E3440",



"nord1": "#3B4252",



"nord2": "#434C5E",



"nord3": "#4C566A",



"nord4": "#D8DEE9",



"nord5": "#E5E9F0",



"nord6": "#ECEFF4",



"nord7": "#8FBCBB",



"nord8": "#88C0D0",



"nord9": "#81A1C1",



"nord10": "#5E81AC",



"nord11": "#BF616A",



"nord12": "#D08770",



"nord13": "#EBCB8B",



"nord14": "#A3BE8C",



"nord15": "#B48EAD"



},



"theme": {



"primary": {



"dark": "nord8",



"light": "nord10"



},



"secondary": {



"dark": "nord9",



"light": "nord9"



},



"accent": {



"dark": "nord7",



"light": "nord7"



},



"error": {



"dark": "nord11",



"light": "nord11"



},



"warning": {



"dark": "nord12",



"light": "nord12"



},



"success": {



"dark": "nord14",



"light": "nord14"



},



"info": {



"dark": "nord8",



"light": "nord10"



},



"text": {



"dark": "nord4",



"light": "nord0"



},



"textMuted": {



"dark": "nord3",



"light": "nord1"



},



"background": {



"dark": "nord0",



"light": "nord6"



},



"backgroundPanel": {



"dark": "nord1",



"light": "nord5"



},



"backgroundElement": {



"dark": "nord1",



"light": "nord4"



},



"border": {



"dark": "nord2",



"light": "nord3"



},



"borderActive": {



"dark": "nord3",



"light": "nord2"



},



"borderSubtle": {



"dark": "nord2",



"light": "nord3"



},



"diffAdded": {



"dark": "nord14",



"light": "nord14"



},



"diffRemoved": {



"dark": "nord11",



"light": "nord11"



},



"diffContext": {



"dark": "nord3",



"light": "nord3"



},



"diffHunkHeader": {



"dark": "nord3",



"light": "nord3"



},



"diffHighlightAdded": {



"dark": "nord14",



"light": "nord14"



},



"diffHighlightRemoved": {



"dark": "nord11",



"light": "nord11"



},



"diffAddedBg": {



"dark": "#3B4252",



"light": "#E5E9F0"



},



"diffRemovedBg": {



"dark": "#3B4252",



"light": "#E5E9F0"



},



"diffContextBg": {



"dark": "nord1",



"light": "nord5"



},



"diffLineNumber": {



"dark": "nord2",



"light": "nord4"



},



"diffAddedLineNumberBg": {



"dark": "#3B4252",



"light": "#E5E9F0"



},



"diffRemovedLineNumberBg": {



"dark": "#3B4252",



"light": "#E5E9F0"



},



"markdownText": {



"dark": "nord4",



"light": "nord0"



},



"markdownHeading": {



"dark": "nord8",



"light": "nord10"



},



"markdownLink": {



"dark": "nord9",



"light": "nord9"



},



"markdownLinkText": {



"dark": "nord7",



"light": "nord7"



},



"markdownCode": {



"dark": "nord14",



"light": "nord14"



},



"markdownBlockQuote": {



"dark": "nord3",



"light": "nord3"



},



"markdownEmph": {



"dark": "nord12",



"light": "nord12"



},



"markdownStrong": {



"dark": "nord13",



"light": "nord13"



},



"markdownHorizontalRule": {



"dark": "nord3",



"light": "nord3"



},



"markdownListItem": {



"dark": "nord8",



"light": "nord10"



},



"markdownListEnumeration": {



"dark": "nord7",



"light": "nord7"



},



"markdownImage": {



"dark": "nord9",



"light": "nord9"



},



"markdownImageText": {



"dark": "nord7",



"light": "nord7"



},



"markdownCodeBlock": {



"dark": "nord4",



"light": "nord0"



},



"syntaxComment": {



"dark": "nord3",



"light": "nord3"



},



"syntaxKeyword": {



"dark": "nord9",



"light": "nord9"



},



"syntaxFunction": {



"dark": "nord8",



"light": "nord8"



},



"syntaxVariable": {



"dark": "nord7",



"light": "nord7"



},



"syntaxString": {



"dark": "nord14",



"light": "nord14"



},



"syntaxNumber": {



"dark": "nord15",



"light": "nord15"



},



"syntaxType": {



"dark": "nord7",



"light": "nord7"



},



"syntaxOperator": {



"dark": "nord9",



"light": "nord9"



},



"syntaxPunctuation": {



"dark": "nord4",



"light": "nord0"



}



}



}
```

---

<a name="keybinds-1"></a>

## Keybinds

Customize your keybinds.

OpenCode has a list of keybinds that you can customize through the OpenCode config.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"keybinds": {



"leader": "ctrl+x",



"app_exit": "ctrl+c,ctrl+d,<leader>q",



"editor_open": "<leader>e",



"theme_list": "<leader>t",



"sidebar_toggle": "<leader>b",



"status_view": "<leader>s",



"session_export": "<leader>x",



"session_new": "<leader>n",



"session_list": "<leader>l",



"session_timeline": "<leader>g",



"session_share": "none",



"session_unshare": "none",



"session_interrupt": "escape",



"session_compact": "<leader>c",



"session_child_cycle": "<leader>+right",



"session_child_cycle_reverse": "<leader>+left",



"messages_page_up": "pageup",



"messages_page_down": "pagedown",



"messages_half_page_up": "ctrl+alt+u",



"messages_half_page_down": "ctrl+alt+d",



"messages_first": "ctrl+g,home",



"messages_last": "ctrl+alt+g,end",



"messages_copy": "<leader>y",



"messages_undo": "<leader>u",



"messages_redo": "<leader>r",



"messages_toggle_conceal": "<leader>h",



"model_list": "<leader>m",



"model_cycle_recent": "f2",



"model_cycle_recent_reverse": "shift+f2",



"command_list": "ctrl+p",



"agent_list": "<leader>a",



"agent_cycle": "tab",



"agent_cycle_reverse": "shift+tab",



"input_clear": "ctrl+c",



"input_forward_delete": "ctrl+d",



"input_paste": "ctrl+v",



"input_submit": "enter",



"input_newline": "shift+enter,ctrl+j",



"history_previous": "up",



"history_next": "down"



}



}
```

---

### [Leader key](#leader-key)

OpenCode uses a `leader` key for most keybinds. This avoids conflicts in your terminal.

By default, `ctrl+x` is the leader key and most actions require you to first press the leader key and then the shortcut. For example, to start a new session you first press `ctrl+x` and then press `n`.

You don’t need to use a leader key for your keybinds but we recommend doing so.

---

### [Disable keybind](#disable-keybind)

You can disable a keybind by adding the key to your config with a value of “none”.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"keybinds": {



"session_compact": "none"



}



}
```

---

<a name="commands-1"></a>

## Commands

Create custom commands for repetitive tasks.

Custom commands let you specify a prompt you want to run when that command is executed in the TUI.

```auto
/my-command
```

Custom commands are in addition to the built-in commands like `/init`, `/undo`, `/redo`, `/share`, `/help`. [Learn more](/docs/tui#commands).

---

### [Create command files](#create-command-files)

Create markdown files in the `command/` directory to define custom commands.

Create `.opencode/command/test.md`:

.opencode/command/test.md

```auto
---



description: Run tests with coverage



agent: build



model: anthropic/claude-3-5-sonnet-20241022



---



Run the full test suite with coverage report and show any failures.



Focus on the failing tests and suggest fixes.
```

The frontmatter defines command properties. The content becomes the template.

Use the command by typing `/` followed by the command name.

```auto
"/test"
```

---

### [Configure](#configure)

You can add custom commands through the OpenCode config or by creating markdown files in the `command/` directory.

---

#### [JSON](#json)

Use the `command` option in your OpenCode [config](/docs/config):

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"command": {



// This becomes the name of the command



"test": {



// This is the prompt that will be sent to the LLM



"template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",



// This is show as the description in the TUI



"description": "Run tests with coverage",



"agent": "build",



"model": "anthropic/claude-3-5-sonnet-20241022"



}



}



}
```

Now you can run this command in the TUI:

```auto
/test
```

---

#### [Markdown](#markdown)

You can also define commands using markdown files. Place them in:

- Global: `~/.config/opencode/command/`
- Per-project: `.opencode/command/`

~/.config/opencode/command/test.md

```auto
---



description: Run tests with coverage



agent: build



model: anthropic/claude-3-5-sonnet-20241022



---



Run the full test suite with coverage report and show any failures.



Focus on the failing tests and suggest fixes.
```

The markdown file name becomes the command name. For example, `test.md` lets
you run:

```auto
/test
```

---

### [Prompt config](#prompt-config)

The prompts for the custom commands support several special placeholders and syntax.

---

#### [Arguments](#arguments)

Pass arguments to commands using the `$ARGUMENTS` placeholder.

.opencode/command/component.md

```auto
---



description: Create a new component



---



Create a new React component named $ARGUMENTS with TypeScript support.



Include proper typing and basic structure.
```

Run the command with arguments:

```auto
/component Button
```

And `$ARGUMENTS` will be replaced with `Button`.

You can also access individual arguments using positional parameters:

- `$1` - First argument
- `$2` - Second argument
- `$3` - Third argument
- And so on…

For example:

.opencode/command/create-file.md

```auto
---



description: Create a new file with content



---



Create a file named $1 in the directory $2



with the following content: $3
```

Run the command:

```auto
/create-file config.json src "{ \"key\": \"value\" }"
```

This replaces:

- `$1` with `config.json`
- `$2` with `src`
- `$3` with `{ "key": "value" }`

---

#### [Shell output](#shell-output)

Use *!`command`* to inject [bash command](/docs/tui#bash-commands) output into your prompt.

For example, to create a custom command that analyzes test coverage:

.opencode/command/analyze-coverage.md

```auto
---



description: Analyze test coverage



---



Here are the current test results:



!`npm test`



Based on these results, suggest improvements to increase coverage.
```

Or to review recent changes:

.opencode/command/review-changes.md

```auto
---



description: Review recent changes



---



Recent git commits:



!`git log --oneline -10`



Review these changes and suggest any improvements.
```

Commands run in your project’s root directory and their output becomes part of the prompt.

---

#### [File references](#file-references)

Include files in your command using `@` followed by the filename.

.opencode/command/review-component.md

```auto
---



description: Review component



---



Review the component in @src/components/Button.tsx.



Check for performance issues and suggest improvements.
```

The file content gets included in the prompt automatically.

---

<a name="options-1"></a>

### [Options](#options)

Let’s look at the configuration options in detail.

---

<a name="template"></a>

#### [Template](#template)

The `template` option defines the prompt that will be sent to the LLM when the command is executed.

opencode.json

```auto
{



"command": {



"test": {



"template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes."



}



}



}
```

This is a **required** config option.

---

#### [Description](#description)

Use the `description` option to provide a brief description of what the command does.

opencode.json

```auto
{



"command": {



"test": {



"description": "Run tests with coverage"



}



}



}
```

This is shown as the description in the TUI when you type in the command.

---

<a name="agent-1"></a>

#### [Agent](#agent)

Use the `agent` config to optionally specify which [agent](/docs/agents) should execute this command.
If this is a [subagent](/docs/agents/#subagents) the command will trigger a subagent invocation by default.
To disable this behavior, set `subtask` to `false`.

opencode.json

```auto
{



"command": {



"review": {



"agent": "plan"



}



}



}
```

This is an **optional** config option. If not specified, defaults to your current agent.

---

#### [Subtask](#subtask)

Use the `subtask` boolean to force the command to trigger a [subagent](/docs/agents/#subagents) invocation.
This useful if you want the command to not pollute your primary context and will **force** the agent to act as a subagent,
even if `mode` is set to `primary` on the [agent](/docs/agents) configuration.

opencode.json

```auto
{



"command": {



"analyze": {



"subtask": true



}



}



}
```

This is an **optional** config option.

---

<a name="model"></a>

#### [Model](#model)

Use the `model` config to override the default model for this command.

opencode.json

```auto
{



"command": {



"analyze": {



"model": "anthropic/claude-3-5-sonnet-20241022"



}



}



}
```

This is an **optional** config option.

---

### [Built-in](#built-in)

opencode includes several built-in commands like `/init`, `/undo`, `/redo`, `/share`, `/help`; [learn more](/docs/tui#commands).

Note

Custom commands can override built-in commands.

If you define a custom command with the same name, it will override the built-in command.

---

## Formatters

OpenCode uses language specific formatters.

OpenCode automatically formats files after they are written or edited using language-specific formatters. This ensures that the code that is generated follows the code styles of your project.

---

### [Built-in](#built-in)

OpenCode comes with several built-in formatters for popular languages and frameworks. Below is a list of the formatters, supported file extensions, and commands or config options it needs.

| Formatter | Extensions | Requirements |
| --- | --- | --- |
| gofmt | .go | `gofmt` command available |
| mix | .ex, .exs, .eex, .heex, .leex, .neex, .sface | `mix` command available |
| prettier | .js, .jsx, .ts, .tsx, .html, .css, .md, .json, .yaml, and [more](https://prettier.io/docs/en/index.html) | `prettier` dependency in `package.json` |
| biome | .js, .jsx, .ts, .tsx, .html, .css, .md, .json, .yaml, and [more](https://biomejs.dev/) | `biome.json(c)` config file |
| zig | .zig, .zon | `zig` command available |
| clang-format | .c, .cpp, .h, .hpp, .ino, and [more](https://clang.llvm.org/docs/ClangFormat.html) | `.clang-format` config file |
| ktlint | .kt, .kts | `ktlint` command available |
| ruff | .py, .pyi | `ruff` command available with config |
| uv | .py, .pyi | `uv` command available |
| rubocop | .rb, .rake, .gemspec, .ru | `rubocop` command available |
| standardrb | .rb, .rake, .gemspec, .ru | `standardrb` command available |
| htmlbeautifier | .erb, .html.erb | `htmlbeautifier` command available |
| air | .R | `air` command available |
| dart | .dart | `dart` command available |

So if your project has `prettier` in your `package.json`, OpenCode will automatically use it.

---

### [How it works](#how-it-works)

When OpenCode writes or edits a file, it:

1. Checks the file extension against all enabled formatters.
2. Runs the appropriate formatter command on the file.
3. Applies the formatting changes automatically.

This process happens in the background, ensuring your code styles are maintained without any manual steps.

---

### [Configure](#configure)

You can customize formatters through the `formatter` section in your OpenCode config.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"formatter": {}



}
```

Each formatter configuration supports the following:

| Property | Type | Description |
| --- | --- | --- |
| `disabled` | boolean | Set this to `true` to disable the formatter |
| `command` | string[] | The command to run for formatting |
| `environment` | object | Environment variables to set when running the formatter |
| `extensions` | string[] | File extensions this formatter should handle |

Let’s look at some examples.

---

<a name="disabling-formatters"></a>

#### [Disabling formatters](#disabling-formatters)

To disable **all** formatters globally, set `formatter` to `false`:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"formatter": false



}
```

To disable a **specific** formatter, set `disabled` to `true`:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"formatter": {



"prettier": {



"disabled": true



}



}



}
```

---

<a name="custom-formatters"></a>

#### [Custom formatters](#custom-formatters)

You can override the built-in formatters or add new ones by specifying the command, environment variables, and file extensions:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"formatter": {



"prettier": {



"command": ["npx", "prettier", "--write", "$FILE"],



"environment": {



"NODE_ENV": "development"



},



"extensions": [".js", ".ts", ".jsx", ".tsx"]



},



"custom-markdown-formatter": {



"command": ["deno", "fmt", "$FILE"],



"extensions": [".md"]



}



}



}
```

The **`$FILE` placeholder** in the command will be replaced with the path to the file being formatted.

---

## Permissions

Control which actions require approval to run.

By default, OpenCode allows most operations without approval, except `doom_loop` and `external_directory` which default to `ask`. You can configure this using the `permission` option.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"edit": "allow",



"bash": "ask",



"webfetch": "deny",



"doom_loop": "ask",



"external_directory": "ask"



}



}
```

This lets you configure granular controls for the `edit`, `bash`, `webfetch`, `doom_loop`, and `external_directory` tools.

- `"ask"` — Prompt for approval before running the tool
- `"allow"` — Allow all operations without approval
- `"deny"` — Disable the tool

---

<a name="tools-2"></a>

### [Tools](#tools)

Currently, the permissions for the `edit`, `bash`, `webfetch`, `doom_loop`, and `external_directory` tools can be configured through the `permission` option.

---

<a name="edit-1"></a>

#### [edit](#edit)

Use the `permission.edit` key to control whether file editing operations require user approval.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"edit": "ask"



}



}
```

---

#### [bash](#bash)

You can use the `permission.bash` key to control whether bash commands as a
whole need user approval.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"bash": "ask"



}



}
```

Or, you can target specific commands and set it to `allow`, `ask`, or `deny`.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"bash": {



"git push": "ask",



"git status": "allow",



"git diff": "allow",



"npm run build": "allow",



"ls": "allow",



"pwd": "allow"



}



}



}
```

---

##### [Wildcards](#wildcards)

You can also use wildcards to manage permissions for specific bash commands.

Tip

You can use wildcards to manage permissions for specific bash commands.

For example, **disable all** Terraform commands.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"bash": {



"terraform *": "deny"



}



}



}
```

You can also use the `*` wildcard to manage permissions for all commands. For
example, **deny all commands** except a couple of specific ones.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"bash": {



"*": "deny",



"pwd": "allow",



"git status": "ask"



}



}



}
```

Here a specific rule can override the `*` wildcard.

---

###### [Glob patterns](#glob-patterns)

The wildcard uses simple regex globbing patterns.

- `*` matches zero or more of any character
- `?` matches exactly one character
- All other characters match literally

---

#### [webfetch](#webfetch)

Use the `permission.webfetch` key to control whether the LLM can fetch web pages.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"webfetch": "ask"



}



}
```

---

<a name="doom_loop"></a>

#### [doom\_loop](#doom_loop)

Use the `permission.doom_loop` key to control whether approval is required when a doom loop is detected. A doom loop occurs when the same tool is called 3 times in a row with identical arguments.

This helps prevent infinite loops where the LLM repeatedly attempts the same action without making progress.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"doom_loop": "ask"



}



}
```

---

#### [external\_directory](#external_directory)

Use the `permission.external_directory` key to control whether file operations require approval when accessing files outside the working directory.

This provides an additional safety layer to prevent unintended modifications to files outside your project.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"external_directory": "ask"



}



}
```

---

<a name="agents"></a>

### [Agents](#agents)

You can also configure permissions per agent. Where the agent specific config
overrides the global config. [Learn more](/docs/agents#permissions) about agent permissions.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"permission": {



"bash": {



"git push": "ask"



}



},



"agent": {



"build": {



"permission": {



"bash": {



"git push": "allow"



}



}



}



}



}
```

For example, here the `build` agent overrides the global `bash` permission to
allow `git push` commands.

You can also configure permissions for agents in Markdown.

~/.config/opencode/agent/review.md

```auto
---



description: Code review without edits



mode: subagent



permission:



edit: deny



bash: ask



webfetch: deny



---



Only analyze code and suggest changes.
```

---

<a name="lsp-servers"></a>

## LSP Servers

OpenCode integrates with your LSP servers.

OpenCode integrates with your Language Server Protocol (LSP) to help the LLM interact with your codebase. It uses diagnostics to provide feedback to the LLM.

---

<a name="built-in"></a>

### [Built-in](#built-in)

OpenCode comes with several built-in LSP servers for popular languages:

| LSP Server | Extensions | Requirements |
| --- | --- | --- |
| typescript | .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts | `typescript` dependency in project |
| deno | .ts, .tsx, .js, .jsx, .mjs | `deno` command available (auto-detects deno.json/deno.jsonc) |
| eslint | .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue | `eslint` dependency in project |
| gopls | .go | `go` command available |
| ruby-lsp (rubocop) | .rb, .rake, .gemspec, .ru | `ruby` and `gem` commands available |
| pyright | .py, .pyi | `pyright` dependency installed |
| elixir-ls | .ex, .exs | `elixir` command available |
| zls | .zig, .zon | `zig` command available |
| csharp | .cs | `.NET SDK` installed |
| vue | .vue | Auto-installs for Vue projects |
| rust | .rs | `rust-analyzer` command available |
| clangd | .c, .cpp, .cc, .cxx, .c++, .h, .hpp, .hh, .hxx, .h++ | Auto-installs for C/C++ projects |
| svelte | .svelte | Auto-installs for Svelte projects |
| astro | .astro | Auto-installs for Astro projects |
| yaml-ls | .yaml, .yml | Auto-installs Red Hat yaml-language-server |
| jdtls | .java | `Java SDK (version 21+)` installed |
| lua-ls | .lua | Auto-installs for Lua projects |
| sourcekit-lsp | .swift, .objc, .objcpp | `swift` installed (`xcode` on macOS) |
| php intelephense | .php | Auto-installs for PHP projects |
| dart | .dart | `dart` command available |

LSP servers are automatically enabled when one of the above file extensions are detected and the requirements are met.

Note

You can disable automatic LSP server downloads by setting the `OPENCODE_DISABLE_LSP_DOWNLOAD` environment variable to `true`.

---

<a name="how-it-works-1"></a>

### [How It Works](#how-it-works)

When opencode opens a file, it:

1. Checks the file extension against all enabled LSP servers.
2. Starts the appropriate LSP server if not already running.

---

<a name="configure-3"></a>

### [Configure](#configure)

You can customize LSP servers through the `lsp` section in your opencode config.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"lsp": {}



}
```

Each LSP server supports the following:

| Property | Type | Description |
| --- | --- | --- |
| `disabled` | boolean | Set this to `true` to disable the LSP server |
| `command` | string[] | The command to start the LSP server |
| `extensions` | string[] | File extensions this LSP server should handle |
| `env` | object | Environment variables to set when starting server |
| `initialization` | object | Initialization options to send to the LSP server |

Let’s look at some examples.

---

#### [Disabling LSP servers](#disabling-lsp-servers)

To disable **all** LSP servers globally, set `lsp` to `false`:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"lsp": false



}
```

To disable a **specific** LSP server, set `disabled` to `true`:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"lsp": {



"typescript": {



"disabled": true



}



}



}
```

---

#### [Custom LSP servers](#custom-lsp-servers)

You can add custom LSP servers by specifying the command and file extensions:

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"lsp": {



"custom-lsp": {



"command": ["custom-lsp-server", "--stdio"],



"extensions": [".custom"]



}



}



}
```

---

<a name="additional-information"></a>

### [Additional Information](#additional-information)

<a name="php-intelephense"></a>

#### [PHP Intelephense](#php-intelephense)

PHP Intelephense offers premium features through a license key. You can provide a license key by placing (only) the key in a text file at:

- On macOS/Linux: `$HOME/intelephense/licence.txt`
- On Windows: `%USERPROFILE%/intelephense/licence.txt`

The file should contain only the license key with no additional content.

---

<a name="mcp-servers-2"></a>

## MCP servers

Add local and remote MCP tools.

You can add external tools to OpenCode using the *Model Context Protocol*, or MCP.

OpenCode supports both:

- Local servers
- Remote servers

Once added, MCP tools are automatically available to the LLM alongside built-in tools.

Note

OAuth support for MCP servers is coming soon.

---

<a name="caveats"></a>

### [Caveats](#caveats)

When you use an MCP server, it adds to the context. This can quickly add up if
you have a lot of tools. So we recommend being careful with which MCP servers
you use.

Tip

MCP servers add to your context, so you want to be careful with which
ones you enable.

Certain MCP servers, like the GitHub MCP server tend to add a lot of tokens and
can easily exceed the context limit.

---

<a name="configure-4"></a>

### [Configure](#configure)

You can define MCP servers in your OpenCode config under `mcp`. Add each MCP
with a unique name. You can refer to that MCP by name when prompting the LLM.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"name-of-mcp-server": {



// ...



"enabled": true,



},



"name-of-other-mcp-server": {



// ...



},



},



}
```

You can also disable a server by setting `enabled` to `false`. This is useful if you want to temporarily disable a server without removing it from your config.

---

#### [Local](#local)

Add local MCP servers using `type` to `"local"` within the MCP object.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"my-local-mcp-server": {



"type": "local",



// Or ["bun", "x", "my-mcp-command"]



"command": ["npx", "-y", "my-mcp-command"],



"enabled": true,



"environment": {



"MY_ENV_VAR": "my_env_var_value",



},



},



},



}
```

The command is how the local MCP server is started. You can also pass in a list of environment variables as well.

For example, here’s how I can add the test
[`@modelcontextprotocol/server-everything`](https://www.npmjs.com/package/@modelcontextprotocol/server-everything) MCP server.

opencode.jsonc

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"mcp_everything": {



"type": "local",



"command": ["npx", "-y", "@modelcontextprotocol/server-everything"],



},



},



}
```

And to use it I can add `use the mcp_everything tool` to my prompts.

```auto
use the mcp_everything tool to add the number 3 and 4
```

<a name="options-2"></a>

##### [Options](#options)

Here are all the options for configuring a local MCP server.

| Option | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | String | Y | Type of MCP server connection, must be `"local"`. |
| `command` | Array | Y | Command and arguments to run the MCP server. |
| `environment` | Object |  | Environment variables to set when running the server. |
| `enabled` | Boolean |  | Enable or disable the MCP server on startup. |
| `timeout` | Number |  | Timeout in ms for fetching tools from the MCP server. Defaults to 5000 (5 seconds). |

---

<a name="remote"></a>

#### [Remote](#remote)

Add remote MCP servers under by setting `type` to `"remote"`.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"my-remote-mcp": {



"type": "remote",



"url": "https://my-mcp-server.com",



"enabled": true,



"headers": {



"Authorization": "Bearer MY_API_KEY"



}



}



}



}
```

Here the `url` is the URL of the remote MCP server and with the `headers` option you can pass in a list of headers.

##### [Options](#options-1)

| Option | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | String | Y | Type of MCP server connection, must be `"remote"`. |
| `url` | String | Y | URL of the remote MCP server. |
| `enabled` | Boolean |  | Enable or disable the MCP server on startup. |
| `headers` | Object |  | Headers to send with the request. |
| `timeout` | Number |  | Timeout in ms for fetching tools from the MCP server. Defaults to 5000 (5 seconds). |

---

### [Manage](#manage)

Your MCPs are available as tools in OpenCode, alongside built-in tools. So you
can manage them through the OpenCode config like any other tool.

---

#### [Global](#global)

This means that you can enable or disable them globally.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"my-mcp-foo": {



"type": "local",



"command": ["bun", "x", "my-mcp-command-foo"]



},



"my-mcp-bar": {



"type": "local",



"command": ["bun", "x", "my-mcp-command-bar"]



}



},



"tools": {



"my-mcp-foo": false



}



}
```

We can also use a glob pattern to disable all matching MCPs.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"my-mcp-foo": {



"type": "local",



"command": ["bun", "x", "my-mcp-command-foo"]



},



"my-mcp-bar": {



"type": "local",



"command": ["bun", "x", "my-mcp-command-bar"]



}



},



"tools": {



"my-mcp*": false



}



}
```

Here we are using the glob pattern `my-mcp*` to disable all MCPs.

---

#### [Per agent](#per-agent)

If you have a large number of MCP servers you may want to only enable them per
agent and disable them globally. To do this:

1. Disable it as a tool globally.
2. In your [agent config](/docs/agents#tools) enable the MCP server as a tool.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"my-mcp": {



"type": "local",



"command": ["bun", "x", "my-mcp-command"],



"enabled": true



}



},



"tools": {



"my-mcp*": false



},



"agent": {



"my-agent": {



"tools": {



"my-mcp*": true



}



}



}



}
```

---

<a name="glob-patterns"></a>

##### [Glob patterns](#glob-patterns)

The glob pattern uses simple regex globbing patterns.

- `*` matches zero or more of any character
- `?` matches exactly one character
- All other characters match literally

---

<a name="examples-1"></a>

### [Examples](#examples)

Below are examples of some common MCP servers. You can submit a PR if you want to document other servers.

---

<a name="context7"></a>

#### [Context7](#context7)

Add the [Context7 MCP server](https://github.com/upstash/context7) to search through docs.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"context7": {



"type": "remote",



"url": "https://mcp.context7.com/mcp"



}



}



}
```

If you have signed up for a free account, you can use your API key and get higher rate-limits.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"context7": {



"type": "remote",



"url": "https://mcp.context7.com/mcp",



"headers": {



"CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"



}



}



}



}
```

Here we are assuming that you have the `CONTEXT7_API_KEY` environment variable set.

Add `use context7` to your prompts to use Context7 MCP server.

```auto
Configure a Cloudflare Worker script to cache JSON API responses for five minutes. use context7
```

Alternatively, you can add something like this to your
[AGENTS.md](/docs/rules/).

AGENTS.md

```auto
When you need to search docs, use `context7` tools.
```

---

<a name="grep-by-vercel"></a>

#### [Grep by Vercel](#grep-by-vercel)

Add the [Grep by Vercel](https://grep.app) MCP server to search through code snippets on GitHub.

opencode.json

```auto
{



"$schema": "https://opencode.ai/config.json",



"mcp": {



"gh_grep": {



"type": "remote",



"url": "https://mcp.grep.app"



}



}



}
```

Since we named our MCP server `gh_grep`, you can add `use the gh_grep tool` to your prompts to get the agent to use it.

```auto
What's the right way to set a custom domain in an SST Astro component? use the gh_grep tool
```

Alternatively, you can add something like this to your
[AGENTS.md](/docs/rules/).

AGENTS.md

```auto
If you are unsure how to do something, use `gh_grep` to search code examples from github.
```

---

## ACP Support

Use OpenCode in any ACP-compatible editor.

OpenCode supports the [Agent Client Protocol](https://agentclientprotocol.com) or (ACP), allowing you to use it directly in compatible editors and IDEs.

Tip

For a list of editors and tools that support ACP, check out the [ACP progress report](https://zed.dev/blog/acp-progress-report#available-now).

ACP is an open protocol that standardizes communication between code editors and AI coding agents.

---

### [Configure](#configure)

To use OpenCode via ACP, configure your editor to run the `opencode acp` command.

The command starts OpenCode as an ACP-compatible subprocess that communicates with your editor over JSON-RPC via stdio.

Below are examples for popular editors that support ACP.

---

#### [Zed](#zed)

Add to your [Zed](https://zed.dev) configuration (`~/.config/zed/settings.json`):

~/.config/zed/settings.json

```auto
{



"agent_servers": {



"OpenCode": {



"command": "opencode",



"args": ["acp"]



}



}



}
```

To open it, use the `agent: new thread` action in the **Command Palette**.

You can also bind a keyboard shortcut by editing your `keymap.json`:

keymap.json

```auto
[



{



"bindings": {



"cmd-alt-o": [



"agent::NewExternalAgentThread",



{



"agent": {



"custom": {



"name": "OpenCode",



"command": {



"command": "opencode",



"args": ["acp"]



}



}



}



}



]



}



}



]
```

---

#### [Avante.nvim](#avantenvim)

Add to your [Avante.nvim](https://github.com/yetone/avante.nvim) configuration:

```auto
{



acp_providers = {



["opencode"] = {



command = "opencode",



args = { "acp" }



}



}



}
```

If you need to pass environment variables:

```auto
{



acp_providers = {



["opencode"] = {



command = "opencode",



args = { "acp" },



env = {



OPENCODE_API_KEY = os.getenv("OPENCODE_API_KEY")



}



}



}



}
```

---

### [Support](#support)

OpenCode works the same via ACP as it does in the terminal. All features are supported:

Note

Some built-in slash commands like `/undo` and `/redo` are currently unsupported.

- Built-in tools (file operations, terminal commands, etc.)
- Custom tools and slash commands
- MCP servers configured in your OpenCode config
- Project-specific rules from `AGENTS.md`
- Custom formatters and linters
- Agents and permissions system

---

## Custom Tools

Create tools the LLM can call in opencode.

Custom tools are functions you create that the LLM can call during conversations. They work alongside opencode’s [built-in tools](/docs/tools) like `read`, `write`, and `bash`.

---

### [Creating a tool](#creating-a-tool)

Tools are defined as **TypeScript** or **JavaScript** files. However, the tool definition can invoke scripts written in **any language** — TypeScript or JavaScript is only used for the tool definition itself.

---

#### [Location](#location)

They can be defined:

- Locally by placing them in the `.opencode/tool/` directory of your project.
- Or globally, by placing them in `~/.config/opencode/tool/`.

---

#### [Structure](#structure)

The easiest way to create tools is using the `tool()` helper which provides type-safety and validation.

.opencode/tool/database.ts

```auto
import { tool } from "@opencode-ai/plugin"



export default tool({



description: "Query the project database",



args: {



query: tool.schema.string().describe("SQL query to execute"),



},



async execute(args) {



// Your database logic here



return `Executed query: ${args.query}`



},



})
```

The **filename** becomes the **tool name**. The above creates a `database` tool.

---

<a name="multiple-tools-per-file"></a>

##### [Multiple tools per file](#multiple-tools-per-file)

You can also export multiple tools from a single file. Each export becomes **a separate tool** with the name **`<filename>_<exportname>`**:

.opencode/tool/math.ts

```auto
import { tool } from "@opencode-ai/plugin"



export const add = tool({



description: "Add two numbers",



args: {



a: tool.schema.number().describe("First number"),



b: tool.schema.number().describe("Second number"),



},



async execute(args) {



return args.a + args.b



},



})



export const multiply = tool({



description: "Multiply two numbers",



args: {



a: tool.schema.number().describe("First number"),



b: tool.schema.number().describe("Second number"),



},



async execute(args) {



return args.a * args.b



},



})
```

This creates two tools: `math_add` and `math_multiply`.

---

#### [Arguments](#arguments)

You can use `tool.schema`, which is just [Zod](https://zod.dev), to define argument types.

```auto
args: {



query: tool.schema.string().describe("SQL query to execute")



}
```

You can also import [Zod](https://zod.dev) directly and return a plain object:

```auto
import { z } from "zod"



export default {



description: "Tool description",



args: {



param: z.string().describe("Parameter description"),



},



async execute(args, context) {



// Tool implementation



return "result"



},



}
```

---

#### [Context](#context)

Tools receive context about the current session:

.opencode/tool/project.ts

```auto
import { tool } from "@opencode-ai/plugin"



export default tool({



description: "Get project information",



args: {},



async execute(args, context) {



// Access context information



const { agent, sessionID, messageID } = context



return `Agent: ${agent}, Session: ${sessionID}, Message: ${messageID}`



},



})
```

---

<a name="examples-2"></a>

### [Examples](#examples)

<a name="write-a-tool-in-python"></a>

#### [Write a tool in Python](#write-a-tool-in-python)

You can write your tools in any language you want. Here’s an example that adds two numbers using Python.

First, create the tool as a Python script:

.opencode/tool/add.py

```auto
import sys



a = int(sys.argv[1])



b = int(sys.argv[2])



print(a + b)
```

Then create the tool definition that invokes it:

.opencode/tool/python-add.ts

```auto
import { tool } from "@opencode-ai/plugin"



export default tool({



description: "Add two numbers using Python",



args: {



a: tool.schema.number().describe("First number"),



b: tool.schema.number().describe("Second number"),



},



async execute(args) {



const result = await Bun.$`python3 .opencode/tool/add.py ${args.a} ${args.b}`.text()



return result.trim()



},



})
```

Here we are using the [`Bun.$`](https://bun.com/docs/runtime/shell) utility to run the Python script.

---

<a name="sdk"></a>

## SDK

Type-safe JS client for opencode server.

The opencode JS/TS SDK provides a type-safe client for interacting with the server.
Use it to build integrations and control opencode programmatically.

[Learn more](/docs/server) about how the server works.

---

<a name="install-2"></a>

### [Install](#install)

Install the SDK from npm:

Terminal window

```auto
npm install @opencode-ai/sdk
```

---

### [Create client](#create-client)

Create an instance of opencode:

```auto
import { createOpencode } from "@opencode-ai/sdk"



const { client } = await createOpencode()
```

This starts both a server and a client

<a name="options-3"></a>

##### [Options](#options)

| Option | Type | Description | Default |
| --- | --- | --- | --- |
| `baseUrl` | `string` | URL of the server | `http://localhost:4096` |
| `fetch` | `function` | Custom fetch implementation | `globalThis.fetch` |
| `parseAs` | `string` | Response parsing method | `auto` |
| `responseStyle` | `string` | Return style: `data` or `fields` | `fields` |
| `throwOnError` | `boolean` | Throw errors instead of return | `false` |

---

<a name="config-1"></a>

### [Config](#config)

You can pass a configuration object to customize behavior. The instance still picks up your `opencode.json`, but you can override or add configuration inline:

```auto
import { createOpencode } from "@opencode-ai/sdk"



const opencode = await createOpencode({



hostname: "127.0.0.1",



port: 4096,



config: {



model: "anthropic/claude-3-5-sonnet-20241022",



},



})



console.log(`Server running at ${opencode.server.url}`)



opencode.server.close()
```

### [Client only](#client-only)

If you already have a running instance of opencode, you can create a client instance to connect to it:

```auto
import { createOpencodeClient } from "@opencode-ai/sdk"



const client = createOpencodeClient({



baseUrl: "http://localhost:4096",



})
```

<a name="options-4"></a>

##### [Options](#options-1)

| Option | Type | Description | Default |
| --- | --- | --- | --- |
| `hostname` | `string` | Server hostname | `127.0.0.1` |
| `port` | `number` | Server port | `4096` |
| `signal` | `AbortSignal` | Abort signal for cancellation | `undefined` |
| `timeout` | `number` | Timeout in ms for server start | `5000` |
| `config` | `Config` | Configuration object | `{}` |

---

<a name="types-1"></a>

### [Types](#types)

The SDK includes TypeScript definitions for all API types. Import them directly:

```auto
import type { Session, Message, Part } from "@opencode-ai/sdk"
```

All types are generated from the server’s OpenAPI specification and available in the [types file](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts).

---

### [Errors](#errors)

The SDK can throw errors that you can catch and handle:

```auto
try {



await client.session.get({ path: { id: "invalid-id" } })



} catch (error) {



console.error("Failed to get session:", (error as Error).message)



}
```

---

<a name="apis"></a>

### [APIs](#apis)

The SDK exposes all server APIs through a type-safe client.

---

<a name="app"></a>

#### [App](#app)

| Method | Description | Response |
| --- | --- | --- |
| `app.log()` | Write a log entry | `boolean` |
| `app.agents()` | List all available agents | [`Agent[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |

---

<a name="examples-3"></a>

##### [Examples](#examples)

```auto
// Write a log entry



await client.app.log({



body: {



service: "my-app",



level: "info",



message: "Operation completed",



},



})



// List available agents



const agents = await client.app.agents()
```

---

#### [Project](#project)

| Method | Description | Response |
| --- | --- | --- |
| `project.list()` | List all projects | [`Project[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `project.current()` | Get current project | [`Project`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |

---

##### [Examples](#examples-1)

```auto
// List all projects



const projects = await client.project.list()



// Get current project



const currentProject = await client.project.current()
```

---

<a name="path"></a>

#### [Path](#path)

| Method | Description | Response |
| --- | --- | --- |
| `path.get()` | Get current path | [`Path`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |

---

<a name="examples-4"></a>

##### [Examples](#examples-2)

```auto
// Get current path information



const pathInfo = await client.path.get()
```

---

#### [Config](#config-1)

| Method | Description | Response |
| --- | --- | --- |
| `config.get()` | Get config info | [`Config`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `config.providers()` | List providers and default models | `{ providers:` [`Provider[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: { [key: string]: string } }` |

---

##### [Examples](#examples-3)

```auto
const config = await client.config.get()



const { providers, default: defaults } = await client.config.providers()
```

---

<a name="sessions-1"></a>

#### [Sessions](#sessions)

| Method | Description | Notes |
| --- | --- | --- |
| `session.list()` | List sessions | Returns [`Session[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.get({ path })` | Get session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.children({ path })` | List child sessions | Returns [`Session[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.create({ body })` | Create session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.delete({ path })` | Delete session | Returns `boolean` |
| `session.update({ path, body })` | Update session properties | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.init({ path, body })` | Analyze app and create `AGENTS.md` | Returns `boolean` |
| `session.abort({ path })` | Abort a running session | Returns `boolean` |
| `session.share({ path })` | Share session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.unshare({ path })` | Unshare session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.summarize({ path, body })` | Summarize session | Returns `boolean` |
| `session.messages({ path })` | List messages in a session | Returns `{ info:` [`Message`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts:` [`Part[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}[]` |
| `session.message({ path })` | Get message details | Returns `{ info:` [`Message`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts:` [`Part[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}` |
| `session.prompt({ path, body })` | Send prompt message | `body.noReply: true` returns UserMessage (context only). Default returns [`AssistantMessage`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) with AI response |
| `session.command({ path, body })` | Send command to session | Returns `{ info:` [`AssistantMessage`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts:` [`Part[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}` |
| `session.shell({ path, body })` | Run a shell command | Returns [`AssistantMessage`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.revert({ path, body })` | Revert a message | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `session.unrevert({ path })` | Restore reverted messages | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `postSessionByIdPermissionsByPermissionId({ path, body })` | Respond to a permission request | Returns `boolean` |

---

<a name="examples-5"></a>

##### [Examples](#examples-4)

```auto
// Create and manage sessions



const session = await client.session.create({



body: { title: "My session" },



})



const sessions = await client.session.list()



// Send a prompt message



const result = await client.session.prompt({



path: { id: session.id },



body: {



model: { providerID: "anthropic", modelID: "claude-3-5-sonnet-20241022" },



parts: [{ type: "text", text: "Hello!" }],



},



})



// Inject context without triggering AI response (useful for plugins)



await client.session.prompt({



path: { id: session.id },



body: {



noReply: true,



parts: [{ type: "text", text: "You are a helpful assistant." }],



},



})
```

---

#### [Files](#files)

| Method | Description | Response |
| --- | --- | --- |
| `find.text({ query })` | Search for text in files | Array of match objects with `path`, `lines`, `line_number`, `absolute_offset`, `submatches` |
| `find.files({ query })` | Find files by name | `string[]` (file paths) |
| `find.symbols({ query })` | Find workspace symbols | [`Symbol[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `file.read({ query })` | Read a file | `{ type: "raw" | "patch", content: string }` |
| `file.status({ query? })` | Get status for tracked files | [`File[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |

---

##### [Examples](#examples-5)

```auto
// Search and read files



const textResults = await client.find.text({



query: { pattern: "function.*opencode" },



})



const files = await client.find.files({



query: { query: "*.ts" },



})



const content = await client.file.read({



query: { path: "src/index.ts" },



})
```

---

<a name="tui-1"></a>

#### [TUI](#tui)

| Method | Description | Response |
| --- | --- | --- |
| `tui.appendPrompt({ body })` | Append text to the prompt | `boolean` |
| `tui.openHelp()` | Open the help dialog | `boolean` |
| `tui.openSessions()` | Open the session selector | `boolean` |
| `tui.openThemes()` | Open the theme selector | `boolean` |
| `tui.openModels()` | Open the model selector | `boolean` |
| `tui.submitPrompt()` | Submit the current prompt | `boolean` |
| `tui.clearPrompt()` | Clear the prompt | `boolean` |
| `tui.executeCommand({ body })` | Execute a command | `boolean` |
| `tui.showToast({ body })` | Show toast notification | `boolean` |

---

<a name="examples-6"></a>

##### [Examples](#examples-6)

```auto
// Control TUI interface



await client.tui.appendPrompt({



body: { text: "Add this to prompt" },



})



await client.tui.showToast({



body: { message: "Task completed", variant: "success" },



})
```

---

#### [Auth](#auth)

| Method | Description | Response |
| --- | --- | --- |
| `auth.set({ ... })` | Set authentication credentials | `boolean` |

---

##### [Examples](#examples-7)

```auto
await client.auth.set({



path: { id: "anthropic" },



body: { type: "api", key: "your-api-key" },



})
```

---

<a name="events"></a>

#### [Events](#events)

| Method | Description | Response |
| --- | --- | --- |
| `event.subscribe()` | Server-sent events stream | Server-sent events stream |

---

<a name="examples-7"></a>

##### [Examples](#examples-8)

```auto
// Listen to real-time events



const events = await client.event.subscribe()



for await (const event of events.stream) {



console.log("Event:", event.type, event.properties)



}
```

---

## Server

Interact with opencode server over HTTP.

The `opencode serve` command runs a headless HTTP server that exposes an OpenAPI endpoint that an opencode client can use.

---

#### [Usage](#usage)

Terminal window

```auto
opencode serve [--port <number>] [--hostname <string>]
```

<a name="options-5"></a>

##### [Options](#options)

| Flag | Short | Description | Default |
| --- | --- | --- | --- |
| `--port` | `-p` | Port to listen on | `4096` |
| `--hostname` | `-h` | Hostname to listen on | `127.0.0.1` |

---

<a name="how-it-works-2"></a>

#### [How it works](#how-it-works)

When you run `opencode` it starts a TUI and a server. Where the TUI is the
client that talks to the server. The server exposes an OpenAPI 3.1 spec
endpoint. This endpoint is also used to generate an [SDK](/docs/sdk).

Tip

Use the opencode server to interact with opencode programmatically.

This architecture lets opencode support multiple clients and allows you to interact with opencode programmatically.

You can run `opencode serve` to start a standalone server. If you have the
opencode TUI running, `opencode serve` will start a new server.

---

<a name="connect-to-an-existing-server"></a>

##### [Connect to an existing server](#connect-to-an-existing-server)

When you start the TUI it randomly assigns a port and hostname. You can instead pass in the `--hostname` and `--port` [flags](/docs/cli). Then use this to connect to its server.

The [`/tui`](#tui) endpoint can be used to drive the TUI through the server. For example, you can prefill or run a prompt. This setup is used by the OpenCode [IDE](/docs/ide) plugins.

---

<a name="spec"></a>

### [Spec](#spec)

The server publishes an OpenAPI 3.1 spec that can be viewed at:

```auto
http://<hostname>:<port>/doc
```

For example, `http://localhost:4096/doc`. Use the spec to generate clients or inspect request and response types. Or view it in a Swagger explorer.

---

### [APIs](#apis)

The opencode server exposes the following APIs.

---

#### [App](#app)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `GET` | `/app` | Get app info | [`App`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `POST` | `/app/init` | Initialize the app | `boolean` |

---

#### [Config](#config)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `GET` | `/config` | Get config info | [`Config`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `GET` | `/config/providers` | List providers and default models | `{ providers:` [Provider[]](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: { [key: string]: string } }` |

---

#### [Sessions](#sessions)

| Method | Path | Description | Notes |
| --- | --- | --- | --- |
| `GET` | `/session` | List sessions | Returns [`Session[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `GET` | `/session/:id` | Get session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `GET` | `/session/:id/children` | List child sessions | Returns [`Session[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `POST` | `/session` | Create session | body: `{ parentID?, title? }`, returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `DELETE` | `/session/:id` | Delete session |  |
| `PATCH` | `/session/:id` | Update session properties | body: `{ title? }`, returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `POST` | `/session/:id/init` | Analyze app and create `AGENTS.md` | body: `{ messageID, providerID, modelID }` |
| `POST` | `/session/:id/abort` | Abort a running session |  |
| `POST` | `/session/:id/share` | Share session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `DELETE` | `/session/:id/share` | Unshare session | Returns [`Session`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `POST` | `/session/:id/summarize` | Summarize session |  |
| `GET` | `/session/:id/message` | List messages in a session | Returns `{ info:` [Message](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts:` [Part[]](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}[]` |
| `GET` | `/session/:id/message/:messageID` | Get message details | Returns `{ info:` [Message](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts:` [Part[]](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}` |
| `POST` | `/session/:id/message` | Send chat message | body matches [`ChatInput`](https://github.com/sst/opencode/blob/main/packages/opencode/src/session/index.ts#L358). Optional `noReply: true` skips AI inference and returns UserMessage. Returns [`Message`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `POST` | `/session/:id/shell` | Run a shell command | body matches [`CommandInput`](https://github.com/sst/opencode/blob/main/packages/opencode/src/session/index.ts#L1007), returns [`Message`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `POST` | `/session/:id/revert` | Revert a message | body: `{ messageID }` |
| `POST` | `/session/:id/unrevert` | Restore reverted messages |  |
| `POST` | `/session/:id/permissions/:permissionID` | Respond to a permission request | body: `{ response }` |

---

#### [Files](#files)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `GET` | `/find?pattern=<pat>` | Search for text in files | Array of match objects with `path`, `lines`, `line_number`, `absolute_offset`, `submatches` |
| `GET` | `/find/file?query=<q>` | Find files by name | `string[]` (file paths) |
| `GET` | `/find/symbol?query=<q>` | Find workspace symbols | [`Symbol[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |
| `GET` | `/file?path=<path>` | Read a file | `{ type: "raw" | "patch", content: string }` |
| `GET` | `/file/status` | Get status for tracked files | [`File[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |

---

#### [Logging](#logging)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `POST` | `/log` | Write log entry. Body: `{ service, level, message, extra? }` | `boolean` |

---

#### [Agents](#agents)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `GET` | `/agent` | List all available agents | [`Agent[]`](https://github.com/sst/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) |

---

#### [TUI](#tui)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `POST` | `/tui/append-prompt` | Append text to the prompt | `boolean` |
| `POST` | `/tui/open-help` | Open the help dialog | `boolean` |
| `POST` | `/tui/open-sessions` | Open the session selector | `boolean` |
| `POST` | `/tui/open-themes` | Open the theme selector | `boolean` |
| `POST` | `/tui/open-models` | Open the model selector | `boolean` |
| `POST` | `/tui/submit-prompt` | Submit the current prompt | `boolean` |
| `POST` | `/tui/clear-prompt` | Clear the prompt | `boolean` |
| `POST` | `/tui/execute-command` | Execute a command (`{ command }`) | `boolean` |
| `POST` | `/tui/show-toast` | Show toast (`{ title?, message, variant }`) | `boolean` |
| `GET` | `/tui/control/next` | Wait for the next control request | Control request object |
| `POST` | `/tui/control/response` | Respond to a control request (`{ body }`) | `boolean` |

---

#### [Auth](#auth)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `PUT` | `/auth/:id` | Set authentication credentials. Body must match provider schema | `boolean` |

---

#### [Events](#events)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `GET` | `/event` | Server-sent events stream. First event is `server.connected`, then bus events | Server-sent events stream |

---

#### [Docs](#docs)

| Method | Path | Description | Response |
| --- | --- | --- | --- |
| `GET` | `/doc` | OpenAPI 3.1 specification | HTML page with OpenAPI spec |

---

## Plugins

Write your own plugins to extend OpenCode.

Plugins allow you to extend OpenCode by hooking into various events and customizing behavior. You can create plugins to add new features, integrate with external services, or modify OpenCode’s default behavior.

---

### [Create a plugin](#create-a-plugin)

A plugin is a **JavaScript/TypeScript module** that exports one or more plugin
functions. Each function receives a context object and returns a hooks object.

---

#### [Location](#location)

Plugins are loaded from:

1. `.opencode/plugin` directory either in your project
2. Or, globally in `~/.config/opencode/plugin`

---

#### [Basic structure](#basic-structure)

.opencode/plugin/example.js

```auto
export const MyPlugin = async ({ project, client, $, directory, worktree }) => {



console.log("Plugin initialized!")



return {



// Hook implementations go here



}



}
```

The plugin function receives:

- `project`: The current project information.
- `directory`: The current working directory.
- `worktree`: The git worktree path.
- `client`: An opencode SDK client for interacting with the AI.
- `$`: Bun’s [shell API](https://bun.com/docs/runtime/shell) for executing commands.

---

<a name="typescript-support"></a>

#### [TypeScript support](#typescript-support)

For TypeScript plugins, you can import types from the plugin package:

my-plugin.ts

```auto
import type { Plugin } from "@opencode-ai/plugin"



export const MyPlugin: Plugin = async ({ project, client, $, directory, worktree }) => {



return {



// Type-safe hook implementations



}



}
```

---

#### [Events](#events)

Plugins can subscribe to events as seen below in the Examples section. Here is a list of the different events available.

##### [Command Events](#command-events)

- `command.executed`

##### [File Events](#file-events)

- `file.edited`
- `file.watcher.updated`

##### [Installation Events](#installation-events)

- `installation.updated`

##### [LSP Events](#lsp-events)

- `lsp.client.diagnostics`
- `lsp.updated`

##### [Message Events](#message-events)

- `message.part.removed`
- `message.part.updated`
- `message.removed`
- `message.updated`

##### [Permission Events](#permission-events)

- `permission.replied`
- `permission.updated`

##### [Server Events](#server-events)

- `server.connected`

##### [Session Events](#session-events)

- `session.created`
- `session.compacted`
- `session.deleted`
- `session.diff`
- `session.error`
- `session.idle`
- `session.status`
- `session.updated`

##### [Todo Events](#todo-events)

- `todo.updated`

##### [Tool Events](#tool-events)

- `tool.execute.after`
- `tool.execute.before`

##### [TUI Events](#tui-events)

- `tui.prompt.append`
- `tui.command.execute`
- `tui.toast.show`

---

### [Examples](#examples)

Here are some examples of plugins you can use to extend opencode.

---

#### [Send notifications](#send-notifications)

Send notifications when certain events occur:

.opencode/plugin/notification.js

```auto
export const NotificationPlugin = async ({ project, client, $, directory, worktree }) => {



return {



event: async ({ event }) => {



// Send notification on session completion



if (event.type === "session.idle") {



await $`osascript -e 'display notification "Session completed!" with title "opencode"'`



}



},



}



}
```

We are using `osascript` to run AppleScript on macOS. Here we are using it to send notifications.

---

<a name="env-protection"></a>

#### [.env protection](#env-protection)

Prevent opencode from reading `.env` files:

.opencode/plugin/env-protection.js

```auto
export const EnvProtection = async ({ project, client, $, directory, worktree }) => {



return {



"tool.execute.before": async (input, output) => {



if (input.tool === "read" && output.args.filePath.includes(".env")) {



throw new Error("Do not read .env files")



}



},



}



}
```

---

#### [Custom tools](#custom-tools)

Plugins can also add custom tools to opencode:

.opencode/plugin/custom-tools.ts

```auto
import { type Plugin, tool } from "@opencode-ai/plugin"



export const CustomToolsPlugin: Plugin = async (ctx) => {



return {



tool: {



mytool: tool({



description: "This is a custom tool",



args: {



foo: tool.schema.string(),



},



async execute(args, ctx) {



return `Hello ${args.foo}!`



},



}),



},



}



}
```

The `tool` helper creates a custom tool that opencode can call. It takes a Zod schema function and returns a tool definition with:

- `description`: What the tool does
- `args`: Zod schema for the tool’s arguments
- `execute`: Function that runs when the tool is called

Your custom tools will be available to opencode alongside built-in tools.

---

You need to enable JavaScript to run this app.
