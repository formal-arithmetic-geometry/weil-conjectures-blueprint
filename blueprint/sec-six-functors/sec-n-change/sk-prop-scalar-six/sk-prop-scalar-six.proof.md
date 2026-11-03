+++
kind = "proof"
of = "sk-prop-scalar-six"
uses = ["sk-prop-ctf-finite-comparison", "sk-cor-pe-bounded-continuity", "sk-thm-existence", "sk-prop-geo-p1-adjunction", "sk-prop-diagonal-tower"]
+++
Extension of scalars along a composite is the composite of the extensions,
and the comparison maps for a composite are the composites of the
comparison maps. Hence it suffices to treat the elementary maps in the
list. Since an object that is locally $\Lambda_S\otimes P$ on a stratum
$S$, with $P$ perfect, remains of this form after derived extension of
scalars, and
extension of scalars commutes with extension by zero and with
finite cones, extension of scalars preserves $D^b_{\mathrm{ctf}}(-,\Lambda)$.

*Pullback and extension by zero.*
Associativity of derived pullback for ringed topoi [Stacks, Tag 06YV](https://stacks.math.columbia.edu/tag/06YV)
shows that $(f^*K)_{\Lambda'}\simeq f^*(K_{\Lambda'})$
for $K\in D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$.
The same assertion for $j_!$ follows from its stalkwise description
or from the equality of the corresponding right adjoints. These
identifications respect composition.

*Ordinary direct image.*
The comparison

$$
(Rf_*K)_{\Lambda'}\longrightarrow Rf_*(K_{\Lambda'})
$$

is formed from the unit, the pullback identification and the counit
of $f^*\dashv Rf_*$ on $D(-_{\mathrm{pro}\acute{e}t},\Lambda')$. For finite $A\to B$, we compute on the étale
site using Proposition [sk-prop-ctf-finite-comparison]. For a
quasi-compact étale $V\to Y$, we apply the projection
formula for constant coefficients [Stacks, Tag 0F12](https://stacks.math.columbia.edu/tag/0F12) on both $V$ and $X_V=X\times_YV$ and obtain

$$
R\Gamma(V,(Rf_*K)_B)
\simeq R\Gamma(X_V,K)\otimes_A^{\mathbf L}B
\simeq R\Gamma(X_V,K_B).
$$

Thus the comparison induces an isomorphism on derived sections over
every such $V$. This projection formula needs only cohomological
bounds for $\ell$-primary coefficients, which hold for schemes of finite
type over $k$, and so it applies to every finite $A$-algebra $B$ in (1). Since these
isomorphisms commute with restriction in $V$, the canonical morphism is
an isomorphism in $D(Y_{\acute{e}t},B)$, and hence, by
Proposition [sk-prop-ctf-finite-comparison], in $D(Y_{\mathrm{pro}\acute{e}t},B)$.

Next consider $\mathcal O_E\to A$ with $A$ finite. Then $A$ has a finite free
$\mathcal O_E$-resolution of length at most one. Its condensed
version is again exact. To see this, note that a continuous map from a
profinite set to the finite quotient $A$ is constant on the pieces of a
finite clopen partition, and hence lifts to a continuous map to the free
module. Its pullback is a finite free resolution
of $A_X$ over $\mathcal O_{E,X}$. Consequently, tensoring with $A_X$ is
computed by finite sums and a cone, which commute with the exact
derived functor $Rf_*$. For $\mathcal O_E\to\mathcal O_F$ and
$E\to F$, the extension of coefficients is finite free, and the assertion
follows from finite sums. For $\mathcal O_E\to E$, the complex $K_E$ is the
colimit of $K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$, and for
$E\to \overline{\mathbf Q}_\ell$, the complex $K_{\overline{\mathbf Q}_\ell}$ is the filtered colimit of the $K_F$
over finite extensions $F/E$ in $\overline{\mathbf Q}_\ell$. Since $K$ is bounded, all terms of
these systems are bounded below by a common integer, and
Corollary [sk-cor-pe-bounded-continuity] shows that the colimits commute with
$Rf_*$. This proves the comparison for direct images in all cases.

*Compactly supported direct image.*
For $f=pj$, we combine the preceding comparison for $Rp_*$ with the
one for $j_!$. Both commute with the refinement maps of the
construction by compactifications, since they are formed from the same
identifications of pullbacks and adjunction maps and restrict to the
identity on the open subscheme. Thus

$$
(Rf_!K)_{\Lambda'}\simeq Rf_!(K_{\Lambda'})
$$

is independent of the compactification and respects composition.

*Exceptional inverse image.*
For $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$ define

$$
\beta_{f,K}:(f^!K)_{\Lambda'}\longrightarrow f^!(K_{\Lambda'})
$$

