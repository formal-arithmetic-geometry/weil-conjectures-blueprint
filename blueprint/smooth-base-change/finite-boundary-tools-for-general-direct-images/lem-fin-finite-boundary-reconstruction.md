+++
id = "lem-fin-finite-boundary-reconstruction"
kind = "lemma"
title = "Recovering constructibility at a finite boundary"
order = 5224
lean = ["AlgebraicGeometry.Etale.mem_Dbc_of_finite_boundary"]
uses = ["sbc-def-coefficient-conventions", "lem-fin-extension-by-zero", "lem-fin-proper-bounded-constructible", "lem-fin-finite-reflects-derived", "lem-fin-closed-immersion"]
+++
Let $b:Y\to S$ be proper between finite-type schemes, with the finite
coefficients of [sbc-def-coefficient-conventions]. Let
$a:G\hookrightarrow Y$ be open, with closed complement
$i:Z\hookrightarrow Y$, and assume $bi:Z\to S$ is finite. For
$K\in D^+(Y,\Lambda)$, suppose $a^*K$ and the direct image $Rb_*K$ belong to
their respective bounded constructible categories. Then
$K\in\Dbc(Y,\Lambda)$.

## Proof

For any sheaf $E$, the sequence
$$
0\to a_!a^*E\to E\to i_*i^*E\to0
$$
is exact on every geometric stalk, hence exact. Here $a_!$ is extension by
zero. The four functors in this sequence are exact, so applying the sequence
term by term to a representative of $K$ gives a triangle
$$
a_!a^*K\longrightarrow K\longrightarrow i_*i^*K\longrightarrow.
$$

By [lem-fin-extension-by-zero], $a_!a^*K$ is bounded constructible. Apply
$Rb_*$. Its image is bounded constructible by
[lem-fin-proper-bounded-constructible], as is $Rb_*K$ by assumption. Their
cone $R(bi)_*i^*K$ is bounded constructible, by the cohomology long exact
sequence and the weak-Serre property.

Since $bi$ is finite, [lem-fin-finite-reflects-derived] proves
$i^*K\in\Dbc(Z,\Lambda)$. Exact closed direct image
[lem-fin-closed-immersion] gives the same property for $i_*i^*K$. Return to
the displayed triangle and use the same long exact sequence to prove it for
$K$. No identification of $i^*Rj_*$ with a lower-dimensional open direct
image occurs.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, def:weil-pbc-extension-by-zero, lem:weil-pbc-geometric-stalk-conservative, lem:weil-pbc-constructible-serre
