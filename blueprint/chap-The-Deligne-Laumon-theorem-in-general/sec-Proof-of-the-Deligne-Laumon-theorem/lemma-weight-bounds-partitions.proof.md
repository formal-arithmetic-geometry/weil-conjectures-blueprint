+++
kind = "proof"
of = "lemma-weight-bounds-partitions"
order = 1356
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "proposition-six-operations-dctf", "lemma-perfect-complexes-geometric-point", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "lemma-weights-exact-sequence"]
+++
In both cases the restrictions of $K$ are again [mixed](@definition-weights) of weights at
most $w$ (Proposition [proposition-weights-under-usual-operations]),
and we place [$R^qf_!K$](@proposition-construction-independence-rf-shriek) in the middle of an exact sequence of [Weil
sheaves](@definition-weil-structure) whose outer terms are bounded.

For (1), applying [$Rf_!$](@proposition-construction-independence-rf-shriek) and the [composition isomorphism](@proposition-composition-base-change-rf-shriek) to the
triangle $j_!j^*K\to K\to i_*i^*K\to$ gives an exact sequence

$$
\href{@proposition-construction-independence-rf-shriek}{R^q(fj)_!j^*K}\longrightarrow \href{@proposition-construction-independence-rf-shriek}{R^qf_!K}\longrightarrow \href{@proposition-construction-independence-rf-shriek}{R^q(fi)_!i^*K},
$$

which is Frobenius-equivariant by naturality, and
Lemma [lemma-weights-exact-sequence] gives the bound for
[$R^qf_!K$](@proposition-construction-independence-rf-shriek).

For (2), let $j':V_0\to Y_0$ and $i':W_0\to Y_0$ be the inclusions.
Base change for direct images with compact support
(Proposition [proposition-composition-base-change-rf-shriek])
identifies $j'^*\href{@proposition-construction-independence-rf-shriek}{R^qf_!K}$ with [$R^qf_{V!}(K|_{f^{-1}V_0})$](@proposition-construction-independence-rf-shriek) and
$i'^*\href{@proposition-construction-independence-rf-shriek}{R^qf_!K}$ with [$R^qf_{W!}(K|_{f^{-1}W_0})$](@proposition-construction-independence-rf-shriek). By
Lemma [lemma-finite-quasi-finite-direct-images], the outer terms of

$$
0\longrightarrow j'_!j'^*\href{@proposition-construction-independence-rf-shriek}{R^qf_!K}\longrightarrow \href{@proposition-construction-independence-rf-shriek}{R^qf_!K}
\longrightarrow i'_*i'^*\href{@proposition-construction-independence-rf-shriek}{R^qf_!K}\longrightarrow0
$$

are [mixed](@definition-weights) of weights at most $w+q$, and
Lemma [lemma-weights-exact-sequence] gives the bound for the
middle term.
