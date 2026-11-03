+++
id = "lemma-nagata-conrad-disjointness-blowup"
kind = "lemma"
title = "Deligne's disjointness blow-up (Deligne, *Lemme* 0.3) (Conrad)"
order = 219
lean = ["AlgebraicGeometry.disjoint_closure_range_of_blowupMap_sup"]
uses = ["def-nagata-blowup-chart-ring", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-overlap-basic-map", "lemma-nagata-scheme-image-restrict-open", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open"]
+++
Let $X$ be a scheme, let $U\subseteq V\subseteq X$ be opens, and let
$p\colon Z\to X$ and $f\colon Y\to Z$ be morphisms with
$p(f(Y))\subseteq U$; write $\overline Y$ for the scheme-theoretic image of
$f$. Let $\mathcal I_1,\mathcal I_2$ be quasi-coherent ideals on $X$ with
$V\setminus U\subseteq V(\mathcal I_1)$ and
$V(\mathcal I_2)\cap V=\varnothing$, and suppose

$$
\mathcal I_2\mathcal O_Z\subseteq\mathcal I_1^2\mathcal O_Z+\mathcal I_{\overline Y},
$$

that is, the closed subscheme $p^{-1}(V(\mathcal I_1^2))\cap\overline Y$ of
$Z$ factors through $p^{-1}(V(\mathcal I_2))$. Let $q\colon X'\to X$ be the
blow-up of $X$ along $\mathcal I_1+\mathcal I_2$. Let $Z'$ be a scheme with
morphisms $r\colon Z'\to Z$ and $p'\colon Z'\to X'$ such that
$p\circ r=q\circ p'$, and let $Y'$ be a scheme with a morphism
$f_Y\colon Y'\to Y$ and a quasi-compact morphism $f'\colon Y'\to Z'$ such
that $r\circ f'=f\circ f_Y$ (for instance the base changes of $Z$ and $Y$
along $q$). Then the two closed subsets

$$
\overline{f'(Y')},\qquad
p'^{-1}\bigl(\overline{q^{-1}(V\setminus U)}\bigr)
$$

of $Z'$ are disjoint.
