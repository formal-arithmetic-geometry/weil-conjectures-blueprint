+++
id = "pur713-def-base-changed-compactification"
kind = "definition"
title = "Base change of a compactification"
lean = ["AlgebraicGeometry.Compactification.ofIsPullback"]
order = 3360
uses = ["sk-thm-sf-comp-composition"]
+++
Let $c=(j,p)$ be a compactification of $f$ (Definition “Chosen compactifications” (`pur456-pbc-chosen-compactification`, in [sk-thm-sf-comp-composition])); in the exchange maps below $c=c_f$. Write $X\xrightarrow{j}\overline X\xrightarrow{p}Y$. For the Cartesian square $\square$, put $\overline X'=\overline X\times_YY'$, with projections $\bar g:\overline X'\to\overline X$ and $p':\overline X'\to Y'$, and let $j':X'\hookrightarrow\overline X'$ be the morphism induced by $j$ and $\mathrm{id}_{Y'}$. Then $X'=X\times_{\overline X}\overline X'$, $jg'=\bar gj'$, $j'$ is an open immersion and $p'$ is proper, because open immersions and proper morphisms are stable under base change; and $p'j'=f'$. The base change of $c$ along $g$ is the compactification $c'=(j',p')$ of $f'$. Write $\square_p$ for the Cartesian square formed by $p$, $g$, $p'$ and $\bar g$.
