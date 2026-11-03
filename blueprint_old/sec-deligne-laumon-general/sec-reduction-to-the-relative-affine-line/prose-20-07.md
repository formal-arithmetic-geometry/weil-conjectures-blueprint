+++
id = "prose-20-07"
kind = "hidden"
title = "Reduction to the relative affine line (2)"
order = 781
+++
To prove a weight bound for $R^if_!$ of a morphism $f$, it suffices
to prove it over the pieces of finite partitions of the source and of
the target. On the source, let $j$ be the inclusion of an open
subscheme and $i$ that of its closed complement. Applying $Rf_!$ and
the composition isomorphism to the triangle
$j_!j^*K\to K\to i_*i^*K\to$, we obtain a long exact sequence relating
$R^if_!$ of $K$ to $R^i(fj)_!$ of $j^*K$ and $R^i(fi)_!$ of $i^*K$.
This sequence is Frobenius-equivariant by naturality, and the
restrictions $j^*K$ and $i^*K$ are again mixed of weights at most
those of $K$. Hence, by Lemma [sk-lem-wgen-triangle-weights], the
bound for the two pieces implies the bound for $K$. On the target,
base change for direct images with compact support identifies the
restriction of $R^if_!K$ to a piece with the direct image of the
restriction of $K$ to its inverse image. Since extension by zero and
closed direct image preserve weights, the same triangle on the target
and Lemma [sk-lem-wgen-triangle-weights] show that the bounds over the
pieces imply the bound over the whole target.
