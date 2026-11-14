+++
id = "dag-lem-pe-roos-cone-calculus"
kind = "dag-lemma"
title = "Roos fibres preserve cones, shifts and levelwise quasi-isomorphisms"
name_showing = false
order = 210514
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "lem-pe-roos-cone-calculus"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.RoosConeCalculus.π", "CategoryTheory.RoosConeCalculus.v", "CategoryTheory.RoosConeCalculus.ucoord", "CategoryTheory.RoosConeCalculus.coneTarget", "CategoryTheory.RoosConeCalculus.coneSource", "CategoryTheory.RoosConeCalculus.ConeFormula", "CategoryTheory.RoosConeCalculus.ShiftFormula", "CategoryTheory.RoosConeCalculus.augmentation", "CategoryTheory.RoosConeCalculus.AugmentedSquare", "CategoryTheory.RoosConeCalculus.AugmentationNaturality", "CategoryTheory.RoosConeCalculus.ConeCompatibility", "CategoryTheory.RoosConeCalculus.ConeAugmentation", "CategoryTheory.RoosConeCalculus.ShiftAugmentation", "CategoryTheory.RoosConeCalculus.CoordinateCalculus", "CategoryTheory.RoosConeCalculus.DerivedRoos", "CategoryTheory.RoosConeCalculus.roos_cone_calculus"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $X$ be a scheme, $R$ a sheaf of rings on the pro-étale site $X_{\mathrm{pro\acute et}}$ [dag-def-weil-pbc-proetale-site], and $\mathcal A=\operatorname{Mod}(R)$ `def-weil-sheaf-of-modules-category`. Use cochain complexes and cones of `def-weil-abstract-derived-category`. For a strict inverse tower $N=(N_n,t_n)_{n\ge1}$ of cochain complexes of $\mathcal A$ `def-weil-inverse-system`, let $P(N)=\prod_nN_n$ be the termwise product `def-weil-category-product`, let $s_N=1-T_N$ with $\operatorname{pr}_nT_N=t_n\operatorname{pr}_{n+1}$, and set $H(N)=\operatorname{Cone}(s_N)[-1]$. In reordered coordinates,
$$H(N)^q=P(N)^q\oplus P(N)^{q-1},\qquad d(v,u)=(dv,-du-s_Nv).$$
On strict tower maps let $H$ act diagonally by the product map. This is an additive functor, it sends levelwise quasi-isomorphisms to quasi-isomorphisms, and its localized Roos triangle makes $QH(N)$ a derived limit of $(QN_n)_n$ in the sense of `def-weil-derived-limit`. For every strict tower map $f:N\to N'$ there is a natural chain isomorphism
$$H(\operatorname{Cone}(f))\xrightarrow{\sim}\operatorname{Cone}(H(f)),\qquad(b,a,b',a')\mapsto(b,b',a,-a'),$$
in source order $P(N')^q,P(N)^{q+1},P(N')^{q-1},P(N)^q$. It preserves the cone inclusion and boundary after the shift comparison. The coherent natural shift comparison $H(N[r])\xrightarrow{\sim}H(N)[r]$ is $(v,u)\mapsto(v,(-1)^r u)$. If $j_n:M\to N_n$ are compatible chain maps, $m\mapsto((j_n(m))_n,0)$ is a natural chain map $M\to H(N)$. The cone and shift comparisons carry such zero-second-coordinate augmentations to the induced cone and shifted augmentations whenever the levelwise augmentations do so.

(SHEAF DAG node `lem-pe-roos-cone-calculus`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: statement. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-category-product`, `def-weil-inverse-system`, `def-weil-sheaf-of-modules-category`, `def-weil-strict-roos-model`.
