+++
kind  = "proof"
of    = "lem-fin-finite-boundary-reconstruction"
+++
For any sheaf $E$, the sequence

$$
0\to a_!a^*E\to E\to i_*i^*E\to0
$$

is exact on every geometric stalk, hence exact by
[lemma-weil-pbc-geometric-stalk-conservative].
Here $a_!$ is the extension by zero of
[def-weil-pbc-extension-by-zero].
The four functors in this sequence are exact, so applying the
sequence term by term to a representative of $K$ gives a triangle

$$
a_!a^*K\longrightarrow K\longrightarrow i_*i^*K\longrightarrow .
$$

By [lem-fin-extension-by-zero], $a_!a^*K$ is bounded
constructible. Apply $Rb_*$.
Its image is bounded constructible by
[lem-fin-proper-bounded-constructible], as is $Rb_*K$
by assumption. Their cone $R(bi)_*i^*K$ is bounded constructible,
because the bounded constructible complexes form a triangulated
subcategory [prop-constructible-derived-subcategory] (the cohomology
long exact sequence and the weak Serre property
[thm-constructible-serre]).
Since $bi$ is finite, [lem-fin-finite-reflects-derived]
proves $i^*K\in D^b_c(Z,\Lambda)$.
Exact closed direct image
[lem-fin-closed-immersion] gives the same property for
$i_*i^*K$. Return to the displayed triangle: its outer terms are bounded
constructible, so $K$ is by
[prop-constructible-derived-subcategory].
No identification of $i^*Rj_*$ with a lower-dimensional
open direct image occurs.
