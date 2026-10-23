+++
id = "def-nagata-finite-affine-gluing-presentation"
kind = "definition"
title = "Selected finite affine gluing presentation"
order = 31
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation", "AlgebraicGeometry.Scheme.nonempty_finiteAffineGluingPresentation", "AlgebraicGeometry.Scheme.finiteAffineGluingPresentation"]
+++
A *finite affine gluing presentation* of a scheme $S$ consists of a finite
affine open cover $S=\bigcup_{a}U_a$ together with, for every pair $(a,b)$
of charts, finitely many sections $f_{abr}\in\Gamma(S,U_a)$ and
$g_{abr}\in\Gamma(S,U_b)$ with $D(f_{abr})=D(g_{abr})$ such that

$$
U_a\cap U_b=\bigcup_r D(f_{abr}).
$$

Each $D(f_{abr})$ is thus a basic open both of $U_a$ and of $U_b$, and the
overlap maps are the identifications
$\Gamma(S,U_a)_{f_{abr}}\cong\Gamma(S,D(f_{abr}))\cong\Gamma(S,U_b)_{g_{abr}}$.
We call the $f_{abr}$ and $g_{bar}$ the *basic-open elements* of the chart
$a$.

If $S$ is quasi-compact and quasi-separated, such a presentation exists:
quasi-compactness gives the finite affine cover, and quasi-separatedness
makes each $U_a\cap U_b$ quasi-compact, so it is covered by finitely many
opens that are basic opens both of $U_a$ and of $U_b$. Select one and call
it $\mathsf G_S$.
