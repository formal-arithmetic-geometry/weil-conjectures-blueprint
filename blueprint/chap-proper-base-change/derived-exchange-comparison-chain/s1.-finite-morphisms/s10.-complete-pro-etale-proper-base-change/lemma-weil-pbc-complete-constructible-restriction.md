+++
id = "lemma-weil-pbc-complete-constructible-restriction"
kind = "lemma"
title = "Constructible-subcategory restriction"
order = 903
uses = ["def-weil-pbc-a2-constructible-rebind", "lemma-weil-pbc-a2-comparison-rfshriek-transport", "lemma-weil-pbc-a2-reduction-tensor-transport", "lemma-weil-pbc-a2-s7-s10-endpoint-compatibility", "prop-weil-proet-complete-proper-base-change"]
+++
For every proper Cartesian square, the complete base-change isomorphism
restricts to a natural isomorphism on the selected A2 full subcategory:

$$
\xi_K:S(K)=Lg^*_{\mathrm{comp}}Rf_*K
\xrightarrow{\sim}
T(K)=Rf'_*L(g')^*_{\mathrm{comp}}K,
\qquad K\in\mathsf C_\square(X),
$$

where both endpoints lie in $\mathsf C(Y')$. Its finite reductions, $Rf_!$
proper aliases, etale/pro-etale transports, compatible tower endomorphisms,
and identity and pasting equations are the A2 transports of the S7–S10
endpoints. The
restricted isomorphism is independent of all certificate and notation
choices.

## Proof

A rebinding certificate supplies the compatible bounded constructible etale
witnesses required in the complete proposition. Its uniform intervals and
stratifications are exactly the input of S9 bounded reconstruction, while the
perfect coefficient is the two-term resolution used in the reduction
transport lemma. Thus Proposition
[prop-weil-proet-complete-proper-base-change] gives an ambient isomorphism
$\xi_K:S(K)\to T(K)$ and its explicit ambient inverse.

The last field of the certificate exhibits $S(K)$ and $T(K)$ as objects of
the A2 full subcategory $\mathsf C(Y')$. Fullness puts $\xi_K$ and its inverse
in that subcategory, and faithfulness preserves their two inverse equations.
The three transport lemmas identify all A2 and A3 aliases and prove every
finite-reduction and coherence equation. Since the ambient map is constructed
without consulting a membership witness, replacing the certificate changes
neither the map nor its inverse. This proves the claimed restriction with no
additional external hypothesis.
