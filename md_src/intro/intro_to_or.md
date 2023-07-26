# Introduction

In this section we'll cover the big picture questions: What is Operations Research? Where did it come from? What can I do with it?

## What is Operations Research?

If you're like me, one of the first things you'll do when learning a new subject is look it up on Wikipedia. As of this writing, [their page on Operations Research](https://en.wikipedia.org/wiki/Operations_research) first defines OR as:

> The discipline that deals with the development and application of analytical methods to improve decision-making.

I think this is a good first definition! Continuing on a bit, the article gets a little more specific:

> Employing techniques from other mathematical sciences, such as modeling, statistics, and optimization, operations research arrives at optimal or near-optimal solutions to decision-making problems.

Right. So the practice of OR involves using mathematical techniques to find the best decision possible in a given situation ("optimal" is just fancy way of saying "best"[^moreOptimal]).

[^moreOptimal]: The pedant in me wants to point out that this word "optimal" is horribly misused in conversation fairly regularly, in the common misguided phrase "more optimal". As I mentioned, "optimal" really just means "best", and "best" is not on a sliding scale; either you have the best answer or you don't. One choice can't be "more best" than another, just as one solution can't be "more optimal" than another. I think I'm fighting a losing battle on this, but maybe for the sake of this course we can all agree to never put the words "more" and "optimal" next to each other? Thanks.

## Can you give me some examples?

The above definitions were great, but maybe it's feeling a little too abstract at this point. Fair enough. Let's outline a few common problems in the OR space.

### Traveling Salesman Problem

There are many well-known problems in the world of OR, but I reckon the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP) is the best-known and most-loved among them. The setup is simple: Some old-timey door-to-door salesman is heading out on the road to sell his product to the masses. He plans to visit a certain group of cities, and thanks to his trusty atlas he knows the way between any pair of cities. Less clear, however, is the shortest path that will lead you through _all_ of the cities, and this is the aim of the TSP: In which order should you visit the cities such that your total distance traveled is minimized?

As I said, this a famous problem in the OR space. I think it's due to the simple, relatable exposition, paired with the fact that it is actually quite computationally challenging. And yet despite the challenges, modern methods are able to solve problem instances where the number of cities is in the 10,000s! The image below shows the optimal tour through selected cities in the continental US[^tspFurtherReading].

[^tspFurtherReading]: You can tell from the image that this map is pretty old. [The site from which it came](https://www.math.uwaterloo.ca/tsp/usa50/) tells a neat story about how this instance was solved, by hand, way back in 1954! There are some other interesting bits there too, well worth a read in my opinion.

![The shortest tour through 49 US cities [@tspPic]](https://www.math.uwaterloo.ca/tsp/usa50/img/newsweek_medium.jpg)

### Job-shop scheduling

You run a machine shop, and have a certain number of jobs to complete in a day. Each job requires a certain number of tasks to be done by one of your many machines, and the tasks are at least partially ordered, such that you must complete the tasks in a certain order (e.g. you have to cut a piece of wood before you sand the edges). Each machine can only work on one task at a time. You get to decide the work schedule, assigning machines to tasks at certain times in the day. What is the schedule that lets you complete all the jobs in the least amount of time?

### Portfolio optimization

You have some money to invest, and a list of potential project/assets to invest in. You'd like to invest in a way that gives you a high expected return, but there is risk involved as well. Each project comes with its own risks, and some projects may be highly correlated such that failure in one would suggest a high chance of failure in another. How can you deploy your capital in a way that minimizes downside risk while still likely generating a good profit?

## OR in practice

So we've given a few broad classes of OR problems, but maybe this is still too abstract. Let's get to real applications. Are people actually using OR out in the wild? Do these methods make a difference? In this section I'll point you to some real-life case studies where OR methods have been used to great effect.

### Textbook case studies

Your textbook handily comes chock full of case studies explaining how companies have used OR to inform their decision-making. Below I've copied part of the summary table. Check out the book to get more background on anything that piques your interest.

![Selected OR case studies [@classText]](images/or-case-studies.png)

It's pretty staggering to look at the Annual Savings figures, which taken together sum to the billions. OR is an enormously valuable tool.

### Edelman Prize

Now, admittedly, some of those case studies are a little stale. But don't fret, OR is still relevant in industry today. The [Institute for Operations Research and Management Science (INFORMS)](https://www.informs.org/) annually gives an award called the Edelman Prize for the best application of OR methodologies in industry. You can take a look at the [program for the 2023 edition of the award](https://3449182.fs1.hubspotusercontent-na1.net/hubfs/3449182/2023_Edelman_Gala_Book.pdf) and find cases submitted by names like DHL, Huawei, Lyft, and the winner Walmart.

## A brief history of OR

## Topics we'll cover
