+++
kind = "proof"
of = "proposition-construction-independence-rf-shriek"
order = 513
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-descent-finite-coefficient-field", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "theorem-proper-base-change-classical-pro", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-etale-derived-category", "corollary-proper-direct-image-finite-coefficients-localizing", "lemma-uniform-bound-proper-direct-image", "lemma-proper-direct-image-unbounded-complexes", "proposition-compactness-proper-direct-image", "proposition-sp-unique-adjoint", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "definition-relative-picard-functor"]
+++
For a single compactification there is nothing new to prove, and two
compactifications are compared through a third one that refines both,
by the argument described at the start of this subsection.

The properties of $Rp_*\circ j_!$ for a single compactification follow from
Proposition [proposition-proper-direct-image-extension-zero] and the preservation
of $D^b_{\mathrm{ctf}}(-,\Lambda)$ by proper direct image
(Proposition [proposition-proper-direct-image-constructible-complexes]).

For independence it suffices to
compare a compactification with a refinement of it. Indeed, the
schematic closure of $X$ in a compactification is a refinement of it,
since its inverse image over $X$ is $X$. Moreover, any two dense
compactifications have a common refinement
(Proposition [proposition-dense-compactifications-form-cofiltered-category]).

*Refinements.* Let $j:X\to Z$ and $j':X\to Z'$ be
compactifications over $Y$, and let $h:Z'\to Z$ be a refinement
(Definition [definition-compactification-refinement]), that is, a proper $Y$-morphism
with $h\circ j'=j$ and $h^{-1}(X)=X$. To construct the comparison
map, note that restriction to the open subscheme
$X$ commutes with $Rh_*$. This holds because $h^{-1}(X)=X$ and
restriction is exact and preserves K-injectives, its left adjoint $j_!$
being exact. As $j'^*j'_!K=K$, we get $j^*Rh_*j'_!K\simeq K$. By adjunction this isomorphism
corresponds to a map

$$
e_{h,K}:j_!K\longrightarrow Rh_*j'_!K
\tag{5.7}
$$

whose restriction to $X$ is the identity. We claim that it is an isomorphism
for $K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. By
Proposition [proposition-proper-direct-image-extension-zero], both sides are exact
functors of $K$ preserving direct sums, so by
Lemma [lemma-checking-isomorphisms-constructible-complexes] we may assume that
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, where proper base change is available.

By the exact sequence for an open and its closed complement, applied in
each degree [Stacks, [09AH](https://stacks.math.columbia.edu/tag/09AH)], a morphism in $D(Z_{\mathrm{pro}\acute{e}t},\Lambda)$ that is an isomorphism on $X$ and on $Z\setminus X$ is an isomorphism. On $X$ our map is the identity, so it remains to see that on $Z\setminus X$ both sides vanish. For $j_!K$ this holds by definition of extension by zero, while for $Rh_*j'_!K$ we use proper base change on $D^b_{\mathrm{ctf}}$
(Proposition [proposition-proper-base-change-localizing-categories]) for the inclusion
of $Z\setminus X$ into $Z$. It shows that the restriction of $Rh_*j'_!K$
is the direct image of the
restriction of $j'_!K$ to $h^{-1}(Z\setminus X)=Z'\setminus X$, which is
zero. This proves the claim. Applying $Rp_*$
and using $R(p\circ h)_*=Rp_*Rh_*$, we obtain an isomorphism between the two
candidate functors $Rf_!$, namely $Rp_*j_!$ and $R(ph)_*j'_!$.

If $Z''\xrightarrow{k}Z'\xrightarrow{h}Z$ are two successive refinements,
with $j'':X\to Z''$ the open immersion, then $Rh_*(e_{k,K})\circ e_{h,K}$ and $e_{hk,K}$ are maps from $j_!K$ to
$R(hk)_*j''_!K$ that both restrict to the identity on $X$. By the
observation before the proposition, they are equal.

*Common refinements.* Two arbitrary compactifications need not be related by a refinement, but they have a common one. Indeed, given dense compactifications $Z_1$ and
$Z_2$, Proposition [proposition-dense-compactifications-form-cofiltered-category] provides a dense
compactification $Z$ with proper maps $h_i:Z\to Z_i$ satisfying
$h_i^{-1}(X)=X$, and similarly for finitely many compactifications. The refinement isomorphisms for $h_1$ and $h_2$ then compose to an isomorphism
between the functors defined by $Z_1$ and $Z_2$, and transitivity of the refinement maps on a common refinement shows that this comparison does
not depend on the chosen refinement and satisfies the cocycle
condition.
