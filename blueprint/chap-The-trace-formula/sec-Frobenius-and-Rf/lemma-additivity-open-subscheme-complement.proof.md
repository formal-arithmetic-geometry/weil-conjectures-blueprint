+++
kind = "proof"
of = "lemma-additivity-open-subscheme-complement"
order = 1004
uses = ["proposition-pro-etale-coverings", "lemma-inverse-image-coefficient-sheaves", "lemma-reduction-derived-nakayama", "proposition-proper-base-change-degree-zero", "proposition-proper-base-change-etale-site", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex"]
+++
The four induced correspondences come from base change, and $R\Gamma_c$
of the localization triangle is a two-step filtered object with an
endomorphism, on which traces add.

Since Frobenius preserves opens defined over the finite field, its
square with $j$ is cartesian, and by base change we get the correspondences on
$j^*K$ and $j_!j^*K$. The Frobenius square of the closed complement, however, is cartesian only after passing to reductions, and we obtain the
correspondences on $i^*K$ and $Ri_*i^*K$ from
Lemma [lemma-comparison-via-relative-frobenius](1)–(2) and nilpotent invariance.
We then apply the functorial localization triangle $j_!j^*K\to K\to Ri_*i^*K$
to the Frobenius correspondence and take direct images with
compact support. Since the triangle is functorial, the Frobenius
correspondence becomes an endomorphism of a two-step filtered object, and hence
the traces add by Proposition [proposition-properties-trace].
Finally, Lemma [lemma-comparison-via-relative-frobenius](3) for $j$ and $i$ identifies the
endomorphisms $T_{c_m}$ of the cohomology of $j_!j^*K$ and $Ri_*i^*K$ with those on $U$ and
$Z$.
