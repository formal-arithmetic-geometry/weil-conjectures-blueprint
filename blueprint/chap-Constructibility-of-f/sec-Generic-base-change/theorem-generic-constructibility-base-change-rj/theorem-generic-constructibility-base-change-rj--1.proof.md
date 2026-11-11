+++
kind = "proof"
of = "theorem-generic-constructibility-base-change-rj--1"
order = 583002
uses = ["lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "definition-underived-base-change-map--1", "lemma-identity-pasting--2", "lemma-identity-pasting--3", "lemma-acyclic-resolutions--1", "lemma-finite-morphisms--2", "lemma-smooth-morphisms-locally-constant-sheaves--1", "lemma-coordinate-projections--1", "lemma-coordinate-projections--2", "lemma-extension-across-finite-subset--1", "lemma-generic-smooth-open--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "lemma-finite-direct-images--2"]
+++
We prove clauses [theorem-generic-constructibility-base-change-rj--1] and [theorem-generic-constructibility-base-change-rj--2] together. Since
$S_0\subset S$ is open, a morphism $t:T\to S$ with image in $S_0$ factors
through $S_0$, and then $X_T=(X_{S_0})_T$ and $Y_T=(Y_{S_0})_T$. Write
$F_0=F|_{X_{S_0}}$.

*Step 1: $\Lambda=\Fell$ and $T$ of finite type over $k$.* The prime
$\ell$ is invertible on $S$. The argument of
the proof of Theorem [theorem-generic-constructibility-base-change-rj], applied to the étale sheaf
$F$, gives a nonempty open $S_0$ for which (6.19) holds and
(6.20) is an isomorphism for every $k$-scheme $T\to S_0$ of
finite type.

*Step 2: finite $\Lambda$ and $T$ of finite type over $k$.* Let $N$
be a positive integer killing $\Lambda$ and invertible on $S$. Then
$\Lambda$ is the product of its $p$-primary parts for the primes $p$
dividing $N$, and $F$, $Rj_*$, the inverse images and the base change maps
decompose accordingly. So we may assume that $\Lambda$ is killed by $p^r$
for a prime $p$ invertible on $S$. The functors $Rj_*$ commute with the
forgetful functors to $\mathbf Z/p^r$-modules [Stacks, [0D6J](https://stacks.math.columbia.edu/tag/0D6J)], the base
change maps are built from units and counits and so commute with them
too, and a $\Lambda$-sheaf is constructible if and only if its underlying
sheaf is, as shown in the proof of Corollary [corollary-open-direct-image-over-field]. So we
may assume $\Lambda=\mathbf Z/p^r$. The filtration
$F\supset pF\supset\cdots\supset p^rF=0$ has constructible
$\mathbf F_p$-sheaves as successive quotients. Apply Step 1 to each of
these $r$ quotients and intersect the resulting opens to get $S_0$. The
short exact sequences of the filtration are triangles, and $Rj_{S_0,*}$
and $Rj_{T,*}g_{X,0}^*$ carry them to triangles. By induction on $r$ and
the long exact cohomology sequences, $Rj_{S_0,*}F_0$ is bounded with
constructible cohomology sheaves, these being extensions of kernels by
cokernels of maps between constructible sheaves [Stacks, [09BH](https://stacks.math.columbia.edu/tag/09BH)]. The base
change maps form morphisms between these triangles, so they are
isomorphisms by the five lemma.

*Step 3: noetherian $T$.* Let $T\to S_0$ with $T$ noetherian. By
[Stacks, [09MV](https://stacks.math.columbia.edu/tag/09MV)], $T=\varprojlim_\lambda T_\lambda$ for a directed system of
$S_0$-schemes $T_\lambda$ of finite presentation over $S_0$, hence of
finite type over $k$, with affine transition morphisms. Write
$F_\lambda$ and $F_T$ for the pullbacks of $F_0$ to $X_{T_\lambda}$ and $X_T$, and
$h_\lambda:Y_T\to Y_{T_\lambda}$, $h_{\mu\lambda}:Y_{T_\mu}\to Y_{T_\lambda}$
for the projections. Base change maps are compatible with composition of
cartesian squares. Hence the base change map (6.20) for $T$
is $h_\lambda^*$ of the one for $T_\lambda$ followed by the base change map
$\gamma_\lambda:h_\lambda^*Rj_{T_\lambda,*}F_\lambda\to Rj_{T,*}F_T$ for
$T\to T_\lambda$, and similarly for $T_\mu\to T_\lambda$. By Step 2 the
base change maps for $T_\lambda$ and $T_\mu$ are isomorphisms, and so
$h_{\mu\lambda}^*R^ij_{T_\lambda,*}F_\lambda\to R^ij_{T_\mu,*}F_\mu$ is an
isomorphism for $\mu\geq\lambda$. The open immersions $j_{T_\lambda}$ are base changes of $j$, which is
quasi-compact because $Y$ is Noetherian, so they are quasi-compact and
quasi-separated; and $X_T=\varprojlim_\lambda X_{T_\lambda}$,
$Y_T=\varprojlim_\lambda Y_{T_\lambda}$ with affine transition morphisms.
So by [Stacks, [0EYM](https://stacks.math.columbia.edu/tag/0EYM)]

$$
R^ij_{T,*}F_T=\varinjlim_\mu h_\mu^{-1}R^ij_{T_\mu,*}F_\mu,
$$

a colimit whose transition maps are isomorphisms. Thus $H^i(\gamma_\lambda)$
is an isomorphism for every $i$, and so is (6.20) for $T$.

Finally, (6.20) identifies $Rj_{T,*}g_X^*F$ with
$g_{Y,0}^*Rj_{S_0,*}F_0$. By (6.19) and since inverse image
preserves boundedness and constructibility, this lies in
$\Dbc(Y_T,\Lambda)$.
