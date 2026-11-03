+++
id = "lem-sp-abelian-refinements"
kind = "lemma"
title = "Element chasing up to refinements in an abelian category"
uses = ["def-sp-abelian"]
lean = ["CategoryTheory.epi_iff_surjective_up_to_refinements", "CategoryTheory.ShortComplex.exact_iff_exact_up_to_refinements", "CategoryTheory.Limits.CokernelCofork.IsColimit.comp_π_eq_zero_iff_up_to_refinements"]
order = 2096
tags = ["mathlib", "stacks-08N5"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian]. Call a morphism $a:T\to X$ from an arbitrary object $T$ an *element* of $X$, and for an element $a$ an *epimorphic refinement* a composite $a\circ\rho$ with $\rho:T'\twoheadrightarrow T$ an epimorphism. Then:

(a) A morphism $u:X\to Y$ is an epimorphism if and only if every element $y:T\to Y$ lifts after an epimorphic refinement: there are an epimorphism $\rho:T'\to T$ and $x:T'\to X$ with $y\circ\rho=u\circ x$.

(b) A complex $X_1\xrightarrow{u}X_2\xrightarrow{v}X_3$ ($v\circ u=0$) is exact at $X_2$, i.e. $\operatorname{im}u=\ker v$ as subobjects of $X_2$, if and only if for every element $x_2:T\to X_2$ with $v\circ x_2=0$ there are an epimorphism $\rho:T'\to T$ and $x_1:T'\to X_1$ with $x_2\circ\rho=u\circ x_1$.

(c) If $c:Y\to Q$ is a cokernel of $u:X\to Y$, then for an element $y:T\to Y$ one has $c\circ y=0$ if and only if there are an epimorphism $\rho:T'\to T$ and $x:T'\to X$ with $y\circ\rho=u\circ x$.
