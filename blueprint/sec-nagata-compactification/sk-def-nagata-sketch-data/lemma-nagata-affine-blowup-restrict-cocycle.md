+++
id = "lemma-nagata-affine-blowup-restrict-cocycle"
kind = "lemma"
title = "Identity and cocycle laws for affine restriction"
order = 47
lean = ["AlgebraicGeometry.AffineBlowup.hom_comp"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-localization-mul", "lemma-nagata-rees-localization-one", "lemma-nagata-rees-piece-membership", "prop-nagata-affine-blowup-restrict", "prop-nagata-rees-graded"]
+++
Let $\varphi\colon A\to B$ and $\psi\colon B\to C$ be ring homomorphisms and
let $I\subseteq A$, $J\subseteq B$, $K\subseteq C$ be ideals with
$J=\varphi(I)B$ and $K=\psi(J)C$, so that $K=(\psi\varphi)(I)C$. Then the
morphisms of [def-nagata-affine-blowup-restriction-map] satisfy

$$
r_{\psi\varphi}=r_\varphi\circ r_\psi\colon
\operatorname{Bl}_K(\operatorname{Spec}C)\longrightarrow
\operatorname{Bl}_I(\operatorname{Spec}A).
$$
