+++
kind  = "proof"
of    = "lemma-weil-pbc-projection-formula-base-change-naturality"
+++
For a map $u:K\to L$, both naturality composites are adjoint to

$$
Lf^*Rf_*K\otimes Lf^*Q
\xrightarrow{\epsilon_K\otimes1}K\otimes Lf^*Q
\xrightarrow{u\otimes1}L\otimes Lf^*Q.
$$

This proves the forward operator equation; conjugation by $\rho_n=\pi_n^{-1}$
gives the second. For base change, expand both exchange maps as unit followed
by counit. After adjunction to $X'$, both displayed routes become

$$
L(g')^*Lf^*Rf_*K\otimes L(g')^*Lf^*Q
\xrightarrow{L(g')^*(\epsilon_K)\otimes1}
L(g')^*K\otimes L(g')^*Lf^*Q.
$$

The Cartesian identification
$L(g')^*Lf^*=L(f')^*Lg^*$ identifies the coefficient factors. Hence the
adjoints, and therefore the two routes, are equal.
