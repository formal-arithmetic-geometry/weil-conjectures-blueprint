+++
id = "lem-trf-weil-extension-functorial"
kind = "lemma"
title = "Functoriality of the Weil extension by zero"
order = 3939
uses = ["def-trf-strict-weil-complex", "def-trf-weil-extension-zero", "def-weil-extension-by-zero", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "lem-trf-open-square-exchange", "lem-trf-weil-extension-strict"]
+++
Let $j_0:X_0\hookrightarrow Y_0$ be an
open immersion of
separated finite-type schemes over $k_0$, with base change
$j:X\hookrightarrow Y$, and let $f:(K,\varphi)\to(K',\varphi')$ be
a morphism of strict Weil
complexes on $X$. Then the assignment $(K,\varphi)\mapsto(\bar K,\bar\varphi)$ of [def-trf-weil-extension-zero] is functorial:
the morphism $j_!f:j_!K\to j_!K'$ of
[def-weil-extension-by-zero] commutes with the strict Weil
structures, i.e. it is a morphism
$(\bar K,\bar\varphi)\to(\bar K',\bar\varphi')$ of strict Weil
complexes in the sense of [def-trf-strict-weil-complex].

## Proof

By [def-trf-strict-weil-complex] the morphism $f$ commutes with
the Weil structures, i.e. $\varphi\circ Lg_X^*f=f\circ\varphi'$.
Applying the functor $j_!$ of [def-weil-extension-by-zero] to
this identity and using the functoriality of $j_!$ gives
$j_!\varphi\circ j_!Lg_X^*f=j_!f\circ j_!\varphi'$. The comparison
isomorphisms $b_{g_Y}$ of [lem-trf-open-square-exchange] are
natural in the coefficient complex, so that
$j_!Lg_X^*f\circ b_{g_Y}=b_{g_Y}\circ Lg_Y^*j_!f$; substituting this
into the previous identity shows
$\bar\varphi\circ Lg_Y^*(j_!f)=j_!f\circ\bar\varphi'$, with
$\bar\varphi$ the Weil structure of
[def-trf-weil-extension-zero]; this, by the
definition of the morphisms of strict Weil complexes in
[def-trf-strict-weil-complex] for the strict Weil complexes of
[lem-trf-weil-extension-strict], is the assertion.
