+++
id = "lem-pur-vector-diagonal-class"
kind = "lemma"
title = "Diagonal class of a vector bundle"
order = 2077
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-vector-bundle-thom-class", "def-weil-derived-tensor", "thm-pur-localized-top-chern"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $\pi:E\to B$ be a vector bundle of constant rank $r$, and let

$$
\delta:E\times_BE\longrightarrow E,\qquad(v_1,v_2)\longmapsto v_2-v_1.
$$

The inverse image of the zero section under $\delta$ is the relative
diagonal $\Delta_\pi$. Pullback of the Thom class gives

$$
\operatorname{cl}_{\Delta_\pi}:=
\Delta_{\pi,*}\Lambda_E
\xrightarrow{\ \delta^*\operatorname{thom}(E)\ }
\Lambda_{E\times_BE}(r)[2r],
$$

the *diagonal class* of $\pi$.

## Proof

Start with the specified supported morphism $\operatorname{thom}(E)$ of [def-pur-vector-bundle-thom-class].
The zero scheme of the tautological section of the pullback of
$\pi^*E$ along $\delta$ is the preimage of $z(B)$:

$$
\delta^{-1}(z(B))=\{(v_1,v_2):v_2-v_1=0\}=\Delta_\pi,
$$

and this scheme-theoretic preimage is regular, so (L2) of
[thm-pur-localized-top-chern] applies: the pullback of the
localized class is the localized class of the pulled-back section,
which is the displayed morphism.
