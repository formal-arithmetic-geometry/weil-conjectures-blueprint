+++
id = "lem-weil-pbc-right-adjoint-preserves-limits"
kind = "lemma"
title = "A right adjoint preserves limits"
uses = ["def-weil-category-product"]
lean = ["CategoryTheory.Adjunction.rightAdjoint_preservesLimits"]
order = 1308
tags = ["mathlib", "stacks-0038"]
+++
Let $L:\mathcal C\to\mathcal D$ be left adjoint to $R:\mathcal D\to\mathcal C$. Let $I$ be a small category and $M:I\to\mathcal D$ a diagram with a limit $(\varprojlim_IM,(\pi_i)_i)$ in $\mathcal D$. Then $(R(\varprojlim_IM),(R\pi_i)_i)$ is a limit of $R\circ M$ in $\mathcal C$. In particular (with $I$ discrete with two objects, resp. empty): if $\mathcal D$ has finite products, then for objects $Y,Y'$ of $\mathcal D$ the morphism $(R\mathrm{pr}_1,R\mathrm{pr}_2):R(Y\times Y')\to RY\times RY'$ is an isomorphism whenever the product $RY\times RY'$ exists, and $R(*)$ is a final object of $\mathcal C$ for a final object $*$ of $\mathcal D$.
