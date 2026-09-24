+++
id = "lem-trf-localization-diagonal"
kind = "lemma"
title = "Localization in the diagonal case"
order = 3922
uses = ["def-trf-correspondence", "def-trf-global-operator", "lem-trf-devissage-generation", "prop-trf-pairing-point-normalization", "prop-trf-trace-formal-laws"]
+++
Let $X$ be proper over
$s$, let $c=\Delta_X:X\to X\times_sX$ be the diagonal correspondence
(so that $F=X$), and let $u$ be the canonical coefficient map of
the diagonal, i.e. the class corresponding to the identity
endomorphism of $K\in D^b_{ctf}(X,A)$ under the supported-class
bijection of [def-trf-correspondence]. Then

$$
\operatorname{tr}_A\bigl(T_c(u)\mid R\Gamma_c(X,K)\bigr)
=\int_X\operatorname{Tr}_c(u)
\qquad\text{in }A .
$$

## Proof

For the diagonal correspondence both legs equal the identity, so the
composite of [def-trf-global-operator] is the identity
endomorphism of $R\Gamma_c(X,K)$; by the formal laws for the
categorical trace ([prop-trf-trace-formal-laws]) its trace is the
alternating sum of the ranks of the (perfect) cohomology of
$R\Gamma_c(X,K)$.
For the other side we use the supported pairing of the trace-formula chapter: by
the point normalization [prop-trf-pairing-point-normalization],
pairing the class $\operatorname{Tr}_c(u)$ with the class of a test
correspondence at a point gives the categorical trace of the composite
of the two coefficient maps. Devissage over the generating class of
[lem-trf-devissage-generation] reduces the verification of the
identity of classes to the verification of their pairings with all test
classes, and each such pairing is the categorical trace of the
corresponding composite operator, which for the diagonal class is
again the alternating sum of the ranks above; hence
$\int_X\operatorname{Tr}_c(u)$ equals the same element of $A$. This
proves the diagonal case.
