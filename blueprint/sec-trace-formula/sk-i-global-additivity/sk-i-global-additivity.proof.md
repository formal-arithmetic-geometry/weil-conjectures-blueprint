+++
kind = "proof"
of = "sk-i-global-additivity"
uses = ["sk-i-relative-frob", "sk-p-trace"]
+++
Frobenius preserves opens defined over the finite field, so its
square with $j$ is Cartesian. For the closed complement, whose
Frobenius square is Cartesian only after passing to reductions, use
Lemma [sk-i-relative-frob] (1)–(2) and nilpotent invariance.
Applying the functorial localization triangle $j_!j^*K\to K\to Ri_*i^*K$
to the Frobenius correspondence and then compact-support pushforward
produces a
coherently equivariant cofibre sequence of perfect complexes, and
Proposition [sk-p-trace] gives the identity of traces.
Lemma [sk-i-relative-frob] (3) for $j$ and $i$ identifies the
global operators of $j_!j^*K$ and $Ri_*i^*K$ with those on $U$ and
$Z$.
