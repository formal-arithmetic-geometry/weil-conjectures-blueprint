+++
kind = "proof"
of = "proposition-transitivity-trace-map"
order = 809
+++
Each [trace map](@definition-trace-map) is a map [$\gamma$](@theorem-smooth-purity-all-admissible-coefficients) followed by a counit. The maps [$\gamma$](@theorem-smooth-purity-all-admissible-coefficients)
compose by Proposition [proposition-compatibility-purity-composition],
and the counits compose because the counit of a composite adjunction is the
composite of the counits, so the only thing to arrange is the order of the
factors.
If we expand both traces using (9.25), naturality of [$\gamma_f$](@theorem-smooth-purity-all-admissible-coefficients)
lets us move the map $\gamma_g(K):g^{*}K(e)[2e]\to g^!K$
past the map [$\gamma_f$](@theorem-smooth-purity-all-admissible-coefficients) of the first trace. The composite then consists of
the two maps [$\gamma_f$](@theorem-smooth-purity-all-admissible-coefficients) and [$\gamma_g$](@theorem-smooth-purity-all-admissible-coefficients), which together are [$\gamma_{g\circ f}(K)$](@theorem-smooth-purity-all-admissible-coefficients) by
Proposition [proposition-compatibility-purity-composition], followed by

$$
Rg_!Rf_!f^!g^!K
\xrightarrow{\ Rg_!(\varepsilon_{f}(g^!K))\ }
Rg_!g^!K
\xrightarrow{\ \varepsilon_{g}(K)\ }K.
$$

This is the counit of the composite adjunction
$R(g\circ f)_!\dashv(g\circ f)^!$, so the composite is the map [$\gamma_{g\circ f}(K)$](@theorem-smooth-purity-all-admissible-coefficients)
followed by its counit, that is,
[$\operatorname{Tr}_{g\circ f}(K)$](@definition-trace-map).
