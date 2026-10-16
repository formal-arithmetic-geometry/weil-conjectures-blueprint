+++
id = "thm-pod-degreewise-perfectness-over-a-field"
kind = "theorem"
title = "Degreewise perfectness over a field"
lean = ["AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_adicConstant"]
order = 2784
uses = ["def-pod-derived-poincare-pairing", "def-pod-perfect-complex-on-x", "def-pod-perfect-point-complex", "def-weil-finite-coefficient-point", "lem-pod-cohomology-of-dual-over-field", "lem-pod-perfect-point-complex-field", "prop-pod-degree-of-the-pairing", "thm-pod-derived-poincare-duality", "thm-pod-point-perfectness"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), fix the field stage $\Lambda \in \{ E,\overline{\mathbf Q}_{\ell }\}$ of the datum (with the finite coefficient groups $H^i_c(X,K)$, $H^i(X,K)$); let $K\in D^b_{ctf}(X,\Lambda )$ be perfect over $\Lambda _X$ in the sense of [def-pod-perfect-complex-on-x], and let $\langle -,-\rangle _i$ denote the degreewise pairings of [prop-pod-degree-of-the-pairing],

$$
\langle -,-\rangle _i:\   H_c^i(X,K)\times H^{2d-i}\bigl(X,K^\vee (d)\bigr)\longrightarrow \Lambda ,
$$

obtained by decomposing the degree-zero part of the derived Poincare pairing $\beta _K$ of [def-pod-derived-poincare-pairing]. Then all cohomology spaces in the displays of [prop-pod-degree-of-the-pairing] are finite-dimensional, and each map

$$
H^{2d-i}\bigl(X,K^\vee (d)\bigr) \xrightarrow {\  \sim \  }H_c^i(X,K)^\vee
$$

– the adjoint of $\langle -,-\rangle _i$, the right side being the ordinary dual of a finite-dimensional $\Lambda$-vector space – is an isomorphism; equivalently each bilinear pairing $\langle -,-\rangle _i$ is perfect, and the line-valued pairing $H_c^i(X,K)\times H^{2d-i}(X,K^\vee )\to \Lambda (-d)$ is perfect degreewise.
