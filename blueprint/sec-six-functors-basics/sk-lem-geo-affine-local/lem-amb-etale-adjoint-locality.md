+++
id = "lem-amb-etale-adjoint-locality"
kind = "lemma"
title = "Etale localization of the ambient adjoint"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp_leftDerivedUpperStar_of_etale"]
order = 2363
uses = ["def-amb-etale-compact-support", "def-nagata-compactifiable", "def-weil-pbc-derived-categories", "def-weil-scheme-morphism-properties", "lem-amb-etale-compact-comparisons", "thm-amb-etale-exceptional-adjoint"]
+++
For a separated etale morphism $u:U\to X$ of finite type,
$u_!$ is exact and is left adjoint to $u^*$ on the whole
ordinary derived categories. If $f$ and $fu$ are
compactifiable, there is a canonical isomorphism

$$
u^*f^\times K\cong(fu)^\times K.
$$
