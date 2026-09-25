+++
id = "lem-exc-open-locality-direct-image"
kind = "lemma"
title = "Locality of direct images for open immersions"
order = 1963
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let

$$
\begin{array}{ccc}
U\cap V&\xrightarrow{\ j''\ }&U\\
g''\big\downarrow&&\big\downarrow j\\
V&\xrightarrow{\ g\ }&T
\end{array}
$$

be a Cartesian square of open immersions. Then the canonical comparison

$$
Lg^*Rj_*\xrightarrow{\ \sim\ }Rj''_*L(g'')^*
$$

of functors on the ordinary derived categories of
[def-weil-pbc-derived-categories] is an isomorphism.

## Proof

At the sheaf level the two functors agree: for a sheaf $F$ on $U$ and
an etale $W\to V$, the sections of $g^*j_*F$ over $W$ are the
sections of $F$ over the open $W\times_TU=W\times_V(U\cap V)$, and the
same description holds for $j''_*(g'')^*F$ by the definition of the
inverse and direct images in
[def-weil-pbc-inverse-image], [def-weil-pbc-direct-image]; the
identification is natural, so it is a natural isomorphism of left exact
functors. Resolving injectively by
[prop-weil-pbc-kinjective-resolutions-exist] and using that
$j^*$ preserves injectives (its left adjoint $j_!$ is exact) derives
the comparison, which is the displayed isomorphism.
