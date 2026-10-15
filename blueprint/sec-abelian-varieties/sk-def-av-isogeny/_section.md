+++
id = "sk-def-av-isogeny"
kind = "definition"
title = "Isogenies and their degree"
lean = ["AlgebraicGeometry.IsIsogeny", "AlgebraicGeometry.isogenyDegree"]
order = 531
tags = ["sketch"]
+++
Let $A,B$ be group schemes over $k$.
An *isogeny* $f:A\to B$ is a surjective homomorphism of $k$-group
schemes with finite kernel; its *degree* is the order of the kernel,
$\deg f:=\lvert\ker f\rvert$ ([sk-def-av-group-scheme]).

When $A$ and $B$ are abelian varieties, an isogeny $f$ is finite and
flat, and its degree as a finite flat morphism agrees with $\deg f$.
