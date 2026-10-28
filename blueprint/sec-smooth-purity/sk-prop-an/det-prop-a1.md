+++
id = "det-prop-a1"
kind = "proposition"
title = "Rank-one orientation: the fundamental class of the zero section"
order = 3227
uses = ["det-def-purity-conv", "det-prop-a1-kummer"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineLineZero"]
+++
In the conventions of [det-def-purity-conv], for $Y$ separated finite type
and the zero section $s:Y\hookrightarrow\Aaf^1_Y$, the complex
$Rs^{!}\Lambda_{\Aaf^1_Y}(1)[2]$ is concentrated in degree zero, and its
cohomology sheaf is identified with the constant sheaf by the normalized
Kummer boundary: the map of sheaves on $Y$

$$
\Lambda_Y\ \xrightarrow{\ \sim\ }\
\mathcal H^0\bigl(Rs^{!}\Lambda_{\Aaf^1_Y}(1)[2]\bigr),\qquad
1\longmapsto\partial\kappa(t),
$$

is an isomorphism (so $\mathcal H^0$ is lisse of rank one, and its generator
$\partial\kappa(t)$ restricts to the normalized generator $1$ at every
geometric point). Separately, on global sections,

$$
\Gamma\bigl(Y,\mathcal H^0(Rs^{!}\Lambda_{\Aaf^1_Y}(1)[2])\bigr)
=\operatorname{Hom}\bigl(\Lambda_Y,Rs^{!}\Lambda_{\Aaf^1_Y}(1)[2]\bigr)
\cong H^2_{s(Y)}(\Aaf^1_Y,\Lambda(1)),
$$

a module, not a sheaf (for $Y=\Spec k\sqcup\Spec k$ the sheaf has rank one
on each component while the module is $\Lambda^2$). The global section
$\partial\kappa(t)\in H^2_{s(Y)}(\Aaf^1_Y,\Lambda(1))$ is the
*fundamental class (orientation)*

$$
\mathrm{pur}_s:\Lambda_Y\longrightarrow Rs^{!}\Lambda_{\Aaf^1_Y}(1)[2],
$$

the unique morphism whose stalk at every geometric point is the normalized
generator $1$ (sections of a sheaf are determined by their stalks).
