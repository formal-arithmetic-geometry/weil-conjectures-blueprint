+++
id = "lem-weil-pbc-finite-stalk-formula-restriction"
kind = "lemma"
title = "The finite stalk formula is given by the restrictions of germs"
uses = ["def-weil-finite-integral-morphism", "def-weil-pbc-abelian-etale-sheaves", "def-weil-geometric-point", "def-weil-pbc-geometric-stalks", "def-weil-pbc-direct-image"]
lean = ["branch", "declarations", "note"]
tags = ["stacks-03QP"]
+++
Let $f:X\to Y$ be a finite morphism of schemes [def-weil-finite-integral-morphism], $F$ an abelian sheaf on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves] and $\bar y:\operatorname{Spec}\Omega\to Y$ a geometric point [def-weil-geometric-point]. Let $P(\bar y)$ be the set of geometric points $\bar x:\operatorname{Spec}\Omega\to X$ with $f\circ\bar x=\bar y$ (the geometric points of the fibre $X\times_Y\operatorname{Spec}\Omega$ with field $\Omega$). For $\bar x\in P(\bar y)$ let $r_{f,\bar x,F}:(f_*F)_{\bar y}\to F_{\bar x}$ be the restriction of germs: for a pointed etale neighbourhood $(V,\bar v)$ of $\bar y$ [def-weil-pbc-geometric-stalks], $(V\times_YX,(\bar v,\bar x))$ is a pointed etale neighbourhood of $\bar x$, and $r_{f,\bar x,F}$ sends the germ at $(V,\bar v)$ of $s\in(f_*F)(V)=F(V\times_YX)$ [def-weil-pbc-direct-image] to the germ of $s$ at $(V\times_YX,(\bar v,\bar x))$. Then $P(\bar y)$ is finite and the homomorphism
$$(r_{f,\bar x,F})_{\bar x\in P(\bar y)}:(f_*F)_{\bar y}\longrightarrow\prod_{\bar x\in P(\bar y)}F_{\bar x}$$
is an isomorphism. In particular each $r_{f,\bar x,F}$ is surjective. (This is the isomorphism of [lemma-weil-pbc-finite-stalk-formula] with its components named.)
