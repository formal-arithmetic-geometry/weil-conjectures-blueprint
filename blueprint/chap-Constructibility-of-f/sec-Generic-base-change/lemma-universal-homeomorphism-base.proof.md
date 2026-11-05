+++
kind = "proof"
of = "lemma-universal-homeomorphism-base"
order = 579
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions", "definition-compactification-refinement"]
+++
A finite universal homeomorphism is a homeomorphism of underlying spaces,
so we may remove from $S$ the closed image of $S'\setminus U'$. The remaining
open $U$ is nonempty, and its inverse image $S'_U$ lies in $U'$. Over $U$
the morphisms $X'_U\to X_U$ and $Y'_U\to Y_U$ are finite universal
homeomorphisms, and pullback along them is therefore an equivalence of étale
topoi [Stacks, [03SI](https://stacks.math.columbia.edu/tag/03SI)]. Such equivalences preserve constructibility in both
directions and commute with $Rj_*$. Hence pullback along these morphisms
detects boundedness and constructibility, and we get
$Rj_{U,*}(F|_{X_U})\in\Dbc(Y_U,\Fell)$.

For base change, let $T\to U$ be a $k$-scheme of finite type, with
projections $g_X:X_T\to X$ and $g_Y:Y_T\to Y$, and let

$$
\beta_T:g_Y^*Rj_*F\longrightarrow Rj_{T,*}g_X^*F
$$

be the base change map for $j$ along $T$. Put $T'=T\times_US'_U$. Then
$v:T'\to T$ is again a universal homeomorphism, and so are the induced maps
$v_X:X'_{T'}\to X_T$ and $v_Y:Y'_{T'}\to Y_T$, each a thickening followed by
a base change of $v$. Let $\beta'_{T'}:g_{Y'}^*Rj'_*F'\to Rj'_{T',*}g_{X'}^*F'$ be the
base change map for $j'$ along $T'$. Base change maps compose
[Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)], and $v_Y^*Rj_{T,*}\simeq Rj'_{T',*}v_X^*$ because $v_X^*$ and
$v_Y^*$ are equivalences of étale topoi [Stacks, [03SI](https://stacks.math.columbia.edu/tag/03SI)]. Hence $v_Y^*\beta_T$ is
identified with $\beta'_{T'}$. The map $\beta'_{T'}$ is an isomorphism by
assumption, so $v_Y^*\beta_T$ is one. Since $v_Y^*$ is an equivalence, it is
conservative, and therefore $\beta_T$ is an isomorphism.
