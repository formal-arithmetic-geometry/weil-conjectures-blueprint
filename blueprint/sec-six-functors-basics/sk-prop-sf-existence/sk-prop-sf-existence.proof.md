+++
kind = "proof"
of = "sk-prop-sf-existence"
uses = ["sk-lem-brown-hypotheses"]
+++
For $N\in\Loc(\Dctf(Y,\Lambda))$, the functor

$$
\Loc(\Dctf(X,\Lambda))^{\mathrm{op}}\longrightarrow\Ab,\qquad
M\longmapsto\Hom(Rf_!M,N)
$$

is cohomological and sends direct sums to products. By
[sk-lem-brown-hypotheses], $\Loc(\Dctf(X,\Lambda))$ is compactly generated, and
Brown representability ([Stacks, Tag 0A8F](https://stacks.math.columbia.edu/tag/0A8F))
says that on such a category every cohomological functor sending direct sums to
products is representable. This gives a representing object $f^!N$. By the
Yoneda lemma, these objects form a right adjoint, and a right adjoint of an
exact functor of triangulated categories is exact
([Stacks, Tag 0A8G](https://stacks.math.columbia.edu/tag/0A8G)).

To see that $f^!$ preserves direct sums, we test the canonical map
$\bigoplus_\alpha f^!N_\alpha\to f^!(\bigoplus_\alpha N_\alpha)$ on a compact
generator $G\in\Dctf(X,\Lambda)$ and its shifts. Since both $G$ and
$Rf_!G\in\Dctf(Y,\Lambda)$ are compact, adjunction identifies the two Hom groups
with $\bigoplus_\alpha\Hom(Rf_!G[n],N_\alpha)$. We conclude because the
generators detect isomorphisms.
