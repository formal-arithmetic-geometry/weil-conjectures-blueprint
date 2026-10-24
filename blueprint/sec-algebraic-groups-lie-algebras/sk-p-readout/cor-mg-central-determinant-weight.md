+++
id = "cor-mg-central-determinant-weight"
kind = "theorem"
title = "Central element determines the determinant weight"
order = 3773
tags = ["latex:corollary"]
uses = ["d-monodromy", "d-weights", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "def-wf-monodromy-data", "lem-mg-degree-component-functoriality", "lem-mg-determinant-monodromy-morphism", "lem-wf-schur-scalar"]
+++
Fix a real weight character $\lambda$ ([d-weights]). Let
$\rho:W\to\operatorname{GL}(V)$ be a represented degree datum over a
field $k$ ([d-monodromy]), with the monodromy data of
[def-wf-monodromy-data], computed with the chosen degree-one element
$s$, and let $z=(h,m)\in G^{[m]}(k)$ be an algebraic-monodromy element of
positive degree $m$ which is central in $G_{\mathrm{arith}}(\rho)$ (such
an element exists when $\rho$ is semisimple and $k$ is algebraically
closed of characteristic zero). Let $Q\neq0$ be a $W$-stable subquotient of $V$, or more
generally any of the tensor, exterior-power or iterated-subquotient
constructions of [lem-mg-degree-component-functoriality], of rank $r$,
with Weil representation $\rho_Q$, with finite geometric determinant,
i.e. $\det\rho_Q(P)$ finite, and with the homomorphism
$\Phi_Q:G_{\mathrm{arith}}(\rho)\to G_{\mathrm{arith}}(\rho_Q)$ of that
lemma. The representation $Q$ need not be irreducible or semisimple.
Say that $z$ *acts on $Q$ as a scalar* $c_Q\in k^\times$ if the matrix
of $\Phi_Q(z)$ under the matrix map $(h',n)\mapsto h'\rho_Q(s)^n$ of
[def-wf-arithmetic-monodromy-extension] is $c_Q\,1_Q$. If $z$ acts on
$Q$ as a scalar $c_Q$, then

$$
\dw_\lambda(Q)=\frac{\lambda(c_Q)}{m}.
$$

The scalar-action hypothesis holds whenever $Q$ is irreducible.
In particular, for an irreducible Weil representation $\rho_{\mathcal W}$
of rank $r$ with finite geometric determinant, and $z\in G^{[m]}$
central in $G_{\mathrm{arith}}(\rho_{\mathcal W})$ (the case $V=Q$,
$\Phi_Q$ the identity), $z$ acts by a scalar $c_W$ and

$$
\dw_\lambda(\rho_{\mathcal W})=\frac{\lambda(c_W)}{m};
$$

for $k=\Qlb$, an embedding $\iota:\Qlb\hookrightarrow\mathbf C$, $q>1$
and $\lambda=\lambda_\iota$ this reads

$$
\frac{2\log_q|\iota(\det\rho_{\mathcal W}(s))|}{r}=\frac{2\log_q|\iota(c_W)|}{m},
$$

where $\log_q$ is the base-$q$ logarithm. The determinant weight
$\dw_\lambda(Q)$ does not depend on the degree-one element used to
define it in [d-weights].
