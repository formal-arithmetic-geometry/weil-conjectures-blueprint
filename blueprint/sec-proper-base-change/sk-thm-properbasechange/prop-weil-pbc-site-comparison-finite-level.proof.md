+++
kind  = "proof"
of    = "prop-weil-pbc-site-comparison-finite-level"
+++
The inverse image of [def-weil-pbc-site-comparison-morphism] preserves finite
limits and is a left adjoint. On module sheaves it therefore preserves
kernels and cokernels, and is exact. Equivalently on affine charts, the
section formula in [lem-weil-pbc-comparison-sections] preserves kernels, and
an epimorphism lifts locally after an etale cover at the stage representing a
section. These covers are also pro-etale covers.

On every affine etale $W\to T$, the same section formula identifies
$(\nu_T^*F)(W)$ with $F(W)$: apply it on an affine open of $T$, then use
ordinary etale gluing. Under this identification the unit is the identity on
sections. The affine etale basis consequently proves that it is an
isomorphism of etale sheaves.

If $I$ is injective on $T_{\Et}$, its restriction to any affine etale $W$ is
injective by the etale-restriction lemma. The adjunction, or its explicit
section construction, identifies $(\nu_T^*I)|_W$ with $\nu_W^*(I|_W)$. Its
positive cohomology on $W$ vanishes by
[lem-weil-pbc-comparison-injective-acyclicity]. Finally
$R^q\nu_{T,*}(\nu_T^*I)$ is the sheafification of $W\mapsto
H^q(W_{\Proet},(\nu_T^*I)|_W)$: apply restriction to an injective resolution
and then sheafify the cohomology of the resulting section complex.
Restriction of that injective resolution computes cohomology on $W$ by
[lem-weil-pbc-proetale-restriction-injectives]. The basis detection in
[lem-weil-pbc-ind-etale-basis], or just the affine etale basis on the target,
now gives the required zero sheaf.
