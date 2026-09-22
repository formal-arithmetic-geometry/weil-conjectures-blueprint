+++
id = "lem-kun-0BKZ"
kind = "lemma"
title = "Cohomology of unbounded complexes"
order = 6081
lean = ["AlgebraicGeometry.Etale.cohomology_unbounded_of_acyclic_basis"]
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-kun-rgamma-unbounded"]
+++
Let $X$ be a scheme, $K\in D(X_{\Et})$, and $\mathcal B$ a class of objects
of $X_{\Et}$ such that (1) every object of $X_{\Et}$ admits a covering by
objects of $\mathcal B$, and (2) $H^p(U_{\Et},\mathcal H^q(K))=0$ for all
$p>0$, all $q\in\mathbf Z$, and all $U\in\mathcal B$. Then
$H^q(U_{\Et},K)=H^0(U_{\Et},\mathcal H^q(K))$ for all $q$ and all
$U\in\mathcal B$.

(*Source:* Stacks Project, [Tag
0BKZ](https://stacks.math.columbia.edu/tag/0BKZ).)

## Proof

For $U\in\mathcal B$ the hypercohomology spectral sequence (in the
global-section form) has
$E_2^{p,q}=H^p(U_{\Et},\mathcal H^q(K))\Rightarrow H^{p+q}(U_{\Et},K)$.
Hypothesis (2) kills the columns $p>0$, so only the column $p=0$ survives
and there are no differentials to or from it; hence
$H^n(U_{\Et},K)=E_2^{0,n}=H^0(U_{\Et},\mathcal H^n(K))$ for every $n$.

Unresolved dependencies: def:weil-pbc-etale-cohomology