as the transpose, under the adjunction
$Rf_!\dashv f^!$ on $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda'))$, of the morphism

$$
Rf_!((f^!K)_{\Lambda'})
\xrightarrow{\sim}(Rf_!f^!K)_{\Lambda'}
\xrightarrow{(\varepsilon_K)_{\Lambda'}}K_{\Lambda'}.
$$

The first arrow is the comparison for $Rf_!$, which applies because
$f^!K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ by Theorem [sk-thm-existence]. Since the counit of a
composite is the composite of its counits, these maps respect composition
and restriction to opens.

For a closed immersion $i$ with open complement $j$, we use the triangle

$$
i_*i^!K\longrightarrow K\longrightarrow Rj_*j^*K.
$$

Extension of scalars commutes with $i_*$, $j^*$ and, by the preceding
argument, $Rj_*$. Therefore it carries this triangle to the triangle
over $\Lambda'$. Since the first map is the counit, the comparison on
fibres is $i_*\beta_{i,K}$, and hence $\beta_{i,K}$ is an isomorphism.

Next let $q:\mathbf P^1_Y\to Y$. The adjunction $Rq_*\dashv q^*(1)[2]$
between $D^b_{\mathrm{ctf}}(\mathbf P^1_Y,\Lambda)$ and $D^b_{\mathrm{ctf}}(Y,\Lambda)$ is defined
by the diagonal class and the trace. We claim that these commute with all the
maps of coefficient rings listed above. Indeed, the classes with finite coefficients are
constructed from the Kummer sequence and derived extension of scalars, the
integral classes are their compatible limits, and
the classes over fields are obtained from these by extension of scalars
(Propositions [sk-prop-geo-p1-adjunction]
and [sk-prop-diagonal-tower]). For $\mathcal O_E\to A$, the
perfectness of $A_X$ proved above implies that the derived tensor product with
$A_X$ commutes with the inverse limits defining the integral classes, and the
resulting classes are exactly the classes with finite coefficients.
Hence the identification $q^!\simeq q^*(1)[2]$ is compatible with
extension of scalars, and $\beta_{q,K}$ becomes the comparison for
$q^*$, twisted by $(1)[2]$, which is an isomorphism. Since $\mathbf A^1_Y$
is open in $\mathbf P^1_Y$ and $\mathbf A^d_Y\to Y$ is a composite of $d$
projections of this kind, the compatibility of $\beta$ with restriction to
opens and with composition gives the case of affine space. In general,
whether $\beta_{f,K}$ is an isomorphism may be checked locally on $X$, so we
may assume, using a finite affine cover, that $f$ factors as a closed
immersion into an affine space over $Y$ followed by the projection. Then the
two cases already treated and compatibility with composition give the
claim.

*Tensor product and internal Hom.*
Derived extension of scalars is symmetric monoidal,
by associativity of tensor product. For internal Hom, we use a stratification on
whose strata the first argument is locally $\Lambda_S\otimes P$ with $P$
perfect, and finite cones to reduce to the case where the first argument is $a_!P$, as in the
preceding proposition. The identity

$$
\cHom_X(a_!P,K)
\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K)
$$

commutes with extension of scalars by the comparisons for $Ra_*$,
$a^!$, and the dual of a perfect complex. Since all of these are defined
by the same evaluation pairing, they are the canonical
comparison maps. Finite cones then give the result for every first argument.
