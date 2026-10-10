+++
kind  = "proof"
of    = "def-nagata-global-blowup-glue-data"
+++
For affine opens $W\subseteq V$, the transition map
$\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)$ is induced by the
restriction $A_V\to A_W$, and the structure morphisms are induced by the
degree-zero maps $A_V\to\mathcal R_{A_V}(I_V)_0$ and
$A_W\to\mathcal R_{A_W}(I_W)_0$. The coefficientwise map of Rees algebras
restricts in degree zero to $A_V\to A_W$, so the structure morphisms are
compatible with the transition maps and with the inclusion $W\subseteq V$.

If $W$ is a basic open $D(s)$ of $V$, the square is cartesian by
[lemma-nagata-global-blowup-overlap-basic]. For general affine opens
$W\subseteq V$, cover $W$ by opens $W'$ that are basic opens both of $W$
and of $V$ (any point of $W$ has such a neighbourhood: take a basic open of
$V$ inside $W$; it is then also a basic open of $W$). By the basic case
applied to $W'\subseteq W$ and to $W'\subseteq V$, and since the transition
maps compose (the diagram is a functor), both
$\mathsf B_W(\mathcal I)$ and $\mathsf B_V(\mathcal I)\times_VW$ restrict
over $W'$ to $\mathsf B_{W'}(\mathcal I)$, compatibly with the canonical
morphism $\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)\times_VW$.
Hence this morphism over $W$ is an isomorphism over every $W'$ of a cover
of $W$, so it is an isomorphism, and the square is cartesian.
