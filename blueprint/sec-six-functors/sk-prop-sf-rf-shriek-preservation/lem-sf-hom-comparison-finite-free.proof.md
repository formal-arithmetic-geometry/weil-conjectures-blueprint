+++
kind  = "proof"
of    = "lem-sf-hom-comparison-finite-free"
+++
Write $P'^\vee=R\mathcal H om_A(P',A_T)$, so that
$P'^{\vee,i}=\mathcal H om_A(P'^i,A_T)$ is again finite free. For a
bounded complex $P'$ of finite free modules the termwise identity
$\mathcal H om_A(P'^i,N^j)\cong(P'^i)^\vee\otimes_AN^j$ of
[lem-sf-hom-finite-projective], with the total-complex signs, is a
computation of finite free modules and uses nothing about $N$ beyond its
being a complex of modules; it gives

$$
P'^\vee\otimes_A^LN\cong R\mathcal H om_A(P',N),
$$

the finite free modules being flat, so that the derived tensor product of
[def-weil-derived-tensor] is computed by the ordinary tensor complex.
The comparison pullback $\nu_T^*$ is exact, is monoidal and carries finite
free modules to finite free modules by
[def-weil-derived-pullback-tensor-hom]; hence
$\nu_T^*(P'^\vee)\cong(\nu_T^*P')^\vee$ termwise, and the same computation
on the pro-étale side, applied to the bounded complex $\nu_T^*P'$ of
finite free modules and to $\nu_T^*N$, gives

$$
R\mathcal H om_A(\nu_T^*P',\nu_T^*N)
\cong(\nu_T^*P')^\vee\otimes_A^L\nu_T^*N
\cong\nu_T^*\bigl(P'^\vee\otimes_A^LN\bigr)
\cong\nu_T^*R\mathcal H om_A(P',N).
$$

Both the comparison map and this composite are induced by the evaluation of
[lem-sf-hom-finite-projective] and its pullback, so they agree, and the
comparison is an isomorphism.
