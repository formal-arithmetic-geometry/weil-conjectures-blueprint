+++
kind = "proof"
of = "sk-thm-geo-generic-open"
uses = ["sk-lem-geo-coordinates", "sk-lem-geo-smooth-generic", "sk-lem-geo-finite-boundary", "sk-thm-pe-direct-image-comparison", "sk-thm-pe-constructible-comparison"]
+++
We prove the assertion for the étale antecedent of $F$ and then transport it
by [sk-thm-pe-direct-image-comparison] and
[sk-thm-pe-constructible-comparison]. These compare the canonical base-change
maps, so the induction below, carried out with the functors between the
categories $D^+(-_{\mathrm{ét}},\Fell)$, proves (G21) and (G22) on the
pro-étale site.

We prove (G21) and (G22) together by induction on $n=\dim X_{k(S)}$, allowing
at each stage all integral bases $S$ of finite type over $k$. In the inductive
step, coordinate projections give the assertions away from a part of $Y$
finite over $S$; when $X$ is smooth and $F$ locally constant,
[sk-lem-geo-smooth-generic] controls the proper direct image to $S$, which by
[sk-lem-geo-finite-boundary] fills in the finite part; and a general $F$
differs from such a sheaf by something supported in smaller dimension.

*Preliminary reductions.* The assertions extend from open to locally closed
immersions with the same source: factor such an immersion as an open immersion
into its scheme-theoretic closure followed by a closed immersion, and note that
closed direct image is exact, preserves constructibility, and commutes with
arbitrary pullback (Stacks, Tag [0959](https://stacks.math.columbia.edu/tag/0959)).
We will use the induction hypothesis in this form. Replacing $Y$ by the
scheme-theoretic closure of $X$, we may assume $X$ dense in $Y$. We may also
shrink $S$ to be affine, and remove the closures of the images of the
irreducible components of $Y$ that do not dominate $S$: there are finitely
many, and none contains the generic point of $S$.

The assertions are local on $Y$, and since we only use finite affine covers,
the finitely many resulting opens of $S$ can be intersected.

*Base case.* If the generic fibre $X_{k(S)}$ is empty, so is $Y_{k(S)}$, by
density. Then $Y$ becomes empty after shrinking $S$: on a finite affine cover,
a coordinate algebra that vanishes over $k(S)$ has its unit killed by a nonzero
element of $\mathcal O(S)$. If $n=0$, the dense open $X_{k(S)}$ of the
zero-dimensional Noetherian space $Y_{k(S)}$ is all of it; the same argument
applied to $Y\setminus X$ shows that $j$ becomes an isomorphism after shrinking
$S$.

Now let $n\geq1$ and assume the theorem, including (G22), for generic fibres of
dimension less than $n$.

*Step 1: for $Y$ projective over $S$, both assertions hold on an open
$G\subset Y$ whose complement is finite over $S$.* Choose charts and
coordinates as in [sk-lem-geo-coordinates]. Via $t_{\alpha r}$, regard
$X\cap Y_\alpha\hookrightarrow Y_\alpha$ as an open immersion of schemes over
the integral base $\mathbf A^1_S$, which is of finite type over $k$. By part
(1) of that lemma its generic fibre has dimension less than $n$, so the
induction hypothesis gives a dense open $V_{\alpha r}\subset\mathbf A^1_S$ over
which both assertions hold. They also hold after a base change in the standing
range $T\to S$: apply the hypothesis to the inverse image of $V_{\alpha r}$ in
$\mathbf A^1_T$. Hence on the finite union $G$ of the opens
$t_{\alpha r}^{-1}(V_{\alpha r})$, the complex $Rj_*F$ is bounded constructible
(there are finitely many pieces, so its cohomology lies in a common finite
range of degrees), and (G22) is an isomorphism. By part (2) of the lemma, after
shrinking $S$ the reduced complement $Z=Y\setminus G$ is finite over $S$.

*Step 2: the theorem holds in dimension $n$ when $X$ is smooth over $S$ and $F$
is locally constant.* First reduce to $Y$ projective. Restrict to a member of a
finite affine cover of $Y$, embed it in affine space over the affine base, and
take its closure in projective space. This affine member, and hence $X$, is
open in that closure. Replacing the closure by the closure of $X$ makes $X$
dense without changing its generic fibre, and a result there restricts to the
affine member. So we may assume $b:Y\to S$ projective.

Step 1 gives $(Rj_*F)|_G\in\Dbc$ with $Z\to S$ finite; also
$Rj_*F\in D^+(Y_{\mathrm{ét}},\Fell)$. Since $bj:X\to S$ is smooth and $F$ is
locally constant, [sk-lem-geo-smooth-generic], after a further shrinking of
$S$, shows that $Rb_*Rj_*F=R(bj)_*F$ lies in $\Dbc(S,\Fell)$ and that its
formation commutes with every base change in the standing range. Part (1) of
[sk-lem-geo-finite-boundary] gives $Rj_*F\in\Dbc(Y,\Fell)$.

For a finite-type $k$-scheme $T\to S$, let $c$ be the map (G22). It is an
isomorphism on $G_T$ by Step 1. By proper base change for $b$ and the
compatibility of base-change maps with composition (Stacks, Tag
[0E46](https://stacks.math.columbia.edu/tag/0E46)), $Rb_{T,*}c$ is identified
with the base-change map for $R(bj)_*F$, which is an isomorphism. Part (2) of
[sk-lem-geo-finite-boundary], over $T$, shows that $c$ is an isomorphism. (A
priori the target of $c$ is only bounded below; the isomorphism shows it is
bounded constructible.)

*Step 3: the general case in dimension $n$.* We first make the smooth locus
large. By Stacks, Tag [0550](https://stacks.math.columbia.edu/tag/0550), after
shrinking $S$ there is a finite universal homeomorphism $S'\to S$ with $S'$
integral, such that $(X_{S'})_{\mathrm{red}}\to S'$ is flat of finite
presentation with geometrically reduced generic fibre. That generic fibre has a
dense smooth open (Stacks, Tag [056V](https://stacks.math.columbia.edu/tag/056V)),
so by the fibrewise criterion (Stacks, Tag
[01V9](https://stacks.math.columbia.edu/tag/01V9)) its generic points lie in
the smooth locus of $(X_{S'})_{\mathrm{red}}\to S'$. After shrinking the base
once more to remove non-dominant components, this smooth locus contains a dense
open of $(X_{S'})_{\mathrm{red}}$. Since $F$ is constructible, there is a
smaller dense open $V$ on which the pullback of $F$ is locally constant. Its
complement contains no generic point of a component of the generic fibre, so
its generic fibre has dimension less than $n$. Passing to reductions and along
finite universal homeomorphisms does not change étale topoi (Stacks, Tag
[03SI](https://stacks.math.columbia.edu/tag/03SI)). We may therefore work over
$S'$, with all schemes replaced by their reductions, and descend to $S$ at the
end.

Let $v:V\hookrightarrow X$ be the open immersion and
$i:X\setminus V\hookrightarrow X$ its reduced closed complement. By Step 2,
after shrinking the base, both $v$ and $jv$ have bounded constructible direct
images of $v^*F$, and their base-change maps are isomorphisms after every base
change in the standing range. Complete the unit of $v^*\dashv Rv_*$ to a
triangle in $D^+(X_{\mathrm{ét}},\Fell)$

$$
F\longrightarrow Rv_*v^*F\longrightarrow D\longrightarrow F[1].
\qquad\text{(G23)}
$$

The first two terms are bounded constructible, hence so is $D$, by Stacks, Tag
[09BH](https://stacks.math.columbia.edu/tag/09BH) and the long exact
cohomology sequence. The unit is an isomorphism on $V$, so $v^*D=0$ and the
localization triangle (G19) of [sk-lem-geo-finite-boundary] gives

$$
D=i_*i^*D.\qquad\text{(G24)}
$$

The locally closed immersion $ji:X\setminus V\to Y$ has generic fibre of
dimension less than $n$. Applying the induction hypothesis to each of the
finitely many constructible cohomology sheaves of $i^*D$, and using their
truncation triangles, we get

$$
R(ji)_*i^*D=Rj_*D\in\Dbc(Y,\Fell),
$$

with base-change maps that are isomorphisms. Now apply $Rj_*$ to (G23). The
middle term is $R(jv)_*v^*F$, treated by Step 2, and the third term was just
treated. Hence $Rj_*F$ is bounded constructible.

For base change along $T$, the base-change map for $v$ identifies the pullback
of the first arrow of (G23) with the unit for $v_T$. Since cones are not
functorial, we fix the triangle for this unit to be the pullback of (G23),
transported through that identification. The base-change map is a natural
transformation $(Rj_*-)|_{Y_T}\to Rj_{T,*}(-|_{X_T})$ of exact functors
$D^+(X_{\mathrm{ét}},\Fell)\to D^+((Y_T)_{\mathrm{ét}},\Fell)$, so it gives a
morphism from the pullback of $Rj_*$ of (G23) to $Rj_{T,*}$ of this triangle.
It is an isomorphism on the second and third terms, hence on the first, which
is (G22).

*Descent to $S$.* A finite universal homeomorphism is a homeomorphism of
underlying spaces. If the argument over $S'$ gives a nonempty open
$U'\subset S'$, remove from $S$ the closed image of $S'\setminus U'$. The
remaining open $U$ is nonempty and its inverse image lies in $U'$. Over $U$,
pullback along $S'_U\to U$ is an equivalence of étale topoi (Stacks, Tag
[03SI](https://stacks.math.columbia.edu/tag/03SI)); it preserves constructible
sheaves in both directions and commutes with direct images and their derived
functors. So it detects boundedness and constructibility, and (G21) holds over
$U$. For a finite-type $k$-scheme $T\to U$, the map $T\times_US'_U\to T$ is
again a universal homeomorphism, and compatibility of base-change maps with
composition identifies the pullback of (G22) to $T\times_US'_U$ with the
base-change map already shown to be an isomorphism over $S'$. Since the
equivalence is conservative, (G22) is an isomorphism over $T$. This completes
the induction.
