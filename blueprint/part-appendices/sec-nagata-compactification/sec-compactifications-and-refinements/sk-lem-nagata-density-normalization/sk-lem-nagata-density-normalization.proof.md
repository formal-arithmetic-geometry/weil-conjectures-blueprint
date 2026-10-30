+++
kind = "proof"
of = "sk-lem-nagata-density-normalization"
uses = ["sk-prop-sf-open-closed-triangle"]
+++
Since $j_!K$ vanishes outside $X\subseteq Z$, it is
pushed forward from $Z$, and we must check that $i_*$ is exact, so
that $Ri_*=i_*$. By Proposition [sk-prop-sf-open-closed-triangle], the functors
attached to open and closed immersions on the pro-étale site are
exact, provided that the complementary open is quasi-compact. Since
$\overline X$ is Noetherian, the complement of $Z$ is quasi-compact, and
therefore $i_*$ is exact. All functors below are then exact and may
be applied degreewise to unbounded complexes.
The inverse image of $j_!K$ on $Z$ is $j_{Z,!}K$. The natural map
$j_!K\to i_*i^*j_!K=i_*j_{Z,!}K$ is the identity on the open $X$,
and both sides restrict to zero on its closed complement, so that the
localization sequence for an open and its closed complement shows
that this map is an isomorphism. Applying $Rp_*$ and using
$Rp_*Ri_*\simeq R(p\circ i)_*$, we obtain the second identification.
