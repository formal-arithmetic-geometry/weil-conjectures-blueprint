+++
id = "prop-weil-localized-tstructure"
kind = "theorem"
title = "The rational t-structure"
order = 1432
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-pbc-bounded-constructible-complete", "def-weil-pbc-rational-category", "def-weil-t-structure", "prop-weil-pbc-integral-tstructure", "thm-weil-pbc-integral-truncations"]
tags = ["latex:proposition"]
+++
Let $E/\Ql$ be finite and let $\varpi$ be a uniformizer of $\mathcal O_E$.
By [prop-weil-pbc-integral-tstructure] the standard t-structure restricts to
$\Dbc(T,\mathcal O_E)$ [def-weil-pbc-bounded-constructible-complete], and
the $\varpi$-power-torsion subcategory is stable under the truncation
functors; the truncations are the levelwise ones on the reduction tower
[thm-weil-pbc-integral-truncations], which is exactly the adic-model
condition of the standard t-structure (objectwise cohomological boundedness
alone is not a bounded t-structure on a derived-complete category, and the
levelwise definition shows the truncations to persist). Then the
subcategories
$$
  (\Dbc(T,E))^{\le0}:=
  \{K:K\cong L\text{ in }\Dbc(T,E),\ L\in(\Dbc(T,\mathcal O_E))^{\le0}\},
$$
$$
  (\Dbc(T,E))^{\ge0}:=
  \{K:K\cong L\text{ in }\Dbc(T,E),\ L\in(\Dbc(T,\mathcal O_E))^{\ge0}\},
$$
with the objects of $\Dbc(T,E)$ [def-weil-pbc-rational-category] identified
with those of $\Dbc(T,\mathcal O_E)$, form a bounded t-structure on
$\Dbc(T,E)$ for which the localization functor is t-exact; the truncation
functors are the levelwise canonical truncations on an integral
representative, and the heart is the essential image of the integral heart.
