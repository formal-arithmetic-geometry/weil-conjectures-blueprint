+++
id = "lem-weil-pbc-finite-algebra-etale-idempotent-decomposition"
kind = "lemma"
title = "After an etale neighbourhood with trivial residue extension, a finite algebra splits by idempotents into factors with at most one prime over the point (finite case of Stacks 00UK/00UL)"
uses = ["def-weil-etale-morphism", "def-weil-residue-field"]
lean = ["Algebra.exists_etale_completeOrthogonalIdempotents_forall_liesOver_eq"]
tags = ["sheaf-dag", "mathlib", "stacks-00UK"]
+++
Let $R$ be a commutative ring, $\mathfrak p\subset R$ a prime ideal and $R\to S$ a ring map making $S$ a finitely generated $R$-module. For a prime $\mathfrak q$ of a ring $A$ write $\kappa(\mathfrak q)$ for its residue field, the residue field of the local ring $A_{\mathfrak q}$ (the residue field of $\operatorname{Spec}A$ at the point $\mathfrak q$ [def-weil-residue-field]). Then there exist: a ring map $R\to R'$ such that $\operatorname{Spec}R'\to\operatorname{Spec}R$ is etale [def-weil-etale-morphism]; a prime $\mathfrak p'\subset R'$ whose preimage in $R$ is $\mathfrak p$ and such that the induced map $\kappa(\mathfrak p)\to\kappa(\mathfrak p')$ is bijective; an integer $n\ge0$; elements $e_1,\dots,e_n,e_\infty$ of the ring $C=R'\otimes_RS$ (an $R'$-algebra via $r'\mapsto r'\otimes1$) that are complete orthogonal idempotents ($e_i^2=e_i$, $e_ie_j=0$ for $i\neq j$, $e_1+\dots+e_n+e_\infty=1$); and primes $Q_1,\dots,Q_n$ of $C$, each with preimage $\mathfrak p'$ in $R'$, such that (a) $e_i\notin Q_i$ for $i=1,\dots,n$, and (b) every prime $Q$ of $C$ with preimage $\mathfrak p'$ in $R'$ contains $e_\infty$, and for each $i$ with $e_i\notin Q$ one has $Q=Q_i$.
