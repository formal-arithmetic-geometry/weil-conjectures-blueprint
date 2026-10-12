+++
id = "thm-trf-trace-formula-e"
kind = "theorem"
title = "Trace formula over a finite extension"
order = 2700
uses = ["def-trf-adic-system", "def-trf-admissibility", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-weil-cohomological-support", "def-weil-derived-complete-integral-detailed", "def-weil-finite-field-fiber", "def-weil-integral-rational-qbar-compact-support", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-rational-category", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "lem-trf-chain-supertrace", "prop-trf-adic-coefficient-morphism-systems", "prop-trf-rational-frobenius-integral-model", "prop-trf-trace-formal-laws", "prop-weil-pbc-rational-transport", "thm-trf-coefficient-morphism-trace-formula", "thm-trf-integral-adic-coefficient-morphism-trace-formula"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and the
coefficient conventions of [def-trf-coefficient-conventions], with
$A_n=A_{E,n}=\mathcal O_E/\varpi^n$. Let $X_0$ be
separated finite-type
over $k_0$ ([def-weil-scheme-morphism-properties]), put
$X=X_0\times_{k_0}k$, let
$K_E\in D^b_c(X,E)$ be an object of the
rationalized
$E$-coefficient category ([def-weil-rationalization-karoubi],
[def-weil-pbc-rational-category]), and let

$$
\varphi_E:Lg_\gamma^*K_E\longrightarrow K_E
$$

be an arbitrary morphism of $D^b_c(X,E)$, for instance the Weil
structure of an $E$-Weil complex. No invertibility of $\varphi_E$, no
invertibility of a rescaling $c\,\varphi_E$ on a lattice, and no
integral Weil presentation is assumed. Let $F^{\,m}_{c,K_E}$ on
$R\Gamma_c(X,K_E)$ and $F_{y,m}$ on $K_{E,\bar y}$ be the $E$-stage
Frobenius operators of $(K_E,\varphi_E)$ defined in
[prop-trf-rational-frobenius-integral-model] (the stalk being
$K_{\mathcal O,\bar y}\otimes_{\mathcal O_E}E$ for a lattice
$K_{\mathcal O}$, as there).

*Lattice and finite-level hypotheses.* Let $K_{\mathcal O}\in
D^b_c(X,\mathcal O_E)$ ([def-weil-derived-complete-integral-detailed])
together with an isomorphism $\alpha:K_{\mathcal O}\xrightarrow{\sim}K_E$
of $D^b_c(X,E)$ be a lattice of $K_E$. One always exists: the objects of
$D^b_c(X,E)$ are those of $D^b_c(X,\mathcal O_E)$, so one may take
$K_{\mathcal O}=K_E$ and $\alpha=\operatorname{id}$. Put
$K_n=K_{\mathcal O}\otimes^L_{\mathcal O_E}A_n$. Assume at every finite
level $n$ the finite-level hypotheses of
[thm-trf-coefficient-morphism-trace-formula] for $K_n$. These are an
explicit etale-origin witness for $K_n$
([def-weil-pbc-etale-origin-witness]) and the exceptional-adjoint
admissibility of [def-trf-admissibility] for the graph correspondences of
the iterates $\Phi^m$ and the fixed-point base changes on a chosen
compactification defined over $k_0$. They concern $K_n$ and the geometry
of $X_0$ only, not $\varphi_E$.

Then the $E$-vector spaces $H_c^i(X,K_E)$ and $H^j(K_{E,\bar y})$ are
finite-dimensional and nonzero for only finitely many $i$, $j$, and for
every $m\geq1$,

$$
\sum_{i\in\mathbf Z}(-1)^i
\operatorname{Tr}\bigl(F_{c,K_E}^m\mid H_c^i(X,K_E)\bigr)
=
\sum_{y\in X_0(\mathbf F_{q^m})}
\sum_{j\in\mathbf Z}(-1)^j
\operatorname{Tr}\bigl(F_{y,m}\mid H^j(K_{E,\bar y})\bigr)
$$

in $E$. For any clearing of denominators $\varphi_E=\varpi^{-N}u$ on the
lattice, the two sides are $\varpi^{-Nm}$ times the images under
$\mathcal O_E\to E$ of the two sides of the integral identity of
[thm-trf-integral-adic-coefficient-morphism-trace-formula], item (2), and
they agree with the corresponding $E$-valued categorical traces by the
supertrace law over the field $E$ of [prop-trf-trace-formal-laws].

This covers the Weil structure of every $E$-Weil complex. It also covers
Weil maps that are not invertible after any rescaling on any lattice, such
as $\varphi_E=\operatorname{diag}(1,\ell)$ on $E^2$ over
$X_0=\Spec\mathbf F_q$ (the example of
[prop-trf-rational-frobenius-integral-model]).
