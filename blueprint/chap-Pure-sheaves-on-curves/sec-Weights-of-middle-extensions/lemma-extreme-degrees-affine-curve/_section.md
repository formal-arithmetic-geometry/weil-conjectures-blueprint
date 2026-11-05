+++
id = "lemma-extreme-degrees-affine-curve"
kind = "lemma"
title = "The extreme degrees on an affine curve"
order = 1186
lean = ["AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage", "AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage_zero", "AlgebraicGeometry.nonempty_equiv_compactlySupportedCohomology_directImage_two", "AlgebraicGeometry.isPureOfWeightOver_compactlySupportedCohomology_directImage_two"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open in a smooth
geometrically connected affine curve, let $F$ be lisse on $U_0$, and
put $V=F_{\bar\eta}$. Then $H_c^i(C,j_*F)=0$ for $i\ne1,2$, and there
is a canonical identification

$$
H_c^2(C,j_*F)=V_{\pi_1(U)}(-1).
$$

If $F$ is pure of weight $w$, the group in degree two, when nonzero,
is pure of weight $w+2$.
