+++
kind = "proof"
of = "sk-thm-geo-generic-open"
uses = ["sk-lem-geo-coordinates", "sk-lem-geo-smooth-generic", "sk-lem-geo-finite-boundary"]
+++
We work with the étale sheaf corresponding to $F$, in
$D^+(-_{\acute{e}t},\Fell)$.

We prove (7.19) and (7.20) together by induction on
$n=\dim X_{k(S)}$, allowing at each stage all integral bases $S$ of
finite type over $k$.

*Preliminary reductions.* The assertions extend from open to
locally closed immersions with the same source. To see this, factor
such an immersion as an open immersion into its scheme-theoretic
closure followed by a closed immersion, and note that closed direct image is
exact, preserves constructibility, and commutes with arbitrary pullback
[Stacks, Tag 0959](https://stacks.math.columbia.edu/tag/0959). We will use the induction hypothesis in this form.
Replacing $Y$ by the scheme-theoretic closure of $X$, we may assume
that $X$ is dense in $Y$.
We may also shrink $S$ to be affine, and remove
the closures of the images of the irreducible components of $Y$ that
do not dominate $S$, since there are finitely many of them and none
contains the generic point of $S$.
The assertions are local on $Y$, and since we only use finite affine
covers, the finitely many resulting opens of $S$ can be intersected.

*Base case.* If the generic fibre $X_{k(S)}$ is empty, so is
$Y_{k(S)}$, by density, and then $Y$ becomes empty after shrinking
$S$. Indeed, on a finite affine cover, a coordinate algebra that vanishes
over $k(S)$ has its unit killed by a nonzero element of
$\mathcal O(S)$. If $n=0$, the dense open $X_{k(S)}$ of the
zero-dimensional Noetherian space $Y_{k(S)}$ is all of $Y_{k(S)}$, and the same
argument applied to $Y\setminus X$ shows that $j$ becomes an
isomorphism after shrinking $S$.

Now let $n\geq1$, and assume the theorem, including (7.20), for
generic fibres of dimension less than $n$.

*Step 1: for $Y$ projective over $S$, both assertions hold on
an open $G\subset Y$ whose complement is finite over $S$.* Choose
charts and coordinates as in Lemma [sk-lem-geo-coordinates]. Via
$t_{\alpha r}$, we regard $X\cap Y_\alpha\hookrightarrow Y_\alpha$ as an
open immersion of schemes over the integral base $\mathbf A^1_S$,
which is of finite type over $k$. By part (1) of that lemma, its
generic fibre has dimension less than $n$. Hence the induction
hypothesis provides a dense open $V_{\alpha r}\subset\mathbf A^1_S$ over
which both assertions hold. Since $Rj_*$ commutes with restriction to
the open $Y_\alpha$, they hold for $Rj_*F$ on
$t_{\alpha r}^{-1}(V_{\alpha r})$. They also hold after a base
change $T\to S$ with $T$ of finite type over $k$, as we see by applying the
hypothesis to the inverse image of
$V_{\alpha r}$ in $\mathbf A^1_T$. Therefore, on the finite union $G$
of the opens $t_{\alpha r}^{-1}(V_{\alpha r})$, the complex
$Rj_*F$ is bounded constructible (there are finitely many pieces, so
its cohomology lies in a common finite range of degrees), and (7.20) is
an isomorphism. By part (2) of the lemma, after shrinking $S$, the
reduced complement $Z=Y\setminus G$ is finite over $S$.

*Step 2: the theorem holds in dimension $n$ when $X$ is
smooth over $S$ and $F$ is locally constant.* We first reduce to the case
where $Y$ is projective. Let $Y_\beta$ be a member of a finite affine
cover of $Y$, embed it in some $\mathbf A^m_S$ over the affine base,
and let $\overline Y$ be the closure of $X\cap Y_\beta$ in
$\mathbf P^m_S$. Then $X\cap Y_\beta$ is open and dense in
$\overline Y$, which is projective over $S$, and $X\cap Y_\beta$ is
still smooth over $S$, with generic fibre of dimension at most $n$. Since $Rj_*$ and its base
change maps commute with restriction to opens of the target, the result
for $X\cap Y_\beta\subset\overline Y$ gives it on $Y_\beta$. Hence we
may assume that $b:Y\to S$ is projective.

By Step 1, we have $(Rj_*F)|_G\in\Dbc$ with $Z\to S$ finite, and moreover
$Rj_*F\in D^+(Y_{\acute{e}t},\Fell)$. Since $bj:X\to S$ is smooth and $F$
is locally constant, Lemma [sk-lem-geo-smooth-generic], after a
further shrinking of $S$, shows that $Rb_*Rj_*F=R(bj)_*F$ lies in
$\Dbc(S,\Fell)$ and that its formation commutes with base change
along every $T\to S$ of finite type over $k$. By part (1) of
Lemma [sk-lem-geo-finite-boundary], we conclude that
$Rj_*F\in\Dbc(Y,\Fell)$.

For a $k$-scheme $T\to S$ of finite type, let $\varphi$ be the map (7.20), which is an
isomorphism on $G_T$ by Step 1. By proper base change for $b$ and
the compatibility of base change maps with composition [Stacks, Tag 0E46](https://stacks.math.columbia.edu/tag/0E46),
$Rb_{T,*}\varphi$ is identified with the base change map for $R(bj)_*F$,
which is an isomorphism. Applying part (2) of
Lemma [sk-lem-geo-finite-boundary] over $T$, which is possible since
$b_T$ is proper and $b_Ti_T$ is finite, we see that $\varphi$ is
an isomorphism. A priori the target of $\varphi$ is only bounded below, and
the isomorphism shows that it is bounded constructible.

*Step 3: the general case in dimension $n$.* We first arrange that
the smooth locus is large. By [Stacks, Tag 0550](https://stacks.math.columbia.edu/tag/0550), after shrinking $S$, there is a
finite universal homeomorphism $S'\to S$ with $S'$ integral, such
that $(X_{S'})_{\mathrm{red}}\to S'$ is flat of finite presentation
with geometrically reduced generic fibre. This generic fibre has a dense
smooth open [Stacks, Tag 056V](https://stacks.math.columbia.edu/tag/056V), and hence, by the fibrewise criterion [Stacks, Tag 01V9](https://stacks.math.columbia.edu/tag/01V9),
its generic points lie in the smooth locus of
$(X_{S'})_{\mathrm{red}}\to S'$. After shrinking the base once more to
remove non-dominant components, this smooth locus contains a dense open
of $(X_{S'})_{\mathrm{red}}$. Since $F$ is constructible, there is a
smaller dense open $V$ on which the pullback of $F$ is locally
constant. Its complement contains no generic point of a component of
the generic fibre, so its generic fibre has dimension less than $n$.
Passing to reductions and along finite universal homeomorphisms does
not change étale topoi [Stacks, Tag 03SI](https://stacks.math.columbia.edu/tag/03SI). We may therefore work over
$S'$, with all schemes replaced by their reductions, and descend to
$S$ at the end.

Let $v:V\hookrightarrow X$ be the open immersion and
$i:X\setminus V\hookrightarrow X$ its reduced closed complement. By
Step 2, after shrinking the base, both $v$ and $jv$ have bounded
constructible direct images of $v^*F$, and their base change maps are
isomorphisms after every base change $T\to S$ with $T$ of finite
type over $k$. We complete the unit of
$v^*\dashv Rv_*$ to a triangle

$$
F\longrightarrow Rv_*v^*F\longrightarrow D
\longrightarrow F[1].
\tag{7.21}
$$

The first two terms are bounded constructible, and hence so is $D$, by
[Stacks, Tag 09BH](https://stacks.math.columbia.edu/tag/09BH) and the long exact cohomology sequence. Since the unit is an
isomorphism on $V$, we have $v^*D=0$, and the localization triangle
(7.18) for $v$ and $i$ shows that

$$
D=i_*i^*D.
$$

The locally closed immersion $ji:X\setminus V\to Y$ has generic fibre
of dimension less than $n$. Applying the induction hypothesis to each
of the finitely many constructible cohomology sheaves of $i^*D$, and
using their truncation triangles, we obtain

$$
R(ji)_*i^*D=Rj_*D\in\Dbc(Y,\Fell),
$$

with base change maps that are isomorphisms. Now apply $Rj_*$ to
(7.21). The middle term becomes $R(jv)_*v^*F$, which was treated in Step 2,
and the third term was treated just now. Hence $Rj_*F$ is bounded constructible.

For base change along $T$, the base change map for $v$ identifies
the pullback of the first arrow of (7.21) with the unit for $v_T$.
Since cones are not functorial, we fix the triangle for this unit to be
the pullback of (7.21), transported through that identification. The
base change map is a natural transformation
$g_Y^*Rj_*\to Rj_{T,*}g_X^*$ of exact functors, where
$g_X:X_T\to X$ and $g_Y:Y_T\to Y$ are the projections. Hence it
induces a morphism from the pullback of $Rj_*$ of (7.21) to $Rj_{T,*}$
of this triangle. This morphism is an isomorphism on the second and third terms,
and hence on the first, which is (7.20).

*Descent to $S$.* A finite universal homeomorphism is a
homeomorphism of underlying spaces. If the argument over $S'$ gives a
nonempty open $U'\subset S'$, we remove from $S$ the closed image of
$S'\setminus U'$. The remaining open $U$ is nonempty, and its inverse
image lies in $U'$. Over $U$, the morphisms
$(X_{S'_U})_{\mathrm{red}}\to X_U$ and $(Y_{S'_U})_{\mathrm{red}}\to Y_U$
are finite universal homeomorphisms, so pullback along them is an
equivalence of étale topoi [Stacks, Tag 03SI](https://stacks.math.columbia.edu/tag/03SI). These equivalences preserve
constructibility in both directions and commute with $Rj_*$. Hence
pullback along these morphisms detects boundedness and constructibility, and
(7.19) holds over $U$. For a $k$-scheme $T\to U$ of finite type, the map
$T\times_US'_U\to T$ is again a universal homeomorphism, and the
compatibility of base change maps with composition identifies the
pullback of (7.20) to $T\times_US'_U$ with the base change map that we
have already shown to be an isomorphism over $S'$. Since pullback along
the universal homeomorphism $Y_{T\times_US'_U}\to Y_T$ is an equivalence
of étale topoi, hence conservative, (7.20) is an isomorphism over $T$. This completes the
induction.
