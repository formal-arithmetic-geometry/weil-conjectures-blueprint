+++
kind  = "proof"
of    = "prop-weil-pbc-preservation-constructible"
+++
By [thm-weil-pbc-amplification-proper] the three conditions
$$
 \mathrm{AMP}(\square;2e),\qquad\mathrm{WIT}(\square),\qquad\mathrm{TOW}(\square)
$$
of [def-weil-pbc-finite-level-amplification],
[def-weil-pbc-witness-compatibility] and [def-weil-pbc-tower-preservation]
hold for $c=2e$, so the argument below applies. Let
$K\in\Dbc(X_{\Proet},A)$ have all reductions supported in $[a,b]$, so that
its reduction tower is uniformly bounded constructible in the sense of
[def-weil-pbc-bounded-constructible-complete] with compatible etale-origin
witnesses. By the amplification $\mathrm{AMP}(\square;c)$ and the tower
preservation $\mathrm{TOW}(\square)$, the levelwise tower functors carry
this tower to uniformly bounded constructible towers whose local models have
amplitude compatible with the containments, and by the witness compatibility
of [def-weil-pbc-witness-compatibility] the compatible etale-origin
witnesses are carried to compatible witnesses. By the reconstruction lemma
for uniform towers each of the four derived limits is then realized by its
local models, hence lies in the bounded constructible complete category, is
derived complete and has the stated reduction amplitude; and by the
direct-image-limits proposition the four limits are exactly $Rf_*K$,
$Lg^*_{\mathrm{comp}}Rf_*K$, $Lg'^*_{\mathrm{comp}}K$ and
$Rf'_*Lg'^*_{\mathrm{comp}}K$, which proves the assertions.
