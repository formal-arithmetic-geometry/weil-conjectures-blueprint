+++
id = "cor-mg-central-determinant-weight"
kind = "theorem"
title = "Central element determines the determinant weight"
order = 2901
tags = ["latex:corollary"]
uses = ["d-weights", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "def-wf-monodromy-data", "def-wf-weil-category", "lem-mg-degree-component-functoriality", "lem-mg-determinant-monodromy-morphism", "lem-wf-rank-one-algebraic-extension", "lem-wf-schur-scalar"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, put
$|k_0|=q$, and fix a real weight character $\lambda$ ([d-weights]). Let
$\rho:W(X_0)\to\operatorname{GL}(V)$ be the representation of a lisse
Weil sheaf, with the monodromy data of [def-wf-monodromy-data], computed
with one fixed degree-one element $s$, and let
$z=(h,m)\in G^{[m]}(\Qlb)$ be an algebraic-monodromy element of positive
degree $m$ which is central in $G_{\mathrm{arith}}(\rho)$ (such an
element exists when $\rho$ is semisimple). Let $Q\neq0$ be a Weil-stable subquotient of $V$, or more
generally any of the tensor, exterior-power or iterated-subquotient
constructions of [lem-mg-degree-component-functoriality], of rank $r$,
with Weil representation $\rho_Q$, with finite geometric determinant,
i.e. $\det\rho_Q(\pi_1(X))$ finite, and with the homomorphism
$\Phi_Q:G_{\mathrm{arith}}(\rho)\to G_{\mathrm{arith}}(\rho_Q)$ of that
lemma. The representation $Q$ need not be irreducible or semisimple.
Say that $z$ *acts on $Q$ as a scalar* $c_Q\in\Qlb^\times$ if the matrix
of $\Phi_Q(z)$ under the matrix map $(h',n)\mapsto h'\rho_Q(s)^n$ of
[def-wf-arithmetic-monodromy-extension] is $c_Q\,1_Q$. If $z$ acts on
$Q$ as a scalar $c_Q$, then

$$
\dw_\lambda(Q)=\frac{\lambda(c_Q)}{m}.
$$

The scalar-action hypothesis holds whenever $Q$ is Weil-irreducible.
In particular, for an irreducible lisse Weil sheaf $\mathcal W_0$ of rank
$r$ with representation $\rho_{\mathcal W}$ and finite geometric
determinant, and $z\in G^{[m]}$ central in
$G_{\mathrm{arith}}(\rho_{\mathcal W})$ (the case $V=Q$, $\Phi_Q$ the
identity), $z$ acts by a scalar $c_W$ and

$$
\dw_\lambda(\mathcal W_0)=\frac{\lambda(c_W)}{m};
$$

for $\lambda=\lambda_\iota$ this reads

$$
\frac{2\log_q|\iota(\det\rho_{\mathcal W}(s))|}{r}=\frac{2\log_q|\iota(c_W)|}{m},
$$

where $\log_q$ is the base-$q$ logarithm. The determinant weight
$\dw_\lambda(Q)$ does not depend on the degree-one element used to
define it in [d-weights].
