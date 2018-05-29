# QuEST-Man
Quick. and Easy. Source code. Task. Manager.

## Motivation

The motivation for this project is literally just more motivation. Sometimes I'll begin developing an idea by opening a new repo and it's really difficult to actually start programming.

With this I hope to setup an automatic server or frequently manual tracker which runs locally and tracks total git contributions. The program will run and spit out a project I'm currently working on with some sort of goal to achieve. This could be increasing the number of lines I write, commits to perform, etc... If the goal is met, then the new goal will be set higher and the priority for the accomplished project will be set lower. If the goal is not accomplished, then the priority will be set higher and the goal will stay the same.

I hope to make it dynamic and intelligent enough to mitigate senseless quest requests, but, for example, if I'm not able to add any more lines of code to a project to fulfill a quest then that project *should* be completed, and thus QuEST-Man has fulfilled its duty.

In the future I plan to break away from just covering git contributions and maybe focus more on integrated unit-testing. At that point QuEST-Man will be a package that you include in your repo as you build out the project, something similar to pytest, but perhaps more gamified.

## Goals:
 - [ ] every week provide a new quest to complete: i.e. commit this many times on a repo; write this many lines of code; etc.
 - [ ] monitor given quests on the changeover to a new quest
 - [ ] dynamically prioritize quests so that old quests are more likely to be completed
 - [ ] score the user and provide a simple UI to view progress
