+++
kind = "proof"
of = "lemma-weight-bounds-partitions--2"
order = 1355005
uses = ["definition-w-local-w-strictly-local--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "theorem-enough-affine-weakly-contractible-objects--1", "lemma-integral-models--3", "proposition-proper-direct-image-constructible-complexes--7", "proposition-proper-direct-image-constructible-complexes--8", "proposition-six-operations-dctf--4", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "lemma-perfect-complexes-geometric-point--6", "definition-weights--2", "definition-weights--6", "lemma-subobjects-quotients-weil-sheaves--2", "proposition-weights-under-usual-operations--9", "proposition-weights-under-usual-operations--10", "lemma-finite-quasi-finite-direct-images--2", "lemma-finite-quasi-finite-direct-images--3", "lemma-weights-exact-sequence--1", "definition-compactification-refinement--3"]
+++
In both cases the restrictions of $K$ are again mixed of weights at
most $w$ (Proposition [proposition-weights-under-usual-operations]),
and we place $R^qf_!K$ in the middle of an exact sequence of Weil
sheaves whose outer terms are bounded.

For (2), let $j':V_0\to Y_0$ and $i':W_0\to Y_0$ be the inclusions.
Base change for direct images with compact support
(Proposition [proposition-composition-base-change-rf-shriek])
identifies $j'^*R^qf_!K$ with $R^qf_{V!}(K|_{f^{-1}V_0})$ and
$i'^*R^qf_!K$ with $R^qf_{W!}(K|_{f^{-1}W_0})$. By
Lemma [lemma-finite-quasi-finite-direct-images], the outer terms of

$$
0\longrightarrow j'_!j'^*R^qf_!K\longrightarrow R^qf_!K
\longrightarrow i'_*i'^*R^qf_!K\longrightarrow0
$$

are mixed of weights at most $w+q$, and
Lemma [lemma-weights-exact-sequence] gives the bound for the
middle term.

*Source:* the proof of Lemma [lemma-weight-bounds-partitions].
