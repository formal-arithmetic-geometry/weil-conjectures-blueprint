+++
id = "sk-thm-sf-pf-adic"
kind = "section"
title = "Projection formula: the derived-complete stage"
order = 2095
uses = ["sk-def-sf-operations", "sk-prop-sf-pf-reduction"]
lean = ["AlgebraicGeometry.Etale.hasProjectionFormula_of_derivedCompleteIntegral"]
+++
*Theorem (sketch).*

Let $E/\Ql$ be a finite extension inside $\Qlb$ with ring of integers
$\mathcal O_E$, let $f:X\to Y$ be a morphism of schemes admitting a
compactification, with $Rf_!$ formed from the chosen compactification, and
let $K\in D(X_{\Et},\mathcal O_E)$, $L\in D(Y_{\Et},\mathcal O_E)$ be
complexes of étale sheaves of $\mathcal O_E$-modules that are derived
complete with respect to the maximal ideal of $\mathcal O_E$ and of finite
Tor amplitude, with finite reductions $K_n,L_n$. Then the projection map

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L L\longrightarrow Rf_!\bigl(K\otimes^L Lf^*L\bigr)
$$

is an isomorphism.

## Proof

Write $\varpi$ for a uniformizer of $\mathcal O_E$ and
$\rho_n=-\otimes^L_{\mathcal O_E}\mathcal O_E/\varpi^n$ for reduction, so that
$K_n=\rho_nK$ and $L_n=\rho_nL$ are complexes of sheaves of
$\mathcal O_E/\varpi^n$-modules, of finite Tor amplitude over
$\mathcal O_E/\varpi^n$ because $K$ and $L$ have finite Tor amplitude over
$\mathcal O_E$.

*Step 1 (reduction of the projection map).* $\mathcal O_E/\varpi^n$ is the
cone of $\varpi^n$ on $\mathcal O_E$, so $\rho_n$ is the cone of
multiplication by $\varpi^n$; it therefore commutes with the triangulated
functors $Rf_!$ and $Lf^*$, and with $\otimes^L$ through the monoidal
structure of scalar extension. Under these identifications
$\rho_n\operatorname{PF}_{f,K,L}=\operatorname{PF}_{f,K_n,L_n}$: this is the
commutativity of the reduction square of [sk-prop-sf-pf-reduction], whose
proof only uses the constructions of the projection map and of the
reduction comparisons, not the boundedness or constructibility of $K$ and
$L$.

*Step 2 (finite levels).* When $K_n$ and $L_n$ are bounded constructible,
$\operatorname{PF}_{f,K_n,L_n}$ is an isomorphism for every $n$ by the
finite-level projection formula [sk-thm-sf-pf-finite]; this is the case
when $K$ and $L$ are derived-complete $\Dctf$-objects over $\mathcal O_E$.

*Step 3 (passage to the limit).* Let $C$ be the cone of
$\operatorname{PF}_{f,K,L}$. By Steps 1 and 2,
$\rho_nC=0$ for all $n$, i.e. multiplication by $\varpi$ is invertible on
$C$. If both source and target of $\operatorname{PF}_{f,K,L}$ are derived
complete, so is $C$, and a derived-complete object on which $\varpi$ is
invertible is $0$ (its derived limit $\Rlim(\cdots\xrightarrow{\varpi}C
\xrightarrow{\varpi}C)$ is both $C$ and $0$); hence
$\operatorname{PF}_{f,K,L}$ is an isomorphism. For derived-complete
$\Dctf$-objects the two sides are derived complete, being the derived limits
of their finite reductions by the uniform-tower reconstruction
(lem:weil-pbc-reconstruction-uniform-tower): finite Tor amplitude of a
derived-complete object is uniform in $n$, so $Rf_!K\otimes^LL$ and
$Rf_!(K\otimes^LLf^*L)$ have uniformly bounded constructible reductions.

*What remains for the statement as given.* The statement assumes only
derived completeness and finite Tor amplitude, with no constructibility or
boundedness. Then Step 2 needs the finite-level projection formula for
unbounded, non-constructible complexes of finite Tor amplitude, and Step 3
needs the derived completeness of $Rf_!K\otimes^LL$ and of
$Rf_!(K\otimes^LLf^*L)$; the derived tensor product of two derived-complete
objects need not be derived complete, and $j_!$ need not preserve derived
completeness. Neither input is available in the blueprint, so in this
generality the argument above is incomplete.
