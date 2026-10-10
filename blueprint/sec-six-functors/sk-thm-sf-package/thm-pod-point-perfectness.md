+++
id = "thm-pod-point-perfectness"
kind = "theorem"
title = "Point perfectness of global sections"
order = 2249
uses = ["cor-sf-direct-image-ctf-proetale", "def-coef-normalized-dvr-tower", "def-compact-support-direct-image-detailed", "def-pod-conventions", "def-pod-perfect-point-complex", "def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-finite-coefficient-point", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-integral-rational-qbar-compact-support", "def-weil-ordinary-compact-cohomology", "def-weil-rationalization-karoubi", "lem-coef-finite-direct-image", "lem-coef-integral-compact-support", "lem-coef-integral-residue-tor", "lem-coef-normalized-dvr-effectivity", "lem-trf-finite-tor-amplitude-perfect", "prop-trf-compact-support-perfectness"]
+++
Fix the finite-field datum and the coefficient stages
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$ of the Poincare duality
conventions [def-pod-conventions], but let $X_0$ be an arbitrary
separated finite-type $k_0$-scheme: neither properness nor smoothness
of $X_0$ is assumed. Put $X=X_0\times_{k_0}k$, let
$a_X:X\to s=\Spec k$ be the structure morphism, and let
$d\geq\dim X$. Let $K\in D^b_{ctf}(X,\Lambda )$. Then the four
complexes

$$
R\Gamma (X,K),\qquad R\Gamma _c(X,K),\qquad R\Gamma (X,K)^\vee,\qquad R\Gamma _c(X,K)^\vee
$$

are perfect point complexes at every coefficient stage, in the
following sense.

1. At finite level $\Lambda=A=A_{E,n}$ they are bounded with finite
cohomology modules and finite Tor amplitude, i.e. quasi-isomorphic to
bounded complexes of finite free $A$-modules
([def-pod-perfect-point-complex]). If $K$ has Tor amplitude in
$[a,b]$, then $R\Gamma(X,K)$ and $R\Gamma_c(X,K)$ have Tor amplitude
in $[a,b+2d]$ and their duals in $[-b-2d,-a]$.
1. At the stage $\mathcal O_E$ they lie in
$D^b_{\mathrm{fg}}(\mathcal O_E)$ and are perfect; their reductions
modulo $\varpi_E^n$ are the corresponding finite-level complexes of the
reductions $K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$, and these are
perfect with one common amplitude independent of $n$.
1. At the stages $E$ and $\Qlb$ they are bounded with
finite-dimensional cohomology.

If $X_0$ is proper, the canonical comparison
$R\Gamma_c(X,K)\xrightarrow{\sim}R\Gamma(X,K)$ of
[def-weil-ordinary-compact-cohomology] identifies the two cases; in
particular this applies in the fixed setting of
[def-pod-conventions].
