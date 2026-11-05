+++
kind = "proof"
of = "lemma-triviality-near-fibre--1"
order = 1483002
uses = ["theorem-chow-s-lemma-projective-form"]
+++
Put $W=P\times Q$, and let $\mathcal I_{p_0}$ and $\mathcal I_{q_0}$
be the ideal sheaves of the two rational points. The ideal sheaf of
$(p_0\times Q)\cup(P\times q_0)$ in $W$ is
$$
\mathcal J=\mathcal I_{p_0}\boxtimes\mathcal I_{q_0}.
$$
Since $H^0(P,\mathcal O_P)=H^0(Q,\mathcal O_Q)=k$, both point ideals
have no global sections. The Künneth formula therefore gives
$H^1(W,\mathcal J)=0$. This is
`AlgebraicGeometry.TheoremOfCube.subsingleton_H_one_crossIdeal`.

Let $\pi:W\times T\to W$ be the projection and put
$\mathcal G=\pi^*\mathcal J\otimes\mathcal L$. This sheaf is of finite
presentation and flat over $T$. Since $\mathcal L_t$ is trivial, base
change gives
$$
H^1(W_t,\mathcal G_t)
\simeq H^1(W,\mathcal J)\otimes_k\kappa(t)=0.
$$
It follows that, for an affine neighbourhood $V$ of $t$ small enough,
$H^1(f^{-1}(V),\mathcal G)=0$. Lean uses
`AlgebraicGeometry.Scheme.Modules.exists_subsingleton_H_preimage_of_hFiber_eq_zero`:
a bounded complex of finite free modules computes cohomology and its
base changes, and suitable minors of the two differentials are units
near $t$, making the complex exact in degree $1$. The finiteness input
for this construction uses [theorem-chow-s-lemma-projective-form].

Choose generators of $\mathcal L$ on the two slices. Their restrictions
to $p_0\times q_0\times T\simeq T$ differ by a unit on $T$; rescaling
one generator makes them agree. On affine opens of $f^{-1}(V)$ where
$\mathcal L$ is free, these compatible sections lift to sections of
$\mathcal L$. The differences of the lifts on overlaps are sections
of $\mathcal G$, since they vanish on both slices. They form a Čech
cocycle, and the vanishing of $H^1(f^{-1}(V),\mathcal G)$ lets us
correct the lifts by sections of $\mathcal G$ so that they glue.
The resulting section $\sigma$ still restricts to the chosen generator
on $p_0\times Q\times V$. This is the construction in
`AlgebraicGeometry.TheoremOfCube.exists_section_isFreeGenerator`.

In particular, $\sigma$ generates at $(p_0,q_0,t)$. Under a
trivialization of $\mathcal L_t$, its restriction is a nonzero global
function on the proper geometrically integral scheme $W_t$, hence a
nonzero scalar in $\kappa(t)$. It therefore generates on all of $W_t$.
The locus in $f^{-1}(V)$ where $\sigma$ fails to generate is closed,
and properness makes its image in $V$ closed. Removing this image
gives the required neighbourhood $U$ of $t$. Lean packages this last
step as
`AlgebraicGeometry.Scheme.Modules.exists_isFreeGenerator_preimage_of_generatesAt`.
