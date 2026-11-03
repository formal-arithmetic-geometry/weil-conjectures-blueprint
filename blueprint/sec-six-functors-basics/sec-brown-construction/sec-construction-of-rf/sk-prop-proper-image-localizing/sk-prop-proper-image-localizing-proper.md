+++
id = "det-proper-image-localizing-proper"
kind = "lemma"
title = "Proper direct image on the localizing categories"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.proper_image_localizing_proper"]
order = 2485
uses = ["det-proper-image-localizing-principle", "sk-thm-sfb-proper-base-change", "det-lem-proper-unbounded-window-ii", "sk-prop-ctf-finite-proper", "sk-prop-int-compactness", "sk-cor-ambient-ind-derived"]
+++
Let $\Lambda$ be admissible and $p\colon X\to Y$ proper. Suppose that $Rp_*$ maps $\Dctf(X,\Lambda)$ into
$\Dctf(Y,\Lambda)$ and preserves direct sums of objects of $\Loc(\Dctf(X,\Lambda))$. Then $Rp_*$ restricts to an
exact, sum-preserving functor $\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$. The hypotheses hold:

- for $\Lambda=E,\Qlb$, by [sk-thm-sfb-proper-base-change] and [det-lem-proper-unbounded-window-ii] (sums in
  $\Loc(\Dctf(X,\Lambda))\subset\Dic(X,\Lambda)$);
- for $\Lambda=A$ finite, by [sk-prop-ctf-finite-proper];
- for $\Lambda=\mathcal O_E$, by [sk-thm-sfb-proper-base-change] (preservation of $\Dctf=\Dbc$) and
  [sk-prop-int-compactness] (direct sums).
