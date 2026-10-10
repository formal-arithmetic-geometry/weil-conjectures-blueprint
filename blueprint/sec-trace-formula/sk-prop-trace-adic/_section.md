+++
id = "sk-prop-trace-adic"
kind = "proposition"
title = "Adic realization"
order = 2384
uses = ["sk-d-setup", "sk-d-six", "sk-d-weil", "sk-def-sf-weil-complexes", "sk-p-trace-coeff", "sk-prop-sf-trace-perfectness", "sk-thm-sf-ctf-stability"]
lean = ["AlgebraicGeometry.ProEtale.derivedComplete_limit", "AlgebraicGeometry.ProEtale.nonempty_derivedCompletionDiagram_obj_limit_iso", "AlgebraicGeometry.ProEtale.nonempty_rightDerivedLowerShriek_obj_limit_iso", "AlgebraicGeometry.ProEtale.nonempty_leftDerivedUpperStar_obj_limit_iso"]
tags = ["sketch"]
+++
Write $A_n=A_{E,n}$. Call a system
$K_\bullet=(K_n,t_{n+1,n})_{n\ge1}$ with $K_n\in D^b_{ctf}(X,A_n)$
*normalized* if $K_n\otimes^{\mathrm L}_{A_n}A_j\xrightarrow{\sim}K_j$
for $j\le n$, and *uniform* if the $K_n$ share a cohomological range and
Tor amplitude.

1. **(i)** *Realization.* For a normalized uniform system the derived
limit $K_{\mathcal O_E}=R\varprojlim_nK_n$ is derived complete, lies in the
same range, and satisfies
$K_{\mathcal O_E}\otimes^{\mathrm L}_{\mathcal O_E}A_n\cong K_n$ for every
$n$, compatibly with the transitions.
1. **(ii)** *Compact cohomology and stalks.* The systems
$R\Gamma_c(X,K_n)$ and $(K_n)_{\bar y}$ are normalized systems of perfect
$A_n$-complexes, and realization commutes with both:
$$
R\Gamma_c(X,K_{\mathcal O_E})\cong R\varprojlim_nR\Gamma_c(X,K_n),
\qquad
(K_{\mathcal O_E})_{\bar y}\cong R\varprojlim_n(K_n)_{\bar y},
$$
both perfect over $\mathcal O_E$. If moreover $K_\bullet$ is a
*compatible tower of Weil pairs* — isomorphisms
$\varphi_n:\Phi_1^*K_n\xrightarrow{\sim}K_n$ as in [sk-d-weil] at every
level, i.e. strict Weil complexes at $A_n$ in the sense of
[sk-def-sf-weil-complexes], with
$t_{n+1,n}\circ\varphi_{n+1}=\varphi_n\circ\Phi_1^*t_{n+1,n}$ under the
coefficient identifications — or, more generally, carries a compatible
tower of Frobenius coefficient morphisms $\psi_n:\Phi_1^*K_n\to K_n$
satisfying the same compatibility, then the global and local Frobenius
operators of the levels form compatible families of endomorphisms of the
two towers, the realizations carry induced operators, and the displayed
isomorphisms are equivariant for them. For a bare normalized system no
Frobenius structure and no equivariance is asserted: a tower of skyscraper
sheaves at a point of $\mathbf A^1$ not fixed by $\Phi_1$ has moving
support and admits no $\varphi_n$ at any level.
1. **(iii)** *Rationalization and coefficient-field extension.*
$D^b_c(X,E)=D^b_c(X,\mathcal O_E)[1/\varpi]$ has the same objects as the
integral category and morphisms
$\operatorname{Hom}_{\mathcal O_E}(-,-)\otimes_{\mathcal O_E}E$; it is
idempotent complete, and the canonical functor to its Karoubi envelope is an
exact equivalence. Exact $\mathcal O_E$-linear functors and natural
transformations between integral categories transport to the rational ones.
Consequently every $E$-stage object is the rationalization of an integral
system — a lattice — and every $E$-stage morphism is $\varpi^{-N}u$ for
an integral $u$ and some $N$. The $\overline{\mathbf Q}_\ell$-stage is the filtered colimit over
finite $E/\mathbf Q_\ell$, so each of its objects and morphisms is already represented
at a finite stage.
