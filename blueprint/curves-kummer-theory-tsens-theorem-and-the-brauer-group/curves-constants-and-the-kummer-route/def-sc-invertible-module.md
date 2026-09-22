+++
id = "def-sc-invertible-module"
kind = "definition"
title = "Invertible modules and their duals"
order = 3407
lean = ["AlgebraicGeometry.Invertible", "AlgebraicGeometry.Invertible.dual"]
uses = ["def-sc-curves"]
+++
Let $C$ be a curve [def-sc-curves]. An *invertible
$\mathcal O_C$-module* is a quasi-coherent $\mathcal O_C$-module
$\mathcal L$ which is locally free of rank one for the Zariski topology
(equivalently: there is an $\mathcal O_C$-module $\mathcal L^{-1}$ with
$\mathcal L\otimes\mathcal L^{-1}\cong\mathcal O_C$). Its *dual* is
$$
 \mathcal L^{\vee}:=\mathcal{H}om_{\mathcal O_C}(\mathcal L,\mathcal O_C).
$$
