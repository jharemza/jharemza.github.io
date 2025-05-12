---
layout: post
title: "Private vs Protected in Java"
excerpt: A concise explanation of access modifiers in Java and how `private` and `protected` differ in use and scope.
author: jharemza
date: 2019-01-02
updated: 2019-01-02
tags: [java, access-modifiers, oop]
categories: [blog]
---
## Introduction

In this post we look at some of the different modifiers in Java.

## The Lead Up

Recently, I discovered a course by Princeton University on [Coursera](https://www.coursera.org/) that focuses on algorithms. You can check them out here:

- [Algorithms, Part I](https://www.coursera.org/learn/algorithms-part1)
- [Algorithms, Part II](https://www.coursera.org/learn/algorithms-part2)

However, when I checked the course requirements I found that it was taught in Java. At the time I found the course(s) about a week ago (at the time of writing) I knew zero Java, and I still know very little. So off I went to [SoloLearn](https://www.sololearn.com).

There's a section that covers inheritance in OOP, and I had some familiarity with inheritance from working in other OOP languages such as Python and C/C++. However, I started seeing code snippets with various modifiers and no real outlay of definitions. For example:

{% highlight java %}
class BankAccount {
private double balance=0;
public void deposit(double x) {
if(x > 0) {
balance += x;
}
}
}
{% endhighlight %}

And then later on I see:

{% highlight java %}
class Animal {
protected int legs;
public void eat() {
System.out.println("Animal eats");
}
}
class Dog extends Animal {
Dog() {
legs = 4;
}
}
class MyClass {
public static void main(String[ ] args) {
Dog d = new Dog();
d.eat();
}
}
{% endhighlight %}

So then I wanted to know the difference between `private` and `protected`.

## The Answer

It turns out Java has what are referred to as modifiers. "What's a modifier?" you ask. "Don't worry baby birds. I'll feed ya."

A Java access modifier specifies which classes can access a given class and its fields, constructors and methods. Access modifiers can be specified separately for a class, its constructors, fields and methods. Java access modifiers are also sometimes referred to in daily speech as Java access specifiers, but the correct name is Java access modifiers. (See [Jenkov.com Java Tutorial](https://tutorials.jenkov.com/java/access-modifiers.html))

**Aside:** Java apparently has "access modifiers" (what we're talking about here) and non-access modifiers (a subject for another time).

![Access Modifiers vs. Non-Access Modifiers](/assets/img/posts/AccessAndNonAccessModifiers.png)

As seen in the table above the 4 types of access modifiers are:

- `private` - Visible to the class only.
- `default` - Visible to the package. No modifiers are required.
- `protected` -Visible to the package and all subclasses.
- `public` - Visible to the world.

## tl;dr: The Answer in One Table

To summarize:

![Summary Table](/assets/img/posts/access-modifier.png)

## Extra References on Java Modifiers

The below references include extended descriptions of Java modifiers as well as code examples.

- [GeeksforGeeks](https://www.geeksforgeeks.org/access-modifiers-java/)
- [w3schools](https://www.w3schools.com/java/java_modifiers.asp)
