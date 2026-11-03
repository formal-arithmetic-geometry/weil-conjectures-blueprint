+++
kind = "proof"
of = "sk-i-global-additivity"
uses = ["sk-i-relative-frob", "sk-p-trace"]
+++
Since Frobenius preserves opens defined over the finite field, its
square with $j$ is cartesian, and base change gives the correspondences on
$j^*K$ and $j_!j^*K$. The Frobenius square of the closed complement is
cartesian only after passing to reductions, and we obtain the
correspondences on $i^*K$ and $Ri_*i^*K$ from
Lemma [sk-i-relative-frob](1)–(2) and nilpotent invariance.
We apply the functorial localization triangle $j_!j^*K\to K\to Ri_*i^*K$
to the Frobenius correspondence and take direct images with
compact support. This gives a
cofibre sequence of perfect complexes with compatible endomorphisms, and
the identity of traces follows from Proposition [sk-p-trace].
Finally, Lemma [sk-i-relative-frob](3) for $j$ and $i$ identifies the
endomorphisms $T_{c_m}$ of the cohomology of $j_!j^*K$ and $Ri_*i^*K$ with those on $U$ and
$Z$.
