+++
kind  = "proof"
of    = "det-lem-int-tensor-shriek"
uses = ["sk-prop-integral-criterion", "def-pe-derived-complete", "sk-prop-sf-open-closed-triangle", "sk-def-sfb-constructible", "sk-lem-int-integral-heart"]
+++
By [sk-prop-integral-criterion], $K\in\D(X_{\mathrm{proét}},\mathcal O_E)$ lies in
$\Dbc(X,\mathcal O_E)$ if and only if $K$ is derived complete
([def-pe-derived-complete]) and
$K/\pi_E:=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E)_X$ lies in
$\Dbc(X,\mathcal O_E/\pi_E)$. We verify both conditions.

*Exactness and limits.* Since $X$ is Noetherian, $j$ is quasi-compact. By
[sk-prop-sf-open-closed-triangle] (Stacks, Tags 09BP, 09BM, 09AA), $j_!$ and
$i_*$ are exact on module sheaves, so they act on complexes termwise without
deriving, and both preserve products and derived inverse limits of module
complexes ($j_!$ by loc. cit., $i_*$ because it is exact and a right adjoint).
Both are $\mathcal O_E$-linear and the coefficient sheaves are compatible with
pullback, so for $F\in\{j_!,i_*\}$ there is a natural isomorphism
$F(K\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n))\simeq F(K)\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)$:
both sides are the cone of $\pi_E^n$ on $F(K)$, because the resolution
$\mathcal O_E\xrightarrow{\pi_E^n}\mathcal O_E$ of $\mathcal O_E/\pi_E^n$ computes the reduction
and $F$ is exact.

*Derived completeness.* If $K\to R\varprojlim_nK\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ is an
isomorphism, applying $F$ and the two compatibilities of the previous
paragraph shows that $F(K)\to R\varprojlim_nF(K)\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ is an
isomorphism. So $F$ preserves derived completeness.

*Reduction.* $F(K)/\pi_E\simeq F(K/\pi_E)$, so it suffices that $F$ preserves bounded
constructible complexes with coefficients $\mathcal O_E/\pi_E$. Being exact, $F$
commutes with cohomology sheaves, so it preserves boundedness and it suffices
to treat a constructible sheaf $G$ ([sk-def-sfb-constructible]). If $G$ on $U$
is constructible for a stratification $(U_a)$ of $U$, then the $U_a$ together
with $X\setminus U$ form a finite stratification of $X$ by locally closed
subschemes; $j_!G$ restricts to $G|_{U_a}$ on $U_a$ (as $j^*j_!=\mathrm{id}$) and to
$0$ on $X\setminus U$, so $j_!G$ is constructible. If $G$ on $Z$ is constructible
for a stratification $(Z_b)$ of $Z$, then the $Z_b$ (locally closed in $X$)
together with $X\setminus Z$ stratify $X$; $i_*G$ restricts to $G|_{Z_b}$ on $Z_b$
(as $i^*i_*=\mathrm{id}$) and to $0$ on $X\setminus Z$, so $i_*G$ is constructible.

This proves (1) for $j_!$ and $i_*$, and hence for the composite $a_!=i_*u_!$.

*(2)* By [sk-lem-int-integral-heart] (in the form of its local-model statement)
there is a finite stratification of $X$ such that on each stratum $S$ the
restriction $K|_S$ is pro-étale locally $P\otimes_{\mathcal O_E}\mathcal O_{E,S}$ for a
bounded complex $P$ of finite free $\mathcal O_E$-modules. This local-model property
passes to refinements: if $T\subseteq S$ is locally closed, then $K|_T$ is locally
$P\otimes_{\mathcal O_E}\mathcal O_{E,T}$ on the base-changed cover.

We prove, by Noetherian induction on the closed subscheme $Y\subseteq X$, that for
every $K\in\Dbc(Y,\mathcal O_E)$ with such local models on a finite stratification
of $Y$, the object $K$ is an iterated extension of objects $b_!M$ with
$b\colon S\hookrightarrow Y$ a stratum of a refinement and $M$ a local model; for
$Y=X$ this is (2), and pushing forward along the closed immersion $Y\hookrightarrow X$
(exact, and $i_*b_!=(ib)_!$) gives the analogous statement on $X$.

*An open stratum.* Let $\eta$ be the generic point of an irreducible component of
$Y$ and $Y_a$ the stratum containing it. For $b\neq a$, $\eta\notin\overline{Y_b}$:
$Y_b$ is constructible, so its closure consists of specializations of points of
$Y_b$, and the only point specializing to the generic point $\eta$ of a component
is $\eta$ itself, which is not in $Y_b$. Hence
$W=Y\setminus\bigcup_{b\neq a}\overline{Y_b}$ is a nonempty open subset of $Y$ contained in
$Y_a$. Replace $Y_a$ by the two strata $W$ and $Y_a\setminus W=Y_a\cap(Y\setminus W)$ (locally
closed); by the previous paragraph the local models persist.

*Induction step.* Let $j\colon W\hookrightarrow Y$ and $i\colon Y'=Y\setminus W\hookrightarrow Y$ (reduced
closed complement, a proper closed subscheme). The localization sequence of
[sk-prop-sf-open-closed-triangle], applied termwise, gives a distinguished
triangle
$$
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K\longrightarrow j_!j^*K[1].
$$
Here $j^*K=K|_W$ is a local model on the stratum $W$, so $j_!j^*K$ is a
generator. The complex $i^*K$ lies in $\Dbc(Y',\mathcal O_E)$ (inverse image along a
closed immersion is exact, preserves limits, hence derived completeness, and
preserves constructibility by restricting stratifications), and it has local
models on the induced stratification of $Y'$. By the induction hypothesis
$i^*K$ is an iterated extension of objects $b_!M$ for strata
$b\colon S\hookrightarrow Y'$; then $i_*i^*K$ is an iterated extension of
$i_*b_!M=(ib)_!M$, as $i_*$ is exact. Hence $K$ lies in the stated subcategory.
(The base case $Y=\emptyset$ is trivial.)
