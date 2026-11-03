+++
kind  = "proof"
of    = "prop-weil-pbc-site-comparison-finite-level"
+++
The inverse image of [def-weil-pbc-site-comparison-morphism] is a left
adjoint, so it preserves finite colimits. It preserves finite limits: the
inclusion of the etale site into the pro-etale site is representably flat, so
left Kan extension along it is left exact, and sheafification is left exact.
On module sheaves it therefore preserves kernels and cokernels, and is exact.

On every affine etale $W\to T$, [lem-weil-pbc-comparison-sections] applied to
the constant system at $W$ identifies $(\nu_T^*F)(W)$ with $F(W)$, and under
this identification the unit is the identity on sections. The affine etale
objects form a basis of $T_{\Et}$, so the unit is an isomorphism of etale
sheaves.

Let $I$ be injective on $T_{\Et}$ and choose an injective resolution
$\nu_T^*I\to J^\bullet$ on $T_{\Proet}$. As $\nu_{T,*}$ is restriction to the
etale subsite, $R^q\nu_{T,*}(\nu_T^*I)$ is the sheafification of
$W\mapsto H^q(J^\bullet(W))$, and $H^q(J^\bullet(W))$ is the $q$-th derived
functor of evaluation at $W$, applied to $\nu_T^*I$. An affine etale $W\to T$
is an object of the affine pro-etale site of $T$, so these groups vanish for
$q>0$ by [lem-weil-pbc-comparison-injective-acyclicity]. Since affine etale
objects form a basis of $T_{\Et}$ (compare [lem-weil-pbc-ind-etale-basis]),
the sheafification is zero.
