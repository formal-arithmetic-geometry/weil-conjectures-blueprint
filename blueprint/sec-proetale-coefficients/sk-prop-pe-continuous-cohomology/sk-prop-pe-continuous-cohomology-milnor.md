+++
id = "det-pe-continuous-cohomology-milnor"
kind = "corollary"
title = "The Milnor sequence for continuous cohomology"
lean = ["DerivedCategory.shortExact_milnor_of_isHomotopyLimit", "CategoryTheory.Pretriangulated.IsHomotopyLimit.bijective_milnorMap", "AlgebraicGeometry.Scheme.ProEt.bijective_extLimitToLimit_of_isMittagLeffler"]
order = 1089
uses = ["det-pe-continuous-cohomology-limit", "det-pe-milnor-sequence"]
+++
In the situation of [det-pe-continuous-cohomology-limit], for every $q$ there is
a natural exact sequence

$$
0\to\varprojlim\nolimits^1_nH^{q-1}(X_{\Proet},F_n)\to H^q(X_{\Proet},F)
\to\varprojlim_nH^q(X_{\Proet},F_n)\to0 .
$$

If the system $(H^{q-1}(X_{\Proet},F_n))_n$ satisfies the Mittag-Leffler condition,
in particular if all these groups are finite, the first term vanishes and
$H^q(X_{\Proet},F)\cong\varprojlim_nH^q(X_{\Proet},F_n)$.
