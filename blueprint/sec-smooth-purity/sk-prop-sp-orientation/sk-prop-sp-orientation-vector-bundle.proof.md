+++
kind = "proof"
of = "det-sp-orientation-vector-bundle"
+++
*Step 1: translation.* Regard $V\times_SV$ as a vector bundle over the first
factor, with projection $p_1$. The automorphism $\tau:(v,w)\mapsto(v,w-v)$ of
$V\times_SV$ over the first factor takes the diagonal to the zero section.
It preserves integration in the second factor: let the translation vector
vary over $V$; its effect on the top compactly supported direct image
$R^{2d}p_{1!}(\mathbf Z/\ell^n)(d)$, identified with the constant sheaf by
integration, is multiplication by a section of the locally constant sheaf of
units of $\mathbf Z/\ell^n\mathbf Z$ on $V$. The locus where this unit is $1$
is open and closed. It contains the zero section, where the translation is
the identity, and every geometric fibre of $V\to S$ is connected, so it is
all of $V$. Hence $\tau$ identifies the pair $(p_1,\Delta)$, together with the
vector-bundle integration of $p_1$, with the pair (bundle, zero section)
together with its own integration.

*Step 2: deformation of a zero section.* The deformation to the normal
bundle of the zero section of a vector bundle $W\to T$ is canonically the
product $W\times\mathbf A^1$: in a local frame with coordinates $u$ on the
deformation space and $x$ on $W$, the map to the original bundle is $x=tu$,
and these descriptions agree under linear changes of frame (a linear change
of frame commutes with multiplication by $t$). Vector-bundle integration in
this product family is the pullback of the original integration along the
projection to $W$. The comparison of the deformation lemma is the identity
at $t=1$ under these integrations; the constant family of identities has the
same property, so by the uniqueness in the deformation lemma the comparison
is the identity at every $t$, in particular at $t=0$.

*Step 3.* By Step 1 the first two isomorphisms of the diagonal orientation
(the base change $\omega_\pi\simeq L\Delta^*\omega_{p_1}$ and the deformation
comparison) are carried by $\tau$ to those of the zero section, which are the
identity under integration by Step 2; the third is vector-bundle purity
itself. Therefore the diagonal orientation of $\pi$ is the vector-bundle
orientation.
