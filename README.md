# TwoScouts

Python solution for the Two Scouts problem.

## Problem

Two scouts start from different towns and must reach the same destination.

Their routes cannot share any town except the destination.

The goal is to minimize the total number of unique towns visited by both scouts.

## Approach

The program finds all possible paths from each scout to the destination using DFS.

It then compares pairs of paths and checks whether they share only the destination.

For every valid pair, the number of unique towns is calculated and the minimum is selected.

## Language

Python 3
