+++
id = "lem-pc-higher-direct-image-derived-model"
kind = "lemma"
title = "A global derived model for higher direct images"
order = 781
lean = ["AlgebraicGeometry.Scheme.Modules.exists_derived_model_higherDirectImage", "AlgebraicGeometry.exists_isIso_canonicalModuleBaseChange_of_isFlatOver"]
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-derived-direct-image", "def-pc-derived-pullback", "lem-pc-relatively-flat-canonical-module-base-change"]
+++
Let $f:X\to T$ be a proper morphism which is locally of finite presentation
and let $\mathcal F$ be an $\mathcal O_X$-module of finite presentation
which is flat over $T$. Then there is an object $E$ of the derived category
$D(\mathcal O_T)$ ([def-pc-derived-category]) such that

- **(a)** $H^n(E)=0$ for all $n<0$;
- **(b)** $H^q(E)\cong R^qf_*\mathcal F$ for all $q\ge0$
  ([def-pc-derived-direct-image]);
- **(c)** for every cartesian square ([def-pc-base-change]) with
  $g:T'\to T$, $g':X'\to X$ and $f':X'\to T'$, the base-change map
  $Lg^*E\to Rf'_*(g'^*\mathcal F)$ is an isomorphism in $D(\mathcal O_{T'})$,
  where $Lg^*$ is the derived pullback of [def-pc-derived-pullback]; in
  particular $H^q(Lg^*E)\cong R^qf'_*(g'^*\mathcal F)$ for every $q\ge0$.
