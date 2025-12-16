# Google Antigravity Documentation

## Table of Contents

- [Google Antigravity](#google-antigravity)
  - [Core Surfaces](#core-surfaces)
  - [Key Terms](#key-terms)
- [Getting Started](#getting-started)
  - [Download](#download)
  - [Basic Navigation](#basic-navigation)
- [Agent](#agent)
  - [Core Components](#core-components)
  - [Customizations](#customizations)
- [Models](#models)
  - [Reasoning Model](#reasoning-model)
  - [Additional Models](#additional-models)
- [Agent Modes / Settings](#agent-modes-settings)
  - [Conversation-Level](#conversation-level)
  - [Overall Settings](#overall-settings)
- [Rules](#rules)
  - [Global Rules](#global-rules)
  - [Workspace Rules](#workspace-rules)
  - [@ Mentions](#mentions)
- [Workflows](#workflows)
  - [Agent-Generated Workflows](#agent-generated-workflows)
- [Task Groups](#task-groups)
- [Browser Subagent](#browser-subagent)
- [Secure Mode](#secure-mode)
  - [Features](#features)
- [Antigravity Editor: MCP Integration](#antigravity-editor-mcp-integration)
  - [What is MCP?](#what-is-mcp)
  - [Core Features](#core-features)
  - [How to Connect](#how-to-connect)
  - [Connecting Custom MCP Servers](#connecting-custom-mcp-servers)
  - [Supported Servers](#supported-servers)
- [Artifacts](#artifacts)
- [Task List](#task-list)
- [Implementation Plan](#implementation-plan)
- [Walkthrough](#walkthrough)
- [Screenshots](#screenshots)
- [Browser Recordings](#browser-recordings)
- [Knowledge](#knowledge)
  - [What is a Knowledge Item?](#what-is-a-knowledge-item)
  - [How are Knowledge Items Generated?](#how-are-knowledge-items-generated)
  - [Viewing Knowledge Items](#viewing-knowledge-items)
  - [How are Knowledge Items used by the Agent?](#how-are-knowledge-items-used-by-the-agent)
- [Editor](#editor)
- [Antigravity Editor: Tab & Navigation](#antigravity-editor-tab-navigation)
  - [Supercomplete](#supercomplete)
  - [Tab-to-Jump](#tab-to-jump)
  - [Tab-to-Import](#tab-to-import)
  - [Settings](#settings)
- [Antigravity Editor: Command](#antigravity-editor-command)
  - [How it Works](#how-it-works-3)
  - [Where to Use It](#where-to-use-it)
- [Agent Side Panel](#agent-side-panel)
- [Review Changes + Source Control](#review-changes-source-control)
- [Agent Manager](#agent-manager)
- [Workspaces](#workspaces)
- [Playground](#playground)
  - [Creating a Playground](#creating-a-playground)
  - [Persisting Your Work](#persisting-your-work)
- [Inbox](#inbox)
- [Conversation View](#conversation-view)
- [Browser Subagent View](#browser-subagent-view)
  - [Overview](#overview)
  - [What’s in the side panel](#whats-in-the-side-panel)
  - [Visual Inspection Feature](#visual-inspection-feature)
- [Panes](#panes)
- [Review Changes + Source Control](#review-changes-source-control-1)
- [Changes Sidebar](#changes-sidebar)
- [Terminal](#terminal)
- [Files](#files)
- [Browser](#browser)
- [Chrome Extension](#chrome-extension)
  - [Troubleshooting](#troubleshooting)
- [Allowlist / Denylist](#allowlist-denylist)
  - [How It Works](#how-it-works-4)
- [Separate Chrome Profile](#separate-chrome-profile)
- [Plans](#plans)
- [Settings](#settings-1)
  - [Data Collection Settings](#data-collection-settings)
- [FAQ](#faq)
  - [Why can I not authenticate into Google Antigravity?](#why-can-i-not-authenticate-into-google-antigravity)
  - [Why is my age unverified?](#why-is-my-age-unverified)
  - [What is Google Antigravity’s geographical availability?](#what-is-google-antigravitys-geographical-availability)
  - [Why am I ineligible for Google One AI quotas, even though I am a subscribed to a plan?](#why-am-i-ineligible-for-google-one-ai-quotas-even-though-i-am-a-subscribed-to-a-plan)
  - [What is Google Antigravity’s stance on data collection?](#what-is-google-antigravitys-stance-on-data-collection)
  - [How do I get support?](#how-do-i-get-support)
  - [What are the model rate limits?](#what-are-the-model-rate-limits)
  - [Does Google Antigravity currently support worktrees?](#does-google-antigravity-currently-support-worktrees)
  - [What happens when my computer goes to sleep?](#what-happens-when-my-computer-goes-to-sleep)

- side\_navigation
- Home

<a name="google-antigravity"></a>
## Google Antigravity

Google Antigravity is an agentic development platform, evolving the IDE into the agent-first era. Antigravity enables developers to operate at a higher, task-oriented level managing agents across workspaces, while retaining a familiar AI IDE experience at its core. Antigravity extracts agents into their own surface and provides them the tools needed to autonomously operate across the editor, terminal, and browser emphasizing verification and higher-level communication via tasks and artifacts. This capability enables agents to plan and execute more complex, end-to-end software tasks, elevating all aspects of development, from building features, UI iteration, and fixing bugs to research and generating reports.

Main Features

automatic\_cluster

AI-powered IDE keyboard\_arrow\_right

An AI-powered IDE with all of the AI features that developers have come to rely on such as Agent, Tab, and Command.automatic\_cluster

Asynchronous Agents keyboard\_arrow\_right

Asynchronous, local agents that can work in parallel on all of your workspaces.automatic\_cluster

Agent Manager keyboard\_arrow\_right

New Agent Manager view for an agent-first experience built around planning mode, the conversation UI, and artifact review.automatic\_cluster

Multi-window keyboard\_arrow\_right

A multi-window product with an Editor, Manager, and Browser.automatic\_cluster

Browser Agent keyboard\_arrow\_right

Agent that can actuate the browser for you and to accomplish dev tasks like dashboard reads, SCM actions, UI testing, etc. in the Browser.

<a name="core-surfaces"></a>
### Core Surfaces

automatic\_cluster

Editor keyboard\_arrow\_right

A fully-functional AI-powered IDE that maps to a single workspace.automatic\_cluster

Browser keyboard\_arrow\_right

(In preview) Browser-use agent capabilities to read & actuate on more surfaces beyond just the IDE.automatic\_cluster

Agent Manager keyboard\_arrow\_right

(In preview) An orchestration “no code” view to start and view tasks in a minimalist product focused on the conversation and artifacts.

<a name="key-terms"></a>
### Key Terms

- **Agent**: The primary AI modality within Antigravity. While the user can work tightly with an Agent within the Editor, they can also have multiple agents working across multiple codebases, orchestrated and monitored through the Agent Manager.
- **Tab & Command**: The other AI modalities within Antigravity, specifically within the text editor part of the editor surface. Tab is a more powerful “autocomplete” and Command is an inline instructive modality. From past experience, these do not get nearly as much use as the Agent.
- **Artifacts**: We define an artifact as anything that the agent creates to allow it to get its work done or communicate its accomplishments to the human user. These include rich markdown files, diff views, architecture diagrams, images, browser recordings, etc.

---

- side\_navigation
- [Home](/docs/home)
>- Getting Started

<a name="getting-started"></a>
## Getting Started

<a name="download"></a>
### Download

Please visit [antigravity.google/download](https://antigravity.google/download) to download Google Antigravity.

- **macOS**: macOS versions with Apple security update support. This is typically the current and two previous versions. Min Version 12 (Monterey), X86 is not supported
- **Windows**: Windows 10 (64 bit)
- **Linux**: glibc >= 2.28, glibcxx >= 3.4.25 (e.g. Ubuntu 20. Debian 10, Fedora 36, RHEL 8)

The application will prompt when updates are available:

![Update Available](assets/image/docs/restart-to-update.png)

<a name="basic-navigation"></a>
### Basic Navigation

The Agent Manager can be opened from the Editor via the button on the top bar or via keyboard shortcut `Cmd + E`:

![Editor Open Agent Manager](assets/image/docs/editor-open-agent-manager.png)

Similarly, from the Agent Manager, the Editor can be opened from any workspace via the “Focus Editor” option in the workspace’s drop down. When focused on a workspace, the Editor can be opened from any of the “Open Editor” buttons, or via the keyboard shortcut `Cmd + E`.

![Agent Manager Open Editor](assets/image/docs/agent-manager-open-editor.png)

---

- side\_navigation
- Agent

<a name="agent"></a>
## Agent

The Agent is the main AI functionality within Google Antigravity. It is a multi-step reasoning system powered by a frontier LLM that can reason over your existing code, use a wide range of tools (including the browser), and communicate with the user through tasks, artifacts, and more.

<a name="core-components"></a>
### Core Components

- Reasoning model
- Tools
- Artifacts
- Knowledge

<a name="customizations"></a>
### Customizations

- Agent Modes / Settings
- MCP
- Rules / Workflows

You can spin up multiple Agent conversations, including in parallel. Deleting an Agent conversation via “Right Click > Delete Conversation” in the Agent Manager or by clicking the trash icon in the Editor’s Agent panel.

---

- side\_navigation
- [Agent](/docs/agent)
>- Models

<a name="models"></a>
## Models

<a name="reasoning-model"></a>
### Reasoning Model

For the core reasoning model, Antigravity offers leading frontier models from the Google Vertex Model Garden:

- Gemini 3 Pro (high)
- Gemini 3 Pro (low)
- Claude Sonnet 4.5
- Claude Sonnet 4.5 (thinking)
- Claude Opus 4.5 (thinking)
- GPT-OSS

Users can select which reasoning model they want to use within the model selector drop down under the conversation prompt box:

![Model Selector Drop Down](/assets/image/docs/model-selector.png)

The choice of reasoning model is sticky between user messages within a conversation, so if you change the reasoning model while the Agent is running, it will continue to use the previously selected reasoning model until it has completed its steps for that user turn (or until the user cancels the current execution).

Learn more about reasoning model rate limits in [our plans page](/docs/plans).

<a name="additional-models"></a>
### Additional Models

Antigravity uses a number of other models for various parts of the stack that are not customizable:

- **Nano Banana Pro**: Used by the generative image tool when the Agent wants to produce a UI mockup, needs images to populate a web page or application, generate system or architecture diagrams, or other generative image tasks.
- **Gemini 2.5 Pro UI Checkpoint**: Used by the [browser subagent](/docs/browser-subagent) to actuate the browser, such as clicking, scrolling, or filling in input.
- **Gemini 2.5 Flash**: Used in the background for checkpointing and context summarization.
- **Gemini 2.5 Flash Lite**: Used by the codebase semantic search tool.

---

- side\_navigation
- [Agent](/docs/agent)
>- Agent Modes / Settings

<a name="agent-modes-settings"></a>
## Agent Modes / Settings

<a name="conversation-level"></a>
### Conversation-Level

When starting a new Agent conversation, users can choose between multiple modes:

- Planning: Agent can plan before executing tasks. Use for deep research, complex tasks, or collaborative work. In this mode, the Agent organizes its work in [task groups](/docs/task-groups), produces [Artifacts](/docs/artifacts), and takes other steps to thoroughly research, think through, and plan its work for optimal quality.
- Fast: Agent will execute tasks directly. Use for simple tasks that can be completed faster, such as renaming variables, kicking off a few bash commands, or other smaller, localized tasks. This is helpful for when speed is an important factor, and the task is simple enough that there is low worry of worse quality.

<a name="overall-settings"></a>
### Overall Settings

Settings across every Agent conversation can be found in the “Agent” tab of the Settings pane. Some of the major ones include:

<a name="artifact-review-policy"></a>
#### Artifact Review Policy

These are the possible options for Artifact Review Policy:

- Always Proceed: Agent never asks for review
- Request Review: Agent always asks for review

When Agent decides to request review from the user for implementation plans, this policy determines what the agent does. When set to “Request Review”, the agent will always terminate after notifying, allowing the user to spend time reviewing the plan and adding comments to augment proposed changes.

![Settings Review Policy Proceed](assets/image/docs/agent/settings-review-policy-proceed.png)

If you do not need to manually review Agent’s plan before making changes, set this to “Always Proceed”, in which case every time the agent decides to request review from the user, it will then immediately continue with executing the plan.

![Settings Review Policy Manual](assets/image/docs/agent/settings-review-policy-manual.png)

<a name="terminal-command-auto-execution"></a>
#### Terminal Command Auto Execution

For the terminal command generation tool:

- Request Review: Never auto-execute terminal commands (except those in a configurable Allow list)
- Always Proceed: Agent never asks for review (except those in a configurable Deny list)

The allow list and deny list are configurable in the settings in the “Agent” tab. Configure these to add more advanced permissioning to your terminal auto execution policy.

Note: a change to this setting will only apply to new messages sent to Agent. In-progress responses will use the previous setting value.

For Unix shells, an allow or deny list entry matches a command if its space-separated tokens form a prefix of the command's tokens. For PowerShell, the entry tokens may match any contiguous subsequence of the command tokens.

<a name="agent-non-workspace-file-access"></a>
#### Agent Non-Workspace File Access

Allow Agent to view and edit files outside of the current workspace. By default, the Agent only has access to the files in the workspace and in the application’s root folder `~/.antigravity/`, which contains [Artifacts](docs/artifacts), [Knowledge Items](docs/knowledge), and other Antigravity-specific data.

Use with caution, as this could expose local secret or sensitive data to the Agent.

---

- side\_navigation
- [Agent](/docs/agent)
>- Rules / Workflows

<a name="rules"></a>
## Rules

Rules are manually defined constraints for the Agent to follow, at both the local and global levels. Rules allow users to guide the agent to follow behaviors particular to their own use cases and style.

To get started with Rules:

1. Open the Customizations panel via the "..." dropdown at the top of the editor's agent panel.
2. Navigate to the Rules panel.
3. Click **+ Global** to create new Global Rules, or **+ Workspace** to create new Workspace-specific rules.

A Rule itself is simply a Markdown file, where you can input the constraints to guide the Agent to your tasks, stack, and style.

Rules files are limited to 12,000 characters each.

<a name="global-rules"></a>
### Global Rules

Global rules live in ~/.gemini/GEMINI.md and are applied across all workspaces.

<a name="workspace-rules"></a>
### Workspace Rules

Workspace rules live in the .agent/rules folder of your workspace or git root.

At the rule level you can define how a rule should be activated:

- Manual: The rule is manually activated via at mention in Agent’s input box.
- Always On: The rule is always applied.
- Model Decision: Based on a natural language description of the rule, the model decides whether to apply the rule.
- Glob: Based on the glob pattern you define (e.g., *.js, src/\*\*/*.ts), the rule will be applied to all files that match the pattern.

<a name="mentions"></a>
### @ Mentions

You can reference other files using @filename in a Rules file. If filename is a relative path, it will be interpreted relative to the location of the Rules file. If filename is an absolute path, it will be resolved as a true absolute path, otherwise it will be resolved relative to the repository. For example, @/path/to/file.md will first attempt to be resolved to /path/to/file.md, and if that file does not exist, it will be resolved to workspace/path/to/file.md.

<a name="workflows"></a>
## Workflows

Workflows enable you to define a series of steps to guide the Agent through a repetitive set of tasks, such as deploying a service or responding to PR comments. These Workflows are saved as markdown files, allowing you to have an easy repeatable way to run key processes. Once saved, Workflows can be invoked in Agent via a slash command with the format /workflow-name.

While Rules provide models with guidance by providing persistent, reusable context at the prompt level, Workflows provide a structured sequence of steps or prompts at the trajectory level, guiding the model through a series of interconnected tasks or actions.

To create a workflow:

1. Open the Customizations panel via the "..." dropdown at the top of the editor's agent panel.
2. Navigate to the Workflows panel.
3. Click the **+ Global** button to create a new global workflow that can be accessed across all your workspaces, or click the **+ Workspace** button to create a workflow specific to your current workspace.

To execute a workflow, simply invoke it in Agent using the /workflow-name command. You can call other Workflows from within a workflow! For example, /workflow-1 can include instructions like “Call /workflow-2” and “Call /workflow-3”. Upon invocation, Agent sequentially processes each step defined in the workflow, performing actions or generating responses as specified.

Workflows are saved as markdown files and contain a title, a description and a series of steps with specific instructions for Agent to follow. Workflow files are limited to 12,000 characters each.

<a name="agent-generated-workflows"></a>
### Agent-Generated Workflows

You can also ask Agent to generate Workflows for you! This works particularly well after manually working with Agent through a series of steps since it can use the conversation history to create the Workflow.

---

- side\_navigation
- [Agent](/docs/agent)
>- Task Groups

<a name="task-groups"></a>
## Task Groups

When Agent is in planning mode, large and complex tasks are handled with Task Groups, which break down these problems into smaller, more approachable units of work. Oftentimes, Agent will work on multiple parts of the greater task at the same time, and task sections are how these changes are presented to the user. Here is an example task group.

![Task Group](assets/image/docs/agent/task-group.png)

The top component of the task group specifies the overarching goal of this task as well as summarizes the changes made within this unit of work. There is also a section of edited files for quick user audit of changes: click on the file pill and you will view the current state of the changed files.

![Task Group Clicked Pill](assets/image/docs/agent/task-group-clicked-pill.png)

Within a task group, Agent identifies subtasks that help modularize necessary changes, and all work done by the Agent is viewable within these progress update sections. By default, the details in each subtask are not directly exposed to the user, but if you are interested, there is a toggle that will expand on the exact steps that Agent made.

![Task Group Expanded](assets/image/docs/agent/task-group-expanded.png)

Sometimes, there are pending steps, such as browser setup or terminal commands requiring approval, that are created inside these progress updates. In this case, instead of expanding all of the updates, Agent provides a special section at the end of the task group where you can review these pending steps accordingly.

![Task Group Pending](assets/image/docs/agent/task-group-pending.png)

---

- side\_navigation
- [Agent](/docs/agent)
>- Browser Subagent

<a name="browser-subagent"></a>
## Browser Subagent

When the agent wants to interact with the browser, it invokes a browser subagent to handle the task at hand. The browser subagent runs a model specialized to operate on the pages that are open within the Antigravity-managed browser, which is different from the model you selected for the main agent.

This subagent has access to a variety of tools that are necessary to control your browser, including clicking, scrolling, typing, reading console logs, and more. It can also read your open pages through DOM capture, screenshots, or markdown parsing, as well as taking videos.

While the agent is controlling a page, it will show an overlay on the page with a blue border and a small panel with short descriptions of the actions being taken. When this is shown, you will not be allowed to interact with the page to ensure it doesn’t get confused by your actions.

The browser subagent can act on tabs that are not focused, so you are free to open other tabs and use them uninterrupted as it works.

---

- side\_navigation
- [Agent](/docs/agent)
>- Secure Mode

<a name="secure-mode"></a>
## Secure Mode

Secure Mode provides enhanced security controls for the Agent, allowing you to restrict its access to external resources and sensitive operations. When Secure Mode is enabled, several security measures are enforced to protect your environment.

<a name="features"></a>
### Features

<a name="browser-url-allowlistdenylist"></a>
#### Browser URL Allowlist/Denylist

In Secure Mode, the Agent's ability to interact with external websites is governed by the browser's Allowlist and Denylist. This applies to:

- **External Markdown Images**: The Agent will only render images from URLs that are allowed.
- **Read URL Tool**: The Read URL tool will only auto-execute for allowed URLs.

<a name="terminal-browser-and-artifact-review-policies"></a>
#### Terminal, Browser, and Artifact Review Policies

Secure Mode enforces the following behavior for terminal, browser, and artifact interactions:

- **Terminal Auto Execution**: Set to "Request Review". The Agent will always prompt for permission before executing any terminal command. The terminal allowlist is ignored when Secure Mode is enabled.
- **Browser Javascript Execution**: Set to "Request Review". The Agent will always prompt for permission before executing Javascript in the browser.
- **Artifact Review**: Set to "Request Review". The Agent will always prompt for confirmation before acting on plans laid out in artifacts.

<a name="file-system-access"></a>
#### File System Access

Secure Mode restricts the Agent's access to the file system to ensure it only interacts with authorized files:

- **Respect .gitignore**: The Agent will respect `.gitignore` rules, preventing it from accessing ignored files.
- **Workspace Isolation**: Access to files outside the workspace is disabled. The Agent can only view and edit files within the designated workspace.

---

- side\_navigation
- Tools
>- MCP

<a name="antigravity-editor-mcp-integration"></a>
## Antigravity Editor: MCP Integration

Antigravity supports the Model Context Protocol (MCP), a standard that allows the editor to securely connect to your local tools, databases, and external services. This integration provides the AI with real-time context beyond just the files open in your editor.

<a name="what-is-mcp"></a>
### What is MCP?

MCP acts as a bridge between Antigravity and your broader development environment. Instead of manually pasting context (like database schemas or logs) into the editor, MCP allows Antigravity to fetch this information directly when needed.

<a name="core-features"></a>
### Core Features

<a name="1-context-resources"></a>
#### 1. Context Resources

The AI can read data from connected MCP servers to inform its suggestions.

**Example:** When writing a SQL query, Antigravity can inspect your live Neon or Supabase schema to suggest correct table and column names.

**Example:** When debugging, the editor can pull in recent build logs from Netlify or Heroku.

<a name="2-custom-tools"></a>
#### 2. Custom Tools

MCP enables Antigravity to execute specific, safe actions defined by your connected servers.

**Example:** "Create a Linear issue for this TODO."

**Example:** "Search Notion or GitHub for authentication patterns."

<a name="how-to-connect"></a>
### How to Connect

Connections are managed directly through the built-in MCP Store.

1. **Access the Store:** Open the MCP Store panel within the "..." dropdown at the top of the editor's side panel.
2. **Browse & Install:** Select any of the supported servers from the list and click Install.
3. **Authenticate:** Follow the on-screen prompts to securely link your accounts (where applicable).

Once installed, resources and tools from the server are automatically available to the editor.

<a name="connecting-custom-mcp-servers"></a>
### Connecting Custom MCP Servers

To connect to a custom MCP server:

1. Open the MCP store via the "..." dropdown at the top of the editor's agent panel.
2. Click on "Manage MCP Servers"
3. Click on "View raw config"
4. Modify the mcp\_config.json with your custom MCP server configuration.

<a name="supported-servers"></a>
### Supported Servers

The MCP Store currently features integrations for:

- Airweave
- AlloyDB for PostgreSQL
- Atlassian
- BigQuery
- Cloud SQL for PostgreSQL
- Cloud SQL for MySQL
- Cloud SQL for SQL Server
- Dart
- Dataplex
- Figma Dev Mode MCP
- Firebase
- GitHub
- Harness
- Heroku
- Linear
- Locofy
- Looker
- MCP Toolbox for Databases
- MongoDB
- Neon
- Netlify
- Notion
- PayPal
- Perplexity Ask
- Pinecone
- Prisma
- Redis
- Sequential Thinking
- SonarQube
- Spanner
- Stripe
- Supabase

---

- side\_navigation
- Artifacts

<a name="artifacts"></a>
## Artifacts

We define an Artifact as anything that the agent creates to allow it to get its work done or communicate its work and thinking to the human user. These include rich markdown files, diff views, architecture diagrams, images, browser recordings, code diffs, etc. As Agents become more autonomous and can run for longer and longer periods, Artifacts allow for the Agent to asynchronously communicate its work to the user, as opposed to requiring the user to carefully monitor every Agent step synchronously.

Artifacts are produced while the Agent is in [Planning mode](/docs/agent-modes-settings), and appear in both the [Agent Manager](/docs/agent-manager) and [Editor](/docs/editor) views, though the former is optimized for displaying, organizing, and managing Artifacts.

Feedback is another key concept with Artifacts. Depending on the user settings, the Agent may ask for review on intermediate Artifacts to receive confirmation that it has made progress in its thinking or implementation that aligns with the user’s intent and goal. The user is able to provide feedback on the Artifact to provide guidance to steer the Agent in the proper direction. The UI/UX of feedback differs from Artifact type to Artifact type.

---

- side\_navigation
- [Artifacts](/docs/artifacts)
>- Task List

<a name="task-list"></a>
## Task List

A task list is an artifact that the agent uses to approach complex tasks and monitor progress on various action items. You can find a live snapshot of what the agent is doing in this artifact, which is constructed as a markdown list of items related to research, implementation, verification, and more. This type of artifact is generally used by the agent to keep on track with the user’s overarching goal; typically, you do not need to directly interact with this artifact.

![Task List](assets/image/docs/artifacts/artifact-task.png)

---

- side\_navigation
- [Artifacts](/docs/artifacts)
>- Implementation Plan

<a name="implementation-plan"></a>
## Implementation Plan

Agent utilizes the implementation plan artifact to architect changes within your codebase to accomplish a task. These plans contain technical details on what revisions are necessary and are meant to be reviewed by the user. Below is an example plan generated by the agent.

![Artifact Implementation Plan](assets/image/docs/artifacts/artifact-implementation-plan.png)

Unless you have you artifact review policy set to “Always Proceed” [link to docs on this setting], Agent will typically request your review on the implementation plan before making the changes needed to complete your task. You can click either the in-conversation or artifact header “Proceed” button to instantly continue with Agent’s plan.

![Artifact Implementation Plan Proceed](assets/image/docs/artifacts/artifact-implementation-plan-proceed.png)

Oftentimes, Agent will create a plan that is slightly different from what you exactly want. Antigravity supports commenting on these artifacts so you can provide feedback to Agent for any reason, whether it be to decrease scope of changes, use a different tech stack, or correct any Agent discrepancies.

![Artifact Implementation Plan Comments](assets/image/docs/artifacts/artifact-implementation-plan-comments.png)

Once you have left comments on the implementation plan, you can still use the “Proceed” to continue with Agent’s plan; alternatively, you can also toggle the “Review” button in the artifact header, where you can examine all comments and leave a message as feedback instead of directly proceeding, if needed.

![Artifact Implementation Plan Submit Comments](assets/image/docs/artifacts/artifact-implementation-plan-submit-comments.png)

Once you have proceeded or left a review, Agent will continue its work, either iterating on the implementation plan and re-requesting your review or beginning with its work!

![Artifact Implementation Plan Proceeded](assets/image/docs/artifacts/artifact-implementation-plan-proceeded.png)

---

- side\_navigation
- [Artifacts](/docs/artifacts)
>- Walkthrough

<a name="walkthrough"></a>
## Walkthrough

Agent creates walkthrough artifacts when it has completed task implementation; this type of artifact includes a concise summary of the changes that have been made to remind the user of what has happened in the active conversation. This is a great way to get up to speed with the state of your codebase after Agent has made its changes in case you were not strictly following it the whole time.

![Walkthrough](assets/image/docs/artifacts/artifact-walkthrough.png)

For browser tasks, walkthroughs often contain screenshots and screen recordings of what Agent has built or created in the browser!

![Walkthrough with Image](assets/image/docs/artifacts/artifact-walkthrough-image.png)

---

- side\_navigation
- [Artifacts](/docs/artifacts)
>- Screenshots

<a name="screenshots"></a>
## Screenshots

The browser subagent can take screenshots of open pages or elements on pages when it would like your review of the state of the page. This is surfaced as a tool to the agent, and you can also prompt the agent to take a screenshot of a page.

![Browser Screenshot Capture Tool](assets/image/docs/artifacts/browser-screenshot-capture.png)

All screenshots are saved as image artifacts and can be commented on to give feedback to the agent.

![Browser Screenshot Artifact](assets/image/docs/artifacts/browser-screenshot-artifact.png)

---

- side\_navigation
- [Artifacts](/docs/artifacts)
>- Browser Recordings

<a name="browser-recordings"></a>
## Browser Recordings

Every time the browser subagent actuates on the Browser, it may choose to generate a recording of the agent’s actions for your review. You can view this playback, if it is available, at the bottom of the Browser step UI.

![Browser Recording Capture Tool](assets/image/docs/artifacts/browser-recording-capture.png)

All browser recordings are also saved as a recording artifact for your review. This view loops through the browser agent’s actions.

![Browser Recording Artifact](assets/image/docs/artifacts/browser-recording-artifact.png)

---

- side\_navigation
- [Artifacts](/docs/artifacts)
>- Knowledge

<a name="knowledge"></a>
## Knowledge

Knowledge Items are Antigravity's persistent memory system that automatically captures and organizes important insights, patterns, and solutions from your coding sessions. They help you build upon previous work across conversations.

<a name="what-is-a-knowledge-item"></a>
### What is a Knowledge Item?

A Knowledge Item is a collection of related information on a specific topic. Each Knowledge Item contains a title and summary describing what it covers, and a collection of artifacts providing information on the topic. Possible examples of artifacts include automatically generated documentation, code examples, or persistent memories of user instructions.

<a name="how-are-knowledge-items-generated"></a>
### How are Knowledge Items Generated?

As you interact with the agent, Antigravity automatically analyzes and extracts information from your conversation and uses that information to create new KIs or update existing KIs.

<a name="viewing-knowledge-items"></a>
### Viewing Knowledge Items

You can view your Knowledge Items in the Antigravity **Agent Manager**.

![Knowledge View](assets/image/docs/artifacts/knowledge-view.png)

<a name="how-are-knowledge-items-used-by-the-agent"></a>
### How are Knowledge Items used by the Agent?

The summaries of all your Knowledge Items are available to the agent, which uses them to inform its responses. When the agent identifies a Knowledge Item that is relevant to the conversation, it will automatically study the artifacts in that Knowledge Item and use the applicable information.

---

- side\_navigation
- Editor

<a name="editor"></a>
## Editor

The primary entry point to Antigravity is our Editor, a surface based upon the VS Code codebase but full of rich AI-enabled features designed to improve your code-writing experience.

Much of this editor is designed to feel the same as prior experiences you may have had. You can open files up, tab through them, edit them directly, get suggestions with [Tab](docs/tab), and work with an agent on [smaller](docs/command) or [larger tasks](docs/agent-side-panel). When you’re done, you can review your changes and interface with your preferred [source control](docs/review-changes-editor). You can also still download extensions from the Open VSX marketplace to augment your experience, through further syntax highlighting, source control integrations, or other additions.

![Editor Screenshot](assets/image/docs/editor/editor.png)

---

- side\_navigation
- [Editor](/docs/editor)
>- Tab

<a name="antigravity-editor-tab-navigation"></a>
## Antigravity Editor: Tab & Navigation

This guide covers the core navigation and completion tools: **Supercomplete**, **Tab-to-Jump**, and **Tab-to-Import**.

<a name="supercomplete"></a>
### Supercomplete

Supercomplete provides code suggestions in a region near your current cursor position.

![Supercomplete](assets/image/docs/editor/supercomplete.png)

<a name="how-it-works"></a>
#### How it Works

- **File-Wide Suggestions**: Suggestions can modify code throughout the document, handling tasks like changing variable names or updating separate function definitions simultaneously.
- **Accepting**: Press `Tab` to accept the changes.

<a name="tab-to-jump"></a>
### Tab-to-Jump

Tab-to-Jump is a fluid navigation tool that suggests the next logical place in your document to move your cursor to.

![Tab-to-Jump](assets/image/docs/editor/tab_to_jump.png)

<a name="how-it-works-1"></a>
#### How it Works

- A "Tab to jump" icon will appear offering to move your cursor to where your next logical edit will be. Pressing `Tab` instantly moves your cursor to that location.
- **Accepting**: Press `Tab` to accept the jump.

<a name="tab-to-import"></a>
### Tab-to-Import

Tab-to-Import handles missing dependencies without breaking your flow.

![Tab-to-Import](assets/image/docs/editor/tab_to_import.png)

<a name="how-it-works-2"></a>
#### How it Works

- **Detection**: If you type a class or function that isn't imported, Antigravity suggests the import.
- **Action**: Press `Tab` to complete the word and instantly add the import statement to the top of the file.

<a name="settings"></a>
### Settings

In your settings, you can customize the behavior of these features:

- **Enable/Disable Features**: You can individually turn off Autocomplete, Tab-to-Jump, Supercomplete, or Tab-to-Import.
- **Tab Speed**: Controls the responsiveness of suggestions.
- `Slow`: Waits for more context before suggesting.
- `Default`: Offers a balanced pace.
- `Fast`: Provides rapid-fire suggestions.
- **Highlight Inserted Text**: When enabled, text inserted via Tab is highlighted to track changes easily.
- **Clipboard Context**: When enabled, Antigravity uses the contents of your clipboard to improve completion accuracy.
- **Allow Gitignored Files**: Enables Tab features (suggestions and jumping) within files listed in your `.gitignore` file. Tab will only ignore gitignored files if git is installed.

---

- side\_navigation
- [Editor](/docs/editor)
>- Command

<a name="antigravity-editor-command"></a>
## Antigravity Editor: Command

The **Command** feature brings the power of natural language directly into your workflow, allowing you to request specific inline completions or terminal commands on the fly.

<a name="how-it-works-3"></a>
### How it Works

1. **Trigger**: Press `Command + I` (Mac) or `Ctrl + I` (Windows/Linux).
2. **Prompt**: A text input box will appear at your current cursor position.
3. **Instruction**: Type your request in natural language (e.g., "Create a function to sort this list" or "Add error handling to this block").
4. **Execution**: Antigravity generates the code or command directly inline for you to review and accept.

<a name="where-to-use-it"></a>
### Where to Use It

<a name="in-the-editor"></a>
#### In the Editor

![Command in Editor](assets/image/docs/editor/command_editor.png)

Use Command to generate boilerplate code, refactor complex functions, or write documentation without breaking your coding flow.

- *Example*: "Create a React component for a login form."

<a name="in-the-terminal"></a>
#### In the Terminal

![Command in Terminal](assets/image/docs/editor/command_terminal.png)

Use Command within the integrated Antigravity terminal to generate complex shell commands without needing to memorize syntax.

- *Example*: "Find all processes listening on port 3000 and kill them."

---

- side\_navigation
- [Editor](/docs/editor)
>- Agent Side Panel

<a name="agent-side-panel"></a>
## Agent Side Panel

Use the panel on the right side of the editor to work directly with the agent. You can spin up new conversations, attach images, switch [agent modes](docs/agent-modes-settings), and select between [different models](docs/models).

![Editor Agent Panel](assets/image/docs/editor/editor_agent_panel.png)

As your conversation progresses, you’ll be able to keep track of open file changes, running terminal processes, and artifacts in the bottom toolbar above the input.

![Editor Agent Panel](assets/image/docs/editor/agent_panel_toolbar.png)

---

- side\_navigation
- [Editor](/docs/editor)
>- Review Changes + Source Control

<a name="review-changes-source-control"></a>
## Review Changes + Source Control

Once the agent has begun writing code within a conversation, you’ll see a `Review Changes` section within the Agent panel’s [bottom toolbar](docs/agent-side-panel). Clicking it will open up a pane within your editor where you can scroll through all of the changes you and your agent made within the conversation.

![Editor Review Changes](assets/image/docs/editor/review_changes_editor.png)

Just like with artifacts, you can comment on any of the file diffs to communicate with the agent.

![Editor Source Control](assets/image/docs/editor/source_control_editor.png)

---

- side\_navigation
- Agent Manager

<a name="agent-manager"></a>
## Agent Manager

We've built out the Agent Manager, to provide a higher level view into the work Antigravity agents are doing under your guidance. Here, you can work across multiple workspaces, oversee dozens of agents simultaneously, and interact with your codebase primarily through the agent, rather than through writing code directly. As agents and models continue to get better, we believe that this birds-eye view will be the primary entry point to all of your work. For now, as we continue to get feedback and iterate on this new surface area, the Agent Manager is under open public preview. We expect to move it to be central to the Antigravity experience soon.

At any point, you can toggle between the Agent Manager and the editor by hitting CMD+E (Mac) or CTRL+E (Windows), or through the Open Editor & Open Agent Manager buttons at the top right of the menu bar. You can also manage your editor windows through the manager, either hiding, focusing, or closing them.

![Agent Manager Editor](assets/image/docs/agent_manager_editor.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- Workspaces

<a name="workspaces"></a>
## Workspaces

In the Agent Manager, you can work across multiple workspaces simultaneously. In order to open a new workspace, just select the button in the left sidebar and select a starting folder. At any point, you can switch between conversations across workspaces through the left sidebar.

![Switch Workspaces](../../../assets/image/docs/workspaces/switch_workspace.png)

To start a new conversation within a workspace, either select the desired workspace from the Start Conversation tab or hit the Plus button next to the workspace name in the sidebar.

![Start Conversation Within Workspace](../../../assets/image/docs/workspaces/start_within_workspace.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Workspaces](/docs/workspaces)
>- Playground

<a name="playground"></a>
## Playground

Playgrounds are independent workspaces that allow you to start a conversation and explore ideas instantly, without the overhead of setting up a new workspace.

<a name="creating-a-playground"></a>
### Creating a Playground

From the Start Conversation page, you can quickly send a message to a new playground by clicking the Use Playground button below the input box.

![Playground Button](../../../assets/image/docs/playground/playground_button.png)

From here, you can send a message as you would normally.

![Playground Send Message](../../../assets/image/docs/playground/playground_send.png)

<a name="persisting-your-work"></a>
### Persisting Your Work

If you want to keep the work you've done in a playground, you can move its contents into a dedicated workspace in a folder of your choosing. This action preserves your conversation history and any files created during your session, allowing you to continue exploring with multiple conversations.

![Playground Persist](../../../assets/image/docs/playground/playground_persist.png)

Clicking on the move button in the top bar will pop up the following modal:

![Playground Move Modal](../../../assets/image/docs/playground/playground_move.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Workspaces](/docs/workspaces)
>- Inbox

<a name="inbox"></a>
## Inbox

The inbox is your one stop shop to track all of your conversations in one place. From the inbox you can see if any of your conversations are awaiting your approval to run terminal commands, use the browser, or build out an implementation plan.

![Inbox Overview](../../../assets/image/docs/inbox/basic_inbox.png)

You can use the search bar and the pending switch to search for conversations by folder or by title to make sure your inbox is always focused on what is most relevant to you.

Selecting a conversation from the inbox will jump directly to the conversation, where you can continue where you left off.

![Continue Conversation](../../../assets/image/docs/inbox/continue_conversation.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- Conversation View

<a name="conversation-view"></a>
## Conversation View

The [Agent Panel](/docs/agent-side-panel) takes center stage in the agent manager. As the agent makes progress, you'll be able to follow along with what it's doing. To toggle off this follow-along mode, simply hit the `Following` button at the top right of the conversation.

![Follow Along Manager](assets/image/docs/follow_along_manager.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Conversation View](/docs/conversation-view)
>- Browser Subagent View

<a name="browser-subagent-view"></a>
## Browser Subagent View

<a name="overview"></a>
### Overview

The Manager has a dedicated side panel that allows you to expand and inspect the Agent’s work for a task.

![Browser Subagent View](assets/image/docs/browser-subagent-view.png)

In the regular manager conversation view (left half of the image), the browser subagent’s work is hidden. Clicking the expand button (shown in red box) will bring up the subagent view (right half of the image). Updates to the Agent’s work will be streamed into this view, so you can follow along and interact with steps as required (e.g. confirm/deny actions).

<a name="whats-in-the-side-panel"></a>
### What’s in the side panel

- All subagent actions (clicking, scrolling, navigating, etc.)
- Visual feedback showing exactly where clicks happened
- Screenshots captured at each step

<a name="visual-inspection-feature"></a>
### Visual Inspection Feature

Tool calls that produce actions in the browser, like clicks, include a button (shown in blue box) which opens a screenshot of the browser at that exact moment and a red dot showing what interaction the agent has done in the browser.

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Conversation View](/docs/conversation-view)
>- Panes

<a name="panes"></a>
## Panes

You can open files, [artifacts](/docs/artifacts), knowledge items, and other content directly within the manager in panes that persist per-conversation. In order to open up a pane, simply open up the quick picker (by hitting CMD+P on Mac or CTRL+P on Windows/Linux) and select a resource. You can also hit the "+" from within a conversation's header.

![Manager New Tab](assets/image/docs/agent-manager/manager_new_tab.png)![Manager File Picker](assets/image/docs/agent-manager/manager_file_picker.png)

These panes are resizable, splittable, and drag-and-droppable. You should configure them around as makes sense for your workflow.

![Manager Split Pane](assets/image/docs/agent-manager/manager_split_pane.png)

If you use CMD+Click or CMD+Enter (Mac) or CTRL+Click / CTRL+Enter (non-Mac), the contents will open in a new pane, rather than replacing the currently open pane.

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Conversation View](/docs/conversation-view)
>- Review Changes + Source Control

<a name="review-changes-source-control-1"></a>
## Review Changes + Source Control

Just as in the [editor](/docs/review-changes-editor), you can easily review the work you and your agent have collaborated on from within the manager.

Once you enter a conversation, you can toggle the Review Changes pane through the button at the top right to open up a pane where you can scroll through and comment on any file diffs made as a part of the conversation.

![Review Changes Manager](assets/image/docs/review_changes_manager.png)

You can similarly toggle to the Source Control tab within the Review Changes pane to see changed files, stage or unstage them, and commit them upstream.

![Manager Source Control](assets/image/docs/manager_source_control.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Conversation View](/docs/conversation-view)
>- Changes Sidebar

<a name="changes-sidebar"></a>
## Changes Sidebar

Similar to the toolbar at the bottom of the editor's [Agent Panel](docs/agent-side-panel), the Changes Sidebar in the manager offers a quick way to see what [artifacts](docs/artifacts) the agent has created and what files it has modified within a conversation.

Clicking on any of the listed resources will open its contents within a pane. The icons on each resource indicate whether there are new changes to a resource since your last review.

![Aux Sidebar](assets/image/docs/aux-sidebar.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Conversation View](/docs/conversation-view)
>- Terminal

<a name="terminal"></a>
## Terminal

The agent manager window has terminal support as well! To toggle this, use Cmd/Ctrl + J to open the bottom pane of the agent manager, which is where terminals live. They are attached to the workspace that your current conversation is in.

**Note:** Agent manager window's terminal integration works for local workspaces only, and Agent-used terminals run inside the editor window.

![agent-manager-terminal](assets/image/docs/agent-manager-terminal.png)

---

- side\_navigation
- [Agent Manager](/docs/agent-manager)
>- [Conversation View](/docs/conversation-view)
>- Files

<a name="files"></a>
## Files

As you open up [file panes](/docs/panes) within the manager, you can also leave comments for the agent to highlight specific points.

![File commenting manager](assets/image/docs/file_commenting_manager.png)

---

- side\_navigation
- Browser

<a name="browser"></a>
## Browser

Antigravity has the ability to open, read, and control a Chrome browser, allowing you to test development websites, read internet data sources, and automate various different browser tasks.

Using a [subagent](/docs/browser-subagent), Antigravity can operate on the browser as it sees fit, as well as [recording its actions](/docs/browser-recordings) and presenting select screenshots and videos as [artifacts](/docs/screenshots).

To isolate the Antigravity agent from your normal browsing, it runs in a separate browser profile. This means that it will show up as a separate application in your dock and nothing will be signed in. You can read more about this in the [Separate Chrome Profile](/docs/separate-chrome-profile) section.

To disable the use of all browser tools, you may disable the browser tools setting in the “Browser” section of your settings.

![Enable Browser Tools](/assets/image/docs/enable_browser_tools.png)

Antigravity detects and uses your existing Chrome application. If you don’t already have Chrome, you must download it here. If Antigravity is unable to detect your chrome installation, you may have to specify the path to it in the following setting:

![Chrome Binary Path](/assets/image/docs/chrome_binary_path.png)

---

- side\_navigation
- [Browser](/docs/browser)
>- Chrome Extension

<a name="chrome-extension"></a>
## Chrome Extension

Antigravity Browser Extension is required for the Antigravity Agent to access the web.

It empowers the agent to see and interact with websites to complete your development goals, whether you are building a site from scratch or automating a workflow.

It enhances the user experience by allowing the user to cancel the current conversation from the browser, switch the focus back to Antigravity from the web agent is working on, and more seamlessly work parallely with the browser agent.

The first time you use the Antigravity browser agent, you should be directed to the Chrome Web Store to install the extension.

<a name="troubleshooting"></a>
### Troubleshooting

If for any reason you need to manually install it:

- Click the Chrome icon in Antigravity (opens Chrome with Antigravity user profile)
- In the editor, you can find the Chrome icon on the top right
- In the Agent Manager, you can find the Chrome icon on the bottom left
- Navigate to the URL and click “Add to Chrome”

---

- side\_navigation
- [Browser](/docs/browser)
>- Allowlist / Denylist

<a name="allowlist-denylist"></a>
## Allowlist / Denylist

The browser uses a two-layer security system to control which URLs can be accessed:

- **Denylist** - Deny dangerous/malicious URLs
- **Allowlist** - Explicitly allow trusted URLs

<a name="how-it-works-4"></a>
### How It Works

<a name="denylist"></a>
#### Denylist

The denylist is maintained and enforced using the Google Superroots’s BadUrlsChecker service (See documentation). When the browser attempts to navigate to a URL, the hostname is checked against the server-side denylist via RPC.

**NOTE:** If the server is unavailable, access is denied by default.

<a name="allowlist"></a>
#### Allowlist

The allowlist is a local text file that you can edit to explicitly trust specific URLs.

![Allowlist](assets/image/docs/browser-allowlist.png)

The allowlist is initialized with just localhost, and can be edited at anytime.

When the browser attempts to navigate to a non-allowlisted URL, it will prompt you with an “always allow” button, which if clicked will add the URL to the allowlist and enable the browser to open and interact with the web page. An example situation is shown below:

![Always Allow](assets/image/docs/always-allow-url.png)

You can also add/remove URLS from the allowlist manually. However, the denylist always takes precedence: you cannot allowlist a URL that appears on the denylist.

---

- side\_navigation
- [Browser](/docs/browser)
>- Separate Chrome Profile

<a name="separate-chrome-profile"></a>
## Separate Chrome Profile

To isolate the browser from your general browsing, it operates on a [separate Chrome profile](https://support.google.com/chrome/answer/2364824).

Since Chrome profiles are isolated, this will not share any of the cookies or sign-in information from your normal browsing profile. However, all sign-ins will be persisted such that anytime you open the browser in the future, all your accounts will still be there. This profile should also contain your installation of the [Chrome Extension](./chrome-extension.md), so that your normal browsing profile is entirely unaffected.

If you had your normal Chrome open while launching this profile, it will show up as a separate dock icon and be considered a separate application. If Chrome was not open beforehand, this application will look the same as your default profile. To return to the default profile, you must quit the application and relaunch Chrome.

If you would like to change the location where your browser profile will be created, you can modify the following setting in the browser section.

![Browser Profile](../../../assets/image/docs/browser/browser-profile.png)

---

- side\_navigation
- Plans

<a name="plans"></a>
## Plans

At this moment, Google Antigravity is only available in public preview. This plan is for use by individual accounts, with [terms](/terms) derived from Google's terms of service, not Google Cloud's enterprise terms of service.

Rate limits and model availability differs based on usage of [Google AI paid plans](https://one.google.com/about/google-ai-plans/).

All plans receive:

- Use of Gemini 3 Pro and other offered Vertex Model Garden models as the core agent model
- Unlimited Tab completions
- Unlimited Command requests
- Access to all product features, such as the Agent Manager and Browser integration

Users on Google AI Ultra receive:

- The highest, most generous rate limits
- Quota is refreshed every five hours

Users on Google AI Pro receive:

- High, generous rate limits
- Quota is refreshed every five hours

Users not on Google AI plans receive:

- Meaningful rate limits
- Quota is refreshed every week

These rate limits are primarily determined to the degree we have capacity, and exist to prevent abuse. Under the hood, the rate limits are correlated with the amount of work done by the agent, which can differ from prompt to prompt. Thus, you may get many more prompts if your tasks are more straightforward and the agent can complete the work quickly, and the opposite is also true.

There is currently no support for:

- Bring-your-own-key or bring-your-own-endpoint for additional rate limits
- Organizational tiers (self-serve or via contract)

---

- side\_navigation
- Settings

<a name="settings-1"></a>
## Settings

You can configure your Antigravity settings across Agent, Browser, Editor, and more via:

- Keyboard shortcut in any surface: `Cmd + ,`
- From the Settings tab or gear icon in the Agent Manager
- From "Settings > Open Antigravity User Settings" in the Editor

<a name="data-collection-settings"></a>
### Data Collection Settings

The "Enable Telemetry" setting can be found in the Settings panel under the "Account" section. When toggled on, Antigravity collects interactions for use in evaluating, developing, and improving Antigravity and models that support Antigravity.

---

- side\_navigation
- FAQ

<a name="faq"></a>
## FAQ

<a name="why-can-i-not-authenticate-into-google-antigravity"></a>
### Why can I not authenticate into Google Antigravity?

Google Antigravity is currently available for personal Google accounts in approved geographies. Please try using an @gmail.com email address if having challenges with Workspace Google accounts.

<a name="why-is-my-age-unverified"></a>
### Why is my age unverified?

At the moment, Antigravity is unavailable to under-18 users. If you do meet the minimum age requirement, you may [verify your age](https://myaccount.google.com/age-verification) to continue using Antigravity.

<a name="what-is-google-antigravitys-geographical-availability"></a>
### What is Google Antigravity’s geographical availability?

Google Antigravity is available in the following countries and territories. If you're not in one of these countries or territories, you will be unable to use Google Antigravity at this time:

**Important**: Please check the country listed on the [Google Terms of Service](https://policies.google.com/terms) page. If this is the wrong country, you may [submit a request](https://policies.google.com/country-association-form) to change your associated region.

Americas

- American Samoa
- Anguilla
- Antigua and Barbuda
- Argentina
- Aruba
- Barbados
- Belize
- Bermuda
- Bolivia
- Brazil
- British Virgin Islands
- Canada
- Cayman Islands
- Chile
- Colombia
- Costa Rica
- Dominica
- Dominican Republic
- Ecuador
- El Salvador
- Grenada
- Guatemala
- Guyana
- Haiti
- Honduras
- Jamaica
- Mexico
- Montserrat
- Nicaragua
- Panama
- Paraguay
- Peru
- Puerto Rico
- Saint Lucia
- Saint Pierre and Miquelon
- Suriname
- Trinidad and Tobago
- Turks and Caicos Islands
- United States
- Uruguay
- Venezuela

Europe

- Armenia
- Austria
- Belgium
- Bulgaria
- Croatia
- Cyprus
- Czech Republic
- Denmark
- Estonia
- Finland
- France
- Germany
- Gibraltar
- Greece
- Hungary
- Iceland
- Ireland
- Italy
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Malta
- Netherlands
- Norway
- Poland
- Portugal
- Romania
- Slovakia
- Slovenia
- Spain
- Sweden
- Switzerland
- United Kingdom

Africa

- Algeria
- Angola
- Benin
- Botswana
- Burkina Faso
- Burundi
- Cameroon
- Central African Republic
- Chad
- Comoros
- Djibouti
- Egypt
- Equatorial Guinea
- Eritrea
- Ethiopia
- Gabon
- Ghana
- Guinea
- Kenya
- Lesotho
- Liberia
- Libya
- Madagascar
- Malawi
- Mali
- Mauritania
- Mauritius
- Morocco
- Mozambique
- Namibia
- Niger
- Nigeria
- Rwanda
- Senegal
- Seychelles
- Sierra Leone
- Somalia
- South Africa
- Tanzania
- Togo
- Tunisia
- Uganda
- Western Sahara
- Zambia
- Zimbabwe

Asia

- Azerbaijan
- Bahrain
- Bangladesh
- Bhutan
- British Indian Ocean Territory
- Cambodia
- Christmas Island
- Cocos (Keeling) Islands
- Georgia
- India
- Indonesia
- Iraq
- Israel
- Japan
- Jordan
- Kazakhstan
- Kuwait
- Kyrgyzstan
- Laos
- Lebanon
- Malaysia
- Maldives
- Mongolia
- Nepal
- Oman
- Pakistan
- Palestine
- Philippines
- Qatar
- Saudi Arabia
- Singapore
- South Korea
- Sri Lanka
- Taiwan
- Tajikistan
- Thailand
- Timor-Leste
- Turkey
- Turkmenistan
- United Arab Emirates
- Uzbekistan
- Vietnam
- Yemen

Oceania

- Australia
- Cook Islands
- Fiji
- Guam
- Kiribati
- Marshall Islands
- Micronesia
- Nauru
- New Zealand
- Niue
- Norfolk Island
- Northern Mariana Islands
- Palau
- Papua New Guinea
- Samoa
- Solomon Islands
- Tokelau
- Tonga
- Tuvalu
- Vanuatu

<a name="why-am-i-ineligible-for-google-one-ai-quotas-even-though-i-am-a-subscribed-to-a-plan"></a>
### Why am I ineligible for Google One AI quotas, even though I am a subscribed to a plan?

You might need to [verify your age](https://myaccount.google.com/age-verification) to receive the increased quotas.

<a name="what-is-google-antigravitys-stance-on-data-collection"></a>
### What is Google Antigravity’s stance on data collection?

Please refer to the [Terms of Service](/terms). You may opt out of data collection at any point from the Settings panel.

<a name="how-do-i-get-support"></a>
### How do I get support?

During this public preview period, there will be limited support at [antigravity-support@google.com](mailto:antigravity-support@google.com)

<a name="what-are-the-model-rate-limits"></a>
### What are the model rate limits?

Please see more details in the docs on [Plans](/docs/plans).

<a name="does-google-antigravity-currently-support-worktrees"></a>
### Does Google Antigravity currently support worktrees?

Not at the moment.

<a name="what-happens-when-my-computer-goes-to-sleep"></a>
### What happens when my computer goes to sleep?

If an agent is running, Antigravity will prevent your computer from sleeping.