+++
id = "prose-10-17"
kind = "hidden"
title = "The orientation from the diagonal (6)"
order = 456
+++
The orientation (10.13) is defined without
coordinates. We now check that on a coordinate chart it agrees with the
identification given by the trace map of affine space
(10.7), so that the map
$f^*K(d)[2d]\to f^!K$ below is the expected one. This comparison is used
again for the trace map in
Section [sec-sp-grp-trace].

*Vector bundles.* Let $\pi:V\to S$ be a vector bundle of rank $d$.
We claim that in this case the orientation obtained from the diagonal is the
orientation of Proposition [sk-prop-an]. Regard $V\times_SV$ as a vector
bundle over the first factor. The automorphism $(v,w)\mapsto(v,w-v)$ of
$V\times_SV$ over the first factor takes the diagonal to the zero
section, and it preserves integration in the second factor. To see this, let the
translation vector vary over $V$. Its effect on the top compactly
supported direct image, identified with the constant sheaf by
integration, is multiplication by a locally constant unit on $V$. This
unit is $1$ at the zero vector, where the translation is the identity.
Since each geometric fibre of $V\to S$ is connected, the unit is $1$
everywhere. Next, the deformation to the normal bundle of the zero
section of $V$ is $V\times\mathbf A^1$, with the map
$V\times\mathbf A^1\to V\times\mathbf A^1$, $(w,t)\mapsto(tw,t)$, to the
original family. This map is defined by scalar multiplication, without
a trivialization; in a local trivialization it is $x_i=tu_i$, as in the coordinate
description above.
Integration on this product family is the pullback of the
original integration. Therefore the comparison of Lemma [sk-thm-dnc],
which is the identity at $t=1$, is the identity under these integrations,
in particular at $t=0$. Together with the translation, this identifies
the orientation obtained from the diagonal for $\pi$ with the orientation of
the vector bundle.

*Coordinate charts.* By Lemma [sk-lem-lem-sp-dnc-naturality] it suffices to see
that every ingredient of the orientation of a chart obtained from the diagonal
is pulled back from affine space, where the case of vector bundles applies. Let
$U\subset X$ be open with an étale map
$e:U\to\mathbf A^d_Y$ over $Y$. The étale map
$e\times e:U\times_YU\to\mathbf A^d_Y\times_Y\mathbf A^d_Y$ carries the
diagonal of $U$ into the diagonal of $\mathbf A^d_Y$. The inverse image
of the latter is $U\times_{\mathbf A^d_Y}U$, in which the diagonal of
$U$ is open and closed because $e$ is separated and étale. Removing
the other components, as in the proof of Lemma [sk-thm-dnc], we obtain
a cartesian square of centers. The induced map of normal bundles is the
differential $T_{U/Y}\simeq e^*T_{\mathbf A^d_Y/Y}$ (pullback of vector
bundles). It remains to see that both ingredients of the orientation are
pulled back from the affine model. For the dualizing complex, this holds
because, by composing adjunctions, the exceptional inverse image along
an étale map is its ordinary inverse image. For the comparison obtained
from the deformation, we factor $e\times e$ as

$$
U\times_YU\xrightarrow{\mathrm{id}_U\times e}
U\times_Y\mathbf A^d_Y\xrightarrow{e\times\mathrm{id}}
\mathbf A^d_Y\times_Y\mathbf A^d_Y.
$$

First we apply Lemma [sk-lem-lem-sp-dnc-naturality](1) to the second arrow.
This arrow is the base change of the first projection along $e$, and the base
change of the diagonal section is the graph of $e$ over $U$.
Then we apply part (2), over the common base $U$, to the first arrow,
after removing the other components of the inverse image of that
graph. The map on special fibres is the displayed differential, and the
comparison at $t=1$ is the one obtained from the adjunction in coordinates.
Integration on vector bundles is preserved by the linear
isomorphism of normal bundles. By the case of vector bundles, we conclude that the
orientation on $U$ obtained from the diagonal is the orientation of affine
space given by its adjunction in coordinates.

Combining the orientation with the isomorphism
$f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$, we obtain
Theorem [sk-thm-purity-transport] with finite coefficients.
