+++
kind  = "proof"
of    = "lemma-nagata-valuation-pair-factors-comparison"
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-valuation-factor-closed"]
+++
Since $g_1$ and $g_2$ agree over $S$, they define
$(g_1,g_2)\colon\operatorname{Spec}(A)\to X_1\times_SX_2$. Both generic
maps come from $\eta$ through $U_i\subseteq V_i$, and $\psi_i$ restricts to
the inclusion on $U_i$, so their compositions with $\psi_1$ and $\psi_2$
agree in $U$; hence the generic pair lands in $V_1\times_UV_2=V_{12}$.
Composing with the canonical image-factor map gives a factorization of the
generic pair through $X_{12}$. Apply
[lemma-nagata-valuation-factor-closed] to the domain $A$, the closed
immersion $X_{12}\hookrightarrow X_1\times_SX_2$ and the morphism
$(g_1,g_2)$. It extends the generic factorization to a morphism
$l\colon\operatorname{Spec}(A)\to X_{12}$, and $p_i\circ l=g_i$ because
$p_i$ is the restriction of the $i$-th projection.
