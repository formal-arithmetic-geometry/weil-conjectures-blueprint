+++
id = "det-pe-continuous-cohomology-milnor"
kind = "corollary"
title = "The Milnor sequence for continuous cohomology"
uses = ["det-pe-continuous-cohomology-limit", "sk-prop-pe-milnor"]
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
