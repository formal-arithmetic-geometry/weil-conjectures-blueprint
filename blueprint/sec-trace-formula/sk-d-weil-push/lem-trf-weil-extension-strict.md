+++
id = "lem-trf-weil-extension-strict"
kind = "lemma"
title = "The Weil extension by zero is a strict Weil complex"
order = 2506
uses = ["def-trf-strict-weil-complex", "def-trf-weil-extension-zero", "def-weil-extension-by-zero", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "lem-trf-frobenius-open-square", "lem-trf-open-ctf", "lem-trf-open-square-exchange"]
+++
Let $j_0:X_0\hookrightarrow Y_0$ be an
open immersion of
separated finite-type schemes over the finite field $k_0$, with
base change $j:X\hookrightarrow Y$, and let $(K,\varphi)$ be a
strict Weil complex on $X$.
Then the pair $(\bar K,\bar\varphi)=(j_!K,\bar\varphi)$ of
[def-trf-weil-extension-zero] is a strict Weil complex on $Y$ in
the sense of [def-trf-strict-weil-complex]: $\bar K=j_!K\in D^b_{ctf}(Y,A)$ and $\bar\varphi:Lg_Y^*\bar K\to\bar K$ is
an isomorphism.

## Proof

By [def-trf-strict-weil-complex] the complex $K$ lies in
$D^b_{ctf}(X,A)$ and $\varphi:Lg_X^*K\to K$ is an isomorphism.
Extension by zero preserves $D^b_{ctf}$ along the open immersion
$j$, by [lem-trf-open-ctf], applied to the extension-by-zero
functor of [def-weil-extension-by-zero]; hence
$\bar K=j_!K\in D^b_{ctf}(Y,A)$. By
[lem-trf-frobenius-open-square] the square relating $j$ to the
geometric Frobenius $g_Y$ is Cartesian, so
[lem-trf-open-square-exchange] supplies the isomorphism
$b_{g_Y}:Lg_Y^*j_!K\xrightarrow{\sim}j_!Lg_X^*K$; the second arrow
$j_!\varphi$ of the composite defining $\bar\varphi$ in
[def-trf-weil-extension-zero] is an isomorphism because
$\varphi$ is one and $j_!$ is a functor. A composite of two
isomorphisms is an isomorphism, so $\bar\varphi$ is an isomorphism
$Lg_Y^*\bar K\xrightarrow{\sim}\bar K$, as asserted.
