+++
id = "theorem-pro-etale-refinements-weakly-etale--1"
kind = "theorem"
title = "The canonical refinement of a weakly étale algebra"
name_showing = false
order = 62001
aliases = ["bp-r014-1"]
lean = ["Algebra.WeaklyEtale.indEtale_faithfullyFlat_refinement"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-w-local-w-strictly-local"]
+++
Let $R\to B$ be a weakly étale map of commutative rings. Let $C$ be
the w-strict localization of $R$, with its canonical ideal $J\subset C$
cutting out the closed points of $\operatorname{Spec}(C)$. Thus $J$ is
the extension to $C$ of the ideal cutting out the closed points of the
w-localization of $R$. Put

$$
D'=C\otimes_R B,\qquad K=JD',
$$

and let $D$ be the w-localization of $D'$ along $K$. Then $B\to D$
is ind-étale and faithfully flat, and the composite $R\to D$ is
ind-étale.
