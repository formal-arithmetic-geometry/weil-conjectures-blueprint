+++
kind  = "proof"
of    = "lem-exc-closed-support-triangle"
+++
Choose a K-injective resolution $K\to I$ with injective terms, using
[prop-weil-pbc-kinjective-resolutions-exist]; by
[lem-exc-closed-ambient] the right adjoint $Ri^!$ of the statement
is computed on such a resolution, so $Ri^!K=i^!I$ for the sheaf-level
functor $i^!=i^*\Gamma_Z$ constructed there. Both $j^*I$ and
$i^!I$ are K-injective: their left adjoints $j_!$ and $i_*$ are
exact, so Hom from an acyclic complex into either restriction is
acyclic; in particular $Rj_*j^*K\simeq j_*j^*I$. For each injective
term $I^q$, the map $I^q\to j_*j^*I^q$ is surjective. Indeed, a section
on the open part of an etale object extends because the inclusion of its
free module sheaf into that of the whole object is a monomorphism, and
injectivity extends the corresponding map to $I^q$.
Consequently the degreewise exact sequence

$$
0\longrightarrow i_*i^!I\longrightarrow I
\longrightarrow j_*j^*I\longrightarrow0
$$

gives the asserted triangle. The functors $i_*$, $Rj_*$, $j^*$
used here are the direct image and inverse image of
[def-weil-pbc-direct-image], [def-weil-pbc-inverse-image]; no
constructibility has been used.
