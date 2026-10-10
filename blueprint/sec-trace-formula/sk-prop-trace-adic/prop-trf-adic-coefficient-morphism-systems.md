+++
id = "prop-trf-adic-coefficient-morphism-systems"
kind = "theorem"
title = "Adic realization for systems of Frobenius coefficient morphisms"
order = 2386
tags = ["latex:proposition"]
uses = ["def-trf-adic-system", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-trf-frobenius-coefficient-morphism", "def-weil-derived-complete-integral-detailed", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber", "def-weil-integral-rational-qbar-compact-support", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-completed-pullback", "def-weil-pbc-derived-inverse-limit", "lem-fix-compact-support-coefficient-change", "lem-trf-chain-supertrace", "prop-trf-compact-support-perfectness", "prop-trf-graph-frobenius-operator", "prop-trf-rational-frobenius-integral-model", "prop-trf-scheme-galois-comparison", "prop-trf-trace-formal-laws", "thm-trf-finite-coefficient-map"]
+++
Fix the global finite-field datum $p,a,q,k_0,k$ and the coefficient
conventions of [def-trf-coefficient-conventions], with
$A_n=A_{E,n}=\mathcal O_E/\varpi^n$ and $k_E=A_1$. Let $X_0$ be a separated
finite-type $k_0$-scheme, $X=X_0\times_{k_0}k$, $\Phi$ the $q$-power scheme
Frobenius, $g_\gamma$ the geometric-Frobenius automorphism and
$\kappa^{(m)}:L\Phi^{m*}\xrightarrow{\sim}Lg_\gamma^{m*}$ the comparison of
[prop-trf-scheme-galois-comparison].

Let $K_\bullet=(K_n)_{n\geq1}$ be a normalized $A_\bullet$-system of
[def-trf-adic-system], $K_n\in D^b_{ctf}(X,A_n)$, with normalization
isomorphisms $\nu_n:K_{n+1}\otimes^L_{A_{n+1}}A_n\xrightarrow{\sim}K_n$; no
Weil structure is assumed. A *compatible system of Frobenius coefficient
morphisms* on $K_\bullet$ is a family of Frobenius coefficient morphisms
$\psi_n:L\Phi^*K_n\to K_n$ of [def-trf-frobenius-coefficient-morphism]
such that
$$
\nu_n\circ(\psi_{n+1}\otimes^L_{A_{n+1}}A_n)=\psi_n\circ L\Phi^*(\nu_n)\circ\mu_n
\qquad(n\geq1),
$$
where $\mu_n:(L\Phi^*K_{n+1})\otimes^L_{A_{n+1}}A_n\xrightarrow{\sim}
L\Phi^*(K_{n+1}\otimes^L_{A_{n+1}}A_n)$ is the monoidality of pullback
([def-weil-derived-pullback-tensor-hom]); no invertibility is assumed.
Examples: the scheme-Frobenius maps $\varphi_n\circ\kappa_{K_n}$ of a system
with a strict Weil structure at every level, and the systems
$\psi_n=u_n\circ\kappa_{K_n}$ of [prop-trf-rational-frobenius-integral-model],
item (2), attached to a lattice $K_{\mathcal O}$ and a clearing of
denominators $\varphi_E=\varpi^{-N}u$.

Put, for a geometric point $\bar y$ of $X$,
$$
P_n=R\Gamma_c(X,K_n),\qquad P_{\bar y,n}=(K_n)_{\bar y},\qquad
P_{\mathcal O}=R\!\varprojlim_nP_n,\qquad
P_{\bar y,\mathcal O}=R\!\varprojlim_nP_{\bar y,n},
$$
the derived limits of [def-weil-pbc-derived-inverse-limit] of the towers
in $D(\mathcal O_E)$ (via the point identification of
[def-weil-finite-coefficient-point]) whose transition maps are the
composites $P_{n+1}\to P_{n+1}\otimes^L_{A_{n+1}}A_n\xrightarrow{\sim}P_n$ of
item (1) below, with projections $\mathrm{pr}_n$. If $K_\bullet$ is the
reduction tower $K_n=K_{\mathcal O}\otimes^L_{\mathcal O_E}A_n$ of an integral
object $K_{\mathcal O}$ ([def-weil-derived-complete-integral-detailed],
[def-weil-pbc-adic-coefficient-datum]), then
$P_{\mathcal O}=R\Gamma_c(X,K_{\mathcal O})$ by
[def-weil-integral-rational-qbar-compact-support] and
$P_{\bar y,\mathcal O}=L\bar y^*_{\mathrm{comp}}K_{\mathcal O}=:K_{\mathcal O,\bar y}$
is the completed stalk of [def-weil-pbc-completed-pullback].

Call a family $f_\bullet=(f_n)$ of endomorphisms $f_n$ of $P_n$
*compatible* if $f_n$ corresponds to $f_{n+1}\otimes^L_{A_{n+1}}A_n$ under
the isomorphisms of item (1), and call an endomorphism $V$ of $P_{\mathcal O}$
in $D(\mathcal O_E)$ a *lift* of $f_\bullet$ if
$\pi_n\circ(V\otimes^L_{\mathcal O_E}A_n)=f_n\circ\pi_n$ for all $n$, where
$\pi_n:P_{\mathcal O}\otimes^L_{\mathcal O_E}A_n\to P_n$ is the
$A_n$-linear map adjoint to $\mathrm{pr}_n$; likewise for the stalks. Then:

1. *Levelwise perfectness and normalization.* Each $P_n$ and $P_{\bar y,n}$ lies
in $D^b_{\mathrm{fin}}(A_n)$, and $\nu_n$ induces isomorphisms
$P_{n+1}\otimes^L_{A_{n+1}}A_n\xrightarrow{\sim}P_n$ and
$P_{\bar y,n+1}\otimes^L_{A_{n+1}}A_n\xrightarrow{\sim}P_{\bar y,n}$.
1. *Integral realization and lifts.* $P_{\mathcal O}$ and
$P_{\bar y,\mathcal O}$ are represented by bounded complexes of finite free
$\mathcal O_E$-modules, and every $\pi_n$ is an isomorphism. Every
compatible family of endomorphisms has a lift, and every $V$ with
$\mathrm{pr}_n\circ V=f_n\circ\mathrm{pr}_n$ for all $n$ (for instance the
derived limit of a morphism of towers) is a lift of $f_\bullet$.
1. *Compatibility of the Frobenius operators.* For every $m\geq1$ the global
operators $F_{c,m}(\psi_n)=T_{c_m}(\psi_{n,m})$ of
[def-trf-frobenius-coefficient-morphism] form a compatible family on
$(P_n)$, and for $y\in X_0(\mathbf F_{q^m})$ with geometric point $\bar y$
the stalk endomorphisms $\psi_{n,m,\bar y}=(\psi_{n,m})_{\bar y}\circ\iota_{K_n}$
(normalized as in [prop-trf-rational-frobenius-integral-model]) form a
compatible family on $(P_{\bar y,n})$.
1. *Traces.* If $V$ lifts the compatible family $f_\bullet$, then the
categorical trace $\operatorname{tr}_{\mathcal O_E}(V\mid P_{\mathcal O})$
reduces modulo $\varpi^n$ to $\operatorname{tr}_{A_n}(f_n\mid P_n)$ for
every $n$; hence
$$
\operatorname{tr}_{\mathcal O_E}(V\mid P_{\mathcal O})
=\bigl(\operatorname{tr}_{A_n}(f_n\mid P_n)\bigr)_n\in\varprojlim_nA_n=\mathcal O_E,
$$
independently of the lift. In particular the elements
$\operatorname{tr}_{\mathcal O_E}\bigl(F_{c,m}(\psi_\bullet)\mid P_{\mathcal O}\bigr)$
and
$\operatorname{tr}_{\mathcal O_E}\bigl(\psi_{\bullet,m,\bar y}\mid P_{\bar y,\mathcal O}\bigr)$,
the traces of any lifts of the families of item (3), are well defined.

Here $\operatorname{tr}_{\mathcal O_E}$ is the categorical trace of
[def-trf-categorical-trace] formed over the commutative ring
$\mathcal O_E$, with the duality data of [lem-trf-chain-supertrace].
