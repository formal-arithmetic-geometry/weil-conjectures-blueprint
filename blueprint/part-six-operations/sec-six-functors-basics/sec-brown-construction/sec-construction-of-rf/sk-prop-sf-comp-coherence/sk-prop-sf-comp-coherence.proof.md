+++
kind = "proof"
of = "sk-prop-sf-comp-coherence"
uses = ["sk-prop-proper-image-localizing", "sk-thm-sfb-proper-base-change", "sk-lem-nagata-density-normalization", "sk-prop-nagata-sketch-comp-category", "sk-def-nagata-sketch-data", "sk-lem-sf-determination", "sk-prop-proper-base-change-unbounded"]
+++
The properties of $Rp_*\circ j_!$ for a single compactification follow from
Proposition [sk-prop-proper-image-localizing] and the preservation
of $D^b_{\mathrm{ctf}}(-,\Lambda)$ by proper direct image
(Proposition [sk-thm-sfb-proper-base-change]). For independence, it suffices to
compare a compactification with a refinement of it. Indeed, the
schematic closure of $X$ in a compactification is a refinement of it,
since its inverse image over $X$ is $X$, and any two dense
compactifications have a common refinement
(Proposition [sk-prop-nagata-sketch-comp-category]).

*Refinements.* Let $j:X\to Z$ and $j':X\to Z'$ be
compactifications over $Y$, and let $h:Z'\to Z$ be a refinement
(Definition [sk-def-nagata-sketch-data]), that is, a proper $Y$-morphism
with $h\circ j'=j$ and $h^{-1}(X)=X$. Restriction to the open subscheme
$X$ commutes with $Rh_*$, because $h^{-1}(X)=X$ and
restriction is exact and preserves K-injectives (its left adjoint $j_!$
is exact). Hence $j^*Rh_*j'_!K\simeq K$. By adjunction, this isomorphism
corresponds to a map

$$
e_{h,K}:j_!K\longrightarrow Rh_*j'_!K
\tag{6.6}
$$

whose restriction to $X$ is the identity. We claim that it is an isomorphism
for $K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. By
Proposition [sk-prop-proper-image-localizing], both sides are exact
functors of $K$ preserving direct sums, so by
Lemma [sk-lem-sf-determination] we may assume that
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$. On $X$ the map is the identity, and so it suffices
to show that both sides vanish on the closed complement $Z\setminus X$. For $j_!K$ this is clear.
For $Rh_*j'_!K$, we apply proper base change on $D^b_{\mathrm{ctf}}$
(Proposition [sk-prop-proper-base-change-unbounded]) to the inclusion
of $Z\setminus X$ into $Z$. It identifies the restriction of $Rh_*j'_!K$
with the direct image of the
restriction of $j'_!K$ to $h^{-1}(Z\setminus X)=Z'\setminus X$, which is
zero. By the exact sequence for an open and its closed complement, applied in
each degree [Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH), a morphism in $D(Z_{\mathrm{pro}\acute{e}t},\Lambda)$ that is an
isomorphism on $X$ and on $Z\setminus X$ is an isomorphism. Applying $Rp_*$
and using $R(p\circ h)_*=Rp_*Rh_*$, we obtain an isomorphism between the two
candidate functors $Rf_!$.

If $Z''\xrightarrow{k}Z'\xrightarrow{h}Z$ are two successive refinements,
with $j'':X\to Z''$ the open immersion, then $Rh_*(e_{k,K})\circ e_{h,K}$ and $e_{hk,K}$ are maps from $j_!K$ to
$R(hk)_*j''_!K$ that both restrict to the identity on $X$. By the
observation before the proposition, they are equal.

*Common refinements.* Given dense compactifications $Z_1$ and
$Z_2$, Proposition [sk-prop-nagata-sketch-comp-category] provides a dense
compactification $Z$ with proper maps $h_i:Z\to Z_i$ satisfying
$h_i^{-1}(X)=X$, and similarly for finitely many compactifications. The
refinement isomorphisms for $h_1$ and $h_2$ compose to an isomorphism
between the functors defined by $Z_1$ and $Z_2$. Transitivity of the
refinement maps on a common refinement shows that this comparison does
not depend on the chosen refinement and satisfies the cocycle
condition.
