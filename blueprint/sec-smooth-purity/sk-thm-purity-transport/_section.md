+++
id = "sk-thm-purity-transport"
kind = "theorem"
title = "Smooth purity over $\\mathcal O_E$, $E$ and $\\overline{\\mathbf Q}_\\ell$"
order = 2364
uses = ["sk-def-purity-conv", "sk-lem-sf-flat-model", "sk-prop-a1", "sk-prop-cohsm", "sk-thm-smooth-purity"]
lean = ["AlgebraicGeometry.Etale.derivedCompleteIntegral_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Keep the geometric conventions of [sk-def-purity-conv], but let the
coefficient ring range over the remaining three stages

$$
\Lambda\in\{\mathcal O_E,\ E,\ \overline{\mathbf Q}_\ell\},
$$

where $D^b_{ctf}(-,\mathcal O_E)$ is the adic category of normalized
systems $(K_n)_n$ with $K_n\in D^b_{ctf}(-,A_{E,n})$ and common bounds and
stratifications, $D^b_{ctf}(-,E)$ its rationalization, and
$D^b_{ctf}(-,\overline{\mathbf Q}_\ell)$ the colimit over finite
$E/\mathbf Q_\ell$. Let $f:X\to Y$ be smooth separated
of relative dimension $d$ and let $K\in D^b_{ctf}(Y,\Lambda)$. Then the
purity map

$$
\gamma_{f,K}:Lf^{*}K(d)[2d]\ \xrightarrow{\ \sim\ }\ Rf^{!}K
$$

extends the finite-coefficient isomorphism of [sk-thm-smooth-purity]
to these stages, naturally in $K$ and
compatibly with composition, étale base change, the finite reductions
$A_{E,n}\to A_{E,m}$ and scalar extension of coefficient fields. In
particular, for the structure morphism $a_X$ of a smooth $X$ of pure
dimension $d$,

$$
\omega_{X,\Lambda}=Ra_X^{!}\Lambda\ \cong\ \Lambda_X(d)[2d],
$$

and the counit of $Ra_{X!}\dashv Ra_X^{!}$ is the normalized integration
map $R\Gamma_c(X,\Lambda_X(d)[2d])\to\Lambda$.
The coefficient compatibilities and this counit normalization also hold
for the finite-coefficient isomorphisms of [sk-thm-smooth-purity].
