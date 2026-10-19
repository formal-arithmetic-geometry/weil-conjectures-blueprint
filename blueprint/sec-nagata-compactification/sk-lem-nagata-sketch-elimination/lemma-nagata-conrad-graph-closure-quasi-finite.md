+++
id = "lemma-nagata-conrad-graph-closure-quasi-finite"
kind = "lemma"
title = "The closed graph is quasi-finite over the blow-up (Conrad)"
order = 224
lean = ["AlgebraicGeometry.exists_isAdmissible_locallyQuasiFinite_image_graph"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be qcqs, let $U\subseteq V\subseteq X$ be quasi-compact opens, let
$p\colon Y\to X$ be separated and locally of finite type with $Y$ qcqs, and
let $f\colon U\to Y$ be a section of $p$ over $U$ whose image is closed in
$p^{-1}(V)$. There is a $V$-admissible blow-up
$q\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$ and an open
immersion $\sigma\colon U\hookrightarrow\widetilde X$ with
$q\circ\sigma$ the inclusion of $U$, with the following property. Let
$F=(f,\sigma)\colon U\to Y\times_X\widetilde X$ be the induced morphism
and let $\overline{F(U)}$ be its scheme-theoretic image. Then

$$
\overline{F(U)}\longrightarrow\widetilde X
$$

is quasi-finite (locally quasi-finite, locally of finite type and
quasi-compact) and separated.

Neither $U$ nor $V$ is assumed dense in $X$.
