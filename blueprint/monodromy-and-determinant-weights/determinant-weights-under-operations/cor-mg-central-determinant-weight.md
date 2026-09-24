+++
id = "cor-mg-central-determinant-weight"
kind = "theorem"
title = "Central element determines the determinant weight"
order = 4119
tags = ["latex:corollary"]
uses = ["cor-wf-rank-one-punctual-purity-curve", "def-wf-degree-components", "def-wf-determinantal-weight", "def-wf-monodromy-data", "def-wf-weil-category", "lem-mg-determinant-monodromy-morphism", "lem-wf-determinantal-weight-exists", "lem-wf-rank-one-component-modulus", "lem-wf-schur-scalar", "prop-wf-positive-degree-centre", "thm-wf-rank-one-finite-geometric-image-curve"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, put
$|k_0|=q$, fix $\iota:\Qlb\xrightarrow{\sim}\mathbf C$, and in the
setting of [def-wf-monodromy-data] let
$\mathcal W_0$ be an irreducible lisse
Weil sheaf of rank $r$ with
representation $\rho_{\mathcal W}$, and let
$z\in G^{[m]}(\Qlb)$ be an algebraic-monodromy element of positive
degree $m$ which is central in
$G_{\mathrm{arith}}(\rho_{\mathcal W})$ (an element furnished by
[prop-wf-positive-degree-centre] when the geometric monodromy
identity component is semisimple). The matrix of $z$ commutes with
the Weil-group image on the fiber $W$, because $z$ is central and
the Weil image is contained in the arithmetic monodromy group. Since
$\mathcal W_0$ is Weil-irreducible,
[lem-wf-schur-scalar] gives a scalar $c_W\in\Qlb^\times$ by which
$z$ acts. Its
determinant weight is then

$$
\dw_\iota(\mathcal W_0)=\frac{2\log_q|\iota(c_W)|}{m},
$$

where $\log_q$ is the base-$q$ logarithm.

## Proof

Let $\chi_{\det}:W(X_0)\to\Qlb^\times$ be the character of the
rank-one determinant sheaf $\det\mathcal W_0$, and let $s$ be a
degree-one element of the Weil group with $c=\chi_{\det}(s)$.
The determinant of the scalar $c_W$ on the $r$-dimensional fiber is
$c_W^{r}$. The morphism
$\Delta_{\rho_{\mathcal W}}$ of
[lem-mg-determinant-monodromy-morphism] sends $z$ to a central
degree-$m$ element of the arithmetic monodromy group of the rank-one
determinant sheaf, whose associated scalar is $c_W^r$. By the curve finiteness theorem
[thm-wf-rank-one-finite-geometric-image-curve], the component-modulus
lemma applies. The rank-one
modulus identity of
[lem-wf-rank-one-component-modulus] applied to $\det(z)$
gives

$$
|\iota(c_W)|^{r}=|\iota(\chi_{\det}(s))|^{m}.
$$

By [lem-wf-determinantal-weight-exists] and
[def-wf-determinantal-weight] the determinant weight is
$a/r$ with $a$ the weight of the rank-one sheaf
$\det\mathcal W_0$, and
[cor-wf-rank-one-punctual-purity-curve] gives

$$
a=2\log_q|\iota(\chi_{\det}(s))|
\qquad\text{whence}\qquad
\dw_\iota(\mathcal W_0)=\frac{a}{r}=\frac{2\log_q|\iota(c_W)|}{m}.
$$
