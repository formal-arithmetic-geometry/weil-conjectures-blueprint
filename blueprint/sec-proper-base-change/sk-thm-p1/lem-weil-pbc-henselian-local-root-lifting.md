+++
id = "lem-weil-pbc-henselian-local-root-lifting"
kind = "lemma"
title = "A local ring is henselian (idempotent lifting) iff simple roots of monic polynomials lift"
lean = ["IsLocalRing.idempotent_lifting_iff_monic_simple_root_lifting"]
order = 1908
uses = ["def-weil-pbc-henselian-terminology"]
tags = ["stacks-04GF"]
+++
Let $(R,\mathfrak m,\kappa)$ be a local ring. The following are equivalent: (i) $R$ is henselian in the sense of [def-weil-pbc-henselian-terminology], i.e. for every finite $R$-algebra $B$ every idempotent of $B/\mathfrak mB$ lifts uniquely to an idempotent of $B$; (ii) for every monic polynomial $f\in R[T ]$ and every $a_0\in\kappa$ with $\overline f(a_0)=0$ and $\overline{f'}(a_0)\neq0$ (where $\overline f\in\kappa[T ]$ is the reduction of $f$) there exists $a\in R$ with $f(a)=0$ and $a\bmod\mathfrak m=a_0$.
