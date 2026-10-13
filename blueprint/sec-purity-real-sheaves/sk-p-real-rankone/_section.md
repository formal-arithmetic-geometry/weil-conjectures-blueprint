+++
id = "sk-p-real-rankone"
kind = "proposition"
title = "Purity of rank-one Weil sheaves"
order = 2961
uses = ["sk-d-real-jacobian", "sk-d-real-setup", "sk-d-real-weights", "sk-d-real-weil", "sk-def-av-jacobian", "sk-def-av-pic", "sk-i-real-compactification", "sk-i-real-sheaves", "sk-lem-finite", "sk-p-rankone", "sk-p-real-integral", "sk-p-real-operations", "sk-prop-hilbert90", "sk-prop-jacobian-descent", "sk-prop-sf-open-closed-triangle", "sk-thm-av-final", "sk-thm-derived-duality", "sk-thm-frobenius"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.finite_geometric_image", "AlgebraicGeometry.WeilGroup.IsLisse.isPunctuallyPure_of_finrank_eq_one"]
tags = ["sketch"]
+++
Let $L$ be a rank-one lisse Weil sheaf on a
smooth geometrically connected curve $U_0/\Fq$,
with character $\chi:W(U_0)\to E^\times$ under [sk-i-real-sheaves].
Its geometric image $\chi(\pi_1(U))$ is finite, so the rank-one
factorization of [sk-p-rankone] applies. Consequently $L$ is
punctually $\iota$-pure of weight
$w=2\log|\iota(c)|/\log q$, where $c=\chi(\gamma)$ for any degree-one
lift $\gamma$.
