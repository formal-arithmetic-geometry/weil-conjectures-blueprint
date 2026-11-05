+++
id = "theorem-smooth-base-change-all-admissible--3"
kind = "theorem"
title = "Finite extension of $\\Ql$"
order = 700006
aliases = ["bp-r210-3"]
lean = []
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-pro-etale-base-change-map", "theorem-smooth-base-change-all-admissible--2"]
+++
The separate finite-extension smooth-base-change stage is bypassed by the
Lean route: it uses the scalar comparisons for
$\mathcal O_E\to E\to\overline{\mathbf Q}_\ell$ directly on an integral
model, without invoking this assertion as a separate theorem.

Under the hypotheses of (8.1), with $g$ smooth and the schemes separated
and of finite type over $k$ of characteristic $p>0$ different from $\ell$,
the corresponding consequence for a finite extension $E/\mathbf Q_\ell$
is that, for $K\in\Dbc(X,E)$, the map

$$
g^*_{E}Rf_{*,E}K\longrightarrow Rf'_{*,E}g'^*_{E}K
$$

is an isomorphism, with bounded constructibility read as in
[theorem-smooth-base-change-all-admissible--2].
