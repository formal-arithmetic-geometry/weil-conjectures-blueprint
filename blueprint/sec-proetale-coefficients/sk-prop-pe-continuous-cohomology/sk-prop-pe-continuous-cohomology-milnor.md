+++
id = "det-pe-continuous-cohomology-milnor"
kind = "corollary"
title = "The Milnor sequence for continuous cohomology"
lean = ["DerivedCategory.shortExact_milnor_of_isHomotopyLimit", "CategoryTheory.Pretriangulated.IsHomotopyLimit.bijective_milnorMap"]
order = 1089
uses = ["det-pe-continuous-cohomology-limit", "det-pe-milnor-sequence"]
+++
In the situation of [det-pe-continuous-cohomology-limit], for every $q$ there is
a natural exact sequence

$$
0\to\varprojlim\nolimits^1_nH^{q-1}(X_{\Proet},F_n)\to H^q(X_{\Proet},F)
\to\varprojlim_nH^q(X_{\Proet},F_n)\to0 .
$$

If all the groups $H^{q-1}(X_{\Proet},F_n)$ are finite, the first term vanishes and
$H^q(X_{\Proet},F)\cong\varprojlim_nH^q(X_{\Proet},F_n)$.
