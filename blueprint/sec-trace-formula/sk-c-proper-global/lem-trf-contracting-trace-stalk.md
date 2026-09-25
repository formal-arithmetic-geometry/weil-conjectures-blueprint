+++
id = "lem-trf-contracting-trace-stalk"
kind = "theorem"
title = "Trace map of a contracting correspondence"
order = 2508
uses = ["def-trf-categorical-trace", "lem-trf-contracting-local-model", "lem-trf-contracting-normal-cone-evaluation", "lem-trf-frobenius-formal-contraction", "lem-trf-local-term-locality", "lem-trf-trace-map-from-external-duality", "prop-trf-pairing-point-normalization"]
+++
Let $c$ be an admissible correspondence on $X$, let $y\in \operatorname{Fix}(c)(k)$ be an isolated fixed point, and suppose that
the two legs of $c$ agree modulo the square of the maximal ideal at
$y$, as in [lem-trf-frobenius-formal-contraction]. Then the trace
map of [lem-trf-trace-map-from-external-duality] restricted to $y$
is the stalk evaluation: under the identifications of
[lem-trf-local-term-locality],

$$
\theta_{c,K,y}:\RHom_A(K_{\bar y},K_{\bar y})
\longrightarrow A_y
$$

sends the class of $u_{\bar y}$ to
$\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})$, the categorical trace
of [def-trf-categorical-trace].

## Proof

By [lem-trf-contracting-local-model] the situation at the isolated
fixed point is that of the graph correspondence of a contracting
endomorphism of the strict henselization, and the class of
$u_{\bar y}$ is an endomorphism of the stalk $K_{\bar y}$. By
[lem-trf-contracting-normal-cone-evaluation] the trace map at
$y$ is the supported pairing of that class with the normalized Thom
class of the normal cone of the diagonal. By
[prop-trf-pairing-point-normalization] the supported pairing of
two classes on the point is the categorical trace ([def-trf-categorical-trace]) of their composite,
and the normalization clause of
[lem-trf-contracting-normal-cone-evaluation] identifies the Thom
class contribution with the identity of the point; hence the value is
$\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})$, which is the
assertion, the identification of the fixed point with the component
$\{y\}$ being [lem-trf-local-term-locality].
