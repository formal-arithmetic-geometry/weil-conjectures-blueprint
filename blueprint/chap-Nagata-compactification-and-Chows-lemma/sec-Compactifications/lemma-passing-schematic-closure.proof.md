+++
kind = "proof"
of = "lemma-passing-schematic-closure"
order = 1416
+++
The first identification is a statement about supports, and the
second follows from it by applying $Rp_*$. The only point that needs
care on the pro-étale site is the exactness of $i_*$.

Since $j_!K$ vanishes outside $X\subseteq Z$, it should be
pushed forward from $Z$. To say this in the derived category we need
$i_*$ to be exact, so that $Ri_*=i_*$. By Proposition [proposition-extension-zero-restriction-closed-subscheme], the functors
attached to open and closed immersions on the pro-étale site are
exact when the complementary open is quasi-compact. Since
$\overline X$ is Noetherian, the complement of $Z$ is quasi-compact,
so all functors below are exact and may be applied degreewise
to unbounded complexes.
The inverse image of $j_!K$ on $Z$ is $j_{Z,!}K$, so we have the
natural map $j_!K\to i_*i^*j_!K=i_*j_{Z,!}K$. It is the identity on the
open $X$, and both sides restrict to zero on the closed complement of
$X$. By the localization sequence for an open and its closed
complement, this map is therefore an isomorphism. The second identification then follows by
applying $Rp_*$ and using $Rp_*Ri_*\simeq R(p\circ i)_*$.
