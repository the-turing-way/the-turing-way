# Continuous integration

## Setting up my own CI step by step

- On my computer I made a diretory, made a simple function adding two numbers and a test for it. Ran pytest and it passed.
- Used git init, added and commited the files.
- On github made a repo with the same name as the directory (CI-practise)
- Put my code on github using `git remote add origin the_url` then `git push -u origin master`
- Went to https://travis-ci.org/
- Clicked "Sign in with GitHub"
- Redirected me to GitHub where permission was aked for Travis to have access to my stuff, clicked authorise
- Came up with a page with a list of my repos each of which had a switch next to them, they were all off. For my CI-practise repo I turned it on.
- On my local machine I created subtract.py which subtracts two numbers and a test for it, added and committed those files.
- I pushed to my github but travis didn't run.
- On my machine I created a branch called multiply_feature and added and committed a function and test to do that
- Pushed that to github using `git push -u origin multiply_feature`
- Switched to that branch on github and made a pull request to master
- Continuos intergration didn't run, but there is a link just above the bit saying no merge conficts saying continuous intergration hasn't been set up and there are apps that can do it.
- Clicked that, it took me to a github page about contuinous intergration
- Remembered I need a .travis.yml file if travis is to run. Created one on my local machine

 ```
language: python
python:
  - "2.7"
script:
  - pytest
```

- Pushed to the github version of the branch. On the pull request travis automatically started running and the tests passed. Worth noting that throughout I was still able to merge.
- Merged.
- Switched back to master on my machine and github.
- Made an inconsequential change, just added a print statement to the add funtion. Committed and pushed to github.
- The change immediatly appeared in my master on github, however on travis it did run the tests and showed up green.
- Made another branch, on it created a function and test to square numbers. Made a deliberate mistake so the tests would fail. Pushed to github.
- The files/code I added immediatly appeared in my github version of that branch, however on travis the tests failed.
- Made a pull request from the branch to master. The travis tests re-ran on the pull request and failed again (though i still had the option to merge if I wanted).
- On my computer I fixed the bug, added, committed and pushed. On the pull request the tests automatically re-ran.
- The tests passed and I merged into master.

## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
> why we think you should read the whole thing

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

## Chapter content
> depending on the content, this might be more structured, e.g. with exercises, gotcha sections etc

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.

## Acknowledgements

Thanks to David Jones for useful discussions.
