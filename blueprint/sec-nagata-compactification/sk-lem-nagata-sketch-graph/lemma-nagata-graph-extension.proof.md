+++
kind  = "proof"
of    = "lemma-nagata-graph-extension"
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-global-blowup", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "lem-weil-pbc-closed-immersion-from-composite", "lemma-nagata-admissible-blowup-over-open", "thm-nagata-global-blowup-proper", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-partial-section", "prop-nagata-global-blowup-cover-independent"]
+++
**Construction.** Write $u\colon U\to S$ and
$C=(V\xrightarrow{j}Y\xrightarrow{p}S)$ for the given compactification.
Define

$$
Z_V=\operatorname{SIm}
\bigl(V\xrightarrow{(j,\,\mathrm{incl})}Y\times_SU\bigr).
$$

Apply [def-nagata-elimination-indeterminacy] to the first projection
$Z_V\to Y$ over the open $j(V)\subseteq Y$. Denote the resulting blow-up by
$\pi\colon Y^{\mathrm{gr}}\to Y$ and the open strict transform by
$Z_V^{\mathrm{st}}\hookrightarrow Y^{\mathrm{gr}}$. Define

$$
V^{\mathrm{gr}}\subseteq Y^{\mathrm{gr}}
\quad\text{to be the represented open subscheme }Z_V^{\mathrm{st}},
\qquad
\psi^{\mathrm{gr}}\colon V^{\mathrm{gr}}\longrightarrow U
$$

by transporting the second projection
$Z_V^{\mathrm{st}}\to U$ across the open-immersion identification.

**Verification.** This is Stacks Project, Tag 0F3Z (Lemma 38.33.6), applied
to the separated finite-type morphism $U\to S$, the quasi-compact open
$V\subseteq U$, and the compactification $C$. First, the inputs of the
construction are legitimate. Since $S$ is qcqs and $Y\to S$ is proper, $Y$
is qcqs. Since $V$ is quasi-compact and $S$ is quasi-separated, $V\to S$ is
quasi-compact, so $j$ is quasi-compact by
[lemma-nagata-open-immersion-qc-over-separated-target]; in particular
$j(V)\subseteq Y$ is a quasi-compact open. The projection $Z_V\to Y$ is the
composite of a closed immersion with the base change $Y\times_SU\to Y$ of
$u$, hence separated and of finite type. By
[lemma-nagata-scheme-image-partial-section], applied to the quasi-compact
open immersion $j$ and the separated morphism $u$, the inverse image of
$j(V)$ in $Z_V$ maps isomorphically to $V$.

By [lemma-nagata-elimination-indeterminacy], $\pi$ is a $V$-admissible
blow-up and the strict transform $Z_V^{\mathrm{st}}\to Y^{\mathrm{gr}}$ is an
open immersion, so $V^{\mathrm{gr}}$ is an open subscheme of
$Y^{\mathrm{gr}}$. By [lemma-nagata-strict-transform-ambient-closed], the
strict transform is a closed subscheme of $Y^{\mathrm{gr}}\times_SU$. Since
$Y^{\mathrm{gr}}\to S$ is proper by [thm-nagata-global-blowup-proper], the
projection $Y^{\mathrm{gr}}\times_SU\to U$ is proper, and so is its
restriction to the closed subscheme $Z_V^{\mathrm{st}}$; this restriction is
$\psi^{\mathrm{gr}}$. The two projections of $Z_V^{\mathrm{st}}$ come from
$Y^{\mathrm{gr}}\times_SU$, so $u\circ\psi^{\mathrm{gr}}=p\circ
\pi|_{V^{\mathrm{gr}}}$.

Finally, [lemma-nagata-scheme-image-partial-section] identifies the graph
image over the open $j(V)\subseteq Y$ with $V$, while
[lemma-nagata-strict-transform-over-complement] identifies the admissible
blow-up with the identity over that open. Therefore

$$
V^{\mathrm{gr}}\cap(Y^{\mathrm{gr}}\times_YV)=V
$$

as schemes. This gives an open immersion $v\colon V\to V^{\mathrm{gr}}$ with
$\pi\circ v=j$; the second projection agrees with the original inclusion on
this open, i.e. $\psi^{\mathrm{gr}}\circ v$ is the inclusion
$V\subseteq U$; and the inverse image of $V\subseteq U$ under
$\psi^{\mathrm{gr}}$ is exactly $v(V)$, mapped isomorphically onto $V$.
For the last point, apply [lemma-nagata-scheme-image-partial-section] also
with the roles of the factors exchanged, to the quasi-compact open immersion
$V\hookrightarrow U$ (quasi-compact because $V$ is quasi-compact and $U$ is
quasi-separated over the quasi-separated $S$) and the separated morphism
$p$: the part of $Z_V$ over $V\subseteq U$ is $V$, lying over
$j(V)\subseteq Y$. Hence every point of $V^{\mathrm{gr}}$ over
$V\subseteq U$ lies over $j(V)$, where $\pi$ is an isomorphism, and so lies
in $v(V)$.
These are the data and conditions of a graph extension of $C$
([def-nagata-graph-extension]).
