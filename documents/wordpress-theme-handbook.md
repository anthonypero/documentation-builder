# WordPress Theme Handbook

## Table of Contents

- [Theme Handbook](#theme-handbook)
- [Getting Started](#getting-started)
  - [Navigating this chapter](#navigating-this-chapter)
- [What Is a Theme?](#what-is-a-theme)
  - [In this article](#in-this-article)
  - [What can themes do?](#what-can-themes-do)
  - [Theme types](#theme-types)
  - [Become familiar with themes](#become-familiar-with-themes)
  - [What are themes made of?](#what-are-themes-made-of)
  - [What is the difference between themes and plugins?](#what-is-the-difference-between-themes-and-plugins)
- [Who Is This Handbook For?](#who-is-this-handbook-for)
  - [In this article](#in-this-article-1)
  - [Your skill level](#your-skill-level)
  - [What this handbook covers](#what-this-handbook-covers)
- [Reading This Handbook](#reading-this-handbook)
  - [In this article](#in-this-article-2)
  - [Requirements](#requirements)
  - [Your next steps](#your-next-steps)
  - [How to read code examples](#how-to-read-code-examples)
- [Tools and Setup](#tools-and-setup)
  - [In this article](#in-this-article-3)
  - [Development environment](#development-environment)
  - [Installing WordPress](#installing-wordpress)
  - [Code editor](#code-editor)
  - [Other development tools](#other-development-tools)
  - [WordPress.org Theme Review Guidelines](#wordpressorg-theme-review-guidelines)
- [Quick-Start Guide](#quick-start-guide)
  - [In this article](#in-this-article-4)
  - [Activating your first theme](#activating-your-first-theme)
  - [Customizing your theme](#customizing-your-theme)
  - [Exporting your theme](#exporting-your-theme)
  - [Custom CSS](#custom-css)
- [Templates](#templates)
  - [In this article](#in-this-article-5)
  - [What are templates?](#what-are-templates)
  - [Including JavaScript](#including-javascript)
  - [Including images](#including-images)
  - [Including fonts](#including-fonts)
- [Global Settings and Styles](#global-settings-and-styles)
  - [In this article](#in-this-article-6)
  - [What is theme.json?](#what-is-themejson)
  - [theme.json structure](#themejson-structure)
  - [Settings and styles hierarchy](#settings-and-styles-hierarchy)
- [Starter Patterns](#starter-patterns)
  - [In this article](#in-this-article-7)
  - [Starter page patterns](#starter-page-patterns)
- [Block Stylesheets](#block-stylesheets-1)
  - [In this article](#in-this-article-8)
  - [Why use block stylesheets?](#why-use-block-stylesheets)
  - [Creating block stylesheets](#creating-block-stylesheets)
- [Feedback](#feedback)
  - [Giving Feedback](#giving-feedback)

<a name="theme-handbook"></a>
## Theme Handbook

[↑ Back to top](#wp--skip-link--target)

*Welcome to the WordPress Theme Developer Handbook, your resource for learning all about the exciting world of WordPress themes.*

The Theme Developer Handbook is a repository for all things WordPress themes. Whether you’re new to WordPress themes, or you’re an experienced theme developer, you should be able to find the answer to many of your theme-related questions right here.

In this handbook, you can learn how to build **block themes or classic themes.**

- A block theme is a new theme that you can use from WordPress version 5.9. It is built mainly using HTML and a theme configuration file. The block theme is composed entirely of blocks, allowing you to edit all parts of your site in the Site Editor.
- A classic theme is the original theme, without version limitations, that primarily uses PHP, JavaScript and CSS. Classic themes take advantage of WordPress PHP functions, hooks and filters.

1. If you’re new to developing WordPress themes, start with section 1, where you can [find out what a theme is](https://developer.wordpress.org/theme/getting-started/what-is-a-theme/), learn about [WordPress’ license](https://wordpress.org/about/license/), and [set up your development environment](https://developer.wordpress.org/themes/getting-started/tools-and-setup/).
2. Once you’re through the introduction, continue with the [Core Concepts](https://developer.wordpress.org/themes/core-concepts/) section.

It is recommended to read through both the block theme section and the classic theme sections. This will give you an understanding of the differences between the two types of themes, and help you choose what type of theme to build.

If you’ve got to grips with the basics of themes, check out the [Advanced Theme Topics](https://developer.wordpress.org/theme/advanced-topics/) to learn about child themes, best UI practices, theme testing and more.

Once you’ve got your theme ready for the world, the final section will cover [releasing your theme](https://developer.wordpress.org/themes/releasing-your-theme/), teaching you some best practices for theme distribution, and for getting it ready for the WordPress.org theme directory.

---

The WordPress Theme Developer Handbook is created by the WordPress community, for the WordPress community. We are always looking for more contributors; if you’re interested stop by the [docs team blog](https://make.wordpress.org/docs) to find out more about getting involved.

First published

July 30, 2014

Last updated

December 15, 2023

[Next
Getting Started
Next: Getting Started](https://developer.wordpress.org/themes/getting-started/)

---

<a name="getting-started"></a>
## Getting Started

[↑ Back to top](#wp--skip-link--target)

Welcome to the Getting Started documentation. This chapter is primarily intended to introduce you to navigating the handbook itself, learning what WordPress themes are, and helping you get your first WordPress block theme up and running.

While this chapter primarily focuses on readers who are new to theme development altogether, it is also meant as a resource for seasoned themers who are learning how to build block themes for the first time.

<a name="navigating-this-chapter"></a>
### Navigating this chapter

Use the following links to locate a topic within this chapter. Each article will walk you through the steps of navigating this handbook and getting a base understanding of how WordPress themes work:

- [**What Is a Theme?**](https://developer.wordpress.org/themes/getting-started/what-is-a-theme/)**:** An introduction to what WordPress themes are and an explanation of the various types of themes.
- [**Who Is This Handbook For?**](https://developer.wordpress.org/themes/getting-started/who-is-this-handbook-for/)**:** Explains who this handbook is for and why you might want to read it.
- [**Reading This Handbook**](https://developer.wordpress.org/themes/getting-started/reading-this-handbook/)**:** Offers learning pathways for navigating the handbook based on skill level and provides an introduction on reading code samples.
- [**Tools and Setup**](https://developer.wordpress.org/themes/getting-started/tools-and-setup/)**:** Gives an overview of all the tools that are required to create WordPress themes and offers recommendations on other useful apps and programs to consider.
- [**Quick-Start Guide**](https://developer.wordpress.org/themes/getting-started/quick-start-guide/)**:** A step-by-step guide for getting your first basic theme up and running for those new to block theme development.

First published

July 31, 2014

Last updated

December 14, 2023

[Next
What Is a Theme?
Next: What Is a Theme?](https://developer.wordpress.org/themes/getting-started/what-is-a-theme/)

---

<a name="what-is-a-theme"></a>
## What Is a Theme?

<a name="in-this-article"></a>
### In this article

Table of Contents

- [What can themes do?](#what-can-themes-do)
- [Theme types](#theme-types)
  - [Block themes](#block-themes)
  - [Classic themes](#classic-themes)
  - [Hybrid themes](#hybrid-themes)
- [Become familiar with themes](#become-familiar-with-themes)
- [What are themes made of?](#what-are-themes-made-of)
- [What is the difference between themes and plugins?](#what-is-the-difference-between-themes-and-plugins)

[↑ Back to top](#wp--skip-link--target)

A WordPress theme represents the design of your website. It can control everything from colors, to fonts, to the entire layout. In essence, what you see when viewing the front-end of your site is shaped by the theme.

[![A collage of site designs at an angle.](https://i0.wp.com/developer.wordpress.org/files/2023/11/twenty-twenty-two-collage.jpg?resize=2400%2C1500&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/twenty-twenty-two-collage.jpg?ssl=1)

Templates from the default Twenty Twenty-Two theme.

There are 1,000s of free WordPress themes in the [WordPress.org Theme Directory](https://wordpress.org/themes/) and even more from third-party directories and shops. Many people and businesses also have bespoke (custom-made) themes for their sites.

<a name="what-can-themes-do"></a>
### [What can themes do?](#what-can-themes-do)

Themes take the content stored by WordPress and display it in the browser. When you create a WordPress theme, you decide how that content looks and is displayed. There are many options available to you when building your theme. The biggest limit is your imagination.

As a theme creator, you can:

- Create different layouts, such as one, two or more columns.
- Control the typography of the site with custom font choices.
- Skin the site with any color scheme you want.
- Put a sidebar on the left or right side of the page. Or, have no sidebar at all.
- Display featured images alongside posts.

[![The WordPress site editor showing the homepage template with a dotted black background and a three-column grid of posts.](https://i0.wp.com/developer.wordpress.org/files/2023/11/twenty-twenty-three-style-variation.jpg?resize=2400%2C1255&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/twenty-twenty-three-style-variation.jpg?ssl=1)

Editing a Twenty Twenty-Three theme style variation.

The WordPress theming system is incredibly powerful. As with every web design project, a good theme is more than defining a layout or two and a few custom colors. The best themes improve engagement with a website’s content *in addition* to being beautiful.

There really are not many limits to the possibilities. Outside of your imagination, theme creation requires some baseline knowledge, which is covered in the [Reading this handbook](https://developer.wordpress.org/themes/getting-started/reading-this-handbook/) page of this chapter. That’s what this handbook is all about—*teaching you what you need to know to build themes of your own*.

<a name="theme-types"></a>
### [Theme types](#theme-types)

WordPress supports two primary types of themes: **block** and **classic**.

There is also a classic subtype that is called a **hybrid** theme, and you’ll learn about it below, too. But the most important distinction is block vs. classic.

Technically, you can even build your own theming system altogether. That’s outside the scope of this handbook, but it’s at least worth noting that WordPress lets you build pretty much whatever you set your mind to.

<a name="block-themes"></a>
#### [Block themes](#block-themes)

Block themes are the modern method of building WordPress themes. They generally follow a standard set of conventions and are built entirely out of blocks. This handbook will primarily focus on building themes using this method because it is the future of the WordPress project.

Block themes rely on HTML-based [block templates](https://developer.wordpress.org/themes/templates/) that contain block markup. Both creators and users can edit the templates in the Site Editor. Users can also customize [global settings and styles](https://developer.wordpress.org/themes/global-settings-and-styles/) defined by the theme’s `theme.json` file through the Styles interface.

It’s also possible to export a theme directly from the Site Editor without touching any code. Technically, you cannot create a new theme from scratch entirely from the editor, but you can modify the templates and styles of an existing theme—in essence, creating a custom theme of your own.

[![WordPress site editor with a single post template that shows a design with a yellow background and black text.](https://i0.wp.com/developer.wordpress.org/files/2023/11/site-editor-styles.png?resize=2400%2C1255&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/site-editor-styles.png?ssl=1)

Editing a theme’s styles in the Site Editor.

<a name="classic-themes"></a>
#### [Classic themes](#classic-themes)

Classic themes use a PHP-based templating system, which is still supported in WordPress today. They are still in wide use because they were built on the theming system that was first introduced in 2005 with the launch of [WordPress 1.5](https://wordpress.org/news/2005/02/strayhorn/). There is a long and deep history of classic theming in WordPress, which continues on. For this reason, the handbook maintains documentation for classic themes in the [Classic Themes](https://developer.wordpress.org/themes/classic-themes/) chapter.

Unlike block themes, classic themes have far fewer standards to adhere to, but there are APIs you can use for specific features. The classic theme creation process also requires some minimal PHP, HTML, and CSS code knowledge, at least.

[![WordPress customizer showing the Twenty Twenty-Two theme. On the left is a list of options, and on the right a preview of the site homepage.](https://i0.wp.com/developer.wordpress.org/files/2023/11/customizer-twenty-twenty.jpg?resize=2400%2C1255&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/customizer-twenty-twenty.jpg?ssl=1)

Editing the default Twenty Twenty theme styles in the customizer.

<a name="hybrid-themes"></a>
#### [Hybrid themes](#hybrid-themes)

Hybrid themes are merely classic themes that have adopted some modern block-related features, such as [global settings and styles](https://developer.wordpress.org/themes/global-settings-and-styles/) or [block template parts](https://developer.wordpress.org/themes/templates/template-parts/). This is a widely agreed-upon term by the community, but it is not an “official” theme type. At the end of the day, hybrids are still classic themes.

<a name="become-familiar-with-themes"></a>
### [Become familiar with themes](#become-familiar-with-themes)

To build a WordPress theme of your own, you should familiarize yourself with how themes work from a user’s viewpoint. Before diving into the creation process, try [installing a theme](https://wordpress.org/documentation/article/work-with-themes/) and playing around with it.

WordPress comes with several default themes, titled *Twenty [Year]*, but you should also try other themes from the [Theme Directory](https://wordpress.org/themes/) just to get a feel for the possibilities.

<a name="what-are-themes-made-of"></a>
### [What are themes made of?](#what-are-themes-made-of)

Themes can include many different folders and file types. The list below is non-exhaustive, but it includes some of common things you might see:

- Templates (`.html` in block themes and `.php` in classic themes)
- CSS Stylesheets
- JavaScript
- PHP
- Media (images, audio, video, etc.)
- JSON

You will learn more about the specific folders and files used to create a theme in the next chapter: [Core Concepts](https://developer.wordpress.org/themes/core-concepts).

<a name="what-is-the-difference-between-themes-and-plugins"></a>
### [What is the difference between themes and plugins?](#what-is-the-difference-between-themes-and-plugins)

It is common for there to be overlap between features found in themes and plugins. However, best practices are:

- Themes control the *presentation* of content.
- Plugins control the behaviors and features of your site.

Any theme that you create should not add site-critical functionality. Doing so means that a user loses access to that functionality when they change their theme.

For example, say you build a theme with a portfolio feature. Users who build their portfolio with your feature will lose it when they change themes. By leaving critical features to plugins, you make it possible to change the design of a website while its features remain intact.

Remember, some users switch themes often. It is best practice to make sure any functionality their sites require, even if the design changes, is in a separate plugin.

First published

July 31, 2014

Last updated

December 14, 2023

[Previous
Getting Started
Previous: Getting Started](https://developer.wordpress.org/themes/getting-started/)

[Next
Who Is This Handbook For?
Next: Who Is This Handbook For?](https://developer.wordpress.org/themes/getting-started/who-is-this-handbook-for/)

---

<a name="who-is-this-handbook-for"></a>
## Who Is This Handbook For?

<a name="in-this-article-1"></a>
### In this article

Table of Contents

- [Your skill level](#your-skill-level)
- [What this handbook covers](#what-this-handbook-covers)

[↑ Back to top](#wp--skip-link--target)

The Theme Developer Handbook is a self-contained resource to help you learn the fundamental principles of creating a WordPress theme. It covers a range of topics that span the basics to advanced development.

You should read this handbook if you want to:

- Create a theme based on nothing but your imagination
- Build a new theme based on an existing one
- Extend another theme by creating a child theme
- Understand how themes work

Regardless of your reasons for starting down this adventure, this handbook will help you take the next steps toward building a WordPress theme of your own.

<a name="your-skill-level"></a>
### [Your skill level](#your-skill-level)

While not a strict requirement, you will get the most out of this handbook if you have a baseline understanding and some experience with web technologies, such as HTML, CSS, and PHP. JavaScript knowledge would be a bonus if you plan to add interactivity to the front end.

Present-day WordPress and its block theme system allow you to customize and export a theme directly from the Site Editor interface:

[![WordPress Site Editor with the options menu dropdown open on the right. The Export option is highlighted.](https://i0.wp.com/developer.wordpress.org/files/2023/11/twenty-twenty-three-export.jpg?resize=2400%2C1250&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/twenty-twenty-three-export.jpg?ssl=1)

Exporting a variation of the core Twenty Twenty-Three theme.

With each major WordPress update, its visual building tools become even more robust. Still, having some basic HTML, CSS, and PHP knowledge will help you move along faster.

Unlike block themes, [classic themes](https://developer.wordpress.org/themes/classic-themes/) are built entirely from code. This requires that you be comfortable enough to edit one or more of those languages to some degree.

The [Reading this handbook](https://developer.wordpress.org/themes/getting-started/reading-this-handbook/) page has more information on the prerequisite knowledge you need to build themes.

At the very least, you must be able to set up and configure a website using WordPress. Otherwise, you won’t be able to test or use the theme that you are building. You can learn more about getting things running in the [Tools and setup](https://developer.wordpress.org/themes/getting-started/tools-and-setup/) documentation.

<a name="what-this-handbook-covers"></a>
### [What this handbook covers](#what-this-handbook-covers)

This handbook provides the basic information you need to build both block and classic WordPress themes. This includes in-depth coverage of the essential features and APIs that you should know, such as the topics in the [Core Concepts](https://developer.wordpress.org/themes/core-concepts/) chapter. It also dives into tools and techniques for building more advanced themes in the [Advanced Topics](https://developer.wordpress.org/themes/advanced-topics/) chapter.

WordPress is a vast subject. HTML, CSS, PHP, accessibility, and other web technologies are even larger. It’d be impossible to cover every aspect of building a website in this handbook alone. Therefore, it is highly-focused on the fundamentals of theme building.

The goal of this handbook is to give you a solid foundation for WordPress theme creation by providing step-by-step instructions for building basic themes and providing resources to further your skills.

If this sounds like something you’d be interested in, come along. You’re in for a journey.

First published

November 21, 2023

Last updated

December 14, 2023

[Previous
What Is a Theme?
Previous: What Is a Theme?](https://developer.wordpress.org/themes/getting-started/what-is-a-theme/)

[Next
Reading This Handbook
Next: Reading This Handbook](https://developer.wordpress.org/themes/getting-started/reading-this-handbook/)

---

<a name="reading-this-handbook"></a>
## Reading This Handbook

<a name="in-this-article-2"></a>
### In this article

Table of Contents

- [Requirements](#requirements)
- [Your next steps](#your-next-steps)
  - [For newcomers](#for-newcomers)
  - [For seasoned theme authors](#for-seasoned-theme-authors)
  - [For classic themes documentation](#for-classic-themes-documentation)
- [How to read code examples](#how-to-read-code-examples)
  - [Namespacing examples](#namespacing-examples)

[↑ Back to top](#wp--skip-link--target)

The goal of this handbook is to walk you through the basics of modern WordPress theme development in its early chapters. Then, work through more advanced topics with each chapter that follows.

The quickest way to learn theme development is to simply read this handbook from beginning to end and follow along with its examples.

<a name="requirements"></a>
### [Requirements](#requirements)

The biggest requirement for building a WordPress theme is a willingness to learn. You are here reading this handbook, so let’s check that one off the list of requirements.

WordPress theming has changed many times over the years. Today, the pathway for creating one is much lower than it was in the past. You can absolutely create a theme with no coding knowledge. But you will find it much easier to familiarize yourself with a few web languages.

You will see HTML, CSS, PHP, JSON, and JavaScript within the handbook, so it helps to be able to easily recognize what language you are looking at. HTML and CSS are foundational pieces of the web, so those should be prioritized over others.

The following are external resources that you can use to learn more, but there are 1,000s of guides and tutorials around the web:

- [MDN Web Docs: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN Web Docs: CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [PHP official documentation](https://www.php.net/docs.php)
- [MDN Web Docs: JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [MDN Web Docs: JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript)

You can get pretty far into theme building via the WordPress user interface, at least by modifying and exporting an existing block theme. But you’ll want to pick up a few more skills to build more advanced features, or to truly create a theme from scratch.

<a name="your-next-steps"></a>
### [Your next steps](#your-next-steps)

<a name="for-newcomers"></a>
#### [For newcomers](#for-newcomers)

It is time to truly embark on your journey into learning theme development. It is an exciting moment, so get ready for an adventure.

**Setting things up:** if this is your first time building a theme, or if you just want a refresher on the basics of theme development, your next stop should be the [Tools and Setup](https://developer.wordpress.org/themes/getting-started/tools-and-setup/) page. This will help you set up your development environment and determine which tools you need to start off on the right foot.

**Getting off to a quick start:** once you’re set up, check out the [Quick-start guide](https://developer.wordpress.org/themes/getting-started/quick-start-guide/), which is aimed at giving you a taste of what’s to come. It will walk you through setting up a theme to work with.

**Understanding the basics:** once you have everything set up and running, move onto the [Core Concepts](https://developer.wordpress.org/themes/core-concepts/) chapter. There, you will learn the foundational principles behind creating WordPress themes.

Afterward, just keep working through each chapter of the handbook.

<a name="for-seasoned-theme-authors"></a>
#### [For seasoned theme authors](#for-seasoned-theme-authors)

Even if you’ve been creating themes for years, it never hurts to give the full handbook a reading from time to time. It is regularly updated, so there may be new content that you haven’t seen before.

Feel free to hop around to find the specific topic you need using the handbook’s navigation links. Whatever the case, the Theme Handbook is here to help you discover a solution.

*Feeling pretty hardcore?* Jump over to the [Advanced Topics](https://developer.wordpress.org/themes/advanced-topics/) chapter.

*Can’t remember the naming format for a particular template?* Find it in the [Template Hierarchy](https://developer.wordpress.org/themes/templates/template-hierarchy/) docs.

*Need to brush up on `theme.json`?* No problem. Check out the [Global Settings and Styles](https://developer.wordpress.org/themes/global-settings-and-styles/) documentation.

You can also find theming tutorials and walk-throughs under the [Themes category](https://developer.wordpress.org/news/category/themes/) on the WordPress Developer blog if you can’t find the topic you’re looking for in the handbook.

<a name="for-classic-themes-documentation"></a>
#### [For classic themes documentation](#for-classic-themes-documentation)

While some of the content in most chapters will apply to classic themes, the docs are primarily geared toward modern block theming. However, there is a dedicated [Classic Themes](https://developer.wordpress.org/themes/classic-themes/) chapter if you need to locate documentation on a specific classic feature.

<a name="how-to-read-code-examples"></a>
### [How to read code examples](#how-to-read-code-examples)

Throughout the handbook, you will see code examples, and this section is aimed at helping you understand how to read them.

The handbook will use a consistent “namespace” or “prefix” throughout its pages, generally seen as `theme_slug` or `theme-slug`.  This namespace is meant to be replaced in your theme with one that is unique to it.

*But how do you know what your namespace is?* The most straightforward way is to use your theme’s name. If your theme is titled **Fabled Sunset**, you would convert it to the appropriate format for the use case. For example, it would become `fabled_sunset` when used in a PHP function name or `fabled-sunset` as a handle/slug/ID.

The practice of “namespacing” code is decades old. Essentially, a namespace is an identifier for a group of objects created so that they do not conflict with objects in other namespaces.

WordPress has a vast ecosystem of plugins and themes. Each needs a way to distinguish itself from the others. Without unique namespaces, it would get a bit chaotic and errors would arise.

For example, if your theme declared a custom function named `get_post()` instead of `fabled_sunset_get_post()`, your site would fail with a fatal error because WordPress already has a function with this name:

[![Screenshot of an error message stating that you cannot redeclare the get_post() function, which was already declared.](https://i0.wp.com/developer.wordpress.org/files/2023/11/fatal-error.jpg?resize=1760%2C824&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/fatal-error.jpg?ssl=1)

Avoiding these types of errors is the primary reason the handbook will include namespaced or prefixed code examples.

<a name="namespacing-examples"></a>
#### [Namespacing examples](#namespacing-examples)

Using the fictional theme name **Fabled Sunset**, let’s look at some examples of formatting your namespace. Don’t worry if you don’t understand these yet or if you do not know anything about code. This is only meant to help you read the handbook.

**Usage in script and style handles:**

```auto
<?php
// theme-slug-editor becomes:
wp_enqueue_script( 'fabled-sunset-editor', ... );

// theme-slug-main becomes:
wp_enqueue_style( 'fabled-sunset-main', ... );
```

**Usage in text domains (used for translations):**

```auto
<?php
// theme-slug becomes:
esc_html_e( 'Hello, world!', 'fabled-sunset' );
```

**Usage in PHP Functions:**

```auto
<?php
// theme_slug_func() becomes:
function fabled_sunset_func() {
	// ...
}
```

**Usage in PHP classes:**

```auto
<?php
// Theme_Slug_Class() becomes:
class Fabled_Sunset_Class() {
	// ...
}
```

As you read through the handbook, you will learn when to use each case. For now, just know that you should always replace the example namespace with one that is unique to your project.

The WordPress Coding Standards [encourages the use of PHP’s built-in namespaces](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/#namespace-declarations). The same guideline would apply: use your theme’s name to create your namespace. In this case, the namespace for the example theme would be `Fabled_Sunset` or `FabledSunset`. The Theme Handbook uses a prefixed style for PHP function and class names, as shown above. This is primarily because it is simpler for showing one-off code examples.

First published

November 21, 2023

Last updated

December 14, 2023

[Previous
Who Is This Handbook For?
Previous: Who Is This Handbook For?](https://developer.wordpress.org/themes/getting-started/who-is-this-handbook-for/)

[Next
Tools and Setup
Next: Tools and Setup](https://developer.wordpress.org/themes/getting-started/tools-and-setup/)

---

<a name="tools-and-setup"></a>
## Tools and Setup

<a name="in-this-article-3"></a>
### In this article

Table of Contents

- [Development environment](#development-environment)
  - [Why set up a development environment?](#why-set-up-a-development-environment)
  - [Setting up a local development environment](#setting-up-a-local-development-environment)
- [Installing WordPress](#installing-wordpress)
- [Code editor](#code-editor)
- [Other development tools](#other-development-tools)
  - [Test data](#test-data)
  - [Plugins](#plugins)
- [WordPress.org Theme Review Guidelines](#wordpress-org-theme-review-guidelines)

[↑ Back to top](#wp--skip-link--target)

In this document, you will learn about the tools that you will need to get off to a solid start when building WordPress themes. You will also find resources on setting up a development environment for testing your projects.

While it is definitely possible to create and build block themes without any of these tools, they are foundational pieces of a good workflow.

<a name="development-environment"></a>
### [Development environment](#development-environment)

When building WordPress themes, it is a good idea to do it within an environment that is separate from a live (i.e., production) site. Before creating your first WordPress theme, you should set up a development environment.

Don’t let this process scare you if it’s your first time. In the long run, you will be happy you learned how to set this up.

<a name="why-set-up-a-development-environment"></a>
#### [Why set up a development environment?](#why-set-up-a-development-environment)

Development environments allow you to test code before it goes live on a production site. You don’t want to change something, push it live, and later realize you created a fatal error that took down the whole website.

By using a development environment, you can test things to ensure they work before they are live.

Your development environment can either be local (on your computer) or on a remote server. But configuring a local environment to work on your theme is beneficial for several reasons:

- You do not need an internet connection to build your theme.
- You can build your theme without relying on a remote server. This speeds up the building process, and you can see changes instantly in your browser.
- You can test your theme from many perspectives. This is important if you plan on releasing it to a larger audience and want maximum compatibility.

<a name="setting-up-a-local-development-environment"></a>
#### [Setting up a local development environment](#setting-up-a-local-development-environment)

For developing WordPress themes, you need to set up a development environment that is suited to WordPress. This list is not exhaustive, but here are several options to choose from:

- [@wordpress/env](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-env/) (local WordPress environment package)
- [Docker](https://www.docker.com/)
- [WordPress Studio](https://developer.wordpress.com/studio/)
- [Local](https://localwp.com/)
- [MAMP](https://www.mamp.info/en/mamp/mac/)
- [XAMPP](https://www.apachefriends.org/)
- [Varying Vagrant Vagrants](https://varyingvagrantvagrants.org/) (VVV)

For more information, read the [Setting Up a Development Environment](https://make.wordpress.org/core/handbook/tutorials/installing-a-local-server/) documentation in the Core Handbook.

<a name="installing-wordpress"></a>
### [Installing WordPress](#installing-wordpress)

Before you begin building themes in your development environment, you must also install WordPress.

Some of the development environments include methods for automatically installing an instance of WordPress. You can skip this step if this is the case for you.

To install WordPress on your own, follow the [How to install WordPress](https://developer.wordpress.org/advanced-administration/before-install/howto-install/) documentation from the Advanced Administration handbook. Then, of course, come back here and learn more about creating WordPress themes!

<a name="code-editor"></a>
### [Code editor](#code-editor)

> *A good code editor is worth its weight in gold.*
>
> Someone Wise

On a more serious note, a good code editor gives you proper syntax highlighting, error reporting, integration with version control systems (VCS), and much more. It’s there to make your life easier.

Technically, you could edit code in a plain text editor, but you’d be missing out on all the best features that true code editors and IDEs (Integrated Development Environments) bring to life.

[![Visual Studio Code editor program with a theme's single.html file open, showing block markup.](https://i0.wp.com/developer.wordpress.org/files/2023/11/vs-code-editor.png?resize=2757%2C1497&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/vs-code-editor.png?ssl=1)

Editing a theme’s `single.html` template in Visual Studio Code

There are many free and open-source editors to choose from. Here are some of the more popular ones:

- [Visual Studio Code](https://code.visualstudio.com/) (VS Code)
- [VIM](https://www.vim.org/)
- [Brackets](https://brackets.io/)
- [Notepad++](https://notepad-plus-plus.org/)
- [GNU Emacs](https://www.gnu.org/software/emacs/)
- [TextMate](https://macromates.com/)

There are also many proprietary editors that are free or cost a fee to use. Whatever you decide to use, pick something you feel comfortable with.

<a name="other-development-tools"></a>
### [Other development tools](#other-development-tools)

A code editor and development environment are the foundational pieces of creating a WordPress theme. However, there are other tools and resources that you will likely find useful for your project.

<a name="test-data"></a>
#### [Test data](#test-data)

WordPress allows you to [import XML files](https://wordpress.org/documentation/article/importing-content/) containing real or dummy data for testing your themes. This lets you see how your theme performs with different types of content and layouts. Here are two options for importing:

- [WordPress.org Theme Test Data](https://codex.wordpress.org/Theme_Unit_Test)
- [WordPress.com Theme Test Data](http://themetest.wordpress.com/) *(includes WordPress.com-specific data)*

If nothing else, you need some type of demo/test content to see what your theme looks like in action. You could even create test posts and pages of your own!

<a name="plugins"></a>
#### [Plugins](#plugins)

In addition to test data, there are several WordPress plugins that can help make sure your theme is following standard practices and not producing debugging notices. These are optional but can be useful:

- [Theme Check](https://wordpress.org/plugins/theme-check/): Tests your theme for compliance with the latest WordPress standards and practices.
- [Debug Bar](https://wordpress.org/plugins/debug-bar/): Adds an admin bar to your WordPress admin and provides a central location for debugging.
- [Query Monitor](https://wordpress.org/plugins/query-monitor/): Allows debugging of database queries, API requests, and AJAX used to generate theme pages and functionality.
- [Log Deprecated Notices](https://wordpress.org/plugins/log-deprecated-notices/): Logs incorrect function usage, deprecated file usage, and deprecated function usage in your theme.
- [Monster Widget](https://wordpress.org/plugins/monster-widget/): Consolidates the core WordPress widgets into a single widget, making it easier to test them all at once (*classic themes only*).

<a name="wordpressorg-theme-review-guidelines"></a>
### [WordPress.org Theme Review Guidelines](#wordpress-org-theme-review-guidelines)

It is a good idea to stay up to date with the [theme guidelines](https://make.wordpress.org/themes/handbook/review/required/) provided by the WordPress.org Themes Team. These guidelines are required if you plan to submit your theme to the official [Theme Directory](https://wordpress.org/themes), but they are also good principles for anyone creating a theme.

You should also follow the [WordPress Coding Standards](https://make.wordpress.org/core/handbook/best-practices/coding-standards/) when writing any code for your theme. This will help make sure what you are creating meets some minimum quality standards.

First published

November 21, 2023

Last updated

July 11, 2025

[Previous
Reading This Handbook
Previous: Reading This Handbook](https://developer.wordpress.org/themes/getting-started/reading-this-handbook/)

[Next
Quick-Start Guide
Next: Quick-Start Guide](https://developer.wordpress.org/themes/getting-started/quick-start-guide/)

---

<a name="quick-start-guide"></a>
## Quick-Start Guide

<a name="in-this-article-4"></a>
### In this article

Table of Contents

- [Activating your first theme](#activating-your-first-theme)
  - [Choosing a theme to learn from](#choosing-a-theme-to-learn-from)
- [Customizing your theme](#customizing-your-theme)
- [Exporting your theme](#exporting-your-theme)
  - [Exporting from the Styles interface](#exporting-from-the-styles-interface)
  - [Using the Create Block Theme plugin](#using-the-create-block-theme-plugin)

[↑ Back to top](#wp--skip-link--target)

The first step is always the hardest to take. Now that you’ve made it this far into the Getting Started chapter, you’ve already taken several steps. Congratulations on getting through all of the necessary setup.

In a way, actually building your first theme can feel like another first step, but you are ready to trek out into the wilderness and beyond. Don’t worry—this guide will walk with you as you set out on this journey.

<a name="activating-your-first-theme"></a>
### [Activating your first theme](#activating-your-first-theme)

One of the best ways to understand how to build themes is to look at and study existing themes.

Even in advanced development circles, one of the cornerstones of sound development is to reuse code. This is because developers understand that this is the most efficient way to get things done, and many try to abide by the “don’t reinvent the wheel” mantra.

Regardless of whether you are a developer, this is sound advice. You don’t need to build everything from scratch. There’s a good chance that most of what you want to do has already been created by someone else.

So, your next step is to activate an existing theme.

<a name="choosing-a-theme-to-learn-from"></a>
#### [Choosing a theme to learn from](#choosing-a-theme-to-learn-from)

Packaged in every version of WordPress since version 3.0 (and named after the year they were released in), the default themes are some of the best to study how themes are built. This is because they are designed with broad use in mind and fully adhere to WordPress coding standards.

Because this handbook primarily focuses on modern, block theming, you should choose one of the newest default themes:

- [Twenty Twenty-Four](https://wordpress.org/themes/twentytwentyfour/)
- [Twenty Twenty-Three](https://wordpress.org/themes/twentytwentythree/)
- [Twenty Twenty-Two](https://wordpress.org/themes/twentytwentytwo/)

It’s typically best to use the latest default theme. This is because it will be built with the most up-to-date features in mind. Plus, it should already be activated if you’ve recently installed WordPress:

[![WordPress Appearance > Theme admin screen, showing the Twenty Twenty-Four theme activated.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-activated.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-activated.jpg?ssl=1)

You can also choose any theme from the official [Theme Directory](https://wordpress.org/themes/) to learn from, but for the purposes of this guide, it should be a [block theme](https://wordpress.org/themes/tags/full-site-editing/). For more information on installing and activating themes, read the [Work with themes](https://wordpress.org/documentation/article/work-with-themes/) documentation.

If your interests lie in classic WordPress, you should jump forward to the [Classic Themes](https://developer.wordpress.org/themes/classic-themes/) chapter for more details on building classic themes.

<a name="customizing-your-theme"></a>
### [Customizing your theme](#customizing-your-theme)

Once you’ve activated a block theme, take some time to simply have fun exploring and tinkering with the available options in the [Site Editor](https://wordpress.org/documentation/article/site-editor/). Essentially, this is an editable, visual representation of your theme in the WordPress admin.

And, as promised earlier in the Getting Started chapter, you can build your theme entirely from this interface without touching a single line of code.

You can locate the Site Editor via **Appearance > Editor** in the WordPress admin menu. Once opened, your screen should look similar to this:

[![WordPress Site Editor with the Design menu shown in the left panel. In the preview panel is the homepage of the Twenty Twenty-Four theme.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-editor.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-editor.jpg?ssl=1)

There are a lot of pieces to this, and you can find yourself lost for hours just tinkering around in the Site Editor. It can be fun, and you’ll learn more about how this integrates with your theme as you read through this handbook. For now, let’s get to the basics of “creating” a theme.

This part of the journey can be entirely self-directed, so feel free to do this at your own pace and in your own way. But most people will want to begin by adjusting their design.

You can do this by first selecting the **Styles** item in the menu panel:

[![WordPress Styles screen under the Site Editor in the admin. The left panel shows several style variation options.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-styles.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-styles.jpg?ssl=1)

The Twenty Twenty-Four theme (and many other block themes) include pre-designed style variations, which you can see in the sidebar in the above screenshot. You will learn more about these variations in the [Global Settings and Styles](https://developer.wordpress.org/themes/global-settings-and-styles/) chapter, but feel free to use one as a starting point for your own customizations.

The next step is to select the **Style Book** icon (it looks like an eye). Opening this screen will give you full access to modifying the global styles of the site:

[![Style Book screen under the WordPress Site Editor in the admin. It shows a tabbed overlay with various blocks.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-style-book.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-style-book.jpg?ssl=1)

At this point, *the world is your oyster*—in other words, feel free to let your creativity run wild. But most importantly, get a feel for what settings and styles are available in the interface. This familiarity will come in hand as you dive into more advanced sections of the handbook.

For a deeper dive into using the Style Book, read this guide from the WordPress Developer Blog: [The Style Book: a one-stop shop for styling block themes](https://developer.wordpress.org/news/2023/06/the-style-book-a-one-stop-shop-for-styling-block-themes/).

<a name="exporting-your-theme"></a>
### [Exporting your theme](#exporting-your-theme)

Once you’ve customized the theme to your liking, be sure to hit the **Save** button. When you’re ready, you will “create” your first theme.

You have two options for doing this. The first is to use the built-in exporter from the Site Editor in WordPress. The second is to use the [Create Block Theme](https://wordpress.org/plugins/create-block-theme/) plugin, which has more extensive options available. There are instructions for both methods below.

<a name="exporting-from-the-styles-interface"></a>
#### [Exporting from the Styles interface](#exporting-from-the-styles-interface)

To export your theme from the Site Editor interface, click the **⋮ (Options)** button in the header area. You will see a dropdown of available options. Click the **Export** option, as shown below:

[![WordPress Site Editor with the Options menu dropdown open. The Export option is highlighted.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-export.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-export.jpg?ssl=1)

This will give you a ZIP file with your complete theme in it. The filename will match that of the theme you were working from. In the case of the default Twenty Twenty-Four theme, it will be `twentytwentyfour.zip`.

***Congratulations!*** You have now successfully created your first WordPress theme.

You were assured that you could create a theme without touching code. That was the truth. You have built a theme that can be uploaded to any WordPress website just like any other theme.

But there was a *fib*—a harmless white lie—mixed in with that truth about there being no code involved.

The theme you downloaded is still named “Twenty Twenty-Four,” and it’s best to rename it so that it’s representative of what you’ve created. To do this, unzip the `twentytwentyfour.zip` folder and rename it to `your-theme-name`.

Then, open the `style.css` file within that folder. You should see something like this at the top of the file:

```auto
/*
Theme Name: Twenty Twenty-Four
Theme URI: https://wordpress.org/themes/twentytwentyfour/
Author: the WordPress team
Author URI: https://wordpress.org
...
```

At the very least, you should adjust those first four lines, particularly the `Theme Name` value. And that’s all the code you *really* have to touch.

As a final step, zip the file again with whatever utility program you have on your computer for creating ZIP files.

#### [Using the Create Block Theme plugin](#using-the-create-block-theme-plugin)

The [Create Block Theme](https://wordpress.org/plugins/create-block-theme/) plugin is an official, first-party plugin that WordPress contributors maintain. Often, you will see new ideas for exporting themes tried and tested here before they land in WordPress.

The plugin is more robust than what you will find in core WordPress, meaning that it has many more options for exporting your theme. This guide will only cover the basics of exporting your theme, but feel free to explore the plugin’s features in more detail.

Once you’ve activated Create Block Theme, you should see a new button in the Site Editor that is displayed as a wrench icon. Click this button to open the **Create Block Theme** menu.

You will see several options for saving changes, exporting a ZIP, editing theme info, and creating a new theme:

[![WordPress Site Editor with a "tool" icon in the top right. A menu is open titled "Create Block Theme" and has several options.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-create-block-theme-menu.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-create-block-theme-menu.jpg?ssl=1)

You can use the **Export ZIP** option to export the theme as you did earlier.

But Create Block Theme offers more customization options that you’ll want to use for truly creating a custom theme. Click on the **Create Theme** option:

[![WordPress Site Editor with the Create Block Theme > Create Theme menu open. Several fields are shown within the menu panel.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-create-block-theme-customize.jpg?resize=2048%2C1064&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt4-create-block-theme-customize.jpg?ssl=1)

From there, you’ll be able to customize all of the information about your theme to make it unique. Once finished, click the **Export Theme** button for your new theme.

The one thing that Create Block Theme does not yet do is let you upload a custom screenshot. You’ll still need to add a unique `screenshot.[png|jpg]` file in your theme if you intend to distribute to others.

First published

November 21, 2023

Last updated

January 22, 2024

[Previous
Tools and Setup
Previous: Tools and Setup](https://developer.wordpress.org/themes/getting-started/tools-and-setup/)

[Next
Core Concepts
Next: Core Concepts](https://developer.wordpress.org/themes/core-concepts/)

---

## Core Concepts

[↑ Back to top](#wp--skip-link--target)

Welcome to the Core Concepts documentation. The goal of this chapter is to introduce you to the foundational concepts necessary for creating your own WordPress block themes.

The focus of this chapter is to help you familiarize yourself with the basic theme structure and standard files like `style.css`, `functions.php`, and `theme.json`. Once you have these core concepts down, you can more comfortably dive into the later chapters in this handbook.

### Navigating this chapter

Use the following links to locate a topic within this chapter. Each article is listed in the recommended reading order for those new to theme development. For those with existing experience creating themes, feel free to jump to the section you need:

- [**Theme Structure**](https://developer.wordpress.org/themes/core-concepts/theme-structure/)**:** Walks through how a theme’s files and folders are structured following WordPress standards.
- [**Main Stylesheet**](https://developer.wordpress.org/themes/core-concepts/main-stylesheet/)**:** Explains the importance of the theme’s `style.css` file and how to use it.
- [**Custom Functionality**](https://developer.wordpress.org/themes/core-concepts/custom-functionality/)**:** Dives into the theme’s functions file (`functions.php`) and how you can use it to add your own functionality to a theme.
- [**Templates**](https://developer.wordpress.org/themes/core-concepts/templates/)**:** Introduces how WordPress’ block templates system works and provides pathways for deeper learning.
- [**Including Assets**](https://developer.wordpress.org/themes/core-concepts/including-assets/)**:** A guide on including CSS, JavaScript, images, and more in your themes.
- [**Global Settings and Styles**](https://developer.wordpress.org/themes/core-concepts/global-settings-and-styles/)**:** Gives a basic overview of how the `theme.json` file works in themes with learning pathways to more detailed articles.

First published

November 3, 2023

Last updated

December 14, 2023

[Previous
Quick-Start Guide
Previous: Quick-Start Guide](https://developer.wordpress.org/themes/getting-started/quick-start-guide/)

[Next
Theme Structure
Next: Theme Structure](https://developer.wordpress.org/themes/core-concepts/theme-structure/)

---

## Main Stylesheet (style.css)

### In this article

Table of Contents

- [File Header](#file-header)
  - [Header fields](#header-fields)
  - [Child theme header fields](#child-theme-header-fields)
  - [Custom header fields](#custom-header-fields)
- [Custom CSS](#custom-css)

[↑ Back to top](#wp--skip-link--target)

As described in [Theme Structure](https://developer.wordpress.org/themes/core-concepts/theme-structure/), WordPress requires that all themes include a `style.css` file. Its most important function is to “register” the theme with WordPress through configuration data at the top of the file. Many themes also use it to serve CSS to the front-end (and even the editor).

In this document, you will learn how to configure your theme data via the `style.css` file header.

### [File Header](#file-header)

The `style.css` file header is used to configure data about the theme. WordPress uses this information to determine how some features work and displays some of this data under the **Appearance > Themes** screen for users.

Here is a look at what the theme details overlay looks like for the default Twenty Twenty-Three theme:

[![WordPress themes screen with the Twenty Twenty-Three modal overlay over the screen. It shows the theme screenshot, description, and metadata.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-theme-details.jpg?resize=2048%2C1002&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-theme-details.jpg?ssl=1)

Most of that information is pulled directly from the `style.css` file header. It is one of the most vital parts of creating a WordPress theme.

When determining which themes are available to activate, WordPress searches through each folder under `/wp-content/themes`, looking for a `style.css` file. If one is found, it pulls the first 8kb of data from the file and determines if there is a file header with standard fields defined.

In themes, this is merely a CSS comment block with some standard keys and values defined.

Suppose you were creating a theme with the folder name of `fabled-sunset`. WordPress would look for your theme’s `style.css` in the following location:

- `wp-content/`
  - `themes/`
    - `fabled-sunset/`
      - `style.css`

For WordPress to recognize your theme, you would at least need the `Theme Name` field defined at the top of `style.css` like so:

```auto
/**
 * Theme Name: Fabled Sunset
 */
```

This is the minimum required header field for a valid theme. Of course, you’ll want to add much more information about your theme.

<a name="header-fields"></a>
#### [Header fields](#header-fields)

There are many supported fields, and you will likely use most of them in your themes. Here is a quick look at a theme’s `style.css` file header with each of the fields configured:

```auto
/**
 * Theme Name:        Fabled Sunset
 * Theme URI:         https://example.com/fabled-sunset
 * Description:       Custom theme description...
 * Version:           1.0.0
 * Author:            Your Name
 * Author URI:        https://example.com
 * Tags:              block-patterns, full-site-editing
 * Text Domain:       fabled-sunset
 * Domain Path:       /assets/lang
 * Tested up to:      6.4
 * Requires at least: 6.2
 * Requires PHP:      7.4
 * License:           GNU General Public License v2.0 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 */
```

The following list outlines what each of these fields does.

While the `Theme Name` is the only field required to work with WordPress, you must also include some other fields when submitting a theme to the WordPress theme directory. These fields are marked with **\*** below.

- **Theme Name\*:** A unique name for your theme.
- **Theme URI:** The URL of a public web page where users can find more information about the theme.
- **Description\*:** A description of the theme, which will be displayed when viewing a theme’s details in the WordPress admin and other places. It is also used for themes submitted to the WordPress theme directory.
- **Version\*:** The version of the theme, written in `X.X` or `X.X.X` format.
- **Author\*:**  Your name or the name of the organization who developed the theme. For themes submitted to the theme directory, it is recommended to use the WordPress.org username.
- **Author URI:** The URL of the individual or organization who created the theme.
- **Tags:** A comma-separated list of features the theme supports. The Theme Review Handbook has a [list of valid tags](https://make.wordpress.org/themes/handbook/review/required/theme-tags/) for submission to the theme directory, but third-party sites may use a different system.
- **Text Domain\*:** The string used for the textdomain for translations.
- **Domain Path:** A relative path to where theme translations are stored. WordPress uses this field when the theme is disabled to detect translations. Defaults to `/languages`.
- **Tested up to\*:** The last WordPress version the theme has been tested up to, written in `X.X` format (e.g., `6.`4, `6.2.1`, etc.).
- **Requires at least\*:** The oldest WordPress version the theme will work with, written in `X.X` format (e.g., `6.3`, `6.2.1`, etc.).
- **Requires PHP\*:** The oldest PHP version the theme will work with, written in `X.X` format (e.g., `8.0`, `7.4`, etc.).
- **License\*:** The license for the theme.
- **License URI\*:** The URL of the theme’s license.

#### [Child theme header fields](#child-theme-header-fields)

When building a child theme, there is one additional supported field: **Template**. This is used to designate the parent theme’s folder.

If the fictional “Fabled Sunset” theme listed above was the parent of your child theme named “Grand Sunrise,” your `style.css` header fields would look similar to this:

```auto
/**
 * Theme Name: Grand Sunrise
 * Template:   fabled-sunset
 * ...other header fields
 */
```

The `Template` field must match the parent theme’s folder name exactly (relative to the `wp-content/themes` directory) for this to work. Otherwise, WordPress will not be able to appropriately match them.

You can [learn more about child themes](https://developer.wordpress.org/themes/advanced-topics/child-themes/) in the Advanced Topics chapter.

<a name="custom-header-fields"></a>
#### [Custom header fields](#custom-header-fields)

Some third-party marketplaces or systems may also make use of custom header fields. These are not officially supported by WordPress, but they are definitely allowed and should not negatively impact how the theme works within WordPress.

<a name="custom-css"></a>
### [Custom CSS](#custom-css)

The `style.css` file is not merely a configuration file. You can also use it to write custom CSS code to alter the design of your theme, assuming the file is properly loaded.

With block themes, most or all of the design is ideally handled through the `theme.json` file, which you will learn about in the [Global Settings and Styles](https://developer.wordpress.org/themes/core-concepts/global-settings-and-styles/) documentation.

But there are times when you will want or need to add custom CSS. You can learn more about this in the [Including Assets](https://developer.wordpress.org/themes/core-concepts/including-assets/) documentation.

First published

November 21, 2023

Last updated

December 14, 2023

[Previous
Theme Structure
Previous: Theme Structure](https://developer.wordpress.org/themes/core-concepts/theme-structure/)

[Next
Templates
Next: Templates](https://developer.wordpress.org/themes/core-concepts/templates/)

---

<a name="templates"></a>
## Templates

<a name="in-this-article-5"></a>
### In this article

Table of Contents

- [What are templates?](#what-are-templates)
- [How the templating system works](#how-the-templating-system-works)
  - [Template files](#template-files)
- [Template parts](#template-parts)

[↑ Back to top](#wp--skip-link--target)

In block themes, templates are made up of a collection of blocks. You might have a Site Logo block sitting next to a Navigation block in the header area. You might put Social Icons in the footer above a copyright notice.

As you build out your own themes, you will get to decide how your templates come together. *That’s at least half the fun of theming!*

In this document, you will learn the basic terminology around templating in WordPress. Reading through this quick primer on the subject will provide you with some foundational knowledge moving forward. There is a dedicated [Templates](https://developer.wordpress.org/themes/templates/) chapter that provides a full overview of working with templates.

<a name="what-are-templates"></a>
### [What are templates?](#what-are-templates)

Theme templates represent the markup of the webpage. They create the document structure and print both static data (e.g., paragraph text) and dynamic data (e.g., post content) to the front end of your site.

Let’s take a look at a template from the default Twenty Twenty-Three theme.

Go to **Appearance > Editor > Templates > Single Posts** in your WordPress admin. This will show you what a Single post template looks like:

[![WordPress Site Editor with a focus on the Single Post template.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-single-template-editor.jpg?resize=2048%2C1066&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-single-template-editor.jpg?ssl=1)

Single post template of the default Twenty Twenty-Three theme.

As shown above, the template is made up of various blocks. Some of them are in placeholder states and will dynamically display content based on what page is being viewed on the front end of the site.

If you select the **⋮ (Options)** button in the template editor and select the **Code editor** option, you will see the block markup of the template:

[![WordPress site editor showing the Single Post template in code view, which shows the block markup.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-single-template-code.jpg?resize=2048%2C1066&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-single-template-code.jpg?ssl=1)

Code view of the default Twenty Twenty-Three theme’s single post template.

One of the great things about templating in WordPress is that you never really have to interact directly with template code. You have the visual Site Editor to make any and all customizations you want. But the code is there if you need it.

Ultimately, the template produces HTML markup on the front end like this (shortened for clarity):

```auto
<!DOCTYPE html>
<html lang="en-US">
<head>
	<title>Post Title</title>
	<!-- Scripts, styles, and meta here. -->
</head>

<body class="post-template single single-post">
	<div class="wp-site-blocks">
		<header class="wp-block-template-part">
			<!-- Header blocks here. -->
		</header>
		<main class="wp-block-group is-layout-flow wp-block-group-is-layout-flow">
			<!-- Nested blocks here. -->
		</main>
		<footer class="wp-block-template-part">
			<!-- Footer blocks here. -->
		</footer>
	</div>
</body>
</html>
```

WordPress automatically handles the final markup for you, so all you need to do is create the templates.

### [How the templating system works](#how-the-templating-system-works)

Whenever you visit a page on the front end of your website, WordPress must determine which template file to load. In the example above, the Single post template (`single.html`) is used to display the content of single blog posts.

But there are many other types of templates. For example, you might have a Page template (`page.html`) for displaying the content of your site’s pages or an Author template (`author.html`) for displaying post author archives.

WordPress uses the template hierarchy to determine which template file to load. It is essentially a set of rules that defines which template to use based on the web page being viewed. If a template doesn’t exist, WordPress will continue looking down through the hierarchy until it finds one that does.

If no specific template is found, it will fall back to the Index template: `index.html`. As you learned in [Theme Structure](https://developer.wordpress.org/themes/core-concepts/theme-structure/), this is the minimum required template for a block theme to function.

The [Templates](https://developer.wordpress.org/themes/templates/) chapter covers the hierarchy in full detail. There, you will learn which templates are loaded for each page of a WordPress site.

#### [Template files](#template-files)

WordPress expects template files to be located under the `/templates` folder in your theme. A typical theme will have several templates, which would be organized like this:

- `templates/`
  - `404.html`
  - `archive.html`
  - `author.html`
  - `index.html` (required)
  - `page.html`
  - `single.html`
  - `search.html`

These are some of the common templates you will find a theme:

- **`index.html`:** The fallback template file. It is required in all themes.
- **`404.html`:** The 404 template is used when WordPress cannot find a post, page, or other content that matches the visitor’s request.
- **`archive.html`:** The archive template is used when visitors request posts by archive-type views like category, author, or date and a more-specific template is unavailable.
- **`author.html`:** The author page template is used whenever a visitor loads an author archive.
- **`category.html`:** The category template is used when visitors request posts by category.
- **`page.html`:** The page template is used when visitors request individual pages.
- **`search.html`:** The search results template is used to display a visitor’s search results.
- **`single.html`:**  The single post template is used when a visitor requests a single post.
- **`tag.html`:** The tag template is used when visitors request posts by tag.

This is not an exhaustive list. You will learn the ins and outs of every template file as you dive deeper into the [Templates](https://developer.wordpress.org/themes/templates/) chapter. The goal for now is to give you a baseline understanding of what to expect.

### [Template parts](#template-parts)

Template parts, or “parts” for short, are another integral part of the templating system in WordPress. As the name suggests, template parts are a “part” of a template.

A template may consist of none, one, or more parts.

The great thing about parts is they help you follow the DRY (Don’t Repeat Yourself) principle. By including parts in your templates, you avoid having to repeat building the same block code over and over.

On most websites, there are sections of the page that typically stay the same, regardless of the page that you are viewing. *Can you think of any repeated sections that are common on websites?*

The site header and footer are likely the most recognizable “parts” of a webpage, and they just so happen to be the most common template parts you’ll find in themes. While it’s not required to include them, they are *de facto* standards.

Go to **Appearance > Editor > Patterns > Template Parts** in your WordPress admin. Here is what the Header template part looks like from the default Twenty Twenty-Three theme:

[![WordPress Patterns library showing Header Template parts.](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-template-parts.jpg?resize=2048%2C1066&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/tt3-template-parts.jpg?ssl=1)

Headers for the Twenty Twenty-Three theme.

WordPress looks for template parts in your theme’s `/parts` folder, which should be organized like this:

- `parts/`
  - `header.html`
  - `footer.html`

Other common template parts are for the comments area and sidebars, but your theme can have as few or as many parts as you want.

You’ll learn more about how to register and create custom parts in the [Template Parts](https://developer.wordpress.org/themes/templates/template-parts/) documentation.

First published

November 21, 2023

Last updated

December 14, 2023

[Previous
Main Stylesheet (style.css)
Previous: Main Stylesheet (style.css)](https://developer.wordpress.org/themes/core-concepts/main-stylesheet/)

[Next
Custom Functionality (functions.php)
Next: Custom Functionality (functions.php)](https://developer.wordpress.org/themes/core-concepts/custom-functionality/)

---

## Including Assets

### In this article

Table of Contents

- [URL and directory path functions](#url-and-directory-path-functions)
- [Including CSS](#including-css)
  - [Front-end stylesheets](#front-end-stylesheets)
  - [Inline styles](#inline-styles)
  - [Editor stylesheets](#editor-stylesheets)
  - [Block stylesheets](#block-stylesheets)
- [Including JavaScript](#including-javascript)
  - [Front-end JavaScript](#front-end-javascript)
  - [Inline JavaScript](#inline-javascript)
  - [Editor JavaScript](#editor-javascript)
  - [Default WordPress scripts](#default-wordpress-scripts)
- [Including images](#including-images)
- [Including fonts](#including-fonts)

[↑ Back to top](#wp--skip-link--target)

Many block themes do not need to load any assets. For design aspects, specifically, much of this can be handled through the [Global Settings and Styles](https://developer.wordpress.org/themes/global-settings-and-styles/) system. But there are times when you might need to include a CSS stylesheet, custom JavaScript file, or even other types of media.

If you are familiar with HTML, you might be accustomed to including CSS stylesheets via the `<link rel=”stylesheet”/>` or `<style>` tags. The same might be true for including JavaScript via the `<script>` tag. But you should never manually hard code these HTML elements in your theme.

WordPress has specific hooks for determining when to load scripts/styles and functions for generating the markup. This ensures that WordPress, any active plugins, and your theme all play nicely together.

In this document, you will learn the necessary functions for generating the proper URL to point to asset files and how to include scripts, styles, and other assets in your theme.

This documentation is a leap forward in comparison to some of the previous pages in the Core Concepts chapter. You will need some baseline PHP and HTML knowledge to follow along. You must also understand how to use your [theme’s `functions.php` file](https://developer.wordpress.org/themes/core-concepts/custom-functionality/). This is necessary for loading CSS stylesheet and JavaScript files.

### [URL and directory path functions](#url-and-directory-path-functions)

Before including assets, you should become familiar with some of the utility functions that WordPress provides for getting URLs and directory paths within a theme. You should always use these helper functions when including any type of asset to ensure the URL or path is correct.

Three of the primary URL helper functions are:

- [`get_stylesheet_uri()`](https://developer.wordpress.org/reference/functions/get_stylesheet_uri/): Returns the active theme’s `style.css` file URL.
- [`get_theme_file_uri( $file )`](https://developer.wordpress.org/reference/functions/get_theme_file_uri/): Returns the active theme’s URL, with an optional `$file` parameter. Falls back to the parent theme if a child theme is active and the file doesn’t exist.
- [`get_parent_theme_file_uri( $file )`](https://developer.wordpress.org/reference/functions/get_parent_theme_file_uri/): Returns the parent theme’s URL, with an optional `$file` path.

For directory paths, which are needed less often for assets, there are two primary functions:

- [`get_theme_file_path( $file )`](https://developer.wordpress.org/reference/functions/get_theme_file_path/): Returns the active theme’s directory path, with an optional `$file` parameter. Falls back to the parent theme if a child theme is active and the file doesn’t exist.
- [`get_parent_theme_file_path( $file )`](https://developer.wordpress.org/reference/functions/get_parent_theme_file_path/): Returns the parent theme’s directory path, with an optional `$file` parameter.

### [Including CSS](#including-css)

[`wp_enqueue_style()`](https://developer.wordpress.org/reference/functions/wp_enqueue_style/) is the primary function for enqueueing a stylesheet, which tells WordPress that you want to put it in the queue to load. You would use this function within an action hook callback in your `functions.php` file, which you learned about in [Custom Functionality](https://developer.wordpress.org/themes/core-concepts/custom-functionality/). You’ll learn which action hooks to use for specific scenarios in the next sections.

Take a look at the function signature:

```auto
wp_enqueue_style( 
	string $handle, 
	string $src           = '', 
	string[] $deps        = array(), 
	string|bool|null $ver = false, 
	string $media         = 'all'
);
```

You can use these parameters:

- **`$handle`** is a unique name/ID for the stylesheet and should be prefixed with your theme slug.
- **`$src`** is the file URL of your stylesheet. While it is technically an optional parameter, it is required to actually load a specific stylesheet.
- **`$deps`** is an optional array of other stylesheet handles that your stylesheet is dependent upon.
- **`$ver`** sets the version number of your stylesheet and is used for cache busting. Defaults to the current WordPress version.
- **`$media`** is for specifying which type of media to load this stylesheet for, such as `all` (default), `screen`, `print`, or `handheld`.

If you were enqueuing a stylesheet located at `/assets/css/example.css` in your theme, your function call might look like this:

```auto
wp_enqueue_style( 
	'theme-slug-example',
	get_parent_theme_file_uri( 'assets/css/example.css' ),
	array(),
	wp_get_theme()->get( 'Version' ),
	'all'
);
```

The above code uses [`wp_get_theme()`](https://developer.wordpress.org/reference/functions/wp_get_theme/) to grab the theme’s version number for cache busting, but you can leave it at the default or use something custom altogether.

#### [Front-end stylesheets](#front-end-stylesheets)

When loading stylesheets on the front end of a website, you will use the [`wp_enqueue_scripts`](https://developer.wordpress.org/reference/hooks/wp_enqueue_scripts/) hook for most scenarios.

Let’s assume that you wanted to load your theme’s `style.css` file using the `get_stylesheet_uri()` function. You would do this by adding the following code to your `functions.php` file:

```auto
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_styles' );

function theme_slug_enqueue_styles() {
	wp_enqueue_style( 
		'theme-slug-style', 
		get_stylesheet_uri()
	);
}
```

Remember that you can also pass other parameters to the `wp_enqueue_style()` function if needed. The above code is the minimum needed to load the stylesheet.

Let’s further suppose that you wanted to load a second stylesheet located at `/assets/css/primary.css` in your theme. For this, you would use the `get_parent_theme_file_uri()` function to get the correct URL.

Here is what your code would look like with both stylesheets enqueued:

```auto
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_styles' );

function theme_slug_enqueue_styles() {
	wp_enqueue_style(
		'theme-slug-style', 
		get_stylesheet_uri()
	);

	wp_enqueue_style( 
		'theme-slug-primary',
		get_parent_theme_file_uri( 'assets/css/primary.css' )
	);
}
```

#### [Inline styles](#inline-styles)

There are times when you might need to add some inline CSS to the `<head>` area on the front end. WordPress has the [`wp_add_inline_style()`](https://developer.wordpress.org/reference/functions/wp_add_inline_style/) function for this specific scenario.

Here is a look at the function signature:

```auto
wp_add_inline_style( 
	string $handle, 
	string $data 
);
```

In this case, you must pass in a `$handle` parameter that matches a handle of an existing stylesheet that is enqueued for the page. The `$data` parameter is your custom CSS code.

Let’s extend the code from the previous section by adding a small bit of CSS that sets the body background color to a light gray:

```auto
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_styles' );

function theme_slug_enqueue_styles() {
	wp_enqueue_style(
		'theme-slug-style', 
		get_stylesheet_uri()
	);

	wp_enqueue_style( 
		'theme-slug-primary',
		get_parent_theme_file_uri( 'assets/css/primary.css' )
	);

	wp_add_inline_style( 
		'theme-slug-primary', 
		'body { background: #eee; }'
	);
}
```

In the `wp_add_inline_style()` function call, the code uses the existing `theme-slug-primary` handle to attach an inline style.

#### [Editor stylesheets](#editor-stylesheets)

When creating a theme with custom CSS on the front end, you will almost always want your custom styles to also appear in the editor. This will create a consistent user experience across the site. But WordPress does not automatically load your front-end stylesheets in the editor.

For that, you will need to use the [`add_editor_style()`](https://developer.wordpress.org/reference/functions/add_editor_style/) function:

```auto
add_editor_style( array|string $stylesheet = 'editor-style.css' );
```

It accepts a single parameter of `$stylesheet`, which can be a single stylesheet filename or an array of filenames. These can be relative to the theme folder or a full URL.

Note that when using relative URLs, a file in the child theme with the same filename will take priority. That’s why it’s generally best practice to use the full stylesheet URL.

This code snippet shows how to add the active theme’s main `style.css` file as an editor style:

```auto
add_action( 'after_setup_theme', 'theme_slug_setup' );

function theme_slug_setup() {
	add_editor_style( get_stylesheet_uri() );
}
```

If you wanted to add both the `style.css` file and `primary.css` from the earlier examples, you could pass them in as an array:

```auto
add_action( 'after_setup_theme', 'theme_slug_setup' );

function theme_slug_setup() {
	add_editor_style( array(
		get_stylesheet_uri(),
		get_parent_theme_file_uri( 'assets/css/primary.css' )
	) );
}
```

<a name="block-stylesheets"></a>
#### [Block stylesheets](#block-stylesheets)

WordPress also includes a [`wp_enqueue_block_style()`](https://developer.wordpress.org/reference/functions/wp_enqueue_block_style/) function for loading per-block stylesheets in the editor and on the front end. This is covered in full detail in the [Block Stylesheets](https://developer.wordpress.org/themes/features/block-stylesheets/) documentation.

For an advanced exploration of block stylesheets, read [Leveraging theme.json and per-block styles for more performant themes](https://developer.wordpress.org/news/2022/12/leveraging-theme-json-and-per-block-styles-for-more-performant-themes/) on the WordPress Developer Blog.

<a name="including-javascript"></a>
### [Including JavaScript](#including-javascript)

Like stylesheets, WordPress has a primary function for enqueueing JavaScript files: [`wp_enqueue_script()`](https://developer.wordpress.org/reference/functions/wp_enqueue_script/). You would also use this function within an action hook callback in your `functions.php` file, and you’ll learn which hooks to use in the following sections.

Take a look at the function signature:

```auto
wp_enqueue_script( 
	string $handle, 
	string $src           = '', 
	string[] $deps        = array(), 
	string|bool|null $ver = false, 
	array|bool $in_footer = false
);
```

You can use these parameters:

- **`$handle`:** A unique name/ID for the script and should be prefixed with your theme slug.
- **`$src`:** The file URL of your script. While it is technically an optional parameter, it is required to actually load a specific script
- **`$deps`:** An optional array of other script handles that your script is dependent upon.
- **`$ver`:** Sets the version number of your script and is used for cache busting. Defaults to the current WordPress version.
- **`$in_footer`:** Determines whether to load the script in the header or footer. As of WordPress 6.3, this parameter accepts an array of values:
  - **`strategy`:** Accepts either `'defer'` (default) or `'async'` to set the script-loading strategy.
  - **`in_footer`:** A boolean value to determine whether to load the script in the header or footer.

If you were enqueuing a script located at `/assets/js/example.js` in your theme, your function call might look like this:

```auto
wp_enqueue_script( 
	'theme-slug-example',
	get_parent_theme_file_uri( 'assets/js/example.js' ),
	array(),
	wp_get_theme()->get( 'Version' ),
	true
);
```

<a name="front-end-javascript"></a>
#### [Front-end JavaScript](#front-end-javascript)

When loading stylesheets on the front end of a website, you will use the [`wp_enqueue_scripts`](https://developer.wordpress.org/reference/hooks/wp_enqueue_scripts/) hook for most scenarios.

Suppose you had a custom navigation script located at `assets/js/navigations.js` in your theme. For this, you would use the `get_parent_theme_file_uri()` function to get the correct URL.

Here is what your function would look like when enqueueing the script:

```auto
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_scripts' );

function theme_slug_enqueue_scripts() {
	wp_enqueue_script( 
		'theme-slug-navigation',
		get_parent_theme_file_uri( 'assets/js/navigation.js' ),
		array(),
		wp_get_theme()->get( 'Version' ),
		true
	);
}
```

#### [Inline JavaScript](#inline-javascript)

Sometimes you might want to add some inline JavaScript to the `<head>` area on the front end. WordPress has the [`wp_add_inline_script()`](https://developer.wordpress.org/reference/functions/wp_add_inline_script/) function for this purpose.

Take a look at the function signature:

```auto
wp_add_inline_script( 
	string $handle, 
	string $data, 
	string $position = 'after' 
);
```

Like its counterpart for styles, you must attach this to an enqueued script via the `$handle` parameter. The secondary parameter, `$data`, should be the JavaScript code itself. The difference here is the addition of a third parameter, `$position`, which lets you position the inline script before or after the script that it is attached to.

The following code builds on top of the navigation script from the previous section by adding an inline script to it:

```auto
add_action( 'wp_enqueue_scripts', 'theme_slug_enqueue_scripts' );

function theme_slug_enqueue_scripts() {
	wp_enqueue_script( 
		'theme-slug-navigation',
		get_parent_theme_file_uri( 'assets/js/navigation.js' ),
		array(),
		wp_get_theme()->get( 'Version' ),
		true
	);

	wp_add_inline_script( 
		'theme-slug-navigation', 
		'console.log( "Testing" );'
	);
}
```

In the `wp_add_inline_script()` function call, the code uses the existing `theme-slug-navigation` handle to attach the inline style.

#### [Editor JavaScript](#editor-javascript)

When you need to load a JavaScript file for the block editor, you must use the [`enqueue_block_editor_assets`](https://developer.wordpress.org/reference/hooks/enqueue_block_editor_assets/) hook. Note that this is for loading scripts on the admin page itself and not within the content iframe.

Suppose you had an `assets/js/editor.js` file that you needed to load for the editor. Your code should look like this:

```auto
add_action( 'enqueue_block_editor_assets', 'theme_slug_enqueue_editor_scripts' );

function theme_slug_enqueue_editor_scripts() {
	wp_enqueue_script( 
		'theme-slug-editor',
		get_parent_theme_file_uri( 'assets/js/editor.js' ),
		array(),
		wp_get_theme()->get( 'Version' ),
		true
	);
}
```

Generally, themes wouldn’t need to load JavaScript for the editor itself. But for advanced use cases, it may be necessary. It is also recommended to integrate with the [`@wordpress/scripts`](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-scripts/) package for easier management. For more information on how to do this, read [Beyond block styles, part 1: using the WordPress scripts package with themes](https://developer.wordpress.org/news/2023/07/beyond-block-styles-part-1-using-the-wordpress-scripts-package-with-themes/).

<a name="default-wordpress-scripts"></a>
#### [Default WordPress scripts](#default-wordpress-scripts)

WordPress bundles many custom and third-party scripts. You should always use these scripts if you need one of them instead of loading a custom version. This ensures that you avoid conflicts with plugins.

Some of the scripts are referenced in the [`wp_enqueue_script()` documentation](https://developer.wordpress.org/reference/functions/wp_enqueue_script/), but that list may not always be up to date. You can find the full list of included files in [wp-includes/script-loader.php](https://core.trac.wordpress.org/browser/trunk/src/wp-includes/script-loader.php).

<a name="including-images"></a>
### [Including images](#including-images)

Block themes will not often need to include images, except in patterns. You will learn more about these in the [Block Patterns](https://developer.wordpress.org/themes/features/block-patterns/) documentation. But for a quick overview, let’s take a look at how to reference an image in your theme.

Assuming you had an image file located at `assets/img/example.webp`, you would use this code to reference the correct URL:

```auto
<img src="<?php echo esc_url( get_parent_theme_file_uri( 'assets/img/example.webp' ) ); ?>" alt="" />
```

Note that the above example uses `get_parent_theme_file_uri()`. In most cases, this will be the correct function.

But if you are building a child theme or a theme where you would like to allow other child theme authors to override the image, you can use `get_theme_file_uri()` instead:

```auto
<img src="<?php echo esc_url( get_theme_file_uri( 'assets/img/example.webp' ) ); ?>" alt="" />
```

<a name="including-fonts"></a>
### [Including fonts](#including-fonts)

Typically, you would expect fonts to fall directly under the assets documentation. But WordPress has special methods for loading fonts via the `theme.json` file that integrates with the editor. This documentation is under the [Typography](https://developer.wordpress.org/themes/global-settings-and-styles/settings/typography/) page of the Global Settings and Styles chapter.

First published

November 21, 2023

Last updated

December 14, 2023

[Previous
Custom Functionality (functions.php)
Previous: Custom Functionality (functions.php)](https://developer.wordpress.org/themes/core-concepts/custom-functionality/)

[Next
Global Settings and Styles
Next: Global Settings and Styles](https://developer.wordpress.org/themes/core-concepts/global-settings-and-styles/)

---

<a name="global-settings-and-styles"></a>
## Global Settings and Styles

<a name="in-this-article-6"></a>
### In this article

Table of Contents

- [What is theme.json?](#what-is-theme-json)
- [theme.json structure](#theme-json-structure)
- [Settings and styles hierarchy](#settings-and-styles-hierarchy)

[↑ Back to top](#wp--skip-link--target)

As you learned in [Theme Structure](https://developer.wordpress.org/themes/core-concepts/theme-structure/), `theme.json` is a standard file that WordPress looks for in your theme. While it is not technically required for a block theme, it is almost always necessary to configure various settings and styles for your theme.

This documentation is a quick introduction on what `theme.json` is and how it works. However, it is such a massive topic that there is a dedicated chapter that explores everything you can do with it: [Global Settings and Styles](https://developer.wordpress.org/themes/global-settings-and-styles/).

<a name="what-is-themejson"></a>
### [What is theme.json?](#what-is-theme-json)

`theme.json` is a configuration file that tells WordPress what settings you want to enable, how to style specific elements and blocks, and which templates and template parts to register.

Some of the things you can do with `theme.json` are:

- Enable or disable features like drop caps, padding, margin, and line-height.
- Add a color palette, gradients, duotones, and shadows.
- Configure typographical features like font families, sizes, and more.
- Add CSS custom properties.
- Register custom templates and assign parts to template part areas.

Your `theme.json` configuration will be reflected in what you see in places like the post, template, and site editors in the WordPress admin. Custom styles, in particular, will be reflected in the **Styles** interface:

[![WordPress Site Editor viewing a Single Post template. On the right, the Buttons block is highlighted in the Styles interface.](https://i0.wp.com/developer.wordpress.org/files/2023/11/global-styles-site-editor.jpg?resize=2048%2C1066&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/11/global-styles-site-editor.jpg?ssl=1)

<a name="themejson-structure"></a>
### [theme.json structure](#theme-json-structure)

A `theme.json` file can be as little as a few lines of code, such as this example that enables the appearance tools for blocks:

```auto
{
	"$schema": "https://schemas.wp.org/trunk/theme.json",
	"version": 2,
	"settings": {
		"appearanceTools": true
	}
}
```

Or it can be a massively complex file that spans 1,000s of lines of code. How many of the features you want to configure is entirely up to you.

The starting point is understanding the top-level properties that can be configured. Here is an outline of what this looks like:

```auto
{
	"$schema": "https://schemas.wp.org/trunk/theme.json",
	"version": 2,
	"settings": {},
	"styles": {},
	"customTemplates": {},
	"templateParts": {},
	"patterns": []
}
```

Here are what each of these properties define:

- **`$schema`:** Used for defining the supported JSON schema, which will integrate with many code editors to give you on-the-fly hints and error reporting.
- **`version`:** The `theme.json` schema version you are building for. The latest version is 2 and can always be found in the [`theme.json` Living Reference](https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/theme-json-living/), a document that lists the most up-to-date properties you can set.
- **`settings`:** Used to define your block controls and color palettes, font sizes, and more.
- **`styles`:** Used to apply colors, font sizes, custom CSS, and more to the website and blocks.
- **`customTemplates`:** Metadata for custom templates defined in your theme’s `/templates` folder.
- **`templateParts`:** Metadata for template parts defined in your theme’s  `/parts` folder.
- **`patterns`:** An array of pattern slugs to be registered from the [Pattern Directory](https://wordpress.org/patterns/).

You will learn more about these properties and their sub-properties in the [Global Settings and Styles](https://developer.wordpress.org/themes/global-settings-and-styles/) chapter.

<a name="settings-and-styles-hierarchy"></a>
### [Settings and styles hierarchy](#settings-and-styles-hierarchy)

The `theme.json` file in your theme is only one level in a hierarchy of setting and style configurations for a website. This means it can be overridden under certain circumstances.

The order of this hierarchy from lowest to highest is:

- **WordPress `theme.json`:** WordPress has its own `theme.json` file that defines the default settings and styles.
- **Theme `theme.json`:** Anything you define in your theme’s `theme.json` file overrides the WordPress defaults.
- **Child theme `theme.json`:** If active, a child theme’s `theme.json` takes priority over the main or “parent” theme.
- **User configuration:** Users can further customize how their site works under **Appearance > Editor** in the WordPress admin, and the JSON data is saved in their site’s database. Their choice takes priority over all other levels in the hierarchy.

There are also filter hooks available that let plugin and theme authors override the values dynamically. To learn more about these, check out [How to modify theme.json data using server-side filters](https://developer.wordpress.org/news/2023/07/how-to-modify-theme-json-data-using-server-side-filters/) from the WordPress Developer Blog.

The important thing to remember is that anything configured in your `theme.json` file may not take priority in the hierarchy.

First published

November 21, 2023

Last updated

December 14, 2023

[Previous
Including Assets
Previous: Including Assets](https://developer.wordpress.org/themes/core-concepts/including-assets/)

[Next
Global Settings and Styles (theme.json)
Next: Global Settings and Styles (theme.json)](https://developer.wordpress.org/themes/global-settings-and-styles/)

---

<a name="starter-patterns"></a>
## Starter Patterns

<a name="in-this-article-7"></a>
### In this article

Table of Contents

- [Starter page patterns](#starter-page-patterns)
  - [How to create a page pattern](#how-to-create-a-page-pattern)
- [Starter template patterns](#starter-template-patterns)
  - [How to create template type patterns](#how-to-create-template-type-patterns)
  - [Supported template types](#supported-template-types)
  - [Using template patterns in templates](#using-template-patterns-in-templates)

[↑ Back to top](#wp--skip-link--target)

The WordPress block editor is powerful and can handle many different layouts and designs. However, when building a theme, you must remember that not all of your users will be skilled designers or even have much interest in piecing together their own layouts. This is where starter patterns can be beneficial to them.

WordPress supports two types of starter patterns for pages (or any post type) and templates. This feature lets you create starting points for your theme users to build out their pages and templates with minimal skills.

<a name="starter-page-patterns"></a>
### [Starter page patterns](#starter-page-patterns)

Page patterns let you create custom patterns your theme users can access when adding a new page via **Pages > Add New** in their WordPress admin. From there, a modal will pop up and show them a selection of patterns if any are registered.

Here is what the screen looks like when creating a new page with the default Twenty Twenty-Four theme installed:

[![Modal overlaying the edit page screen, showing a grid of various page layouts.](https://i0.wp.com/developer.wordpress.org/files/2024/04/starter-page-pattern-tt4.webp?resize=2048%2C1061&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2024/04/starter-page-pattern-tt4.webp?ssl=1)

This is a powerful feature because it means that you can provide well-designed starting points for your theme’s users or clients. And they don’t need to build from scratch. They only need to select a pattern, and it will automatically be inserted into the content area. From there, they can make any customizations they want.

<a name="how-to-create-a-page-pattern"></a>
#### [How to create a page pattern](#how-to-create-a-page-pattern)

Technically, any pattern in your theme can be converted to a page pattern. All you need to do is define the correct parameters to mark it as such. As described in [Registering Patterns](https://developer.wordpress.org/themes/patterns/registering-patterns/), there are two available file header fields that you must set to make this happen:

- **`Block Types`:** Adding `core/post-content` as one of the block types for the pattern tells WordPress that the pattern should be used for the post content.
- **`Post Types`:** You can add one or more post types (separated by commas) to connect the pattern.

With these two fields combined, you create a starter page pattern. Here is what the file header looks like for a fictional `/patterns/example-page.php` pattern file:

```auto
<?php
/**
 * Title: Example Page
 * Slug: themeslug/example-page
 * Categories: page
 * Block Types: core/post-content
 * Post Types: page
 * Viewport width: 1376
 */
?>
<!-- Block code here. -->
```

And that’s literally all you must do. Define the pattern’s `Block Types` and `Post Types` parameters and you have a starter page pattern.

This will work with any post type that has opted into the block editor, including both the default `post` and `page` post types.

Because page patterns are actually tied to the content, you wouldn’t typically include something like a site header or footer here. The pattern is output as post content.

### [Starter template patterns](#starter-template-patterns)

Like page patterns, template patterns give users a starting point when building a new template. The difference is that template patterns work from the Site Editor.

If you visit **Appearance > Editor > Templates** in your WordPress admin and click the **+** icon button for creating a new template, you should see a new **Add template** modal:

[![WordPress site editing screen with a modal popup asking the user to add a new template.](https://i0.wp.com/developer.wordpress.org/files/2024/04/add-template.webp?resize=2048%2C1060&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2024/04/add-template.webp?ssl=1)

From there, you can select the template that you want to create. If the template type has any patterns registered for it, a new **Choose a pattern** modal will appear, overlaying the template-editing interface.

For example, when choosing the **Front Page** option with the default Twenty Twenty-Four theme, you will see this:

[![A modal overlay showing four template options for the homepage from within the WordPress site editor.](https://i0.wp.com/developer.wordpress.org/files/2024/04/starter-template-patterns-tt4.webp?resize=2048%2C1061&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2024/04/starter-template-patterns-tt4.webp?ssl=1)

This gives your theme users a really nice onramp for building templates. It means they don’t have to create everything from the ground up and can get started down the right path.

#### [How to create template type patterns](#how-to-create-template-type-patterns)

Unlike page patterns, you will usually not make any of your patterns a template pattern. These are starting points for an entire template, so their use cases are much more limited and specific.

Because template patterns represent an entire template, you would typically include global elements like the header, footer, sidebar, and other sections that your theme’s templates display.

As noted in [Registering Patterns](https://developer.wordpress.org/themes/patterns/registering-patterns/), there is a single required header field needed for your template pattern (and one optional field):

- **`Template Types`:** One or more template types, separated by comma, that the pattern should be associated with.
- **`Inserter`:** *(Optional)* Often, you will not want template patterns to be available via the inserter. To disable this, set it to `no` or `false`.

Suppose that you created a pattern that would work well for the Front Page or Home templates. Here is what a fictional `/patterns/home-template.php` file would look like:

```auto
<?php
/**
 * Title: Home Template
 * Slug: themeslug/home-template
 * Template Types: front-page, home
 * Viewport width: 1376
 * Inserter: no
 */
?>
<!-- Block code here. -->
```

From that point, anytime a user attempted to create a new Front Page or Home template from the WordPress Site Editor, they would be presented with your template pattern as a starting point.

<a name="supported-template-types"></a>
#### [Supported template types](#supported-template-types)

The following list includes the templates that you can define via the `Template Types` field, but you can always reference the [Template Hierarchy](https://developer.wordpress.org/themes/templates/template-hierarchy/) documentation for a full overview of templates:

- `index`
- `home`
- `front-page`
- `singular`
- `single`
- `page`
- `archive`
- `author`
- `category`
- `taxonomy`
- `date`
- `tag`
- `attachment`
- `search`
- `privacy-policy`
- `404`

<a name="using-template-patterns-in-templates"></a>
#### [Using template patterns in templates](#using-template-patterns-in-templates)

When creating custom template patterns, it also makes sense to reuse those patterns within your templates. *Why rewrite code?*

Imagine that you created a template pattern that would work as both a Home and Index template. It would look like this:

```auto
<?php
/**
 * Title: Index Template
 * Slug: themeslug/index-template
 * Template Types: home, index
 * Viewport width: 1376
 * Inserter: no
 */
?>
<!-- Block code here. -->
```

Now suppose that you included a `/templates/index.html` template in your theme. Instead of adding the code in two places, you can simply call the pattern from the template file:

```auto
<!-- wp:pattern {"slug":"themeslug/index-template"} /-->
```

To learn more about including patterns in templates, check out the [Usage in Templates](https://developer.wordpress.org/themes/patterns/usage-in-templates/) documentation.

First published

April 30, 2024

[Previous
Usage in Templates
Previous: Usage in Templates](https://developer.wordpress.org/themes/patterns/usage-in-templates/)

[Next
Block Type Patterns
Next: Block Type Patterns](https://developer.wordpress.org/themes/patterns/block-type-patterns/)

---

<a name="block-stylesheets-1"></a>
## Block Stylesheets

<a name="in-this-article-8"></a>
### In this article

Table of Contents

- [Why use block stylesheets?](#why-use-block-stylesheets)
- [Creating block stylesheets](#creating-block-stylesheets)
  - [Organizing and naming block stylesheets](#organizing-and-naming-block-stylesheets)
  - [Adding CSS to a block stylesheet](#adding-css-to-a-block-stylesheet)
  - [Registering a block stylesheet](#registering-a-block-stylesheet)

[↑ Back to top](#wp--skip-link--target)

When styling blocks, you should always do so via the [`theme.json` styles property](https://developer.wordpress.org/themes/global-settings-and-styles/styles/) if possible. This ensures that your styles have the best compatibility across the system, working alongside the default WordPress styles, those added by plugins, and user customizations.

But there are times when you simply need to step outside of what’s easily achievable via `theme.json`. For those cases, you should use WordPress’ built-in block stylesheets system.

In this article, you will learn how to register per-block stylesheets, but remember that `theme.json` should be your first choice for styling in most cases.

<a name="why-use-block-stylesheets"></a>
### [Why use block stylesheets?](#why-use-block-stylesheets)

The primary use case for block stylesheets is when you have too much CSS to add to [`styles.blocks.{blockname}.css`](https://developer.wordpress.org/themes/global-settings-and-styles/styles/styles-reference/#css) in `theme.json`. This property allows you to add custom CSS, but it’s only ideal when it’s just a small bit of code. This is because you lose out on syntax highlighting and must place everything in a single line (JSON doesn’t support line breaks).

You may also be tempted to put all your custom CSS into your theme’s primary `style.css` file. That may be OK for some use cases, but the block stylesheets system often offers better performance by only loading the block’s CSS if the block is in use on a page. On the front end, it will also inline this code within the `<head>` area.

Creating separate stylesheets for individual blocks is also beneficial for larger and more complex projects that have a lot of custom CSS for many different blocks. The separation of the files makes it easier to organize and manage your code.

<a name="creating-block-stylesheets"></a>
### [Creating block stylesheets](#creating-block-stylesheets)

To create custom block stylesheets, there are three steps you must take:

1. Decide on an organizational and naming scheme.
2. Write your custom CSS.
3. Register your custom block stylesheet(s).

<a name="organizing-and-naming-block-stylesheets"></a>
#### [Organizing and naming block stylesheets](#organizing-and-naming-block-stylesheets)

Before registering a block stylesheet, you first need to know what folder you will store your custom block stylesheets in. This can be anywhere you choose (there is no standard location), and the code below will assume you are putting block stylesheets in an `/assets/blocks` folder in your theme.

You should also decide on how you will name your CSS files. Again, there is no standard naming convention, but a good option is to use the block namespace and slug like so: `{namespace}-{slug}.css`. With this naming convention, a stylesheet for the `core/group` block would become `core-group.css`.

Here is an example structure of what this could look like with CSS files for a few core blocks:

- `assets/`
  - `blocks/`
    - `core-group.css`
    - `core-image.css`
    - `core-media-text.css`

<a name="adding-css-to-a-block-stylesheet"></a>
#### [Adding CSS to a block stylesheet](#adding-css-to-a-block-stylesheet)

To style a core block, the most important thing you need to know is its CSS class. This is automatically generated according to the block’s namespace and slug in the form of `.wp-block-{namespace}-{slug}`.

Here is an example of styling a block with the namespace and slug of `super/duper` would look like:

```auto
.wp-block-super-duper {
	/* custom CSS goes here. */
}
```

Core WordPress blocks are an exception to this naming rule. Their namespace is `core`, but this is not included in any of the core blocks’ CSS classes. Instead, they use the `.wp-block-{slug}` format.

It’s possible for third-party block developers to change the CSS class that gets output, so this general guide may not always be true for third-party blocks. In those cases, you will want to locate the block’s CSS class in the source code.

Suppose that you wanted to add some custom styling for the core Image block, which has the namespace and slug of `core/image`. You would need to target the `.wp-block-image` class.

Let’s try creating a gradient background, which essentially acts as a *faux* border for the `<img>` element within the Image block. The goal is to create a style that looks like this:

[![WordPress post editor showing an image of palm trees with an orange-to-red gradient border.](https://i0.wp.com/developer.wordpress.org/files/2023/10/block-stylesheets-image-bg.jpg?resize=2048%2C923&ssl=1)](https://i0.wp.com/developer.wordpress.org/files/2023/10/block-stylesheets-image-bg.jpg?ssl=1)

First, create an `/assets/blocks/core-image.css` file in your theme. Then, add this CSS code to it:

```auto
.wp-block-image img {
	padding: 1rem;
	background: linear-gradient(-60deg,#ff5858,#f09819);
}
```

Because this stylesheet isn’t registered, your custom styles won’t show in the editor or on the front end yet.

<a name="registering-a-block-stylesheet"></a>
#### [Registering a block stylesheet](#registering-a-block-stylesheet)

To register your block stylesheet, you will use the [`wp_enqueue_block_style()`](https://developer.wordpress.org/reference/functions/wp_enqueue_block_style/) function. When registering block stylesheets, you should also execute the code on the `init` hook.

The `wp_enqueue_block_style()` function accepts two parameters:

- **`$block_name`:** The block name, including both the namespace and slug (e.g., `core/image`).
- **`$args`:** An array of arguments that is passed to [`wp_register_style()`](https://developer.wordpress.org/reference/functions/wp_register_style/):
  - **`handle`:** A unique handle for your stylesheet.
  - **`src`:** The source URL for the stylesheet.
  - **`path`:** The directory path for the stylesheet (needed to inline the CSS in `<head>`).
  - **`deps`:** An array of registered stylesheet handles this stylesheet depends on.
  - **`ver`:** A custom stylesheet version number.
  - **`media`**: The media for which the stylesheet has been defined.

To register your custom stylesheet for the Image block, add this code to your `functions.php` file:

```auto
add_action( 'init', 'themeslug_enqueue_block_styles' );

function themeslug_enqueue_block_styles() {
	wp_enqueue_block_style( 'core/image', array(
		'handle' => 'themeslug-block-image',
		'src'    => get_theme_file_uri( "assets/blocks/core-image.css" ),
		'path'   => get_theme_file_path( "assets/blocks/core-image.css" )
	) );
}
```

You can also configure additional arguments for your call to `wp_enqueue_block_style()`, but the above is the minimum needed for WordPress to inline your CSS code in the `<head>` area of the site.

For a deeper dive into block stylesheets, check out [Leveraging theme.json and per-block styles for more performant themes](https://developer.wordpress.org/news/2022/12/leveraging-theme-json-and-per-block-styles-for-more-performant-themes/) on the WordPress Developer Blog.

First published

November 6, 2023

[Previous
Block Style Variations
Previous: Block Style Variations](https://developer.wordpress.org/themes/features/block-style-variations/)

[Next
Block Variations
Next: Block Variations](https://developer.wordpress.org/themes/features/block-variations/)

---

## Taxonomy Templates

### In this article

Table of Contents

- [Taxonomy Template Hierarchy](#taxonomy-template-hierarchy)
  - [Category](#category)
  - [Tag](#tag)
  - [Custom Taxonomy](#custom-taxonomy)
- [Creating Taxonomy Template Files](#creating-taxonomy-template-files)
- [Examples](#examples)
  - [Adding Text to Category Pages](#adding-text-to-category-pages)
  - [Modify How Posts are Displayed](#modify-how-posts-are-displayed)

[↑ Back to top](#wp--skip-link--target)

When a visitor clicks on a hyperlink to category, tag or custom taxonomy, WordPress displays a page of posts in reverse chronological order filtered by that taxonomy.

By default, this page is generated using the *index.php* template file. You can create optional template files to override and refine the *index.php* template files. This section explains how to use and create such templates.

### [Taxonomy Template Hierarchy](#taxonomy-template-hierarchy)

WordPress display posts in the order determined by the [Template Hierarchy](https://developer.wordpress.org/themes/basics/template-hierarchy/ "Template Hierarchy").

The *category.php*, *tag.php*, and *taxonomy.php* templates allow posts **filtered** by taxonomy to be treated differently from **unfiltered** posts or posts **filtered by a different taxonomy**. (Note: post refers to any post type – posts, pages, custom post types, etc.). These files let you target specific taxonomies or specific taxonomy terms. For example:

- *taxonomy-{taxonomy}-{term}.php*
- *taxonomy-{taxonomy}.php*
- *tag-{slug}.php*
- *tag-{id}.php*
- *category-{slug}.php*
- *category-{ID}.php*

So you could format all posts in an animal taxonomy named *news* on a page that looks different from posts filtered in other categories.

The *archive.php* template provides the most general form of control, providing a layout for all archives; that is, a page that displays a list of posts.

#### [Category](#category)

For categories, WordPress looks for the *category-{slug}.php* file. If it doesn’t exist, WordPress then looks for a file for the next hierarchical level, *category-{ID}.php*, and so on. If WordPress fails to find any specialized templates or an *archive.php* template file, it reverts to the default behavior, using *index.php*.

The category hierarchy is listed below:

1. *category-{slug}.php*: For example, if the category’s slug is named “news,” WordPress would look for a file named *category-news.php.*
2. *category-{ID}.php*: For example, if the category’s ID is “6”, WordPress would look for a file named *category-6.php.*
3. *category.php*
4. *archive.php*
5. *index.php*

#### [Tag](#tag)

For tags, WordPress looks for the *tag-{slug}.php* file. If it doesn’t exist, WordPress then looks for a file for the next hierarchical level, *tag-{ID}.php*, and so on. If WordPress fails to find any specialized templates or an *archive.php* template file, it will revert to the default behavior, using *index.php*.

The tag hierarchy is listed below:

1. *tag-{slug}.php*: For example, if the tag’s slug is named “sometag,” WordPress would look for a file named *tag-sometag.php.*
2. *tag-{id}.php*: For example, if the tag’s ID were “6,” WordPress would look for a file named *tag-6.php*.
3. *tag.php*
4. *archive.php*
5. *index.php*

#### [Custom Taxonomy](#custom-taxonomy)

A custom taxonomy hierarchy works similarly to the categories and tags hierarchies described above. WordPress looks for the *taxonomy-{taxonomy}-{term}.php* file. If it doesn’t exist, WordPress then looks for a file for the next hierarchical level, *taxonomy-{taxonomy}.php*, and so on. If WordPress fails to find any specialized templates or an *archive.php* template file, it will revert to the default behavior, using *index.php*.

The hierarchy for a custom taxonomy is listed below:

1. *taxonomy-{taxonomy}-{term}.php*: For example, if the taxonomy is named “sometax,” and the taxonomy’s term is “someterm,” WordPress would look for a file named *taxonomy-sometax-someterm.php*.
2. *taxonomy-{taxonomy}.php*: For example, if the taxonomy is named “sometax,” WordPress would look for a file named *taxonomy-sometax.php*
3. *taxonomy.php*
4. *archive.php*
5. *index.php*

### [Creating Taxonomy Template Files](#creating-taxonomy-template-files)

Now you’ve decided that you need to create custom designs for content based on taxonomies, where do you start?

Rather than starting from a blank file, it is good practice to **copy the next file in the hierarchy**, if it exists. If you’ve already created an *archive.php*, make a copy called *category.php* and modify that to suit your design needs. If you don’t have an *archive.php* file, use a copy of your theme’s *index.php* as a starting point.

Follow the same procedure if you are creating any taxonomy template file. Use a copy of your *archive.php*, *category.php*, *tag.php*, or *index.php* as a starting point.

### [Examples](#examples)

Now that you’ve selected the template file in your theme’s directory that you need to modify, let’s look at some examples.

#### [Adding Text to Category Pages](#adding-text-to-category-pages)

##### [Static Text Above Posts](#static-text-above-posts)

Suppose you want some static text displayed before the list of posts on your category page(s). “Static” is text that remains the same, no matter which posts are displayed below, and no matter which category is displayed.

Open your file and above [The Loop](https://developer.wordpress.org/themes/basics/the-loop/ "The Loop") section of your Template file, insert the following code:

```auto
<p>This is some text that will display at the top of the Category page.</p>
```

This text will only display on an archive page displaying posts in that category.

<a name="different-text-on-some-category-pages"></a>
##### [Different Text on Some Category Pages](#different-text-on-some-category-pages)

What if you want to display different text based on the category page that the visitor is using? You could add default text to the main *category.php* file, and create special *category-{slug}.php* files each with their own version of the text, but this would create lots of files in your theme. Instead, you can use [conditional tags](https://developer.wordpress.org/themes/basics/conditional-tags/ "Conditional Tags").

Again, this code would be added before the loop:

```auto
<?php if ( is_category( 'Category A' ) ) : ?>
	<p>This is the text to describe category A.</p>
<?php elseif ( is_category( 'Category B' ) ) : ?>
	<p>This is the text to describe category B.</p>
<?php else : ?>
	<p>This is some generic text to describe all other category pages, I could be left blank.</p>
<?php endif; ?>
```

This code does the following:

1. Checks to see if the visitor has requested Category A. If yes, it displays the first piece of text.
2. Checks for category B if the user didn’t request category A. If yes, it displays the second piece of text.
3. Displays the default text, if neither was requested.

##### [Display Text only on First Page of Archive](#display-text-only-on-first-page-of-archive)

If you have more posts than fits on one page of your archive, the category splits into multiple pages. Perhaps you want to display static text, if the user is on the first page of the results.

To do this, use a PHP if statement that looks at the value of the $paged WordPress variable.

Put the following above The Loop:

```auto
<?php if ( $paged < 2 ) : ?>
	<p>Text for first page of Category archive.</p>
<?php endif; ?>
```

This code asks whether the page displayed is the first page of the archive. If it is, the text for the first page is displayed. Otherwise, the text for the subsequent pages is displayed.

<a name="modify-how-posts-are-displayed"></a>
#### [Modify How Posts are Displayed](#modify-how-posts-are-displayed)

<a name="excerpts-vs-full-posts"></a>
##### [Excerpts vs. Full Posts](#excerpts-vs-full-posts)

You can choose whether to display full posts or just excerpts. By displaying excerpts, you shorten the length of your archive page.

Open your file and find the loop. Look for:

```auto
the_content()
```

And replace it with:

```auto
the_excerpt()
```

And if your theme is displaying excerpts but you want to display the full content, replace `the_excerpt` with `the_content`.

First published

October 22, 2014

Last updated

October 29, 2022

[Previous
Post Template Files
Previous: Post Template Files](https://developer.wordpress.org/themes/classic-themes/templates/post-template-files/)

[Next
Page Templates
Next: Page Templates](https://developer.wordpress.org/themes/classic-themes/templates/page-template-files/)

---

<a name="feedback"></a>
## Feedback

[↑ Back to top](#wp--skip-link--target)

<a name="giving-feedback"></a>
### Giving Feedback

We welcome suggestions to improve the article, whether it is to add new topics or to rectify mistakes, you’re invited to help.

You can do so in the following ways

- Connect to [Slack](https://make.wordpress.org/chat/) and join [#docs](https://wordpress.slack.com/messages/docs/) and make your suggestion there, one of the Documentation Team members will help
- Join the [Documentation Team](https://make.wordpress.org/docs/) as an editor and edit away!
- Open a ticket in the [Documentation Issue Tracker repository](https://github.com/WordPress/Documentation-Issue-Tracker) on GitHub with the [“themes” label](https://github.com/WordPress/Documentation-Issue-Tracker/labels/themes).

In-page feedback forms are currently planned for the handbooks.

First published

January 15, 2017

Last updated

June 5, 2024

[Previous
Credits
Previous: Credits](https://developer.wordpress.org/themes/credits/)