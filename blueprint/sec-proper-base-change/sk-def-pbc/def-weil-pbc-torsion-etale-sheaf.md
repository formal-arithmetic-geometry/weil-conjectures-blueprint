+++
id = "def-weil-pbc-torsion-etale-sheaf"
kind = "definition"
title = "Torsion abelian sheaf on the small etale site"
lean = ["AlgebraicGeometry.Scheme.IsTorsionAbelianSheaf"]
order = 1538
uses = ["def-weil-pbc-abelian-etale-sheaves", "def-pur-abelian-sheaf-kernel", "def-weil-pbc-category-colimit"]
tags = ["stacks-0DDB"]
+++
Let $T$ be a scheme and $F$ an abelian sheaf on the small etale site of $T$, i.e. an object of $\Ab(T_{\Et})$ [def-weil-pbc-abelian-etale-sheaves]. For an integer $n\ge1$ let $F[n ]=\ker(n:F\to F)$ [def-pur-abelian-sheaf-kernel] be the kernel of multiplication by $n$, the subsheaf of sections killed by $n$. Order the positive integers by divisibility; this poset is directed ($\operatorname{lcm}(n,m)$ bounds $n$ and $m$), hence a filtered small category, and for $n\mid m$ one has $F[n ]\subseteq F[m ]$ (since $m=(m/n)\cdot n$ as endomorphisms of $F$, the subobject $\ker n$ is contained in $\ker m$; sectionwise, $ns=0$ implies $ms=0$), so $n\mapsto F[n ]$ with the inclusions is a filtered diagram in $\Ab(T_{\Et})$; it has a colimit because $\Ab(T_{\Et})$ has all small colimits [def-weil-pbc-abelian-etale-sheaves], and the inclusions $F[n ]\hookrightarrow F$, which are compatible with the transition inclusions, induce a canonical map

$$
 c_F:\varinjlim_{n}F[n ]\longrightarrow F
$$

from its colimit [def-weil-pbc-category-colimit] in $\Ab(T_{\Et})$. The sheaf $F$ is *torsion* (a *torsion abelian sheaf*) if $c_F$ is an isomorphism.
