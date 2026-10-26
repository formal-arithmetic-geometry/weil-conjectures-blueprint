+++
id = "lem-pur-torsion-sheaf-constant-module"
kind = "lemma"
title = "An abelian sheaf killed by N is a module over the constant sheaf Z/N"
order = 2641
uses = ["def-weil-pbc-constant-sheaf", "def-weil-sheaf-of-modules-category"]
tags = ["stacks-03CY"]
+++
Let $\mathcal C$ be a site, $N\in\mathbf Z_{\geq1}$, and let $(\mathbf Z/N\mathbf Z)_{\mathcal C}$
be the constant sheaf of rings [def-weil-pbc-constant-sheaf] with value
$\mathbf Z/N\mathbf Z$. Let $\mathcal F$ be a sheaf of abelian groups on $\mathcal C$ with
$N\cdot x=0$ for every object $U$ and every $x\in\mathcal F(U)$. Then:

1. $\mathcal F$ carries a unique structure of sheaf of
$(\mathbf Z/N\mathbf Z)_{\mathcal C}$-modules [def-weil-sheaf-of-modules-category] with
underlying sheaf of abelian groups $\mathcal F$ such that, for every $U$, a section of
$(\mathbf Z/N\mathbf Z)_{\mathcal C}(U)$ coming from the constant presheaf, i.e. the image of
a class $a\in\mathbf Z/N\mathbf Z$, acts on $\mathcal F(U)$ as multiplication by any
integer representative of $a$;
2. if $\mathcal F,\mathcal G$ are two such sheaves, every morphism of sheaves of abelian
groups $\mathcal F\to\mathcal G$ is $(\mathbf Z/N\mathbf Z)_{\mathcal C}$-linear, so the
sheaves of $(\mathbf Z/N\mathbf Z)_{\mathcal C}$-modules are exactly the sheaves of abelian
groups killed by $N$, with the same morphisms.

(Proof outline from the source: $\mathcal F$ is a presheaf of modules over the constant
presheaf $\mathbf Z/N\mathbf Z$, each $\mathcal F(U)$ being a $\mathbf Z/N\mathbf Z$-module
since it is killed by $N$; sheafifying, Stacks Lemma 03CY gives the unique
$(\mathbf Z/N\mathbf Z)_{\mathcal C}$-module structure on $\mathcal F^\#=\mathcal F$, and its
second part gives the linearity of morphisms, any additive map between
$\mathbf Z/N\mathbf Z$-modules being linear.)
