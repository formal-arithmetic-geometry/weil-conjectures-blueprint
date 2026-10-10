+++
kind  = "proof"
of    = "pqf-lem-image-proper"
+++
The morphism $X\to Z$ is an $S$-morphism with $X$ proper over $S$ and
$Z$ separated over $S$, hence proper by
[lem-weil-pbc-proper-to-separated] of the ambient-foundations chapter; in particular
it is surjective onto $Z=f(X)$. It remains to see that $Z\to S$ is
proper. It is separated and of finite type: $Z\hookrightarrow Y$ is a
closed immersion (hence separated and of finite type) and $Y\to S$ is
separated of finite type, so the composite $Z\to S$ is separated and
of finite type by
[def-weil-pbc-scheme-conventions]. It is universally closed:
after any base change $T\to S$, write $q_T:X_T\to Z_T$ and
$g_T:Z_T\to T$. Both $q_T$ and $g_Tq_T$ are proper by
[lem-weil-pbc-proper-base-change]. The morphism $q_T$ is
surjective: its geometric
fibres are field extensions of the nonempty fibres of the surjection
$X\to Z$, hence nonempty, so
[lem-weil-pbc-surjective-nonempty-fibres] applies.
The composite $g_Tq_T:X_T\to T$ is proper by
[lem-weil-pbc-proper-base-change], and therefore closed by
[pqf-lem-proper-closed-map]. For any closed subset $C\subset Z_T$,
the subset $q_T^{-1}(C)\subset X_T$ is closed and surjectivity gives

$$
g_T(C)=(g_Tq_T)\bigl(q_T^{-1}(C)\bigr).
$$

The right side is closed in $T$. Thus every $g_T$ is closed,
and $Z\to S$ is separated, of
finite type and universally closed, i.e. proper by
[def-weil-pbc-scheme-conventions].
