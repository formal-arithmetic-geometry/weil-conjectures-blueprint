+++
id = "proposition-compatibility-purity-base-change--2"
kind = "proposition"
title = "Integral coefficients"
order = 797004
aliases = ["bp-r239-2"]
lean = []
uses = ["definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients"]
+++
This integral-coefficient identity is bypassed by the Lean route to the main
theorem; the supplied mainline does not prove this equality for the chosen
purity maps.

Let
$K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)$. Identify the sources by
$g'^{*}f^{*}\simeq(f')^{*}g^{*}$
and the targets by the exceptional base change map of
Definition [definition-exceptional-base-change-map]. Then

$$
g'^{*}\gamma_f(K)
=\gamma_{f'}(g^{*}K)
\quad\text{in }D^b_{\mathrm{ctf}}(X'_{\mathrm{pro}\acute{e}t},\mathcal O_E).
$$
