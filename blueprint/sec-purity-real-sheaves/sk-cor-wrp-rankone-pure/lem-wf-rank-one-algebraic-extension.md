+++
id = "lem-wf-rank-one-algebraic-extension"
kind = "lemma"
title = "Arithmetic monodromy after finite geometric image"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromyExtensionEquivProd", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromyExtensionHom_arithmeticMonodromyExtensionEquivProd_symm", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromyExtensionHom_arithmeticMonodromyExtensionEquivProd_symm_rep"]
order = 3834
uses = ["def-wf-arithmetic-monodromy-extension", "def-wf-geometric-monodromy-group"]
+++
Let $\chi:W(X_0)\to E^\times$ be a continuous rank-one Weil character,
assume that $A=\chi(\Pi)$ is finite, and let $s$ have degree one;
put $c=\chi(s)$. For the rank-one
representation $\rho=\chi$, one has

$$
H_{\mathrm{geom}}(\chi)=A,
\qquad
G_{\mathrm{arith}}(\chi)=A\times\mathbf Z,
\qquad
j_\chi(a,m)=ac^m.
$$

Here $j_\chi:G_{\mathrm{arith}}(\chi)\to\mathbf G_m$ is a regular
homomorphism on every finite-type component.
