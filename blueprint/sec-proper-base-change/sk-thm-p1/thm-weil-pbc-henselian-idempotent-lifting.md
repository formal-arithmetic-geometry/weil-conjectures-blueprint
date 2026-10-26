+++
id = "thm-weil-pbc-henselian-idempotent-lifting"
kind = "theorem"
title = "Idempotent lifting for the structure sheaf over a henselian pair"
lean = ["AlgebraicGeometry.Scheme.bijective_appTop_idempotent_of_henselianRing", "AlgebraicGeometry.Scheme.henselian_clopen_restriction"]
order = 1587
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions"]
+++
Let $(A,I)$ be a henselian pair [def-weil-pbc-henselian-terminology] and let
$Z\to\operatorname{Spec}A$ be proper [def-weil-pbc-scheme-conventions],
with closed fibre $Z_0=Z\times_AA/I$. Then every idempotent of
$H^0(Z_0,\mathcal O_{Z_0})$ lifts uniquely to an idempotent of $H^0(Z,\mathcal
O_Z)$; equivalently, restriction induces a bijection on idempotents, and the
open and closed subschemes of $Z_0$ are exactly the closed fibres of the open
and closed subschemes of $Z$.

