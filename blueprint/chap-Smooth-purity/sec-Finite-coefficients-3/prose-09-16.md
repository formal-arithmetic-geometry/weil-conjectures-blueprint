+++
id = "prose-09-16"
kind = "hidden"
title = "Finite coefficients (6)"
order = 757
+++
The orientation (9.14) is defined without
coordinates, but on a coordinate chart it agrees with the
identification given by the trace map of affine space
(9.11). This is what makes the map
$f^*K(d)[2d]\to f^!K$ below the expected one, and the trace map in
Section [sec-Compatibilities] relies on it as well.

We prove the agreement for a vector bundle, where both
orientations can be computed, and reduce a coordinate chart to the
vector bundle $\mathbf A^d_Y$ by naturality.

*Vector bundles.* Let $\pi:V\to S$ be a vector bundle of rank $d$.
Here the orientation obtained from the diagonal is the
orientation of Proposition [proposition-purity-vector-bundles], because the
construction from the diagonal moves the diagonal to the zero section
and then deforms the zero section to itself, and neither step changes
integration along the fibres. For the first step, regard $V\times_SV$ as a vector
bundle over the first factor. The automorphism $(v,w)\mapsto(v,w-v)$ of
$V\times_SV$ over the first factor takes the diagonal to the zero
section, and it preserves integration in the second factor. To see this,
let the translation vector vary over $V$. Its effect on the top compactly
supported direct image, identified with the constant sheaf by integration,
is then multiplication by a locally constant unit on $V$, and this unit is $1$ at
the zero vector, where the translation is the identity. Since each
geometric fibre of $V\to S$ is connected, it is $1$ everywhere.

Next, the deformation to the normal bundle of the zero section of $V$ is
$V\times\mathbf A^1$, with the map
$V\times\mathbf A^1\to V\times\mathbf A^1$, $(w,t)\mapsto(tw,t)$, to the
original family. This map is defined by scalar multiplication, without
a trivialization, and in a local trivialization it is $x_i=tu_i$, as in the
coordinate description above. Integration on this product family is the
pullback of the original integration. Therefore the comparison of
Lemma [lemma-section-normal-bundle], which is the identity at $t=1$, is
the identity under these integrations, in particular at $t=0$. Combined
with the translation, this identifies the orientation obtained from the
diagonal for $\pi$ with the orientation of the vector bundle.

*Coordinate charts.* A chart $e:U\to\mathbf A^d_Y$ relates the
diagonal of $U$ to the diagonal of $\mathbf A^d_Y$, where the case of vector
bundles applies, so we have to transport the orientation along $e$.
By Lemma [lemma-naturality-under-base-change-etale] it suffices to see
that every ingredient of the orientation of a chart obtained from the diagonal
is pulled back from affine space. So let
$U\subset X$ be open with an étale map
$e:U\to\mathbf A^d_Y$ over $Y$. Then the étale map
$e\times e:U\times_YU\to\mathbf A^d_Y\times_Y\mathbf A^d_Y$ carries the
diagonal of $U$ into the diagonal of $\mathbf A^d_Y$, whose inverse image
is $U\times_{\mathbf A^d_Y}U$. In it the diagonal of $U$ is
open and closed, because $e$ is separated and étale, and removing the other
components, as in the proof of Lemma [lemma-section-normal-bundle], we
obtain a cartesian square of centers. The induced map of normal bundles is
then the differential $T_{U/Y}\simeq e^*T_{\mathbf A^d_Y/Y}$, a pullback of
vector bundles. Likewise, the dualizing complex is pulled back from the affine model,
because by composing adjunctions the exceptional inverse image along an
étale map is its ordinary inverse image. For the comparison obtained
from the deformation, we factor $e\times e$ as

$$
U\times_YU\xrightarrow{\mathrm{id}_U\times e}
U\times_Y\mathbf A^d_Y\xrightarrow{e\times\mathrm{id}}
\mathbf A^d_Y\times_Y\mathbf A^d_Y.
$$

The second arrow is the base change of the first projection along $e$, and it
carries the diagonal section to the graph of $e$ over $U$, so
Lemma [lemma-naturality-under-base-change-etale](1) applies to it.
Part (2), over the common base $U$, applies to the first arrow
after we remove the other components of the inverse image of that
graph. In this factorization the map on special fibres is the displayed differential, and the
comparison at $t=1$ is the one obtained from the adjunction in coordinates.
Moreover, integration on vector bundles is preserved by the linear
isomorphism of normal bundles. By the case of vector bundles, we conclude that the
orientation on $U$ obtained from the diagonal is the orientation of affine
space given by its adjunction in coordinates.

Combining the orientation with the isomorphism
$f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$, we obtain the isomorphism
$\gamma_f$ of Theorem [theorem-smooth-purity-all-admissible-coefficients]
with finite coefficients
(Proposition [proposition-smooth-purity-finite-coefficients]). We state
the result for an arbitrary finite admissible ring.
