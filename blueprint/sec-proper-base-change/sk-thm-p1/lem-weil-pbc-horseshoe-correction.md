+++
id = "lem-weil-pbc-horseshoe-correction"
kind = "lemma"
title = "The horseshoe defect correction preserves both row squares and the augmentation"
uses = ["def-sp-abelian"]
lean = ["CategoryTheory.InjectiveResolution.corrected_middle_map"]
order = 1829
+++
Let $\mathcal C$ be an abelian category [def-sp-abelian]. Let $X,Y,Z,X',Y',Z'$ be cochain complexes of $\mathcal C$ concentrated in degrees $\geq0$, let $U,U'$ be objects of $\mathcal C$, viewed as complexes $U[0],U'[0]$ concentrated in degree $0$, and let
$\alpha:X\to Y$, $\beta:Y\to Z$, $\alpha':X'\to Y'$, $\beta':Y'\to Z'$, $\varphi_A:X\to X'$, $\varphi_C:Z\to Z'$, $\chi,q:Y\to Y'$, $\varepsilon:U[0]\to Y$, $\varepsilon':U'[0]\to Y'$ and $b:U[0]\to U'[0]$ be morphisms of complexes. Suppose that (composition written diagrammatically, $fg$ meaning $f$ followed by $g$)
$$\alpha\chi=\varphi_A\alpha',\qquad \chi\beta'=\beta\varphi_C,\qquad \alpha q=0,\qquad q\beta'=0,\qquad \varepsilon\chi-\varepsilon q=b\varepsilon'.$$
Then there is a morphism of complexes $\varphi_B:Y\to Y'$ (namely $\varphi_B=\chi-q$) with
$$\varepsilon\varphi_B=b\varepsilon',\qquad \alpha\varphi_B=\varphi_A\alpha',\qquad \varphi_B\beta'=\beta\varphi_C.$$
