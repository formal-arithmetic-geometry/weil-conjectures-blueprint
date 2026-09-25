+++
id = "thm-weil-cohomological-finiteness-verified"
kind = "theorem"
title = "Verification of Cohomological finiteness and Frobenius"
order = 3083
tags = ["latex:proposition"]
uses = ["def-trf-frobenius-operators", "def-weil-algebraically-closed-coefficients", "def-weil-derived-cohomology-sheaves", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-weil-sheaf-complex", "lem-sc-cohomological-dimension", "prop-trf-compact-support-perfectness", "prop-weil-operations", "prop-weil-proper-compact-coincidence", "thm-pod-degreewise-perfectness-over-a-field", "thm-pod-point-perfectness", "thm-weil-cohomological-finiteness"]
+++
The interface [thm-weil-cohomological-finiteness] of the framework chapter is verified as follows.

## Proof

*Step 1: boundedness, finite-dimensionality, and the Frobenius
action.* The complexes $R\Gamma(Y,K)$ and $R\Gamma_c(Y,K)$ and
their global geometric-Frobenius endomorphisms are those of
[def-weil-ordinary-compact-cohomology] and
[def-weil-global-geometric-frobenius], applied to the Weil
complex of [def-weil-weil-sheaf-complex]; the equivariant
realizations are induced by [prop-weil-operations], which
delineates the functoriality of the lifted operations and of the
Frobenius-equivariant maps on cohomology. At the finite coefficient
stage, the compact-support global sections of a finite-Tor
constructible object are bounded with finite-amplitude cohomology
modules by [prop-trf-compact-support-perfectness]; at the
$\mathcal O_E$-, $E$-, and $\Qlb$-stages the same functors
produce perfect point complexes in the sense of
[thm-pod-point-perfectness] – bounded with finite cohomology
modules (respectively finite-dimensional spaces at the field stages) –
and [thm-pod-degreewise-perfectness-over-a-field]
gives the finite-dimensionality degreewise. The object $K$ of the
statement is represented at a finite stage $E/\Ql$ by
[def-weil-algebraically-closed-coefficients], so the displayed
conclusions hold for it: there are $u\leq v$ with
$H_c^i(Y,K)=0$ outside $[u,v]$, each $H_c^i(Y,K)$ is
finite-dimensional over $\Qlb$, and the Weil structure induces the
functorial Frobenius automorphism.

*Step 2: the proper case.* For proper $Y_0$, the canonical
map $R\Gamma_c(Y,K)\to R\Gamma(Y,K)$ is the comparison of
[prop-weil-proper-compact-coincidence], whose
Frobenius-equivariance is the compatibility of the compact-support and
ordinary constructions recorded in
[def-weil-ordinary-compact-cohomology] together with the
equivariance of [prop-weil-operations].

*Step 3: the constant sheaf on a scheme of dimension $e$.*
The vanishing range $[0,2e]$ for the constant Weil sheaf
$(\Qlb)_Y$ of [def-weil-weil-sheaf-complex] on the
geometric fiber $Y$ of dimension $e$ is the cohomological-dimension
bound $\operatorname{cd}(X)\leq2\dim X$ for schemes of finite type
over an algebraically closed field, recorded in the blueprint for
dimension one in [lem-sc-cohomological-dimension] (with its
source notes: Stacks Project, Etale Cohomology, Section 59.95,
Tags [0F0P](https://stacks.math.columbia.edu/tag/0F0P) and
[0F0V](https://stacks.math.columbia.edu/tag/0F0V), for the affine
bound $\operatorname{cd}(X)\leq\dim X+\operatorname{cd}(K)$ with
$\operatorname{cd}(k)=0$, and the reduction of that lemma for the
finite-type case); the same bound for all $e$, also for compact
supports, is the recorded input of Deligne, *La conjecture de
Weil. I*, Publ. Math. IHES 43 (1974), (1.3). Degrees
$i<0$ are excluded by the t-structure on the pro-etale derived
category, whose nonpositive part is described in
[def-weil-derived-cohomology-sheaves] on the small pro-etale site
of [def-weil-pbc-proetale-site].

*Step 4: degree zero for a geometrically connected fiber.*
For geometrically connected $Y_0$ the scheme $Y$ is connected
([def-weil-geometric-hypotheses]), and the constant sheaf
$(\Qlb)_Y$ of [def-weil-pbc-proetale-site] is the
sheafification of the constant presheaf, so
$H^0(Y,(\Qlb)_Y)=\Gamma(Y,(\Qlb)_Y)=\Qlb$. Its canonical Weil
structure makes the local geometric Frobenius operators the identities
on the one-dimensional stalks
([def-trf-frobenius-operators]), and the global operator of
[def-weil-global-geometric-frobenius] on this degree is induced
by the canonical identification $\theta_K$,
hence is the identity of the one-dimensional space
$\Qlb=H^0(Y,(\Qlb)_Y)$: this is the last clause of the statement.
