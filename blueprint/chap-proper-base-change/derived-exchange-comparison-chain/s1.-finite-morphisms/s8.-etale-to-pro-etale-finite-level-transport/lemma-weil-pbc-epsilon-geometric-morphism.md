+++
id = "lemma-weil-pbc-epsilon-geometric-morphism"
kind = "lemma"
title = "The comparison functors form a geometric morphism"
order = 1682
uses = ["def-weil-pbc-epsilon-comparison", "lemma-weil-pbc-etale-proetale-continuous", "lemma-weil-pbc-etale-proetale-left-exact"]
+++
For $A$-module sheaves $F$ on $X_{\mathrm{et}}$ and $G$ on
$X_{\mathrm{proet}}$ there is a natural bijection

$$
\operatorname{Hom}_{X_{\mathrm{proet}}}(\epsilon_X^{-1}F,G)
\cong
\operatorname{Hom}_{X_{\mathrm{et}}}(F,\epsilon_{X,*}G),
$$

and $\epsilon_X^{-1}$ preserves finite limits.

## Proof

Restriction along $\iota_X^{\mathrm{op}}$ sends pro-etale sheaves to etale
sheaves by Lemma [lemma-weil-pbc-etale-proetale-continuous]. The left-Kan
extension adjunction, followed by the sheafification adjunction, gives the
displayed bijection.

For a pro-etale object $W$, let $I_W$ be the category of factorizations
$W\to\iota_XU$ with $U$ etale over $X$. It is filtered: the map to $X$
gives an object, two factorizations are dominated by their fiber product over
$X$, and two parallel arrows are equalized by their scheme-theoretic
equalizer, an open etale subobject through which $W$ factors. Filtered
colimits of $A$-modules commute with finite limits. The pointwise Kan
extension therefore preserves finite limits, and $A$-module sheafification
does as well. This proves left exactness of $\epsilon_X^{-1}$ and hence the
geometric-morphism assertion.
