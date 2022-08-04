(pd-sdpw-exposing-data)=

# What do you do if you inadvertently expose sensitive data on GitHub?

Sometimes - no matter how careful we try to be - we might inadvertently expose sensitive data on GitHub.
Unfortunately, it is not as easy as you might think to remove this data again.

Say that you mistakenly commit a file containing sensitive data to your GitHub repository.
Simply removing the file from the repository, or indeed deleting the entire repository, will not fix the problem, as...

> "*commits may still be accessible in any clones or forks of your repository, directly via their SHA-1 hashes in cached views on GitHub, and through any pull requests that reference them*" [- GitHub Docs: Removing sensitive data from a repository](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
> 

Luckily, there are ways to fix these types of mistakes. 
