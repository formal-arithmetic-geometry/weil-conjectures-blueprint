+++
id = "lemma-weil-pbc-constructible-approximation"
kind = "lemma"
title = "Constructible approximation for effacement"
lean = ["AlgebraicGeometry.Etale.exists_isConstructibleSheaf_hom_of_henselianRing"]
order = 1584
uses = ["def-weil-pbc-constructible-complexes"]
+++
Let $\Lambda$ be a finite ring, let $(A,I)$ be a henselian pair with
$T=\operatorname{Spec}A$ and closed fibre $T_0=\operatorname{Spec}A/I$, let
$F$ be a sheaf of $\Lambda$-modules on $T_{\Et}$ with restriction $F_0$ to
$T_0$, and let $c\in H^q(T_0,F_0)$ for some $q\ge0$. Then there are a
constructible sheaf of $\Lambda$-modules $C$ on $T$ and a morphism
$\iota:C\to F$ such that $c$ lies in the image of
$H^q(T_0,C_0)\to H^q(T_0,F_0)$.

The morphism $\iota$ cannot in general be chosen to be a monomorphism: for
$T=T_0=\operatorname{Spec}\prod_{\mathbf N}\mathbf F_2$, $F=x_*\mathbf Z/2$ the
skyscraper sheaf at a closed non-open point $x$ (a non-principal
ultrafilter), $q=1$ and $c$ the nonzero class of
$H^1(T,x_*\mathbf Z/2)=H^1(\operatorname{Gal}(\overline{\mathbf F}_2/\mathbf F_2),\mathbf Z/2)=\mathbf Z/2$,
the only subsheaf of $F$ from which $c$ comes is $F$ itself, whose support
$\{x\}$ is not constructible.
