+++
id = "rem-pd-scope"
kind = "remark"
title = "What changed relative to the separably closed case"
order = 893
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

*Why a rational point over a finite extension is not enough.* One
cannot instead pass to a finite Galois extension $k_1/k$ over which
$C_0$ acquires a rational point and run the rigidified construction of
[thm-pc-picard-representable] over $k_1$: that construction verifies the
criterion of [det-thm-picard-criterion] with the twist lemma
[sk-thm-picard-twist], which needs the dense set of rational points of
a separably closed field. Over $\mathbf F_2$ the genus-$2$ curve
$y^2+y=x^5+x^3+1$ has a rational point $P$, but every degree-zero line
bundle on it is trivial (its only effective divisors of degree $2$ are
$2P$ and the fibres over $x=0$ and $x=1$, all linearly equivalent via
$x$ and $x+1$), so $\omega_C$ admits no twist $\omega_C\otimes\cL_0$ with
$h^0=1$ and $h^1=0$. Likewise, finitely many equations over $\bar k$
need not be defined over a separable extension of an imperfect $k$.
The spreading out of [thm-pd-spreading-out] is therefore done from $k_s$.
