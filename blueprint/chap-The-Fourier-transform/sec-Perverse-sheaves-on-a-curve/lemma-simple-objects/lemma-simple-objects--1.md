+++
id = "lemma-simple-objects--1"
kind = "lemma"
title = "The simple objects (1)"
name_showing = false
order = 1255001
aliases = ["bp-r388-1"]
lean = ["AlgebraicGeometry.WeilComplex.simple_iff"]
uses = ["definition-punctual-sheaf", "definition-perverse-sheaves-curve", "definition-lisse-sheaves", "definition-weil-structure"]
+++
Let $C_0=\Aone_{\Fq}$ and let $\ell\ne\operatorname{char}\Fq$.
In the full subcategory of Weil $\Qbarl$-complexes satisfying the
curve perversity conditions of Definition [definition-perverse-sheaves-curve],
an object $P$ is simple if and only if it is isomorphic to one of the
following objects:

1. $G[0]$, where $G$ is a simple Weil sheaf with finite support;
2. $(j_*M)[1]$, where $j:U_0\hookrightarrow C_0$ is a dense open
   immersion and $M$ is a nonzero irreducible lisse Weil sheaf on $U_0$.

Here irreducibility of $M$ means that every lisse Weil subsheaf of $M$
is zero or all of $M$.
