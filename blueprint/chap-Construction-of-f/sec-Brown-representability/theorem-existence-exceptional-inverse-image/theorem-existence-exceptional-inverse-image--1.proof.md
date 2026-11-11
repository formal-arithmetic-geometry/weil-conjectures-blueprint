+++
kind = "proof"
of = "theorem-existence-exceptional-inverse-image--1"
order = 526003
uses = ["proposition-construction-independence-rf-shriek--1", "lemma-hypotheses-brown-representability--3", "lemma-hypotheses-brown-representability--6", "definition-relative-picard-functor--2"]
+++
For $N\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$, the functor

$$
\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))^{\mathrm{op}}\longrightarrow\operatorname{Ab},
\qquad M\longmapsto\Hom(Rf_!M,N)
$$

is cohomological and sends direct sums to products. By
Lemma [lemma-hypotheses-brown-representability], $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ is
compactly generated, and Brown representability [Stacks, [0A8F](https://stacks.math.columbia.edu/tag/0A8F)] says
that on such a category every cohomological functor sending direct sums
to products is representable, say by $f^!N$. By the
Yoneda lemma, these objects form a right adjoint, and a right adjoint of an
exact functor of triangulated categories is exact [Stacks, [0A8G](https://stacks.math.columbia.edu/tag/0A8G)].

*Source:* the proof of Theorem [theorem-existence-exceptional-inverse-image].
