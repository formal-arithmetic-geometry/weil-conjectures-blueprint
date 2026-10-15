+++
kind = "proof"
of = "sk-prop-sf-comp-coherence"
uses = ["sk-prop-proper-image-localizing", "sk-prop-ctf-finite-proper", "sk-thm-sfb-proper-base-change", "sk-lem-nagata-density-normalization", "sk-prop-nagata-sketch-comp-category", "sk-def-nagata-sketch-data", "sk-lem-sf-determination", "sk-prop-proper-base-change-unbounded"]
+++
The properties of $Rp_*\circ j_!$ for a single compactification follow from
[sk-prop-proper-image-localizing] and the preservation of
$\Dctf(-,\Lambda)$ by proper direct image ([sk-prop-ctf-finite-proper] for
finite rings and [sk-thm-sfb-proper-base-change] for $\mathcal O_E$, $E$ and
$\Qlb$). For independence it suffices to compare a compactification with a
refinement of it: after replacing compactifications by dense ones, which does
not change the functor ([sk-lem-nagata-density-normalization]), any two have a
common refinement ([sk-prop-nagata-sketch-comp-category]).

*Refinements.* Let $j:X\to Z$ and $j':X\to Z'$ be dense compactifications
over $Y$, and let $h:Z'\to Z$ be a refinement ([sk-def-nagata-sketch-data]): a
proper $Y$-morphism with $h\circ j'=j$ and $h^{-1}(X)=X$. Restriction to the
open subscheme $X$ commutes with
$Rh_*:D(Z'_{\mathrm{proét}},\Lambda)\to D(Z_{\mathrm{proét}},\Lambda)$ (restriction is
exact and preserves K-injectives, its left adjoint $j_!$ being exact), so
$j^*Rh_*j'_!K\simeq K$ in $D(X_{\mathrm{proét}},\Lambda)$. By adjunction this
isomorphism corresponds to a map

$$
e_{h,K}:j_!K\longrightarrow Rh_*j'_!K\quad\text{in }D(Z_{\mathrm{proét}},\Lambda)
$$

whose restriction to $X$ is the identity. We claim it is an isomorphism for
$K\in\Loc(\Dctf(X,\Lambda))$. By [sk-prop-proper-image-localizing] both sides
are exact functors of $K$ preserving direct sums, so by
[sk-lem-sf-determination] it suffices to take $K\in\Dctf(X,\Lambda)$. On $X$
the map is the identity. On the closed complement $Z\setminus X$, proper base
change on $\Dctf$ ([sk-prop-proper-base-change-unbounded], for the inclusion of
$Z\setminus X$ into $Z$) identifies, in $D((Z\setminus X)_{\mathrm{proét}},\Lambda)$,
the restriction of $Rh_*j'_!K$ with the direct image of the restriction of
$j'_!K$ to $h^{-1}(Z\setminus X)=Z'\setminus X$, which is zero; the restriction
of $j_!K$ is zero as well. By the open–closed exact sequence, applied in each
degree (Stacks, Tag 09AH), a map of complexes that is an isomorphism on $X$
and on $Z\setminus X$ is an isomorphism. Applying $Rp_*$ and using
$R(p\circ h)_*=Rp_*Rh_*$ gives an isomorphism between the two candidate
functors $Rf_!:\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$.

If $Z''\xrightarrow{k}Z'\xrightarrow{h}Z$ are two successive refinements, then
$Rh_*(e_{k,K})\circ e_{h,K}$ and $e_{hk,K}$ are maps from $j_!K$ to
$R(hk)_*j''_!K$ that both restrict to the identity on $X$, so they are equal:
a map out of $j_!K$ is determined by its restriction to $X$, by the adjunction
$j_!\dashv j^*$.

*Common refinements.* Given dense compactifications $Z_1$ and $Z_2$,
[sk-prop-nagata-sketch-comp-category] gives a dense compactification $Z$ with
proper maps $h_i:Z\to Z_i$ satisfying $h_i^{-1}(X)=X$, and similarly for
finitely many compactifications. The refinement isomorphisms for $h_1$ and
$h_2$ compose to an isomorphism between the functors defined by $Z_1$ and
$Z_2$. Transitivity of the refinement maps on a common refinement shows that
this comparison does not depend on the chosen refinement and satisfies the
cocycle condition.
