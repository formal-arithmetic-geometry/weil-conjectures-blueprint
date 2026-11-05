+++
kind = "proof"
of = "proposition-frobenius-local-term-curve--1"
order = 993002
uses = ["proposition-extension-zero-restriction-closed-subscheme", "lemma-lift-correspondence-invariant-decomposition", "lemma-closed-piece-pushforward", "proposition-additivity-trace-classes", "definition-pushforward-correspondence", "lemma-vanishing-local-term-zero-stalk", "theorem-proper-pushforward-lefschetz-verdier", "lemma-local-terms-point"]
+++
Let $j:U=X\setminus\{x\}\hookrightarrow X$. The open and closed pieces
of the localization triangle are

$$
K^U=j_!j^*K,\qquad K^Z=Rx_*x^*K.
$$

The induced coefficient map on $K^U$ is obtained by restricting
$\psi$ to the inverse image of $U$, applying open base change, and
extending by zero. The coefficient on $K^Z$ is defined as the proper
pushforward of $\psi_x$ along $(x,x)$, as in
[definition-pushforward-correspondence]. These maps are compatible with
the arrows of the localization triangle
([lemma-lift-correspondence-invariant-decomposition] and
[lemma-closed-piece-pushforward]). The graph case of
[proposition-additivity-trace-classes], formalized by
`Correspondence.traceClass_ofGraph_eq_add`, therefore gives

$$
\operatorname{LT}_B(\psi)
=\operatorname{LT}_B(\psi^Z)+\operatorname{LT}_B(\psi^U).
$$

Extension by zero has zero stalk at $x$. Applying the
$\Qbarl$-form of [lemma-vanishing-local-term-zero-stalk] to $K^U$
and its induced coefficient map gives
$\operatorname{LT}_B(\psi^U)=0$. This is the application of
`Correspondence.localTerm_traceClass_frobeniusGraph_eq_zero_of_smooth`
in the Lean proof.

For the closed piece, let $e:s\to B$ be the factorization of
$\tilde x$ through $b$. Proper pushforward compatibility
([theorem-proper-pushforward-lefschetz-verdier]) identifies the
restriction of its trace class to $B$ with
$e_*\operatorname{Tr}(\psi_x)$. Integration commutes with this proper
pushforward, so

$$
\operatorname{LT}_B(\psi^Z)
=\int_s\operatorname{Tr}(\psi_x)
=\operatorname{tr}_{\Qbarl}(\psi_x\mid K_x),
$$

where the last equality is [lemma-local-terms-point], using the
dualizability of $K_x$. Lean packages this reduction from a zero open
local term to the stalk trace in
`Correspondence.localTerm_traceClass_ofGraph_eq_trace_of_localTerm_eq_zero`.
