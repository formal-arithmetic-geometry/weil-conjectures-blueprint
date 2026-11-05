+++
kind = "proof"
of = "lemma-filtered-trace-morphism"
order = 934
+++
The trace morphism is the composite of four steps: the exceptional
tensor–Hom adjunction, external duality, the adjoint of evaluation
along the diagonal, and exceptional proper base change for the closed
diagonal. Since each is defined by units, counits and tensor evaluation,
the composite has a filtered version

$$
\cHom_F(c_2^*\mathcal K,c_1^!\mathcal K)
\simeq c^!(\mathcal K\boxtimes_F\mathbb D_F\mathcal K)
\longrightarrow Ri_{c*}\omega_{\Fix(c)}
$$

whose graded pieces, computed by
Lemma [lemma-graded-pieces-filtered-operations], are the unfiltered
versions. In particular the filtered comparison for external duality is
an isomorphism, because each of its graded maps is a finite sum of the
isomorphisms in Lemma [lemma-external-duality-trace-morphism], and
graded pieces detect isomorphisms of finitely filtered complexes.
Forgetting the filtration we recover the trace morphism for $K$.

The target is pure of weight zero, so $\operatorname{tr}_F$ vanishes on
$F^1$, and its restriction to $F^0$ factors through $\operatorname{gr}^0$.
This factorization holds on filtered dg models, hence also in the
filtered derived category. By Lemma [lemma-graded-pieces-filtered-operations],
$\operatorname{gr}^0$ of the source is $\bigoplus_a\cHom(c_2^*K_a,c_1^!K_a)$.
Now the steps for internal Hom and external duality preserve the two indices, and on a pair of equal indices evaluation along the diagonal is the
evaluation of $K_a$. Hence the map on the summand $a$ is the trace
morphism for $K_a$.
