---
toc: true
layout: post
description: A minimal example of using markdown with fastpages.
categories: [markdown]
title: An Example Markdown Post
image: /images/404.png
tags: []
---
# Example Markdown Post

## Basic setup

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-filename.md`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `filename` is whatever file name you choose, to remind yourself what this post is about. `.md` is the file extension for markdown files.

The first line of the file should start with a single hash character, then a space, then your title. This is how you create a "*level 1 heading*" in markdown. Then you can create level 2, 3, etc headings as you wish but repeating the hash character, such as you see in the line `## File names` above.

## Basic formatting

You can use *italics*, **bold**, `code font text`, and create [links](https://www.markdownguide.org/cheat-sheet/). Here's a footnote [^1]. Here's a horizontal rule:

---

## Lists

Here's a list:

- item 1
- item 2

And a numbered list:

1. item 1
1. item 2

## Boxes and stuff

> This is a quotation

{% include alert.html text="You can include alert boxes" %}

...and...

{% include info.html text="You can include info boxes" %}

## Images

![]({{ site.baseurl }}/images/404.png "fast.ai's logo")

## Code

You can format text and code per usual 

General preformatted text:

    # Do a thing
    do_thing()

Python code and output:

```python
# Prints '2'
print(1+1)
```

    2

Formatting text as shell commands:

```shell
echo "hello world"
./some_script.sh --option "value"
wget https://example.com/cat_photo1.png
```

Formatting text as YAML:

```yaml
key: value
- another_key: "another value"
```


## Tables

| Column 1 | Column 2 |
|-|-|
| A thing | Another thing |


## Tweetcards

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Altair 4.0 is released! <a href="https://t.co/PCyrIOTcvv">https://t.co/PCyrIOTcvv</a><br>Try it with:<br><br> pip install -U altair<br><br>The full list of changes is at <a href="https://t.co/roXmzcsT58">https://t.co/roXmzcsT58</a> ...read on for some highlights. <a href="https://t.co/vWJ0ZveKbZ">pic.twitter.com/vWJ0ZveKbZ</a></p>&mdash; Jake VanderPlas (@jakevdp) <a href="https://twitter.com/jakevdp/status/1204765621767901185?ref_src=twsrc%5Etfw">December 11, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


## Footnotes



[^1]: This is the footnote.

