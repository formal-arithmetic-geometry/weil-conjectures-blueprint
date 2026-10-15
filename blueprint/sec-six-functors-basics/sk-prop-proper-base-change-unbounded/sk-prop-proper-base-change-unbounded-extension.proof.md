+++
kind = "proof"
of = "det-proper-base-change-unbounded-extension"
+++
By [sk-prop-proper-image-localizing], $Rp_*$ and $Rp'_*$ restrict to exact sum-preserving functors between
the localizing categories, and by [det-proper-base-change-unbounded-pullback] so do $g^*$ and $g'^*$. Hence
$F_1=g^*Rp_*$ and $F_2=Rp'_*g'^*$ are exact functors $\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y',\Lambda))$
preserving direct sums. The base change map is a natural transformation $\beta\colon F_1\to F_2$ of exact
functors: it is built from units, counits and the connection isomorphism, all compatible with shifts and
triangles. By [sk-lem-sf-determination] (the set of $K$ with $\beta_K$ invertible is closed under shifts and
cones by the five lemma and under sums since $F_1$, $F_2$ preserve them, and it contains
$\Dctf(X,\Lambda)$), $\beta_K$ is an isomorphism for all $K\in\Loc(\Dctf(X,\Lambda))$.
