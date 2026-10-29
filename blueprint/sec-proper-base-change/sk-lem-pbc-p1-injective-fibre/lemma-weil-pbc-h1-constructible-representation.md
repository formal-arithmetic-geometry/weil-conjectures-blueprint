+++
id = "lemma-weil-pbc-h1-constructible-representation"
kind = "lemma"
title = "Constructible representation of an $H^1$ class"
lean = ["AlgebraicGeometry.Etale.exists_sum_eq_of_injective_projectiveLine"]
order = 1690
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-constructible-approximation", "lemma-weil-pbc-constructible-finite-pushforward", "def-weil-pbc-strict-henselian-setup"]
+++
Let $A$ be a strictly henselian local ring with residue field $\kappa$, and in the
setup of [def-weil-pbc-strict-henselian-setup] let $X=\mathbf P^1_A$ with closed
fibre $X_0=\mathbf P^1_\kappa$. Let $r$ be a prime and $I$ an injective sheaf of
$\mathbf F_r$-modules on $X_{\Et}$. Every class $c\in H^1(X_0,I_0)$ is a finite
sum

$$
 c=\sum_{j=1}^m\psi_{j,0}(x_j),
$$

where $h_j:V_j\to X$ are finite morphisms of finite presentation, $M_j$ are
finite $\mathbf F_r$-modules, $\psi_j:(h_j)_*\underline{M_j}\to I$ are morphisms
of sheaves, and $x_j\in H^1(X_0,((h_j)_*\underline{M_j})_0)$. Equivalently, $c$ is
the image of a class of $H^1\bigl(X_0,(\bigoplus_j(h_j)_*\underline{M_j})_0\bigr)$
under a map $\bigoplus_j(h_j)_*\underline{M_j}\to I$.
