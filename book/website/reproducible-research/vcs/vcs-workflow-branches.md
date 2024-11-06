(rr-vcs-workflow-branches)=
# Non-Linear Development of Your Project with "Branches"

> This chapter is for more advanced users.
> It allows you to work on the code, while allowing other users to see the stable version of your data first.
>Branches are also a way to make changes that can be easily trashed.

 So you have your project and you want to add something new or try something out before reflecting the changes in the main project folder.
 To add something new, you can continue editing your files and save them with the proposed changes.
 Suppose you want to try something without reflecting the changes in the central repository.
 In that case, you can use the "branching" feature of more advanced version control systems such as Git.
 A branch creates a local copy of the main repository where you can work and try new changes.
 Any work you do on your branch will not be reflected on your main project (referred to as your main branch) so it remains secure and error-free.
 At the same time, you can test your ideas and troubleshoot in a local branch.

 When you are happy with the new changes, you can introduce them to the main project.
 The merge feature in Git allows the independent lines of development in a local branch to get integrated into the main branch.

 ```{figure} ../../figures/one-branch.*
 ---
 name: one-branch
 alt: >
  A row of nine grey dots is labelled 'Main', representing the main branch. 
  Each of these dots is connected to the two neighbouring dots with an arrow pointing to the right.
  On top of the main branch is a line of four blue dots, that are also connected by arrows.
  These blue dots are labelled 'Feature A' and represent the development branch. 
  The development branch is connected to the main branch through the same arrows that connect the dots within a branch:
  An arrow points from grey dot number 3 to blue dot number 1, and in the same fashion an arrow points from blue dot number 4 to grey dot number 8.
 ---
 The development and main branch in Git.
 ```

 You can have more than one branch off of your main copy.
 If one of your branches ends up not working, you can either abandon it or delete it without impacting the main branch of your project.

 ```{figure} ../../figures/two-branches.*
 ---
 name: two-branches
 alt: >
  In the same way as in the previous figure, a line of nine connected grey dots represents the main branch.
  On top of the main branch a line of four connected blue dots represents development branch one (named 'Feature A').
  Additionally, below the main branch a line of two connected orange dots, representing development branch two (named 'Feature B'), is shown.
  The two development branches connect to the main branch at different positions. 
 ---
 Two development branches and one main branch in Git.
 ```

 If you want, you can create branches from branches (and branches off of those branches and so on).

 ```{figure} ../../figures/sub-branch.*
 ---
 name: sub-branch1
 alt: >
  In the same way as in the previous figure, a line of nine connected grey dots represents the main branch.
  On top of the main branch a line of four connected blue dots, representing the 'Feature A' development branch, and below the main branch line of two connected orange dots, representing the 'Feature B' development branch, are shown.
  Additionally, a line of two connected green dots shows another development branch (named 'Feature A-1') on top of the 'Feature A' development branch. 
  The Feature A-1 development branch only connects to the Feature A development branch, and not the main branch. 
 ---
 Several development branches in Git.
 ```

 No matter how many branches you have, you can access the past versions you made on any of them.
 If you are curious to know how to use this feature in practice, you will find more details a few sections ahead.
