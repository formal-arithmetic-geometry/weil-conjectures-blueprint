+++
kind = "proof"
of = "theorem-generic-constructibility-base-change-rj"
order = 583
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-detection-proper-direct-image", "lemma-coordinate-projections", "lemma-generic-smooth-open", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-finite-morphisms-cohomology"]
+++
We work with the étale sheaf corresponding to $F$, in
$D^+(-_{\acute{e}t},\Fell)$, and prove (6.19) and $\beta_T$
together by induction on
$n=\dim X_{k(S)}$, allowing at each stage all integral bases $S$ of
finite type over $k$. We first handle the complement of a finite set by
passing to the base $\mathbf A^1_S$, then the smooth, locally constant
case, and finally the general case by dévissage.

*Preliminary reductions.* Several modifications of the data are
harmless, and we will make them freely in the induction. First, the
assertions extend from open to locally closed immersions with the same
source. Indeed, such an immersion factors as an open immersion into its
scheme-theoretic closure followed by a closed immersion. Since closed direct
image is exact, preserves constructibility, and commutes with arbitrary
pullback [Stacks, [0959](https://stacks.math.columbia.edu/tag/0959)], the assertions pass along this factorization. We will use the induction hypothesis in this form.
Next, replacing $Y$ by the scheme-theoretic closure of $X$, we may assume
that $X$ is dense in $Y$. We may also shrink $S$ to be affine, and we may
remove the closures of the images of the irreducible components of $Y$
that do not dominate $S$, since there are finitely many of them and none
contains the generic point of $S$. Finally, the assertions are local on
$Y$. Since we only use finite affine covers, the finitely many resulting
opens of $S$ can be intersected.

*Base case.* If the generic fibre is empty or zero-dimensional,
then after shrinking $S$ the immersion $j$ becomes an isomorphism or $Y$
becomes empty. Suppose first that $X_{k(S)}$ is empty. By density
$Y_{k(S)}$ is empty. On a finite affine cover, a coordinate algebra that
vanishes over $k(S)$ has its unit killed by a nonzero element of
$\mathcal O(S)$. Hence $Y$ becomes empty after shrinking $S$. If $n=0$,
the dense open $X_{k(S)}$ of the zero-dimensional Noetherian space
$Y_{k(S)}$ is all of $Y_{k(S)}$. The same argument applied to
$Y\setminus X$ shows that $j$ becomes an isomorphism after shrinking $S$.

Now let $n\geq1$, and assume the theorem, including $\beta_T$, for
generic fibres of dimension less than $n$.

*Step 1: for $Y$ projective over $S$, both assertions hold on
an open $G\subset Y$ whose complement is finite over $S$.* We replace the
base $S$ by the larger base $\mathbf A^1_S$, over which the generic fibre is
smaller, so that the induction hypothesis applies. To do this, choose charts and
coordinates as in Lemma [lemma-coordinate-projections]. Via
$t_{\alpha r}$, we regard $X\cap Y_\alpha\hookrightarrow Y_\alpha$ as an
open immersion of schemes over the integral base $\mathbf A^1_S$, which is
of finite type over $k$. By part (1) of that lemma, its generic fibre has
dimension less than $n$. Therefore the induction hypothesis, applied over the base
$\mathbf A^1_S$ to the restriction of $F$, gives a dense open
$V_{\alpha r}\subset\mathbf A^1_S$ over which both assertions hold.

Since $Rj_*$ commutes with restriction to the open $Y_\alpha$, the
assertions hold for $Rj_*F$ on $t_{\alpha r}^{-1}(V_{\alpha r})$. They
continue to hold after a base change $T\to S$ with $T$ of finite type over
$k$, as we see by applying the hypothesis to the inverse image of
$V_{\alpha r}$ in $\mathbf A^1_T$. Let $G$ be the finite union of the opens
$t_{\alpha r}^{-1}(V_{\alpha r})$. Then on $G$ the map $\beta_T$ is an isomorphism, and the complex $Rj_*F$ is bounded constructible. For the
boundedness, note that there are finitely many pieces, and therefore the
cohomology lies in a common finite range of degrees. Finally, part (2) of
the lemma shows that, after shrinking $S$, the reduced complement
$Z=Y\setminus G$ is finite over $S$.

*Step 2: the theorem holds in dimension $n$ when $X$ is
smooth over $S$ and $F$ is locally constant.* We may assume that $Y$ is
projective over $S$. Indeed, let $Y_\beta$ be a member of a finite affine
cover of $Y$, embed it in some $\mathbf A^m_S$ over the affine base,
and let $\overline Y$ be the closure of $X\cap Y_\beta$ in
$\mathbf P^m_S$. Then $X\cap Y_\beta$ is open and dense in
$\overline Y$, which is projective over $S$. Moreover $X\cap Y_\beta$ is
still smooth over $S$, with generic fibre of dimension at most $n$. The
result for $X\cap Y_\beta\subset\overline Y$ gives it on $Y_\beta$, because
$Rj_*$ and its base change maps commute with restriction to opens of the
target.

For $Y$ projective, Step 1 gives an open $G\subset Y$ with complement
finite over $S$ on which both assertions hold. Since $X$ is smooth over $S$
and $F$ is locally constant,
Lemma [lemma-extension-across-finite-subset] applies. It shows that
the assertions hold on all of $Y$ after shrinking $S$.

*Step 3: the general case in dimension $n$.* We find a dense open
$V\subset X$ to which Step 2 applies, and treat the difference between
$F$ and $Rv_*v^*F$, which lives on the smaller set $X\setminus V$, by the
induction hypothesis. Let $S'\to S$ and $V$ be as in
Lemma [lemma-generic-smooth-open].
Lemma [lemma-universal-homeomorphism-base] shows that it suffices to prove
the theorem for $(X_{S'})_{\mathrm{red}}\hookrightarrow(Y_{S'})_{\mathrm{red}}$
and the pullback of $F$ over $S'$. Its generic fibre still has dimension
$n$ because $S'\to S$ is a universal homeomorphism. We therefore replace
$S$ by $S'$ and all schemes by these reductions. Then $V\subset X$ is a
dense open, smooth over $S$, on which $F$ is locally constant. The
generic fibre of $X\setminus V$ has dimension less than $n$.

Let $v:V\hookrightarrow X$ be the open immersion and
$i:X\setminus V\hookrightarrow X$ its reduced closed complement. By
Step 2, after shrinking the base, both $v$ and $jv$ have bounded
constructible direct images of $v^*F$. Their base change maps are
isomorphisms after every base change $T\to S$ with $T$ of finite type
over $k$. Complete the unit of
$v^*\dashv Rv_*$ to a triangle

$$
\Delta_F:\ F\longrightarrow Rv_*v^*F\longrightarrow D
\longrightarrow F[1].
\tag{6.21}
$$

The first term is the constructible sheaf $F$, and the second is
bounded constructible by Step 2. Hence $D$ is bounded constructible too.
Indeed, by the long exact cohomology sequence, its cohomology sheaves are
extensions of kernels by cokernels of maps between constructible sheaves,
and these are constructible [Stacks, [09BH](https://stacks.math.columbia.edu/tag/09BH)]. Moreover $v^*D=0$, as the unit
is an isomorphism on $V$. The localization triangle
(6.18) for $v$ and $i$ now shows that

$$
D=i_*i^*D.
$$

The locally closed immersion $ji:X\setminus V\to Y$ has generic fibre
of dimension less than $n$. We apply the induction hypothesis to each of
the finitely many constructible cohomology sheaves of $i^*D$, together
with their truncation triangles. This gives

$$
R(ji)_*i^*D=Rj_*D\in\Dbc(Y,\Fell),
$$

with base change maps that are isomorphisms. Now apply $Rj_*$ to
the triangle $\Delta_F$. In the resulting triangle, the middle term
$R(jv)_*v^*F$ is bounded constructible by Step 2, and the third term
$Rj_*D$ was treated just now. Hence $Rj_*F$ is bounded constructible.

To see that the base change map $\beta_T$ is an isomorphism, we
compare the triangle $\Delta_F$ with its analogue over $T$. Let
$g_X:X_T\to X$, $g_Y:Y_T\to Y$ and $g_V:V_T\to V$ be the projections, and
$v_T:V_T\to X_T$ the base change of $v$. The base change map

$$
\beta_v:g_X^*Rv_*v^*F\longrightarrow Rv_{T,*}g_V^*v^*F
$$

is an isomorphism by Step 2, and it carries $g_X^*$ of the first arrow of
the triangle $\Delta_F$ to the unit $g_X^*F\to Rv_{T,*}v_T^*g_X^*F$ of
$v_T^*\dashv Rv_{T,*}$. Since cones are not functorial, we have to choose the
triangles compatibly, and we take as triangle for this unit the pullback of
the triangle $\Delta_F$, transported through $\beta_v$. Now the base change map

$$
\beta_j:g_Y^*Rj_*\longrightarrow Rj_{T,*}g_X^*
$$

is a natural transformation of exact functors. It therefore induces a morphism from
$g_Y^*$ of $Rj_*$ of the triangle $\Delta_F$ to $Rj_{T,*}$ of this
triangle. On the second term it is $\beta_j$ at $Rv_*v^*F$ followed by
$Rj_{T,*}\beta_v$. Since base change maps compose [Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)], this
composite is the base change map for $jv$, an isomorphism by Step 2. On the third term it is $\beta_j$ at $D$. It is an isomorphism because,
composed with $Rj_{T,*}$ of the base change isomorphism for the closed
immersion $i$ [Stacks, [0959](https://stacks.math.columbia.edu/tag/0959)], it is the base change map for $ji$ at $i^*D$
treated above. Hence, by the five lemma for triangles, it is an
isomorphism on the first term, which is $\beta_T$.

This completes the induction.
