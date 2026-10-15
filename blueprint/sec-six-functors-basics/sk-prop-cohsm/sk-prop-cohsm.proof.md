+++
kind = "proof"
of = "sk-prop-cohsm"
uses = ["sk-prop-pe-unbounded-classical", "sk-lem-geo-affine-local", "sk-prop-geo-p1-adjunction"]
+++
Represent the classical objects by their étale antecedents, so that the
functors below are those between the categories $D(-_{\mathrm{ét}},\Lambda)$.
[sk-prop-pe-unbounded-classical] and the functor comparisons identify the
adjunctions and canonical maps below with the pro-étale ones. The coordinate
charts form a pro-étale covering, so the computed local isomorphisms prove the
pro-étale statement.

Both maps are defined globally as adjoint transposes, and we check locally
that they are isomorphisms. Write $\epsilon_N:Rf_!f^!N\to N$, a morphism in
$D(S_{\mathrm{ét}},\Lambda)$, for the counit of $Rf_!\dashv f^!$ (for the projective
line this is the counit (G7) of [sk-prop-geo-p1-adjunction]). The map (G11)
is the transpose of the morphism in $D(S_{\mathrm{ét}},\Lambda)$

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)\xrightarrow{\ \sim\ }N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{\ 1\otimes\epsilon_{\Lambda_S}\ }N,\qquad\text{(G13)}
$$

the first arrow being the projection formula. The map (G12) is the transpose,
for $f'$, of the morphism in $D(S'_{\mathrm{ét}},\Lambda)$

$$
Rf'_!g'^*f^!N\xrightarrow{\ \sim\ }g^*Rf_!f^!N\xrightarrow{\ g^*\epsilon_N\ }g^*N,\qquad\text{(G14)}
$$

where the first arrow is the inverse of the base-change isomorphism for $Rf_!$
(Stacks, Tag 0F7L).

*Local charts.* By the local structure of smooth morphisms (Stacks, Tag 054L),
every point of $X$ has an affine open neighbourhood $u:U\hookrightarrow X$
mapping into an affine open $v:V\hookrightarrow S$, together with a separated
étale map $e:U\to\mathbf A^d_V$ such that $fu=vae$, where $a:\mathbf A^d_V\to V$ is
the projection. By [sk-lem-geo-affine-local] and uniqueness of right adjoints,
in $D(U_{\mathrm{ét}},\Lambda)$

$$
u^*f^!N=e^*a^*v^*N(d)[2d],\qquad u^*\omega_f=\Lambda_U(d)[2d].\qquad\text{(G15)}
$$

In particular $\omega_f$ has a single nonzero cohomology sheaf, in degree
$-2d$, and it is locally free of rank one.

*(G11) is an isomorphism.* Under (G15), source and target of (G11) are both
$e^*a^*v^*N(d)[2d]$, and one must check that the map is the obvious
reassociation of tensor product and twist. Compare transposes: both are the
projection formula followed by the counit for $v$, the $d$ affine-line counits,
and the étale counit for $e$. They agree by the formula for the counit of a
composite in [sk-lem-geo-affine-local]. So (G11) is an isomorphism on each such
$U$, hence on $X$.

*(G12) is an isomorphism.* Consider first each type of chart separately. For
the projective line, the unit (G6) and counit (G7) of
[sk-prop-geo-p1-adjunction] commute with base change, so transposing (G14)
gives the ordinary pullback identification $g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$.
Restriction to the affine line and composition give the same for affine space.
For a separated étale map, extension by zero is the direct sum over the
geometric sheets and commutes with base change, and its counit is the sum of
the evaluations; so here too the transpose of (G14) is the ordinary
inverse-image identification. To combine these, use that base change for
$Rf_!$ is compatible with composition (Stacks, Tag 0F7L) and that the counit of
a composite is the composite of the counits. Substituting this into (G14)
shows that the restriction of (G12) to $U\times_XX'$ is the composite of the
étale, affine-space and open-immersion cases just treated, so (G12) is an
isomorphism on a cover of $X'$.

Applying the same calculation to (G13), base change respects its projection
map and its counit, and the resulting commutative square is the compatibility
of (G11) with (G12).
