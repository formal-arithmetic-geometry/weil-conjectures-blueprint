+++
id = "lem-exc-ambient-comparison-test"
kind = "lemma"
title = "The ambient comparison test"
order = 1895
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-site-comparison-morphism"]
+++
Use the ordinary derived
categories and the
comparison functors
$v_X=\nu_X^*$, $v_Y=\nu_Y^*$.
Suppose $F_{\mathrm{et}}\dashv G_{\mathrm{et}}$ and
$F_{\mathrm{proet}}\dashv G_{\mathrm{proet}}$ are adjunctions, and
$\alpha:F_{\mathrm{proet}}v_X\xrightarrow{\sim} v_YF_{\mathrm{et}}$ is given. For an object $K$ on the etale
side there is a canonical comparison

$$
\beta_K:v_XG_{\mathrm{et}}K\longrightarrow G_{\mathrm{proet}}v_YK.
$$

It is an isomorphism if and only if its cone $C_K$ satisfies
$\operatorname{Hom}(P,C_K[r])=0$ for every integer $r$ and every
member $P$ of a family detecting zero objects in the full source
pro-etale derived category.

## Proof

Use the counit $\epsilon$ of the etale adjunction to form

$$
F_{\mathrm{proet}}v_XG_{\mathrm{et}}K
\xrightarrow{\alpha}v_YF_{\mathrm{et}}G_{\mathrm{et}}K
\xrightarrow{v_Y\epsilon}v_YK.
$$

Its adjoint is $\beta_K$. The functors $v_X,v_Y$ here are
exactly those of [def-weil-pbc-site-comparison-morphism]; no
identification of right adjoints has been presumed. In the ordinary
derived category of [def-weil-pbc-derived-categories], a map is
an isomorphism exactly when its cone is zero. The stipulated detection
property says exactly that the displayed Hom vanishings detect this.
