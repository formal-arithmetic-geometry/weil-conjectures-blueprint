+++
id = "lemma-nagata-conrad-case3-disjointness-reduction"
kind = "lemma"
title = "The disjointness reduction in Case 3 (Conrad)"
order = 318
lean = ["AlgebraicGeometry.exists_isAdmissible_disjoint_closure_range_of_le"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "def-nagata-scheme-theoretic-image", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be qcqs, let $U\subseteq V\subseteq X$ be quasi-compact open
subschemes, let $p\colon Y\to X$ be a morphism with $Y$ qcqs, and let
$f\colon U\to Y$ be a section of $p$ over $U$ whose image is closed in
$p^{-1}(V)$. There is a $V$-admissible blow-up
$q\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$ with the
following property. Let $Z'$ be a scheme with morphisms $r\colon Z'\to Y$
and $p'\colon Z'\to\widetilde X$ such that $p\circ r=q\circ p'$, and let $Y'$
be a scheme with a morphism $f_Y\colon Y'\to U$ and a quasi-compact morphism
$f'\colon Y'\to Z'$ such that $r\circ f'=f\circ f_Y$ (for instance the base
changes of $Y$ and of $f$ along $q$). Then the closure of $f'(Y')$ is
disjoint from $p'^{-1}\bigl(\overline{q^{-1}(V\setminus U)}\bigr)$.
