+++
kind = "proof"
of = "det-geo-open-finiteness-base-change"
+++
*Step 0: the base-change map is a morphism of triangulated functors.* Both
$g_Y^*Rj_*$ and $Rj_{T,*}g_X^*$ are exact functors
$D^+(X_{\mathrm{ét}},\Lambda)\to D^+((Y_T)_{\mathrm{ét}},\Lambda)$, and
$\operatorname{BC}$ is built from the unit of $g_X^*\dashv Rg_{X,*}$, the
counit of $g_Y^*\dashv Rg_{Y,*}$ and the composition isomorphisms of derived
direct images, all of which commute with shifts and carry distinguished
triangles to morphisms of distinguished triangles. Hence for every
distinguished triangle $K'\to K\to K''\to K'[1]$ in
$D^+(X_{\mathrm{ét}},\Lambda)$ the maps $\operatorname{BC}(K')$,
$\operatorname{BC}(K)$, $\operatorname{BC}(K'')$ form a morphism of
distinguished triangles, and $\operatorname{BC}(K[m])=\operatorname{BC}(K)[m]$.
By the five lemma on cohomology sheaves, if two of the three maps are
isomorphisms, so is the third.

*Step 1: reduction to $\Lambda=\mathbf Z/\ell^r\mathbf Z$.* Let
$\operatorname{For}$ denote the forgetful functor from $\Lambda$-modules to
$\mathbf Z/\ell^r\mathbf Z$-modules along $\mathbf Z/\ell^r\mathbf Z\to\Lambda$.
It is exact, commutes with $g_X^*$, $g_Y^*$ (computed on sheaves), and with the
derived direct images $Rj_*$, $Rj_{T,*}$, $Rg_{X,*}$, $Rg_{Y,*}$ (Stacks, Tag
[0D6J](https://stacks.math.columbia.edu/tag/0D6J); for $\Lambda$ an
$\Fell$-algebra this is [lem-fin-coefficients-forgetful-direct-image]),
compatibly with the units and counits of the adjunctions $g^*\dashv Rg_*$.
Therefore $\operatorname{For}(\operatorname{BC}_\Lambda(K))=
\operatorname{BC}_{\mathbf Z/\ell^r}(\operatorname{For}K)$. The functor
$\operatorname{For}$ does not change cohomology sheaves, so it is conservative;
and a constructible $\Lambda$-sheaf has constructible underlying abelian sheaf,
because a finite locally constant $\Lambda$-module sheaf is finite locally
constant as an abelian sheaf ($\Lambda$ is finite). So
$\operatorname{For}K\in\Dbc(X_{\mathrm{ét}},\mathbf Z/\ell^r\mathbf Z)$, and it
suffices to treat $\Lambda=\mathbf Z/\ell^r\mathbf Z$.

*Step 2: constructible sheaves killed by $\ell$.* Let $F$ be a constructible
sheaf with $\ell F=0$. It is a constructible $\Fell$-sheaf, and by
[lem-fin-coefficients-forgetful-direct-image] its derived direct images may be
computed with $\Fell$-coefficients, compatibly with pullback and with the
base-change map (as in Step 1). Apply [thm-fin-deligne-generic-open] with
$S=\operatorname{Spec}k$: it gives a nonempty open $U\subset S$, and the only
nonempty open of $\operatorname{Spec}k$ is $S$ itself, so $U=S$. Since $T$ is
of finite type over $k$, it is Noetherian, so the theorem says that
$\operatorname{BC}(F)$ is an isomorphism.

*Step 3: constructible sheaves killed by $\ell^s$.* Induct on $s\ge1$, the
case $s=1$ being Step 2. If $\ell^sF=0$, consider the short exact sequence of
sheaves

$$
0\longrightarrow\ell F\longrightarrow F\longrightarrow F/\ell F\longrightarrow0 .
$$

The sheaf $\ell F$ is the image and $F/\ell F$ the cokernel of multiplication
by $\ell$ on $F$, so both are constructible by [thm-constructible-serre].
Moreover $\ell^{s-1}(\ell F)=0$ and $\ell(F/\ell F)=0$. The sequence gives a
distinguished triangle in $D^+(X_{\mathrm{ét}},\mathbf Z/\ell^r\mathbf Z)$; by
induction and Step 2, $\operatorname{BC}(\ell F)$ and
$\operatorname{BC}(F/\ell F)$ are isomorphisms, so $\operatorname{BC}(F)$ is
one by Step 0. Since $\ell^rF=0$ for every
$\mathbf Z/\ell^r\mathbf Z$-sheaf, this covers all constructible sheaves.

*Step 4: bounded constructible complexes.* Induct on the number of nonzero
cohomology sheaves of $K$. If there is one, $K\simeq\mathcal H^m(K)[-m]$ and
Steps 0 and 3 apply. Otherwise, choose $m$ with $\tau^{\le m}K$ and
$\tau^{>m}K$ both having fewer nonzero cohomology sheaves; both are bounded
constructible, and the truncation triangle
$\tau^{\le m}K\to K\to\tau^{>m}K\to$ together with Step 0 finishes the
induction.

Finally, $g_Y^*Rj_*K$ is bounded constructible because $Rj_*K$ is
([cor-fin-deligne-open-finite-coefficients]) and pullback preserves
constructibility of cohomology sheaves; the isomorphism
$\operatorname{BC}(K)$ transfers this to $Rj_{T,*}g_X^*K$.
