+++
id = "cor-mg-central-determinant-weight"
kind = "theorem"
title = "Central element determines the determinant weight"
order = 2713
tags = ["latex:corollary"]
uses = ["d-weights", "def-wf-degree-components", "def-wf-monodromy-data", "def-wf-weil-category", "lem-mg-determinant-monodromy-morphism", "lem-wf-rank-one-algebraic-extension", "lem-wf-schur-scalar"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, put
$|k_0|=q$, fix a real weight character $\lambda$ ([d-weights]), and in the
setting of [def-wf-monodromy-data] let
$\mathcal W_0$ be an irreducible lisse
Weil sheaf of rank $r$ with
representation $\rho_{\mathcal W}$ and with finite geometric
determinant, i.e. $\det\rho_{\mathcal W}(\pi_1(X))$ finite, and let
$z\in G^{[m]}(\Qlb)$ be an algebraic-monodromy element of positive
degree $m$ which is central in
$G_{\mathrm{arith}}(\rho_{\mathcal W})$ (an element furnished by
[lem-mg-common-positive-central-element] when $\mathcal W_0$ is a
summand of a semisimple sheaf). The matrix of $z$ commutes with
the Weil-group image on the fiber $W$, because $z$ is central and
the Weil image is contained in the arithmetic monodromy group. Since
$\mathcal W_0$ is Weil-irreducible,
[lem-wf-schur-scalar] gives a scalar $c_W\in\Qlb^\times$ by which
$z$ acts. Its
determinant weight is then

$$
\dw_\lambda(\mathcal W_0)=\frac{\lambda(c_W)}{m};
$$

in particular, for $\lambda=\lambda_\iota$ and a degree-one $s$,

$$
\frac{2\log_q|\iota(\det\rho_{\mathcal W}(s))|}{r}=\frac{2\log_q|\iota(c_W)|}{m},
$$

where $\log_q$ is the base-$q$ logarithm. The determinant weight
$\dw_\lambda(\mathcal W_0)$ does not depend on the degree-one element $s$.

## Proof

Let $\chi_{\det}=\det\circ\rho_{\mathcal W}:W(X_0)\to\Qlb^\times$ be the
character of the rank-one determinant sheaf $\det\mathcal W_0$, and let
$s$ be a degree-one element of the Weil group with $c=\chi_{\det}(s)$.
The determinant of the scalar $c_W$ on the $r$-dimensional fiber is
$c_W^{r}$. The morphism
$\Delta_{\rho_{\mathcal W}}$ of
[lem-mg-determinant-monodromy-morphism] sends $z$ to a central
degree-$m$ element $\Delta(z)$ of the arithmetic monodromy group of the
rank-one determinant sheaf, whose matrix is $c_W^r$. The group
$A=\chi_{\det}(\pi_1(X))$ is finite by hypothesis, so
[lem-wf-rank-one-algebraic-extension] applies: in the notation of
[def-wf-degree-components],
$G_{\mathrm{arith}}(\chi_{\det})=A\times\mathbf Z$ and
$\Delta(z)=(a,m)$ with $a\in A$, whose image is

$$
c_W^r=a\,c^m .
$$

The element $a$ has finite order, and a real weight character kills
finite-order elements: if $a^e=1$ with $e>0$, then
$e\lambda(a)=\lambda(a^e)=0$. Applying $\lambda$ therefore gives
$r\lambda(c_W)=m\lambda(c)$, that is,

$$
\frac{\lambda(c_W)}{m}=\frac{\lambda(c)}{r}=\dw_\lambda(\mathcal W_0)
$$

by the definition in [d-weights]. Replacing $s$ by $us$ with
$u\in\pi_1(X)$ multiplies $c$ by the finite-order element
$\chi_{\det}(u)\in A$, which $\lambda$ kills; this proves independence of
the degree-one lift. The case $\lambda=\lambda_\iota$ is the second
display.
