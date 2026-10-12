+++
id = "lemma-weil-pbc-constructible-approximation"
kind = "lemma"
title = "Constructible approximation for effacement"
order = 1126
uses = ["def-weil-pbc-constructible-complexes", "lemma-weil-pbc-finite-stage-killing"]
+++
Let $(T,T_0)$ be an affine henselian pair, let $F$ be a torsion sheaf on
$T_{\Et}$ with restriction $F_0$ to $T_0$, and let $c\in H^q(T_0,F_0)$ with
$q>0$. Then there are a constructible torsion sheaf $C$ on $T$ and a
morphism $\iota:C\to F$ such that $c$ lies in the image of
$H^q(T_0,C_0)\to H^q(T_0,F_0)$.

The morphism $\iota$ cannot in general be chosen to be a monomorphism: for
$T=T_0=\operatorname{Spec}\prod_{\mathbf N}\mathbf F_2$, $F=x_*\mathbf Z/2$ the
skyscraper sheaf at a closed non-open point $x$ (a non-principal
ultrafilter), $q=1$ and $c$ the nonzero class of
$H^1(T,x_*\mathbf Z/2)=H^1(\operatorname{Gal}(\overline{\mathbf F}_2/\mathbf F_2),\mathbf Z/2)=\mathbf Z/2$,
the only subsheaf of $F$ from which $c$ comes is $F$ itself, whose support
$\{x\}$ is not constructible.
