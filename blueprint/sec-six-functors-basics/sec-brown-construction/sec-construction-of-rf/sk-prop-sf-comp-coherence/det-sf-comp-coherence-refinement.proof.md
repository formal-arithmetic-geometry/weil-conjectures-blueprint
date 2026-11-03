+++
kind = "proof"
of = "det-sf-comp-coherence-refinement"
uses = ["lem-weil-pbc-proper-open-comparison-iso", "det-sf-comp-coherence-single", "det-sf-determination-localizing"]
+++
*The restriction to $X$.* The open immersion $j:X\to Z$ has an exact left
adjoint $j_!$ of $j^*$, so $j^*$ preserves K-injective complexes and commutes
with derived direct images: $j^*Rh_*=R(h|_{h^{-1}(X)})_*j'^*$ on the open
$h^{-1}(X)=X$, where $h$ restricts to the identity. Hence
$j^*Rh_*j'_!K\simeq j'^*j'_!K\simeq K$, the last map the inverse of the unit,
which is an isomorphism for an open immersion.

*(1) Uniqueness.* By $j_!\dashv j^*$, maps $j_!K\to Rh_*j'_!K$ correspond
bijectively to maps $K\to j^*Rh_*j'_!K\simeq K$, the correspondence being
restriction to $X$. So there is exactly one map restricting to the identity,
and $e_{h,K}$ is it by construction.

*(2) Isomorphism.* Both $K\mapsto j_!K$ and $K\mapsto Rh_*j'_!K$ are exact
functors $\Loc(\Dctf(X,\Lambda))\to D(Z_{\mathrm{proét}},\Lambda)$ preserving direct
sums ([det-sf-comp-coherence-single] applied to $j$ and to $h\circ j'$), and
$e_h$ is a natural transformation of exact functors. By
[det-sf-determination-localizing] it suffices to show that $e_{h,K}$ is an
isomorphism for $K\in\Dctf(X,\Lambda)$. Let $i:Z\setminus X\to Z$ be the
closed complement. Over $X$, $e_{h,K}$ restricts to the identity. Over
$Z\setminus X$: since $h^{-1}(Z\setminus X)=Z'\setminus X$ and the restriction
of $j'_!K$ to $Z'\setminus X$ vanishes, proper base change for $h$ along $i$
(the localizing form, valid on $\Dctf$) gives $i^*Rh_*j'_!K\simeq0$; also
$i^*j_!K=0$. By the open–closed exact sequence applied in each degree ([Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH)), the pair $(j^*,i^*)$ detects isomorphisms of complexes, so
$e_{h,K}$ is an isomorphism. (For finite coefficients and étale-origin $K$
this is the stalkwise argument of [lem-weil-pbc-proper-open-comparison-iso].)

*(3) Identity and transitivity.* For $h=\mathrm{id}$ the identity map restricts
to the identity, so $e_{\mathrm{id},K}=\mathrm{id}$ by (1). For successive
refinements both $e_{hk,K}$ and $Rh_*(e_{k,K})\circ e_{h,K}$ are maps
$j_!K\to R(hk)_*j''_!K$; restricted to $X$, where $h$, $k$ and $hk$ are
identities, both are the identity of $K$. By the uniqueness in (1), applied to
the refinement $hk$, they are equal.
