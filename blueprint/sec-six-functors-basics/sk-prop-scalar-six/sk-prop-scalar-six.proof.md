+++
kind = "proof"
of    = "sk-prop-scalar-six"
uses = ["sk-prop-sfb-module-derived-factorization", "sk-prop-ctf-finite-comparison", "sk-cor-pe-bounded-continuity", "sk-thm-existence", "sk-prop-geo-p1-adjunction", "sk-prop-diagonal-tower"]
+++
It suffices to treat the listed elementary maps. A perfect local model on a stratum remains perfect after
derived extension of scalars. Extension of scalars also commutes with extension by zero and with finite
cones. This proves preservation of $\Dctf(-,\Lambda)$ ([det-sfb-coefficient-comparisons-ctf]).

*Pullback and extension by zero.* Associativity of derived pullback for ringed topoi (Stacks, Tag 06YV)
gives $(f^*K)_{\Lambda'}\simeq f^*(K_{\Lambda'})$ in $\D(X_{\mathrm{proét}},\Lambda')$ for $K\in\D(Y_{\mathrm{proét}},\Lambda)$. The
same assertion for $j_!$ follows from its stalkwise description or from the equality of the corresponding
right adjoints. These identifications respect composition ([def-sfb-derived-pull-iso],
[def-sfb-derived-open-immersion-shriek-iso]).

*Ordinary direct image.* The comparison

$$
(Rf_*K)_{\Lambda'}\longrightarrow Rf_*(K_{\Lambda'})\quad\text{in }\D(Y_{\mathrm{proét}},\Lambda')
$$

is formed from the unit, the pullback identification and the counit of $f^*\dashv Rf_*$ on
$\D(-_{\mathrm{proét}},\Lambda')$. For finite $A\to B$, calculate on the étale site using
[sk-prop-ctf-finite-comparison]. On a quasi-compact étale test object $V\to Y$, the scalar projection formula
(Stacks, Tag 0F12) on both $V$ and $X_V=X\times_YV$ gives

$$
R\Gamma(V,(Rf_*K)_B)\simeq R\Gamma(X_V,K)\otimes_A^{\mathbf L}B\simeq R\Gamma(X_V,K_B).
$$

Thus the comparison induces an isomorphism on derived sections over every such $V$. The scalar projection
formula needs only cohomological bounds for $\ell$-primary coefficients, which hold for the standing
schemes, so it applies to every $B$, whatever its projective dimension over $A$. These isomorphisms commute
with restriction in $V$, so they identify the canonical morphism in $\D(Y_{\mathrm{ét}},B)$, and hence, by
[sk-prop-ctf-finite-comparison], in $\D(Y_{\mathrm{proét}},B)$ ([lem-coef-finite-direct-image]).

For $\mathcal O_E\to A$ with $A$ finite, $A$ has a finite free $\mathcal O_E$-resolution of length at most one. Its
condensed version is exact (a continuous map to a finite quotient lifts on a finite clopen partition), and
pullback gives a finite free resolution of $A_X$ over $\mathcal O_{E,X}$. Tensoring with $A_X$ is consequently
computed by finite sums and a cone, which commute with the exact derived functor $Rf_*$. For
$\mathcal O_E\to\mathcal O_F$ and $E\to F$ the coefficient extension is finite free, so the assertion follows from finite
sums. For $\mathcal O_E\to E$, use the system $K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$; for $E\to\Qlb$, use the
filtered system of finite field extensions. Since $K$ is bounded and these systems have a common lower bound,
[sk-cor-pe-bounded-continuity] commutes their colimits with $Rf_*$. This proves the direct-image comparison in
all cases ([det-sfb-coefficient-comparisons-direct-image]).

*Compactly supported direct image.* For $f=pj$, combine the preceding comparison for $Rp_*$ with the one for
$j_!$. Both commute with the refinement maps of the compactification construction: they are formed from the
same pullback identifications and adjunction maps, and restrict to the identity on the open subscheme. Thus

$$
(Rf_!K)_{\Lambda'}\simeq Rf_!(K_{\Lambda'})\quad\text{in }\Dctf(Y,\Lambda')
$$

is independent of the compactification and respects composition ([det-sfb-coefficient-comparisons-compact-support],
[lem-fix-compact-support-coefficient-change]).

*Exceptional inverse image.* For $K\in\Dctf(Y,\Lambda)$ define

$$
\beta_{f,K}\colon(f^!K)_{\Lambda'}\longrightarrow f^!(K_{\Lambda'})
$$

in $\Dctf(X,\Lambda')$ as the transpose, under the adjunction $Rf_!\dashv f^!$ on $\Loc(\Dctf(-,\Lambda'))$, of
the morphism in $\Dctf(Y,\Lambda')$

$$
Rf_!((f^!K)_{\Lambda'})\xrightarrow{\sim}(Rf_!f^!K)_{\Lambda'}\xrightarrow{(\epsilon_K)_{\Lambda'}}K_{\Lambda'}.
$$

The first arrow is the comparison for $Rf_!$, which applies because $f^!K\in\Dctf(X,\Lambda)$ by
[sk-thm-existence]. The counit of a composite is the composite of its counits, so these maps
respect composition and open restriction.

For a closed immersion $i$ with open complement $j$, use the triangle in $\Dctf(Y,\Lambda)$

$$
i_*i^!K\longrightarrow K\longrightarrow Rj_*j^*K.
$$

Extension of scalars commutes with $i_*$, $j^*$ and, by the preceding argument, $Rj_*$. It therefore carries
this triangle to the triangle over $\Lambda'$. The fibre comparison is $i_*\beta_{i,K}$ because the first map is
the counit; hence $\beta_{i,K}$ is an isomorphism. For $q\colon\mathbf P^1_Y\to Y$, the diagonal class and trace
defining the adjunction $Rq_*\dashv q^*(1)[2]$ between $\Dctf(\mathbf P^1_Y,\Lambda)$ and $\Dctf(Y,\Lambda)$ commute with
all the listed coefficient maps: the finite classes are constructed from Kummer and derived scalar extension,
the integral classes are their compatible limits, and the field classes are their scalar extensions
([sk-prop-geo-p1-adjunction] and [sk-prop-diagonal-tower]). For $\mathcal O_E\to A$, the perfectness of $A_X$ proved
above makes its derived tensor commute with the inverse limits defining the integral classes; the resulting
finite-level classes are exactly the finite coefficient classes. Thus $\beta_{q,K}$ is the usual
pullback-and-twist identification. Open restriction and composition give the affine-space case. A finite
affine cover and local factorization as a closed immersion into affine space prove the assertion for every
$f$ ([det-sfb-coefficient-comparisons-exceptional]).

*Tensor product and internal Hom.* Derived extension of scalars $\D(X_{\mathrm{proét}},\Lambda)\to\D(X_{\mathrm{proét}},\Lambda')$
is symmetric monoidal, by associativity of tensor product. For internal Hom, reduce the first argument by
perfect strata and finite cones to $a_!P$, as in the preceding proposition. The identity

$$
R\mathcal Hom_X(a_!P,K)\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K)
$$

commutes with extension of scalars by the comparisons for $Ra_*$, $a^!$, and the dual of a perfect complex.
These are the canonical comparison maps, since all are defined by the same evaluation pairing. Finite cones
give the result for every first argument ([det-sfb-coefficient-comparisons-hom], [thm-coef-finite-hom]).

*Construction of the comparison maps on the ambient categories.* The comparison maps themselves are produced
formally, as conjugates and mates, from the commutation of restriction of scalars with pushforward and
pullback: [def-sfb-comap-mapmod-square], [def-sfb-conjugate-pull-iso], [def-sfb-mate-push-hom],
[def-sfb-comap-lower-star-iso], [def-sfb-pull-iso], [def-sfb-push-hom], [def-sfb-comap-upper-star-iso],
[def-sfb-derived-comap-lower-star-iso], [def-sfb-derived-push-hom], [def-sfb-open-immersion-shriek-iso],
[def-sfb-derived-lower-shriek-hom], [lem-sfb-derived-lower-shriek-hom-iso].
