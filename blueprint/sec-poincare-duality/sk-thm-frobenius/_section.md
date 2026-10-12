+++
id = "sk-thm-frobenius"
kind = "theorem"
title = "Frobenius: equivariance, similitudine, reciprocity"
order = 2749
uses = ["sk-def-pairing", "sk-def-sf-orientation", "sk-def-weil", "sk-thm-derived-duality"]
tags = ["sketch"]
+++
In the setting of [sk-def-weil] ($X_0$ need not be proper),
for a strict Weil complex $K$ perfect over $\Lambda_X$:

**(a)** *Equivariance and similitude, at every coefficient stage.* At every
stage $\Lambda\in\{\AEn,\Oe,E,\Qlb\}$ the derived pairing $\beta_K$ of
[sk-def-pairing] is a morphism of Weil objects, so the induced degreewise
pairing satisfies
$\langle F_{c,K}x,F_{K^\vee(d)}y\rangle_i=\langle x,y\rangle_i$, and the
untwisted line-valued pairing satisfies

$$
\langle F_{c,K}x,F_{K^\vee}y\rangle_i^{\mathrm{untw}}
=q^d\langle x,y\rangle_i^{\mathrm{untw}}.
$$

These are identities between bilinear maps and use no nondegeneracy.

**(b)** *Reciprocity, at the field stages.* If moreover $\Lambda$ is a field
coefficient stage in the sense of [sk-thm-derived-duality] (in practice
$\Lambda\in\{E,\Qlb\}$), so that the degreewise pairings are perfect, then
$F_{K^\vee}$ is conjugate to $q^d(F_{c,K}^{-1})^{\mathsf t}$ on the
finite-dimensional space $H^{2d-i}(X,K^\vee)$, so the eigenvalues of $F$ on
$H^{2d-i}(X,K^\vee)$ are the $q^d/\alpha$ with the multiplicities of the
eigenvalues $\alpha$ on $H^i_c(X,K)$ (for proper $X$, $H^i_c=H^i$).

Clause (b) is false at the integral stage $\Lambda=\Oe$: for
$X_0=\Spec\Fq$, $d=0$, and the perfect complex
$K=[\Oe\xrightarrow{\varpi_E}\Oe]$ in degrees $-1,0$ with the identity
Weil datum, $H^0(K)=\Oe/\varpi_E$ while $H^0(K^\vee)=0$ and
$H^1(K^\vee)=\Oe/\varpi_E$; the degreewise form of the duality is not
perfect there ([sk-thm-sf-identification]), the missing information being
carried by an $\operatorname{Ext}^1$ term.
