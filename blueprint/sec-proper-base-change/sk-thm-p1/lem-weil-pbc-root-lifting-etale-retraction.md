+++
id = "lem-weil-pbc-root-lifting-etale-retraction"
kind = "lemma"
title = "Over a local ring in which simple roots of monic polynomials lift, etale algebras with a rational point over the closed point retract"
uses = ["def-weil-etale-morphism", "def-weil-residue-field"]
tags = ["sheaf-dag", "stacks-04GG"]
+++
Let $(R,\mathfrak m,\kappa)$ be a local ring such that for every monic $f\in R[T ]$ and every $a_0\in\kappa$ with $\overline f(a_0)=0$ and $\overline{f'}(a_0)\neq0$ there is $a\in R$ with $f(a)=0$ and $a\bmod\mathfrak m=a_0$ (simple roots of monic polynomials lift; Stacks' definition of henselian). Let $R\to S$ be a ring map such that $\operatorname{Spec}S\to\operatorname{Spec}R$ is etale [def-weil-etale-morphism], and let $\mathfrak q\subset S$ be a prime ideal lying over $\mathfrak m$ such that the induced map of residue fields [def-weil-residue-field] $\kappa\to\kappa(\mathfrak q)$ is an isomorphism. Then there is exactly one $R$-algebra homomorphism $\tau:S\to R$ (a retraction of $R\to S$) with $\tau^{-1}(\mathfrak m)=\mathfrak q$.
