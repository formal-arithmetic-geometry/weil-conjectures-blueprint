+++
kind = "proof"
of = "lemma-universal-homeomorphism-base"
order = 573
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions", "definition-compactification-refinement"]
+++
A finite universal homeomorphism is a homeomorphism of underlying spaces.
We remove from $S$ the closed image of $S'\setminus U'$. The remaining
open $U$ is nonempty, and its inverse image $S'_U$ lies in $U'$. Over $U$,
the morphisms $X'_U\to X_U$ and $Y'_U\to Y_U$ are finite universal
homeomorphisms. Pullback along them is therefore an equivalence of étale
topoi [Stacks, [03SI](https://stacks.math.columbia.edu/tag/03SI)]. These equivalences preserve constructibility in both
directions and commute with $Rj_*$. Hence pullback along these morphisms
detects boundedness and constructibility, and we get
$Rj_{U,*}(F|_{X_U})\in\Dbc(Y_U,\Fell)$.

For base change, let $T\to U$ be a $k$-scheme of finite type. Then
$T'=T\times_US'_U\to T$ is again a universal homeomorphism. By the
compatibility of base change maps with composition, the pullback of the
base change map for $j$ along $T$ is the base change map for $j'$ along
$T'$. The latter is an isomorphism by assumption. Pullback along the
universal homeomorphism $Y'_{T'}\to Y_T$ is an equivalence of étale
topoi, hence conservative. Therefore the base change map for $j$ along $T$
is an isomorphism.
