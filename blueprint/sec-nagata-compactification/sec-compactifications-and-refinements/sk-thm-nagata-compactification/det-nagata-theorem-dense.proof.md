+++
kind  = "proof"
of    = "det-nagata-theorem-dense"
uses = ["thm-nagata-compactification", "prop-nagata-dense-refinement", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-immersion-open-in-scheme-image"]
+++
By [thm-nagata-compactification] there is a compactification
$C=(X\xrightarrow{j_0}\overline X_0\xrightarrow{p_0}S)$ with $j_0$ an open
immersion and $p_0$ proper.

*Step 1: $j_0$ is quasi-compact.* The morphism $p_0$ is proper, hence
separated and in particular quasi-separated, and $p_0\circ j_0=f$ is
quasi-compact because $f$ is of finite type. A morphism whose composite with
a quasi-separated morphism is quasi-compact is itself quasi-compact
([lemma-nagata-open-immersion-qc-over-separated-target]); so $j_0$ is a
quasi-compact open immersion.

*Step 2: schematic closure.* Let $\overline X\subseteq\overline X_0$ be the
scheme-theoretic image of $j_0$. Since $j_0$ is a quasi-compact immersion,
[lemma-nagata-immersion-open-in-scheme-image] shows that $j_0$ factors as a
quasi-compact open immersion $j:X\to\overline X$ followed by the closed
immersion $\overline X\hookrightarrow\overline X_0$, and that $j$ is
scheme-theoretically dense: the ideal of $\overline X$ is
$\ker(\mathcal O_{\overline X_0}\to j_{0,*}\mathcal O_X)$, so
$\mathcal O_{\overline X}\to j_*\mathcal O_X$ is injective.

*Step 3: properness.* The composite $p:\overline X\hookrightarrow
\overline X_0\xrightarrow{p_0}S$ is a closed immersion followed by a proper
morphism, hence proper, and $p\circ j=p_0\circ j_0=f$. This is the dense
refinement $\mathsf{Dense}(C)$ of [prop-nagata-dense-refinement], and it is
the required dense compactification.
