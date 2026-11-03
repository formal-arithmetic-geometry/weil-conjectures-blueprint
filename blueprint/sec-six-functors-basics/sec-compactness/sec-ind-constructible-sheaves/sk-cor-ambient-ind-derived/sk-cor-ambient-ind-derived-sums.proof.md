+++
kind = "proof"
of = "det-ambient-ind-derived-sums"
+++
(1) Direct sums in $\D(X_{\mathrm{proét}},\Lambda)$ are computed by termwise direct sums of complexes,
because direct sums of sheaves of modules are exact (so the termwise sum preserves quasi-isomorphisms
and satisfies the universal property, Hom out of a sum being a product). Exactness of sums gives
$H^n(\bigoplus K_s)=\bigoplus H^n(K_s)$, and $\IndCons(X,\Lambda)$ is closed under direct sums by part
(2) of [sk-prop-ind-heart].

(2) $H^m(\tau_{\leq n}K)$ is $H^m(K)$ for $m\leq n$ and $0$ otherwise; similarly for $\tau_{\geq n}$.

(3) A bounded constructible complex has constructible, in particular ind-constructible, cohomology
sheaves. By (1) and [det-ambient-ind-derived-triangulated], $\Dic(X,\Lambda)$ is a triangulated
subcategory closed under direct sums, i.e. a localizing subcategory, and it contains $\Dbc(X,\Lambda)$.
The localizing closure $\Loc(\Dbc(X,\Lambda))$ is the smallest such subcategory
([sk-def-localizing-closure]), hence is contained in $\Dic(X,\Lambda)$.
