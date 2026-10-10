+++
kind  = "proof"
of    = "prop-integral-recovery"
+++
The terminal realization-independent factor interface
[thm-weil-realization-independence] supplies, for every $i$, a unique
integral polynomial $P_i$ whose scalar extension is $P_{i,\ell}$ for every
$\ell\neq p$. Its normalization and the parity products are the
normalizations in [def-weil-integral-frobenius-factor] and
[def-weil-parity-products]; the normalized fraction is the one in
[def-weil-normalized-integral-fraction]. Thus
[def-weil-point-counts-zeta] gives

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}
$$

after scalar extension, and uniqueness of the normalized fraction gives
$A^{(\ell)}=N_\ell$ and $B^{(\ell)}=D_\ell$. The degree of
$P_{i,\ell}$ is $\dim_{\Ql}H^i(X,\Ql)$ by
[def-weil-smooth-proper-cohomological-family]; scalar extension preserves
degree, so the displayed degree equality follows. All objects and
identifications used here are formed with the finite-field and geometric
hypotheses in [def-weil-finite-field-fiber],
[def-weil-geometric-hypotheses], and the ordinary cohomology convention
[def-weil-ordinary-compact-cohomology].
