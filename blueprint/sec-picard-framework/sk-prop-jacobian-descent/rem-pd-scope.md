+++
id = "rem-pd-scope"
kind = "remark"
title = "What changed relative to the separably closed case"
order = 897
uses = ["lem-pc-rational-hyp", "lem-pc-rational-points-dense", "thm-pc-picard-representable", "thm-pd-effective-descent", "thm-pd-geometric-pic0", "thm-pd-jacobian-general-field", "thm-pd-spreading-out", "thm-sc-jacobian-representability"]
+++
[thm-pd-jacobian-general-field] is the statement that
[rem-sc-jacobian-scope] of the Jacobian chapter declares to lie outside
the scope of that chapter. The route taken here is the descent route: the
theorem is proved over a separable closure by
[thm-pd-geometric-pic0] and then descended, so that neither
Grothendieck's existence theorem in the presence of a rational point nor a
choice of a base point enters. In particular the hypothesis that $k$ be
separably closed in [thm-pc-picard-representable] and in
[thm-sc-jacobian-representability] is used only to manufacture a
$k$-rational point, as the proof of [thm-pc-picard-representable]
records through [lem-pc-rational-points-dense] and
[lem-pc-rational-hyp]; over an arbitrary ground field the rational point
is unnecessary.
